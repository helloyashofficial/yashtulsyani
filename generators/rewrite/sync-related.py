#!/usr/bin/env python3
"""sync-related.py :: rewrite every spec's related=[(slug, H1, cat)] titles
to the H1 the target post currently builds with. Prints what changed.
Run, then rebuild the changed specs."""
import re, pathlib, html as H

HERE = pathlib.Path(__file__).resolve().parent
B = HERE.parent.parent / "production-blocks"
h1 = {}
for p in B.glob("[0-9][0-9]-post-*.html"):
    s = p.read_text(encoding="utf-8")
    h1[p.stem.split("-post-", 1)[1]] = H.unescape(re.search(r'yt-post__title">(.*?)</h1>', s, re.S).group(1).strip())

changed = []
for spec in sorted(HERE.glob("[0-9][0-9]-*.py")):
    src = spec.read_text(encoding="utf-8")
    def fix(m):
        slug, q, title = m.group(1), m.group(2), m.group(3)
        want = h1.get(slug)
        if want and title != want:
            changed.append((spec.name, slug, title, want))
            return '("%s", %s%s%s' % (slug, q, want.replace(q, "\\" + q), q)
        return m.group(0)
    new = re.sub(r'\(\s*"([a-z0-9-]+)",\s*(["\'])(.*?)(?<!\\)\2', fix, src)
    if new != src:
        spec.write_text(new, encoding="utf-8")
for c in changed:
    print("%s: %s %r -> %r" % c)
print("%d related titles synced" % len(changed))
