#!/usr/bin/env python3
"""
postkit.py --- shared styling and visual components for blog post blocks.

Design constraints, inherited from the sidebar token system:
  - monochrome, 1px hairlines, 10px radius, no shadows
  - every colour comes from a --yt-* token, never a hex literal, so light
    and dark mode both work. SVG uses currentColor for the same reason.
  - ZERO JavaScript. Bars are CSS widths, charts are inline SVG, and the
    expandable panels are native <details>, which needs no script.
    That keeps posts outside the WordPress JS-mangling problem entirely.

Every component is a <figure> with a caption and, where it carries data,
a visible source line. A chart without its source is decoration.
"""

import re

# ------------------------------------------------------------------ CSS

CSS = """
<style>
  /* These blocks render INSIDE the WordPress single-post template, which
     already supplies the sidebar offset and the content column. Wrapping in
     .yt-shell here double-offset the content by the 240px sidebar width, and
     margin:0 auto then centred it again inside that. Hence: no shell wrapper,
     no auto-centring, no horizontal padding. Left edge lines up with the
     theme's own post title. */
  .yt-post{ max-width:760px; margin:0; padding:0 0 72px; }


  .yt-post__dek{
    font-size:18px; line-height:1.6; color:var(--yt-muted);
    margin:0 0 36px; padding-bottom:28px; border-bottom:1px solid var(--yt-line);
  }

  .yt-post__toc{
    border:1px solid var(--yt-line); border-radius:10px;
    padding:20px 22px; margin:0 0 44px; background:var(--yt-surface);
  }
  .yt-post__toc-label{
    font-family:'JetBrains Mono',ui-monospace,monospace;
    font-size:11px; letter-spacing:.08em; text-transform:uppercase;
    color:var(--yt-muted); margin-bottom:12px;
  }
  .yt-post__toc ol{ margin:0; padding-left:20px; }
  .yt-post__toc li{ margin:6px 0; font-size:15px; }
  .yt-post__toc a{ color:var(--yt-text); text-decoration:none; }
  .yt-post__toc a:hover{ text-decoration:underline; }

  .yt-post__body h2{
    font-size:23px; line-height:1.3; letter-spacing:-.01em; font-weight:640;
    color:var(--yt-text); margin:52px 0 18px; scroll-margin-top:24px;
  }
  .yt-post__body p{
    font-size:17px; line-height:1.72; color:var(--yt-text); margin:0 0 20px;
  }
  .yt-post__body ul{ margin:0 0 24px; padding-left:22px; }
  .yt-post__body li{
    font-size:17px; line-height:1.68; color:var(--yt-text); margin:0 0 12px;
  }
  .yt-post__body strong{ font-weight:620; }

  /* ============================= VISUAL COMPONENTS ============================= */

  .yt-viz{
    margin:36px 0; padding:24px; border:1px solid var(--yt-line);
    border-radius:10px; background:var(--yt-surface);
  }
  .yt-viz__cap{
    font-family:'JetBrains Mono',ui-monospace,monospace;
    font-size:11px; letter-spacing:.08em; text-transform:uppercase;
    color:var(--yt-muted); margin-bottom:18px; display:block;
  }
  .yt-viz__src{
    font-size:12px; color:var(--yt-muted); margin-top:16px;
    padding-top:12px; border-top:1px solid var(--yt-line);
  }

  /* ---- bar chart, widths set inline, no script ---- */
  .yt-bars{ display:flex; flex-direction:column; gap:12px; }
  .yt-bar{ display:grid; grid-template-columns:minmax(0,1fr); gap:5px; }
  .yt-bar__top{ display:flex; justify-content:space-between; align-items:baseline; gap:12px; }
  .yt-bar__label{ font-size:14px; color:var(--yt-text); font-weight:520; }
  .yt-bar__val{
    font-family:'JetBrains Mono',ui-monospace,monospace;
    font-size:12px; color:var(--yt-muted); white-space:nowrap;
  }
  .yt-bar__track{
    height:8px; border-radius:4px; background:var(--yt-hover);
    border:1px solid var(--yt-line); overflow:hidden;
  }
  .yt-bar__fill{ height:100%; background:var(--yt-text); border-radius:3px 0 0 3px; }
  .yt-bar__fill--soft{ background:var(--yt-muted); opacity:.45; }

  /* ---- data table ---- */
  .yt-table{ width:100%; border-collapse:collapse; font-size:14px; }
  .yt-table th{
    text-align:left; padding:10px 12px;
    font-family:'JetBrains Mono',ui-monospace,monospace;
    font-size:11px; letter-spacing:.06em; text-transform:uppercase;
    color:var(--yt-muted); border-bottom:1px solid var(--yt-text);
    font-weight:500;
  }
  .yt-table td{
    padding:11px 12px; border-bottom:1px solid var(--yt-line);
    color:var(--yt-text); line-height:1.5; vertical-align:top;
  }
  .yt-table tr:last-child td{ border-bottom:0; }
  .yt-table td.yt-num{
    font-family:'JetBrains Mono',ui-monospace,monospace;
    text-align:right; white-space:nowrap;
  }
  .yt-table__wrap{ overflow-x:auto; }

  /* ---- scatter plot ---- */
  .yt-plot{ width:100%; height:auto; display:block; color:var(--yt-text); }
  .yt-plot__axis{ stroke:var(--yt-line); stroke-width:1; }
  .yt-plot__tick{
    font-family:'JetBrains Mono',ui-monospace,monospace;
    font-size:9px; fill:var(--yt-muted);
  }
  .yt-plot__dot{ fill:var(--yt-text); }
  .yt-plot__dot--soft{ fill:none; stroke:var(--yt-muted); stroke-width:1.4; }
  .yt-plot__lbl{ font-size:10px; fill:var(--yt-text); }
  .yt-plot__zone{ fill:var(--yt-hover); }
  .yt-plot__zonelbl{
    font-family:'JetBrains Mono',ui-monospace,monospace;
    font-size:9px; fill:var(--yt-muted); letter-spacing:.06em;
  }

  /* ---- structural diagram ---- */
  .yt-dia{ width:100%; height:auto; display:block; color:var(--yt-text); }
  .yt-dia__node{ fill:var(--yt-surface); stroke:currentColor; stroke-width:1.4; }
  .yt-dia__node--hub{ fill:var(--yt-text); }
  .yt-dia__edge{ stroke:var(--yt-muted); stroke-width:1.2; fill:none; }
  .yt-dia__lbl{ font-size:10px; fill:var(--yt-text); text-anchor:middle; }
  .yt-dia__lbl--inv{ fill:var(--yt-bg); }
  .yt-dia__cap{
    font-family:'JetBrains Mono',ui-monospace,monospace;
    font-size:9px; fill:var(--yt-muted); text-anchor:middle;
    letter-spacing:.06em; text-transform:uppercase;
  }

  /* ---- stage timeline ---- */
  .yt-stages{ display:flex; flex-direction:column; }
  .yt-stage{ display:grid; grid-template-columns:auto minmax(0,1fr); gap:16px; }
  .yt-stage__rail{ display:flex; flex-direction:column; align-items:center; }
  .yt-stage__num{
    width:26px; height:26px; flex:none; border-radius:50%;
    border:1px solid var(--yt-text); color:var(--yt-text);
    display:flex; align-items:center; justify-content:center;
    font-family:'JetBrains Mono',ui-monospace,monospace; font-size:11px;
  }
  .yt-stage__line{ width:1px; flex:1; background:var(--yt-line); min-height:14px; }
  .yt-stage:last-child .yt-stage__line{ display:none; }
  .yt-stage__body{ padding-bottom:22px; }
  .yt-stage__ttl{ font-size:15px; font-weight:600; color:var(--yt-text); margin-bottom:4px; }
  .yt-stage__txt{ font-size:14px; line-height:1.6; color:var(--yt-muted); }

  /* ---- expandable panel, native details, zero JS ---- */
  .yt-drop{ border-top:1px solid var(--yt-line); }
  .yt-drop:last-of-type{ border-bottom:1px solid var(--yt-line); }
  .yt-drop summary{
    list-style:none; cursor:pointer; padding:14px 0;
    display:flex; justify-content:space-between; align-items:center; gap:14px;
    font-size:15px; font-weight:560; color:var(--yt-text);
  }
  .yt-drop summary::-webkit-details-marker{ display:none; }
  .yt-drop summary::after{
    content:'+'; font-family:'JetBrains Mono',ui-monospace,monospace;
    font-size:16px; color:var(--yt-muted); flex:none;
  }
  .yt-drop[open] summary::after{ content:'\\2212'; }
  .yt-drop__body{ padding:0 0 16px; font-size:15px; line-height:1.65; color:var(--yt-muted); }
  /* Kadence-override: summary is not a button, but pin anyway */
  .yt-drop summary, .yt-drop summary:hover,
  .yt-drop summary:focus, .yt-drop summary:active{
    color:var(--yt-text) !important; background:none !important;
  }

  /* ---- stat row ---- */
  .yt-stats{ display:grid; grid-template-columns:repeat(auto-fit, minmax(min(130px, 100%),1fr)); gap:20px; }
  .yt-stat__num{
    font-size:30px; font-weight:650; letter-spacing:-.02em;
    color:var(--yt-text); line-height:1.1;
  }
  .yt-stat__lbl{
    font-size:12px; line-height:1.45; color:var(--yt-muted); margin-top:6px;
  }

  .yt-post__takeaway{
    border:1px solid var(--yt-line); border-left:3px solid var(--yt-text);
    border-radius:0 10px 10px 0; padding:22px 24px; margin:48px 0 0;
    background:var(--yt-surface);
  }
  .yt-post__takeaway-label{
    font-family:'JetBrains Mono',ui-monospace,monospace;
    font-size:11px; letter-spacing:.08em; text-transform:uppercase;
    color:var(--yt-muted); margin-bottom:10px;
  }
  .yt-post__takeaway p{ margin:0; font-size:17px; line-height:1.68; }

  .yt-post__foot{ margin-top:64px; padding-top:32px; border-top:1px solid var(--yt-line); }
  .yt-post__foot-label{
    font-family:'JetBrains Mono',ui-monospace,monospace;
    font-size:11px; letter-spacing:.08em; text-transform:uppercase;
    color:var(--yt-muted); margin-bottom:16px;
  }
  .yt-post__related{ display:grid; gap:12px; margin-bottom:40px; }
  .yt-post__rel{
    display:block; border:1px solid var(--yt-line); border-radius:10px;
    padding:16px 18px; text-decoration:none; transition:border-color .18s ease;
  }
  .yt-post__rel:hover{ border-color:var(--yt-text); }
  .yt-post__rel-cat{
    font-family:'JetBrains Mono',ui-monospace,monospace;
    font-size:10px; letter-spacing:.08em; text-transform:uppercase;
    color:var(--yt-muted); display:block; margin-bottom:6px;
  }
  .yt-post__rel-title{ font-size:16px; font-weight:600; color:var(--yt-text); line-height:1.4; }

  .yt-post__cta{
    border:1px solid var(--yt-line); border-radius:10px; padding:28px;
    background:var(--yt-surface);
  }
  .yt-post__cta h3{ font-size:19px; font-weight:640; color:var(--yt-text); margin:0 0 8px; }
  .yt-post__cta p{ font-size:15px; line-height:1.6; color:var(--yt-muted); margin:0 0 18px; }
  .yt-post__btn{
    display:inline-block; padding:11px 20px; border-radius:8px;
    border:1px solid var(--yt-text); background:var(--yt-text);
    color:var(--yt-bg); font-size:14px; font-weight:560; text-decoration:none;
  }
  /* Kadence-override: pin colours across states, see HANDOVER section 3.5 */
  .yt-post__btn, .yt-post__btn:hover, .yt-post__btn:focus, .yt-post__btn:active{
    color:var(--yt-bg) !important; background:var(--yt-text) !important;
    border-color:var(--yt-text) !important; text-decoration:none !important;
  }

  @media (prefers-reduced-motion:reduce){
    .yt-post__rel{ transition:none; }
  }
  @media (max-width:900px){
    .yt-post{ padding:0 0 56px; }
    .yt-viz{ padding:18px; }
    .yt-stat__num{ font-size:25px; }
  }
</style>
"""


