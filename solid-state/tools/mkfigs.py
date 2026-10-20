#!/usr/bin/env python3
"""Generate the ELE 717 figures as inline-ready SVG.

Axes and labels use currentColor so they follow the page's ink in both themes;
the signal itself uses the page's copper accent via a CSS variable with a
literal fallback.
"""
import math, os

OUT = "/home/user/claude/solid-state/figures"
os.makedirs(OUT, exist_ok=True)

INK   = 'currentColor'
SIG   = 'var(--copper,#B4622F)'
SIG2  = 'var(--teal,#1C6E7E)'

def plain(s):
    return (s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))


ZW = "\u200b"   # zero-width carrier for the baseline-restoring dy


def esc(s):
    """Escape a label and set X_{ab}, X_ab and X^{ab} as real sub/superscripts."""
    import re
    s = plain(s)
    def sub(m):
        return (f'<tspan dy="0.32em" font-size="72%">{m.group(1) or m.group(2)}</tspan>'
                f'<tspan dy="-0.32em">{ZW}</tspan>')
    def sup(m):
        return (f'<tspan dy="-0.45em" font-size="72%">{m.group(1)}</tspan>'
                f'<tspan dy="0.45em">{ZW}</tspan>')
    s = re.sub(r"_\{([^}]*)\}|_([A-Za-z0-9]+)", sub, s)
    s = re.sub(r"\^\{([^}]*)\}", sup, s)
    return s


class Panel:
    """One set of axes. Data coords -> SVG coords."""
    def __init__(self, x0, y0, w, h, xr, yr):
        self.x0, self.y0, self.w, self.h = x0, y0, w, h
        self.xmin, self.xmax = xr
        self.ymin, self.ymax = yr
        self.p = []

    def X(self, x):
        return self.x0 + (x - self.xmin) / (self.xmax - self.xmin) * self.w

    def Y(self, y):
        return self.y0 + self.h - (y - self.ymin) / (self.ymax - self.ymin) * self.h

    # --- primitives -------------------------------------------------------
    def line(self, x1, y1, x2, y2, color=INK, w=1, dash=None, op=1.0):
        d = f' stroke-dasharray="{dash}"' if dash else ''
        self.p.append(f'<line x1="{self.X(x1):.1f}" y1="{self.Y(y1):.1f}" '
                      f'x2="{self.X(x2):.1f}" y2="{self.Y(y2):.1f}" '
                      f'style="stroke:{color}" stroke-width="{w}" opacity="{op}"{d}/>')

    def dot(self, x, y, color=SIG, r=3.2):
        self.p.append(f'<circle cx="{self.X(x):.1f}" cy="{self.Y(y):.1f}" r="{r}" '
                      f'style="fill:{color}"/>')

    def hollow(self, x, y, color=SIG, r=3.2):
        self.p.append(f'<circle cx="{self.X(x):.1f}" cy="{self.Y(y):.1f}" r="{r}" '
                      f'style="fill:none;stroke:{color}" stroke-width="1.4"/>')

    def text(self, x, y, s, anchor="middle", dx=0, dy=0, size=11, color=INK,
             italic=False, op=1.0):
        st = f'font-style:italic;' if italic else ''
        self.p.append(f'<text x="{self.X(x)+dx:.1f}" y="{self.Y(y)+dy:.1f}" '
                      f'text-anchor="{anchor}" font-size="{size}" '
                      f'style="fill:{color};{st}" opacity="{op}">{esc(s)}</text>')

    def raw_text(self, px, py, s, anchor="middle", size=11, color=INK, weight=None):
        w = f' font-weight="{weight}"' if weight else ''
        self.p.append(f'<text x="{px:.1f}" y="{py:.1f}" text-anchor="{anchor}" '
                      f'font-size="{size}" style="fill:{color}"{w}>{esc(s)}</text>')

    # --- composites -------------------------------------------------------
    def axes(self, xlabel="t", ylabel=None, xticks=(), yticks=(), ytick_fmt="{:g}"):
        y0 = 0 if self.ymin < 0 < self.ymax else self.ymin
        self.p.append(f'<line x1="{self.X(self.xmin):.1f}" y1="{self.Y(y0):.1f}" '
                      f'x2="{self.X(self.xmax)-6:.1f}" y2="{self.Y(y0):.1f}" '
                      f'style="stroke:{INK}" stroke-width="1" opacity=".55" '
                      f'marker-end="url(#ar)"/>')
        xa = 0 if self.xmin < 0 < self.xmax else self.xmin
        self.p.append(f'<line x1="{self.X(xa):.1f}" y1="{self.Y(self.ymin):.1f}" '
                      f'x2="{self.X(xa):.1f}" y2="{self.Y(self.ymax)+6:.1f}" '
                      f'style="stroke:{INK}" stroke-width="1" opacity=".55" '
                      f'marker-end="url(#ar)"/>')
        self.raw_text(self.X(self.xmax) + 4, self.Y(y0) + 4, xlabel,
                      anchor="start", size=11, color=INK)
        if ylabel:
            self.raw_text(self.X(xa) + 5, self.Y(self.ymax) + 2, ylabel,
                          anchor="start", size=11, color=INK)
        for t in xticks:
            self.line(t, -0.06 * (self.ymax - self.ymin), t, 0.06 * (self.ymax - self.ymin),
                      INK, 1, op=.55)
            self.text(t, y0, "{:g}".format(t), dy=15, size=10, op=.75)
        for t in yticks:
            self.line(self.xmin + 0.02 * (self.xmax - self.xmin), t,
                      self.xmin + 0.05 * (self.xmax - self.xmin), t, INK, 1, op=.55)
            self.text(xa, t, ytick_fmt.format(t), anchor="end", dx=-5, dy=4,
                      size=10, op=.75)

    def stems(self, pts, color=SIG):
        for x, y in pts:
            if abs(y) > 1e-12:
                self.line(x, 0, x, y, color, 1.8)
            self.dot(x, y, color)

    def curve(self, pts, color=SIG, w=2, dash=None):
        d = f' stroke-dasharray="{dash}"' if dash else ''
        s = " ".join(f"{self.X(x):.1f},{self.Y(y):.1f}" for x, y in pts)
        self.p.append(f'<polyline points="{s}" fill="none" '
                      f'style="stroke:{color}" stroke-width="{w}" '
                      f'stroke-linejoin="round" stroke-linecap="round"{d}/>')

    def title(self, s, size=11.5):
        self.p.append(f'<text x="{self.x0 + self.w/2:.1f}" y="{self.y0 - 9:.1f}" '
                      f'text-anchor="middle" font-size="{size}" '
                      f'style="fill:{INK}" opacity=".85">{esc(s)}</text>')


def svg(width, height, panels, aria):
    body = "".join("".join(p.p) for p in panels)
    return (f'<svg viewBox="0 0 {width} {height}" role="img" aria-label="{esc(aria)}" '
            f'style="max-width:100%;height:auto;display:block;margin:0 auto">'
            f'<defs><marker id="ar" viewBox="0 0 10 10" refX="9" refY="5" '
            f'markerWidth="5" markerHeight="5" orient="auto-start-reverse">'
            f'<path d="M0,1 L9,5 L0,9 z" style="fill:{INK}" opacity=".55"/></marker></defs>'
            f'{body}</svg>')


def write(name, content):
    with open(os.path.join(OUT, name), "w", encoding="utf-8") as f:
        f.write(content)
    print("  ", name, len(content), "bytes")


def samp(f, a, b, n=160):
    return [(a + (b - a) * i / n, f(a + (b - a) * i / n)) for i in range(n + 1)]


# =====================================================================
# Raw-coordinate drawing, for schematics that are not graphs
# =====================================================================
SOFT  = 'var(--teal-soft,#E0EEF1)'
SOFT2 = 'var(--copper-soft,#F3E7DE)'
SANS  = '"IBM Plex Sans Condensed",system-ui,sans-serif'


