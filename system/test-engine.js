/* Engine tests. These assert ARITHMETIC and BEHAVIOUR, not just that
   the code runs. A test that only checks "did not throw" tests almost
   nothing, which is how a render bug shipped on the sister site. */

var SYS = require("./engine.js");

var pass = 0;
var fail = 0;

function ok(label, cond, got) {
  if (cond) { pass = pass + 1; return; }
  fail = fail + 1;
  console.log("  FAIL  " + label + "   got: " + JSON.stringify(got));
}

function eq(label, a, b) { ok(label + " (" + a + " === " + b + ")", a === b, a); }

function st(entries, baseline) {
  var b = baseline;
  if (!b) { b = null; }
  return { baseline: b, entries: entries };
}

/* ---------- dates ---------- */
eq("shiftKey forward", SYS.shiftKey("2026-09-12", 1), "2026-09-13");
eq("shiftKey across month", SYS.shiftKey("2026-09-30", 1), "2026-10-01");
eq("shiftKey across year", SYS.shiftKey("2026-12-31", 1), "2027-01-01");
eq("shiftKey backward", SYS.shiftKey("2026-03-01", -1), "2026-02-28");
eq("daysBetween", SYS.daysBetween("2026-09-01", "2026-09-11"), 10);
eq("daysBetween across DST boundary", SYS.daysBetween("2026-10-20", "2026-11-20"), 31);

/* ---------- level curve ---------- */
eq("level 1 costs base", SYS.costOfLevel(1), 1000);
eq("level 2 costs 15pc more", SYS.costOfLevel(2), 1150);
eq("level 3 compounds", SYS.costOfLevel(3), 1322);
eq("cumulative to reach 1 is zero", SYS.cumulativeToReach(1), 0);
eq("cumulative to reach 3", SYS.cumulativeToReach(3), 2150);

var l0 = SYS.levelFromXp(0);
eq("zero xp is level 1", l0.level, 1);
eq("zero xp into 0", l0.into, 0);
var l1 = SYS.levelFromXp(999);
eq("999 xp still level 1", l1.level, 1);
var l2 = SYS.levelFromXp(1000);
eq("1000 xp reaches level 2", l2.level, 2);
eq("1000 xp resets progress into level", l2.into, 0);
var l3 = SYS.levelFromXp(2149);
eq("2149 xp still level 2", l3.level, 2);
var l4 = SYS.levelFromXp(2150);
eq("2150 xp reaches level 3", l4.level, 3);
ok("levels get harder", SYS.costOfLevel(10) > SYS.costOfLevel(9), SYS.costOfLevel(10));
ok("pct is a fraction", SYS.levelFromXp(1575).pct > 0.49, SYS.levelFromXp(1575).pct);
ok("pct never exceeds 1", SYS.levelFromXp(123456).pct <= 1, SYS.levelFromXp(123456).pct);

/* ---------- totals and dedupe ---------- */
var t1 = SYS.totals(SYS.normalise([{ date: "2026-09-10", quests: ["deep", "move"] }]));
eq("xp sums quests", t1.xp, 125);
eq("completions counted", t1.completions, 2);

var t2 = SYS.totals(SYS.normalise([{ date: "2026-09-10", quests: ["deep", "deep", "deep"] }]));
eq("same quest twice in a day counts once", t2.xp, 75);

var t3 = SYS.totals(SYS.normalise([{ date: "2026-09-10", quests: ["nonsense"] }]));
eq("unknown quest id is dropped", t3.xp, 0);

var dupe = SYS.normalise([
  { date: "2026-09-10", quests: ["deep"] },
  { date: "2026-09-10", quests: ["move", "learn"] }
]);
eq("one entry per date", dupe.length, 1);
eq("later write for a date wins", SYS.totals(dupe).xp, 100);

var unsorted = SYS.normalise([
  { date: "2026-09-12", quests: ["move"] },
  { date: "2026-09-01", quests: ["move"] }
]);
eq("entries sort by date", unsorted[0].date, "2026-09-01");

/* ---------- streaks ---------- */
function days(list) {
  var out = [];
  var i = 0;
  while (i < list.length) { out.push({ date: list[i], quests: ["move"] }); i = i + 1; }
  return SYS.normalise(out);
}

