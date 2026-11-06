#!/usr/bin/env python3
"""Figures for the Week 11 presentation: metal–semiconductor interfaces.

Every figure is written twice: figures/NAME.svg (text as paths, for the slides)
and figures/NAME.png (300 dpi, for the Word notes). All labels use matplotlib's
mathtext with the STIX fonts, so symbols match the typeset equations.

    python3 tools/figures.py
"""
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyArrowPatch

OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "figures")
os.makedirs(OUT, exist_ok=True)

INK = "#14213D"       # text and band edges
SOFT = "#5A6975"      # secondary text
COP = "#B4622F"       # Fermi level, accents
TEAL = "#1C6E7E"      # barriers, energy arrows
METAL = "#F1E2D6"     # metal fill
SEMI = "#E3EEF1"      # semiconductor fill
BAND = "#C9DCE2"      # filled valence band
PLUS = "#1C6E7E"

plt.rcParams.update({
    "mathtext.fontset": "stix", "font.family": "STIXGeneral", "font.size": 15,
    "svg.fonttype": "path", "axes.linewidth": 1.0, "text.color": INK,
    "axes.edgecolor": INK, "axes.labelcolor": INK, "xtick.color": INK, "ytick.color": INK,
})


def save(fig, name):
    fig.savefig(os.path.join(OUT, name + ".svg"), transparent=True, bbox_inches="tight", pad_inches=0.05)
    fig.savefig(os.path.join(OUT, name + ".png"), dpi=300, facecolor="white", bbox_inches="tight", pad_inches=0.08)
    plt.close(fig)
    print("  ", name)


def canvas(w, h):
    fig = plt.figure(figsize=(w, h))
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, w * 100)
    ax.set_ylim(0, h * 100)
    ax.axis("off")
    return fig, ax


def arrow(ax, x1, y1, x2, y2, color=TEAL, lw=1.6, style="-|>", both=False, ms=14):
    st = "<|-|>" if both else style
    ax.add_patch(FancyArrowPatch((x1, y1), (x2, y2), arrowstyle=st, mutation_scale=ms,
                                 color=color, lw=lw, shrinkA=0, shrinkB=0))


def hline(ax, x1, x2, y, color=INK, lw=2.2, ls="-"):
    ax.plot([x1, x2], [y, y], color=color, lw=lw, ls=ls, solid_capstyle="butt")


def txt(ax, x, y, s, color=INK, size=15, ha="center", va="center", **kw):
    ax.text(x, y, s, color=color, fontsize=size, ha=ha, va=va, **kw)


# ---------------------------------------------------------------------------
# 1. Energy levels of an isolated n-type semiconductor
# ---------------------------------------------------------------------------
def levels():
    fig, ax = canvas(6.4, 4.6)
    x0, x1 = 120, 470
    yv, yc, yf, yev = 420, 300, 270, 160          # E_vac, E_c, E_F, E_v
    ax.add_patch(Rectangle((x0, yc), x1 - x0, 40, color=SEMI, lw=0))      # empty CB states
    ax.add_patch(Rectangle((x0, yev - 110), x1 - x0, 110, color=BAND, lw=0))   # full VB
    hline(ax, x0, x1, yv, ls=(0, (5, 4)), lw=1.4)
    hline(ax, x0, x1, yc)
    hline(ax, x0, x1, yev)
    hline(ax, x0, x1, yf, color=COP, ls=(0, (7, 4)), lw=2)
    txt(ax, x1 + 12, yv, r"$E_{\mathrm{vac}}$", ha="left")
    txt(ax, x1 + 12, yc + 4, r"$E_c$", ha="left")
    txt(ax, x1 + 12, yf - 6, r"$E_F$", ha="left", color=COP)
    txt(ax, x1 + 12, yev, r"$E_v$", ha="left")
    txt(ax, 340, yc + 22, "conduction band (mostly empty)", size=12, color=SOFT)
    txt(ax, (x0 + x1) / 2, yev - 45, "valence band (almost full)", size=12, color=SOFT)
    txt(ax, (x0 + x1) / 2, yv + 18, "vacuum level: an electron at rest just outside", size=12, color=SOFT)
    arrow(ax, 165, yv, 165, yc, color=INK)
    txt(ax, 155, (yv + yc) / 2, r"$q\chi$", ha="right")
    arrow(ax, 255, yv, 255, yf, color=TEAL)
    txt(ax, 263, (yv + yf) / 2 + 20, r"$q\Phi_s$", ha="left", color=TEAL)
    arrow(ax, 400, yc, 400, yev, color=INK, both=True)
    txt(ax, 410, (yc + yev) / 2, r"$E_g$", ha="left")
    save(fig, "levels")


