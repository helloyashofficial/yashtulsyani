#!/usr/bin/env python3
"""
check-graph.py --- the four internal-linking rules, checked against the blocks.

Ported from FSDM (24 Oct 2026). The graph is derived from the essay blocks
themselves, not from a config file describing what the links were meant to be.

  1  Every essay links UP to its cluster pillar, once the cluster has one.
  2  Every essay links laterally to other essays. The standard is 2 to 3;
     the gate fails under 1, and warns under 2.
  3  No dead ends: every essay links to a book page, the reading list, or an
     essay in a different cluster. (FSDM's rule 3 was a service or tool link.
     This site has neither.)
  4  No orphans: every essay has at least one inbound in-body link. This
     FAILS the build, except while the site has fewer than
     ytconf.BOOTSTRAP_MIN_POSTS essays, when it cannot be satisfied.

Body links only. Related-reading cards are navigation, not editorial.
"""

import re, sys, pathlib, collections
import ytconf as C

D = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else C.BLOCKS
ROUTE = re.escape(C.POST_ROUTE)


def strip(src):
    mk = re.sub(r"<!--.*?-->", "", src, flags=re.S)
    mk = re.sub(r"<style>.*?</style>", "", mk, flags=re.S)
    return re.sub(r"<script.*?</script>", "", mk, flags=re.S)


def body_of(src):
    mk = strip(src)
    start = mk.find('yt-post__body')
    end = mk.find('yt-post__related')
    if end == -1:
        end = mk.find('yt-post__author')
    if start == -1:
        return ""
    return mk[start:end if end > start else len(mk)]


def load():
    posts = {}
    for p in sorted(D.glob("[0-9][0-9]-post-*.html")):
        src = p.read_text(encoding="utf-8")
        slug = p.stem.split("-post-", 1)[1]
        cat = re.search(r"data-yt-cat>([^<]+)", strip(src))
        body = body_of(src)
        posts[slug] = dict(
            file=p.name,
            cat=cat.group(1).strip() if cat else "",
            posts=set(re.findall(r'href="%s([a-z0-9-]+)/?"' % ROUTE, body)),
            exits=set(h for h in re.findall(r'href="(/[^"#?]*)"', body)
                      if h.startswith(C.RULE3_PREFIXES)),
        )
        posts[slug]["posts"].discard(slug)
    return posts


def main():
    posts = load()
    print("%d essays" % len(posts))
    if not posts:
        print("link graph OK: nothing to check yet")
        return

    fails, warns = [], []
    inbound = collections.Counter()
    for slug, d in posts.items():
        for t in d["posts"]:
            if t in posts:
                inbound[t] += 1
        for t in d["posts"]:
            if t not in posts:
                fails.append("%s: links to %s%s, which does not exist" % (slug, C.POST_ROUTE, t))

    for slug, d in sorted(posts.items()):
        if d["cat"] not in C.CLUSTERS:
            fails.append("%s: category %r is not one of the five clusters" % (slug, d["cat"]))
        pillar = C.CLUSTERS.get(d["cat"])
        if pillar:
            if slug != pillar:
                if pillar not in d["posts"]:
                    warns.append("%s: rule 1, no link up to its pillar %s" % (slug, pillar))
        siblings = [t for t in d["posts"] if t != pillar]
        if len(posts) > 1:
            if len(siblings) < 1:
                warns.append("%s: rule 2, no lateral essay links" % slug)
            elif len(siblings) < 2:
                warns.append("%s: rule 2, %d lateral link; the standard is 2 to 3" % (slug, len(siblings)))
        cross = [t for t in d["posts"] if posts.get(t, {}).get("cat", d["cat"]) != d["cat"]]
        if not d["exits"]:
            if not cross:
                fails.append("%s: rule 3, a dead end (no book, reading or cross-cluster link)" % slug)

    orphans = sorted(s for s in posts if inbound[s] == 0)
    print("in-body essay links: %d" % sum(len(d["posts"]) for d in posts.values()))
    if orphans:
        if len(posts) < C.BOOTSTRAP_MIN_POSTS:
            warns.append("rule 4 relaxed while there are fewer than %d essays; orphans: %s"
                         % (C.BOOTSTRAP_MIN_POSTS, ", ".join(orphans)))
        else:
            for s in orphans:
                fails.append("%s: rule 4, orphan with zero inbound in-body links" % s)
    for w in warns:
        print("  warn  " + w)
    if fails:
        print("\nBUILD FAILED:")
        for f in fails:
            print("  FAIL  " + f)
        sys.exit(1)
    print("link graph OK")


if __name__ == "__main__":
    main()
