#!/usr/bin/env python3
"""check.py: fail (exit 1) if the browser suite found any problem.

report.py prints a summary but always exits 0, which is fine by hand and
useless in CI. This reads the same part_*.json files and fails on any
layout, overflow, clipping or contrast issue, any accessibility finding,
any unnamed control, any missing focus ring, or any JavaScript error.
"""
import glob, json, sys
R = {}
for f in glob.glob("part_*.json"):
    R.update(json.load(open(f)))
if not R:
    sys.exit("no results found; run suite.js first")
bad = []
for name, v in sorted(R.items()):
    for key, l in v["layout"].items():
        bad.append("%s @%s: hscroll %s overflow %s clipped %s contrast %s"
                   % (name, key, l["hscroll"], l["overflow"][:2], l["clipped"][:2], l["contrast"][:2]))
    for w, a in v["a11y"].items():
        for k in ["dupIds", "headings", "aria", "nested", "tabindex", "targets", "noalt", "svg"]:
            for x in a[k]:
                bad.append("%s @%s: %s %s" % (name, w, k, x))
        if a["h1"] != 1:
            bad.append("%s @%s: %d visible h1" % (name, w, a["h1"]))
        if a["ax"]["count"]:
            bad.append("%s @%s: %d controls without an accessible name" % (name, w, a["ax"]["count"]))
        for m in a.get("focus", {}).get("missing", []):
            bad.append("%s @%s: no focus ring on %s" % (name, w, m))
    for e in v["errs"]:
        bad.append("%s: JS error %s" % (name, e))
print("%d pages checked, %d problem(s)" % (len(R), len(bad)))
for b in bad[:80]:
    print("  FAIL  " + b)
sys.exit(1 if bad else 0)
