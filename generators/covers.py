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
    "what-rumination-is": "coil",
    "what-epicurus-meant-by-pleasure": "settle",
    "what-entanglement-is": "pair",
    "what-mctaggart-meant-by-the-unreality-of-time": "series",
    "what-the-michelangelo-phenomenon-says": "ideal",
    "what-the-spotlight-effect-is": "spotlight",
    "what-aristotle-meant-by-the-three-kinds-of-friendship": "three",
    "why-looking-at-the-sky-means-looking-into-the-past": "lookback",
    "what-physicists-mean-by-extra-dimensions": "curled",
    "what-the-demand-withdraw-pattern-is": "pursue",
    "what-learned-helplessness-actually-showed": "barrier",
    "what-spinoza-meant-by-hope-and-fear": "waver",
    "what-time-dilation-is": "ticks",
    "what-a-tesseract-is": "hypercube",
    "what-the-research-says-about-love-languages": "channels",
    "what-the-impostor-phenomenon-is": "doubled",
    "what-montaigne-meant-by-because-it-was-he": "seam",
    "what-the-uncertainty-principle-says": "bells",
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


def coil(uid):
    """Rumination: a line arrives, then loops back over itself again and
    again, barely moving forward, before it finally leaves."""
    cy = 120
    out = [line(40, cy + 34, 150, cy + 34)]
    pts = []
    n = 1400
    loops = 11
    for i in range(n + 1):
        t = i / float(n) * loops * 2 * math.pi
        r = 34 - 10 * math.sin(math.pi * i / n)
        x = 150 + t * 2.6 - r * math.sin(t)
        y = cy + r * math.cos(t)
        pts.append((x, y))
    out.append(path("M" + " L".join("%s %s" % (f(x), f(y)) for x, y in pts[::4])))
    ex = pts[-1][0]
    out.append(line(ex, cy + 34, 440, cy + 34, "b", ' stroke-dasharray="2 5"'))
    return out


def settle(uid):
    """Epicurean pleasure as rest: a disturbed line that grows calmer and
    calmer until it lies flat, with a still point where it comes to rest."""
    cy = 120
    k = 2 * math.pi / 56.0
    pts = []
    for x in range(40, 441, 2):
        u = (x - 40) / 400.0
        amp = 46 * math.exp(-4.2 * u) * (1 - u)
        pts.append((x, cy - amp * math.sin((x - 40) * k)))
    out = [path("M" + " L".join("%s %s" % (f(x), f(y)) for x, y in pts))]
    for i, r in enumerate((10, 20, 30)):
        out.append(path("M%s %s A%s %s 0 0 0 %s %s" % (f(400 - r), cy + 22, r, f(r * 0.28), f(400 + r), cy + 22), "c" if i else "b"))
    out.append(dot(400, cy, 2.6))
    return out


def pair(uid):
    """Entanglement: two particles far apart, each measured along a setting,
    with outcomes that always come out opposite. The link between them is
    drawn faint and dashed: a correlation, not a signal."""
    cy = 120
    ax, bx = 92, 388
    out = [circle(ax, cy, 16), circle(bx, cy, 16)]
    out.append(line(ax, cy + 10, ax, cy - 10))
    out.append(line(ax, cy - 10, ax - 4, cy - 4))
    out.append(line(ax, cy - 10, ax + 4, cy - 4))
    out.append(line(bx, cy - 10, bx, cy + 10))
    out.append(line(bx, cy + 10, bx - 4, cy + 4))
    out.append(line(bx, cy + 10, bx + 4, cy + 4))
    out.append(path("M%s %s Q %s %s %s %s" % (ax + 22, cy, 240, cy - 70, bx - 22, cy), "c", ' stroke-dasharray="2 6"'))
    for x in (ax, bx):
        out.append(line(x - 34, cy + 46, x + 34, cy + 46, "b"))
        out.append(line(x, cy + 26, x, cy + 46, "c"))
    out.append(dot(240, cy, 3))
    out.append(line(232, cy, ax + 24, cy, "b", ' stroke-dasharray="1 5"'))
    out.append(line(248, cy, bx - 24, cy, "b", ' stroke-dasharray="1 5"'))
    return out


