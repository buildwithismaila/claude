#!/usr/bin/env python3
"""Generate the signal/response figures as inline-ready SVG.

Axes and labels use currentColor so they follow the page's ink in both themes;
the signal itself uses the page's copper accent via a CSS variable with a
literal fallback.
"""
import math, os

OUT = "/home/user/claude/circuits/figures"
os.makedirs(OUT, exist_ok=True)

INK   = 'currentColor'
SIG   = 'var(--copper,#B4622F)'
SIG2  = 'var(--teal,#1C6E7E)'

def esc(s):
    return (s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))


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
# Module 14 figures
# =====================================================================

# --- 1. graphical representation of a discrete-time signal ------------
p = Panel(60, 30, 330, 150, (-3.2, 4.2), (-4, 4))
p.axes("n", "x(n)", xticks=(-2,-1,1,2,3), yticks=(-3,-2,-1,1,2,3))
p.stems([(-2,-3),(-1,2),(0,0),(1,3),(2,1),(3,2)])
write("sig-graphical.svg", svg(440, 210, [p],
      "Stem plot of the discrete signal x(n) equal to minus 3, 2, 0, 3, 1, 2 at n from minus 2 to 3"))

# --- 2. the four singularity functions, and the integration chain -----
ps = []
X0, W, GAP = 46, 175, 22
def slot(i): return X0 + i*(W+GAP)

# impulse
a = Panel(slot(0), 40, W, 110, (-1.3, 2.6), (-0.35, 1.5))
a.axes("t", xticks=(1,2))
a.line(0, 0, 0, 1, SIG, 2.2); a.dot(0, 1)
a.text(0, 1, "1", anchor="end", dx=-6, dy=4, size=10, color=SIG)
a.title("δ(t)  impulse"); ps.append(a)
# step
b = Panel(slot(1), 40, W, 110, (-1.3, 2.6), (-0.35, 1.5))
b.axes("t", xticks=(1,2))
b.curve([(-1.3,0),(0,0)], SIG); b.curve([(0,1),(2.4,1)], SIG)
b.line(0,0,0,1, SIG, 2)
b.text(0, 1, "1", anchor="end", dx=-6, dy=4, size=10, color=SIG)
b.title("u(t)  step"); ps.append(b)
# ramp
c = Panel(slot(2), 40, W, 110, (-1.3, 2.6), (-0.35, 1.5))
c.axes("t", xticks=(1,2))
c.curve([(-1.3,0),(0,0)], SIG); c.curve([(0,0),(1.4,1.4)], SIG)
c.title("r(t) = t·u(t)  ramp"); ps.append(c)
# parabolic
d = Panel(slot(3), 40, W, 110, (-1.3, 2.6), (-0.35, 1.5))
d.axes("t", xticks=(1,2))
d.curve([(-1.3,0),(0,0)], SIG)
d.curve(samp(lambda t: t*t/2, 0, 1.7, 60), SIG)
d.title("p(t) = t²/2·u(t)  parabolic"); ps.append(d)
# chain arrows between panels
chain = Panel(0,0,1,1,(0,1),(0,1))
for i in range(3):
    x1 = slot(i)+W+3; x2 = slot(i+1)-3; y = 100
    chain.p.append(f'<line x1="{x1}" y1="{y}" x2="{x2-6}" y2="{y}" '
                   f'style="stroke:{SIG2}" stroke-width="1.3" marker-end="url(#ar2)"/>')
    chain.p.append(f'<text x="{(x1+x2)/2:.0f}" y="{y-7}" text-anchor="middle" '
                   f'font-size="10" style="fill:{SIG2}">∫</text>')
chain.p.append(f'<text x="{(slot(0)+slot(3)+W)/2:.0f}" y="185" text-anchor="middle" '
               f'font-size="10.5" style="fill:{INK}" opacity=".7">'
               f'each is the integral of the one before; differentiating runs the other way'
               f'</text>')
total_w = slot(3)+W+40
s = svg(total_w, 200, ps+[chain],
        "Impulse, step, ramp and parabolic functions in a row, joined by integration arrows")
s = s.replace('</defs>',
   f'<marker id="ar2" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="5" markerHeight="5" '
   f'orient="auto-start-reverse"><path d="M0,1 L9,5 L0,9 z" style="fill:{SIG2}"/></marker></defs>')
write("sig-chain.svg", s)

