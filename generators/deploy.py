#!/usr/bin/env python3
"""
deploy.py --- publish blocks to WordPress through its REST API.

    python3 deploy.py --plan  [files...]   show what would change; writes nothing
    python3 deploy.py --apply [files...]   write to WordPress
    python3 deploy.py --apply --all        every block (first sync, or after a
                                           sidebar change)

With no files and no --all, it deploys nothing. Files are block names in
production-blocks/, e.g. 26-now.html. If 01-sidebar.html is in the list,
every page and essay is redeployed, because each one carries the sidebar.

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
    created as a DRAFT; you publish it in WordPress.
  - The only removal is ytconf.RETIRED: listed old pages are moved to the
    Trash (never deleted outright), and only if the ID still has the listed
    path.
  - Every write is read back and compared. If WordPress altered the content
    (a security plugin stripping scripts, say), the run fails loudly.
  - Unchanged content is skipped, so re-running is harmless.
"""
import base64, json, os, re, sys, urllib.error, urllib.parse, urllib.request
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


def block(html):
    return "<!-- wp:html -->\n%s\n<!-- /wp:html -->" % html.strip()


def path_of(link):
    p = urllib.parse.urlparse(link).path.rstrip("/")
    return p if p else "/"


def targets(files):
    """Map block files to (kind, path, file). Unknown files are an error."""
    out = []
    for f in files:
        if f == "01-sidebar.html":
            continue
        if f in C.PAGES:
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
    if "01-sidebar.html" in files:
        files = all_files()
    plan = targets(files)
    retired = getattr(C, "RETIRED", {})
    if not plan:
        if not retired:
            print("nothing to deploy")
            return

    sidebar = (C.BLOCKS / "01-sidebar.html").read_text(encoding="utf-8")
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
            if kind == "pages":
                missing.append(path)
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
        if kind == "pages":
            content = block(sidebar) + "\n\n" + block(src)
        else:
            content = (block(sidebar) + "\n\n" if C.SIDEBAR_IN_POSTS else "") + block(src)
        slug = path.rstrip("/").split("/")[-1]
        cur = found[f]
        data = {"content": content}
        if use_yoast:
            meta = yoast_meta(f, slug)
            if meta:
                data["meta"] = meta
        if cur is None:
            if kind == "pages":
                raise SystemExit("no WordPress page at %s; create it once by hand (or add its ID to "
                                 "ytconf.WP_IDS) and rerun. Pages are never created automatically." % path)
            title = field(src, r'<h1 class="yt-post__title">(.*?)</h1>')
            cat = field(src, r"<span data-yt-cat>(.*?)</span>")
            data.update({"title": title, "slug": slug, "status": "draft"})
            if not apply:
                print("  CREATE draft post %s  (%s)" % (path, cat))
                created += 1
                continue
            data["categories"] = [category_id(wp, cat)]
            res = wp.call("POST", "posts", data)
            created += 1
            print("  created draft post %s, id %d. Publish it in WordPress." % (path, res["id"]))
        else:
            live = cur.get("content", {}).get("raw", "")
            if live.strip() == content.strip():
                skipped += 1
                print("  unchanged  %s" % path)
                if not use_yoast:
                    continue
            if not apply:
                same_page = "yes" if src.strip() in live else "no"
                same_bar = "yes" if sidebar.strip() in live else "no"
                print("  UPDATE     %s  (id %d, %s; live %d chars, new %d; page block already live: %s, "
                      "sidebar already live: %s)" % (path, cur["id"], cur.get("status"), len(live),
                                                     len(content), same_page, same_bar))
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
            # write never stays live. A new draft is left as a draft.
            note = "the new draft was left unpublished"
            if cur is not None:
                wp.call("POST", "%s/%d" % (kind, cur["id"]), {"content": cur.get("content", {}).get("raw", "")})
                note = "its previous content was restored"
            raise SystemExit("READ-BACK MISMATCH on %s: WordPress stored %d chars, sent %d, so %s. Something "
                             "on the site is altering block content (often a security plugin stripping "
                             "<script>). Nothing after this was deployed." % (path, len(stored), len(content), note))
        if use_yoast:
            got = back.get("meta", {})
            if got.get("_yoast_wpseo_title") != data.get("meta", {}).get("_yoast_wpseo_title"):
                print("  warn: Yoast fields did not stick on %s; is wordpress/yt-yoast-rest.php installed?" % path)
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
    print("%s: %d updated, %d created, %d unchanged, %d trashed" % (verb, changed, created, skipped, trashed))


if __name__ == "__main__":
    main()
