import json,glob,collections,sys
R={}
for f in glob.glob('part_*.json'): R.update(json.load(open(f)))
print(len(R),'pages')
lay=[(n,k,l['hscroll'],l['overflow'][:3],l['clipped'][:2],l['contrast'][:3]) for n,v in sorted(R.items()) for k,l in v['layout'].items()]
print('LAYOUT issues:',len(lay))
for x in lay[:40]: print(' ',x)
agg=collections.defaultdict(lambda: collections.defaultdict(set))
for n,v in sorted(R.items()):
    for w,a in v['a11y'].items():
        for k in ['dupIds','headings','aria','nested','tabindex','targets','noalt','svg']:
            for x in a[k]: agg[k][x+' @'+w].add(n)
        if a['h1']!=1: agg['h1count'][str(a['h1'])].add(n)
        for s in a['ax']['sample']: agg['axname'][s[:150]].add(n)
        if 'focus' in a:
            for m in a['focus']['missing']: agg['focus'][m].add(n)
            if a['focus']['stops']<5: agg['fewstops'][str(a['focus']['stops'])].add(n)
    for e in v['errs']: agg['jserr'][e[:120]].add(n)
for k,d in agg.items():
    print('=====',k,len(d))
    for x,ns in sorted(d.items(), key=lambda kv:-len(kv[1]))[:30]:
        print('  [%d] %s :: %s'%(len(ns),x[:140], ', '.join(sorted(ns))[:200]))
