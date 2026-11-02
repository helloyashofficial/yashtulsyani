#!/usr/bin/env python3
"""
yoast.py --- the single source of truth for Yoast fields, and the gate on them.

Ported from FSDM (24 Oct 2026) with its data replaced. Paste each entry into
the page's Yoast panel by hand; the build also writes it into each block's
header comment so it travels with the file.

check() enforces, for every page and essay:
  - SEO title at most 60 characters
  - meta description 120 to 155 characters (FSDM enforced only the maximum)
  - every focus-keyphrase word over 2 letters present in both
  - no two URLs share a focus keyphrase (FSDM caught one cannibalising pair)
  - the SEO title differs from the page's h1 (the h1 is for someone who has
    landed; the title is for someone scanning ten results)
"""
import re, sys, html
import ytconf as C

# Essays, keyed by slug. Empty until the first essay is written.
YOAST = {
    "why-reassurance-is-never-enough": dict(
        focus="reassurance seeking",
        title="Reassurance seeking: why it is never enough, and what helps",
        desc="Why reassurance seeking calms anxiety for an hour and then makes it worse, what the research shows about it, and what to do instead in a relationship."),
    "what-the-observer-effect-actually-says": dict(
        focus="observer effect",
        title="The observer effect: what quantum physics actually says",
        desc="The observer effect, explained from the sources: the observer is a detector, not a mind, decoherence is everywhere, and the real puzzle is still open."),
    "what-attachment-styles-actually-measure": dict(
        focus="attachment styles",
        title="Attachment styles: what the research actually measures",
        desc="Attachment styles from the original studies: two dimensions, not types, weak links to childhood, and scores that shift by relationship and over time."),
}

# Pages, keyed by block file.
PAGES = {
    "02-home.html": dict(
        focus="Yash Tulsyani",
        title="Yash Tulsyani | Essays and books on love and attention",
        desc="Yash Tulsyani writes about relationships, insecurity and the physics we borrow to describe them, with a strict line between the literal and the metaphor."),
    "25-about.html": dict(
        focus="about Yash Tulsyani",
        title="About Yash Tulsyani | How he thinks and what he writes",
        desc="About Yash Tulsyani: four habits of mind, the one question under all his writing, where the physics stops, and why the marketing lives on another site."),
    "23-work.html": dict(
        focus="organic discoverability",
        title="Work | Organic discoverability for software companies",
        desc="The profession behind the writing: organic discoverability for software companies, from topical architecture to honest measurement."),
    "24-writing.html": dict(
        focus="essays on relationships and physics",
        title="Writing | Essays on relationships, physics and time",
        desc="Essays on relationships, physics, psychology and time, each labelled by register so a metaphor never borrows the authority of the physics."),
    "20-books.html": dict(
        focus="Yash Tulsyani books",
        title="Books by Yash Tulsyani | Two unpublished manuscripts",
        desc="Two unpublished books by Yash Tulsyani on love, insecurity and attention, using quantum ideas as a vocabulary rather than as a scientific claim."),
    "21-book-afraid-of.html": dict(
        focus="The Thing You Were Afraid Of",
        title="The Thing You Were Afraid Of | A quantum philosophy of love",
        desc="The Thing You Were Afraid Of: an unpublished book on how insecurity and reassurance turn a feared outcome into a pattern, and how to interrupt it."),
    "22-book-nobody-has-to-shrink.html": dict(
        focus="Nobody Has to Shrink",
        title="Nobody Has to Shrink | A handbook for secure love",
        desc="Nobody Has to Shrink: an unpublished handbook on neglect, self-worth and emotional independence, with quantum philosophy sections and a workbook."),
    "28-reading-provisional.html": dict(
        focus="reading list psychology physics philosophy",
        title="Reading list | Psychology, physics and philosophy",
        desc="A reading list across psychology, physics and philosophy, held to four tests, with a line on why each entry is there rather than what it says."),
    "29-notes-provisional.html": dict(
        focus="notes on new research",
        title="Notes | What new research shows, and what it does not",
        desc="Notes on new research in psychology, physics and philosophy, separating what a finding shows from what it is reported as showing."),
    "26-now.html": dict(
        focus="what Yash Tulsyani is doing now",
        title="Now | What Yash Tulsyani is doing this month",
        desc="What Yash Tulsyani is doing now: two unpublished manuscripts, the first essays, one site becoming two, and the questions still open."),
    "27-contact.html": dict(
        focus="contact Yash Tulsyani",
        title="Contact | Write to Yash Tulsyani about the books",
        desc="How to contact Yash Tulsyani: one email address, read personally. Disagreement and corrections on the physics are the most welcome messages."),
}

