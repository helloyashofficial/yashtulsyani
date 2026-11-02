// suite.js <out.json> <page...>
// Responsive + accessibility audit for yashtulsyani.com blocks (ported from FSDM).
// Layout checks at 10 widths x 2 themes; a11y checks at 375 and 1440 (light).
const { chromium } = require('playwright');
const fs = require('fs');
const WIDTHS = [320, 375, 414, 768, 834, 1024, 1180, 1280, 1440, 1920];

async function open(br, name, w, theme) {
  const ctx = await br.newContext({ viewport: { width: w, height: 900 }, acceptDownloads: true });
  const p = await ctx.newPage();
  p._errs = [];
  p.on('pageerror', e => p._errs.push(String(e).slice(0, 200)));
  p.on('console', m => { if (m.type() === 'error') { const t = m.text(); if (!/ERR_FAILED|file:\/\/\/wp-json|URL scheme "file"/.test(t)) p._errs.push(t.slice(0, 200)); } });
  await p.route(/^https?:/, r => r.abort());
  await p.goto(`file://${__dirname}/${name}.html`);
  await p.addStyleTag({ content: '*,*::before,*::after{ transition:none !important; animation:none !important; }' });
  await p.evaluate(t => document.documentElement.setAttribute('data-yt-theme', t), theme);
  await p.waitForTimeout(250);
  return p;
}

const LAYOUT = () => {
  const out = { hscroll: 0, overflow: [], clipped: [], contrast: [], tiny: [] };
  const vw = window.innerWidth;
  out.hscroll = Math.max(0, document.documentElement.scrollWidth - vw);
  const vis = n => { const cs = getComputedStyle(n); if (cs.display === 'none') return false; if (cs.visibility === 'hidden') return false; const r = n.getBoundingClientRect(); return r.width > 0 ? r.height > 0 : false; };
  const inScroller = n => { let p = n.parentElement; while (p) { const o = getComputedStyle(p).overflowX; if (o === 'auto' || o === 'scroll' || o === 'hidden' || o === 'clip') return true; p = p.parentElement; } return false; };
  const sel = n => (n.tagName.toLowerCase() + (n.id ? '#' + n.id : '') + (typeof n.className === 'string' && n.className ? '.' + n.className.trim().split(/\s+/).slice(0, 2).join('.') : ''));
  const rgb = s => { const m = s.match(/rgba?\(([^)]+)\)/); if (!m) return null; const v = m[1].split(/[ ,\/]+/).filter(Boolean).map(parseFloat); return { c: v.slice(0, 3), a: v.length > 3 ? v[3] : 1 }; };
  const blend = (top, bot) => top.c.map((x, i) => x * top.a + bot[i] * (1 - top.a));
  const bgOf = n => { const stack = []; while (n) { const b = rgb(getComputedStyle(n).backgroundColor); if (b) { if (b.a > 0) stack.push(b); if (b.a >= 0.99) break; } n = n.parentElement; } let base = [255, 255, 255]; for (let i = stack.length - 1; i >= 0; i--) base = blend(stack[i], base); return base; };
  const L = c => { const [r, g, b] = c.map(v => { v /= 255; return v <= 0.03928 ? v / 12.92 : Math.pow((v + 0.055) / 1.055, 2.4); }); return .2126 * r + .7152 * g + .0722 * b; };
  document.querySelectorAll('body *').forEach(n => {
    if (n.closest('svg')) { if (n.tagName.toLowerCase() !== 'text') return; }
    if (!vis(n)) return;
    const r = n.getBoundingClientRect();
    if (r.right > vw + 1) if (getComputedStyle(n).position !== 'fixed') if (!inScroller(n)) out.overflow.push(sel(n) + ' r=' + Math.round(r.right));
    const own = [...n.childNodes].some(c => c.nodeType === 3 ? c.textContent.trim().length > 1 : false);
    if (!own) return;
    if (n.closest('.yt-mt__serp')) return;
    const cs = getComputedStyle(n);
    if (n.scrollWidth > n.clientWidth + 2) if (cs.overflowX === 'hidden') if (cs.textOverflow !== 'ellipsis') if (!/nowrap/.test(cs.whiteSpace)) out.clipped.push(sel(n));
    if (parseFloat(cs.fontSize) < 11) out.tiny.push(sel(n) + ' ' + cs.fontSize);
    const fg = rgb(cs.color); if (!fg) return;
    const bg = bgOf(n);
    const f = fg.a < 1 ? blend(fg, bg) : fg.c;
    const a = L(f), b = L(bg), ratio = (Math.max(a, b) + .05) / (Math.min(a, b) + .05);
    const fsz = parseFloat(cs.fontSize), bold = parseInt(cs.fontWeight) >= 700;
    const big = fsz >= 24 ? true : (fsz >= 18.66 ? bold : false);
    if (ratio < (big ? 3 : 4.5)) out.contrast.push(sel(n) + ' ' + ratio.toFixed(2) + ' "' + n.textContent.trim().slice(0, 30) + '"');
  });
  ['overflow', 'clipped', 'contrast', 'tiny'].forEach(k => { out[k] = [...new Set(out[k])]; });
  return out;
};

