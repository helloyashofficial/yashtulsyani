#!/usr/bin/env python3
"""
newpost.py --- write a new essay block for yashtulsyani.com.

Ported from FSDM's newpost.py (24 Oct 2026). The approach is unchanged: an
EXISTING block is the template and only its content is replaced, so there is
no second definition of the layout to drift out of step. Until the first real
essay exists, the template is generators/templates/post-template.html; after
that, pass template="self" to rewrite an essay in place, or a path.

Usage, from a spec file in generators/rewrite/NN-<slug>.py:

    import newpost, postkit as K
    newpost.build(dict(
        slug="...", num=40, cat="Relationships", read="auto",
        title="...", dek="...", takeaway="...",
        sections=[("Heading", ["para", "H3:sub", "LIST:a|b", "HTML:" + K.table(...)]), ...],
        note=["para", ...],                       # the author's note above the FAQ
        faqs=[("q", "a"), ...],                   # 4 or more; they feed FAQPage schema
        related=[("slug", "Exact H1", "Cluster"), ...],
    ))

Changes from the FSDM version, each for a reason:
- Settings come from ytconf.py, so the cluster list exists once.
- Rule 3 is "no dead ends" (book page, reading list, or a cross-cluster
  essay), because this site has no services or tools.
- Every structural substitution is asserted. FSDM's version used bare
  re.sub calls, which return the input unchanged when the pattern misses:
  the exact failure its own spec warns about in section l.
- A missing Yoast entry now stops the build instead of being skipped.
"""

import re, pathlib, sys, html, json
import ytconf as C

D = C.BLOCKS
TEMPLATE = C.TEMPLATES / "post-template.html"


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def slugify(s):
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")


def must(pattern, repl, text, label, flags=re.S):
    """re.sub that refuses to report success when it matched nothing."""
    out, n = re.subn(pattern, repl, text, count=1, flags=flags)
    if n != 1:
        sys.exit("newpost: anchor for %s matched %d times; template and "
                 "generator disagree, nothing written" % (label, n))
    return out


def render_body(sections):
    out = []
    for title, blocks in sections:
        sid = slugify(title)
        out.append('        <h2 id="%s">%s</h2>' % (sid, esc(title)))
        for b in blocks:
            if b.startswith("HTML:"):
                out.append("        " + b[5:])
            elif b.startswith("H3:"):
                out.append('        <h3 id="%s">%s</h3>' % (sid + "-" + slugify(b[3:])[:48], b[3:]))
            elif b.startswith("OL:"):
                out.append("        <ol>")
                for item in b[3:].split("|"):
                    out.append("          <li>%s</li>" % item)
                out.append("        </ol>")
            elif b.startswith("LIST:"):
                out.append("        <ul>")
                for item in b[5:].split("|"):
                    out.append("          <li>%s</li>" % item)
                out.append("        </ul>")
            else:
                out.append("        <p>%s</p>" % b)
    return "\n".join(out)


def render_toc(sections):
    return "\n".join('            <li><a href="#%s">%s</a></li>' % (slugify(t), esc(t))
                     for t, _ in sections)


def render_faqs(faqs):
    return "\n".join('      <details class="yt-faq__item">\n'
                     '        <summary>%s</summary>\n'
                     '        <div class="yt-faq__a">%s</div>\n'
                     '      </details>' % (esc(q), a) for q, a in faqs)


def render_note(paras):
    return "\n".join("      <p>%s</p>" % x for x in paras)


def render_related(related):
    return "\n".join(
        '          <a class="yt-post__rel" href="%s%s" aria-label="%s">\n'
        '            <span class="yt-post__rel-cat" aria-hidden="true">%s</span>\n'
        '            <span class="yt-post__rel-title">%s</span>\n'
        '          </a>' % (C.POST_ROUTE, slug, esc(title), esc(cat), esc(title))
        for slug, title, cat in related)


def existing_categories():
    cats = {}
    for p in D.glob("[0-9][0-9]-post-*.html"):
        m = re.search(r"data-yt-cat>([^<]+)", p.read_text(encoding="utf-8"))
        if m:
            cats[p.stem.split("-post-", 1)[1]] = m.group(1).strip()
    return cats


