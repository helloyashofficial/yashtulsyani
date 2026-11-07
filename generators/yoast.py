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
    "what-the-impostor-phenomenon-is": dict(
        focus="impostor phenomenon",
        title="The impostor phenomenon: why it is not a syndrome",
        desc="The impostor phenomenon explained: what Clance and Imes described in 1978, the impostor cycle, what 62 studies found, and why it is not a diagnosis."),
    "what-the-research-says-about-love-languages": dict(
        focus="love languages",
        title="Love languages: what the research actually says",
        desc="Do love languages hold up? What studies found on one primary language, the five categories and matching partners, and the balanced diet idea instead."),
    "what-a-tesseract-is": dict(
        focus="tesseract",
        title="What a tesseract is: the four-dimensional cube explained",
        desc="What a tesseract is: the four-dimensional cube, how it is built from a point, the Victorian who named it, his coloured cubes, and what its images show."),
    "what-time-dilation-is": dict(
        focus="time dilation",
        title="Time dilation: why your head ages faster than your feet",
        desc="Time dilation explained: why moving clocks and lower clocks run slow, the experiments that measured it, Einstein's 1905 slip, and why GPS depends on it."),
    "what-spinoza-meant-by-hope-and-fear": dict(
        focus="Spinoza hope and fear",
        title="Spinoza on hope and fear: why they come together",
        desc="Spinoza on hope and fear: how he defined them, why he said there is no hope without fear, how fear breeds superstition, and his remedy of understanding."),
    "what-learned-helplessness-actually-showed": dict(
        focus="learned helplessness",
        title="Learned helplessness: what it showed and what changed",
        desc="Learned helplessness: what the 1960s experiments found, how it was applied to people, and why its discoverers later said the theory got it backward."),
    "what-the-demand-withdraw-pattern-is": dict(
        focus="demand-withdraw pattern",
        title="The demand-withdraw pattern: why it feeds itself",
        desc="The demand-withdraw pattern in couples: what it is, who ends up demanding, what a 74-study meta-analysis found, why it feeds itself, and what helps."),
    "what-physicists-mean-by-extra-dimensions": dict(
        focus="extra dimensions",
        title="Extra dimensions: what physicists mean, and how they search",
        desc="What physicists mean by extra dimensions: Kaluza-Klein, string theory, large extra dimensions, LHC searches, tabletop gravity tests, and the evidence."),
    "why-looking-at-the-sky-means-looking-into-the-past": dict(
        focus="looking back in time",
        title="Looking back in time: why the night sky shows the past",
        desc="Why looking at the sky means looking back in time: the speed of light, the light-year, the oldest light, lookback versus distance, and dead stars."),
    "what-aristotle-meant-by-the-three-kinds-of-friendship": dict(
        focus="Aristotle friendship",
        title="Aristotle on friendship: the three kinds, and why one lasts",
        desc="Aristotle on friendship, in his own words: utility, pleasure and the good, another self, how many friends, and the debate over the lesser kinds."),
    "what-the-spotlight-effect-is": dict(
        focus="spotlight effect",
        title="Spotlight effect: why others notice us less than we think",
        desc="The spotlight effect explained: the T-shirt study, the illusion of transparency, why we overestimate attention, what helps, and the limits."),
    "what-the-michelangelo-phenomenon-says": dict(
        focus="Michelangelo phenomenon",
        title="The Michelangelo phenomenon: how partners shape each other",
        desc="The Michelangelo phenomenon explained: how partners affirm each other's ideal selves, what the studies found, the Pygmalion problem, and the limits."),
    "what-mctaggart-meant-by-the-unreality-of-time": dict(
        focus="McTaggart unreality of time",
        title="McTaggart on the unreality of time: the A and B series",
        desc="McTaggart's 1908 argument for the unreality of time: the A and B series, the contradiction, the replies, the growing block, and relativity."),
    "what-entanglement-is": dict(
        focus="quantum entanglement",
        title="Quantum entanglement: what it is, and what it is not",
        desc="What quantum entanglement is: Einstein's objection, Bell's test, the 2022 Nobel experiments, why it cannot send messages, and why people are not entangled."),
    "what-epicurus-meant-by-pleasure": dict(
        focus="Epicurus pleasure",
        title="What Epicurus meant by pleasure: calm, not indulgence",
        desc="What Epicurus meant by pleasure, in his own words: the absence of pain and trouble, three kinds of desire, death as nothing to fear, and friendship."),
    "what-rumination-is": dict(
        focus="rumination",
        title="Rumination: why thinking it through can make things worse",
        desc="What rumination is and what the research found: the earthquake study, brooding versus reflection, abstract versus concrete thought, and what helps."),
    "what-your-partner-does-with-your-good-news": dict(
        focus="active constructive responding",
        title="Active constructive responding: what to do with good news",
        desc="Active constructive responding to a partner's good news: Gable's four response styles, what the studies found, and how tentative the evidence still is."),
    "what-flatland-teaches-about-the-fourth-dimension": dict(
        focus="Flatland fourth dimension",
        title="Flatland and the fourth dimension: what Abbott's novel shows",
        desc="What Abbott's Flatland (1884) teaches about the fourth dimension: the satire, the argument from analogy, the tesseract, and why it is not about time."),
    "why-time-has-a-direction": dict(
        focus="arrow of time",
        title="The arrow of time: why time has a direction",
        desc="Why time has a direction: time-symmetric laws, Eddington's arrow, Boltzmann's entropy, two classic objections, and the Past Hypothesis still debated."),
    "why-we-blame-the-people-we-love": dict(
        focus="Strawson resentment",
        title="Why we blame the people we love: Strawson on resentment",
        desc="Strawson's Freedom and Resentment, read closely: reactive attitudes, two kinds of excuse, the objective attitude, and what determinism would change."),
    "what-self-silencing-is": dict(
        focus="self-silencing",
        title="Self-silencing: what keeping the peace can cost",
        desc="What self-silencing is, how it is measured, what the research links it to, why it is not only a women's pattern, and when holding back is fine."),
    "what-repair-after-an-argument-actually-involves": dict(
        focus="repair after an argument",
        title="Repair after an argument: what the research actually shows",
        desc="Repair after an argument: most couples rebound, many disagreements never end, what makes an apology work, and where forgiveness stops helping."),
    "what-it-means-to-call-time-the-fourth-dimension": dict(
        focus="time as the fourth dimension",
        title="Time as the fourth dimension: what relativity actually says",
        desc="What it means to call time the fourth dimension: Minkowski's 1908 idea, why time is not just another direction, how it was measured, and what remains open."),
    "what-the-stoics-meant-by-what-is-up-to-us": dict(
        focus="what is up to us",
        title="What is up to us: Epictetus on control and other people",
        desc="What Epictetus meant by what is up to us, read from the Handbook itself, and what the distinction means, and misses, when the thing at stake is love."),
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