# --- 3. shifted versions ----------------------------------------------
ps=[]
for i,(t0,lab) in enumerate([(0,"u(t)"),(1.2,"u(t − a)")]):
    q = Panel(60+i*230, 34, 190, 110, (-1.4, 3.0), (-0.35, 1.5))
    q.axes("t", xticks=(1,2))
    q.curve([(-1.4,0),(t0,0)], SIG); q.curve([(t0,1),(3.0,1)], SIG)
    q.line(t0,0,t0,1, SIG, 2)
    if t0: q.text(t0, 0, "a", dy=15, size=10, color=SIG)
    q.title(lab); ps.append(q)
write("sig-step-shift.svg", svg(530, 165, ps,
      "Unit step and the same step delayed to t equals a"))

# --- 4. real exponential, three cases ---------------------------------
ps=[]
for i,(al,lab) in enumerate([(0,"α = 0  constant"),(0.9,"α > 0  grows"),(-0.9,"α < 0  decays")]):
    q = Panel(52+i*185, 36, 150, 110, (-0.4, 2.4), (-0.2, 3.2))
    q.axes("t", xticks=(1,2), yticks=(1,))
    q.curve(samp(lambda t,al=al: min(math.exp(al*t), 3.1), 0, 2.4, 80), SIG)
    q.title(lab); ps.append(q)
write("sig-exponential.svg", svg(600, 165, ps,
      "Real exponential A e to the alpha t for alpha zero, positive and negative"))

# --- 5. complex exponential: the six sigma/omega cases -----------------
ps=[]
# growth rates kept gentle so the envelope stays inside the frame: a curve
# clipped at the box edge reads as a plateau that is not in the maths
cases = [(0,0,"σ = 0, ω = 0","constant"), (-0.8,0,"σ < 0, ω = 0","decay"),
         (0.27,0,"σ > 0, ω = 0","growth"), (0,1,"σ = 0, ω ≠ 0","sinusoid"),
         (-0.8,1,"σ < 0, ω ≠ 0","damped sinusoid"), (0.27,1,"σ > 0, ω ≠ 0","growing oscillation")]
for i,(sg,om,lab,sub) in enumerate(cases):
    col, row = i % 3, i // 3
    q = Panel(52+col*185, 36+row*140, 150, 92, (-0.2, 3.2), (-2.6, 2.6))
    q.axes("t")
    w = 2*math.pi/1.6 if om else 0
    f = lambda t,sg=sg,w=w: max(-2.5, min(2.5, math.exp(sg*t)*(math.cos(w*t) if w else 1)))
    q.curve(samp(f, 0, 3.2, 140), SIG, w=1.8)
    if sg:
        q.curve(samp(lambda t,sg=sg: max(-2.5,min(2.5, math.exp(sg*t))), 0, 3.2, 80),
                INK, w=1, dash="3 3")
    q.title(lab)
    q.raw_text(q.x0+q.w/2, q.y0+q.h+16, sub, size=10, color=INK)
    ps.append(q)
write("sig-complex-exp.svg", svg(600, 320, ps,
      "Six cases of the complex exponential e to the s t, for sigma negative, zero and positive "
      "with and without an oscillating part"))

# --- 6. rect, signum, sinc --------------------------------------------
ps=[]
q = Panel(48, 36, 150, 100, (-2.2, 2.2), (-1.4, 1.5))
q.axes("t", yticks=(1,))
q.curve([(-2.2,0),(-1,0)], SIG); q.line(-1,0,-1,1,SIG,2)
q.curve([(-1,1),(1,1)], SIG); q.line(1,1,1,0,SIG,2); q.curve([(1,0),(2.2,0)], SIG)
q.title("rectangular pulse"); ps.append(q)

q = Panel(233, 36, 150, 100, (-2.2, 2.2), (-1.4, 1.5))
q.axes("t", yticks=(-1,1))
q.curve([(-2.2,-1),(0,-1)], SIG); q.curve([(0,1),(2.2,1)], SIG)
q.hollow(0,-1); q.hollow(0,1); q.dot(0,0)
q.title("sgn(t)  signum"); ps.append(q)

q = Panel(418, 36, 150, 100, (-9.5, 9.5), (-0.45, 1.25))
q.axes("t", yticks=(1,))
q.curve(samp(lambda t: 1.0 if abs(t)<1e-9 else math.sin(t)/t, -9.4, 9.4, 240), SIG, w=1.8)
q.title("sinc(t) = sin t / t"); ps.append(q)
write("sig-rect-sgn-sinc.svg", svg(600, 155, ps,
      "Rectangular pulse, signum function and sinc function"))