# Private pages: noindex, and no Yoast copy needed beyond that.
NOINDEX = set(C.PRIVATE)


def h1_of(name):
    p = C.BLOCKS / name
    if not name:
        return None
    if not p.exists():
        return None
    src = re.sub(r"<!--.*?-->", "", p.read_text(encoding="utf-8"), flags=re.S)
    m = re.search(r"<h1[^>]*>(.*?)</h1>", src, re.S)
    return html.unescape(re.sub(r"<[^>]+>", "", m.group(1))).strip() if m else None


def check():
    bad, seen = [], {}
    entries = [("page " + k, k, v) for k, v in PAGES.items()] + \
              [("essay " + k, next((q.name for q in C.BLOCKS.glob("*-post-%s.html" % k)), ""), v)
               for k, v in YOAST.items()]
    for label, name, d in entries:
        t, ds, f = d["title"], d["desc"], d["focus"]
        if len(t) > 60:
            bad.append("%s: title %d chars, max 60" % (label, len(t)))
        if not 120 <= len(ds) <= 155:
            bad.append("%s: description %d chars, want 120 to 155" % (label, len(ds)))
        for w in re.findall(r"[A-Za-z']+", f):
            if len(w) > 2:
                if w.lower() not in t.lower():
                    bad.append("%s: focus word %r missing from title" % (label, w))
                if w.lower() not in ds.lower():
                    bad.append("%s: focus word %r missing from description" % (label, w))
        key = f.lower()
        if key in seen:
            bad.append("%s: focus keyphrase %r already used by %s" % (label, f, seen[key]))
        seen[key] = label
        h1 = h1_of(name)
        if h1:
            if h1.lower() == t.lower():
                bad.append("%s: SEO title is identical to the h1" % label)
    for name in C.PAGES:
        if name not in PAGES:
            bad.append("page %s has no Yoast entry" % name)
    return bad


def stamp():
    """Write each page's Yoast fields into its header comment, between
    YOAST:BEGIN and YOAST:END, so the values travel with the file."""
    for name, d in PAGES.items():
        p = C.BLOCKS / name
        if not p.exists():
            continue
        s = p.read_text(encoding="utf-8")
        if s.count("     YOAST:BEGIN") != 1:
            sys.exit("%s: needs exactly one YOAST:BEGIN line in its header comment" % name)
        body = ("     YOAST:BEGIN  (generated by generators/yoast.py; edit there)\n"
                "     URL             : %s\n"
                "     FOCUS KEYPHRASE : %s\n"
                "     SEO TITLE       : %s  [%d chars]\n"
                "     META DESCRIPTION: %s  [%d chars]\n"
                "     YOAST:END" % (C.PAGES[name], d["focus"], d["title"], len(d["title"]),
                                   d["desc"], len(d["desc"])))
        s2, n = re.subn(r"     YOAST:BEGIN.*?     YOAST:END", lambda m: body, s, count=1, flags=re.S)
        assert n == 1, name
        p.write_text(s2, encoding="utf-8")


if __name__ == "__main__":
    if "--stamp" in sys.argv:
        stamp()
    problems = check()
    for p in problems:
        print("  FAIL  " + p)
    if problems:
        sys.exit(1)
    print("yoast: %d essays, %d pages, all valid" % (len(YOAST), len(PAGES)))
