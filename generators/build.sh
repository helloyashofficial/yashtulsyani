#!/bin/bash
# build.sh --- yashtulsyani.com. Ported in shape from FSDM's build.sh.
# Runs from anywhere. set -e: the first failing step stops the build.
#
# Essays are NOT built here. Run their specs first, then this script, so
# the /writing hub is regenerated from them:
#   for f in rewrite/[0-9][0-9]-*.py; do python3 "$f"; done
set -e
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$HERE"
echo "== post widgets into the sidebar =="
python3 install-post-widgets.py
echo "== writing hub (pre-rendered from the essays) =="
python3 sync-writing-hub.py
echo "== page schema =="
python3 add-page-schema.py
echo "== yoast data =="
python3 yoast.py --stamp
echo "== link graph =="
python3 check-graph.py
echo "== block gates =="
python3 verify.py
echo "== schema =="
python3 check-schema.py
echo "== paste manifest =="
python3 gen-paste-manifest.py
echo "BUILD OK"
