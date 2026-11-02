# mkall.sh: wrap every block with the sidebar into a standalone page, inside
# the same .entry-content wrapper WordPress puts block content in.
B="$(cd "$(dirname "${BASH_SOURCE[0]}")/../production-blocks" && pwd)"
OUT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
for f in $B/*.html; do n=$(basename $f .html); [ "$n" = "01-sidebar" ] && continue; { printf '<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>%s</title></head><body style="margin:0"><div class="entry-content single-content">' $n; cat $B/01-sidebar.html $f; printf '</div></body></html>'; } > $OUT/$n.html; done
