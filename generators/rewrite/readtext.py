#!/usr/bin/env python3
"""readtext.py FILE :: print a block as readable text (headings marked, lists bulleted)."""
import re, html, sys
s = open(sys.argv[1], encoding="utf-8").read()
s = re.sub(r"<style.*?</style>|<script(?![^>]*ld\+json).*?</script>|<!--.*?-->", "", s, flags=re.S)
s = re.sub(r"<script[^>]*ld\+json[^>]*>.*?</script>", "\n[JSON-LD block]\n", s, flags=re.S)
s = re.sub(r"<h([1-6])[^>]*>", lambda m: "\n\n" + "#" * int(m.group(1)) + " ", s)
s = re.sub(r"<li[^>]*>", "\n  - ", s)
s = re.sub(r"<(?:/p|/h[1-6]|br|/tr|/figcaption|/summary|/legend|/div)[^>]*>", "\n", s)
s = re.sub(r"<(?:td|th)[^>]*>", " | ", s)
s = re.sub(r'<a [^>]*href="([^"]+)"[^>]*>', r"[\1] ", s)
s = re.sub(r"<[^>]+>", "", s)
s = html.unescape(s)
s = re.sub(r"[ \t]+", " ", s)
s = re.sub(r"\n\s*\n\s*\n+", "\n\n", s)
print(s.strip())
