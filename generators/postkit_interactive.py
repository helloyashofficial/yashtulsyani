"""postkit_interactive.py :: interactive and editorial components for posts.

Every component renders COMPLETE, readable HTML at build time. The shared
runtime in 01-sidebar.html (POST WIDGETS script) only enhances it:

  calc       inputs + formula outputs. Default results are computed here in
             Python with the same expression language the runtime uses, so a
             reader (or crawler) without JavaScript still sees a worked example.
  checklist  real checkboxes; the runtime adds progress, a verdict band,
             saved state (localStorage, try/catch) and copy-as-Markdown.
  tabs       every panel visible and labelled without JS; ARIA tabs with JS.
  table(sortable/filterable) via itable(): plain table without JS.
  decision   nested <details>, zero JS by design.
  takeaways, callout, compare, flow: static.

Expression language (calc): numbers, names of inputs or earlier outputs,
+ - * / ^, parentheses, unary minus, comparisons < <= > >= == !=, and the
functions min max round floor ceil abs sqrt ln log10 pow if(cond,a,b).
"""
import re, math, json

def _e(s):
    return str(s).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")

def _t(s):
    """text that may already contain inline HTML from the author: only bare & escaped"""
    return re.sub(r"&(?!(#\d+|#x[0-9a-fA-F]+|[a-zA-Z]+);)", "&amp;", str(s))

# ------------------------------------------------------------ expressions
_TOK = re.compile(r"\s*(?:(\d+\.?\d*(?:e[+-]?\d+)?|\.\d+)|([A-Za-z_][A-Za-z0-9_]*)|(<=|>=|==|!=|[-+*/^(),<>]))")
def _safe(f):
    """Mirror JS: NaN/Infinity propagate instead of raising."""
    def g(*a):
        try:
            r = f(*a)
            return float(r) if not isinstance(r, complex) else float("nan")
        except (ValueError, OverflowError, ZeroDivisionError, TypeError):
            return float("nan")
    return g

def _jsmin(*a):
    return float("nan") if any(x != x for x in a) else min(a)  # inf compares like JS

def _jsmax(*a):
    return float("nan") if any(x != x for x in a) else max(a)

FUNCS = {k: _safe(f) for k, f in {"min": _jsmin, "max": _jsmax, "round": lambda x, n=0: math.floor(x * 10 ** int(n) + 0.5) / 10 ** int(n), "floor": math.floor, "ceil": math.ceil,
         "abs": abs, "sqrt": math.sqrt, "ln": math.log, "log10": math.log10, "pow": pow}.items()}

def _tokens(src):
    pos, out = 0, []
    src = src.strip()
    while pos < len(src):
        m = _TOK.match(src, pos)
        if not m or m.end() == pos:
            raise ValueError("bad expression near %r" % src[pos:pos + 12])
        out.append(m.group(1) or m.group(2) or m.group(3))
        pos = m.end()
    return out

def evaluate(src, env):
    toks = _tokens(src); i = [0]
    def peek(): return toks[i[0]] if i[0] < len(toks) else None
    def take(x=None):
        t = peek()
        if x is not None and t != x: raise ValueError("expected %s in %r" % (x, src))
        i[0] += 1; return t
    def comp():
        a = add()
        while peek() in ("<", "<=", ">", ">=", "==", "!="):
            op = take(); b = add()
            a = {"<": a < b, "<=": a <= b, ">": a > b, ">=": a >= b, "==": a == b, "!=": a != b}[op] and 1 or 0
        return a
    def add():
        a = mul()
        while peek() in ("+", "-"):
            op = take(); b = mul(); a = a + b if op == "+" else a - b
        return a
    def mul():
        a = unary()
        while peek() in ("*", "/"):
            op = take(); b = unary()
            a = a * b if op == "*" else (a / b if b != 0 else (float("nan") if a == 0 or a != a else math.copysign(float("inf"), a) * math.copysign(1, b)))
        return a
    def unary():
        if peek() == "-": take(); return -unary()
        if peek() == "+": take(); return unary()
        return power()
    def power():
        a = atom()
        if peek() == "^": take(); b = unary(); return _safe(pow)(a, b)
        return a
    def atom():
        t = take()
        if t is None: raise ValueError("unexpected end in %r" % src)
        if t == "(":
            v = comp(); take(")"); return v
        if re.match(r"^[\d.]", t): return float(t)
        if peek() == "(":
            take("(")
            args = []
            if peek() != ")":
                args.append(comp())
                while peek() == ",": take(); args.append(comp())
            take(")")
            if t == "if": return args[1] if args[0] else args[2]
            if t not in FUNCS: raise ValueError("unknown function %s" % t)
            return float(FUNCS[t](*args))
        if t not in env: raise ValueError("unknown name %s in %r" % (t, src))
        return float(env[t])
    v = comp()
    if i[0] != len(toks): raise ValueError("trailing tokens in %r" % src)
    return v