class Sketch:
    """Pixel-coordinate primitives collected into one drawing."""
    def __init__(self):
        self.p = []

    def line(self, x1, y1, x2, y2, color=INK, w=1.2, dash=None, op=1.0, arrow=None):
        d = f' stroke-dasharray="{dash}"' if dash else ''
        m = ''
        if arrow == 'end':   m = ' marker-end="url(#ar)"'
        if arrow == 'both':  m = ' marker-start="url(#ar)" marker-end="url(#ar)"'
        if arrow == 'sig':   m = ' marker-end="url(#ars)"'
        if arrow == 'sig2':  m = ' marker-end="url(#art)"'
        self.p.append(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" '
                      f'style="stroke:{color}" stroke-width="{w}" opacity="{op}"{d}{m}/>')

    def poly(self, pts, color=INK, w=1.6, fill='none', dash=None, op=1.0, close=False, fop=1.0):
        d = f' stroke-dasharray="{dash}"' if dash else ''
        s = " ".join(f"{x:.1f},{y:.1f}" for x, y in pts)
        tag = 'polygon' if close else 'polyline'
        self.p.append(f'<{tag} points="{s}" style="fill:{fill};stroke:{color}" '
                      f'fill-opacity="{fop}" stroke-width="{w}" opacity="{op}" '
                      f'stroke-linejoin="round"{d}/>')

    def rect(self, x, y, w, h, fill='none', stroke=INK, sw=1.2, rx=0, op=1.0, dash=None):
        d = f' stroke-dasharray="{dash}"' if dash else ''
        self.p.append(f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" rx="{rx}" '
                      f'style="fill:{fill};stroke:{stroke}" stroke-width="{sw}" opacity="{op}"{d}/>')

    def circle(self, x, y, r=3, fill=INK, stroke='none', sw=1.2):
        self.p.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" '
                      f'style="fill:{fill};stroke:{stroke}" stroke-width="{sw}"/>')

    def path(self, d, color=INK, w=1.4, fill='none', dash=None, op=1.0, arrow=None):
        da = f' stroke-dasharray="{dash}"' if dash else ''
        m = ' marker-end="url(#ar)"' if arrow == 'end' else (' marker-end="url(#ars)"' if arrow == 'sig' else '')
        self.p.append(f'<path d="{d}" style="fill:{fill};stroke:{color}" stroke-width="{w}" '
                      f'opacity="{op}" stroke-linejoin="round"{da}{m}/>')

    def text(self, x, y, s, anchor="middle", size=11, color=INK, italic=False, weight=None, op=1.0):
        st = 'font-style:italic;' if italic else ''
        w = f' font-weight="{weight}"' if weight else ''
        self.p.append(f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{anchor}" font-size="{size}" '
                      f'style="fill:{color};{st}" opacity="{op}"{w}>{esc(s)}</text>')

    def hole(self, x, y, r=3.2):
        self.circle(x, y, r, fill='var(--surface,#fff)', stroke=INK, sw=1.2)

    def electron(self, x, y, r=3.2):
        self.circle(x, y, r, fill=INK)


def figure(width, height, layers, aria):
    """Like svg(), with a sans label face and accent-coloured arrowheads."""
    body = "".join("".join(l.p) for l in layers)
    return (f'<svg viewBox="0 0 {width} {height}" role="img" aria-label="{plain(aria)}" '
            f'style="width:{width}px;max-width:100%;height:auto;display:block;margin:0 auto;font-family:{SANS}">'
            f'<defs>'
            f'<marker id="ar" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="5" markerHeight="5" '
            f'orient="auto-start-reverse"><path d="M0,1 L9,5 L0,9 z" style="fill:{INK}" opacity=".7"/></marker>'
            f'<marker id="ars" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="5" markerHeight="5" '
            f'orient="auto-start-reverse"><path d="M0,1 L9,5 L0,9 z" style="fill:{SIG}"/></marker>'
            f'<marker id="art" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="5" markerHeight="5" '
            f'orient="auto-start-reverse"><path d="M0,1 L9,5 L0,9 z" style="fill:{SIG2}"/></marker>'
            f'</defs>{body}</svg>')


def _axes(self, xlabel="t", ylabel=None, xticks=(), yticks=(), ytick_fmt="{:g}"):
    y0 = 0 if self.ymin < 0 < self.ymax else self.ymin
    xa = 0 if self.xmin < 0 < self.xmax else self.xmin
    dx = self.xmax - self.xmin
    self.p.append(f'<line x1="{self.X(self.xmin):.1f}" y1="{self.Y(y0):.1f}" '
                  f'x2="{self.X(self.xmax)-6:.1f}" y2="{self.Y(y0):.1f}" '
                  f'style="stroke:{INK}" stroke-width="1" opacity=".55" marker-end="url(#ar)"/>')
    self.p.append(f'<line x1="{self.X(xa):.1f}" y1="{self.Y(self.ymin):.1f}" '
                  f'x2="{self.X(xa):.1f}" y2="{self.Y(self.ymax)+6:.1f}" '
                  f'style="stroke:{INK}" stroke-width="1" opacity=".55" marker-end="url(#ar)"/>')
    self.raw_text(self.X(self.xmax) + 4, self.Y(y0) + 4, xlabel, anchor="start", size=11, color=INK)
    if ylabel:
        self.raw_text(self.X(xa) + 5, self.Y(self.ymax) + 2, ylabel, anchor="start", size=11, color=INK)
    for t in xticks:
        self.p.append(f'<line x1="{self.X(t):.1f}" y1="{self.Y(y0)-4:.1f}" x2="{self.X(t):.1f}" '
                      f'y2="{self.Y(y0)+4:.1f}" style="stroke:{INK}" stroke-width="1" opacity=".55"/>')
        self.text(t, y0, "{:g}".format(t), dy=15, size=10, op=.75)
    for t in yticks:
        self.p.append(f'<line x1="{self.X(xa)-4:.1f}" y1="{self.Y(t):.1f}" x2="{self.X(xa)+4:.1f}" '
                      f'y2="{self.Y(t):.1f}" style="stroke:{INK}" stroke-width="1" opacity=".55"/>')
        self.text(xa, t, ytick_fmt.format(t), anchor="end", dx=-6, dy=4, size=10, op=.75)

Panel.axes = _axes


def erfc(x):
    return math.erfc(x)


# =====================================================================
# M01  band pictures: metal, semiconductor, insulator
# =====================================================================
s = Sketch()
cols = [("Metal", 30), ("Semiconductor", 230), ("Insulator", 430)]
W_, top, bot = 140, 40, 210
for name, x in cols:
    s.text(x + W_/2, 24, name, size=12.5, weight=600)
# metal: one band, lower part filled
x = 30
s.rect(x, 70, W_, 110, fill='none')
s.rect(x, 120, W_, 60, fill=SOFT, stroke='none')
s.rect(x, 70, W_, 110, fill='none')
s.line(x - 6, 120, x + W_ + 6, 120, SIG, 1.6, dash="5 3")
s.text(x + W_ + 8, 124, "E_F", anchor="start", size=10.5, color=SIG)
s.text(x + W_/2, 100, "empty states", size=10, op=.75)
s.text(x + W_/2, 155, "filled states", size=10, op=.75)
s.text(x + W_/2, 205, "partly filled band, no gap", size=10.5, op=.85)
# semiconductor: small gap
x = 230
s.rect(x, 50, W_, 55, fill='none')
s.rect(x, 135, W_, 55, fill=SOFT, stroke=INK)
for i in range(4):
    s.electron(x + 25 + i*30, 98)
    s.hole(x + 25 + i*30, 142)
