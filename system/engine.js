/* ==========================================================
   LIFE SYSTEM -- ENGINE
   Pure logic. No DOM, no storage, no side effects.

   ARCHITECTURE: the dated log is the ONLY stored truth.
   Level, XP, boss HP, streaks and attributes are all DERIVED
   on every load. That means a mis-logged day can be corrected
   and everything self-corrects, and the XP curve can be
   retuned later without losing history.

   HARDENING: zero && , zero || , zero non-ASCII.
   WordPress entity-encodes & (so && becomes &amp;&amp; and the
   script dies) and mangles non-ASCII in block JS.
   ========================================================== */

var SYS = (function () {

  /* ---------- CONFIG: everything tunable lives here ---------- */

  var CONFIG = {
    xpBase: 1000,        // XP to clear level 1
    xpMult: 1.15,        // each level costs 15 percent more
    maxLevel: 99,

    /* Fixed daily quest set. Repeated every day.
       attrs  = which attributes this trains
       damage = HP removed from the campaign boss */
    quests: [
      { id: "deep",   name: "Deep work",        detail: "One uninterrupted 90 minute block.", xp: 75,  attrs: ["FOC", "CRE"], damage: 60 },
      { id: "avoid",  name: "The avoided thing", detail: "20 minutes on what you are postponing.", xp: 100, attrs: ["WIL", "FOC"], damage: 120 },
      { id: "move",   name: "Move",             detail: "30 minutes of physical activity.", xp: 50,  attrs: ["STR"], damage: 30 },
      { id: "learn",  name: "Learn",            detail: "30 minutes on something that compounds.", xp: 50,  attrs: ["INT"], damage: 20 },
      { id: "reflect",name: "Log the day",      detail: "Write down what actually happened.", xp: 25,  attrs: ["INS"], damage: 20 }
    ],

    /* A long campaign. Not reset monthly. */
    boss: {
      id: "avoider",
      name: "The Avoider",
      maxHp: 12000,
      pattern: "You delay difficult actions until urgency forces movement.",
      weakness: "Immediate action, taken small."
    },

    attrs: [
      { key: "STR", name: "Strength",     detail: "Physical capability and energy." },
      { key: "INT", name: "Intellect",    detail: "Learning and reasoning." },
      { key: "FOC", name: "Focus",        detail: "Concentration and execution." },
      { key: "WIL", name: "Will",         detail: "Resilience and emotional control." },
      { key: "CRE", name: "Creation",     detail: "Ability to make and finish things." },
      { key: "FIN", name: "Finance",      detail: "Financial capability and leverage." },
      { key: "CHA", name: "Presence",     detail: "Communication and social presence." },
      { key: "INF", name: "Influence",    detail: "Reach and the weight of your word." },
      { key: "INS", name: "Insight",      detail: "Self-awareness and pattern recognition." }
    ],

    /* Attribute growth: every N completions of a quest training
       an attribute raises it by 1, capped. */
    attrPerPoint: 4,
    attrCap: 99,

    traits: [
      { id: "opened",    name: "Opened",      test: "days",   at: 1,   detail: "You logged a first day." },
      { id: "week",      name: "Consistent",  test: "streak", at: 7,   detail: "Seven consecutive days." },
      { id: "month",     name: "Relentless",  test: "streak", at: 30,  detail: "Thirty consecutive days." },
      { id: "finisher",  name: "Finisher",    test: "quest",  at: 25,  detail: "Twenty-five avoided things faced.", questId: "avoid" },
      { id: "deepworker",name: "Deep worker", test: "quest",  at: 50,  detail: "Fifty deep work blocks.", questId: "deep" },
      { id: "returned",  name: "Returned",    test: "recover",at: 1,   detail: "You came back after breaking a streak." }
    ]
  };

  /* ---------- date helpers (YYYY-MM-DD, no timezone maths) ---------- */

  function pad2(n) {
    if (n < 10) { return "0" + n; }
    return "" + n;
  }

  function todayKey(d) {
    var x = d;
    if (!x) { x = new Date(); }
    return x.getFullYear() + "-" + pad2(x.getMonth() + 1) + "-" + pad2(x.getDate());
  }

  function keyToUTC(key) {
    var p = key.split("-");
    return Date.UTC(parseInt(p[0], 10), parseInt(p[1], 10) - 1, parseInt(p[2], 10));
  }

  function daysBetween(aKey, bKey) {
    var ms = keyToUTC(bKey) - keyToUTC(aKey);
    return Math.round(ms / 86400000);
  }

  function shiftKey(key, deltaDays) {
    var t = keyToUTC(key) + deltaDays * 86400000;
    var d = new Date(t);
    return d.getUTCFullYear() + "-" + pad2(d.getUTCMonth() + 1) + "-" + pad2(d.getUTCDate());
  }

  /* ---------- levels ---------- */

  /* Cost of clearing a single level. */
  function costOfLevel(level) {
    return Math.round(CONFIG.xpBase * Math.pow(CONFIG.xpMult, level - 1));
  }

  /* Total XP needed to REACH a level (level 1 starts at 0). */
  function cumulativeToReach(level) {
    var total = 0;
    var i = 1;
    while (i < level) {
      total = total + costOfLevel(i);
      i = i + 1;
    }
    return total;
  }

  function levelFromXp(xp) {
    var level = 1;
    var spent = 0;
    var guard = 0;
    while (guard < CONFIG.maxLevel) {
      var cost = costOfLevel(level);
      if (spent + cost > xp) { break; }
      spent = spent + cost;
      level = level + 1;
      guard = guard + 1;
    }
    var into = xp - spent;
    var need = costOfLevel(level);
    var pct = 0;
    if (need > 0) { pct = into / need; }
    return { level: level, into: into, need: need, pct: pct };
  }

  /* ---------- log helpers ---------- */

  function questById(id) {
    var i = 0;
    while (i < CONFIG.quests.length) {
      if (CONFIG.quests[i].id === id) { return CONFIG.quests[i]; }
      i = i + 1;
    }
    return null;
  }

  /* Entries are { date: "YYYY-MM-DD", quests: [id,...], note: "" }.
     Duplicate quest ids within one day count once: the same block of
     deep work cannot be banked twice. */
  function cleanEntry(entry) {
    var seen = {};
    var out = [];
    var list = entry.quests;
    if (!list) { list = []; }
    var i = 0;
    while (i < list.length) {
      var id = list[i];
      var known = questById(id);
      if (known) {
        if (seen[id] !== true) {
          seen[id] = true;
          out.push(id);
        }
      }
      i = i + 1;
    }
    var note = "";
    if (entry.note) { note = entry.note; }
    return { date: entry.date, quests: out, note: note };
  }

  /* One entry per date, newest last. Later writes for the same date win. */
  function normalise(entries) {
    var byDate = {};
    var i = 0;
    while (i < entries.length) {
      var e = cleanEntry(entries[i]);
      if (e.date) { byDate[e.date] = e; }
      i = i + 1;
    }
    var keys = Object.keys(byDate).sort();
    var out = [];
    var j = 0;
    while (j < keys.length) {
      out.push(byDate[keys[j]]);
      j = j + 1;
    }
    return out;
  }

  /* ---------- totals ---------- */

  function totals(entries) {
    var xp = 0;
    var questCounts = {};
    var completions = 0;
    var activeDays = 0;
    var i = 0;
    while (i < entries.length) {
      var e = entries[i];
      if (e.quests.length > 0) { activeDays = activeDays + 1; }
      var j = 0;
      while (j < e.quests.length) {
        var q = questById(e.quests[j]);
        if (q) {
          xp = xp + q.xp;
          completions = completions + 1;
          if (!questCounts[q.id]) { questCounts[q.id] = 0; }
          questCounts[q.id] = questCounts[q.id] + 1;
        }
        j = j + 1;
      }
      i = i + 1;
    }
    return { xp: xp, questCounts: questCounts, completions: completions, activeDays: activeDays };
  }

  /* ---------- streaks ---------- */

  /* Current streak counts back from today. A gap of one day is a break.
     Logging nothing today does NOT break the streak until tomorrow,
     because the day is not over yet. */
  function streaks(entries, today) {
    var active = [];
    var i = 0;
    while (i < entries.length) {
      if (entries[i].quests.length > 0) { active.push(entries[i].date); }
      i = i + 1;
    }
    if (active.length === 0) { return { current: 0, longest: 0, lastActive: null, breaks: 0 }; }

    var longest = 1;
    var run = 1;
    var breaks = 0;
    var k = 1;
    while (k < active.length) {
      var gap = daysBetween(active[k - 1], active[k]);
      if (gap === 1) {
        run = run + 1;
      } else {
        breaks = breaks + 1;
        run = 1;
      }
      if (run > longest) { longest = run; }
      k = k + 1;
    }

    var last = active[active.length - 1];
    var sinceLast = daysBetween(last, today);
    var current = 0;
    if (sinceLast <= 1) {
      current = 1;
      var idx = active.length - 1;
      while (idx > 0) {
        if (daysBetween(active[idx - 1], active[idx]) !== 1) { break; }
        current = current + 1;
        idx = idx - 1;
      }
    }
    return { current: current, longest: longest, lastActive: last, breaks: breaks };
  }

  /* ---------- boss ---------- */

  function bossState(entries) {
    var dealt = 0;
    var todayDealt = 0;
    var lastDate = null;
    if (entries.length > 0) { lastDate = entries[entries.length - 1].date; }
    var i = 0;
    while (i < entries.length) {
      var e = entries[i];
      var dayDamage = 0;
      var j = 0;
      while (j < e.quests.length) {
        var q = questById(e.quests[j]);
        if (q) { dayDamage = dayDamage + q.damage; }
        j = j + 1;
      }
      dealt = dealt + dayDamage;
      i = i + 1;
    }
    var max = CONFIG.boss.maxHp;
    var hp = max - dealt;
    var defeated = false;
    if (hp <= 0) { hp = 0; defeated = true; }
    return {
      id: CONFIG.boss.id,
      name: CONFIG.boss.name,
      pattern: CONFIG.boss.pattern,
      weakness: CONFIG.boss.weakness,
      hp: hp, max: max, dealt: dealt, defeated: defeated,
      pct: hp / max, lastDate: lastDate, todayDealt: todayDealt
    };
  }

  function damageOnDate(entries, dateKey) {
    var i = 0;
    while (i < entries.length) {
      if (entries[i].date === dateKey) {
        var d = 0;
        var j = 0;
        while (j < entries[i].quests.length) {
          var q = questById(entries[i].quests[j]);
          if (q) { d = d + q.damage; }
          j = j + 1;
        }
        return d;
      }
      i = i + 1;
    }
    return 0;
  }

  /* ---------- attributes ---------- */

  function attributes(baseline, entries) {
    var out = {};
    var i = 0;
    while (i < CONFIG.attrs.length) {
      var key = CONFIG.attrs[i].key;
      var base = 10;
      if (baseline) {
        if (typeof baseline[key] === "number") { base = baseline[key]; }
      }
      out[key] = { base: base, earned: 0, value: base };
      i = i + 1;
    }
    var t = totals(entries);
    var ids = Object.keys(t.questCounts);
    var k = 0;
    while (k < ids.length) {
      var q = questById(ids[k]);
      if (q) {
        var gained = Math.floor(t.questCounts[ids[k]] / CONFIG.attrPerPoint);
        var a = 0;
        while (a < q.attrs.length) {
          var ak = q.attrs[a];
          if (out[ak]) { out[ak].earned = out[ak].earned + gained; }
          a = a + 1;
        }
      }
      k = k + 1;
    }
    var keys = Object.keys(out);
    var m = 0;
    while (m < keys.length) {
      var v = out[keys[m]].base + out[keys[m]].earned;
      if (v > CONFIG.attrCap) { v = CONFIG.attrCap; }
      out[keys[m]].value = v;
      m = m + 1;
    }
    return out;
  }

  function bottleneck(attrValues) {
    var keys = Object.keys(attrValues);
    if (keys.length === 0) { return null; }
    var lowKey = keys[0];
    var i = 1;
    while (i < keys.length) {
      if (attrValues[keys[i]].value < attrValues[lowKey].value) { lowKey = keys[i]; }
      i = i + 1;
    }
    var meta = null;
    var j = 0;
    while (j < CONFIG.attrs.length) {
      if (CONFIG.attrs[j].key === lowKey) { meta = CONFIG.attrs[j]; }
      j = j + 1;
    }
    return { key: lowKey, value: attrValues[lowKey].value, meta: meta };
  }

  /* ---------- traits ---------- */

  function traits(entries, today) {
    var t = totals(entries);
    var s = streaks(entries, today);
    var earned = [];
    var i = 0;
    while (i < CONFIG.traits.length) {
      var tr = CONFIG.traits[i];
      var got = false;
      if (tr.test === "days") {
        if (t.activeDays >= tr.at) { got = true; }
      }
      if (tr.test === "streak") {
        if (s.longest >= tr.at) { got = true; }
      }
      if (tr.test === "quest") {
        var c = t.questCounts[tr.questId];
        if (!c) { c = 0; }
        if (c >= tr.at) { got = true; }
      }
      if (tr.test === "recover") {
        if (s.breaks >= tr.at) {
          if (s.current >= 1) { got = true; }
        }
      }
      if (got) { earned.push(tr); }
      i = i + 1;
    }
    return earned;
  }

  /* ---------- the one call the interface makes ---------- */

  function derive(state, today) {
    var day = today;
    if (!day) { day = todayKey(); }
    var entries = normalise(state.entries);
    var t = totals(entries);
    var lv = levelFromXp(t.xp);
    var s = streaks(entries, day);
    var boss = bossState(entries);
    boss.todayDealt = damageOnDate(entries, day);
    var attrs = attributes(state.baseline, entries);
    return {
      today: day,
      entries: entries,
      xp: t.xp,
      completions: t.completions,
      activeDays: t.activeDays,
      questCounts: t.questCounts,
      level: lv.level,
      into: lv.into,
      need: lv.need,
      pct: lv.pct,
      streak: s,
      boss: boss,
      attrs: attrs,
      bottleneck: bottleneck(attrs),
      traits: traits(entries, day),
      todayEntry: entryFor(entries, day)
    };
  }

  function entryFor(entries, dateKey) {
    var i = 0;
    while (i < entries.length) {
      if (entries[i].date === dateKey) { return entries[i]; }
      i = i + 1;
    }
    return { date: dateKey, quests: [], note: "" };
  }

  /* ---------- writes: always return a NEW state ---------- */

  function toggleQuest(state, dateKey, questId) {
    var entries = normalise(state.entries);
    var cur = entryFor(entries, dateKey);
    var has = false;
    var i = 0;
    while (i < cur.quests.length) {
      if (cur.quests[i] === questId) { has = true; }
      i = i + 1;
    }
    var next = [];
    var j = 0;
    while (j < cur.quests.length) {
      if (cur.quests[j] !== questId) { next.push(cur.quests[j]); }
      j = j + 1;
    }
    if (!has) { next.push(questId); }
    var merged = [];
    var k = 0;
    var placed = false;
    while (k < entries.length) {
      if (entries[k].date === dateKey) {
        merged.push({ date: dateKey, quests: next, note: cur.note });
        placed = true;
      } else {
        merged.push(entries[k]);
      }
      k = k + 1;
    }
    if (!placed) { merged.push({ date: dateKey, quests: next, note: "" }); }
    return { baseline: state.baseline, entries: normalise(merged) };
  }

  function setNote(state, dateKey, note) {
    var entries = normalise(state.entries);
    var cur = entryFor(entries, dateKey);
    var merged = [];
    var k = 0;
    var placed = false;
    while (k < entries.length) {
      if (entries[k].date === dateKey) {
        merged.push({ date: dateKey, quests: cur.quests, note: note });
        placed = true;
      } else {
        merged.push(entries[k]);
      }
      k = k + 1;
    }
    if (!placed) { merged.push({ date: dateKey, quests: [], note: note }); }
    return { baseline: state.baseline, entries: normalise(merged) };
  }

  return {
    CONFIG: CONFIG,
    todayKey: todayKey,
    shiftKey: shiftKey,
    daysBetween: daysBetween,
    costOfLevel: costOfLevel,
    cumulativeToReach: cumulativeToReach,
    levelFromXp: levelFromXp,
    normalise: normalise,
    totals: totals,
    streaks: streaks,
    bossState: bossState,
    attributes: attributes,
    bottleneck: bottleneck,
    traits: traits,
    derive: derive,
    entryFor: entryFor,
    toggleQuest: toggleQuest,
    setNote: setNote,
    questById: questById
  };
})();

if (typeof module !== "undefined") { module.exports = SYS; }