var s0 = SYS.streaks([], "2026-09-12");
eq("empty log has no streak", s0.current, 0);

var s1 = SYS.streaks(days(["2026-09-10", "2026-09-11", "2026-09-12"]), "2026-09-12");
eq("three in a row, logged today", s1.current, 3);
eq("longest matches", s1.longest, 3);

var s2 = SYS.streaks(days(["2026-09-10", "2026-09-11"]), "2026-09-12");
eq("not logged yet today, day not over, streak holds", s2.current, 2);

var s3 = SYS.streaks(days(["2026-09-09", "2026-09-10"]), "2026-09-12");
eq("missed a full day, streak broken", s3.current, 0);

var s4 = SYS.streaks(days(["2026-09-01", "2026-09-02", "2026-09-03", "2026-09-08", "2026-09-09"]), "2026-09-09");
eq("longest survives a later shorter run", s4.longest, 3);
eq("current is the recent run", s4.current, 2);
eq("one break counted", s4.breaks, 1);

var s5 = SYS.streaks([{ date: "2026-09-11", quests: [] }, { date: "2026-09-12", quests: ["move"] }], "2026-09-12");
eq("a day with zero quests is not an active day", s5.current, 1);

/* ---------- boss ---------- */
var b0 = SYS.bossState([]);
eq("boss starts at full hp", b0.hp, 12000);
eq("boss not defeated at start", b0.defeated, false);

var b1 = SYS.bossState(SYS.normalise([{ date: "2026-09-10", quests: ["avoid"] }]));
eq("avoid quest deals 120", b1.dealt, 120);
eq("boss hp drops", b1.hp, 11880);

var allQuests = ["deep", "avoid", "move", "learn", "reflect"];
var perfectDay = 60 + 120 + 30 + 20 + 20;
eq("a perfect day deals 250", SYS.bossState(SYS.normalise([{ date: "2026-09-10", quests: allQuests }])).dealt, perfectDay);

var manyDays = [];
var d = "2026-01-01";
var n = 0;
while (n < 40) { manyDays.push({ date: d, quests: allQuests }); d = SYS.shiftKey(d, 1); n = n + 1; }
var bBig = SYS.bossState(SYS.normalise(manyDays));
eq("hp floors at zero, never negative", SYS.bossState(SYS.normalise(manyDays.concat(manyDays.map(function(e){return {date:SYS.shiftKey(e.date,60),quests:e.quests};})))).hp, 0);
eq("defeated after enough damage", SYS.bossState(SYS.normalise(manyDays.concat(manyDays.map(function(e){return {date:SYS.shiftKey(e.date,60),quests:e.quests};})))).defeated, true);
ok("campaign is long: 40 perfect days do not finish it",
   SYS.bossState(SYS.normalise(manyDays)).defeated === false,
   SYS.bossState(SYS.normalise(manyDays)).hp);

/* ---------- attributes ---------- */
var a0 = SYS.attributes(null, []);
eq("attributes default to 10", a0.STR.value, 10);
var a1 = SYS.attributes({ STR: 48, FOC: 39 }, []);
eq("baseline respected", a1.STR.value, 48);
eq("unset baseline still defaults", a1.INT.value, 10);

var fourMoves = SYS.normalise([
  { date: "2026-09-01", quests: ["move"] }, { date: "2026-09-02", quests: ["move"] },
  { date: "2026-09-03", quests: ["move"] }, { date: "2026-09-04", quests: ["move"] }
]);
eq("4 completions raise the attribute by 1", SYS.attributes({ STR: 20 }, fourMoves).STR.value, 21);
eq("3 completions raise nothing", SYS.attributes({ STR: 20 }, fourMoves.slice(0, 3)).STR.value, 20);
eq("attribute caps at 99", SYS.attributes({ STR: 99 }, fourMoves).STR.value, 99);

var bn = SYS.bottleneck(SYS.attributes({ STR: 50, INT: 50, FOC: 12, WIL: 50, CRE: 50, FIN: 50, CHA: 50, INF: 50, INS: 50 }, []));
eq("bottleneck finds the lowest attribute", bn.key, "FOC");

/* ---------- traits ---------- */
var tr0 = SYS.traits([], "2026-09-12");
eq("no traits on an empty log", tr0.length, 0);
var tr1 = SYS.traits(days(["2026-09-12"]), "2026-09-12");
ok("first day unlocks Opened", tr1.length >= 1, tr1.map(function (x) { return x.id; }));

