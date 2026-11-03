#!/usr/bin/env python3
"""
covers.py --- line-drawn covers for essays, in the site's own style.

Monochrome, 1px hairlines, no fills beyond a hatch, no text, and every
colour from a --yt-* token via currentColor, so light and dark mode both
work and nothing is hosted. Each essay can name its own motif; otherwise
its subject's default is used, so a new essay always has a cover.

    svg = cover(slug, subject)

Classes used inside each SVG (styled by the page that embeds it):
    yt-cv-a   primary line     (--yt-text-2)
    yt-cv-b   secondary line   (--yt-fill-3)
    yt-cv-c   faint structure  (--yt-line)
"""
import math, random

W, H = 480, 240

# Per-essay motifs; anything not listed falls back to its subject.
BY_SLUG = {
    "why-reassurance-is-never-enough": "loop",
    "what-the-observer-effect-actually-says": "fringes",
    "what-attachment-styles-actually-measure": "scatter",
    "what-the-stoics-meant-by-what-is-up-to-us": "dichotomy",
    "what-it-means-to-call-time-the-fourth-dimension": "cone",
    "what-repair-after-an-argument-actually-involves": "repair",
    "what-self-silencing-is": "muted",
    "why-we-blame-the-people-we-love": "regard",
    "why-time-has-a-direction": "spread",
    "what-flatland-teaches-about-the-fourth-dimension": "slice",
    "what-your-partner-does-with-your-good-news": "echo",
}
BY_SUBJECT = {
    "Relationships": "overlap",
    "Psychology": "scatter",
    "Philosophy": "dichotomy",
    "Physics and time": "fringes",
    "Fourth dimension": "cone",
}


def f(x):
    return ("%.1f" % x).rstrip("0").rstrip(".")


def line(x1, y1, x2, y2, c="a", extra=""):
    return '<line class="yt-cv-%s" x1="%s" y1="%s" x2="%s" y2="%s"%s/>' % (c, f(x1), f(y1), f(x2), f(y2), extra)


def circle(cx, cy, r, c="a", extra=""):
    return '<circle class="yt-cv-%s" cx="%s" cy="%s" r="%s"%s/>' % (c, f(cx), f(cy), f(r), extra)


def path(d, c="a", extra=""):
    return '<path class="yt-cv-%s" d="%s"%s/>' % (c, d, extra)


def dot(cx, cy, r=2.2, c="a"):
    return '<circle class="yt-cv-%s yt-cv-dot" cx="%s" cy="%s" r="%s"/>' % (c, f(cx), f(cy), f(r))


def arc(cx, cy, r, a0, a1):
    x0, y0 = cx + r * math.cos(a0), cy + r * math.sin(a0)
    x1, y1 = cx + r * math.cos(a1), cy + r * math.sin(a1)
    large = 1 if abs(a1 - a0) > math.pi else 0
    return "M%s %s A%s %s 0 %d 1 %s %s" % (f(x0), f(y0), f(r), f(r), large, f(x1), f(y1))


# ------------------------------------------------------------- motifs

def loop(uid):
    """The validation loop: one circuit drawn firmly, its earlier rounds
    fainter around it, and an arrow that brings it back to the start."""
    cx, cy = 240, 120
    out = [circle(cx, cy, r, "c") for r in (110, 96)]
    out.append(circle(cx, cy, 82, "b", ' stroke-dasharray="3 5"'))
    R = 62
    a0, a1 = math.radians(-60), math.radians(240)
    out.append(path(arc(cx, cy, R, a0, a1)))
    ax, ay = cx + R * math.cos(a1), cy + R * math.sin(a1)
    t = a1 + math.pi / 2
    for s in (-1, 1):
        out.append(line(ax, ay, ax - 12 * math.cos(t) + s * 7 * math.cos(a1), ay - 12 * math.sin(t) + s * 7 * math.sin(a1)))
    out.append(dot(cx + R * math.cos(a0), cy + R * math.sin(a0), 3.4))
    return out


def fringes(uid):
    """Two slits, the wavefronts spreading from them, and the bands that
    build up on the screen."""
    out = []
    bx, sx = 120, 400
    s1, s2 = 104, 136
    out += [line(bx, 24, bx, s1 - 6), line(bx, s1 + 6, bx, s2 - 6), line(bx, s2 + 6, bx, 216)]
    for sy in (s1, s2):
        for r in range(22, 260, 26):
            a = math.asin(min(1, (sx - bx - 4) / r)) if r > sx - bx - 4 else math.pi / 2
            lim = min(math.radians(62), a)
            out.append(path(arc(bx, sy, r, -lim, lim), "c"))
    out.append(line(sx, 24, sx, 216, "b"))
    mid = (s1 + s2) / 2.0
    for i in range(-14, 15):
        y = mid + i * 6.4
        k = math.cos(i * math.pi / 4.2) ** 2 * math.exp(-(i / 11.0) ** 2)
        if k > 0.04:
            out.append(line(sx + 4, y, sx + 4 + 56 * k, y))
    return out