# ---------------------------------------------------------------------------
# 2. Metal and n-semiconductor before contact (phi_m > phi_s)
# ---------------------------------------------------------------------------
def before():
    fig, ax = canvas(9.0, 5.0)
    yv = 450
    # metal
    mx0, mx1, yFm = 60, 300, 210
    ax.add_patch(Rectangle((mx0, 60), mx1 - mx0, yFm - 60, color=METAL, lw=0))
    hline(ax, mx0, mx1, yFm, color=COP, ls=(0, (7, 4)), lw=2)
    txt(ax, (mx0 + mx1) / 2, 130, "filled states", size=12, color=SOFT)
    txt(ax, (mx0 + mx1) / 2, 30, "metal", size=16)
    txt(ax, mx0 - 8, yFm, r"$E_{F,m}$", ha="right", color=COP)
    arrow(ax, 110, yv, 110, yFm, color=TEAL)
    txt(ax, 120, (yv + yFm) / 2, r"$q\Phi_m$", ha="left", color=TEAL)
    # semiconductor
    sx0, sx1 = 530, 820
    yc, yf, yev = 330, 300, 190
    ax.add_patch(Rectangle((sx0, yev - 120), sx1 - sx0, 120, color=BAND, lw=0))
    hline(ax, sx0, sx1, yc)
    hline(ax, sx0, sx1, yev)
    hline(ax, sx0, sx1, yf, color=COP, ls=(0, (7, 4)), lw=2)
    txt(ax, sx1 + 10, yc + 6, r"$E_c$", ha="left")
    txt(ax, sx1 + 10, yf - 8, r"$E_{F,s}$", ha="left", color=COP)
    txt(ax, sx1 + 10, yev, r"$E_v$", ha="left")
    txt(ax, (sx0 + sx1) / 2, 30, r"$n$-type semiconductor", size=16)
    arrow(ax, 580, yv, 580, yc, color=INK)
    txt(ax, 572, (yv + yc) / 2, r"$q\chi$", ha="right")
    arrow(ax, 680, yv, 680, yf, color=TEAL)
    txt(ax, 690, (yv + yf) / 2 + 30, r"$q\Phi_s$", ha="left", color=TEAL)
    arrow(ax, 780, yc, 780, yev, color=INK, both=True)
    txt(ax, 772, (yc + yev) / 2, r"$E_g$", ha="right")
    # vacuum level and the Fermi-level step
    hline(ax, mx0, sx1, yv, ls=(0, (5, 4)), lw=1.4)
    txt(ax, sx1 + 10, yv, r"$E_{\mathrm{vac}}$", ha="left")
    hline(ax, mx1, 440, yFm, color=COP, lw=1, ls=":")
    hline(ax, 440, sx0, yf, color=COP, lw=1, ls=":")
    arrow(ax, 440, yf, 440, yFm, color=COP)
    txt(ax, 450, (yf + yFm) / 2, r"$q(\Phi_m-\Phi_s)$", ha="left", color=COP, size=14)
    txt(ax, 415, 375, r"electrons will flow $\rightarrow$ metal", size=12, color=SOFT, ha="center")
    save(fig, "before-contact")