s.line(x + W_ + 10, 105, x + W_ + 10, 135, INK, 1, arrow='both', op=.8)
s.text(x + W_ + 15, 124, "E_g ≈ 1 eV", anchor="start", size=10.5)
s.text(x + W_/2, 72, "conduction band", size=10, op=.75)
s.text(x + W_/2, 170, "valence band", size=10, op=.75)
s.text(x + W_/2, 205, "small gap, a few carriers", size=10.5, op=.85)
# insulator: wide gap
x = 430
s.rect(x, 40, W_, 40, fill='none')
s.rect(x, 150, W_, 40, fill=SOFT, stroke=INK)
s.line(x + W_ + 10, 80, x + W_ + 10, 150, INK, 1, arrow='both', op=.8)
s.text(x + W_ + 15, 119, "E_g > 4 eV", anchor="start", size=10.5)
s.text(x + W_/2, 64, "conduction band", size=10, op=.75)
s.text(x + W_/2, 174, "valence band", size=10, op=.75)
s.text(x + W_/2, 205, "wide gap, no carriers", size=10.5, op=.85)
# energy axis
s.line(12, 195, 12, 45, INK, 1, arrow='end', op=.7)
s.text(18, 50, "E", anchor="start", size=11, italic=True)
write("bands.svg", figure(660, 220, [s],
      "Band diagrams of a metal with a partly filled band, a semiconductor with a small gap, and an insulator with a wide gap"))


# =====================================================================
# M02  cube planes (100), (110), (111) and the (326) plane
# =====================================================================
def proj(ox, oy, sc):
    def f(x, y, z):
        return (ox + sc*(y - 0.55*x), oy - sc*z + sc*0.32*x)
    return f

s = Sketch()
planes = [("(100)", [(1,0,0),(1,1,0),(1,1,1),(1,0,1)]),
          ("(110)", [(1,0,0),(0,1,0),(0,1,1),(1,0,1)]),
          ("(111)", [(1,0,0),(0,1,0),(0,0,1)])]
corners = [(x,y,z) for x in (0,1) for y in (0,1) for z in (0,1)]
edges = [(a,b) for a in corners for b in corners
         if a < b and sum(abs(a[i]-b[i]) for i in range(3)) == 1]
for k, (lab, pts) in enumerate(planes):
    P = proj(90 + k*200, 150, 95)
    s.poly([P(*q) for q in pts], SIG, 1.4, fill=SIG, close=True, fop=0.28)
    for a, b in edges:
        hidden = (0,0,0) in (a, b)
        (x1,y1), (x2,y2) = P(*a), P(*b)
        s.line(x1, y1, x2, y2, INK, 1.1, dash="3 3" if hidden else None, op=.8)
    ox, oy = P(0,0,0)
    for v, name in (((1.45,0,0),"x"), ((0,1.35,0),"y"), ((0,0,1.35),"z")):
        ex, ey = P(*v)
        s.line(ox, oy, ex, ey, INK, .9, op=.45, arrow='end')
        s.text(ex + (-8 if name == "x" else 6), ey + (12 if name == "x" else 4 if name == "y" else -2),
               name, anchor="middle", size=11, italic=True, op=.8)
    s.text(90 + k*200 + 45, 205, lab, size=13, color=SIG, weight=600)
write("planes.svg", figure(640, 215, [s],
      "Unit cubes with the (100) face, the (110) diagonal plane and the (111) plane shaded"))

s = Sketch()
P = proj(170, 160, 48)
ox, oy = P(0,0,0)
for v, name in (((2.9,0,0),"x"), ((0,4.0,0),"y"), ((0,0,1.9),"z")):
    ex, ey = P(*v)
    s.line(ox, oy, ex, ey, INK, 1, op=.6, arrow='end')
    s.text(ex + (-10 if name == "x" else 8), ey + (10 if name == "x" else 4 if name == "y" else -4),
           name, size=11.5, italic=True)
for i in (1, 2):
    tx, ty = P(i, 0, 0); s.line(tx - 4, ty - 3, tx + 4, ty + 3, INK, 1, op=.7)
for i in (1, 2, 3):
    tx, ty = P(0, i, 0); s.line(tx, ty - 4, tx, ty + 4, INK, 1, op=.7)
tx, ty = P(0, 0, 1); s.line(tx - 4, ty, tx + 4, ty, INK, 1, op=.7)
tri = [P(2,0,0), P(0,3,0), P(0,0,1)]
s.poly(tri, SIG, 1.6, fill=SIG, close=True, fop=0.25)
for (x, y), lab, dx, dy in zip(tri, ("2a", "3b", "1c"), (-16, 4, -16), (14, 18, 2)):
    s.circle(x, y, 3.2, fill=SIG)
    s.text(x + dx, y + dy, lab, size=11.5, color=SIG, weight=600)
s.text(330, 40, "intercepts 2, 3, 1", anchor="start", size=11)
s.text(330, 58, "reciprocals ½, ⅓, 1", anchor="start", size=11)
s.text(330, 76, "× 6  →  (3 2 6)", anchor="start", size=12, color=SIG, weight=600)
write("miller-326.svg", figure(470, 225, [s],
      "The plane cutting the x axis at 2a, the y axis at 3b and the z axis at c, with Miller indices 3 2 6"))


# =====================================================================
# M04  Czochralski puller
# =====================================================================
s = Sketch()
cx = 200
s.line(cx, 10, cx, 62, INK, 2.2)                                                       # pull rod
s.path(f"M{cx-16},34 a16,6 0 1,0 32,0", INK, 1, arrow='end', op=.7)                    # rotation
s.line(cx + 26, 52, cx + 26, 22, SIG2, 1.4, arrow='sig2')                              # lift arrow
s.rect(cx - 7, 62, 14, 14, fill=INK, stroke=INK)                                       # holder
s.rect(cx - 4, 76, 8, 12, fill=SOFT2, stroke=INK)                                      # seed
s.rect(cx - 2.5, 88, 5, 22, fill=SOFT2, stroke=INK)                                    # neck
s.path(f"M{cx-2.5},110 L{cx-38},140 L{cx-38},212 Q{cx},222 {cx+38},212 L{cx+38},140 L{cx+2.5},110 Z",
       INK, 1.3, fill=SOFT2)                                                           # ingot
s.path(f"M110,190 L110,280 Q{cx},300 290,280 L290,190", INK, 2.4)                      # crucible
s.path(f"M120,214 L120,276 Q{cx},292 280,276 L280,214 Z", 'none', 0, fill=SOFT)       # melt
s.line(120, 214, cx - 40, 214, SIG2, 1.4); s.line(cx + 40, 214, 280, 214, SIG2, 1.4)
s.path(f"M100,186 L100,288 Q{cx},312 300,288 L300,186", INK, 1, op=.55)               # susceptor
for x in (84, 306):
    for y in range(196, 292, 16):
        s.rect(x - 5, y, 10, 10, fill=SIG, stroke='none', op=.75)                      # heater coils
s.path(f"M{cx-18},304 a18,6 0 1,1 36,0", INK, 1, arrow='end', op=.7)                    # crucible rotation
labels = [
    (cx + 36, 30, "pull rod: rotate and lift slowly (≈ 1 mm/min)"),
    (cx + 12, 83, "seed crystal (sets orientation)"),
    (cx + 10, 102, "Dash neck (removes dislocations)"),
    (cx + 44, 172, "single-crystal ingot"),
    (cx + 104, 236, "Si melt, ≈ 1420 °C"),
    (cx + 104, 266, "quartz crucible"),
    (cx + 112, 296, "heater"),
]
for x, y, t in labels:
    s.text(x, y, t, anchor="start", size=10.5)