def series(uid):
    """McTaggart's two series: a fixed row of events in earlier-later order
    (the B series), and above it a marker for the present that seems to
    move along them (the A series), with its earlier positions fading."""
    cy = 150
    out = [line(40, cy, 440, cy, "b")]
    xs = [70, 130, 190, 250, 310, 370, 420]
    for x in xs:
        out.append(dot(x, cy, 3))
    now = 250
    out.append(line(now, cy - 14, now, 70))
    out.append(path("M%s 70 L%s 58 L%s 58 Z" % (now, now - 8, now + 8)))
    for i, x in enumerate((190, 130)):
        out.append(line(x, cy - 14, x, 82 + i * 12, "c", ' stroke-dasharray="2 4"'))
    out.append(path("M%s 46 Q %s 30 %s 46" % (now - 40, now + 10, now + 60), "b"))
    out.append(line(now + 60, 46, now + 52, 42, "b"))
    out.append(line(now + 60, 46, now + 53, 52, "b"))
    return out


def ideal(uid):
    """The Michelangelo phenomenon: you as a small circle inside a dashed
    outline of the person you want to be, and a partner beside you whose
    attention reaches that outline, not the circle as it is now."""
    cy = 120
    cx = 290
    out = [circle(cx, cy, 34), circle(cx, cy, 70, "b", ' stroke-dasharray="3 5"')]
    px = 130
    out.append(circle(px, cy, 22))
    for dy in (-40, 0, 40):
        ty = cy + dy
        tx = cx - math.sqrt(max(0, 70 ** 2 - dy ** 2))
        out.append(line(px + 26, cy + dy * 0.35, tx - 4, ty, "c"))
    return out


def spotlight(uid):
    """The spotlight effect: a cone of light falling on one person in a
    crowd, as it feels from inside, while only a few of the people around
    are actually turned towards them."""
    cx, cy = 240, 168
    out = [path("M%s 20 L%s %s M%s 20 L%s %s" % (cx - 8, cx - 46, cy + 14, cx + 8, cx + 46, cy + 14), "c")]
    out.append(path("M%s %s A46 9 0 1 0 %s %s A46 9 0 1 0 %s %s" % (cx - 46, cy + 14, cx + 46, cy + 14, cx - 46, cy + 14), "b", ' stroke-dasharray="2 4"'))
    out.append(circle(cx, cy - 14, 9))
    out.append(line(cx, cy - 5, cx, cy + 12))
    crowd = [(96, 120), (128, 186), (150, 92), (330, 96), (352, 182), (388, 132), (70, 170), (410, 196), (300, 210), (180, 214)]
    looking = {(150, 92), (352, 182)}
    for x, y in crowd:
        out.append(dot(x, y, 3, "b"))
        if (x, y) in looking:
            dx, dy = cx - x, (cy - 14) - y
            n = math.hypot(dx, dy)
            out.append(line(x + dx / n * 8, y + dy / n * 8, x + dx / n * 22, y + dy / n * 22, "b"))
    return out


def three(uid):
    """Aristotle's three friendships, as three pairs: one held together only
    by a thin dashed line (utility), one barely touching (pleasure), and one
    in which the two circles share a large part of each other (the good)."""
    cy = 120
    out = []
    out += [circle(64, cy, 20, "b"), circle(136, cy, 20, "b"), line(84, cy, 116, cy, "c", ' stroke-dasharray="2 4"')]
    out += [circle(222, cy, 24, "b"), circle(266, cy, 24, "b")]
    out += [circle(366, cy, 30), circle(398, cy, 30)]
    out.append(dot(382, cy, 2.6))
    return out


def lookback(uid):
    """Light that left a star long ago: wavefronts spreading from a point on
    the left, fading as they go, with the newest close to the star and the
    oldest only now reaching an observer on the right."""
    cy = 120
    sx = 70
    out = [dot(sx, cy, 3.4)]
    for i, r in enumerate((40, 90, 145, 205, 270, 340)):
        a0 = -math.asin(min(1.0, 96.0 / r))
        cls = "a" if i == 5 else ("b" if i >= 3 else "c")
        out.append(path(arc(sx, cy, r, a0, -a0), cls))
    ox = sx + 340
    out.append(circle(ox + 16, cy, 9))
    out.append(line(ox + 16, cy + 9, ox + 16, cy + 30, "b"))
    return out


