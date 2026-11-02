import sys, pathlib; HERE=pathlib.Path(__file__).resolve().parent; sys.path.insert(0,str(HERE.parent/'generators'))
import postkit as K, newpost as np, yoast
# Widget demo: a throwaway essay that is never written to production-blocks.
yoast.YOAST['widget-test']=dict(focus='widget test',title='Widget test',desc='x'*130)
POST=dict(slug="widget-test",num=99,cat="Relationships",read="auto",title="Widget test",dek="Test",takeaway="T",
 sections=[("Widgets",[
  "HTML:"+K.takeaways(["One <strong>bold</strong> point","Second point linking <a href=\"/books\">the books</a>, <a href=\"/writing/why-reassurance-is-never-enough\">the pillar</a> and <a href=\"/writing/what-the-observer-effect-actually-says\">a sibling</a>"]),
  "HTML:"+K.calc("calc-kv","Keyword value calculator",
     [dict(name="vol",label="Monthly searches",value=390),dict(name="ctr",label="Click share",value=10,unit="%"),dict(name="demo",label="Visit to demo",value=5,unit="%"),
      dict(name="win",label="Demo to customer",value=20,unit="%"),dict(name="acv",label="Annual contract value",value=12000,unit="$"),
      dict(name="plan",label="Plan",value=1,options=[(1,"Monthly"),(12,"Annual")])],
     [dict(name="visits",label="Visits a year",expr="vol*12*ctr/100",fmt="int"),dict(name="cust",label="Customers a year",expr="visits*demo/100*win/100",fmt="num1"),
      dict(label="Revenue a year",expr="cust*acv",fmt="money",big=True,hint="Before churn"),dict(label="Ratio",expr="if(cust>1, cust/plan, 0)",fmt="x")],
     note="Hypothetical inputs. Change any number."),
  "HTML:"+K.checklist("audit-basics","Technical checklist",[("Crawl",["robots.txt allows the pages that matter","XML sitemap submitted"]),("Index",["No accidental noindex"])],bands=[[0,"Start with crawl."],[67,"Nearly there."],[100,"Done."]]),
  "HTML:"+K.tabs("In-house vs agency",[("In-house","<p>Owns context.</p>"),("Agency","<p>Brings breadth.</p>"),("Consultant","<p>Sets direction.</p>")]),
  "HTML:"+K.itable("Benchmarks",["Industry","CTR","CPC"],[["Legal","4.1%","$8.50"],["Travel","9.3%","$1.20"],["Dental","5.0%","$6.10"]]+[["Row%d"%i,"%d%%"%i,"$%d"%i] for i in range(10)],source="WordStream 2026",num_cols=(1,2)),
  "HTML:"+K.decision("Merge or keep?",("Do both pages target the same intent?",[("Yes",("Does one page earn most clicks?",[("Yes","Merge into the stronger page."),("No","Merge into the better-linked page.")])),("No","Keep both; differentiate titles.")])),
  "HTML:"+K.callout("warn","Do not redirect first","Update <a href=\"/tools/internal-link-mapper\">internal links</a> before the redirect."),
  "HTML:"+K.callout("example","A 40-page site","Numbers <strong>here</strong>."),
  "HTML:"+K.callout("tip",None,"Short tip."),
  "HTML:"+K.compare("Who should run it",[("In-house",["Context","Speed"],["Hiring cost"],"Best after Series A"),("Agency",["Breadth"],["Context"],None)]),
  "HTML:"+K.flow("The audit loop",[("Crawl","Collect"),("Diagnose","Find cause"),("Fix","Change the rule"),("Measure","Recurrence")]),
 ])],faqs=[("Q1?","A."),("Q2?","A."),("Q3?","A."),("Q4?","A.")],related=[("other","x","Philosophy")])
out=np.build(POST,write=False)
s=open(HERE.parent/'production-blocks'/'01-sidebar.html').read()
open(HERE/'wtest.html','w').write('<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>w</title></head><body style="margin:0"><div class="entry-content single-content">'+s+out+'</div></body></html>')