def check_rules(spec, body_html):
    """Rules 1 to 3, asserted before anything is written. Rule 4 is
    check-graph.py's job, once other essays link here."""
    route = re.escape(C.POST_ROUTE)
    body_links = set(re.findall(r'href="%s([a-z0-9-]+)/?"' % route, body_html))
    body_links.discard(spec["slug"])
    pillar = C.CLUSTERS.get(spec["cat"])
    problems = []
    if spec["cat"] not in C.CLUSTERS:
        problems.append("category %r is not one of the five clusters in ytconf.py" % spec["cat"])
    if pillar:
        if spec["slug"] != pillar:
            if pillar not in body_links:
                problems.append("rule 1: no in-body link up to the pillar %s" % pillar)
    siblings = [s for s in body_links if s != pillar]
    cats = existing_categories()
    if cats:
        if len(siblings) < 1:
            problems.append("rule 2: %d lateral essay link(s) in the body, wants 2-3" % len(siblings))
    exits = [h for h in re.findall(r'href="(/[^"#?]*)"', body_html)
             if h.startswith(C.RULE3_PREFIXES)]
    cross = [s for s in body_links if cats.get(s, spec["cat"]) != spec["cat"]]
    if not exits:
        if not cross:
            problems.append("rule 3: no exit to a book page, the reading list or "
                            "an essay in another cluster")
    if len(spec.get("faqs", [])) < 4:
        problems.append("%d FAQs; the standard is 4 or more" % len(spec.get("faqs", [])))
    return problems


