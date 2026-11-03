// live-audit.js <base-url> <path> [outdir]
// Read-only audit of a LIVE hub page (default /writing/): layout at 12 widths
// in both themes, the cards' data against each live essay, page metadata and
// JSON-LD, console errors and broken links. Prints a JSON report; saves
// screenshots to outdir. Makes GET requests only; needs no credentials.
const { chromium } = require('playwright');
const fs = require('fs');
const src = fs.readFileSync(__dirname + '/suite.js', 'utf8');
const LAYOUT = eval('(' + src.split('const LAYOUT = ')[1].split('\n};\n')[0] + '\n})');
const WIDTHS = [320, 360, 375, 390, 414, 768, 834, 1024, 1180, 1280, 1440, 1920];
const SHOTS = [320, 390, 768, 1024, 1440];

(async () => {
  const base = (process.argv[2] || 'https://yashtulsyani.com').replace(/\/$/, '');
  const path = process.argv[3] || '/writing/';
  const out = process.argv[4] || __dirname + '/live-shots';
  fs.mkdirSync(out, { recursive: true });
  const br = await chromium.launch();
  const R = { url: base + path, layout: {}, page: {}, cards: [], essays: [], links: [], problems: [] };

  // 1. Layout and contrast at every width, both themes.
  for (const w of WIDTHS) for (const th of ['light', 'dark']) {
    const ctx = await br.newContext({ viewport: { width: w, height: 900 }, colorScheme: th });
    const p = await ctx.newPage();
    const errs = [];
    p.on('pageerror', e => errs.push(String(e).slice(0, 200)));
    p.on('console', m => { if (m.type() === 'error') errs.push('console: ' + m.text().slice(0, 200)); });
    const resp = await p.goto(base + path, { waitUntil: 'networkidle', timeout: 60000 });
    await p.evaluate(t => document.documentElement.setAttribute('data-yt-theme', t), th);
    await p.waitForTimeout(400);
    const L = await p.evaluate(LAYOUT);
    const key = w + '-' + th;
    R.layout[key] = { status: resp ? resp.status() : 0, hscroll: L.hscroll, overflow: L.overflow.slice(0, 8),
                      clipped: L.clipped.slice(0, 8), contrast: L.contrast.slice(0, 8), tiny: L.tiny.slice(0, 8), errors: errs.slice(0, 5) };
    if (SHOTS.includes(w)) await p.screenshot({ path: `${out}/writing-${w}-${th}.png`, fullPage: true });
    await ctx.close();
  }

  // 2. The page itself: metadata, schema, cards.
  const ctx = await br.newContext({ viewport: { width: 1280, height: 900 } });
  const p = await ctx.newPage();
  await p.goto(base + path, { waitUntil: 'networkidle', timeout: 60000 });
  R.page = await p.evaluate(() => {
    const m = s => { const n = document.querySelector(s); return n ? (n.getAttribute('content') || n.getAttribute('href') || '') : null; };
    const ld = [];
    document.querySelectorAll('script[type="application/ld+json"]').forEach(t => {
      try { const d = JSON.parse(t.textContent); (d['@graph'] || [d]).forEach(n => ld.push(n)); }
      catch (e) { ld.push({ PARSE_ERROR: String(e).slice(0, 120) }); }
    });
    const list = ld.filter(n => n['@type'] === 'ItemList' || (n['@type'] || '').toString().includes('CollectionPage'));
    return {
      title: document.title, description: m('meta[name="description"]'), canonical: m('link[rel="canonical"]'),
      ogTitle: m('meta[property="og:title"]'), robots: m('meta[name="robots"]'),
      h1: [...document.querySelectorAll('h1')].map(h => h.textContent.trim()),
      headings: [...document.querySelectorAll('h2,h3')].map(h => h.tagName + ': ' + h.textContent.trim()).slice(0, 40),
      ldTypes: ld.map(n => n['@type'] || Object.keys(n)[0]),
      itemList: list.map(n => ({ type: n['@type'], id: n['@id'], items: (n.itemListElement || []).map(i => i.url || (i.item && (i.item['@id'] || i.item.url)) || i) })),
      count: (document.querySelector('.yt-wr-count') || {}).textContent || null,
      cards: [...document.querySelectorAll('a.yt-wr-card')].map(a => ({
        href: a.getAttribute('href'), aria: a.getAttribute('aria-label'),
        cat: (a.querySelector('.yt-wr-card__cat') || {}).textContent, meta: (a.querySelector('.yt-wr-card__meta') || {}).textContent,
        title: (a.querySelector('.yt-wr-card__title') || {}).textContent, dek: (a.querySelector('.yt-wr-card__dek') || {}).textContent })),
      links: [...new Set([...document.querySelectorAll('.yt-shell a[href]')].map(a => a.href))],
    };
  });
  R.cards = R.page.cards; delete R.page.cards;
  const links = R.page.links; delete R.page.links;
  await ctx.close();

  // 3. Every essay the cards point to, as rendered live.
  for (const c of R.cards) {
    const ec = await br.newContext({ viewport: { width: 1280, height: 900 } });
    const ep = await ec.newPage();
    const r = await ep.goto(new URL(c.href, base).toString(), { waitUntil: 'networkidle', timeout: 60000 });
    await ep.waitForTimeout(500);
    const e = await ep.evaluate(() => {
      const t = s => { const n = document.querySelector(s); return n ? n.textContent.trim() : null; };
      const m = s => { const n = document.querySelector(s); return n ? n.getAttribute('content') : null; };
      return { h1: t('h1.yt-post__title') || t('h1'), cat: t('[data-yt-cat]'), date: t('[data-yt-date]'), read: t('[data-yt-read]'),
               published: m('meta[property="article:published_time"]'), modified: m('meta[property="article:modified_time"]'),
               yoastRead: m('meta[name="twitter:data2"]'), canonical: (document.querySelector('link[rel="canonical"]') || {}).href || null,
               dek: t('.yt-post__dek'), ogImage: m('meta[property="og:image"]'),
               cover: !!document.querySelector('.yt-post__cover svg'),
               themeImage: [...document.querySelectorAll('img.wp-post-image, .post-thumbnail img')].filter(i => { const r = i.getBoundingClientRect(); const cs = getComputedStyle(i); return r.width > 0 && r.height > 0 && cs.visibility !== 'hidden'; }).length };
    });
    e.href = c.href; e.status = r ? r.status() : 0;
    R.essays.push(e);
    const norm = s => (s || '').replace(/\s+/g, ' ').trim();
    const [cdate, cread] = norm(c.meta).split(/\s*·\s*/);
    if (e.status !== 200) R.problems.push(`${c.href}: HTTP ${e.status}`);
    if (norm(c.title) !== norm(e.h1)) R.problems.push(`${c.href}: card title "${norm(c.title)}" vs essay h1 "${norm(e.h1)}"`);
    if (norm(c.cat) !== norm(e.cat)) R.problems.push(`${c.href}: card subject "${norm(c.cat)}" vs essay "${norm(e.cat)}"`);
    if (norm(cdate) !== norm(e.date)) R.problems.push(`${c.href}: card date "${norm(cdate)}" vs essay shows "${norm(e.date)}" (published ${e.published})`);
    if (norm(cread) !== norm(e.read)) R.problems.push(`${c.href}: card "${norm(cread)}" vs essay shows "${norm(e.read)}" (Yoast: ${e.yoastRead})`);
    if (e.dek) if (norm(c.dek) !== norm(e.dek)) R.problems.push(`${c.href}: card summary differs from the essay dek`);
    if (!e.cover) R.problems.push(`${c.href}: essay has no cover drawing`);
    if (e.themeImage) R.problems.push(`${c.href}: the theme shows the featured image on the page (${e.themeImage})`);
    if (!e.ogImage) R.problems.push(`${c.href}: no og:image`);
    else if (!/yt-social-/.test(e.ogImage)) R.problems.push(`${c.href}: og:image is not the share image: ${e.ogImage}`);
    await ec.close();
  }
  // order: newest first by published time
  const pubs = R.essays.map(e => e.published || '');
  const sorted = [...pubs].sort().reverse();
  if (JSON.stringify(pubs) !== JSON.stringify(sorted)) R.problems.push('cards are not in newest-first order of published date: ' + pubs.join(', '));

  // 4. Every link on the page answers.
  const lc = await br.newContext();
  for (const u of links) {
    if (!/^https?:/.test(u)) continue;
    try { const res = await lc.request.get(u, { timeout: 30000, maxRedirects: 5 }); R.links.push([res.status(), u]); if (res.status() >= 400) R.problems.push(`broken link ${res.status()} ${u}`); }
    catch (e) { R.links.push(['ERR', u]); R.problems.push(`link failed ${u}: ${String(e).slice(0, 80)}`); }
  }
  await br.close();

  for (const [k, v] of Object.entries(R.layout)) {
    if (v.hscroll > 0) R.problems.push(`${k}: page scrolls sideways by ${v.hscroll}px`);
    ['overflow', 'clipped', 'contrast', 'tiny', 'errors'].forEach(f => { if (v[f].length) R.problems.push(`${k}: ${f}: ${v[f].join(' | ')}`); });
  }
  console.log('LIVE-AUDIT-JSON ' + JSON.stringify(R));
  console.log('\nPROBLEMS (' + R.problems.length + ')');
  R.problems.forEach(x => console.log(' - ' + x));
})();