# --- 7. operations on signals -----------------------------------------
base = [(-1.4,0),(-1,0),(0,2),(0,2),(1,2),(1,1),(2,1),(2,0),(2.6,0)]
def tri(pts):   # the Fig-1 shape used in the tutorial
    return pts
ops = [("x(t)", lambda t: t),
       ("x(t − 1)  delay", lambda t: t-1),
       ("x(−t)  reversal", lambda t: -t),
       ("x(2t)  compression", lambda t: 2*t)]
ps=[]
def xof(t):
    if -1 <= t <= 0: return 2*t+2
    if 0 < t <= 1: return 2
    if 1 < t <= 2: return 1
    return 0
for i,(lab,g) in enumerate(ops):
    col,row = i%2, i//2
    q = Panel(60+col*250, 38+row*138, 200, 92, (-2.6, 3.4), (-0.4, 2.6))
    q.axes("t", xticks=(-2,-1,1,2,3), yticks=(1,2))
    q.curve(samp(lambda t,g=g: xof(g(t)), -2.6, 3.4, 300), SIG, w=1.9)
    q.title(lab); ps.append(q)
write("sig-operations.svg", svg(580, 320, ps,
      "One signal shown unchanged, delayed by one, time reversed, and compressed by two"))

# --- 8. even / odd decomposition --------------------------------------
ps=[]
def xe(t): return 0.5*(xof(t)+xof(-t))
def xo(t): return 0.5*(xof(t)-xof(-t))
for i,(lab,g) in enumerate([("x(t)", xof), ("x_e(t) even", xe), ("x_o(t) odd", xo)]):
    q = Panel(52+i*185, 38, 150, 105, (-2.6, 2.6), (-1.4, 2.4))
    q.axes("t", xticks=(-2,-1,1,2), yticks=(1,2))
    q.curve(samp(g, -2.6, 2.6, 300), SIG, w=1.9)
    q.title(lab); ps.append(q)
ps[1].p.append(f'<text x="{ps[1].x0+ps[1].w/2:.0f}" y="{38+105+30}" text-anchor="middle" '
               f'font-size="10" style="fill:{INK}" opacity=".7">½[x(t) + x(−t)]</text>')
ps[2].p.append(f'<text x="{ps[2].x0+ps[2].w/2:.0f}" y="{38+105+30}" text-anchor="middle" '
               f'font-size="10" style="fill:{INK}" opacity=".7">½[x(t) − x(−t)]</text>')
write("sig-even-odd.svg", svg(600, 195, ps,
      "A signal and its even and odd parts, which sum back to the original"))

# =====================================================================
# Module 15 — first-order response and the time constant
# =====================================================================
ps=[]
q = Panel(60, 40, 220, 120, (-0.3, 5.6), (-0.15, 1.25))
q.axes("t / τ", xticks=(1,2,3,4,5), yticks=(1,))
q.curve(samp(lambda t: math.exp(-t), 0, 5.5, 140), SIG, w=2)
q.line(0,1,0,0,INK,1,dash="3 3",op=.4)
q.line(1,0,1,math.exp(-1),INK,1,dash="3 3",op=.5)
q.line(0,math.exp(-1),1,math.exp(-1),INK,1,dash="3 3",op=.5)
q.text(1, math.exp(-1), "36.8%", anchor="start", dx=6, dy=-4, size=10, color=INK, op=.8)
q.title("decay  x(0)e^(−t/τ)"); ps.append(q)

q = Panel(340, 40, 220, 120, (-0.3, 5.6), (-0.15, 1.25))
q.axes("t / τ", xticks=(1,2,3,4,5), yticks=(1,))
q.curve(samp(lambda t: 1-math.exp(-t), 0, 5.5, 140), SIG, w=2)
q.line(0,1,5.5,1,INK,1,dash="4 3",op=.45)
q.line(1,0,1,1-math.exp(-1),INK,1,dash="3 3",op=.5)
q.line(0,1-math.exp(-1),1,1-math.exp(-1),INK,1,dash="3 3",op=.5)
q.text(1, 1-math.exp(-1), "63.2%", anchor="start", dx=6, dy=12, size=10, color=INK, op=.8)
q.text(4.6, 1, "final value", anchor="end", dy=-6, size=10, color=INK, op=.7)
q.title("rise  x(∞)[1 − e^(−t/τ)]"); ps.append(q)
tail = Panel(0,0,1,1,(0,1),(0,1))
tail.p.append(f'<text x="310" y="192" text-anchor="middle" font-size="10.5" '
              f'style="fill:{INK}" opacity=".7">1τ → 63% · 3τ → 95% · 5τ → effectively finished</text>')