# ---------------------------------------------------------------------------
# 3. Schottky contact at equilibrium
# ---------------------------------------------------------------------------
def bands_after(ax, xi, xw, xe, yF, Vbi, gap, chi, phiB_label=True, Vshift=0.0, label_W=True):
    """Draw n-semiconductor bands bending up to the interface at xi."""
    x = np.linspace(xi, xe, 300)
    ycb_bulk = yF + 30 + Vshift
    bend = np.where(x < xw, (Vbi) * (1 - (x - xi) / (xw - xi)) ** 2, 0)
    yc = ycb_bulk + bend
    ax.plot(x, yc, color=INK, lw=2.2)
    ax.plot(x, yc - gap, color=INK, lw=2.2)
    ax.fill_between(x, np.maximum(yc - gap - 60, 75), yc - gap, color=BAND, lw=0)
    ax.plot(x, yc + chi, color=INK, lw=1.2, ls=(0, (5, 4)))
    return x, yc


def equilibrium():
    fig, ax = canvas(9.0, 5.4)
    xm0, xi, xw, xe = 60, 300, 560, 840
    yF, Vbi, gap, chi = 220, 80, 135, 150
    ax.add_patch(Rectangle((xm0, 70), xi - xm0, yF - 70, color=METAL, lw=0))
    x, yc = bands_after(ax, xi, xw, xe, yF, Vbi, gap, chi)
    hline(ax, xm0, xe, yF, color=COP, ls=(0, (7, 4)), lw=2)
    ax.plot([xi, xi], [60, 520], color=INK, lw=1.4)
    ax.plot([xm0, xi], [yc[0] + chi, yc[0] + chi], color=INK, lw=1.2, ls=(0, (5, 4)))
    txt(ax, xe + 10, yc[-1] + 4, r"$E_c$", ha="left")
    txt(ax, xe + 10, yF - 8, r"$E_F$", ha="left", color=COP)
    txt(ax, xe + 10, yc[-1] - gap, r"$E_v$", ha="left")
    txt(ax, xe + 10, yc[-1] + chi, r"$E_{\mathrm{vac}}$", ha="left")
    # barrier height from the metal side
    arrow(ax, xi + 22, yF, xi + 22, yc[0], color=TEAL)
    txt(ax, xi + 14, yF + 120, r"$q\Phi_{Bn}$", ha="right", color=TEAL)
    # built-in potential from the semiconductor side
    xa = xw + 70
    hline(ax, xi + 40, xa + 15, yc[0], color=SOFT, lw=0.8, ls=":")
    arrow(ax, xa, yc[-1], xa, yc[0], color=COP)
    txt(ax, xa + 10, (yc[-1] + yc[0]) / 2, r"$qV_{bi}$", ha="left", color=COP)
    # depletion region: donor ions and the electron sheet
    for xx in np.linspace(xi + 70, xw - 30, 4):
        yy = np.interp(xx, x, yc) - 28
        txt(ax, xx, yy, r"$\oplus$", color=PLUS, size=17)
    for yy in np.linspace(110, 190, 5):
        txt(ax, xi - 14, yy, r"$-$", color=COP, size=17)
    arrow(ax, xi, 45, xw, 45, color=INK, both=True, lw=1.2)
    txt(ax, (xi + xw) / 2, 25, r"depletion width $W$", size=14)
    ax.plot([xw, xw], [45, 260], color=SOFT, lw=0.8, ls=":")
    txt(ax, (xm0 + xi) / 2, 25, "metal", size=16)
    txt(ax, (xw + xe) / 2 + 20, 25, r"$n$-type semiconductor", size=16)
    txt(ax, xi + 150, np.interp(xi + 150, x, yc) + 22, r"ionised donors $N_D^{+}$", size=13, color=PLUS, ha="left")
    txt(ax, xi - 30, 150, "electron\nsheet", size=12, color=COP, ha="right")
    save(fig, "equilibrium")