s.line(cx + 100, 233, 252, 240, INK, .8, op=.5)
s.line(cx + 100, 263, 287, 262, INK, .8, op=.5)
s.line(cx + 108, 293, 312, 286, INK, .8, op=.5)
s.text(cx, 335, "crucible counter-rotates; chamber filled with argon", size=10.5, op=.8)
write("cz.svg", figure(470, 345, [s],
      "Czochralski crystal puller: a rotating seed is slowly withdrawn from silicon melt in a heated quartz crucible, growing a single-crystal ingot"))


# =====================================================================
# M05  three epitaxy methods
# =====================================================================
s = Sketch()
# VPE
s.text(100, 20, "VPE / CVD", size=12.5, weight=600)
s.rect(30, 40, 140, 90, fill='none', rx=4, op=.6)
s.rect(55, 108, 90, 14, fill=SIG, stroke='none', op=.55)       # susceptor heated
s.rect(65, 100, 70, 8, fill=SOFT2, stroke=INK)                 # substrate
for y in (60, 76):
    s.line(8, y, 160, y, SIG2, 1.3, arrow='sig2')
s.text(30, 55, "SiCl₄ + H₂", anchor="start", size=10)
s.line(170, 90, 190, 90, INK, 1, arrow='end', op=.7)
s.text(178, 104, "HCl", size=10)
s.text(100, 162, "gas reacts on hot", size=10.5)
s.text(100, 177, "substrate, 1000–1250 °C", size=10.5)
# LPE
X = 230
s.text(X + 85, 20, "LPE", size=12.5, weight=600)
s.rect(X + 15, 60, 140, 40, fill='none', stroke=INK, sw=1.4)   # boat
s.rect(X + 40, 62, 50, 26, fill=SOFT, stroke=INK)              # melt well
s.rect(X + 100, 62, 40, 26, fill=SOFT, stroke=INK, op=.6)
s.rect(X + 45, 88, 40, 8, fill=SOFT2, stroke=INK)              # substrate under the melt
s.line(X + 155, 92, X + 185, 92, INK, 1, arrow='end', op=.7)
s.text(X + 65, 54, "Ga + As melt", size=10)
s.text(X + 85, 120, "slider moves substrate", size=10, op=.8)
s.text(X + 85, 162, "cool slowly: GaAs", size=10.5)
s.text(X + 85, 177, "precipitates, 700–900 °C", size=10.5)
# MBE
X = 450
s.text(X + 85, 20, "MBE", size=12.5, weight=600)
s.rect(X + 10, 34, 150, 100, fill='none', rx=30, op=.6)
s.rect(X + 55, 44, 60, 8, fill=SOFT2, stroke=INK)              # substrate (face down)
s.rect(X + 60, 36, 50, 8, fill=SIG, stroke='none', op=.55)
for i, (x, lab) in enumerate(((X + 32, "Ga"), (X + 85, "As"), (X + 138, "Si"))):
    s.rect(x - 9, 112, 18, 14, fill=INK, stroke=INK, op=.8)
    s.text(x, 140, lab, size=10)
    s.line(x, 110, X + 85 + (x - X - 85)*0.25, 56, SIG2, 1.1, dash="3 3")
s.line(X + 20, 100, X + 44, 100, INK, 1.6)                     # shutter
s.text(X + 85, 162, "UHV ≈ 10⁻¹⁰ Torr, 500–650 °C", size=10.5)
s.text(X + 85, 177, "atomic-layer control", size=10.5)
write("epitaxy.svg", figure(640, 186, [s],
      "Schematics of vapour-phase, liquid-phase and molecular-beam epitaxy"))


# =====================================================================
# M06  donor and acceptor levels
# =====================================================================
s = Sketch()
for k, (lab, kind) in enumerate((("n-type: donors", "n"), ("p-type: acceptors", "p"))):
    x0 = 40 + k*270
    s.text(x0 + 100, 20, lab, size=12.5, weight=600)
    s.rect(x0, 34, 200, 30, fill='none', stroke='none')
    s.line(x0, 60, x0 + 200, 60, INK, 1.8)                 # Ec
    s.line(x0, 150, x0 + 200, 150, INK, 1.8)               # Ev
    s.rect(x0, 30, 200, 30, fill='none', stroke='none')
    s.rect(x0, 150, 200, 26, fill=SOFT, stroke='none')
    s.text(x0 + 206, 64, "E_c", anchor="start", size=10.5)
    s.text(x0 + 206, 154, "E_v", anchor="start", size=10.5)
    if kind == "n":
        for i in range(6):
            x = x0 + 18 + i*33
            s.line(x - 9, 72, x + 9, 72, SIG, 2)
            s.text(x, 88, "+", size=12, color=SIG)
            if i < 5: s.electron(x + 4, 48)
        s.text(x0 + 206, 76, "E_D", anchor="start", size=10.5, color=SIG)
        s.text(x0 + 100, 196, "E_c − E_D ≈ 0.045 eV (P in Si)", size=10.5, op=.85)
    else:
        for i in range(6):
            x = x0 + 18 + i*33
            s.line(x - 9, 138, x + 9, 138, SIG, 2)
            s.text(x, 130, "−", size=12, color=SIG)
            if i < 5: s.hole(x + 4, 162)
        s.text(x0 + 206, 141, "E_A", anchor="start", size=10.5, color=SIG)
        s.text(x0 + 100, 196, "E_A − E_v ≈ 0.045 eV (B in Si)", size=10.5, op=.85)
write("donor-acceptor.svg", figure(560, 206, [s],
      "Donor levels just below the conduction band release electrons; acceptor levels just above the valence band create holes"))


# =====================================================================
# M06  diffusion profiles
# =====================================================================
a = Panel(50, 36, 230, 140, (0, 5), (0, 1.15))
a.axes("x", "C/C_s", xticks=(1,2,3,4), yticks=(0.5, 1))
for sd, lab in ((0.5, "t₁"), (1.0, "4t₁"), (1.5, "9t₁")):
    a.curve(samp(lambda x: erfc(x/(2*sd)), 0, 5), SIG, 2)
    xl = 2*sd*0.75
    a.text(xl, erfc(0.75), lab, anchor="start", dx=5, dy=-3, size=10, color=SIG)
a.title("constant source: erfc")
b = Panel(360, 36, 230, 140, (0, 5), (0, 1.15))
b.axes("x", "C (relative)", xticks=(1,2,3,4), yticks=(0.5, 1))
for sd, lab in ((0.5, "t₁"), (1.0, "4t₁"), (1.5, "9t₁")):
    b.curve(samp(lambda x: (0.5/sd)*math.exp(-x*x/(4*sd*sd)), 0, 5), SIG2, 2)
    b.text(0, 0.5/sd, lab, anchor="start", dx=6, dy=-4, size=10, color=SIG2)
b.title("fixed dose: Gaussian")
write("diffusion.svg", figure(660, 200, [a, b],
      "Constant-source erfc profiles all start at the same surface value and deepen with time; fixed-dose Gaussian profiles spread and their surface value falls"))


# =====================================================================
# M07  implanted profile
# =====================================================================
p = Panel(60, 30, 400, 150, (0, 0.42), (0, 1.15))
p.axes("depth x (μm)", "N(x)/N_p", xticks=(0.1, 0.2, 0.3, 0.4), yticks=(0.5, 1))
Rp, dR = 0.15, 0.045
p.curve(samp(lambda x: math.exp(-(x - Rp)**2/(2*dR*dR)), 0, 0.42), SIG, 2.2)
p.line(Rp, 0, Rp, 1, INK, 1, dash="4 3", op=.6)
p.text(Rp, 1.0, "R_p", dy=-6, size=11)
y6 = math.exp(-0.5)
p.line(Rp, y6, Rp + dR, y6, SIG2, 1.4)
p.text(Rp + dR, y6, "ΔR_p", anchor="start", dx=4, dy=4, size=10.5, color=SIG2)
p.line(0, 0.12, 0.42, 0.12, INK, 1, dash="2 3", op=.6)
p.text(0.42, 0.12, "N_B", anchor="end", dy=-5, size=10.5)
xj = Rp + dR*math.sqrt(2*math.log(1/0.12))
p.dot(xj, 0.12, SIG2)
p.text(xj, 0.12, "x_j", dx=0, dy=15, size=10.5, color=SIG2)
write("implant.svg", figure(540, 205, [p],
      "Gaussian implanted profile peaking at the projected range R_p below the surface, with straggle ΔR_p and the junction where it meets the background doping"))