write("first-order.svg", svg(620, 205, ps+[tail],
      "Exponential decay and exponential rise, marked at one time constant and at the final value"))

# =====================================================================
# Module 16 — the three damping cases, and the LC energy cycle
# =====================================================================
w0 = 1.0
def step_resp(z, t):
    if z > 1:
        a = z*w0; wd = w0*math.sqrt(z*z-1)
        s1, s2 = -a+wd, -a-wd
        return 1 - (s1*math.exp(s2*t) - s2*math.exp(s1*t))/(s1-s2)
    if abs(z-1) < 1e-9:
        return 1 - (1 + w0*t)*math.exp(-w0*t)
    a = z*w0; wd = w0*math.sqrt(1-z*z)
    return 1 - math.exp(-a*t)*(math.cos(wd*t) + (a/wd)*math.sin(wd*t))

q = Panel(66, 38, 420, 150, (-0.5, 16), (-0.1, 1.85))
q.axes("ω₀t", xticks=(5,10,15), yticks=(1,))
q.line(0,1,16,1,INK,1,dash="4 3",op=.4)
for z,col,lab,dash in [(2.0, SIG2, "overdamped  ζ = 2", None),
                       (1.0, INK,  "critically damped  ζ = 1", "5 3"),
                       (0.25, SIG, "underdamped  ζ = 0.25", None)]:
    q.curve(samp(lambda t,z=z: step_resp(z,t), 0, 16, 300), col, w=2, dash=dash)
leg = Panel(0,0,1,1,(0,1),(0,1))
for i,(col,lab,dash) in enumerate([(SIG,"underdamped  ζ = 0.25",None),
                                   (INK,"critically damped  ζ = 1","5 3"),
                                   (SIG2,"overdamped  ζ = 2",None)]):
    y = 46+i*17
    d = f' stroke-dasharray="{dash}"' if dash else ''
    leg.p.append(f'<line x1="505" y1="{y}" x2="535" y2="{y}" style="stroke:{col}" '
                 f'stroke-width="2"{d}/>')
    leg.p.append(f'<text x="541" y="{y+4}" font-size="10.5" style="fill:{INK}" '
                 f'opacity=".85">{esc(lab)}</text>')
write("damping.svg", svg(700, 210, [q,leg],
      "Step response of a second-order circuit for underdamped, critically damped and "
      "overdamped cases; only the underdamped case overshoots"))

# --- LC energy cycle: a mechanism diagram, not a plot -----------------
d = Panel(0,0,1,1,(0,1),(0,1))
cx, cy, R = 300, 128, 86
states = [("capacitor full",  "all energy electric\ni = 0",          0),
          ("discharging",     "energy splits",                       1),
          ("inductor full",   "all energy magnetic\nv = 0",          2),
          ("recharging",      "energy splits",                       3)]
pos = [(cx, cy-R), (cx+R, cy), (cx, cy+R), (cx-R, cy)]
for (title,sub,i) in states:
    x,y = pos[i]
    col = SIG if i%2==0 else INK
    d.p.append(f'<rect x="{x-78:.0f}" y="{y-21:.0f}" width="156" height="42" rx="3" '
               f'fill="none" style="stroke:{col}" stroke-width="1.4" '
               f'opacity="{1 if i%2==0 else .55}"/>')
    d.p.append(f'<text x="{x}" y="{y-4}" text-anchor="middle" font-size="11.5" '
               f'style="fill:{col}" font-weight="600">{esc(title)}</text>')
    for k,ln in enumerate(sub.split("\n")):
        d.p.append(f'<text x="{x}" y="{y+10+k*11}" text-anchor="middle" font-size="9.5" '
                   f'style="fill:{INK}" opacity=".7">{esc(ln)}</text>')