def fmt(v, kind):
    if v != v or v in (float("inf"), float("-inf")): return "n/a"
    r0 = lambda x: int(math.floor(x + 0.5))   # same rounding as the JS runtime
    if kind == "int": return "{:,}".format(r0(v))
    if kind == "num1": return "{:,.1f}".format(v)
    if kind == "num2": return "{:,.2f}".format(v)
    if kind == "pct": return "{:,.1f}%".format(v)
    if kind == "pct0": return "{:,.0f}%".format(v)
    if kind == "money": return ("-$" if v < 0 else "$") + "{:,}".format(r0(abs(v)))
    if kind == "gbp": return ("-\u00a3" if v < 0 else "\u00a3") + "{:,}".format(r0(abs(v)))
    if kind == "gbp2": return ("-\u00a3" if v < 0 else "\u00a3") + "{:,.2f}".format(abs(v))
    if kind == "money2": return ("-$" if v < 0 else "$") + "{:,.2f}".format(abs(v))
    if kind == "x": return "{:,.1f}x".format(v)
    if kind == "months": return "{:,.1f} months".format(v)
    if kind == "years": return "{:,.1f} years".format(v)
    if kind == "days": return "{:,.0f} days".format(v)
    return "{:,.2f}".format(v)

FORMATS = {"int", "num1", "num2", "pct", "pct0", "money", "money2", "gbp", "gbp2", "x", "months", "years", "days"}

def calc(cid, caption, inputs, outputs, note=None, intro=None):
    """inputs: [dict(name, label, value, unit=None, step=None, min=None, max=None, options=None)]
       outputs: [dict(name=None, label, expr, fmt, hint=None, big=False)]"""
    env, rows_in, rows_out = {}, [], []
    for d in inputs:
        n = d["name"]
        assert re.match(r"^[a-z][a-z0-9_]*$", n), n
        env[n] = float(d["value"])
        lab = '<span class="yt-calc__lbl">%s</span>' % _t(d["label"])
        if d.get("options"):
            opts = "".join('<option value="%s"%s>%s</option>' % (_e(v), " selected" if float(v) == float(d["value"]) else "", _e(t)) for v, t in d["options"])
            ctl = '<select class="yt-calc__ctl" data-v="%s" id="%s-%s">%s</select>' % (n, cid, n, opts)
        else:
            attrs = "".join(' %s="%s"' % (k, d[k]) for k in ("min", "max", "step") if d.get(k) is not None)
            ctl = '<input class="yt-calc__ctl" type="number" inputmode="decimal" data-v="%s" id="%s-%s" value="%s"%s>' % (n, cid, n, d["value"], attrs)
        unit = '<span class="yt-calc__unit">%s</span>' % _e(d["unit"]) if d.get("unit") else ""
        rows_in.append('<label class="yt-calc__in" for="%s-%s">%s<span class="yt-calc__field">%s%s</span></label>' % (cid, n, lab, ctl, unit))
    for d in outputs:
        assert d["fmt"] in FORMATS, d["fmt"]
        v = evaluate(d["expr"], env)
        if d.get("name"):
            env[d["name"]] = v
        name_attr = ' data-name="%s"' % d["name"] if d.get("name") else ""
        hint = '<span class="yt-calc__hint">%s</span>' % _t(d["hint"]) if d.get("hint") else ""
        rows_out.append('<div class="yt-calc__out%s"><span class="yt-calc__olbl">%s</span><output data-expr="%s" data-fmt="%s"%s>%s</output>%s</div>'
                        % (" yt-calc__out--big" if d.get("big") else "", _t(d["label"]), _e(d["expr"]), d["fmt"], name_attr, fmt(v, d["fmt"]), hint))
    out = ['<figure class="yt-viz yt-calc" data-yt-calc id="%s">' % cid,
           '  <figcaption class="yt-viz__cap">%s</figcaption>' % _e(caption)]
    if intro:
        out.append('  <p class="yt-calc__intro">%s</p>' % _t(intro))
    out += ['  <div class="yt-calc__ins">' + "".join(rows_in) + '</div>',
            '  <div class="yt-calc__outs" aria-live="polite">' + "".join(rows_out) + '</div>']
    if note:
        out.append('  <div class="yt-viz__src">%s</div>' % _t(note))
    out.append('</figure>')
    return "\n".join(out)