def esc(s):
    return s.replace("&", "&amp;")


# ------------------------------------------------------- components

def bars(caption, rows, source=None, soft_from=None):
    """rows: [(label, numeric_value, display_value)]. Widths scaled to max."""
    top = max(r[1] for r in rows) or 1
    out = ['<figure class="yt-viz">',
           '  <figcaption class="yt-viz__cap">%s</figcaption>' % esc(caption),
           '  <div class="yt-bars">']
    for i, (lbl, val, disp) in enumerate(rows):
        pct = round(100.0 * val / top, 1)
        mod = " yt-bar__fill--soft" if (soft_from is not None and i >= soft_from) else ""
        out += ['    <div class="yt-bar">',
                '      <div class="yt-bar__top">',
                '        <span class="yt-bar__label">%s</span>' % esc(lbl),
                '        <span class="yt-bar__val">%s</span>' % esc(disp),
                '      </div>',
                '      <div class="yt-bar__track">',
                '        <div class="yt-bar__fill%s" style="width:%s%%"></div>' % (mod, pct),
                '      </div>',
                '    </div>']
    out.append('  </div>')
    if source:
        out.append('  <div class="yt-viz__src">%s</div>' % esc(source))
    out.append('</figure>')
    return "\n".join(out)


def table(caption, headers, rows, source=None, num_cols=()):
    out = ['<figure class="yt-viz">',
           '  <figcaption class="yt-viz__cap">%s</figcaption>' % esc(caption),
           '  <div class="yt-table__wrap">',
           '  <table class="yt-table">',
           '    <thead><tr>']
    for h in headers:
        out.append('      <th>%s</th>' % esc(h))
    out += ['    </tr></thead>', '    <tbody>']
    for r in rows:
        out.append('      <tr>')
        for i, c in enumerate(r):
            cls = ' class="yt-num"' if i in num_cols else ''
            out.append('        <td%s>%s</td>' % (cls, esc(str(c))))
        out.append('      </tr>')
    out += ['    </tbody>', '  </table>', '  </div>']
    if source:
        out.append('  <div class="yt-viz__src">%s</div>' % esc(source))
    out.append('</figure>')
    return "\n".join(out)


