#!/usr/bin/env python3
"""
verify.py --- the build gates, rebuilt after the workspace was lost.

The surviving copy of this file predated every check added during the session.
Each gate below exists because something shipped broken:

  hardening         A stray middot in block JS was mangled by WordPress.
  control_chars     content:'\\2212' written in a NORMAL Python string is an
                    octal escape, so it emitted U+0091 and the FAQ accordion
                    rendered a tofu box. The JS-only non-ASCII check could not
                    see it, because the corruption was in CSS.
  json_ld           A bare & inside a script is invalid. Author names carry
                    them, so JSON-LD must escape as \\u0026.
  js_syntax         node --check over every script block.
  class_coverage    Post styling lives in the sidebar, so a class a post uses
                    and the sidebar lacks renders unstyled with no error.
  unpinned_headings Kadence colours headings with a value that does not flip,
                    so a heading with no colour of its own vanishes in dark
                    mode. This shipped three times before becoming a gate.
  shortcut_range    The homepage advertised shortcuts 1-9 while the sidebar
                    bound 1-8.
  now_freshness     /now promises a refresh every 4-6 weeks and then carries a
                    date. A stale date advertises neglect. Here it also fails
                    when the stamp is more than 3 months older than today.

Added for yashtulsyani.com when this was ported (24 Oct 2026), carried over
from the site's own earlier verify.py:

  logical_ops       zero && and zero || in any non-JSON-LD script. FSDM only
                    gated these in its tool and widget generators, so a hand
                    edited page block could ship one. WordPress entity-encodes
                    the ampersand and the script dies.
  h1_count          the sidebar carries no h1; every other block exactly one.
  em_dash           no em-dash in markup, styles or scripts (house style).
  tag_balance       non-void tags balance once scripts and comments are out.

The blocks are the source of truth now. This validates them as they are; it
does not regenerate anything.
"""

import re, sys, json, subprocess, pathlib, tempfile

fails = []


def blocks_of(src):
    """Script contents, with HTML comments masked FIRST.

    12-resources.html documents itself with the words "<script> block" in its
    header comment. Locating scripts before masking comments opened a false
    span that swallowed the entire file and silently disabled the checks.
    """
    masked = re.sub(r"<!--.*?-->", lambda m: " " * len(m.group(0)), src, flags=re.S)
    return re.findall(r"<script(?![^>]*ld\+json)[^>]*>(.*?)</script>", masked, re.S)


def styles_of(src):
    return "\n".join(re.findall(r"<style>(.*?)</style>", src, re.S))


def markup_of(src):
    s = re.sub(r"<!--.*?-->", "", src, flags=re.S)
    s = re.sub(r"<style>.*?</style>", "", s, flags=re.S)
    return re.sub(r"<script.*?</script>", "", s, flags=re.S)


def check(path):
    src = path.read_text(encoding="utf-8")
    name = path.name
    js_blocks = blocks_of(src)

    for i, b in enumerate(js_blocks):
        bad = sorted({c for c in b if ord(c) > 127})
        if bad:
            fails.append("%s: JS block %d non-ASCII %s" % (name, i, bad))

    m = re.search(r"[\u0080-\u009f]", src)
    if m:
        fails.append("%s: control character U+%04X at offset %d"
                     % (name, ord(m.group(0)), m.start()))

    for i, b in enumerate(re.findall(
            r'<script type="application/ld\+json">(.*?)</script>', src, re.S)):
        if "&" in b:
            fails.append("%s: JSON-LD %d raw ampersand" % (name, i))
        try:
            json.loads(b)
        except Exception as e:
            fails.append("%s: JSON-LD %d does not parse: %s" % (name, i, e))

    # CSS brace balance. A stray "}" in the sidebar silently dropped the rule
    # after it (found Oct 2026, when that rule was the post widgets' first).
    for i, st in enumerate(re.findall(r"<style>(.*?)</style>", src, re.S)):
        st = re.sub(r"/\*.*?\*/", "", st, flags=re.S)
        d = stray = 0
        for ch in st:
            if ch == "{":
                d += 1
            elif ch == "}":
                d -= 1
                if d < 0:
                    stray += 1
                    d = 0
        if stray or d:
            fails.append("%s: <style> %d unbalanced braces (stray %d, unclosed %d)" % (name, i, stray, d))

    for i, b in enumerate(js_blocks):
        if "&&" in b:
            fails.append("%s: JS block %d contains &&" % (name, i))
        if "||" in b:
            fails.append("%s: JS block %d contains ||" % (name, i))

    mk = markup_of(src)
    h1 = len(re.findall(r"<h1[ >]", mk))
    want = 0 if name == "01-sidebar.html" else 1
    if h1 != want:
        fails.append("%s: %d h1, expected %d" % (name, h1, want))

    nocomment = re.sub(r"<!--.*?-->", "", src, flags=re.S)
    nocomment = re.sub(r"/\*.*?\*/", "", nocomment, flags=re.S)
    if "\u2014" in nocomment:
        fails.append("%s: %d em-dash(es) outside comments" % (name, nocomment.count("\u2014")))

    unclosed, stray = tag_balance(re.sub(r"<style>.*?</style>", "", mk, flags=re.S))
    if unclosed:
        fails.append("%s: unclosed tags %s" % (name, unclosed[:6]))
    if stray:
        fails.append("%s: stray closing tags %s" % (name, stray[:6]))

    if js_blocks:
        with tempfile.NamedTemporaryFile("w", suffix=".js", delete=False) as f:
            f.write("\n".join(js_blocks))
            p = f.name
        r = subprocess.run(["node", "--check", p], capture_output=True, text=True)
        if r.returncode != 0:
            tail = r.stderr.strip().splitlines()[-1:] or ["unknown"]
            fails.append("%s: node --check failed :: %s" % (name, tail))