const A11Y = () => {
  const out = { dupIds: [], headings: [], aria: [], nested: [], tabindex: [], targets: [], noalt: [], svg: [], h1: 0, landmarks: [] };
  const sel = n => (n.tagName.toLowerCase() + (n.id ? '#' + n.id : '') + (typeof n.className === 'string' && n.className ? '.' + n.className.trim().split(/\s+/).slice(0, 2).join('.') : ''));
  const vis = n => { const cs = getComputedStyle(n); if (cs.display === 'none') return false; if (cs.visibility === 'hidden') return false; const r = n.getBoundingClientRect(); return r.width > 0 ? r.height > 0 : false; };
  const ids = {}; document.querySelectorAll('[id]').forEach(n => { ids[n.id] = (ids[n.id] || 0) + 1; });
  out.dupIds = Object.keys(ids).filter(k => ids[k] > 1);
  let last = 0;
  document.querySelectorAll('h1,h2,h3,h4,h5,h6').forEach(h => { if (!vis(h)) return; if (h.closest('[aria-hidden="true"]')) return; const l = +h.tagName[1]; if (l === 1) out.h1++; if (last) if (l > last + 1) out.headings.push('h' + last + ' -> h' + l + ' "' + h.textContent.trim().slice(0, 40) + '"'); last = l; });
  document.querySelectorAll('[aria-labelledby],[aria-describedby],[aria-controls],label[for]').forEach(n => {
    ['aria-labelledby', 'aria-describedby', 'aria-controls'].forEach(a => { const v = n.getAttribute(a); if (v) v.split(/\s+/).forEach(id => { if (!document.getElementById(id)) out.aria.push(sel(n) + ' ' + a + '=' + id); }); });
    if (n.tagName === 'LABEL') { const f = n.getAttribute('for'); if (!document.getElementById(f)) out.aria.push('label for=' + f + ' missing'); }
  });
  const INTER = 'a[href],button,input,select,textarea,summary,[role="button"],[tabindex]';
  const small = [];
  const allRects = [...document.querySelectorAll(INTER)].filter(vis).map(n => ({ n, r: n.getBoundingClientRect() }));
  document.querySelectorAll(INTER).forEach(n => {
    const par = n.parentElement ? n.parentElement.closest('a[href],button') : null;
    if (par) out.nested.push(sel(par) + ' > ' + sel(n));
    const ti = parseInt(n.getAttribute('tabindex'));
    if (ti > 0) out.tabindex.push(sel(n) + ' tabindex=' + ti);
    if (!vis(n)) return;
    if (n.type === 'hidden') return;
    const r = n.getBoundingClientRect();
    if (r.width >= 24) if (r.height >= 24) return;
    // WCAG 2.5.8 exceptions: inline links in a sentence; native unstyled controls (checkbox in a label)
    if (n.tagName === 'A') { const p = n.closest('p,li,td,dd,figcaption,span.yt-field__hint,.yt-viz__src,small'); if (p) if (p.textContent.trim().length > n.textContent.trim().length + 3) return; }
    if (n.type === 'checkbox' || n.type === 'radio') { if (n.closest('label')) return; }
    small.push({ n, r, s: sel(n) + ' ' + Math.round(r.width) + 'x' + Math.round(r.height) });
  });
  // WCAG 2.5.8 spacing exception: an undersized target passes when a 24px
  // circle centred on it does not intersect any other target, nor the
  // 24px circle of another undersized target.
  const dist = (cx, cy, r) => { const dx = Math.max(r.left - cx, 0, cx - r.right), dy = Math.max(r.top - cy, 0, cy - r.bottom); return Math.sqrt(dx * dx + dy * dy); };
  small.forEach(t => {
    const cx = (t.r.left + t.r.right) / 2, cy = (t.r.top + t.r.bottom) / 2;
    let ok = true;
    allRects.forEach(o => { if (o.n === t.n) return; if (o.n.contains(t.n)) return; if (t.n.contains(o.n)) return; if (dist(cx, cy, o.r) < 12) ok = false; });
    small.forEach(u => { if (u === t) return; const ux = (u.r.left + u.r.right) / 2, uy = (u.r.top + u.r.bottom) / 2; if (Math.hypot(ux - cx, uy - cy) < 24) ok = false; });
    if (!ok) out.targets.push(t.s);
  });
  document.querySelectorAll('img').forEach(i => { if (!i.hasAttribute('alt')) out.noalt.push(i.src.slice(-50)); });
  document.querySelectorAll('svg').forEach(s => {
    if (s.closest('[aria-hidden="true"]')) return;
    if (s.getAttribute('aria-hidden') === 'true') return;
    const role = s.getAttribute('role');
    const named = s.getAttribute('aria-label') ? true : (s.getAttribute('aria-labelledby') ? true : !!s.querySelector('title'));
    if (role === 'img') { if (!named) out.svg.push('role=img without name ' + sel(s.parentElement)); return; }
    if (role === 'presentation' || role === 'none') return;
    out.svg.push('svg neither hidden nor labelled in ' + sel(s.parentElement));
  });
  out.landmarks = ['main', 'nav', 'header', 'footer', 'aside'].map(t => t + ':' + document.querySelectorAll(t + ',[role="' + (t === 'nav' ? 'navigation' : t === 'aside' ? 'complementary' : t) + '"]').length);
  ['dupIds', 'headings', 'aria', 'nested', 'tabindex', 'targets', 'noalt', 'svg'].forEach(k => { out[k] = [...new Set(out[k])]; });
  return out;
};

