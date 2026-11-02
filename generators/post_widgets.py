"""post_widgets.py :: CSS and runtime for postkit_interactive components.

Installed into 01-sidebar.html by install-post-widgets.py, between markers, so
every page carries them once. House rules for the JS: no && or ||, ASCII only,
addEventListener only, everything wrapped in try/catch where storage or the
clipboard is touched.
"""

CSS = r"""
  /* ===================== POST WIDGETS (postkit_interactive) ===================== */
  .yt-kt{ margin:28px 0 36px; padding:20px 22px; border:1px solid var(--yt-line); border-left:3px solid var(--yt-text); border-radius:10px; background:var(--yt-surface); }
  .yt-kt__h{ font-family:'JetBrains Mono',ui-monospace,monospace; font-size:11px; letter-spacing:.08em; text-transform:uppercase; color:var(--yt-text-2); margin-bottom:10px; }
  .yt-post__body .yt-kt ul{ margin:0; padding-left:20px; }
  .yt-post__body .yt-kt li{ font-size:16px; margin:0 0 8px; }
  .yt-post__body .yt-kt li:last-child{ margin-bottom:0; }

  .yt-cl{ margin:28px 0; padding:16px 18px; border:1px solid var(--yt-line); border-radius:10px; background:var(--yt-surface); }
  .yt-cl__k{ display:inline-block; font-family:'JetBrains Mono',ui-monospace,monospace; font-size:10.5px; letter-spacing:.08em; text-transform:uppercase; padding:3px 8px; border-radius:4px; margin-bottom:8px; background:var(--yt-active-bg); color:var(--yt-text); }
  .yt-cl--warn .yt-cl__k{ background:rgba(234,179,8,.18); }
  .yt-cl--tip .yt-cl__k{ background:rgba(22,163,74,.14); }
  .yt-cl--example .yt-cl__k{ background:rgba(59,130,246,.14); }
  .yt-cl--definition .yt-cl__k{ background:rgba(139,92,246,.15); }
  .yt-cl--template{ border-style:dashed; }
  .yt-cl--template .yt-cl__k{ background:rgba(20,184,166,.15); }
  .yt-cl--note .yt-cl__k{ background:var(--yt-active-bg); }
  .yt-calc, .yt-check, .yt-dec, .yt-tabs{ position:relative; }
  .yt-cl__t{ font-weight:620; font-size:16px; color:var(--yt-text); margin-bottom:6px; }
  .yt-cl__b{ font-size:15.5px; line-height:1.65; color:var(--yt-text); }
  .yt-cl__b p{ font-size:15.5px !important; margin:0 0 10px !important; }
  .yt-cl__b p:last-child{ margin-bottom:0 !important; }
  .yt-cl__b ul, .yt-cl__b ol{ margin:6px 0 0 !important; }
  .yt-cl__b li{ font-size:15.5px !important; margin-bottom:6px !important; }

  .yt-calc__intro{ font-size:15px !important; color:var(--yt-text-2) !important; margin:0 0 16px !important; }
  .yt-calc__ins{ display:grid; grid-template-columns:repeat(auto-fit, minmax(min(190px, 100%), 1fr)); gap:12px 16px; margin-bottom:18px; }
  .yt-calc__in{ display:flex; flex-direction:column; gap:6px; font-size:13px; color:var(--yt-text-2); }
  .yt-calc__lbl{ font-size:13px; line-height:1.35; color:var(--yt-text-2); }
  .yt-calc__field{ display:flex; align-items:center; gap:8px; }
  .yt-calc__ctl{ appearance:none; -webkit-appearance:none; width:100%; min-width:0; min-height:40px; padding:8px 10px; font-size:16px; font-family:'JetBrains Mono',ui-monospace,monospace; color:var(--yt-text); background:var(--yt-field-bg, var(--yt-bg)); border:1px solid var(--yt-field-border, var(--yt-line)); border-radius:8px; }
  select.yt-calc__ctl{ font-family:inherit; }
  .yt-calc__ctl:focus-visible{ outline:2px solid var(--yt-text); outline-offset:2px; }
  .yt-calc__unit{ font-size:12px; color:var(--yt-text-2); white-space:nowrap; }
  .yt-calc__outs{ display:grid; grid-template-columns:repeat(auto-fit, minmax(min(200px, 100%), 1fr)); gap:10px; padding-top:16px; border-top:1px solid var(--yt-line); }
  .yt-calc__out{ display:flex; flex-direction:column; gap:3px; padding:12px 14px; border-radius:8px; background:var(--yt-bg); border:1px solid var(--yt-line); }
  .yt-calc__out--big{ border-color:var(--yt-text); }
  .yt-calc__olbl{ font-size:12.5px; color:var(--yt-text-2); }
  .yt-calc__out output{ font-family:'JetBrains Mono',ui-monospace,monospace; font-size:20px; font-weight:600; color:var(--yt-text); font-variant-numeric:tabular-nums; overflow-wrap:anywhere; }
  .yt-calc__out--big output{ font-size:24px; }
  .yt-calc__hint{ font-size:12px; color:var(--yt-text-2); line-height:1.45; }
  @media (max-width:640px){ .yt-calc__ctl{ font-size:16px; } }

  .yt-check__grp{ border:0; margin:0 0 14px; padding:0; min-width:0; }
  .yt-check__grp legend{ font-weight:620; font-size:15px; color:var(--yt-text); margin-bottom:8px; padding:0; }
  .yt-check__item{ display:grid; grid-template-columns:auto minmax(0,1fr); gap:10px; align-items:start; padding:9px 4px; border-top:1px solid var(--yt-line); font-size:15.5px; line-height:1.55; color:var(--yt-text); cursor:pointer; }
  .yt-check__item input{ width:18px; height:18px; margin:3px 0 0; accent-color:var(--yt-text); }
  .yt-check__item input:checked + span{ color:var(--yt-text-2); text-decoration:line-through; text-decoration-color:var(--yt-fill-3, #9ca3af); }
  .yt-check__bar{ display:flex; align-items:center; gap:12px; margin-bottom:16px; }
  .yt-check__bar[hidden], .yt-check__verdict[hidden], .yt-check__actions[hidden]{ display:none; }
  .yt-check__count{ font-family:'JetBrains Mono',ui-monospace,monospace; font-size:12.5px; color:var(--yt-text); white-space:nowrap; }
  .yt-check__track{ flex:1; height:6px; border-radius:3px; background:var(--yt-active-bg); overflow:hidden; }
  .yt-check__fill{ display:block; height:100%; width:0; background:var(--yt-text); transition:width .2s ease; }
  .yt-post__body .yt-check__verdict{ font-size:15px; margin:6px 0 12px; padding:10px 12px; border-radius:8px; background:var(--yt-bg); border:1px solid var(--yt-line); }
  .yt-check__actions{ display:flex; flex-wrap:wrap; gap:8px; }
  .yt-check__btn, .yt-tabs__tab, .yt-sortbtn{ appearance:none; font:inherit; cursor:pointer; }
  .yt-check__btn{ font-family:'JetBrains Mono',ui-monospace,monospace !important; font-size:12px !important; padding:8px 12px !important; min-height:32px; border-radius:6px; border:1px solid var(--yt-line) !important; background:var(--yt-bg) !important; color:var(--yt-text) !important; text-transform:none !important; letter-spacing:0 !important; }

  .yt-tabs__list{ display:flex; flex-wrap:wrap; gap:6px; margin-bottom:16px; }
  .yt-tabs__list[hidden]{ display:none; }
  .yt-tabs__tab{ font-size:13.5px !important; padding:8px 14px !important; min-height:34px; border-radius:8px; border:1px solid var(--yt-line) !important; background:var(--yt-bg) !important; color:var(--yt-text-2) !important; text-transform:none !important; letter-spacing:0 !important; }
  .yt-tabs__tab[aria-selected="true"]{ background:var(--yt-text) !important; color:var(--yt-bg) !important; border-color:var(--yt-text) !important; }
  .yt-tabs__panel{ margin:0 0 18px; }
  .yt-tabs__panel:last-of-type{ margin-bottom:0; }
  .yt-post__body h3.yt-tabs__h{ margin:0 0 10px; font-size:16px; color:var(--yt-text); }
  .yt-js .yt-tabs__h{ position:absolute !important; width:1px; height:1px; overflow:hidden; clip:rect(0 0 0 0); white-space:nowrap; }
  .yt-tabs__panel p, .yt-tabs__panel li{ font-size:15.5px !important; }

  .yt-dec__q{ font-weight:620; font-size:15.5px; color:var(--yt-text); margin:4px 0 10px; }
  .yt-dec__opt{ border:1px solid var(--yt-line); border-radius:8px; margin:0 0 8px; background:var(--yt-bg); }
  .yt-dec__opt > summary{ list-style:none; cursor:pointer; padding:10px 14px; font-size:15px; color:var(--yt-text); display:flex; gap:10px; align-items:center; min-height:24px; }
  .yt-dec__opt > summary::-webkit-details-marker{ display:none; }
  .yt-dec__opt > summary::before{ content:"\2192"; font-family:'JetBrains Mono',ui-monospace,monospace; color:var(--yt-text-2); transition:transform .15s ease; }
  .yt-dec__opt[open] > summary::before{ transform:rotate(90deg); }
  .yt-dec__opt[open] > summary{ border-bottom:1px solid var(--yt-line); font-weight:600; }
  .yt-dec__opt > .yt-dec__q, .yt-dec__opt > .yt-dec__opt, .yt-dec__opt > .yt-dec__out{ margin-left:14px; margin-right:14px; }
  .yt-dec__opt > .yt-dec__q{ margin-top:12px; }
  .yt-dec__opt > .yt-dec__opt:last-child, .yt-dec__opt > .yt-dec__out{ margin-bottom:12px; }
  .yt-dec__out{ font-size:15px; line-height:1.6; color:var(--yt-text); padding:12px 14px; border-left:3px solid var(--yt-text); background:var(--yt-surface); border-radius:0 8px 8px 0; margin-top:12px; }

  .yt-cmp{ display:grid; grid-template-columns:repeat(auto-fit, minmax(min(220px, 100%), 1fr)); gap:12px; }
  .yt-cmp__col{ border:1px solid var(--yt-line); border-radius:10px; padding:14px 16px; background:var(--yt-bg); }
  .yt-cmp__t{ font-weight:640; font-size:16px; color:var(--yt-text); margin-bottom:8px; }
  .yt-cmp__k{ font-family:'JetBrains Mono',ui-monospace,monospace; font-size:10.5px; letter-spacing:.08em; text-transform:uppercase; color:var(--yt-text-2); margin:10px 0 4px; }
  .yt-post__body .yt-cmp ul{ margin:0; padding-left:18px; }
  .yt-post__body .yt-cmp li{ font-size:14.5px; margin:0 0 5px; }
  .yt-post__body .yt-cmp__pro li::marker{ color:#16a34a; }
  .yt-post__body .yt-cmp__con li::marker{ color:#d97706; }
  .yt-cmp__v{ margin-top:10px; padding-top:10px; border-top:1px solid var(--yt-line); font-size:14px; color:var(--yt-text); font-weight:560; }

  .yt-post__body .yt-flow{ list-style:none; margin:0; padding:0; display:grid; grid-template-columns:repeat(auto-fit, minmax(min(150px, 100%), 1fr)); gap:10px; counter-reset:none; }
  .yt-post__body .yt-flow__s{ position:relative; margin:0; padding:12px 14px; border:1px solid var(--yt-line); border-radius:10px; background:var(--yt-bg); display:flex; flex-direction:column; gap:4px; }
  .yt-flow__n{ font-family:'JetBrains Mono',ui-monospace,monospace; font-size:11px; color:var(--yt-text-2); }
  .yt-flow__t{ font-weight:620; font-size:15px; color:var(--yt-text); }
  .yt-flow__x{ font-size:13.5px; line-height:1.5; color:var(--yt-text-2); }

  .yt-tfilter{ display:flex; align-items:center; gap:10px; margin:0 0 12px; flex-wrap:wrap; }
  .yt-tfilter input{ flex:1 1 200px; min-width:0; min-height:38px; padding:8px 10px; font-size:16px; color:var(--yt-text); background:var(--yt-field-bg, var(--yt-bg)); border:1px solid var(--yt-field-border, var(--yt-line)); border-radius:8px; }
  .yt-tfilter span{ font-family:'JetBrains Mono',ui-monospace,monospace; font-size:12px; color:var(--yt-text-2); }
  .yt-sortbtn{ background:none !important; border:0 !important; padding:2px 0 !important; margin:0 !important; color:inherit !important; font:inherit !important; text-transform:inherit !important; letter-spacing:inherit !important; display:inline-flex; gap:6px; align-items:center; min-height:24px; text-align:left; }
  .yt-sortbtn::after{ content:"\2195"; opacity:.55; }
  th[aria-sort="ascending"] .yt-sortbtn::after{ content:"\2191"; opacity:1; }
  th[aria-sort="descending"] .yt-sortbtn::after{ content:"\2193"; opacity:1; }
  .yt-table tr[hidden]{ display:none; }
"""

