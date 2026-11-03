#!/usr/bin/env python3
"""
deploy.py --- publish blocks to WordPress through its REST API.

    python3 deploy.py --plan  [files...]   show what would change; writes nothing
    python3 deploy.py --apply [files...]   write to WordPress
    python3 deploy.py --apply --all        every block (a full sync)

With no files and no --all, it deploys nothing. Files are block names in
production-blocks/, e.g. 26-now.html.

How the live site is put together (read from it on 2 Nov 2026): the sidebar
is one synced pattern (ytconf.SIDEBAR_PATTERN), and every page and essay is
that pattern followed by one Custom HTML block. So 01-sidebar.html goes into
the pattern, and a page deploy replaces only the inside of its one HTML
block, keeping the pattern reference and the block's name. A page that has
no HTML block yet gets one; a page with more than one is refused.

Credentials come from the environment, never from this repository:
    WP_URL           https://yashtulsyani.com
    WP_USER          the WordPress username the application password belongs to
    WP_APP_PASSWORD  an application password (Users > Profile > Application Passwords)
Optional:
    YOAST_REST=1     also set Yoast title, description and focus keyphrase.
                     Needs wordpress/yt-yoast-rest.php installed on the site.

Safety, in order of importance:
  - Only URLs mapped in ytconf (PAGES, PRIVATE), essay blocks and RETIRED are touched.
    A page that cannot be found is an error; pages are never created.
  - Status is never changed on an existing page or post. A new essay is
    created with ytconf.NEW_POST_STATUS (publish: it goes live on merge).
  - The only removal is ytconf.RETIRED: listed old pages are moved to the
    Trash (never deleted outright), and only if the ID still has the listed
    path.
  - Every write is read back and compared. If WordPress altered the content
    (a security plugin stripping scripts, say), the run fails loudly.
  - Unchanged content is skipped, so re-running is harmless.
"""
import base64, hashlib, json, os, re, sys, urllib.error, urllib.parse, urllib.request
import ytconf as C

STATUSES = "publish,private,draft,pending,future"


class WP:
    def __init__(self, url, user, password):
        self.base = url.rstrip("/") + "/wp-json/wp/v2/"
        token = base64.b64encode(("%s:%s" % (user, password)).encode()).decode()
        self.auth = "Basic " + token

    def call(self, method, path, data=None, query=None, missing_ok=False):
        url = self.base + path
        if query:
            url += "?" + urllib.parse.urlencode(query)
        body = json.dumps(data).encode() if data is not None else None
        req = urllib.request.Request(url, data=body, method=method, headers={
            "Authorization": self.auth, "Content-Type": "application/json",
            "Accept": "application/json", "User-Agent": "yt-deploy/1"})
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                return json.loads(r.read().decode() or "null")
        except urllib.error.HTTPError as e:
            if missing_ok:
                if e.code in (404, 410):
                    return None
            detail = e.read().decode(errors="replace")[:300]
            raise SystemExit("WordPress %s %s returned %d: %s" % (method, path, e.code, detail))
        except urllib.error.URLError as e:
            raise SystemExit("could not reach WordPress at %s: %s" % (self.base, e.reason))


    def upload(self, filename, data, mime):
        req = urllib.request.Request(self.base + "media", data=data, method="POST", headers={
            "Authorization": self.auth, "Content-Type": mime, "Accept": "application/json",
            "Content-Disposition": 'attachment; filename="%s"' % filename, "User-Agent": "yt-deploy/1"})
        try:
            with urllib.request.urlopen(req, timeout=120) as r:
                return json.loads(r.read().decode())
        except urllib.error.HTTPError as e:
            raise SystemExit("WordPress media upload of %s returned %d: %s" % (filename, e.code, e.read().decode(errors="replace")[:300]))


SOCIAL = C.ROOT / "social" if hasattr(C, "ROOT") else C.BLOCKS.parent / "social"


def social_image(slug):
    """(path, media slug) for an essay's share image, or None. The media slug
    carries a hash of the file, so a changed image is uploaded once, and an
    unchanged one is never uploaded again."""
    p = SOCIAL / (slug + ".png")
    if not p.exists():
        return None
    h = hashlib.sha1(p.read_bytes()).hexdigest()[:10]
    return p, "yt-social-%s-%s" % (slug, h)