# =====================================================================
# M08  Kronig-Penney graphical solution
# =====================================================================
Pkp = 1.5*math.pi
f_kp = lambda u: Pkp*math.sin(u)/u + math.cos(u)
p = Panel(60, 24, 470, 190, (0, 4.15*math.pi), (-2.2, 6.2))
pts = samp(f_kp, 0.02, 4.15*math.pi, 800)
# shade allowed bands
run = None
bands = []
for u, v in pts:
    ok = -1 <= v <= 1
    if ok and run is None: run = u
    if not ok and run is not None: bands.append((run, u)); run = None
if run is not None: bands.append((run, pts[-1][0]))
for u1, u2 in bands:
    p.p.append(f'<rect x="{p.X(u1):.1f}" y="{p.Y(1):.1f}" width="{p.X(u2)-p.X(u1):.1f}" '
               f'height="{p.Y(-1)-p.Y(1):.1f}" style="fill:{SOFT}"/>')
    p.p.append(f'<rect x="{p.X(u1):.1f}" y="{p.Y(-2.2)-6:.1f}" width="{p.X(u2)-p.X(u1):.1f}" '
               f'height="5" style="fill:{SIG2}"/>')
p.axes("αa", "P sin(αa)/αa + cos αa", yticks=(-1, 1, 5))
for k, lab in ((1, "π"), (2, "2π"), (3, "3π"), (4, "4π")):
    u = k*math.pi
    p.line(u, -0.15, u, 0.15, INK, 1, op=.55)
    p.text(u, 0, lab, dy=15, size=10, op=.8)
p.line(0, 1, 4.15*math.pi, 1, INK, 1, dash="4 3", op=.55)
p.line(0, -1, 4.15*math.pi, -1, INK, 1, dash="4 3", op=.55)
p.curve(pts, SIG, 2)
p.raw_text(p.X(4.15*math.pi), p.Y(-2.2) + 18, "bars mark allowed bands", anchor="end", size=10.5, color=SIG2)
write("kronig-penney.svg", figure(600, 250, [p],
      "Graph of the Kronig-Penney function against alpha a; energies where it lies between minus one and plus one form allowed bands"))


# =====================================================================
# M08  E-k diagrams, direct and indirect
# =====================================================================
ps = []
for k, (name, kc) in enumerate((("Direct gap (GaAs)", 0.0), ("Indirect gap (Si)", 0.75))):
    q = Panel(50 + k*300, 34, 230, 170, (-1, 1), (-1.6, 2.2))
    q.line(0, -1.6, 0, 2.15, INK, 1, op=.4)
    q.raw_text(q.X(1) + 4, q.Y(-1.6) + 4, "k", anchor="start", size=11)
    q.raw_text(q.X(0) + 5, q.Y(2.2) + 4, "E", anchor="start", size=11)
    q.line(-1, -1.6, 1, -1.6, INK, 1, op=.55)
    vb = samp(lambda x: -0.15 - 1.3*x*x, -1, 1)
    q.curve(vb, SIG2, 2)
    if kc == 0:
        q.curve(samp(lambda x: 0.6 + 1.4*x*x, -0.95, 0.95), SIG, 2)
        q.p.append(f'<line x1="{q.X(0):.1f}" y1="{q.Y(0.6)+3:.1f}" x2="{q.X(0):.1f}" y2="{q.Y(-0.15)-6:.1f}" '
                   f'style="stroke:{INK}" stroke-width="1.5" marker-end="url(#ar)"/>')
        q.text(0, 0.22, "photon hν", anchor="start", dx=7, size=10.5)
    else:
        q.curve(samp(lambda x: 0.55 + 2.37*(x*x - kc*kc)**2, -1, 1), SIG, 2)
        q.dot(kc, 0.55, SIG); q.hollow(0, -0.15, SIG2)
        q.p.append(f'<line x1="{q.X(kc)-3:.1f}" y1="{q.Y(0.55)+3:.1f}" x2="{q.X(0)+5:.1f}" y2="{q.Y(-0.15)-5:.1f}" '
                   f'style="stroke:{INK}" stroke-width="1.5" stroke-dasharray="4 3" marker-end="url(#ar)"/>')
        q.text(0.42, 0.05, "photon + phonon", anchor="start", dx=4, size=10.5)
    q.text(1, 2.0 if kc == 0 else 1.0, "CB", anchor="start", dx=5, dy=4, size=10.5, color=SIG)
    q.text(1, -1.1, "VB", anchor="start", dx=5, dy=4, size=10.5, color=SIG2)
    q.title(name, 12)
    ps.append(q)
write("ek.svg", figure(600, 225, ps,
      "E-k diagrams: in GaAs the band extrema line up at k equals zero; in silicon the conduction-band minimum is displaced in k"))


# =====================================================================
# M09  Fermi-Dirac function
# =====================================================================
p = Panel(60, 28, 400, 160, (-0.3, 0.3), (0, 1.12))
p.axes("E − E_F (eV)", "f(E)", xticks=(-0.2, -0.1, 0.1, 0.2), yticks=(0.5, 1))
p.curve([(-0.3, 1), (0, 1), (0, 0), (0.3, 0)], INK, 1.8, dash="5 3")
for T, col, lab in ((300, SIG, "300 K"), (900, SIG2, "900 K")):
    kT = 8.617e-5*T
    p.curve(samp(lambda e: 1/(1 + math.exp(e/kT)), -0.3, 0.3), col, 2.1)
p.text(-0.27, 1.0, "0 K", anchor="start", dy=-6, size=10.5)
p.text(0.06, 0.12, "300 K", anchor="start", size=10.5, color=SIG)
p.text(0.12, 0.32, "900 K", anchor="start", size=10.5, color=SIG2)
p.dot(0, 0.5, INK, 3)
p.text(0, 0.5, "f = ½ at E_F", anchor="start", dx=8, dy=-4, size=10.5)
write("fermi.svg", figure(540, 215, [p],
      "Fermi-Dirac function: a step at zero kelvin, smoothed over a few kT at 300 K and 900 K, always one half at the Fermi level"))


# =====================================================================
# M09  Fermi level with doping
# =====================================================================
s = Sketch()
cases = (("intrinsic", 0.0), ("n-type", 0.38), ("p-type", -0.38))
for k, (lab, d) in enumerate(cases):
    x0 = 40 + k*200
    yc, yv = 50, 170
    yi = (yc + yv)/2
    yf = yi - d*(yv - yc)
    s.text(x0 + 70, 24, lab, size=12.5, weight=600)
    s.line(x0, yc, x0 + 140, yc, INK, 1.8)
    s.line(x0, yv, x0 + 140, yv, INK, 1.8)
    s.line(x0, yi, x0 + 140, yi, INK, 1, dash="2 3", op=.6)
    s.line(x0, yf, x0 + 140, yf, SIG, 1.8, dash="6 3")
    s.text(x0 + 146, yc + 4, "E_c", anchor="start", size=10.5)
    s.text(x0 + 146, yv + 4, "E_v", anchor="start", size=10.5)
    if d == 0:
        s.text(x0 + 146, yi + 4, "E_i = E_F", anchor="start", size=10.5, color=SIG)
    else:
        s.text(x0 + 146, yi + (12 if d > 0 else -4), "E_i", anchor="start", size=10.5, op=.75)
        s.text(x0 - 5, yf + 4, "E_F", anchor="end", size=10.5, color=SIG)