def curled(uid):
    """A hidden dimension: from far away a thin line, and close up a tube,
    each point of the line really a small circle that was too tight to see."""
    cy = 120
    out = [line(40, cy, 196, cy, "b")]
    out.append(circle(196, cy, 16, "c", ' stroke-dasharray="2 4"'))
    out.append(line(212, cy - 4, 236, cy - 26, "c", ' stroke-dasharray="2 4"'))
    out.append(line(212, cy + 4, 236, cy + 26, "c", ' stroke-dasharray="2 4"'))
    r = 26
    out.append(line(246, cy - r, 430, cy - r))
    out.append(line(246, cy + r, 430, cy + r))
    for i, x in enumerate(range(246, 431, 30)):
        out.append(path("M%s %s A9 %s 0 1 1 %s %s A9 %s 0 1 1 %s %s" % (x, cy - r, r, x, cy + r, r, x, cy - r), "a" if i in (0, 6) else "b"))
    return out


def pursue(uid):
    """Demand and withdraw as a loop: two figures on the same closed track,
    one following the other round, neither ever catching up."""
    cx, cy, rx, ry = 240, 120, 150, 62
    def at(t):
        return cx + rx * math.cos(t), cy + ry * math.sin(t)
    out = []
    stops = (math.radians(200), math.radians(330))
    seg = []
    for i in range(361):
        t = math.radians(i)
        x, y = at(t)
        near = False
        for st in stops:
            sx, sy = at(st)
            if math.hypot(x - sx, y - sy) < 19:
                near = True
        if near:
            if len(seg) > 1:
                out.append(path("M" + " L".join("%s %s" % (f(px), f(py)) for px, py in seg), "b", ' stroke-dasharray="3 6"'))
            seg = []
        else:
            seg.append((x, y))
    if len(seg) > 1:
        out.append(path("M" + " L".join("%s %s" % (f(px), f(py)) for px, py in seg), "b", ' stroke-dasharray="3 6"'))
    for t, cls in ((math.radians(200), "a"), (math.radians(330), "a")):
        x, y = at(t)
        out.append(circle(x, y, 15, cls))
    for t in (math.radians(255), math.radians(30), math.radians(120)):
        x, y = at(t)
        dx, dy = -rx * math.sin(t), ry * math.cos(t)
        n = math.hypot(dx, dy); ux, uy = dx / n, dy / n
        for sg in (-1, 1):
            ang = math.radians(28) * sg
            vx = ux * math.cos(ang) - uy * math.sin(ang); vy = ux * math.sin(ang) + uy * math.cos(ang)
            out.append(line(x, y, x - 10 * vx, y - 10 * vy))
    return out



def waver(uid):
    """Spinoza on hope and fear: a line swinging between two faint limits,
    the swings shrinking as it goes, until it runs level between them."""
    cy = 120
    out = [line(60, cy - 44, 420, cy - 44, "c", ' stroke-dasharray="2 5"'),
           line(60, cy + 44, 420, cy + 44, "c", ' stroke-dasharray="2 5"')]
    pts = []
    n = 600
    for i in range(n + 1):
        x = 60 + 300.0 * i / n
        amp = 40 * (1 - float(i) / n) ** 1.6
        y = cy - amp * math.sin(i / float(n) * 7 * 2 * math.pi)
        pts.append((x, y))
    out.append(path("M" + " L".join("%s %s" % (f(x), f(y)) for x, y in pts[::3])))
    out.append(line(360, cy, 420, cy))
    out.append(dot(420, cy, 3))
    return out


def ticks(uid):
    """Time dilation: two clocks drawn as tick tracks, one above the other.
    Over the same stretch the upper track fits one more tick, because the
    higher clock runs a little faster."""
    out = []
    for y, n, c in ((92, 13, "a"), (156, 12, "b")):
        out.append(line(90, y, 390, y, c))
        for i in range(n + 1):
            x = 90 + 300.0 * i / n
            out.append(line(x, y - 9, x, y + 9, c))
    out.append(line(240, 112, 240, 136, "c", ' stroke-dasharray="2 4"'))
    return out