def block(html):
    return "<!-- wp:html -->\n%s\n<!-- /wp:html -->" % html.strip()


HTML_BLOCK = re.compile(r"<!-- wp:html(?: \{.*?\})? -->(.*?)<!-- /wp:html -->", re.S)


def sidebar_ref():
    return '<!-- wp:block {"ref":%d} /-->' % C.SIDEBAR_PATTERN


def compose(live, src, with_ref):
    """Return (new content, live inner html or None, notes) for a page whose
    current content is `live`. Only the inside of the one HTML block changes."""
    notes = []
    blocks = list(HTML_BLOCK.finditer(live))
    if len(blocks) > 1:
        raise ValueError("has %d Custom HTML blocks; expected one. Merge them by hand first." % len(blocks))
    if blocks:
        m = blocks[0]
        new = live[:m.start(1)] + "\n" + src.strip() + "\n" + live[m.end(1):]
        inner = m.group(1)
        other = (live[:m.start()] + live[m.end():]).replace(sidebar_ref(), "").strip()
        if other:
            notes.append("other content on the page is kept: %r" % other[:200])
    else:
        new = (live.strip() + "\n\n" if live.strip() else "") + block(src)
        inner = None
        if live.strip():
            notes.append("no HTML block yet; one is added after the existing content")
    if with_ref:
        if sidebar_ref() not in new:
            new = sidebar_ref() + "\n\n" + new
            notes.append("adds the sidebar pattern, which the page did not have")
    return new, inner, notes


def path_of(link):
    p = urllib.parse.urlparse(link).path.rstrip("/")
    return p if p else "/"


def targets(files):
    """Map block files to (kind, path, file). Unknown files are an error."""
    out = []
    for f in files:
        if f == "01-sidebar.html":
            out.append(("blocks", "sidebar pattern %d" % C.SIDEBAR_PATTERN, f))
        elif f in C.PAGES:
            out.append(("pages", C.PAGES[f], f))
        elif f in C.PRIVATE:
            out.append(("pages", C.PRIVATE[f], f))
        elif re.match(r"\d\d-post-", f):
            src = (C.BLOCKS / f).read_text(encoding="utf-8")
            m = re.search(r"SLUG\s*:\s*(\S+)", src)
            if not m:
                raise SystemExit("%s has no SLUG line" % f)
            out.append(("posts", m.group(1).rstrip("/"), f))
        else:
            raise SystemExit("%s has no destination in ytconf; refusing to guess" % f)
    return out


def all_files():
    return sorted(p.name for p in C.BLOCKS.glob("*.html"))


def find(wp, kind, path, f):
    if kind == "blocks":
        return wp.call("GET", "blocks/%d" % C.SIDEBAR_PATTERN, query={"context": "edit"}, missing_ok=True)
    if f in C.WP_IDS:
        return wp.call("GET", "%s/%d" % (kind, C.WP_IDS[f]), query={"context": "edit"})
    if path == "/":
        # The front page is the one page whose permalink is the site root.
        # Found from the page list, because /settings needs admin rights and
        # security plugins often block it.
        hits, n = [], 1
        while True:
            got = wp.call("GET", "pages", query={"status": STATUSES, "context": "edit",
                                                 "per_page": 100, "page": n})
            hits += [h for h in got if path_of(h.get("link", "")) == "/"]
            if len(got) < 100:
                break
            n += 1
        if len(hits) != 1:
            raise SystemExit("found %d pages at the site root; add the front page ID to "
                             "ytconf.WP_IDS['%s']" % (len(hits), f))
        return hits[0]
    slug = path.rstrip("/").split("/")[-1]
    hits = wp.call("GET", kind, query={"slug": slug, "status": STATUSES, "context": "edit", "per_page": 20})
    hits = [h for h in hits if path_of(h.get("link", "")) == path]
    if len(hits) > 1:
        raise SystemExit("%d %s match %s; add the right ID to ytconf.WP_IDS" % (len(hits), kind, path))
    return hits[0] if hits else None