def scatter(caption, points, source=None, x_label="Keyword difficulty",
            y_label="Monthly search volume", x_max=90):
    """points: [(label, kd, volume, highlight_bool)].

    Volume is plotted on a log scale. A linear axis forced a y_max, and any
    point above it clamped to the same height as every other point above it,
    which made 14,800 and 22,200 render identically. Log spans the real range
    (hundreds to tens of thousands) without misrepresenting anything.
    """
    import math
    W, H = 700, 360
    L, R, T, B = 58, 18, 18, 42
    pw, ph = W - L - R, H - T - B
    ticks = [300, 1000, 3000, 10000, 30000]
    lo, hi = math.log10(200), math.log10(40000)

    def px(kd): return L + pw * min(kd, x_max) / float(x_max)
    def py(v):
        return T + ph - ph * (math.log10(max(v, 200)) - lo) / (hi - lo)

    out = ['<figure class="yt-viz">',
           '  <figcaption class="yt-viz__cap">%s</figcaption>' % esc(caption),
           '  <svg class="yt-plot" viewBox="0 0 %d %d" role="img" '
           'aria-label="%s">' % (W, H, esc(caption))]
    out.append('    <rect class="yt-plot__zone" x="%d" y="%d" width="%.0f" height="%d" />'
               % (L, T, pw * 30.0 / x_max, ph))
    out.append('    <text class="yt-plot__zonelbl" x="%.0f" y="%d">WINNABLE NOW</text>'
               % (L + 6, T + 14))
    out.append('    <line class="yt-plot__axis" x1="%d" y1="%d" x2="%d" y2="%d" />'
               % (L, T + ph, L + pw, T + ph))
    out.append('    <line class="yt-plot__axis" x1="%d" y1="%d" x2="%d" y2="%d" />'
               % (L, T, L, T + ph))
    for kd in range(0, x_max + 1, 15):
        out.append('    <text class="yt-plot__tick" x="%.0f" y="%d" text-anchor="middle">%d</text>'
                   % (px(kd), T + ph + 16, kd))
    for v in ticks:
        out.append('    <text class="yt-plot__tick" x="%d" y="%.0f" text-anchor="end">%s</text>'
                   % (L - 8, py(v) + 3, format(v, ",")))
    out.append('    <text class="yt-plot__tick" x="%.0f" y="%d" text-anchor="middle">%s</text>'
               % (L + pw / 2, H - 6, esc(x_label)))
    out.append('    <text class="yt-plot__tick" x="%d" y="%d" text-anchor="start">%s (log)</text>'
               % (6, T + 10, esc(y_label)))
    for lbl, kd, vol, hi_ in points:
        x, y = px(kd), py(vol)
        cls = "yt-plot__dot" if hi_ else "yt-plot__dot yt-plot__dot--soft"
        out.append('    <circle class="%s" cx="%.1f" cy="%.1f" r="%s" />'
                   % (cls, x, y, "5" if hi_ else "4"))
        anchor = "end" if x > L + pw * 0.66 else "start"
        dx = -9 if anchor == "end" else 9
        out.append('    <text class="yt-plot__lbl" x="%.1f" y="%.1f" text-anchor="%s">%s</text>'
                   % (x + dx, y + 3.5, anchor, esc(lbl)))
    out.append('  </svg>')
    if source:
        out.append('  <div class="yt-viz__src">%s</div>' % esc(source))
    out.append('</figure>')
    return "\n".join(out)