VOID = {"area", "base", "br", "circle", "col", "ellipse", "embed", "hr", "img",
        "input", "line", "link", "meta", "param", "path", "polygon", "polyline",
        "rect", "source", "stop", "track", "use", "wbr"}


def tag_balance(html):
    stack, stray = [], []
    for close, tag, selfc in re.findall(r"<(/?)([a-zA-Z][a-zA-Z0-9]*)[^>]*?(/?)>", html):
        t = tag.lower()
        if t in VOID:
            continue
        if selfc == "/":
            continue
        if close:
            if stack:
                if stack[-1] == t:
                    stack.pop()
                    continue
            stray.append(t)
            continue
        stack.append(t)
    return stack, stray


def class_coverage(files):
    side = [p for p in files if p.name == "01-sidebar.html"]
    if not side:
        return []
    css = styles_of(side[0].read_text(encoding="utf-8"))
    defined = set(re.findall(r"\.(yt-[a-z0-9_-]+)", css))
    out = []
    for p in files:
        if not re.match(r"\d\d-post-", p.name):
            continue
        mk = markup_of(p.read_text(encoding="utf-8"))
        used = set()
        for m in re.finditer(r'class="([^"]+)"', mk):
            for c in m.group(1).split():
                if c.startswith("yt-"):
                    used.add(c)
        for c in sorted(used - defined):
            out.append("%s: uses .%s, which the sidebar does not define" % (p.name, c))
    return out


def unpinned_headings(files):
    side = [p for p in files if p.name == "01-sidebar.html"]
    side_css = styles_of(side[0].read_text(encoding="utf-8")) if side else ""
    out = []
    for p in files:
        src = p.read_text(encoding="utf-8")
        css = styles_of(src) + side_css
        mk = markup_of(src)
        used = set()
        for m in re.finditer(r'<h[1-4][^>]*class="([^"]+)"', mk):
            for c in m.group(1).split():
                if c.startswith("yt-"):
                    used.add(c)
        for c in sorted(used):
            rules = re.findall(r"([^{}]*\.%s[^{]*)\{([^}]*)\}" % re.escape(c), css)
            if not rules:
                out.append("%s: heading class .%s has no CSS rule at all" % (p.name, c))
            elif not any("color:" in b for _, b in rules):
                out.append("%s: heading class .%s never sets a colour, so it "
                           "disappears in dark mode" % (p.name, c))
    return out


def shortcut_range(files):
    side = [p for p in files if p.name == "01-sidebar.html"]
    if not side:
        return []
    bound = sorted(set(re.findall(r'data-shortcut="(\d)"',
                                  side[0].read_text(encoding="utf-8"))))
    if not bound:
        return []
    top = max(bound)
    out = []
    for p in files:
        src = re.sub(r"<!--.*?-->", "", p.read_text(encoding="utf-8"), flags=re.S)
        for m in re.finditer(
                r"keyboard shortcuts\s*<strong>1\s*\u2192\s*(\d)</strong>", src):
            if m.group(1) != top:
                out.append("%s: advertises shortcuts 1 to %s but the sidebar "
                           "binds only 1 to %s" % (p.name, m.group(1), top))
    return out


def now_freshness(files):
    MON = {m: i + 1 for i, m in enumerate(
        ["jan", "feb", "mar", "apr", "may", "jun",
         "jul", "aug", "sep", "oct", "nov", "dec"])}

    def val(month, year):
        return int(year) * 12 + MON[month[:3].lower()]

    out = []
    for p in files:
        if not p.name.endswith("-now.html"):
            continue
        src = re.sub(r"<!--.*?-->", "", p.read_text(encoding="utf-8"), flags=re.S)
        stamp = re.search(r'yt-now__updated">Updated ([A-Za-z]+) (20\d\d)', src)
        if not stamp:
            out.append("%s: no 'Updated <month> <year>' stamp" % p.name)
            continue
        stamped = val(stamp.group(1), stamp.group(2))
        newest = stamped
        for m in re.finditer(
                r"\b(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\s+(20\d\d)\b", src):
            newest = max(newest, val(m.group(1), m.group(2)))
        if newest - stamped > 3:
            out.append("%s: stamped %s %s but carries entries up to %d "
                       "months later" % (p.name, stamp.group(1), stamp.group(2), newest - stamped))
        # FSDM's version only compared the stamp with months named on the
        # page, so a page nobody touched for a year passed as long as it
        # named nothing newer. Compare with today as well. This makes the
        # build fail when /now goes stale, which is the point of the gate.
        import datetime
        t = datetime.date.today()
        age = (t.year * 12 + t.month) - stamped
        if age > 3:
            out.append("%s: stamped %s %s, %d months ago; refresh /now"
                       % (p.name, stamp.group(1), stamp.group(2), age))
    return out


def main():
    root = (pathlib.Path(sys.argv[1]) if len(sys.argv) > 1
            else pathlib.Path(__file__).resolve().parent.parent / "production-blocks")
    files = sorted(root.glob("*.html"))
    for p in files:
        check(p)
    fails.extend(class_coverage(files))
    fails.extend(unpinned_headings(files))
    fails.extend(shortcut_range(files))
    fails.extend(now_freshness(files))

    print("checked %d files" % len(files))
    if fails:
        print("%d FAILURE(S):" % len(fails))
        for f in fails:
            print("  FAIL  " + f)
        sys.exit(1)
    print("ALL CHECKS PASSED")


if __name__ == "__main__":
    main()