def category_id(wp, name, cache={}):
    if name in cache:
        return cache[name]
    hits = [c for c in wp.call("GET", "categories", query={"search": name, "per_page": 50})
            if c.get("name") == name]
    cid = hits[0]["id"] if hits else wp.call("POST", "categories", {"name": name})["id"]
    cache[name] = cid
    return cid


def yoast_meta(f, slug):
    import yoast as Y
    d = Y.PAGES.get(f) or Y.YOAST.get(slug)
    if not d:
        return None
    return {"_yoast_wpseo_title": d["title"], "_yoast_wpseo_metadesc": d["desc"],
            "_yoast_wpseo_focuskw": d["focus"]}


def field(src, pattern):
    m = re.search(pattern, re.sub(r"<!--.*?-->", "", src, flags=re.S), re.S)
    return re.sub(r"<[^>]+>", "", m.group(1)).strip() if m else None


def main():
    args = sys.argv[1:]
    apply = "--apply" in args
    if not apply:
        if "--plan" not in args:
            raise SystemExit(__doc__)
    files = [a for a in args if not a.startswith("--")]
    for f in files:
        if not (C.BLOCKS / f).exists():
            raise SystemExit("no such block: %s" % f)
    if "--all" in args:
        files = all_files()
    plan = targets(files)
    retired = getattr(C, "RETIRED", {})
    if not plan:
        if not retired:
            print("nothing to deploy")
            return

    url, user, pw = os.environ.get("WP_URL"), os.environ.get("WP_USER"), os.environ.get("WP_APP_PASSWORD")
    have_creds = True
    for v in (url, user, pw):
        if not v:
            have_creds = False
    if not have_creds:
        if apply:
            raise SystemExit("WP_URL, WP_USER and WP_APP_PASSWORD must be set to deploy")
        print("PLAN (no credentials, so nothing compared with the live site):")
        for kind, path, f in plan:
            print("  %-6s %-48s <- %s" % (kind[:-1], path, f))
        for pid, rpath in sorted(retired.items()):
            print("  trash  %-48s (page id %d)" % (rpath, pid))
        return

    wp = WP(url, user, pw)
    use_yoast = os.environ.get("YOAST_REST") == "1"
    if getattr(C, "YOAST_REST", False):
        use_yoast = True
    changed = skipped = created = 0
    # Find every target before writing anything, so a missing page stops the
    # run before the first write rather than halfway through.
    found, missing = {}, []
    retire = []
    for pid, rpath in sorted(retired.items()):
        r = wp.call("GET", "pages/%d" % pid, query={"context": "edit"}, missing_ok=True)
        if r is None:
            print("  gone       %s  (id %d no longer exists)" % (rpath, pid))
            continue
        if r.get("status") == "trash":
            print("  gone       %s  (id %d already in the Trash)" % (rpath, pid))
            continue
        if path_of(r.get("link", "")) != rpath:
            raise SystemExit("ytconf.RETIRED says page %d is %s, but WordPress has it at %s. Refusing to "
                             "trash it; nothing was written." % (pid, rpath, path_of(r.get("link", ""))))
        retire.append((pid, rpath, r))
    for kind, path, f in plan:
        found[f] = find(wp, kind, path, f)
        if found[f] is None:
            if kind != "posts":
                missing.append(path)
        else:
            try:
                compose(found[f].get("content", {}).get("raw", ""), "x", kind != "blocks")
            except ValueError as e:
                raise SystemExit("%s %s Nothing was written." % (path, e))
    if use_yoast:
        # The Yoast fields are only exposed once wordpress/yt-yoast-rest.php
        # is active. Check before writing anything.
        probe = [c for (k, p_, f_), c in [((k, p_, f_), found[f_]) for k, p_, f_ in plan]
                 if c is not None and k != "blocks"]
        if probe:
            m = probe[0].get("meta")
            if not isinstance(m, dict) or "_yoast_wpseo_title" not in m:
                raise SystemExit("YOAST_REST is on, but WordPress does not expose the Yoast fields. Is the "
                                 "YT Yoast fields over REST plugin installed and active? Nothing was written.")
    if missing:
        for path in missing:
            slug = path.rstrip("/").split("/")[-1]
            print("  MISSING    %s: no page at this address." % path)
            near = wp.call("GET", "pages", query={"search": slug, "status": STATUSES,
                                                   "context": "edit", "per_page": 20})
            for h in near:
                print("             similar: %s  (id %d, %s, title %r)" % (
                    h.get("link"), h["id"], h.get("status"), h.get("title", {}).get("raw", "")))
            if not near:
                print("             no page with %r in its title or content either." % slug)
        raise SystemExit("%d page(s) missing: %s. Create each once by hand in WordPress (or add its "
                         "ID to ytconf.WP_IDS) and rerun. Pages are never created automatically, and "
                         "nothing was written." % (len(missing), ", ".join(missing)))
    for kind, path, f in plan:
        src = (C.BLOCKS / f).read_text(encoding="utf-8")
        slug = path.rstrip("/").split("/")[-1]
        cur = found[f]
        with_ref = kind != "blocks"
        live = cur.get("content", {}).get("raw", "") if cur is not None else ""
        try:
            content, inner, notes = compose(live, src, with_ref)
        except ValueError as e:
            raise SystemExit("%s %s; nothing after this was deployed." % (path, e))
        data = {"content": content}
        if use_yoast:
            if kind == "blocks":
                use_meta = False
            else:
                use_meta = True
        else:
            use_meta = False
        meta = None
        if use_meta:
            meta = yoast_meta(f, slug)
            if meta:
                data["meta"] = meta
        meta_same = True
        if meta:
            have = (cur or {}).get("meta") or {}
            for k_, v_ in meta.items():
                if have.get(k_) != v_:
                    meta_same = False
        if cur is None:
            if kind == "pages":
                raise SystemExit("no WordPress page at %s; create it once by hand (or add its ID to "
                                 "ytconf.WP_IDS) and rerun. Pages are never created automatically." % path)
            title = field(src, r'<h1 class="yt-post__title">(.*?)</h1>')
            cat = field(src, r"<span data-yt-cat>(.*?)</span>")
            data.update({"title": title, "slug": slug, "status": C.NEW_POST_STATUS})
            data["content"] = content = sidebar_ref() + "\n\n" + block(src)
            if not apply:
                print("  CREATE %s post %s  (%s)" % (C.NEW_POST_STATUS, path, cat))
                created += 1
                continue
            data["categories"] = [category_id(wp, cat)]
            res = wp.call("POST", "posts", data)
            created += 1
            print("  created %s post %s, id %d, in %s" % (res.get("status"), path, res["id"], cat))
        else:
            same = False
            if inner is not None:
                if inner.strip() == src.strip():
                    if not notes:
                        same = True
            if same:
                if meta_same:
                    skipped += 1
                    print("  unchanged  %s" % path)
                    continue
                # Only the Yoast fields differ: send those alone, and expect
                # the content to come back exactly as it is now.
                data = {"meta": meta}
                content = live
            if not apply:
                if same:
                    print("  YOAST      %s  (id %d: SEO title, description and keyphrase will be set)"
                          % (path, cur["id"]))
                    changed += 1
                if not same:
                    print("  UPDATE     %s  (id %d, %s; HTML block %d -> %d chars)" % (
                        path, cur["id"], cur.get("status"), len((inner or "").strip()), len(src.strip())))
                    for n in notes:
                        print("             %s" % n)
                    changed += 1
                continue
            res = wp.call("POST", "%s/%d" % (kind, cur["id"]), data)
            changed += 1
            print("  updated    %s  (id %d, status left as %s)" % (path, res["id"], res.get("status")))
        # read back: WordPress must have stored exactly what was sent
        back = wp.call("GET", "%s/%d" % (kind, res["id"]), query={"context": "edit"})
        stored = back.get("content", {}).get("raw", "")
        if stored.strip() != content.strip():
            # Put the page back the way it was before failing, so a stripped
            # write never stays live. A new post is switched to draft.
            note = "the new post was switched to draft so a damaged version is not live"
            if cur is None:
                wp.call("POST", "posts/%d" % res["id"], {"status": "draft"})
            if cur is not None:
                wp.call("POST", "%s/%d" % (kind, cur["id"]), {"content": cur.get("content", {}).get("raw", "")})
                note = "its previous content was restored"
            raise SystemExit("READ-BACK MISMATCH on %s: WordPress stored %d chars, sent %d, so %s. Something "
                             "on the site is altering block content (often a security plugin stripping "
                             "<script>). Nothing after this was deployed." % (path, len(stored), len(content), note))
        if meta:
            got = back.get("meta") or {}
            for k_, v_ in meta.items():
                if got.get(k_) != v_:
                    raise SystemExit("Yoast field %s did not save on %s (WordPress has %r). The page content "
                                     "is fine; check the YT Yoast fields over REST plugin." % (k_, path, got.get(k_)))
    # Share images: each essay's social/<slug>.png, uploaded once to the media
    # library and set as the post's featured image (Yoast uses it as og:image).
    shared = 0
    for kind, path, f in plan:
        if kind != "posts":
            continue
        slug = path.rstrip("/").split("/")[-1]
        si = social_image(slug)
        if si is None:
            print("  warn: no share image social/%s.png" % slug)
            continue
        png, mslug = si
        post = find(wp, kind, path, f)
        if post is None:
            print("  SOCIAL     %s  (set after the post is created)" % path)
            continue
        hits = [m for m in wp.call("GET", "media", query={"slug": mslug, "per_page": 5}) if m.get("slug") == mslug]
        mid = hits[0]["id"] if hits else None
        if mid is not None:
            if post.get("featured_media") == mid:
                pub = wp.call("GET", "posts/%d" % post["id"])
                yh = pub.get("yoast_head_json")
                if not isinstance(yh, dict):
                    state = "Yoast data not exposed"
                else:
                    og = [i.get("url") for i in (yh.get("og_image") or []) if isinstance(i, dict)]
                    state = "Yoast og:image %s; og:title %s; twitter:card %s" % (og[0] if og else "NOT SET", "set" if yh.get("og_title") else "missing", yh.get("twitter_card"))
                print("  share ok   %s  (featured image %d, post says %s; %s)" % (path, mid, pub.get("featured_media"), state))
                continue
        if not apply:
            print("  SOCIAL     %s  (%s share image %s)" % (path, "set existing" if mid else "upload and set", png.name))
            shared += 1
            continue
        if mid is None:
            title = field((C.BLOCKS / f).read_text(encoding="utf-8"), r'<h1 class="yt-post__title">(.*?)</h1>')
            m = wp.upload(mslug + ".png", png.read_bytes(), "image/png")
            mid = m["id"]
            wp.call("POST", "media/%d" % mid, {"alt_text": "Share image for the essay: %s" % title, "title": title})
            if m.get("slug") != mslug:
                print("  note: WordPress named the upload %r" % m.get("slug"))
        wp.call("POST", "posts/%d" % post["id"], {"featured_media": mid})
        back = wp.call("GET", "posts/%d" % post["id"], query={"context": "edit"})
        if back.get("featured_media") != mid:
            raise SystemExit("share image did not attach to %s" % path)
        shared += 1
        print("  social     %s  (featured image %d)" % (path, mid))

    trashed = 0
    for pid, rpath, r in retire:
        title = r.get("title", {}).get("raw", "")
        if not apply:
            print("  TRASH      %s  (id %d, %s, title %r)" % (rpath, pid, r.get("status"), title))
            trashed += 1
            continue
        res = wp.call("DELETE", "pages/%d" % pid)
        if res.get("status") != "trash":
            raise SystemExit("asked WordPress to trash %s (id %d) but it reports status %r"
                             % (rpath, pid, res.get("status")))
        trashed += 1
        print("  trashed    %s  (id %d, %r). Restore it from Pages > Trash within 30 days if needed."
              % (rpath, pid, title))
    verb = "applied" if apply else "planned"
    print("%s: %d updated, %d created, %d unchanged, %d trashed, %d share images" % (verb, changed, created, skipped, trashed, shared))


if __name__ == "__main__":
    main()