def build(spec, write=True):
    tpl = spec.get("template")
    if tpl == "self":
        hits = sorted(D.glob("%d-post-%s.html" % (spec["num"], spec["slug"])))
        if not hits:
            sys.exit("no existing block for %s" % spec["slug"])
        tpl = hits[0]
    src = (pathlib.Path(tpl) if tpl else TEMPLATE).read_text(encoding="utf-8")

    body = render_body(spec["sections"])
    if spec.get("read") in (None, "auto"):
        words = len(re.sub(r"<[^>]+>", " ", body).split())
        spec["read"] = "%d min" % max(1, round(words / 225.0))
    problems = check_rules(spec, body)
    if problems:
        print("RULES NOT SATISFIED for %s:" % spec["slug"])
        for p in problems:
            print("  " + p)
        sys.exit(1)

    import yoast as Y
    if spec["slug"] not in Y.YOAST:
        sys.exit("no YOAST entry for %s in yoast.py; add it before building" % spec["slug"])
    d = Y.YOAST[spec["slug"]]

    out = src
    # Header comment. Two spaces either side of the middot: FSDM's
    # single-space pattern matched nothing and six posts shipped labelled
    # with the template's slug.
    out = must(r"(ESSAY\s{2}·\s{2})[a-z0-9-]+", lambda m: m.group(1) + spec["slug"], out, "header slug")
    # Publication date, baked so the /writing card and the essay agree before
    # any script runs. Same format the essay's script upgrades to: 02 Nov 2026.
    if not spec.get("date"):
        sys.exit("spec has no date: add date=\"YYYY-MM-DD\" (the day it is published)")
    import datetime
    pubd = datetime.date.fromisoformat(spec["date"])
    shown = "%02d %s %d" % (pubd.day, ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"][pubd.month - 1], pubd.year)
    out = must(r"(<span data-yt-date>)[^<]*(</span>)", lambda m: m.group(1) + shown + m.group(2), out, "date")
    import covers
    out = must(r'(<div class="yt-post__cover">).*?(</div>)', lambda m: m.group(1) + covers.cover(spec["slug"], spec["cat"]) + m.group(2), out, "cover")
    tail = ("     Regenerate with generators/%s\n"
            "     FOCUS KEYPHRASE : %s\n"
            "     SEO TITLE       : %s  [%d chars]\n"
            "     META DESCRIPTION: %s  [%d chars]\n"
            "     SLUG            : %s%s\n"
            % (spec.get("gen", "newpost.py"), d["focus"], d["title"], len(d["title"]),
               d["desc"], len(d["desc"]), C.POST_ROUTE, spec["slug"]))
    out = must(r"     Regenerate with .*?(?=     =+ -->)", lambda m: tail, out, "header yoast")

    out = must(r'(<span data-yt-cat>)[^<]*(</span>)',
               lambda m: m.group(1) + esc(spec["cat"]) + m.group(2), out, "category")
    out = must(r'(<span data-yt-read>)[^<]*(</span>)',
               lambda m: m.group(1) + spec["read"] + " read" + m.group(2), out, "read time")
    out = must(r'(<h1 class="yt-post__title">).*?(</h1>)',
               lambda m: m.group(1) + esc(spec["title"]) + m.group(2), out, "title")
    out = must(r'(<p class="yt-post__dek">).*?(</p>)',
               lambda m: m.group(1) + esc(spec["dek"]) + m.group(2), out, "dek")
    out = must(r'(<div class="yt-post__toc-label">[^<]*</div>\s*<ol>).*?(</ol>)',
               lambda m: m.group(1) + "\n" + render_toc(spec["sections"]) + "\n          " + m.group(2),
               out, "contents")
    # The takeaway sits INSIDE .yt-post__body; the body ends where it begins.
    out = must(r'(<div class="yt-post__body">).*?(\n\s*<div class="yt-post__takeaway")',
               lambda m: m.group(1) + "\n" + body + "\n" + m.group(2), out, "body")
    out = must(r'(<div class="yt-post__takeaway-label">[^<]*</div>\s*<p>).*?(</p>)',
               lambda m: m.group(1) + esc(spec["takeaway"]) + m.group(2), out, "takeaway")
    out = must(r'(Author\'s note</div>).*?(\n\s*</div>\s*\n\s*<section class="yt-faq")',
               lambda m: m.group(1) + "\n" + render_note(spec.get("note", [])) + m.group(2),
               out, "author note")
    out = must(r'(<h2 class="yt-faq__h" id="faq">[^<]*</h2>).*?(\n\s*</section>)',
               lambda m: m.group(1) + "\n" + render_faqs(spec["faqs"]) + m.group(2), out, "faqs")
    out = must(r'(<div class="yt-post__related">).*?(\n\s*</div>)',
               lambda m: m.group(1) + "\n" + render_related(spec["related"]) + m.group(2),
               out, "related")

    # Schema: FAQPage always, HowTo optional. Yoast owns Article, WebPage
    # and BreadcrumbList; these fragment @ids never collide with them.
    page = C.url(C.POST_ROUTE + spec["slug"])
    plain = lambda x: html.unescape(re.sub(r"<[^>]+>", "", x)).strip()
    graph = [{"@type": "FAQPage", "@id": page + "#faq", "mainEntityOfPage": page,
              "mainEntity": [{"@type": "Question", "name": plain(q),
                              "acceptedAnswer": {"@type": "Answer", "text": plain(a)}}
                             for q, a in spec["faqs"]]}]
    if spec.get("howto"):
        hname, hsteps = spec["howto"]
        assert len(hsteps) >= 3, "HowTo needs 3 or more steps"
        graph.append({"@type": "HowTo", "@id": page + "#howto", "name": plain(hname),
                      "mainEntityOfPage": page,
                      "step": [{"@type": "HowToStep", "position": i + 1, "name": plain(n), "text": plain(t)}
                               for i, (n, t) in enumerate(hsteps)]})
    ld = json.dumps({"@context": "https://schema.org", "@graph": graph}, indent=2, ensure_ascii=False)
    ld = ld.replace("&", "\\u0026").replace("<", "\\u003c").replace(">", "\\u003e")
    out = must(r'<script type="application/ld\+json">.*?</script>',
               lambda m: '<script type="application/ld+json">\n' + ld + "\n</script>", out, "schema")

    dest = D / ("%d-post-%s.html" % (spec["num"], spec["slug"]))
    mk = re.sub(r"<script.*?</script>", "", re.sub(r"<!--.*?-->", "", out, flags=re.S), flags=re.S)
    b = mk[mk.find("yt-post__body"):mk.find("yt-post__takeaway")]
    stats = "%s  %d body words, %d figures, %d sections" % (
        dest.name, len(re.sub(r"<[^>]+>", " ", b).split()),
        len(re.findall(r'class="yt-viz[ "]', out)), len(spec["sections"]))
    if write:
        dest.write_text(out, encoding="utf-8")
        print(stats)
    return out


if __name__ == "__main__":
    print(__doc__)