def checklist(cid, caption, groups, bands=None, note=None):
    """groups: [(title, [item_html, ...])]; bands: [(min_pct, verdict_text)] ascending"""
    assert re.match(r"^[a-z][a-z0-9-]*$", cid), cid
    out = ['<figure class="yt-viz yt-check" data-yt-check="%s"%s>' % (cid, (" data-bands='%s'" % _e(json.dumps(bands))) if bands else ""),
           '  <figcaption class="yt-viz__cap">%s</figcaption>' % _e(caption),
           '  <div class="yt-check__bar" hidden><span class="yt-check__count" aria-live="polite"></span><span class="yt-check__track"><span class="yt-check__fill"></span></span></div>']
    k = 0
    for title, items in groups:
        out.append('  <fieldset class="yt-check__grp"><legend>%s</legend>' % _t(title))
        for it in items:
            k += 1
            out.append('    <label class="yt-check__item"><input type="checkbox" data-k="%d"><span>%s</span></label>' % (k, _t(it)))
        out.append('  </fieldset>')
    out.append('  <p class="yt-check__verdict" hidden aria-live="polite"></p>')
    out.append('  <div class="yt-check__actions" hidden><button type="button" class="yt-check__btn" data-act="copy">Copy as Markdown</button><button type="button" class="yt-check__btn" data-act="reset">Reset</button></div>')
    if note:
        out.append('  <div class="yt-viz__src">%s</div>' % _t(note))
    out.append('</figure>')
    return "\n".join(out)

def tabs(caption, panels, note=None):
    """panels: [(label, html)]"""
    out = ['<figure class="yt-viz yt-tabs" data-yt-tabs>',
           '  <figcaption class="yt-viz__cap">%s</figcaption>' % _e(caption),
           '  <div class="yt-tabs__list" role="tablist" hidden>' + "".join(
               '<button type="button" role="tab" class="yt-tabs__tab">%s</button>' % _e(l) for l, _ in panels) + '</div>']
    for l, h in panels:
        out.append('  <section class="yt-tabs__panel" role="tabpanel"><h3 class="yt-tabs__h">%s</h3>%s</section>' % (_e(l), h))
    if note:
        out.append('  <div class="yt-viz__src">%s</div>' % _t(note))
    out.append('</figure>')
    return "\n".join(out)

def itable(caption, headers, rows, source=None, num_cols=(), sortable=True, filterable=None):
    """A table the runtime makes sortable and, with many rows, filterable."""
    if filterable is None:
        filterable = len(rows) >= 10
    out = ['<figure class="yt-viz">',
           '  <figcaption class="yt-viz__cap">%s</figcaption>' % _e(caption),
           '  <div class="yt-table__wrap">',
           '  <table class="yt-table"%s%s>' % (" data-yt-sort" if sortable else "", " data-yt-filter" if filterable else ""),
           '    <thead><tr>' + "".join('<th scope="col"%s>%s</th>' % (' class="yt-num"' if i in num_cols else "", _t(h)) for i, h in enumerate(headers)) + '</tr></thead>',
           '    <tbody>']
    for r in rows:
        out.append('      <tr>' + "".join('<td%s>%s</td>' % (' class="yt-num"' if i in num_cols else "", _t(c)) for i, c in enumerate(r)) + '</tr>')
    out += ['    </tbody>', '  </table>', '  </div>']
    if source:
        out.append('  <div class="yt-viz__src">%s</div>' % _t(source))
    out.append('</figure>')
    return "\n".join(out)

