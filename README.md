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
system/              the Life System engine and its tests
HANDOVER-V4.md       the full technical handover: read this before changing anything
PASTE-MANIFEST.md    generated: every block, its URL, and the paste order
```

## How a change goes live

1. **Change** on a branch: a page block, an essay spec, `yoast.py` or `ytconf.py`.
2. **Build:** `bash generators/build.sh`. It must end `BUILD OK`. It regenerates the sidebar widgets, the `/writing` hub, page schema and Yoast headers, so commit what it changes.
3. **Open a pull request.** GitHub runs two checks:
   - **Build and gates:** the full build, a check that the committed blocks match what the build produces, the essay content check, and the Life System tests.
   - **Browser QA:** every page at 10 screen widths in light and dark, checking for sideways scroll, clipping, contrast, heading order, accessible names and focus rings.
4. **Merge** once both are green.
5. **Paste** the changed blocks into WordPress. The pull request's file list is the list of what to re-paste. The sidebar always goes first if it changed.

Nothing in this repository publishes to WordPress on its own.

## Writing an essay

1. Add its entry to `YOAST` in `generators/yoast.py`.
2. Write `generators/rewrite/NN-<slug>.py`; copy an existing spec for the shape.
3. Run it, then `bash generators/build.sh`. The `/writing` hub regenerates from the essays automatically.
4. Publish the block as a WordPress **Post** at `/writing/<slug>`, set its category, copy the Yoast fields from its header comment, and re-paste `/writing`.

Every outside claim in an essay links to a primary source that was actually read. Section 5 of `HANDOVER-V4.md` has the details and the linking rules.

## Things that will fail the build on purpose

- `/now` stamped more than three months ago. Refresh it and change its "Updated" date.
- A fifth essay with no other essay linking to it.
- An essay with no link to a book, the reading list or an essay in another subject.
- Any em-dash, any `&&` or `||` in a script, or any non-ASCII character in a script. WordPress breaks these.
- A heading with no colour of its own, which disappears in dark mode.