JS = r"""
<script>
/* POST WIDGETS runtime: calculators, checklists, tabs, sortable tables.
   Enhances markup that is complete without it. House rules: no double
   ampersand or double pipe, ASCII only, addEventListener only. */
(function(){
  function ready(fn){ if(document.readyState === 'loading'){ document.addEventListener('DOMContentLoaded', fn); } else { fn(); } }
  ready(function(){
    document.documentElement.classList.add('yt-js');

    /* ---------- expression language, mirrors postkit_interactive.evaluate ---------- */
    var FUN = {
      min: Math.min, max: Math.max, floor: Math.floor, ceil: Math.ceil, abs: Math.abs, sqrt: Math.sqrt,
      ln: Math.log, log10: function(x){ return Math.log(x) / Math.LN10; }, pow: Math.pow,
      round: function(x, n){ var k = Math.pow(10, n ? n : 0); return Math.floor(x * k + 0.5) / k; }
    };
    function tokens(src){
      var re = /\s*(?:(\d+\.?\d*(?:e[+-]?\d+)?|\.\d+)|([A-Za-z_][A-Za-z0-9_]*)|(<=|>=|==|!=|[-+*\/^(),<>]))/g, out = [], m, pos = 0;
      src = String(src).replace(/\s+$/, '');
      while(pos < src.length){
        re.lastIndex = pos; m = re.exec(src);
        if(m === null){ throw new Error('bad expression'); }
        if(m.index !== pos){ throw new Error('bad expression'); }
        out.push(m[1] !== undefined ? m[1] : (m[2] !== undefined ? m[2] : m[3]));
        pos = re.lastIndex;
      }
      return out;
    }
    function evaluate(src, env){
      var t = tokens(src), i = 0;
      function peek(){ return i < t.length ? t[i] : null; }
      function take(){ i = i + 1; return t[i - 1]; }
      function comp(){
        var a = add(), op, b;
        while(['<', '<=', '>', '>=', '==', '!='].indexOf(peek()) !== -1){
          op = take(); b = add();
          if(op === '<'){ a = a < b ? 1 : 0; } else if(op === '<='){ a = a <= b ? 1 : 0; } else if(op === '>'){ a = a > b ? 1 : 0; }
          else if(op === '>='){ a = a >= b ? 1 : 0; } else if(op === '=='){ a = a === b ? 1 : 0; } else { a = a !== b ? 1 : 0; }
        }
        return a;
      }
      function add(){ var a = mul(), op; while(peek() === '+' ? true : peek() === '-'){ op = take(); a = op === '+' ? a + mul() : a - mul(); } return a; }
      function mul(){ var a = unary(), op, b; while(peek() === '*' ? true : peek() === '/'){ op = take(); b = unary(); a = op === '*' ? a * b : (b !== 0 ? a / b : NaN); } return a; }
      function unary(){ if(peek() === '-'){ take(); return -unary(); } if(peek() === '+'){ take(); return unary(); } return power(); }
      function power(){ var a = atom(); if(peek() === '^'){ take(); return Math.pow(a, unary()); } return a; }
      function atom(){
        var x = take(), args, v;
        if(x === undefined){ throw new Error('end'); }
        if(x === '('){ v = comp(); take(); return v; }
        if(/^[\d.]/.test(x)){ return parseFloat(x); }
        if(peek() === '('){
          take(); args = [];
          if(peek() !== ')'){ args.push(comp()); while(peek() === ','){ take(); args.push(comp()); } }
          take();
          if(x === 'if'){ return args[0] ? args[1] : args[2]; }
          return FUN[x].apply(null, args);
        }
        if(!(x in env)){ throw new Error('unknown ' + x); }
        return env[x];
      }
      return comp();
    }
    function num(v, d){ return v.toLocaleString('en-US', { minimumFractionDigits: d, maximumFractionDigits: d }); }
    function fmt(v, k){
      if(!isFinite(v)){ return 'n/a'; }
      if(k === 'int'){ return num(Math.floor(v + 0.5), 0); }
      if(k === 'num1'){ return num(v, 1); }
      if(k === 'num2'){ return num(v, 2); }
      if(k === 'pct'){ return num(v, 1) + '%'; }
      if(k === 'pct0'){ return num(v, 0) + '%'; }
      if(k === 'money'){ return (v < 0 ? '-$' : '$') + num(Math.floor(Math.abs(v) + 0.5), 0); }
      if(k === 'money2'){ return (v < 0 ? '-$' : '$') + num(Math.abs(v), 2); }
      if(k === 'gbp'){ return (v < 0 ? '-\u00a3' : '\u00a3') + num(Math.floor(Math.abs(v) + 0.5), 0); }
      if(k === 'gbp2'){ return (v < 0 ? '-\u00a3' : '\u00a3') + num(Math.abs(v), 2); }
      if(k === 'x'){ return num(v, 1) + 'x'; }
      if(k === 'months'){ return num(v, 1) + ' months'; }
      if(k === 'years'){ return num(v, 1) + ' years'; }
      if(k === 'days'){ return num(v, 0) + ' days'; }
      return num(v, 2);
    }

    /* ---------- calculators ---------- */
    document.querySelectorAll('[data-yt-calc]').forEach(function(box){
      function run(){
        var env = {};
        box.querySelectorAll('[data-v]').forEach(function(c){ var x = parseFloat(String(c.value).replace(/,/g, '')); env[c.getAttribute('data-v')] = isNaN(x) ? NaN : x; });
        box.querySelectorAll('output[data-expr]').forEach(function(o){
          var v;
          try { v = evaluate(o.getAttribute('data-expr'), env); } catch(e){ v = NaN; }
          var n = o.getAttribute('data-name');
          if(n){ env[n] = v; }
          o.textContent = fmt(v, o.getAttribute('data-fmt'));
        });
      }
      box.addEventListener('input', run);
      box.addEventListener('change', run);
      run();
    });

    /* ---------- checklists ---------- */
    function copyText(text, btn){
      var done = function(){ var o = btn.textContent; btn.textContent = 'Copied'; setTimeout(function(){ btn.textContent = o; }, 1400); };
      try { navigator.clipboard.writeText(text).then(done, function(){}); } catch(e){
        var ta = document.createElement('textarea'); ta.value = text; document.body.appendChild(ta); ta.select();
        try { document.execCommand('copy'); done(); } catch(e2){}
        ta.remove();
      }
    }
    document.querySelectorAll('[data-yt-check]').forEach(function(box){
      var id = 'yt-check:' + location.pathname + ':' + box.getAttribute('data-yt-check');
      var boxes = box.querySelectorAll('input[type="checkbox"]');
      var bands = null;
      try { bands = JSON.parse(box.getAttribute('data-bands')); } catch(e){ bands = null; }
      var saved = null;
      try { saved = JSON.parse(localStorage.getItem(id)); } catch(e){ saved = null; }
      if(saved){ boxes.forEach(function(b){ if(saved.indexOf(b.getAttribute('data-k')) !== -1){ b.checked = true; } }); }
      ['.yt-check__bar', '.yt-check__actions'].forEach(function(s){ var el = box.querySelector(s); if(el){ el.hidden = false; } });
      var verdict = box.querySelector('.yt-check__verdict');
      if(bands){ verdict.hidden = false; }
      function update(){
        var n = 0, on = [];
        boxes.forEach(function(b){ if(b.checked){ n = n + 1; on.push(b.getAttribute('data-k')); } });
        var pct = boxes.length ? Math.round(n / boxes.length * 100) : 0;
        box.querySelector('.yt-check__count').textContent = n + ' of ' + boxes.length + ' done';
        box.querySelector('.yt-check__fill').style.width = pct + '%';
        if(bands){ var txt = ''; bands.forEach(function(b){ if(pct >= b[0]){ txt = b[1]; } }); verdict.textContent = txt; }
        try { localStorage.setItem(id, JSON.stringify(on)); } catch(e){}
      }
      box.addEventListener('change', update);
      box.addEventListener('click', function(e){
        var b = e.target.closest('[data-act]');
        if(b === null){ return; }
        if(b.getAttribute('data-act') === 'reset'){ boxes.forEach(function(x){ x.checked = false; }); update(); return; }
        var md = ['## ' + box.querySelector('figcaption').textContent.trim(), ''];
        box.querySelectorAll('fieldset').forEach(function(f){
          md.push('### ' + f.querySelector('legend').textContent.trim());
          f.querySelectorAll('.yt-check__item').forEach(function(it){ md.push('- [' + (it.querySelector('input').checked ? 'x' : ' ') + '] ' + it.textContent.trim()); });
          md.push('');
        });
        copyText(md.join('\n'), b);
      });
      update();
    });

    /* ---------- tabs ---------- */
    var tcount = 0;
    document.querySelectorAll('[data-yt-tabs]').forEach(function(box){
      tcount = tcount + 1;
      var list = box.querySelector('[role="tablist"]'), tabs = box.querySelectorAll('[role="tab"]'), panels = box.querySelectorAll('[role="tabpanel"]');
      list.hidden = false;
      function show(k, focus){
        tabs.forEach(function(t, j){ t.setAttribute('aria-selected', j === k ? 'true' : 'false'); t.tabIndex = j === k ? 0 : -1; });
        panels.forEach(function(p, j){ p.hidden = j !== k; });
        if(focus){ tabs[k].focus(); }
      }
      tabs.forEach(function(t, j){
        t.id = 'yt-tab-' + tcount + '-' + j; panels[j].id = 'yt-tabp-' + tcount + '-' + j;
        t.setAttribute('aria-controls', panels[j].id); panels[j].setAttribute('aria-labelledby', t.id); panels[j].tabIndex = 0;
        t.addEventListener('click', function(){ show(j, false); });
        t.addEventListener('keydown', function(e){
          var k = -1;
          if(e.key === 'ArrowRight'){ k = (j + 1) % tabs.length; } else if(e.key === 'ArrowLeft'){ k = (j - 1 + tabs.length) % tabs.length; }
          else if(e.key === 'Home'){ k = 0; } else if(e.key === 'End'){ k = tabs.length - 1; }
          if(k !== -1){ e.preventDefault(); show(k, true); }
        });
      });
      show(0, false);
    });

    /* ---------- sortable and filterable tables ---------- */
    function cellVal(td){
      var s = td.textContent.trim(), n = parseFloat(s.replace(/[$,%\u00a3\u20ac\s]|x$/g, '').replace(/^~/, ''));
      return isNaN(n) ? s.toLowerCase() : n;
    }
    document.querySelectorAll('table[data-yt-sort]').forEach(function(tb){
      var body = tb.tBodies[0];
      tb.querySelectorAll('thead th').forEach(function(th, col){
        var b = document.createElement('button');
        b.type = 'button'; b.className = 'yt-sortbtn'; b.innerHTML = th.innerHTML;
        th.innerHTML = ''; th.appendChild(b);
        b.addEventListener('click', function(){
          var asc = th.getAttribute('aria-sort') !== 'ascending';
          tb.querySelectorAll('thead th').forEach(function(o){ o.removeAttribute('aria-sort'); });
          th.setAttribute('aria-sort', asc ? 'ascending' : 'descending');
          var rows = Array.prototype.slice.call(body.rows);
          rows.sort(function(r1, r2){
            var a = cellVal(r1.cells[col]), z = cellVal(r2.cells[col]), c;
            if(typeof a === typeof z){ c = a < z ? -1 : (a > z ? 1 : 0); } else { c = typeof a === 'number' ? -1 : 1; }
            return asc ? c : -c;
          });
          rows.forEach(function(r){ body.appendChild(r); });
        });
      });
      if(tb.hasAttribute('data-yt-filter')){
        var wrap = document.createElement('div'), inp = document.createElement('input'), cnt = document.createElement('span');
        wrap.className = 'yt-tfilter';
        inp.type = 'search'; inp.placeholder = 'Filter rows'; inp.setAttribute('aria-label', 'Filter the rows of this table');
        cnt.setAttribute('aria-live', 'polite');
        wrap.appendChild(inp); wrap.appendChild(cnt);
        var host = tb.closest('.yt-table__wrap'); host = host ? host : tb;
        host.parentNode.insertBefore(wrap, host);
        var all = body.rows.length;
        inp.addEventListener('input', function(){
          var q = inp.value.trim().toLowerCase(), shown = 0;
          Array.prototype.forEach.call(body.rows, function(r){ var hit = r.textContent.toLowerCase().indexOf(q) !== -1; r.hidden = !hit; if(hit){ shown = shown + 1; } });
          cnt.textContent = q === '' ? '' : shown + ' of ' + all + ' rows';
        });
      }
    });
  });
})();
</script>
"""
