#!/usr/bin/env python3
"""
sync-writing-hub.py --- pre-render the /writing hub from the essay blocks.

Does the job of FSDM's sync-post-cards.py, but generates the cards instead of
only updating ones added by hand, so a new essay cannot be missing from the
hub. Reads every NN-post-*.html, newest (highest number) first, and writes:

  - the card list between WRITING-CARDS markers in 24-writing.html
  - an ItemList (#essays) between WRITING-SCHEMA markers

Everything a card says is read from the essay block itself (h1, dek, cluster,
build-time date and read time), so the hub cannot disagree with the essay.
"""
import html, json, re, sys
import ytconf as C
import covers

HUB = C.BLOCKS / "24-writing.html"


def field(src, pattern, label, name):
    m = re.search(pattern, src, re.S)
    if not m:
        sys.exit("%s: no %s found" % (name, label))
    return html.unescape(re.sub(r"<[^>]+>", "", m.group(1))).strip()


def essays():
    out = []
    for p in C.BLOCKS.glob("[0-9][0-9]-post-*.html"):
        src = re.sub(r"<!--.*?-->", "", p.read_text(encoding="utf-8"), flags=re.S)
        out.append(dict(
            num=int(p.name[:2]),
            slug=p.stem.split("-post-", 1)[1],
            title=field(src, r'<h1 class="yt-post__title">(.*?)</h1>', "title", p.name),
            dek=field(src, r'<p class="yt-post__dek">(.*?)</p>', "dek", p.name),
            cat=field(src, r"<span data-yt-cat>(.*?)</span>", "category", p.name),
            date=field(src, r"<span data-yt-date>(.*?)</span>", "date", p.name),
            read=field(src, r"<span data-yt-read>(.*?)</span>", "read time", p.name),
        ))
    return sorted(out, key=lambda e: -e["num"])


def esc(s):
    return html.escape(s, quote=True)


def cards(es):
    if not es:
        return ('<p class="yt-wr-count">NOTHING PUBLISHED YET</p>')
    # No essay count above the list (Yash, 3 Nov 2026). The count line class
    # is kept only for the empty state above.
    rows = ['<ol class="yt-wr-cards">']
    for e in es:
        rows.append(
            '  <li><a class="yt-wr-card" href="%s%s" aria-label="%s">\n'
            '    <div class="yt-wr-card__cover">%s</div>\n'
            '    <div class="yt-wr-card__body">\n'
            '    <div class="yt-wr-card__top"><span class="yt-wr-card__cat" aria-hidden="true">%s</span>'
            '<span class="yt-wr-card__meta" aria-hidden="true">%s &middot; %s</span></div>\n'
            '    <h3 class="yt-wr-card__title">%s</h3>\n'
            '    <p class="yt-wr-card__dek">%s</p>\n'
            '    </div>\n'
            '  </a></li>' % (C.POST_ROUTE, e["slug"], esc("%s. %s, %s, %s" % (e["title"], e["cat"], e["date"], e["read"])),
                             covers.cover(e["slug"], e["cat"]), esc(e["cat"]),
                             esc(e["date"]), esc(e["read"]), esc(e["title"]), esc(e["dek"])))
    rows.append("</ol>")
    return "\n".join(rows)


def schema(es):
    doc = {"@context": "https://schema.org", "@graph": [{
        "@type": "ItemList", "@id": C.url("/writing") + "#essays", "name": "Essays by Yash Tulsyani",
        "numberOfItems": len(es),
        "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": e["title"],
                             "url": C.url(C.POST_ROUTE + e["slug"])} for i, e in enumerate(es)]}]}
    ld = json.dumps(doc, indent=2, ensure_ascii=False)
    return '<script type="application/ld+json">\n%s\n</script>' % (
        ld.replace("&", "\\u0026").replace("<", "\\u003c").replace(">", "\\u003e"))


def put(s, name, body):
    b, e = "<!-- %s:BEGIN -->" % name, "<!-- %s:END -->" % name
    if s.count(b) != 1 or s.count(e) != 1:
        sys.exit("24-writing.html: needs exactly one %s marker pair" % name)
    return re.sub(re.escape(b) + ".*?" + re.escape(e), lambda m: b + "\n" + body + "\n" + e, s, flags=re.S)


def main():
    es = essays()
    s = HUB.read_text(encoding="utf-8")
    s = put(s, "WRITING-CARDS", cards(es))
    s = put(s, "WRITING-SCHEMA", schema(es) if es else "")
    HUB.write_text(s, encoding="utf-8")
    print("writing hub: %d essay card(s)" % len(es))


if __name__ == "__main__":
    main()
