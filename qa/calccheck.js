const { chromium } = require('playwright'); const fs=require('fs');
(async()=>{ const br=await chromium.launch(); const pages=fs.readdirSync(__dirname).filter(f=>/^\d\d-post-.*\.html$/.test(f));
 let bad=0, n=0, tabsN=0, chk=0;
 for(const f of pages){ const src=fs.readFileSync(__dirname+'/'+f,'utf8');
  const pre=[...src.matchAll(/<output data-expr="[^"]*" data-fmt="[^"]*"(?: data-name="[^"]*")?>([^<]*)<\/output>/g)].map(m=>m[1].replace(/&amp;/g,'&'));
  const p=await br.newPage(); const errs=[]; p.on('pageerror',e=>errs.push(String(e))); await p.route(/^https?:/,r=>r.abort());
  await p.goto('file://'+__dirname+'/'+f); await p.waitForTimeout(150);
  // trigger an input event on every calc to force recompute
  await p.evaluate(()=>document.querySelectorAll('[data-yt-calc] .yt-calc__ctl').forEach(i=>i.dispatchEvent(new Event('input',{bubbles:true}))));
  const post=await p.$$eval('output[data-expr]',o=>o.map(x=>x.textContent));
  n+=post.length; pre.forEach((v,i)=>{ if(v!==post[i]){ bad++; console.log(f,'#'+i,'py='+v,'js='+post[i]); }});
  tabsN+=await p.$$eval('[role=tab]',t=>t.length); chk+=await p.$$eval('.yt-check__item input',t=>t.length);
  if(errs.length) console.log(f,'ERR',errs);
  await p.close(); }
 console.log('outputs',n,'mismatch',bad,'tabs',tabsN,'check items',chk); await br.close(); })();
