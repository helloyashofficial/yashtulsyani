// states.js <out.json> <page...> : layout + contrast in interactive states
// (every data-tab view on tool pages, all <details> open, mobile menu open)
const { chromium } = require('playwright');
const fs = require('fs');
const src = fs.readFileSync(__dirname + '/suite.js', 'utf8');
const LAYOUT = eval('(' + src.split('const LAYOUT = ')[1].split('\n};\n')[0] + '\n})');
const WIDTHS = [320, 375, 768, 1024, 1280];

(async () => {
  const outFile = process.argv[2], pages = process.argv.slice(3);
  const br = await chromium.launch();
  const R = {};
  for (const name of pages) {
    R[name] = {};
    for (const w of WIDTHS) for (const th of ['light', 'dark']) {
      const ctx = await br.newContext({ viewport: { width: w, height: 900 } });
      const p = await ctx.newPage();
      const errs = [];
      p.on('pageerror', e => errs.push(String(e).slice(0, 160)));
      await p.route(/^https?:/, r => r.abort());
      await p.goto(`file://${__dirname}/${name}.html`);
      await p.addStyleTag({ content: '*,*::before,*::after{ transition:none !important; animation:none !important; }' });
      await p.evaluate(t => document.documentElement.setAttribute('data-yt-theme', t), th);
      await p.waitForTimeout(200);
      const states = [];
      // every details open
      await p.evaluate(() => document.querySelectorAll('details').forEach(d => { d.open = true; }));
      await p.evaluate(() => document.querySelectorAll('.yt-faq-item').forEach(d => d.classList.add('is-open')));
      states.push(['details-open', await p.evaluate(LAYOUT)]);
      // tabs on tool pages
      const tabs = await p.$$eval('button[data-tab]', b => [...new Set(b.map(x => x.getAttribute('data-tab')))]);
      for (const t of tabs) {
        const b = await p.$('button[data-tab="' + t + '"]');
        if (b) { try { await b.click({ timeout: 2000 }); await p.waitForTimeout(80); states.push(['tab:' + t, await p.evaluate(LAYOUT)]); } catch (e) { states.push(['tab:' + t, { err: 'not clickable: ' + String(e).slice(0, 80) }]); } }
      }
      // mobile menu
      if (w < 1024) {
        const tog = await p.$('[aria-controls][aria-expanded], .yt-burger, .yt-nav-toggle, button[aria-label*="menu" i]');
        if (tog) { try { await tog.click({ timeout: 2000 }); await p.waitForTimeout(200); states.push(['menu-open', await p.evaluate(LAYOUT)]); } catch (e) { states.push(['menu-open', { err: String(e).slice(0, 80) }]); } }
      }
      for (const [s, l] of states) {
        if (l.err) { (R[name][w + '-' + th] = R[name][w + '-' + th] || []).push([s, l.err]); continue; }
        if (l.hscroll || l.overflow.length || l.contrast.length || l.clipped.length) (R[name][w + '-' + th] = R[name][w + '-' + th] || []).push([s, { hscroll: l.hscroll, overflow: l.overflow.slice(0, 4), contrast: l.contrast.slice(0, 4), clipped: l.clipped.slice(0, 3) }]);
      }
      if (errs.length) R[name]['errs-' + w] = errs;
      await ctx.close();
    }
    process.stdout.write(name + ' ');
  }
  fs.writeFileSync(outFile, JSON.stringify(R, null, 1));
  await br.close();
  console.log('\nwrote ' + outFile);
})();