# ---------------------------------------------------------------------------
# 4. Under bias: equilibrium, forward, reverse
# ---------------------------------------------------------------------------
def bias():
    fig, axs = plt.subplots(1, 3, figsize=(13.5, 4.6))
    titles = ["Equilibrium,  $V=0$", "Forward bias,  $V>0$", "Reverse bias,  $V=-V_R$"]
    shifts = [0, 45, -45]                      # semiconductor E_F moves by qV
    def draw(ax, title, sh):
        ax.set_xlim(0, 450); ax.set_ylim(0, 420); ax.axis("off")
        xm0, xi, xe = 10, 140, 440
        yFm, Vbi0, gap = 190, 75, 125
        yFs = yFm + sh
        Vb = Vbi0 - sh                        # band bending q(Vbi - V)
        W = 150 * np.sqrt(max(Vb, 5) / Vbi0)
        xw = xi + W
        x = np.linspace(xi, xe, 200)
        ycb = yFs + 28
        yc = ycb + np.where(x < xw, Vb * (1 - (x - xi) / (xw - xi)) ** 2, 0)
        ax.add_patch(Rectangle((xm0, 60), xi - xm0, yFm - 60, color=METAL, lw=0))
        ax.plot(x, yc, color=INK, lw=2); ax.plot(x, yc - gap, color=INK, lw=2)
        ax.fill_between(x, yc - gap - 60, yc - gap, color=BAND, lw=0)
        ax.plot([xm0, xi], [yFm, yFm], color=COP, lw=2, ls=(0, (6, 3)))
        ax.plot([xi, xe], [yFs, yFs], color=COP, lw=2, ls=(0, (6, 3)))
        ax.plot([xi, xi], [40, 400], color=INK, lw=1.2)
        ax.add_patch(FancyArrowPatch((xi + 16, yFm), (xi + 16, yc[0]), arrowstyle="-|>",
                                     mutation_scale=12, color=TEAL, lw=1.4))
        ax.text(xi + 8, yFm + 135, r"$q\Phi_{Bn}$", color=TEAL, fontsize=18.9, ha="right")
        xa = xw + 40
        ax.plot([xi + 30, xa + 10], [yc[0], yc[0]], color=SOFT, lw=0.8, ls=":")
        ax.add_patch(FancyArrowPatch((xa, ycb), (xa, yc[0]), arrowstyle="-|>",
                                     mutation_scale=12, color=COP, lw=1.4))
        lab = {0: r"$qV_{bi}$", 45: r"$q(V_{bi}-V)$", -45: r"$q(V_{bi}+V_R)$"}[sh]
        ax.text(xa + 8, (ycb + yc[0]) / 2, lab, color=COP, fontsize=17.6, va="center")
        if sh:
            ax.add_patch(FancyArrowPatch((xe - 30, yFm), (xe - 30, yFs), arrowstyle="<|-|>",
                                         mutation_scale=10, color=INK, lw=1.0))
            ax.plot([xi, xe], [yFm, yFm], color=COP, lw=0.8, ls=":")
            ax.text(xe - 30, min(yFm, yFs) - 22, r"$q|V|$", ha="center", va="center", fontsize=17.6)
        ax.add_patch(FancyArrowPatch((xi, 25), (xw, 25), arrowstyle="<|-|>", mutation_scale=10,
                                     color=INK, lw=1))
        ax.text((xi + xw) / 2, 2, r"$W$", ha="center", fontsize=17.6)
        ax.text(225, 405, title, ha="center", fontsize=20.2)
        flow = {0: "net current\nzero", 45: "many electrons\ncross: large\ncurrent",
                -45: "flow blocked:\nsmall current\n$I\\approx -I_s$"}[sh]
    for ax, title, sh in zip(axs, titles, shifts):
        draw(ax, title, sh)
    fig.subplots_adjust(wspace=0.05, left=0.01, right=0.99, top=0.98, bottom=0.02)
    save(fig, "bias")
    # the same three panels as separate images, for a step-by-step slide
    for name, title, sh in zip(("bias-eq", "bias-fwd", "bias-rev"), titles, shifts):
        f1, a1 = plt.subplots(figsize=(4.5, 4.6))
        draw(a1, title, sh)
        f1.subplots_adjust(left=0.01, right=0.99, top=0.98, bottom=0.02)
        save(f1, name)


