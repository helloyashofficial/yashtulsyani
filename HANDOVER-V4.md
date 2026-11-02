# yashtulsyani.com: handover v4

Read this first, written to be read cold. It supersedes `HANDOVER-V3.md`. Where this file and `yashtulsyani-com-BUILD-GUIDELINES.md` disagree, this file describes what the code actually does; the differences are listed in section 8.

On 24 October 2026 the whole site was rebuilt on the machinery behind fullstackdigitalmarketer.com (FSDM), taken from `FSDM-TECH-KIT.zip` and its spec. The two sites still share nothing but that machinery.

---

## 1. What is in this bundle

```
production-blocks/   the blocks to paste (sidebar, 11 pages, essays)
generators/          the build: gates, schema, Yoast, essay pipeline
  ytconf.py          the ONE place site settings live (domain, clusters, routes, page map)
  templates/         post-template.html, the block every essay is built from
  rewrite/           qa.py (essay content gate), plus helpers; essay specs go here
qa/                  Playwright harness: layout, contrast, accessibility, widgets
PASTE-MANIFEST.md    generated: every block, its URL, and the paste order
HANDOVER-V4.md       this file
```

Run `bash generators/build.sh`. It must end `BUILD OK`.

---

## 2. Paste order

`PASTE-MANIFEST.md` is generated and authoritative. In short:

1. `01-sidebar.html` first, as its own Custom HTML block, on every page **and every essay**. It is the site's stylesheet: tokens, page globals, all essay CSS and the widget runtime live in it and nowhere else.
2. The pages. Book detail pages before `/books`, since the index links to them.
3. Essays, when there are any, then re-paste `/writing`.

Every page block needs the new sidebar. Pasting a page without re-pasting the sidebar will leave it on the old tokens.

---

## 3. What changed from v2

**The sidebar (v3)** is FSDM's sidebar ported by namespace transform (`fs-` to `yt-`), with this site's navigation put back: nine slots, shortcuts 1 to 9 and 0 for home, and the prefix match that keeps Books lit on `/books/<slug>` and Writing lit on `/writing/<slug>`. From FSDM it brings:

- **Contrast-audited tokens.** `--yt-text-2` is now `#4b5563` (was `#6b7280`, 4.43:1) and `--yt-text-3` is `#5f666d` (was `#9ca3af`, 2.33:1) in light; `--yt-text-3` dark is `#8b9299`. The old greys survive as `--yt-fill-2` and `--yt-fill-3` for borders, rules and meters, which is where every page's non-text uses now point.
- Form-field tokens (`--yt-field-*`), focus rings site-wide, `.yt-sr-only`, 16px inputs on touch, the narrow-screen rules, reduced motion.
- All essay CSS (post anatomy, sticky TOC rail at 1240px) and the widget CSS and runtime (calculator, checklist, tabs, sortable table, decision tree, callouts, compare, flow).
- Legacy FSDM multi-block wrappers (`postwrap`, `ps`) were removed; nothing here used them.

**Every page block** was brought to that standard:

- Wrapper is `<div class="yt-shell">`, never `<main>`. Kadence already wraps page content in `main#main`, so a second `<main>` would nest landmarks.
- Heading colours pinned with `!important` and a literal fallback; `-webkit-text-fill-color` pinned on every hover/focus/active link and button colour.
- Every `var(--yt-*)` colour carries a literal fallback at the current light value.
- Every `h2` has an id. Decorative SVGs and arrow glyphs are `aria-hidden`.
- Grid tracks are `minmax(0, …)` and auto-fill grids are `minmax(min(Npx, 100%), 1fr)`, so nothing forces sideways scroll at 320px.
- **The specificity trap was live on every page and is fixed.** The sidebar's `.yt-page p, .yt-page h1–h4{margin:0}` and its heading `letter-spacing` are (0,1,1), and beat every single-class page rule at (0,1,0). Page titles, subtitles, section headings and hints were losing their margins and tracking. Found by screenshot, not by any gate. Those rules are now qualified as `.yt-page .class`.
- SVG diagram labels on the book pages use a text token, not a fill token, so they meet 4.5:1.

