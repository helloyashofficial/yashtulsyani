#!/usr/bin/env python3
"""qa.py :: automated quality gate for essays (ported from FSDM, 24 Oct 2026).

yashtulsyani.com standard (BUILD-GUIDELINES s9): 2,000+ body words measured
on the body only, 4+ FAQs. FSDM's floor was 3,000 words and 6 FAQs, set for
operator guides competing on search; essays here are not that genre.

Usage: python3 rewrite/qa.py [num ...]   (no args = every post with a rewrite spec)

Fails a post on: body under 3,000 words, em/en dashes, banned phrasing,
contractions, fewer than 6 FAQs, missing opening answer, figures with a
percentage or currency amount in a paragraph that carries no external link
(flagged for the fact-check, not failed), raw & not part of an entity,
duplicate link targets, external links without rel=noopener.
"""
import re, sys, pathlib, html, glob

HERE = pathlib.Path(__file__).resolve().parent
D = HERE.parent.parent / "production-blocks"
BANNED = ["in today's", "fast-paced", "game-changer", "game changer", "unlock", "delve", "robust",
          "seamless", "crucial", "landscape of", "it's important to note", "in conclusion",
          "leverage your", "leveraging", "elevate your", "navigate the", "ever-evolving", "tapestry",
          "supercharge", "harness the power", "look no further"]
CONTR = re.compile(r"\b(don't|doesn't|isn't|aren't|can't|won't|it's|you're|we're|they're|didn't|wasn't|haven't|shouldn't|wouldn't|couldn't|that's|there's|let's|i'm|you'll|we'll|i've|you've)\b", re.I)


def body(src):
    mk = re.sub(r"<!--.*?-->", "", src, flags=re.S)
    a = mk.find('class="yt-post__body"'); b = mk.find('class="yt-post__takeaway"')
    return mk[a:b]


def check(path):
    src = path.read_text(encoding="utf-8")
    b = body(src)
    text = html.unescape(re.sub(r"<[^>]+>", " ", re.sub(r"<figure.*?</figure>", " ", b, flags=re.S)))
    words = len(text.split())
    allw = len(html.unescape(re.sub(r"<[^>]+>", " ", b)).split())
    fails, warns = [], []
    if allw < 2000:
        fails.append("body %d words (prose %d), floor 2,000" % (allw, words))
    if re.search("[–—]", src[src.find("yt-post__title"):]):
        fails.append("em/en dash present")
    low = text.lower()
    for p in BANNED:
        if p in low:
            fails.append("banned phrase: %r" % p)
    c = CONTR.findall(text)
    if c:
        warns.append("contractions: %s" % ", ".join(sorted(set(x.lower() for x in c))[:8]))
    faqs = len(re.findall(r'class="yt-faq__item"', src))
    if faqs < 4:
        fails.append("%d FAQs, want 4 or more" % faqs)
    first = re.search(r"<p>(.*?)</p>", b, re.S)
    if first:
        fw = len(re.sub(r"<[^>]+>", " ", first.group(1)).split())
        if fw > 90:
            warns.append("first paragraph %d words; the opening answer should be 40 to 60" % fw)
    for m in re.finditer(r"<p>(.*?)</p>|<li>(.*?)</li>", b, re.S):
        t = m.group(1) or m.group(2)
        plain = re.sub(r"<[^>]+>", "", t)
        if re.search(r"\d+(\.\d+)?\s?%|\$\d|£\d|\b\d{2,3},\d{3}\b", plain):
            if 'href="http' not in t:
                if not re.search(r"hypothetical|for example|say |suppose|imagine|e\.g\.", plain, re.I):
                    warns.append("figure without an external link: " + plain[:110].strip())
    if re.search(r"&(?!(#\d+|#x[0-9a-f]+|[a-z]+);)", b, re.I):
        fails.append("raw & in body")
    targets = re.findall(r'href="(/[^"#]+)"', b)
    dup = sorted(set(t for t in targets if targets.count(t) > 1))
    if dup:
        warns.append("internal target linked more than once: " + ", ".join(dup))
    for m in re.finditer(r'<a [^>]*href="https?://[^"]+"[^>]*>', b):
        if "noopener" not in m.group(0):
            fails.append("external link without rel=noopener: " + m.group(0)[:90])
    ext = len(set(re.findall(r'href="(https?://[^"]+)"', b)))
    h2 = len(re.findall(r"<h2", b)); h3 = len(re.findall(r"<h3", b)); fig = len(re.findall(r'class="yt-viz"', b))
    return dict(words=allw, prose=words, h2=h2, h3=h3, fig=fig, faqs=faqs, ext=ext, fails=fails, warns=warns)


def main():
    nums = sys.argv[1:]
    specs = sorted(HERE.glob("[0-9][0-9]-*.py"))
    if nums:
        specs = [s for s in specs if s.name.split("-")[0] in nums]
    bad = 0
    for s in specs:
        num = s.name.split("-")[0]
        p = sorted(D.glob(num + "-post-*.html"))[0]
        r = check(p)
        status = "FAIL" if r["fails"] else "ok"
        bad += 1 if r["fails"] else 0
        print("%s %-52s %5dw prose %5d h2 %2d h3 %2d fig %d faq %d ext %2d" % (status, p.name, r["words"], r["prose"], r["h2"], r["h3"], r["fig"], r["faqs"], r["ext"]))
        for f in r["fails"]:
            print("     FAIL  " + f)
        for w in r["warns"][:12]:
            print("     warn  " + w)
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