# ---------------------------------------------------------------------------
# 5. Charge, field and energy in the depletion region
# ---------------------------------------------------------------------------
def depletion():
    fig, axs = plt.subplots(3, 1, figsize=(6.6, 6.6), sharex=True)
    W = 1.0
    x = np.linspace(-0.25, 1.5, 600)
    # charge density
    ax = axs[0]
    ax.fill_between([0, W], [1, 1], color=SEMI, lw=0)
    ax.plot([0, 0, W, W, 1.5], [0, 1, 1, 0, 0], color=INK, lw=2)
    ax.annotate("", xy=(-0.02, -1.6), xytext=(-0.02, 0), arrowprops=dict(arrowstyle="-|>", color=COP, lw=2))
    ax.text(0.5, 1.15, r"$\rho = +qN_D$", ha="center", fontsize=14)
    ax.text(0.05, -1.1, "negative electron sheet\nat the metal surface", ha="left", fontsize=11, color=COP)
    ax.set_ylabel(r"$\rho(x)$"); ax.set_ylim(-1.9, 1.6)
    # field: magnitude, maximum at the interface
    ax = axs[1]
    E = np.where((x >= 0) & (x <= W), (W - x), 0)
    ax.plot(x, -E, color=TEAL, lw=2.2)
    ax.text(0.04, -1.05, r"$-\mathcal{E}_{\max}$", fontsize=14, color=TEAL, va="center")
    ax.text(0.6, -0.55, r"$\mathcal{E}(x) = -\dfrac{qN_D}{\varepsilon_s}(W-x)$", fontsize=13)
    ax.set_ylabel(r"$\mathcal{E}(x)$"); ax.set_ylim(-1.3, 0.3)
    # conduction-band edge
    ax = axs[2]
    Ec = np.where(x < 0, np.nan, np.where(x <= W, (W - x) ** 2, 0))
    ax.plot(x, Ec, color=INK, lw=2.2)
    ax.annotate("", xy=(1.25, 1.0), xytext=(1.25, 0), arrowprops=dict(arrowstyle="<|-|>", color=COP, lw=1.6))
    ax.plot([0, 1.3], [1, 1], color=SOFT, lw=0.8, ls=":")
    ax.text(1.29, 0.5, r"$qV_{bi}$", color=COP, fontsize=14, va="center")
    ax.text(0.45, 0.55, r"$E_c(x)$", fontsize=14)
    ax.set_ylabel("energy"); ax.set_ylim(-0.2, 1.3)
    for ax in axs:
        ax.axvline(0, color=INK, lw=1); ax.axvline(W, color=SOFT, lw=0.8, ls=":")
        ax.axhline(0, color=SOFT, lw=0.6)
        ax.set_yticks([]); ax.spines[["top", "right"]].set_visible(False)
    axs[2].set_xticks([0, W]); axs[2].set_xticklabels([r"$0$ (interface)", r"$W$"])
    axs[2].set_xlabel(r"distance into the semiconductor, $x$")
    fig.tight_layout()
    save(fig, "depletion")