s.text(325, 200, "E_F − E_i = kT ln(N_D/n_i)  for n-type;   E_i − E_F = kT ln(N_A/n_i)  for p-type",
       size=10.5, op=.85)
write("fermi-level.svg", figure(660, 210, [s],
      "Band diagrams showing the Fermi level at mid-gap for intrinsic material, near the conduction band for n-type and near the valence band for p-type"))


# =====================================================================
# M10  mobility versus temperature
# =====================================================================
lg = math.log10
p = Panel(70, 28, 380, 170, (lg(50), lg(600)), (2, 4.3))
p.p.append(f'<line x1="{p.X(lg(50)):.1f}" y1="{p.Y(2):.1f}" x2="{p.X(lg(600))-6:.1f}" y2="{p.Y(2):.1f}" '
           f'style="stroke:{INK}" stroke-width="1" opacity=".55" marker-end="url(#ar)"/>')
p.p.append(f'<line x1="{p.X(lg(50)):.1f}" y1="{p.Y(2):.1f}" x2="{p.X(lg(50)):.1f}" y2="{p.Y(4.3)+6:.1f}" '
           f'style="stroke:{INK}" stroke-width="1" opacity=".55" marker-end="url(#ar)"/>')
for T in (50, 100, 200, 300, 500):
    p.line(lg(T), 2, lg(T), 2.06, INK, 1, op=.6); p.text(lg(T), 2, str(T), dy=15, size=10, op=.8)
for m, lab in ((2, "10²"), (3, "10³"), (4, "10⁴")):
    p.line(lg(50), m, lg(50) + 0.02, m, INK, 1, op=.6)
    p.text(lg(50), m, lab, anchor="end", dx=-5, dy=4, size=10, op=.8)
p.raw_text(p.X(lg(600)) + 4, p.Y(2) + 4, "T (K)", anchor="start", size=11)
p.raw_text(p.X(lg(50)) + 5, p.Y(4.3) + 2, "μ_n (cm²/V·s)", anchor="start", size=11)
muL = lambda T: 1350*(T/300)**-1.5
for muI300, col, lab in ((15000, SIG, "light doping"), (1500, SIG2, "heavy doping")):
    f = lambda T: 1/(1/muL(T) + 1/(muI300*(T/300)**1.5))
    p.curve([(lg(T), lg(f(T))) for T in [50*1.02**i for i in range(126)]], col, 2.1)
    at = 60 if col == SIG else 150
    p.text(lg(at), lg(f(at)), lab, anchor="start", dx=2, dy=(-10 if col == SIG else 18), size=10.5, color=col)
p.curve([(lg(T), lg(muL(T))) for T in (80, 600)], INK, 1, dash="4 3")
p.text(lg(90), lg(muL(90)), "lattice ∝ T^{−3/2}", anchor="start", dx=6, dy=-2, size=10, op=.75)
write("mobility.svg", figure(540, 225, [p],
      "Log-log plot of electron mobility against temperature for light and heavy doping, rising then falling, with the lattice-scattering limit shown dashed"))


# =====================================================================
# M10  drift velocity versus field
# =====================================================================
p = Panel(70, 28, 380, 175, (2, 6), (5, 7.5))
p.p.append(f'<line x1="{p.X(2):.1f}" y1="{p.Y(5):.1f}" x2="{p.X(6)-6:.1f}" y2="{p.Y(5):.1f}" '
           f'style="stroke:{INK}" stroke-width="1" opacity=".55" marker-end="url(#ar)"/>')
p.p.append(f'<line x1="{p.X(2):.1f}" y1="{p.Y(5):.1f}" x2="{p.X(2):.1f}" y2="{p.Y(7.5)+6:.1f}" '
           f'style="stroke:{INK}" stroke-width="1" opacity=".55" marker-end="url(#ar)"/>')
for e, lab in ((2, "10²"), (3, "10³"), (4, "10⁴"), (5, "10⁵"), (6, "10⁶")):
    p.line(e, 5, e, 5.05, INK, 1, op=.6); p.text(e, 5, lab, dy=15, size=10, op=.8)
for v, lab in ((5, "10⁵"), (6, "10⁶"), (7, "10⁷")):
    p.line(2, v, 2.04, v, INK, 1, op=.6); p.text(2, v, lab, anchor="end", dx=-5, dy=4, size=10, op=.8)
p.raw_text(p.X(6) + 4, p.Y(5) + 4, "E (V/cm)", anchor="start", size=11)
p.raw_text(p.X(2) + 5, p.Y(7.5) + 2, "v_d (cm/s)", anchor="start", size=11)
Es = [10**(2 + 4*i/300) for i in range(301)]
si_n = lambda E: 1350*E/(1 + (1350*E/1.07e7)**2)**0.5
si_p = lambda E: 480*E/(1 + 480*E/8.4e6)
gaas = lambda E: (8500*E + 1e7*(E/4e3)**4)/(1 + (E/4e3)**4)
for f, col, lab, at, dy in ((gaas, SIG, "GaAs electrons", 3.85, -10), (si_n, INK, "Si electrons", 4.6, -8),
                            (si_p, SIG2, "Si holes", 4.6, 16)):
    p.curve([(lg(E), lg(f(E))) for E in Es], col, 2.1)
    p.text(at, lg(f(10**at)), lab, anchor="start", dx=4, dy=dy, size=10.5, color=col)
p.line(2, 7, 6, 7, INK, 1, dash="2 3", op=.45)
p.text(2.05, 7, "v_sat ≈ 10^{7} cm/s", anchor="start", dy=-5, size=10, op=.75)
write("velocity.svg", figure(540, 230, [p],
      "Drift velocity against electric field on log axes: silicon electrons and holes saturate near ten to the seven centimetres per second, GaAs electrons peak and then fall"))