**Content.** Page copy is unchanged except:

- `/about` gains a **Background** section (2019–2022 independent creator on psychology and philosophy; 2022–2025 Turabit AI, brand strategy; Head of Growth Marketing at BetterBugs and QAble Testlab since April 2025). The audience-size figure is left out because it is unsourced, and so is the channel's name, because it is unconfirmed. Generic anchors ("here", "Go there") were fixed.
- `/work`, `/now` and the homepage name the current role.
- `/now` is stamped **October 2026** and its prefix is now `yt-now` so the freshness gate can read it.
- The homepage shortcut hint now mentions 0 for home.

**`/system`** (the Life System page) was removed from the site on 2 Nov 2026; Yash dropped it as an experiment. Its block and engine remain in git history.

---

## 4. Schema and Yoast

`generators/add-page-schema.py` defines the Person and the two Books **once** and writes them between `PAGE-SCHEMA:BEGIN/END` markers:

| Block | Nodes (all fragment @ids Yoast never uses) |
|---|---|
| home, work | `Person` `/about/#yash` |
| about | `ProfilePage` `/about/#profilepage` → `Person` |
| books index | `ItemList` `/books/#books` of both `Book`s |
| each book | `Book` `/books/<slug>/#book`, `creativeWorkStatus: Unpublished` |

URLs use trailing slashes everywhere, because WordPress serves them. FSDM mixed both conventions.

`check-schema.py` exempts five pages **by name, with a reason each**: the three provisional pages, `/now` and `/contact`. An empty ItemList, or a node invented to satisfy a gate, would be worse than none.

`generators/yoast.py` holds focus keyphrase, title and description for all 11 pages and stamps them into each block's header comment. Its gate enforces a 60-character title, a 120–155 character description (FSDM enforced only the maximum), every keyphrase word present in both, **no shared keyphrases**, and an SEO title different from the h1.

---

## 5. Writing the first essay

The pipeline is ported and was proven end to end on throwaway essays that were then deleted.

1. Add the essay's entry to `YOAST` in `generators/yoast.py`. A missing entry now **stops** the build; FSDM skipped it silently.
2. Write `generators/rewrite/40-<slug>.py`. The shape is in `newpost.py`'s docstring. Category must be one of the five clusters in `ytconf.py`. Use 4 or more FAQs.
3. `python3 generators/rewrite/40-<slug>.py`. It refuses to write if:
   - **rule 3** fails: no link to a book page, `/reading`, or an essay in another cluster;
   - **rule 2** fails: once one essay exists, a later one with no lateral essay link;
   - or the template and generator disagree. Every substitution is asserted; FSDM's version could report success after matching nothing.
4. `python3 generators/rewrite/qa.py 40` (2,000-word body floor, dashes, banned phrases, 4+ FAQs).
5. `bash generators/build.sh`.
6. Publish at `/writing/<slug>` as a WordPress **Post**, set its category, paste the Yoast fields from the header comment, then rebuild `/writing` (see section 7).

**The orphan rule is relaxed until there are four essays** (`ytconf.BOOTSTRAP_MIN_POSTS`). Before that it warns, because the first essay cannot have an inbound link. From four essays on it fails the build. This was tested with four essays. When a cluster gets its pillar essay, put the slug in `ytconf.CLUSTERS` and rule 1 starts applying.

---

## 6. The gates, and proof they fire

`verify.py` carries FSDM's gates plus the ones this site already had:

| Gate | Injected fault | Result |
|---|---|---|
| logical operators | `&&` in /system's script (page since removed) | FAIL, named |
| em-dash | one in /work's copy | FAIL |
| h1 count | a second h1 on /contact | FAIL |
| non-ASCII JS | a middot in the sidebar script | FAIL |
| control chars | U+0091 in CSS | FAIL |
| CSS braces | a stray `}` | FAIL |
| JSON-LD | a raw `&` | FAIL |
| shortcut range | homepage advertising 1 to 8 | FAIL |
| class coverage | an essay using an undefined class | FAIL |
| unpinned headings | colour removed from a title | FAIL |
| tag balance | an unclosed div | FAIL |
| now freshness | stamp four months old | FAIL (new: FSDM compared only against months named on the page, so a page untouched for a year passed) |
| Yoast | title identical to h1; overlong descriptions | FAIL; it caught 12 of my own drafts on first run |

