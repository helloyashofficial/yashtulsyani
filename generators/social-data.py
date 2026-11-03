#!/usr/bin/env python3
"""social-data.py <out.json> :: the data qa/social.js needs to draw each
essay's share image (slug, title, subject, cover), read from the essay
blocks so the image cannot disagree with the essay."""
import html, json, re, sys
import ytconf as C
import covers

out = []
for p in sorted(C.BLOCKS.glob("[0-9][0-9]-post-*.html")):
    src = re.sub(r"<!--.*?-->", "", p.read_text(encoding="utf-8"), flags=re.S)
    slug = p.stem.split("-post-", 1)[1]
    title = html.unescape(re.sub(r"<[^>]+>", "", re.search(r'<h1 class="yt-post__title">(.*?)</h1>', src, re.S).group(1))).strip()
    cat = html.unescape(re.search(r"<span data-yt-cat>(.*?)</span>", src).group(1)).strip()
    out.append(dict(slug=slug, title=title, cat=cat, svg=covers.cover(slug, cat)))
json.dump(out, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
print("%d essays" % len(out))