# =====================================================================
# M11  diffusion flux and current
# =====================================================================
ps = []
for k, (lab, col, cur) in enumerate((("electrons", SIG, -1), ("holes", SIG2, 1))):
    q = Panel(50 + k*290, 34, 210, 110, (0, 1), (0, 1.15))
    q.axes("x", "n(x)" if k == 0 else "p(x)")
    q.curve(samp(lambda x: 0.95*math.exp(-2.2*x) + 0.05, 0, 1), col, 2.2)
    for i in range(7):
        xx = 0.06 + 0.13*i
        yy = 0.95*math.exp(-2.2*xx) + 0.05
        if k == 0: q.dot(xx, yy*0.45, INK, 2.6)
        else:      q.hollow(xx, yy*0.45, INK, 2.6)
    q.title(lab, 12)
    y1 = 34 + 110 + 32
    x1, x2 = 50 + k*290 + 30, 50 + k*290 + 180
    q.p.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y1}" style="stroke:{INK}" stroke-width="1.4" marker-end="url(#ar)"/>')
    q.p.append(f'<text x="{(x1+x2)/2}" y="{y1-6}" text-anchor="middle" font-size="10.5" style="fill:{INK}">flux, down the gradient</text>')
    y2 = y1 + 30
    a1, a2 = (x2, x1) if cur < 0 else (x1, x2)
    mk = "ars" if col == SIG else "art"
    q.p.append(f'<line x1="{a1}" y1="{y2}" x2="{a2}" y2="{y2}" style="stroke:{col}" stroke-width="2" marker-end="url(#{mk})"/>')
    q.p.append(f'<text x="{(x1+x2)/2}" y="{y2-6}" text-anchor="middle" font-size="10.5" style="fill:{col}">'
               f'{"J_n = +qD_n dn/dx  (against the flux)" if cur < 0 else "J_p = −qD_p dp/dx  (with the flux)"}</text>')
    ps.append(q)
write("diffusion-current.svg", figure(600, 225, ps,
      "Electrons and holes both diffuse down their concentration gradients, but electron current flows opposite to electron flux"))


# =====================================================================
# M12  recombination paths
# =====================================================================
s = Sketch()
yc, yv = 50, 170
s.line(20, yc, 600, yc, INK, 1.8); s.line(20, yv, 600, yv, INK, 1.8)
s.rect(20, 26, 580, 24, fill='none', stroke='none')
s.rect(20, yv, 580, 20, fill=SOFT, stroke='none')
s.text(606, yc + 4, "E_c", anchor="start", size=10.5)
s.text(606, yv + 4, "E_v", anchor="start", size=10.5)
# band to band
x = 110
s.electron(x, yc - 8); s.hole(x, yv + 8)
s.line(x, yc - 2, x, yv - 4, INK, 1.6, arrow='end')
s.path(f"M{x+8},110 q6,-8 12,0 t12,0 t12,0 t12,0", SIG, 1.6, arrow='sig')
s.text(x + 34, 100, "hν ≈ E_g", anchor="start", size=10.5, color=SIG)
s.text(x + 15, 210, "band-to-band (radiative)", size=11)
s.text(x + 15, 224, "GaAs, LEDs, lasers", size=10, op=.75)
# SRH
x = 310
s.line(x - 30, 110, x + 30, 110, SIG2, 2.4)
s.text(x + 34, 114, "E_t", anchor="start", size=10.5, color=SIG2)
s.electron(x - 14, yc - 8); s.hole(x + 14, yv + 8)
s.line(x - 14, yc - 2, x - 14, 106, INK, 1.6, arrow='end')
s.line(x + 14, 114, x + 14, yv - 4, INK, 1.6, arrow='end')
s.text(x - 20, 84, "1", anchor="end", size=10, op=.8)
s.text(x + 20, 146, "2", anchor="start", size=10, op=.8)
s.text(x, 210, "Shockley–Read–Hall (trap)", size=11)
s.text(x, 224, "Si; energy to phonons", size=10, op=.75)
# Auger
x = 500
s.electron(x - 16, yc - 8); s.hole(x - 16, yv + 8); s.electron(x + 16, yc - 8)
s.line(x - 16, yc - 2, x - 16, yv - 4, INK, 1.6, arrow='end')
s.path(f"M{x+16},{yc-12} q4,-10 0,-18", INK, 1.4, arrow='end')
s.text(x + 22, 26, "third carrier kicked up", anchor="start", size=10, op=.85)
s.text(x, 210, "Auger", size=11)
s.text(x, 224, "high carrier density", size=10, op=.75)
write("recombination.svg", figure(640, 232, [s],
      "Three recombination paths: direct band-to-band with photon emission, two-step recombination through a mid-gap trap, and Auger recombination giving energy to a third carrier"))


# =====================================================================
# M12  photoconductive decay;  M13  injection profile
# =====================================================================
p = Panel(60, 28, 400, 140, (-1.5, 5), (0, 1.15))
p.p.append(f'<rect x="{p.X(-1.5):.1f}" y="{p.Y(1.15):.1f}" width="{p.X(0)-p.X(-1.5):.1f}" '
           f'height="{p.Y(0)-p.Y(1.15):.1f}" style="fill:{SOFT2}"/>')
p.axes("t / τ_p", "Δp/Δp(0)", xticks=(1, 2, 3, 4), yticks=(0.37, 1), ytick_fmt="{:g}")
p.curve([(-1.5, 1), (0, 1)], SIG, 2.2)
p.curve(samp(lambda t: math.exp(-t), 0, 5), SIG, 2.2)
p.line(1, 0, 1, math.exp(-1), INK, 1, dash="3 3", op=.6)
p.line(0, math.exp(-1), 1, math.exp(-1), INK, 1, dash="3 3", op=.6)
p.text(-0.75, 0.86, "light on", size=10.5)
p.text(-0.75, 0.73, "Δp = Gτ_p", size=10.5)
p.text(1.1, math.exp(-1), "1/e at t = τ_p", anchor="start", dy=-4, size=10.5)
write("decay.svg", figure(540, 195, [p],
      "Excess carrier density held constant under illumination, then decaying exponentially after the light is switched off, reaching one over e after one lifetime"))

p = Panel(60, 28, 400, 140, (0, 5), (0, 1.15))
p.axes("x / L_p", "Δp(x)/Δp(0)", xticks=(1, 2, 3, 4), yticks=(0.37, 1))
p.curve(samp(lambda x: math.exp(-x), 0, 5), SIG, 2.2)
p.line(1, 0, 1, math.exp(-1), INK, 1, dash="3 3", op=.6)
p.line(0, math.exp(-1), 1, math.exp(-1), INK, 1, dash="3 3", op=.6)
p.text(1.1, math.exp(-1), "Δp falls to 1/e at x = L_p = √(D_pτ_p)", anchor="start", dy=-4, size=10.5)
write("injection.svg", figure(540, 195, [p],
      "Steady-state excess minority-carrier density decaying exponentially from the injection point with characteristic length L_p"))


# =====================================================================
# M14  p-n junction: charge, field, bands
# =====================================================================
xp, xn = -0.5, 1.5           # N_A = 3 N_D
NA, ND = 3.0, 1.0
def Efield(x):
    if xp <= x <= 0:  return -NA*(x - xp)
    if 0 < x <= xn:   return -ND*(xn - x)
    return 0.0
def pot(x):
    # V(x) = -∫E dx from the p-side edge (V = 0 there)
    n = 200; a = -2.0
    if x <= a: return 0.0
    h = (x - a)/n
    return -sum(Efield(a + (i + 0.5)*h) for i in range(n))*h
Vbi = pot(2.0)
ps = []
c = Panel(70, 26, 420, 70, (-2, 2), (-3.4, 1.6))
c.line(-2, 0, 2, 0, INK, 1, op=.55)
c.p.append(f'<rect x="{c.X(xp):.1f}" y="{c.Y(0):.1f}" width="{c.X(0)-c.X(xp):.1f}" height="{c.Y(-NA)-c.Y(0):.1f}" '
           f'style="fill:{SIG2};stroke:{SIG2}" fill-opacity=".25"/>')
c.p.append(f'<rect x="{c.X(0):.1f}" y="{c.Y(ND):.1f}" width="{c.X(xn)-c.X(0):.1f}" height="{c.Y(0)-c.Y(ND):.1f}" '
           f'style="fill:{SIG};stroke:{SIG}" fill-opacity=".25"/>')
c.text(xp/2, -NA/2, "−qN_A", size=10, dy=4, color=SIG2)
c.text(xn/2, ND, "+qN_D", size=10, dy=-5, color=SIG)
c.raw_text(c.X(-2) - 8, c.Y(0) + 4, "ρ", anchor="end", size=12)
c.text(-1.5, 1.0, "p side", size=10.5, op=.8); c.text(1.85, -1.5, "n side", anchor="end", size=10.5, op=.8)
ps.append(c)
e = Panel(70, 116, 420, 60, (-2, 2), (-1.7, 0.4))
e.line(-2, 0, 2, 0, INK, 1, op=.55)
e.curve([(x, Efield(x)/NA*1.5) for x in [(-2 + 4*i/400) for i in range(401)]], SIG, 2)
e.text(0, -1.5, "E_max", anchor="start", dx=6, dy=6, size=10)
e.raw_text(e.X(-2) - 8, e.Y(0) + 4, "E", anchor="end", size=12)
ps.append(e)
b = Panel(70, 196, 420, 130, (-2, 2), (-0.4, 2.5))
X = [(-2 + 4*i/400) for i in range(401)]
# p side: E_c = 2.3, E_F 0.25 above E_v; n side: E_F 0.3 below E_c; gap 1.5 units
Ec = lambda x: 2.3 - pot(x)/Vbi*0.95
EF = 1.05
b.curve([(x, Ec(x)) for x in X], INK, 2)
b.curve([(x, Ec(x) - 1.5) for x in X], INK, 2)
b.curve([(x, Ec(x) - 0.75) for x in X], INK, 1, dash="2 3")
b.curve([(-2, EF), (2, EF)], SIG, 1.8, dash="6 3")
b.text(2, Ec(2), "E_c", anchor="start", dx=5, dy=4, size=10.5)
b.text(2, Ec(2) - 0.75, "E_i", anchor="start", dx=5, dy=4, size=10.5, op=.75)
b.text(2, Ec(2) - 1.5, "E_v", anchor="start", dx=5, dy=4, size=10.5)
b.text(-1.95, EF, "E_F", anchor="start", dy=-5, size=10.5, color=SIG)
b.line(-1.25, Ec(-2), 1.0, Ec(-2), SIG2, 0.8, dash="2 3", op=0)
b.p.append(f'<line x1="{b.X(-1.2):.1f}" y1="{b.Y(Ec(-2)):.1f}" x2="{b.X(-1.2):.1f}" y2="{b.Y(Ec(2))-1:.1f}" '
           f'style="stroke:{SIG2}" stroke-width="1.3" marker-end="url(#art)"/>')
b.line(-1.3, Ec(2), 1.5, Ec(2), SIG2, 0.8, dash="2 3")
b.text(-1.2, (Ec(-2) + Ec(2))/2, "qV_bi", anchor="start", dx=6, dy=4, size=10.5, color=SIG2)
dl = Sketch()
for xx, lab in ((xp, "−x_p"), (xn, "x_n")):
    X0 = c.X(xx)
    dl.line(X0, 22, X0, 326, INK, .8, dash="2 4", op=.45)
    dl.text(X0, 344, lab, size=10.5)
dl.text(c.X(0), 344, "0", size=10.5)
write("pn-junction.svg", figure(560, 354, ps + [b, dl],
      "Abrupt p-n junction in equilibrium: fixed charge in the depletion region, the triangular electric field, and the band diagram with a flat Fermi level and bands bent by q V bi"))


# =====================================================================
# M14  diode I-V
# =====================================================================
p = Panel(70, 24, 400, 170, (-1.0, 0.85), (-1.5, 11))
p.axes("V (V)", "I (mA)", xticks=(-0.8, -0.4, 0.4, 0.8), yticks=(5, 10))
Is = 0.01/math.exp(0.7/0.0259)
vtop = 0.0259*math.log(11/(1000*Is) + 1)
p.curve(samp(lambda v: 1000*Is*(math.exp(v/0.0259) - 1), -1.0, vtop, 400), SIG, 2.2)
p.text(-0.95, 0, "reverse: I ≈ −I_s (nA or less)", anchor="start", dy=-8, size=10.5)
p.text(0.62, 5, "≈ 0.6–0.7 V (Si)", anchor="end", dx=-6, size=10.5, color=SIG)
p.text(0.62, 8.5, "×10 per 60 mV", anchor="end", dx=-8, size=10, op=.75)
write("diode-iv.svg", figure(540, 220, [p],
      "Ideal silicon diode current against voltage: negligible reverse current and an exponential rise above about 0.6 volts"))


# =====================================================================
# M15  Schottky barrier band diagram
# =====================================================================
s = Sketch()
x0, xi, xw, xe = 30, 170, 330, 560
yF = 160
yEc_b = 130               # bulk Ec, 30 px above EF
Vbi_px = 55
yEc = lambda x: yEc_b - Vbi_px*(1 - (x - xi)/(xw - xi))**2 if x < xw else yEc_b
s.rect(x0, yF, xi - x0, 60, fill=SOFT2, stroke='none')
s.line(xi, 30, xi, 230, INK, 1.4)
s.text((x0 + xi)/2, 200, "metal", size=11.5)
s.line(x0, yF, xe, yF, SIG, 1.8, dash="6 3")
s.text(xe + 4, yF + 4, "E_F", anchor="start", size=10.5, color=SIG)
pts = [(x, yEc(x)) for x in range(xi, xe + 1, 4)]
s.poly(pts, INK, 2)
s.poly([(x, y + 95) for x, y in pts], INK, 2)
s.text(xe + 4, yEc_b + 4, "E_c", anchor="start", size=10.5)
s.text(xe + 4, yEc_b + 99, "E_v", anchor="start", size=10.5)
# vacuum level: Evac = Ec - chi, follows Ec; metal Evac at EF - phi_m
chi = 55
s.poly([(x, y - chi) for x, y in pts], INK, 1, dash="3 3")
s.line(x0, yEc(xi) - chi, xi, yEc(xi) - chi, INK, 1, dash="3 3")
s.text(xe + 4, yEc_b - chi + 4, "E_vac", anchor="start", size=10.5, op=.8)
# phi_B arrow at the interface
s.line(xi + 12, yF, xi + 12, yEc(xi) + 3, SIG2, 1.4, arrow='sig2')
s.text(xi - 6, (yF + yEc(xi))/2 + 4, "qΦ_B = q(Φ_m − χ)", anchor="end", size=10.5, color=SIG2)
s.line(x0 + 10, yEc(xi) - chi, x0 + 10, yF - 2, INK, 1, arrow="end", op=.6)
s.text(x0 + 16, yEc(xi) - chi + 24, "qΦ_m", anchor="start", size=10.5, op=.85)
# Vbi arrow in bulk
s.line(xw + 70, yEc_b, xw + 70, yEc(xi) + 3, SIG, 1.4, arrow='sig')
s.line(xi + 2, yEc(xi), xw + 80, yEc(xi), INK, .8, dash="2 3", op=.5)
s.text(xw + 76, (yEc_b + yEc(xi))/2 + 10, "qV_bi", anchor="start", size=10.5, color=SIG)
# depletion width
s.line(xi, 250, xw, 250, INK, 1, arrow='both', op=.7)
s.text((xi + xw)/2, 266, "depletion width W", size=10.5)
s.text(xe - 20, 266, "n-type Si", anchor="end", size=11.5)
write("schottky.svg", figure(620, 275, [s],
      "Band diagram of a metal on n-type silicon after contact: the conduction band bends upward to the barrier q phi B at the interface, with built-in potential q V bi across the depletion width"))


# =====================================================================
# M16  Mott-Schottky plot
# =====================================================================
p = Panel(70, 24, 400, 160, (-5.5, 1.4), (0, 7.5))
p.axes("V (V)", "1/C²", xticks=(-5, -4, -3, -2, -1, 1))
Vb = 0.6
p.curve([(-5, 1.1*(Vb + 5)), (Vb, 0)], SIG, 2.2)
for v in (-5, -4, -3, -2, -1, 0):
    p.dot(v, 1.1*(Vb - v), SIG, 3.2)
p.dot(Vb, 0, SIG2, 3.6)
p.text(Vb, 0, "V_bi", dx=6, dy=-8, anchor="start", size=10.5, color=SIG2)
p.text(-2.4, 1.1*(Vb + 2.4), "slope = −2/(qε_sNA²)", anchor="start", dx=10, dy=-6, size=10.5)
p.text(-5.3, 6.9, "reverse bias", anchor="start", size=10, op=.75)
write("cv.svg", figure(540, 210, [p],
      "1 over C squared against bias is a straight line whose slope gives the doping and whose voltage intercept gives the built-in potential"))