var weekDays = [];
var wd = "2026-09-06";
var w = 0;
while (w < 7) { weekDays.push({ date: wd, quests: ["move"] }); wd = SYS.shiftKey(wd, 1); w = w + 1; }
var tr2 = SYS.traits(SYS.normalise(weekDays), "2026-09-12").map(function (x) { return x.id; });
ok("seven days unlocks Consistent", tr2.indexOf("week") >= 0, tr2);

var recov = SYS.traits(days(["2026-09-01", "2026-09-05"]), "2026-09-05").map(function (x) { return x.id; });
ok("returning after a break unlocks Returned", recov.indexOf("returned") >= 0, recov);

/* ---------- writes are immutable and correct ---------- */
var base = st([{ date: "2026-09-12", quests: ["deep"] }]);
var after = SYS.toggleQuest(base, "2026-09-12", "move");
eq("toggle adds", SYS.totals(after.entries).xp, 125);
eq("original state untouched", SYS.totals(SYS.normalise(base.entries)).xp, 75);
var off = SYS.toggleQuest(after, "2026-09-12", "move");
eq("toggle removes", SYS.totals(off.entries).xp, 75);
var newDay = SYS.toggleQuest(base, "2026-09-13", "learn");
eq("toggle creates a missing day", SYS.totals(newDay.entries).xp, 125);

var noted = SYS.setNote(base, "2026-09-12", "hard day");
eq("note saved", SYS.entryFor(noted.entries, "2026-09-12").note, "hard day");
eq("note does not disturb quests", SYS.entryFor(noted.entries, "2026-09-12").quests.length, 1);
var notedNew = SYS.setNote(base, "2026-09-20", "future");
eq("note creates a missing day", SYS.entryFor(notedNew.entries, "2026-09-20").note, "future");
eq("note-only day has no quests", SYS.entryFor(notedNew.entries, "2026-09-20").quests.length, 0);

/* ---------- the key architectural promise ---------- */
var corrected = SYS.toggleQuest(st([
  { date: "2026-09-10", quests: ["deep", "avoid"] },
  { date: "2026-09-11", quests: ["deep"] }
]), "2026-09-10", "avoid");
eq("correcting a past day recomputes xp", SYS.totals(corrected.entries).xp, 150);
eq("correcting a past day recomputes boss hp", SYS.bossState(corrected.entries).hp, 12000 - 120);

/* ---------- derive: the single call the UI makes ---------- */
var dv = SYS.derive(st([
  { date: "2026-09-11", quests: ["deep", "avoid", "move"] },
  { date: "2026-09-12", quests: ["deep"] }
], { FOC: 30 }), "2026-09-12");
eq("derive xp", dv.xp, 300);
eq("derive level", dv.level, 1);
eq("derive streak", dv.streak.current, 2);
eq("derive boss hp", dv.boss.hp, 12000 - (60 + 120 + 30 + 60));
eq("derive today damage only", dv.boss.todayDealt, 60);
eq("derive today entry", dv.todayEntry.quests.length, 1);
ok("derive bottleneck present", dv.bottleneck !== null, dv.bottleneck);

var empty = SYS.derive(st([]), "2026-09-12");
eq("empty log derives level 1", empty.level, 1);
eq("empty log derives 0 xp", empty.xp, 0);
eq("empty log has full boss", empty.boss.hp, 12000);
eq("empty log today entry is blank", empty.todayEntry.quests.length, 0);

/* ---------- hardening ---------- */
var src = require("fs").readFileSync(__dirname + "/engine.js", "utf8");
var code = src.replace(/\/\*[\s\S]*?\*\//g, "").replace(/\/\/[^\n]*/g, "");
eq("zero && in engine", code.indexOf("&&"), -1);
eq("zero || in engine", code.indexOf("||"), -1);
var nonAscii = [];
var ci = 0;
while (ci < src.length) {
  if (src.charCodeAt(ci) > 127) { nonAscii.push(src.charAt(ci)); }
  ci = ci + 1;
}
eq("zero non-ASCII in engine", nonAscii.length, 0);

console.log("\n" + pass + " passed, " + fail + " failed");
if (fail > 0) { process.exit(1); }