import math as _m
for i in range(4):
    a0 = [-90, 0, 90, 180][i]
    a1 = a0 + 90
    r = R - 34
    x1 = cx + r*_m.cos(_m.radians(a0+16)); y1 = cy + r*_m.sin(_m.radians(a0+16))
    x2 = cx + r*_m.cos(_m.radians(a1-16)); y2 = cy + r*_m.sin(_m.radians(a1-16))
    d.p.append(f'<path d="M{x1:.1f},{y1:.1f} A{r},{r} 0 0 1 {x2:.1f},{y2:.1f}" fill="none" '
               f'style="stroke:{SIG2}" stroke-width="1.4" marker-end="url(#ar2)"/>')
d.p.append(f'<text x="{cx}" y="{cy-4}" text-anchor="middle" font-size="11" '
           f'style="fill:{INK}" opacity=".8">½q²/C + ½Li² = constant</text>')
d.p.append(f'<text x="{cx}" y="{cy+12}" text-anchor="middle" font-size="10" '
           f'style="fill:{INK}" opacity=".6">ω₀ = 1/√(LC)</text>')
s = svg(600, 258, [d],
        "The LC oscillation as a four-state cycle: energy moves from the capacitor's electric "
        "field to the inductor's magnetic field and back, with the total constant")
s = s.replace('</defs>',
   f'<marker id="ar2" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="5" markerHeight="5" '
   f'orient="auto-start-reverse"><path d="M0,1 L9,5 L0,9 z" style="fill:{SIG2}"/></marker></defs>')
write("lc-cycle.svg", s)

# =====================================================================
# Module 21 — pole location decides the response
# =====================================================================
d = Panel(0,0,1,1,(0,1),(0,1))
ox, oy, sc = 200, 130, 46
d.p.append(f'<line x1="{ox-170}" y1="{oy}" x2="{ox+120}" y2="{oy}" style="stroke:{INK}" '
           f'stroke-width="1" opacity=".55" marker-end="url(#ar)"/>')
d.p.append(f'<line x1="{ox}" y1="{oy+112}" x2="{ox}" y2="{oy-112}" style="stroke:{INK}" '
           f'stroke-width="1" opacity=".55" marker-end="url(#ar)"/>')
d.p.append(f'<text x="{ox+126}" y="{oy+4}" font-size="11" style="fill:{INK}">σ</text>')
d.p.append(f'<text x="{ox+6}" y="{oy-116}" font-size="11" style="fill:{INK}">jω</text>')
d.p.append(f'<rect x="{ox-170}" y="{oy-112}" width="170" height="224" style="fill:{SIG}" '
           f'opacity=".055"/>')
d.p.append(f'<text x="{ox-85}" y="{oy-96}" text-anchor="middle" font-size="10.5" '
           f'style="fill:{INK}" opacity=".65">stable half-plane</text>')
marks = [(-2.6, 0,  "real, negative", "decaying exponential", SIG),
         (-1.5, 1.4,"complex pair",   "damped oscillation",   SIG),
         (0,    1.9,"on the axis",    "sustained oscillation",INK),
         (1.2,  1.0, "right half",    "growing — unstable",   SIG2)]
for (sx, sy, lab, eff, col) in marks:
    px, py = ox + sx*sc, oy - sy*sc
    for sgn in ([1,-1] if sy else [1]):
        qy = oy - sgn*sy*sc
        d.p.append(f'<line x1="{px-5:.1f}" y1="{qy-5:.1f}" x2="{px+5:.1f}" y2="{qy+5:.1f}" '
                   f'style="stroke:{col}" stroke-width="2"/>')
        d.p.append(f'<line x1="{px-5:.1f}" y1="{qy+5:.1f}" x2="{px+5:.1f}" y2="{qy-5:.1f}" '
                   f'style="stroke:{col}" stroke-width="2"/>')
rows = [("real, negative",       "decaying exponential"),
        ("complex pair, left",   "damped oscillation"),
        ("on the jω axis",       "sustained oscillation"),
        ("anywhere on the right","growing — unstable")]
for i,(a,b) in enumerate(rows):
    y = 48 + i*26
    d.p.append(f'<text x="360" y="{y}" font-size="11" style="fill:{INK}" '
               f'font-weight="600">{esc(a)}</text>')
    d.p.append(f'<text x="360" y="{y+12}" font-size="10" style="fill:{INK}" '
               f'opacity=".7">{esc(b)}</text>')
write("poles.svg", svg(620, 262, [d],
      "The s-plane: poles in the left half give decaying responses, poles on the imaginary axis "
      "sustained oscillation, and poles in the right half growth"))
