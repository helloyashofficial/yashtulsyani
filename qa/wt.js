const { chromium } = require('playwright');
(async () => { const br = await chromium.launch(); const ctx=await br.newContext({viewport:{width:1280,height:900}}); const p = await ctx.newPage(); const errs=[]; p.on('pageerror',e=>errs.push(String(e))); p.on('console',m=>{if(m.type()==='error')errs.push(m.text())});
 await p.route(/^https?:/, r => r.abort()); await p.goto(`file://${__dirname}/wtest.html`); await p.waitForTimeout(300);
 const outs=async()=>p.$$eval('#calc-kv output',o=>o.map(x=>x.textContent));
 console.log('calc default', await outs());
 await p.fill('#calc-kv-vol','1000'); console.log('vol=1000', await outs());
 await p.selectOption('#calc-kv-plan','12'); console.log('plan=12', await outs());
 await p.fill('#calc-kv-vol',''); console.log('empty', await outs());
 // checklist
 await p.check('[data-yt-check] input[data-k="1"]'); await p.check('[data-yt-check] input[data-k="2"]');
 console.log('check', await p.$eval('.yt-check__count',e=>e.textContent), await p.$eval('.yt-check__verdict',e=>e.textContent));
 await p.reload(); await p.waitForTimeout(200); console.log('after reload', await p.$eval('.yt-check__count',e=>e.textContent));
 // tabs
 console.log('tabs visible panels', await p.$$eval('.yt-tabs__panel',ps=>ps.map(x=>!x.hidden)));
 await p.focus('.yt-tabs__tab'); await p.keyboard.press('ArrowRight'); console.log('after arrow', await p.$$eval('.yt-tabs__panel',ps=>ps.map(x=>!x.hidden)), await p.evaluate(()=>document.activeElement.textContent));
 // sort
 await p.click('table[data-yt-sort] th:nth-child(2) button'); console.log('sorted asc', await p.$$eval('table[data-yt-sort] tbody tr td:first-child',t=>t.slice(0,4).map(x=>x.textContent)));
 await p.click('table[data-yt-sort] th:nth-child(2) button'); console.log('sorted desc', await p.$$eval('table[data-yt-sort] tbody tr td:first-child',t=>t.slice(0,4).map(x=>x.textContent)));
 await p.fill('.yt-tfilter input','tra'); console.log('filter', await p.$eval('.yt-tfilter span',e=>e.textContent));
 await p.click('.yt-check__btn[data-act="reset"]'); console.log('reset', await p.$eval('.yt-check__count',e=>e.textContent));
 console.log('errs',errs);
 // no-JS rendering
 const c2=await br.newContext({javaScriptEnabled:false,viewport:{width:390,height:900}}); const q=await c2.newPage(); await q.goto(`file://${__dirname}/wtest.html`);
 console.log('nojs calc', await q.$$eval('#calc-kv output',o=>o.map(x=>x.textContent)), 'tabs panels', await q.$$eval('.yt-tabs__panel',ps=>ps.map(x=>x.offsetHeight>0)), 'tablist hidden', await q.$eval('.yt-tabs__list',e=>e.offsetHeight===0));
 await p.screenshot({path:'shots/widgets-1280.png',fullPage:true});
 const m=await (await br.newContext({viewport:{width:375,height:900}})).newPage(); await m.route(/^https?:/, r => r.abort()); await m.goto(`file://${__dirname}/wtest.html`); await m.waitForTimeout(300); await m.evaluate(()=>document.documentElement.setAttribute('data-yt-theme','dark')); await m.screenshot({path:'shots/widgets-375-dark.png',fullPage:true});
 await br.close(); })();