Browser QA (`qa/qa-output.txt`): 12 pages at 10 widths in both themes, with zero layout, overflow, clipping or contrast issues. Accessibility at 375 and 1440 is clean: duplicate ids, heading order, ARIA references, target sizes, focus rings and accessible names. Every `details` open is clean too. The widget runtime in the new sidebar reproduces FSDM's reference output line for line.

---

## 7. Not ported, deliberately

- **Tool pages** (`toolkit.py`, `gen-tool-*`): this site has no tools.
- **`sync-post-cards.py`**: it keeps the blog hub's cards in step with the essays. `/writing` is still provisional, so there is nothing to sync. Port it when the real hub is built, which must be **pre-rendered**: FSDM's REST-only hub showed crawlers 65 words.
- **FSDM's writing briefs** (`BRIEF*.md`): written for search-competitive operator guides, not essays.
- `rewrite/sync-related.py` and `readtext.py` were ported mechanically but are untested here.

---

## 8. Where this departs from the guidelines document

- **Shortcuts:** 1 to 9 plus 0 for home. Section 5's table and the sidebar now agree.
- **Rule 2:** it fails under 1 lateral link and warns under 2. The guidelines say 2 to 3; FSDM's code enforced 1 while printing "2-3".
- **Rule 3:** it **fails** rather than warns, matching the guidelines' "no essay is a dead end".
- **Rule 4:** relaxed below four essays (section 5). The guidelines had no bootstrap and could not be satisfied.
- **`class_coverage`:** essays only. Pages carry their own CSS by design.

---

## 9. Independent fact-check, 24 Oct 2026

A separate agent with no part in the build checked every page's copy and JSON-LD against only the facts Yash has stated. Fixed as a result:

- "take three hundred pages" on /writing: an invented figure. Removed.
- "spent years as a marketing consultancy site" on /now: the "years" was unstated. Now "used to be".
- "Complete", "finished", "two finished manuscripts", "Seeking a home", "manuscript complete" and "when a book finds a publisher": all unconfirmed, and they contradicted /now's "not yet decided". Every page now says "Unpublished".
- /now's "I keep deferring this one, which is itself an answer": an invented personal admission. Removed.
- /work said the marketing writing "moved". The marketing essays on this domain were deleted, not moved, so it now says "live on a separate site".
- "the references exist so you can check me" and "the books carry their own references": only the first book is known to have references.
- /notes promised "a few times a month": a commitment Yash had not made. Removed.
- Book JSON-LD: `numberOfPages` and two topics the pages never state. Removed; schema now mirrors the visible page.

**Not changed, because they come from the manuscripts themselves** (the agent had only a summary of the facts, so it could not confirm them): chapter titles, quotes, part ranges, deep-dive and workbook names on both book pages. They were built from the uploaded manuscripts in August. Recheck them against the final text before querying anyone.

**Unsourced claims kept as opinion, not fact:** the method lines on /work ("usually within a quarter", "the first six months look worse") and the textbook physics definitions on the book pages. Flag them if you want any softened.

---

## 10. Still needs Yash

1. **Contact email.** Done: Yash confirmed `yashtulsyani.work@gmail.com` on 2 Nov 2026.
2. **Book status.** Every page now says only "Unpublished". The unconfirmed "manuscript complete" chip and "Seeking a home" were removed, along with every "finished/complete" claim (section 9). If either book is finished, or you are seeking a publisher, say so and it can go back in.
3. **Audience size and channel name** for `/about`, if they can be sourced and confirmed.
4. **The reading list** (title, author, one line on why). It fills `/reading`, the homepage strip and `/now` at once.
5. **`/notes` sourcing**: manual, a fixed source list, or regenerated on request.
6. **Disclosure on the book pages** before querying agents (quoted lines, principles, chapter titles).
7. **How the sidebar reaches essay pages** in WordPress (a Kadence Element or similar). FSDM's spec marks this unverified on its own site too. Essays render unstyled without it.
8. **Keyphrase overlap across the two domains.** The homepage here targets "Yash Tulsyani"; check FSDM's about page is not targeting the same phrase.