def link_graphs(caption, source=None):
    """Three internal-link topologies, side by side."""
    def cluster(ox, title, edges, hub=True):
        pts = {"h": (60, 34), "a": (18, 92), "b": (60, 108), "c": (102, 92),
               "d": (30, 138), "e": (90, 138)}
        s = []
        for u, v in edges:
            x1, y1 = pts[u]; x2, y2 = pts[v]
            s.append('    <line class="yt-dia__edge" x1="%d" y1="%d" x2="%d" y2="%d" />'
                     % (ox + x1, y1, ox + x2, y2))
        for k, (x, y) in pts.items():
            is_hub = (k == "h" and hub)
            cls = "yt-dia__node yt-dia__node--hub" if is_hub else "yt-dia__node"
            s.append('    <circle class="%s" cx="%d" cy="%d" r="%d" />'
                     % (cls, ox + x, y, 13 if is_hub else 9))
        s.append('    <text class="yt-dia__cap" x="%d" y="%d">%s</text>'
                 % (ox + 60, 172, title))
        return "\n".join(s)

    hub_e = [("h", "a"), ("h", "b"), ("h", "c"), ("h", "d"), ("h", "e")]
    mesh_e = hub_e + [("a", "b"), ("b", "c"), ("a", "d"), ("d", "e"), ("e", "c")]
    chain_e = [("h", "a"), ("a", "d"), ("d", "b"), ("b", "e"), ("e", "c")]

    out = ['<figure class="yt-viz">',
           '  <figcaption class="yt-viz__cap">%s</figcaption>' % esc(caption),
           '  <svg class="yt-dia" viewBox="0 0 480 186" role="img" '
           'aria-label="Three internal link topologies: hub, mesh and chain">']
    out.append(cluster(10, "HUB", hub_e))
    out.append(cluster(170, "MESH", mesh_e))
    out.append(cluster(330, "CHAIN", chain_e, hub=False))
    out.append('  </svg>')
    if source:
        out.append('  <div class="yt-viz__src">%s</div>' % esc(source))
    out.append('</figure>')
    return "\n".join(out)


