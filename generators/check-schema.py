#!/usr/bin/env python3
"""check-schema.py --- site-wide structured data gate.

- every indexable block carries at least one JSON-LD script that parses
- every node @id is on this site and uses a #fragment (Yoast owns the bare
  page URLs, so a bare @id would collide with its WebPage node)
- one @id never carries two different @types across the site
- posts carry a FAQPage whose question count equals the visible FAQ
- HowTo has 3+ steps; Dataset has a 50+ character description and sources
"""
import re, json, sys, pathlib, glob
import ytconf as C

D = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else C.BLOCKS
SITE = C.SITE
# Not indexable, so no schema: the sidebar, and private noindex pages.
SKIP = set(["01-sidebar.html"]) | set(C.PRIVATE)
# Indexable, but with nothing honest to mark up yet. Each needs a reason;
# an empty ItemList or a node invented to satisfy a gate is worse than none.
EXEMPT = {
    "28-reading-provisional.html": "no entries yet; add an ItemList of Book/ScholarlyArticle when filled",
    "29-notes-provisional.html": "no notes yet",
    "26-now.html": "a status page; add an ItemList #reading once the reading list exists",
    "27-contact.html": "Yoast's WebPage covers it; a ContactPage node would be a second page node",
}
bad, types = [], {}


def nodes(x):
    if isinstance(x, list):
        for i in x:
            yield from nodes(i)
    elif isinstance(x, dict):
        if "@type" in x or "@id" in x:
            yield x
        for v in x.values():
            if isinstance(v, (dict, list)):
                yield from nodes(v)


for f in sorted(D.glob("*.html")):
    if f.name in SKIP:
        continue
    if f.name in EXEMPT:
        print("schema exempt: %-30s %s" % (f.name, EXEMPT[f.name]))
        continue
    src = f.read_text(encoding="utf-8")
    # skip JSON-LD that sits inside JS strings (tool examples); real blocks start a line
    scripts = re.findall(r'^\s*<script type="application/ld\+json">(.*?)</script>', src, re.S | re.M)
    if not scripts:
        bad.append("%s: no JSON-LD" % f.name)
        continue
    for s in scripts:
        try:
            doc = json.loads(s)
        except Exception as e:
            bad.append("%s: JSON-LD does not parse: %s" % (f.name, e))
            continue
        for n in nodes(doc):
            i, t = n.get("@id"), n.get("@type")
            if i:
                if not i.startswith(SITE) or "#" not in i:
                    bad.append("%s: @id %s is not a fragment on this site" % (f.name, i))
                if t:
                    prev = types.setdefault(i, (t, f.name))
                    if prev[0] != t:
                        bad.append("%s: @id %s typed %s here, %s in %s" % (f.name, i, t, prev[0], prev[1]))
            if t == "HowTo" and len(n.get("step", [])) < 3:
                bad.append("%s: HowTo with fewer than 3 steps" % f.name)
            if t == "Dataset":
                if len(n.get("description", "")) < 50 or not n.get("isBasedOn"):
                    bad.append("%s: Dataset needs a 50+ char description and isBasedOn" % f.name)
            if t == "FAQPage" and "-post-" in f.name:
                vis = len(re.findall(r"class=\"yt-faq__item", src))
                if vis and vis != len(n.get("mainEntity", [])):
                    bad.append("%s: FAQPage has %d questions, page shows %d" % (f.name, len(n["mainEntity"]), vis))
    if "-post-" in f.name and '"FAQPage"' not in src:
        bad.append("%s: post without FAQPage" % f.name)

for b in bad:
    print("SCHEMA FAIL", b)
print("schema OK: %d @ids, all fragments, no type conflicts" % len(types) if not bad else "%d schema problems" % len(bad))
sys.exit(1 if bad else 0)