---

## 11. The first two essays (24 Oct 2026)

| Block | URL | Cluster | Role |
|---|---|---|---|
| `40-post-why-reassurance-is-never-enough.html` | `/writing/why-reassurance-is-never-enough` | Relationships | pillar |
| `41-post-what-the-observer-effect-actually-says.html` | `/writing/what-the-observer-effect-actually-says` | Physics and time | pillar |

- Both are set as their cluster's pillar in `ytconf.CLUSTERS`, so future essays in those clusters must link up to them.
- They link to each other, which is each one's cross-cluster exit (rule 3), plus links to the book pages.
- Specs are in `generators/rewrite/40-*.py` and `41-*.py`; edit the spec and rerun it, never the block.
- Every outside claim links to a source that was fetched and read when the essay was written: Starr and Davila (2008), Downey et al. (1998), Osborne and Williams (2013), Murray et al. (2005), Merton via Brandmayr (2022), the Weizmann release and Buks et al. (1998), two Stanford Encyclopedia entries, and the 2022 Nobel release.
- `/writing` is now a real hub (`24-writing.html`, replacing the provisional block). Its cards and ItemList are regenerated from the essay blocks by `generators/sync-writing-hub.py`, which `build.sh` runs.

**To publish them:**
1. In WordPress create the categories **Relationships** and **Physics and time**.
2. Create each Post at its slug, paste the block as the only content, and set the category.
3. Copy the focus keyphrase, SEO title and meta description from the block's header comment into Yoast.
4. Re-paste `/writing` (24-writing.html) and `/now` (26-now.html), which now list them.
5. Before any of that, confirm the sidebar reaches single posts (section 10, item 7). Without it, essays render unstyled.

---

## 12. GitHub and automatic publishing (2 Nov 2026)

The site lives in `helloyashofficial/yashtulsyani`. `README.md` is the operating manual; `CLAUDE.md` holds the rules every session must follow.

- `.github/workflows/checks.yml` runs build and gates, the "generated files are committed" check, essay QA and browser QA on every pull request, and a **deploy plan**. On a merge to `main` the same checks run and, if green, `generators/deploy.py --apply` publishes the changed blocks.
- `deploy.py` was tested against a mock WordPress REST server before shipping, in eight scenarios: first full sync; rerun as a no-op; script stripping (detected, page restored); wrong password; plan against live state; Yoast fields with and without the snippet; and a missing page. A decoy page with the same slug under another parent was correctly left alone.
- Settings in `ytconf.py`: `WP_IDS` for any page the lookup cannot find, and `SIDEBAR_PATTERN`. The live site (read 2 Nov 2026) holds the sidebar in synced pattern 612, and every page and essay is `<!-- wp:block {"ref":612} /-->` followed by one named Custom HTML block. That answers how the sidebar reaches single posts. `01-sidebar.html` deploys into the pattern; a page deploy replaces only the inside of its HTML block. Tested on a mock shaped like the live site: full sync and rerun, page already current (not written), two HTML blocks (refused, nothing written), missing pattern reference (added), script stripping on the pattern (restored), Yoast fields (never sent to the pattern).
- First runs against the real WordPress (2 Nov 2026): the login works and all 11 public pages are found. `/settings` returned 403 to this login, so the front page is now found from the page list (the one page whose link is the site root). Every target is looked up before the first write, so a missing page stops the run with nothing written.
- `ytconf.RETIRED` lists old pages to remove: `/insights` (id 623, the old blog hub, replaced by `/writing`) and `/life-system-rpg` (id 923, the dropped Life System experiment, which was published publicly). Each deploy moves them to the Trash, never deletes outright, and only if the ID still has the listed path. Tested on the mock: plan, apply, rerun, wrong ID (refused, nothing written) and already deleted.
