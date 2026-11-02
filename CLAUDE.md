# yashtulsyani.com: working rules

Read `HANDOVER-V4.md` before changing anything. It is the technical source of truth. `README.md` explains the workflow.

## Non-negotiable

- **No invented facts, figures or URLs.** Every outside claim links to a primary source that was fetched and read. Claims about Yash or his books use only what he has stated. If something cannot be verified, leave the gap and say so.
- **Verify output, do not trust that a script ran.** Run `bash generators/build.sh` (must end `BUILD OK`), read what changed, and look at the rendered page for anything visual (`qa/mkall.sh`, then a screenshot).
- **Edit sources, not outputs.** Essays are built from `generators/rewrite/NN-*.py`; the `/writing` hub, page schema, Yoast headers and sidebar widgets are generated. Commit what `build.sh` changes.
- **WordPress hardening, in every script:** no `&&`, no `||` (use nested ifs), ASCII only (use `\uXXXX`), no `<template>`, `addEventListener` only.
- **House style:** sentence case headings, British spelling, no em-dashes in front-end text, ` · ` for label pairs.
- **Every page wrapper is `<div class="yt-shell">`**, never `<main>`. Heading colours are pinned `var(--yt-text, #111827) !important`. Page rules that set margin or letter-spacing on a `p` or heading are qualified with `.yt-page` (specificity trap).
- **The physics line:** quantum vocabulary is metaphor and is labelled as metaphor at the point of use. Never claim consciousness creates reality, that people are entangled, or that physics proves manifestation.

## Git

- Work on a branch and open a pull request; do not push to `main` directly.
- **Merging to `main` publishes to the live site** (generators/deploy.py, the `deploy` job). Treat every merge as a release: the deploy plan on the pull request lists what will change.
- Never run `deploy.py --apply` locally, and never put WordPress credentials in the repo, a commit or a chat. They live only in GitHub secrets.