# ---------------------------------------------------------------------------
# 6. Ohmic contacts: accumulation, and thermionic emission versus tunnelling
# ---------------------------------------------------------------------------
def ohmic():
    fig, axs = plt.subplots(1, 3, figsize=(13.5, 4.6))
    specs = [("(a) Lightly doped: thick barrier", "thick"),
             ("(b) Heavily doped $n^{+}$: thin barrier", "thin"),
             ("(c) Low work function, $\\Phi_m<\\Phi_s$", "acc")]
    for ax, (title, kind) in zip(axs, specs):
        ax.set_xlim(0, 450); ax.set_ylim(0, 500); ax.axis("off")
        xm0, xi, xe = 10, 140, 440
        yF, gap = 200, 120
        x = np.linspace(xi, xe, 300)
        if kind == "thick":
            yc = yF + 25 + 110 * np.where(x < xi + 200, (1 - (x - xi) / 200) ** 2, 0)
        elif kind == "thin":
            yc = yF + 8 + 127 * np.exp(-(x - xi) / 14)
        else:
            yc = yF + 25 - 40 * np.exp(-(x - xi) / 35)
        ax.add_patch(Rectangle((xm0, 60), xi - xm0, yF - 60, color=METAL, lw=0))
        ax.plot(x, yc, color=INK, lw=2.2); ax.plot(x, yc - gap, color=INK, lw=2.2)
        ax.fill_between(x, yc - gap - 60, yc - gap, color=BAND, lw=0)
        ax.plot([xm0, xe], [yF, yF], color=COP, lw=2, ls=(0, (6, 3)))
        ax.plot([xi, xi], [40, 400], color=INK, lw=1.2)
        ax.text(xe - 2, yc[-1] + 14, r"$E_c$", ha="right", fontsize=18.9)
        ax.text(xe - 2, yF - 18, r"$E_F$", ha="right", fontsize=18.9, color=COP)
        ax.text(225, 485, title, ha="center", fontsize=18.9)
        if kind == "thick":
            ax.add_patch(FancyArrowPatch((380, yc[-1] + 12), (150, yc[0] + 22),
                                         connectionstyle="arc3,rad=0.25", arrowstyle="-|>",
                                         mutation_scale=14, color=TEAL, lw=1.6))
            ax.text(300, 445, "thermionic emission:\nonly hot electrons get over", fontsize=15.5,
                    color=TEAL, ha="center", va="center")
            ax.text(290, 40, "rectifying (Schottky)", fontsize=16.2, ha="center", color=SOFT)
        elif kind == "thin":
            ax.add_patch(FancyArrowPatch((300, yF + 10), (60, yF + 10), arrowstyle="<|-|>",
                                         mutation_scale=14, color=TEAL, lw=1.8))
            ax.text(300, 445, "tunnelling: electrons pass\nthrough a barrier a few nm thick",
                    fontsize=15.5, color=TEAL, ha="center", va="center")
            ax.text(290, 40, "ohmic", fontsize=16.2, ha="center", color=SOFT)
        else:
            for xx in (152, 166, 180, 194):
                ax.plot(xx, yF + 4, "o", color=INK, ms=5)
            ax.add_patch(FancyArrowPatch((360, yF + 40), (60, yF + 40), arrowstyle="<|-|>",
                                         mutation_scale=14, color=TEAL, lw=1.8))
            ax.text(300, 445, "accumulation layer:\nno barrier to electrons", fontsize=15.5,
                    color=TEAL, ha="center", va="center")
            ax.text(290, 40, "ohmic", fontsize=16.2, ha="center", color=SOFT)
    fig.subplots_adjust(wspace=0.05, left=0.01, right=0.99, top=0.98, bottom=0.02)
    save(fig, "ohmic")


# ---------------------------------------------------------------------------
# 7. Schottky diode cross-section
# ---------------------------------------------------------------------------
def device():
    fig, ax = canvas(7.6, 4.6)
    L, R = 80, 560
    ax.add_patch(Rectangle((L, 90), R - L, 110, color=SEMI, ec=INK, lw=1.2))
    txt(ax, (L + R) / 2, 140, r"$n^{+}$ substrate (heavily doped)", size=14)
    ax.add_patch(Rectangle((L, 200), R - L, 120, color="white", ec=INK, lw=1.2))
    txt(ax, L + 15, 230, r"$n$-type epitaxial layer (lightly doped)", size=14, ha="left")
    for xo in (L, R - 150):
        ax.add_patch(Rectangle((xo, 320), 150, 26, color="white", ec=INK, lw=1.2, ls="--"))
        txt(ax, xo + 75, 333, r"SiO$_2$", size=13)
    ax.add_patch(Rectangle((L + 150, 320), R - L - 300, 45, color=METAL, ec=INK, lw=1.2))
    txt(ax, (L + R) / 2, 343, "metal (anode)", size=14)
    t = np.linspace(0, np.pi, 100)
    ax.plot((L + R) / 2 + 105 * np.cos(t), 320 - 55 * np.sin(t), color=SOFT, lw=1.2, ls="--")
    txt(ax, (L + R) / 2, 288, "depletion region", size=12, color=SOFT)
    ax.add_patch(Rectangle((L, 70), R - L, 20, color=METAL, ec=INK, lw=1.2))
    ax.plot([(L + R) / 2] * 2, [365, 410], color=INK, lw=1.4)
    ax.plot((L + R) / 2, 412, "o", color=INK, ms=7)
    txt(ax, (L + R) / 2 + 14, 418, "anode", ha="left", size=13)
    ax.plot([(L + R) / 2] * 2, [70, 28], color=INK, lw=1.4)
    ax.plot((L + R) / 2, 26, "o", color=INK, ms=7)
    txt(ax, (L + R) / 2 + 14, 22, "cathode", ha="left", size=13)
    txt(ax, R + 15, 342, "Schottky\ncontact", ha="left", size=13, color=COP)
    txt(ax, R + 15, 80, "ohmic\ncontact", ha="left", size=13, color=TEAL)
    save(fig, "device")