def decision(caption, tree, note=None):
    """tree: (question, [(answer_label, subtree | outcome_html)]). Zero JS: nested <details>."""
    def node(t, depth):
        if isinstance(t, str):
            return '<div class="yt-dec__out">%s</div>' % _t(t)
        q, opts = t
        h = '<div class="yt-dec__q">%s</div>' % _t(q)
        for lab, sub in opts:
            h += '<details class="yt-dec__opt"><summary>%s</summary>%s</details>' % (_t(lab), node(sub, depth + 1))
        return h
    out = ['<figure class="yt-viz yt-dec">',
           '  <figcaption class="yt-viz__cap">%s</figcaption>' % _e(caption),
           '  ' + node(tree, 0)]
    if note:
        out.append('  <div class="yt-viz__src">%s</div>' % _t(note))
    out.append('</figure>')
    return "\n".join(out)

def takeaways(items, title="Key takeaways"):
    return ('<aside class="yt-kt" aria-label="%s"><div class="yt-kt__h">%s</div><ul>%s</ul></aside>'
            % (_e(title), _e(title), "".join("<li>%s</li>" % _t(i) for i in items)))

CALLOUT_LABEL = {"tip": "Tip", "warn": "Watch out", "example": "Worked example", "definition": "Definition", "note": "Note", "template": "Template"}

def callout(kind, title, html):
    assert kind in CALLOUT_LABEL, kind
    return ('<aside class="yt-cl yt-cl--%s"><div class="yt-cl__k">%s</div>%s<div class="yt-cl__b">%s</div></aside>'
            % (kind, CALLOUT_LABEL[kind], ('<div class="yt-cl__t">%s</div>' % _t(title)) if title else "", _t(html)))

def compare(caption, cols, source=None):
    """cols: [(title, [pros], [cons], verdict_or_None)]"""
    out = ['<figure class="yt-viz">', '  <figcaption class="yt-viz__cap">%s</figcaption>' % _e(caption), '  <div class="yt-cmp">']
    for title, pros, cons, verdict in cols:
        out.append('    <div class="yt-cmp__col"><div class="yt-cmp__t">%s</div>' % _t(title)
                   + ('<div class="yt-cmp__k">Strengths</div><ul class="yt-cmp__pro">%s</ul>' % "".join("<li>%s</li>" % _t(p) for p in pros) if pros else "")
                   + ('<div class="yt-cmp__k">Limits</div><ul class="yt-cmp__con">%s</ul>' % "".join("<li>%s</li>" % _t(c) for c in cons) if cons else "")
                   + ('<div class="yt-cmp__v">%s</div>' % _t(verdict) if verdict else "") + '</div>')
    out.append('  </div>')
    if source:
        out.append('  <div class="yt-viz__src">%s</div>' % _t(source))
    out.append('</figure>')
    return "\n".join(out)

def flow(caption, steps, source=None):
    """steps: [(title, text)] left-to-right on desktop, top-to-bottom on phones"""
    out = ['<figure class="yt-viz">', '  <figcaption class="yt-viz__cap">%s</figcaption>' % _e(caption), '  <ol class="yt-flow">']
    for i, (t, x) in enumerate(steps):
        out.append('    <li class="yt-flow__s"><span class="yt-flow__n">%d</span><span class="yt-flow__t">%s</span><span class="yt-flow__x">%s</span></li>' % (i + 1, _t(t), _t(x)))
    out.append('  </ol>')
    if source:
        out.append('  <div class="yt-viz__src">%s</div>' % _t(source))
    out.append('</figure>')
    return "\n".join(out)