async function axNames(p) {
  const c = await p.context().newCDPSession(p);
  const { nodes } = await c.send('Accessibility.getFullAXTree');
  const bad = [];
  const ROLES = new Set(['button', 'link', 'textbox', 'combobox', 'checkbox', 'radio', 'listbox', 'searchbox', 'spinbutton', 'slider', 'switch', 'tab', 'menuitem', 'image', 'img']);
  for (const n of nodes) {
    if (n.ignored) continue;
    const role = n.role ? n.role.value : '';
    if (!ROLES.has(role)) continue;
    const name = n.name ? String(n.name.value || '').trim() : '';
    if (name === '') bad.push(role + (n.backendDOMNodeId ? '#' + n.backendDOMNodeId : ''));
  }
  // resolve a few to selectors
  const res = [];
  for (const b of bad.slice(0, 8)) {
    const id = parseInt(b.split('#')[1]);
    try { const { object } = await c.send('DOM.resolveNode', { backendNodeId: id }); const r = await c.send('Runtime.callFunctionOn', { objectId: object.objectId, functionDeclaration: 'function(){ return this.outerHTML ? this.outerHTML.slice(0,140) : String(this.nodeName); }', returnByValue: true }); res.push(b.split('#')[0] + ': ' + r.result.value); } catch (e) { res.push(b); }
  }
  return { count: bad.length, sample: res };
}

async function focusCheck(p) {
  // Tab through up to 60 stops: each focused element must show a visible indicator
  const missing = [], order = [];
  await p.addStyleTag({ content: '*,*::before,*::after{ transition:none !important; animation:none !important; }' });
  await p.evaluate(() => { document.activeElement && document.activeElement.blur && document.activeElement.blur(); window.scrollTo(0, 0); });
  for (let i = 0; i < 60; i++) {
    await p.keyboard.press('Tab');
    const r = await p.evaluate(() => {
      const e = document.activeElement; if (!e || e === document.body) return null;
      const cs = getComputedStyle(e);
      const ring = (cs.outlineStyle !== 'none' ? parseFloat(cs.outlineWidth) > 0 : false) ? true : (cs.boxShadow !== 'none');
      const rect = e.getBoundingClientRect();
      return { s: e.tagName.toLowerCase() + (e.id ? '#' + e.id : '') + (typeof e.className === 'string' && e.className ? '.' + e.className.trim().split(/\s+/)[0] : ''), ring, visible: rect.width > 0 ? rect.height > 0 : false };
    });
    if (!r) break;
    order.push(r.s);
    if (!r.ring) missing.push(r.s);
    if (!r.visible) missing.push('invisible-focus ' + r.s);
  }
  return { stops: order.length, missing: [...new Set(missing)] };
}

(async () => {
  const outFile = process.argv[2], pages = process.argv.slice(3);
  const br = await chromium.launch();
  const R = {};
  for (const name of pages) {
    R[name] = { layout: {}, a11y: {}, errs: [] };
    for (const w of WIDTHS) for (const th of ['light', 'dark']) {
      const p = await open(br, name, w, th);
      const l = await p.evaluate(LAYOUT);
      const key = w + '-' + th;
      if (l.hscroll || l.overflow.length || l.clipped.length || l.contrast.length) R[name].layout[key] = l;
      if (th === 'light') if (w === 375) R[name].tiny375 = l.tiny.slice(0, 6);
      R[name].errs.push(...p._errs);
      if (th === 'light') if (w === 375 || w === 1440) {
        const a = await p.evaluate(A11Y);
        a.ax = await axNames(p);
        if (w === 1440) a.focus = await focusCheck(p);
        R[name].a11y[w] = a;
      }
      await p.context().close();
    }
    R[name].errs = [...new Set(R[name].errs)];
    process.stdout.write(name + ' ');
  }
  fs.writeFileSync(outFile, JSON.stringify(R, null, 1));
  await br.close();
  console.log('\nwrote ' + outFile);
})();