# ---------------------------------------------------------------------------
# 8. Current–voltage curves
# ---------------------------------------------------------------------------
def iv():
    fig, ax = plt.subplots(figsize=(7.0, 4.4))
    V = np.linspace(-1.0, 1.0, 2001)
    kT = 0.0259
    def diode(Is, Vbr):
        I = Is * (np.exp(V / kT) - 1)
        return np.where(I > 12, np.nan, I)
    ax.plot(V, np.where(V < 0, -0.6 * (1 - np.exp(V / 0.05)), diode(1e-5, 0)), color=COP, lw=2.4, label="Schottky diode")
    ax.plot(V, np.where(V < 0, -0.12 * (1 - np.exp(V / 0.05)), diode(1e-11, 0)), color=TEAL, lw=2.4, label=r"$p$–$n$ diode")
    ax.plot(V, 9 * V, color=INK, lw=1.8, ls=(0, (6, 3)), label="ohmic contact")
    ax.axhline(0, color=INK, lw=0.8); ax.axvline(0, color=INK, lw=0.8)
    ax.set_xlim(-1, 1); ax.set_ylim(-3, 11)
    ax.set_xlabel(r"voltage $V$ (V)"); ax.set_ylabel(r"current $I$ (mA)")
    ax.text(0.22, 7.5, r"turns on" "\n" r"$\approx 0.3$ V", color=COP, ha="right", fontsize=13)
    ax.text(0.80, 3.0, r"turns on" "\n" r"$\approx 0.7$ V", color=TEAL, ha="left", fontsize=13)
    ax.text(-0.97, -2.2, "reverse leakage (exaggerated):\nlarger for the Schottky diode", fontsize=11, color=SOFT)
    ax.legend(frameon=False, loc="upper left", fontsize=12)
    ax.spines[["top", "right"]].set_visible(False)
    fig.tight_layout()
    save(fig, "iv")


# ---------------------------------------------------------------------------
# 9. Ideal versus measured barrier heights on n-Si (Fermi-level pinning)
# ---------------------------------------------------------------------------
def pinning():
    metals = ["Al", "Ti", "W", "Au", "Pt"]
    phim = [4.28, 4.33, 4.55, 5.10, 5.65]
    ideal = [p - 4.05 for p in phim]
    meas = [0.72, 0.50, 0.67, 0.80, 0.90]
    fig, ax = plt.subplots(figsize=(7.0, 4.2))
    xs = np.arange(len(metals))
    ax.bar(xs - 0.2, ideal, 0.38, color=SEMI, ec=INK, lw=1, label=r"ideal: $\Phi_m-\chi$")
    ax.bar(xs + 0.2, meas, 0.38, color=COP, label="measured")
    for xx, a, b in zip(xs, ideal, meas):
        ax.text(xx - 0.2, a + 0.03, f"{a:.2f}", ha="center", fontsize=11)
        ax.text(xx + 0.2, b + 0.03, f"{b:.2f}", ha="center", fontsize=11, color=COP)
    ax.set_xticks(xs); ax.set_xticklabels([f"{m}\n({p:.2f} eV)" for m, p in zip(metals, phim)])
    ax.set_ylabel(r"barrier height $\Phi_{Bn}$ (eV)")
    ax.set_ylim(0, 1.8)
    ax.legend(frameon=False, loc="upper left", fontsize=12)
    ax.spines[["top", "right"]].set_visible(False)
    fig.tight_layout()
    save(fig, "pinning")


if __name__ == "__main__":
    for f in (levels, before, equilibrium, bias, depletion, ohmic, device, iv, pinning):
        f()