def scatter(uid):
    """Two axes, anxiety and avoidance, with people spread continuously
    across them rather than sorted into four boxes."""
    rnd = random.Random(uid)
    x0, y0, x1, y1 = 96, 222, 384, 18
    out = [line(x0, y0, x1 + 14, y0, "b"), line(x0, y0, x0, y1 - 14, "b"),
           line((x0 + x1) / 2, y1, (x0 + x1) / 2, y0, "c", ' stroke-dasharray="2 4"'),
           line(x0, (y0 + y1) / 2, x1, (y0 + y1) / 2, "c", ' stroke-dasharray="2 4"')]
    for _ in range(150):
        u = (rnd.random() + rnd.random() + rnd.random()) / 3.0
        v = (rnd.random() + rnd.random() + rnd.random()) / 3.0
        out.append(dot(x0 + 8 + u * (x1 - x0 - 16), y0 - 8 - v * (y0 - y1 - 16), 2))
    return out


def dichotomy(uid):
    """What is up to us, drawn as a small bounded sphere, hatched, inside a
    much larger field that is not."""
    cx, cy = 240, 120
    cid = "yt-cv-clip-" + uid
    ix, ir = cx - 62, 46
    out = ['<defs><clipPath id="%s"><circle cx="%s" cy="%s" r="%s"/></clipPath></defs>' % (cid, f(ix), f(cy), ir)]
    out.append(circle(cx, cy, 112, "b", ' stroke-dasharray="1 6"'))
    out.append(circle(cx, cy, 98, "c"))
    hatch = [line(ix - 80 + i, cy + 80, ix + i, cy - 80, "b") for i in range(-60, 140, 8)]
    out.append('<g clip-path="url(#%s)">%s</g>' % (cid, "".join(hatch)))
    out.append(circle(ix, cy, ir))
    out.append(line(cx + 4, cy - 112, cx + 4, cy + 112, "c", ' stroke-dasharray="2 4"'))
    return out


def cone(uid):
    """A light cone: past below, future above, the plane of one observer's
    now across the middle, and a worldline passing through the event."""
    cx, cy = 240, 120
    out = [path("M%s %s A%s %s 0 1 1 %s %s A%s %s 0 1 1 %s %s" % (f(cx - 170), f(cy), 170, 30, f(cx + 170), f(cy), 170, 30, f(cx - 170), f(cy)), "c", ' stroke-dasharray="2 4"')]
    for ty in (18, 222):
        out.append(path("M%s %s A%s %s 0 1 1 %s %s A%s %s 0 1 1 %s %s" % (f(cx - 104), ty, 104, 15, f(cx + 104), ty, 104, 15, f(cx - 104), ty), "b"))
    out += [line(cx - 104, 18, cx + 104, 222, "b"), line(cx + 104, 18, cx - 104, 222, "b")]
    out.append(path("M%s %s C%s %s %s %s %s %s S%s %s %s %s" % (f(cx + 40), 228, f(cx + 30), 180, f(cx - 12), 160, cx, cy,
                                                              f(cx + 6), 60, f(cx - 26), 12)))
    out.append(dot(cx, cy, 3.4))
    return out


def repair(uid):
    """A line that breaks and is bridged, while the lines around it carry
    on: most disagreements continue; what matters is the coming back."""
    out = []
    for y in (40, 72, 168, 200):
        out.append(line(36, y, 444, y, "c"))
    out.append(line(36, 132, 196, 132))
    out.append(line(284, 108, 444, 108))
    n = 8
    for i in range(n):
        x = 204 + i * 9.5
        y = 132 - (i + 0.5) * 24 / n
        out.append(line(x, y - 10, x + 6, y + 10, "b"))
    out.append(dot(196, 132, 3.4))
    out.append(dot(284, 108, 3.4))
    return out


def muted(uid):
    """A voice as a waveform that falls to a flat line part way through, with
    the outline of what it would have said still faintly there."""
    out = [line(36, 120, 444, 120, "c")]
    n = 34
    for i in range(n):
        x = 44 + i * 12
        amp = 74 * (0.35 + 0.65 * abs(math.sin(i * 0.9) * math.cos(i * 0.37)))
        if i < 14:
            out.append(line(x, 120 - amp, x, 120 + amp))
        else:
            fade = max(0.0, 1 - (i - 14) / 3.0)
            out.append(line(x, 120 - amp, x, 120 + amp, "c", ' stroke-dasharray="2 4"'))
            if fade > 0:
                out.append(line(x, 120 - amp * fade * 0.5, x, 120 + amp * fade * 0.5))
    out.append(line(44 + 17 * 12, 120, 444, 120))
    out.append(dot(44 + 17 * 12, 120, 3.2))
    return out


