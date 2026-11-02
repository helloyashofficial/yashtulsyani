#!/usr/bin/env python3
"""install-post-widgets.py :: put post_widgets CSS + JS into 01-sidebar.html
between markers. Idempotent: re-running replaces the previous copy."""
import pathlib, re, post_widgets as W
p = pathlib.Path(__file__).resolve().parent.parent / "production-blocks" / "01-sidebar.html"
s = p.read_text(encoding="utf-8")
CB, CE = "/* POST-WIDGETS-CSS:BEGIN */", "/* POST-WIDGETS-CSS:END */"
JB, JE = "<!-- POST-WIDGETS-JS:BEGIN -->", "<!-- POST-WIDGETS-JS:END -->"
css = CB + W.CSS + "  " + CE + "\n"
js = JB + W.JS + JE + "\n"
if CB in s:
    s = re.sub(re.escape(CB) + ".*?" + re.escape(CE) + r"\n?", lambda m: css, s, flags=re.S)
else:
    i = s.index("</style>")
    s = s[:i] + css + s[i:]
if JB in s:
    s = re.sub(re.escape(JB) + ".*?" + re.escape(JE) + r"\n?", lambda m: js, s, flags=re.S)
else:
    s = s.rstrip() + "\n" + js
assert "&&" not in W.JS and "||" not in W.JS
p.write_text(s, encoding="utf-8")
print("post widgets installed in", p.name)