def stages(caption, items, source=None):
    """items: [(label, title, text)] rendered as a numbered rail."""
    out = ['<figure class="yt-viz">',
           '  <figcaption class="yt-viz__cap">%s</figcaption>' % esc(caption),
           '  <div class="yt-stages">']
    for lbl, ttl, txt in items:
        out += ['    <div class="yt-stage">',
                '      <div class="yt-stage__rail">',
                '        <div class="yt-stage__num">%s</div>' % esc(lbl),
                '        <div class="yt-stage__line"></div>',
                '      </div>',
                '      <div class="yt-stage__body">',
                '        <div class="yt-stage__ttl">%s</div>' % esc(ttl),
                '        <div class="yt-stage__txt">%s</div>' % esc(txt),
                '      </div>',
                '    </div>']
    out.append('  </div>')
    if source:
        out.append('  <div class="yt-viz__src">%s</div>' % esc(source))
    out.append('</figure>')
    return "\n".join(out)


def drops(caption, items, source=None):
    """Native <details> panels. Interactive with no script at all."""
    out = ['<figure class="yt-viz">',
           '  <figcaption class="yt-viz__cap">%s</figcaption>' % esc(caption)]
    for q, a in items:
        out += ['  <details class="yt-drop">',
                '    <summary>%s</summary>' % esc(q),
                '    <div class="yt-drop__body">%s</div>' % esc(a),
                '  </details>']
    if source:
        out.append('  <div class="yt-viz__src">%s</div>' % esc(source))
    out.append('</figure>')
    return "\n".join(out)


def stats(caption, items, source=None):
    """items: [(big_number, label)]"""
    out = ['<figure class="yt-viz">',
           '  <figcaption class="yt-viz__cap">%s</figcaption>' % esc(caption),
           '  <div class="yt-stats">']
    for num, lbl in items:
        out += ['    <div class="yt-stat">',
                '      <div class="yt-stat__num">%s</div>' % esc(num),
                '      <div class="yt-stat__lbl">%s</div>' % esc(lbl),
                '    </div>']
    out.append('  </div>')
    if source:
        out.append('  <div class="yt-viz__src">%s</div>' % esc(source))
    out.append('</figure>')
    return "\n".join(out)
from postkit_interactive import *
