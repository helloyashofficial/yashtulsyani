# yashtulsyani.com

The source for yashtulsyani.com: a personal writing site on WordPress and Kadence. Every page and essay is one self-contained Custom HTML block, built and checked here, then pasted into WordPress.

This repository is the single source of truth. If a block in WordPress and a block here disagree, this one wins: edit here, then re-paste.

## Layout

```
production-blocks/   the blocks you paste into WordPress (see PASTE-MANIFEST.md)
generators/          the build: checks, schema, Yoast data, essay pipeline
  ytconf.py          site settings: domain, the five subjects, page map
  yoast.py           focus keyphrase, SEO title and description for every URL
  rewrite/           one spec file per essay; edit these, never the essay blocks
  templates/         the block every essay is built from
qa/                  browser tests: layout, contrast, accessibility, widgets
HANDOVER-V4.md       the full technical handover: read this before changing anything
PASTE-MANIFEST.md    generated: every block, its URL, and the paste order
```

## How a change goes live

1. **Change** on a branch: a page block, an essay spec, `yoast.py` or `ytconf.py`.
2. **Build:** `bash generators/build.sh`. It must end `BUILD OK`. It regenerates the sidebar widgets, the `/writing` hub, page schema and Yoast headers, so commit what it changes.
3. **Open a pull request.** GitHub runs two checks:
   - **Build and gates:** the full build, a check that the committed blocks match what the build produces, and the essay content check.
   - **Browser QA:** every page at 10 screen widths in light and dark, checking for sideways scroll, clipping, contrast, heading order, accessible names and focus rings.
   - **Deploy plan:** the WordPress pages and posts the merge would change. Nothing is written.
4. **Merge** once the checks are green. The same checks run again on `main`, and if they pass, **the changed blocks are published to WordPress automatically**.

## Publishing (Level 2)

`generators/deploy.py`, run by the `deploy` job, writes blocks to WordPress through its REST API:

- **The sidebar is one synced pattern in WordPress** (pattern 612, `SIDEBAR_PATTERN` in `ytconf.py`), placed at the top of every page and essay. `01-sidebar.html` deploys into that pattern, so a sidebar change is one write.
- **A page deploy replaces only the inside of the page's one Custom HTML block.** The pattern reference, the block's name and anything else on the page are kept. A page with more than one HTML block is refused until you merge them by hand.
- **It touches only the URLs listed in `generators/ytconf.py`, the essay blocks and the sidebar pattern.** Everything is looked up before the first write, so a missing page stops the run with nothing written. It never creates pages.
- **It never changes an existing page's status.** A new essay is created **published** in its category, so merging an essay puts it live (`NEW_POST_STATUS` in `ytconf.py`; set it to `draft` to review in WordPress first).
- **Every write is read back.** If WordPress stored something different (a security plugin stripping scripts, say), the page is restored to its previous content and the run fails.
- Unchanged pages are skipped, so a rerun is harmless.
- **The only removal is `RETIRED` in `ytconf.py`:** old pages listed there by WordPress ID are moved to the Trash (restorable for 30 days), and only if that ID still has the listed address. Add a page there to retire it; the plan shows it as `TRASH` first.

Manual runs: **Actions → checks → Run workflow** offers `plan` or `apply`, for every block or only the last commit's changes. Use `plan` with `all` to preview a full sync.

### One-time setup

1. **WordPress:** Users → Profile → **Application Passwords**. Name it `github-deploy`, click Add, and copy the password it shows. It appears only once.
2. **GitHub:** this repo → Settings → Secrets and variables → **Actions → New repository secret**. Add three:
   - `WP_URL`: `https://yashtulsyani.com`
   - `WP_USER`: your WordPress username, the one you log in with
   - `WP_APP_PASSWORD`: the password from step 1, spaces included
3. **Test it:** Actions → checks → Run workflow → `plan`, `all`. It should list every page as `unchanged` or `UPDATE` and finish green.
4. **Optional, Yoast fields:** in WordPress, Plugins → Add New → Upload Plugin → `wordpress/yt-yoast-rest.zip` → Install Now → Activate. Then set `YOAST_REST = True` in `generators/ytconf.py` (or add a repository variable `YOAST_REST` = `1`). From then on the deploy also sets each page's SEO title, description and focus keyphrase from `generators/yoast.py`. Without it, you paste those three fields by hand.
5. **Optional, approval:** Settings → Environments → `production` → Required reviewers. Each deploy then waits for you to click Approve.

After every merge, `tidy-branches.yml` deletes branches whose pull request has been merged (and the live-audit screenshots branch). Branches with open pull requests are never touched.

To switch publishing off, delete the `WP_APP_PASSWORD` secret, or revoke the application password in WordPress. The checks keep running and you paste blocks by hand again.

## Writing an essay

1. Add its entry to `YOAST` in `generators/yoast.py`.
2. Write `generators/rewrite/NN-<slug>.py`; copy an existing spec for the shape.
3. Run it, then `bash generators/build.sh`. The `/writing` hub regenerates from the essays automatically.
4. Open a pull request and merge it. The deploy publishes the essay in its category and updates `/writing`. Merging is publishing, so read the essay before you merge.

Every outside claim in an essay links to a primary source that was actually read. Section 5 of `HANDOVER-V4.md` has the details and the linking rules.

## Things that will fail the build on purpose

- `/now` stamped more than three months ago. Refresh it and change its "Updated" date.
- A fifth essay with no other essay linking to it.
- An essay with no link to a book, the reading list or an essay in another subject.
- Any em-dash, any `&&` or `||` in a script, or any non-ASCII character in a script. WordPress breaks these.
- A heading with no colour of its own, which disappears in dark mode.