def regard(uid):
    """Strawson's two stances: two people facing each other, joined by the
    exchange of attitudes between them (the participant stance), and a third
    point looking on from outside along a straight dashed line (the objective
    stance)."""
    y = 132
    ax, bx, r = 140, 340, 26
    out = [circle(ax, y, r), circle(bx, y, r)]

    def arrow_arc(x0, y0, cx, cy, x1, y1, c):
        out.append(path("M%s %s Q %s %s %s %s" % (f(x0), f(y0), f(cx), f(cy), f(x1), f(y1)), c))
        dx, dy = x1 - cx, y1 - cy
        n = math.hypot(dx, dy)
        ux, uy = dx / n, dy / n
        for sgn in (-1, 1):
            ang = math.radians(28) * sgn
            vx = ux * math.cos(ang) - uy * math.sin(ang)
            vy = ux * math.sin(ang) + uy * math.cos(ang)
            out.append(line(x1, y1, x1 - 11 * vx, y1 - 11 * vy, c))

    arrow_arc(ax + 22, y - 14, 240, y - 78, bx - 22, y - 14, "a")
    arrow_arc(bx - 22, y + 14, 240, y + 78, ax + 22, y + 14, "b")
    ox, oy = 424, 34
    out.append(circle(ox, oy, 11, "b"))
    out.append(line(ox - 12, oy + 4, 262, y - 44, "c", ' stroke-dasharray="3 5"'))
    return out


def spread(uid):
    """Three moments of the same box: particles gathered in one corner, then
    spreading, then spread through it; an arrow underneath points the way
    the sequence is always seen to run."""
    rnd = random.Random(uid)
    out = []
    boxes = [(48, 116), (186, 254), (324, 392)]
    for k, (x0, x1) in enumerate(boxes):
        out.append(path("M%s 40 H%s V176 H%s Z" % (x0, x1 + 40, x0), "b"))
        w = (x1 + 40 - x0)
        frac = (0.28, 0.62, 1.0)[k]
        for _ in range(26):
            px = x0 + 8 + rnd.random() * (w - 16) * frac
            py = 48 + rnd.random() * (120 * frac + 0.0) + (0 if k == 2 else 0)
            out.append(dot(px, min(py, 168), 2))
    out.append(line(48, 206, 432, 206))
    out.append(line(432, 206, 422, 200))
    out.append(line(432, 206, 422, 212))
    return out


def slice(uid):
    """A sphere passing down through a flat plane, and below it the circles a
    Flatlander would see: a point, growing circles, the largest, then
    shrinking again to a point."""
    out = []
    out.append(path("M40 150 L130 104 L440 104 L350 150 Z", "b"))
    cx, r = 240, 46
    out.append(circle(cx, 104 - r + 16, r))
    out.append(path("M%s %s A%s %s 0 0 0 %s %s" % (cx - 43, 120, 43, 9, cx + 43, 120), "a", ' stroke-dasharray="3 4"'))
    seq = [0, 9, 17, 22, 17, 9, 0]
    xs = [74, 122, 176, 240, 304, 358, 406]
    for x, rr in zip(xs, seq):
        if rr == 0:
            out.append(dot(x, 198, 2.6))
        else:
            out.append(path("M%s %s A%s %s 0 1 1 %s %s A%s %s 0 1 1 %s %s" % (x - rr, 198, rr, rr * 0.32, x + rr, 198, rr, rr * 0.32, x - rr, 198), "a"))
    out.append(line(60, 222, 420, 222, "c"))
    out.append(line(420, 222, 412, 217, "c"))
    out.append(line(420, 222, 412, 227, "c"))
    return out


def echo(uid):
    """Good news and its answer: a small message leaves one person as short
    waves, and comes back from the other as wider, stronger ones."""
    y, ax, bx = 120, 80, 400
    out = [circle(ax, y, 28), circle(bx, y, 28)]
    for i, r in enumerate((14, 24, 34)):
        out.append(path(arc(ax + 30, y, r, -0.45, 0.45), "a" if i == 0 else "b"))
    for i, r in enumerate((30, 56, 82, 108, 134)):
        out.append(path(arc(bx - 34, y, r, math.pi - 0.62, math.pi + 0.62), "a" if i < 3 else "b"))
    return out


def overlap(uid):
    """Default for Relationships: two circles, overlapping, neither inside
    the other."""
    return [circle(205, 120, 72), circle(275, 120, 72), circle(205, 120, 92, "c"), circle(275, 120, 92, "c")]


MOTIFS = dict(loop=loop, fringes=fringes, scatter=scatter, dichotomy=dichotomy, cone=cone, repair=repair, overlap=overlap, muted=muted, regard=regard, spread=spread, slice=slice, echo=echo)


def cover(slug, subject):
    name = BY_SLUG.get(slug) or BY_SUBJECT.get(subject)
    if not name:
        raise SystemExit("no cover motif for %s (%s): add it to covers.BY_SLUG or BY_SUBJECT" % (slug, subject))
    body = "".join(MOTIFS[name](slug))
    return ('<svg class="yt-cv" viewBox="0 0 %d %d" preserveAspectRatio="xMidYMid meet" aria-hidden="true" '
            'focusable="false" fill="none" stroke-width="1" stroke-linecap="round">%s</svg>' % (W, H, body))


if __name__ == "__main__":
    import sys
    print(cover(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else ""))
