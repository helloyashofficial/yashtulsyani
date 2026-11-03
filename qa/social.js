// social.js <essays.json> <outdir> <fontdir>
// Renders a 1200x630 share image per essay: the essay's cover drawing and
// its title, in the site's light theme and fonts (Inter, JetBrains Mono).
// essays.json: [{slug, title, cat, svg}], from generators/social-data.py.
const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');

const [, , dataFile, outDir, fontDir] = process.argv;
const essays = JSON.parse(fs.readFileSync(dataFile, 'utf8'));
fs.mkdirSync(outDir, { recursive: true });
const font = (fam, file, w) => {
  const p = path.join(fontDir, file);
  if (!fs.existsSync(p)) throw new Error('missing font ' + p);
  // Embedded as data: URLs. A page built with setContent cannot load file:// fonts.
  const b64 = fs.readFileSync(p).toString('base64');
  return `@font-face{font-family:"${fam}";font-weight:${w};src:url(data:font/woff2;base64,${b64}) format("woff2");}`;
};
const FONTS = [
  font('Inter', '@fontsource/inter/files/inter-latin-500-normal.woff2', 500),
  font('Inter', '@fontsource/inter/files/inter-latin-600-normal.woff2', 600),
  font('JetBrains Mono', '@fontsource/jetbrains-mono/files/jetbrains-mono-latin-500-normal.woff2', 500),
].join('\n');

const esc = s => s.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
const page = e => `<!doctype html><html><head><meta charset="utf-8"><style>
${FONTS}
*{ box-sizing:border-box; margin:0; padding:0; }
html,body{ width:1200px; height:630px; background:#f5f5f3; }
.w{ position:absolute; inset:0; padding:64px 72px; display:grid; grid-template-columns:1fr 460px; gap:56px; align-items:center; }
.eb{ font:500 17px/1 "JetBrains Mono", monospace; letter-spacing:.16em; text-transform:uppercase; color:#4b5563; margin-bottom:26px; }
.eb span{ background:#ececea; padding:7px 12px; border-radius:7px; }
h1{ font:600 50px/1.12 Inter, sans-serif; letter-spacing:-.025em; color:#111827; }
.by{ position:absolute; left:72px; bottom:60px; font:500 21px/1 Inter, sans-serif; color:#111827; }
.by b{ font:500 17px/1 "JetBrains Mono", monospace; color:#4b5563; margin-left:14px; letter-spacing:.02em; font-weight:500; }
.cv{ width:460px; height:230px; border-radius:16px; background:#ececea; overflow:hidden; }
.yt-cv{ display:block; width:100%; height:100%; }
.yt-cv *{ vector-effect:non-scaling-stroke; }
.yt-cv .yt-cv-a{ stroke:#4b5563; stroke-width:2; }
.yt-cv .yt-cv-b{ stroke:#9ca3af; stroke-width:1.25; }
.yt-cv .yt-cv-c{ stroke:#9ca3af; stroke-opacity:.5; stroke-width:1.25; }
.yt-cv .yt-cv-dot{ stroke:none; fill:#4b5563; }
.ln{ position:absolute; left:72px; right:72px; top:0; height:1px; }
</style></head><body><div class="w">
<div><div class="eb"><span>${esc(e.cat)}</span></div><h1>${esc(e.title)}</h1></div>
<div class="cv">${e.svg}</div>
</div><div class="by">Yash Tulsyani<b>yashtulsyani.com</b></div></body></html>`;

(async () => {
  const br = await chromium.launch();
  const p = await br.newPage({ viewport: { width: 1200, height: 630 }, deviceScaleFactor: 1 });
  for (const e of essays) {
    await p.setContent(page(e), { waitUntil: 'load' });
    await p.evaluate(() => document.fonts.ready);
    const ok = await p.evaluate(() => [...document.fonts].filter(f => f.status === 'loaded').map(f => f.family.replace(/"/g, '') + ' ' + f.weight));
    for (const need of ['Inter 600', 'JetBrains Mono 500']) {
      if (!ok.includes(need)) throw new Error('font did not load: ' + need + ' (loaded: ' + ok.join(', ') + ')');
    }
    const fit = await p.evaluate(() => { const h = document.querySelector('h1'); return h.getBoundingClientRect().height; });
    if (fit > 300) await p.evaluate(() => { document.querySelector('h1').style.fontSize = '42px'; });
    await p.screenshot({ path: path.join(outDir, e.slug + '.png'), type: 'png' });
    console.log('wrote', e.slug + '.png');
  }
  await br.close();
})();