def hypercube(uid):
    """The tesseract as it is usually drawn: a cube inside a cube, each
    corner of the inner one joined to the matching corner of the outer."""
    def cube(cx, cy, w, d):
        h = w / 2.0
        front = [(cx - h, cy - h), (cx + h, cy - h), (cx + h, cy + h), (cx - h, cy + h)]
        back = [(x + d, y - d) for x, y in front]
        return front, back
    out = []
    of, ob = cube(232, 128, 150, 34)
    inf, inb = cube(232, 128, 62, 14)
    for (fr, bk), c in (((of, ob), "a"), ((inf, inb), "b")):
        for ring in (fr, bk):
            for i in range(4):
                x1, y1 = ring[i]
                x2, y2 = ring[(i + 1) % 4]
                out.append(line(x1, y1, x2, y2, c))
        for (x1, y1), (x2, y2) in zip(fr, bk):
            out.append(line(x1, y1, x2, y2, c))
    for (x1, y1), (x2, y2) in zip(of + ob, inf + inb):
        out.append(line(x1, y1, x2, y2, "c", ' stroke-dasharray="2 4"'))
    return out


def channels(uid):
    """Love languages, read as a balanced diet: two people joined not by one
    line but by several, of equal weight."""
    out = [circle(110, 120, 16), circle(370, 120, 16)]
    for k, off in enumerate((-56, -28, 0, 28, 56)):
        out.append(path("M126 120 Q 240 %s 354 120" % (120 + off * 1.6), "a" if k % 2 == 0 else "b"))
    return out


def doubled(uid):
    """The impostor phenomenon: a solid figure and, slightly behind it, a
    dashed copy of the same figure, the self someone fears being seen as."""
    out = [circle(214, 112, 30), path("M160 196 Q 214 132 268 196")]
    out.append(circle(262, 104, 30, "c", ' stroke-dasharray="3 5"'))
    out.append(path("M208 188 Q 262 124 316 188", "c", ' stroke-dasharray="3 5"'))
    return out


def seam(uid):
    """Montaigne on friendship: two lines that come in from apart and run
    together into one, with no sign of the seam where they joined."""
    out = [path("M60 70 C 170 70, 200 120, 260 120"),
           path("M60 170 C 170 170, 200 120, 260 120"),
           line(260, 120, 420, 120)]
    out.append(dot(60, 70, 3))
    out.append(dot(60, 170, 3))
    return out


def bells(uid):
    """The uncertainty relation drawn as two distributions: a narrow, tall
    one for a sharply defined quantity and a wide, low one for its partner."""
    base = 180
    def bell(cx, sd, h, step=2):
        pts = []
        x = cx - 4 * sd
        while x <= cx + 4 * sd:
            y = base - h * math.exp(-((x - cx) ** 2) / (2.0 * sd * sd))
            pts.append((x, y))
            x += step
        return "M" + " L".join("%s %s" % (f(px), f(py)) for px, py in pts)
    out = [line(40, base, 440, base, "c")]
    out.append(path(bell(140, 12, 120)))
    out.append(path(bell(330, 34, 42), "b"))
    return out

def barrier(uid):
    """The shuttle box, reduced to lines: a floor with a low barrier in the
    middle, a figure still on the first side, and the arc of the jump it
    could make, drawn faint because it is not made."""
    cy = 172
    out = [line(60, cy, 420, cy, "b")]
    out.append(line(240, cy, 240, cy - 34))
    out.append(circle(160, cy - 16, 14))
    out.append(path("M174 %s Q 240 %s 306 %s" % (cy - 26, cy - 110, cy - 26), "c", ' stroke-dasharray="3 5"'))
    out.append(line(306, cy - 26, 298, cy - 34, "c"))
    out.append(line(306, cy - 26, 296, cy - 24, "c"))
    out.append(circle(320, cy - 16, 14, "c", ' stroke-dasharray="2 4"'))
    return out


def overlap(uid):
    """Default for Relationships: two circles, overlapping, neither inside
    the other."""
    return [circle(205, 120, 72), circle(275, 120, 72), circle(205, 120, 92, "c"), circle(275, 120, 92, "c")]


MOTIFS = dict(loop=loop, fringes=fringes, scatter=scatter, dichotomy=dichotomy, cone=cone, repair=repair, overlap=overlap, muted=muted, regard=regard, spread=spread, slice=slice, echo=echo, coil=coil, settle=settle, pair=pair, series=series, ideal=ideal, spotlight=spotlight, three=three, lookback=lookback, curled=curled, pursue=pursue, barrier=barrier, waver=waver, ticks=ticks, hypercube=hypercube, channels=channels, doubled=doubled, seam=seam, bells=bells)


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
