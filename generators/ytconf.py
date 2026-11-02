"""ytconf.py --- the ONE place site-specific settings live.

FSDM kept PILLARS in two files (newpost.py and check-graph.py) and the domain
in four, and its spec lists "change both" as a standing gotcha. Here every
generator and gate imports these values instead.
"""
import pathlib

SITE = "https://yashtulsyani.com"
ROOT = pathlib.Path(__file__).resolve().parent.parent
BLOCKS = ROOT / "production-blocks"
TEMPLATES = pathlib.Path(__file__).resolve().parent / "templates"

# Essays live under /writing/<slug>. The sidebar's prefix match keeps
# Writing lit on every essay.
POST_ROUTE = "/writing/"

# Trailing-slash URLs everywhere, because that is what WordPress serves
# (the live canonical tags end in "/"). FSDM mixed both conventions in its
# @ids; this site picks one. Use url() rather than writing URLs by hand.
def url(path):
    path = path if path.startswith("/") else "/" + path
    if path != "/":
        path = path.rstrip("/") + "/"
    return SITE + path

PERSON_ID = url("/about") + "#yash"

# The five subjects. The value is the pillar essay's slug once one exists;
# None means the cluster has no pillar yet, so rule 1 is not checked for it.
# There is deliberately no Marketing cluster: that writing lives on
# fullstackdigitalmarketer.com.
CLUSTERS = {
    "Relationships": "why-reassurance-is-never-enough",
    "Philosophy": "what-the-stoics-meant-by-what-is-up-to-us",
    "Psychology": "what-attachment-styles-actually-measure",
    "Physics and time": "what-the-observer-effect-actually-says",
    "Fourth dimension": None,
}

# Rule 3 on FSDM was "link to a service or tool". This site sells nothing,
# so the rule becomes: no essay is a dead end. It must link to a book page,
# the reading list, or an essay in a DIFFERENT cluster.
RULE3_PREFIXES = ("/books", "/reading")

# Rule 4 (no orphans) cannot pass for the first essay: nothing exists to
# link to it. Below this many essays the orphan gate warns instead of
# failing. Raise or lower it deliberately; do not delete it.
BOOTSTRAP_MIN_POSTS = 4

# Every block and where it is pasted. gen-paste-manifest.py refuses to run
# if a block is missing from here.
PAGES = {
    "02-home.html": "/",
    "25-about.html": "/about",
    "23-work.html": "/work",
    "24-writing.html": "/writing",
    "20-books.html": "/books",
    "21-book-afraid-of.html": "/books/the-thing-you-were-afraid-of",
    "22-book-nobody-has-to-shrink.html": "/books/nobody-has-to-shrink",
    "28-reading-provisional.html": "/reading",
    "29-notes-provisional.html": "/notes",
    "26-now.html": "/now",
    "27-contact.html": "/contact",
}
# Private, noindex pages built here. None at present.
PRIVATE = {
}

# ---------------------------------------------------------------- deploy
# Level 2: generators/deploy.py publishes blocks to WordPress over its REST
# API. It only ever touches the URLs mapped in PAGES, PRIVATE and the essay
# blocks; anything else on the site is left alone.

# Pages are found by their URL path. The front page is the one page whose
# link is the site root. Fill in an ID for any page the lookup cannot find.
WP_IDS = {
    # "02-home.html": 123,
}

# The sidebar lives in one synced pattern, placed at the top of every page
# and essay (read from the live site, 2 Nov 2026). 01-sidebar.html deploys
# into it; pages keep their reference to it.
SIDEBAR_PATTERN = 612

# Status for a new essay. "publish" makes it live on merge (Yash's choice,
# 2 Nov 2026); "draft" would wait for someone to publish it in WordPress.
NEW_POST_STATUS = "publish"

# Set Yoast's SEO title, meta description and focus keyphrase from
# generators/yoast.py on every deploy. Needs wordpress/yt-yoast-rest.php
# installed and active on the site; until then, leave this False.
YOAST_REST = False

# Old WordPress pages to retire: WordPress page ID -> the path it must have.
# Every deploy moves these to the Trash (restorable there for 30 days), but
# only if the ID still has that path, so a wrong ID never trashes the wrong
# page. Already trashed or deleted pages are skipped.
RETIRED = {
    623: "/insights",           # the old blog hub, replaced by /writing
    923: "/life-system-rpg",    # Life System experiment, dropped 2 Nov 2026
}

# Category IDs are looked up by name and created if missing.
