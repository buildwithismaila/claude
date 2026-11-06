#!/usr/bin/env python3
"""Typeset every equation used on the slides as an image (STIX maths).

Writes equations/NAME.svg (vector, text as paths) and equations/NAME.png.
The same LaTeX is used in the Word notes, so both say exactly the same thing.

    python3 tools/equations.py
"""
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "equations")
os.makedirs(OUT, exist_ok=True)
INK = "#14213D"
plt.rcParams.update({"mathtext.fontset": "stix", "font.family": "STIXGeneral", "svg.fonttype": "path"})

EQ = {
    # energies and definitions
    "workfn-m":  r"$q\Phi_m = E_{\mathrm{vac}} - E_{F,m}$",
    "affinity":  r"$q\chi = E_{\mathrm{vac}} - E_c$",
    "workfn-s":  r"$q\Phi_s = q\chi + (E_c - E_F)$",
    "ec-ef":     r"$E_c - E_F = kT\,\ln\!\left(\dfrac{N_c}{N_D}\right)$",
    "gap":       r"$E_g = E_c - E_v$",
    "ef-align":  r"$E_{F,m} = E_{F,s}$",
    # barrier and built-in potential
    "barrier-n": r"$q\Phi_{Bn} = q\left(\Phi_m - \chi\right)$",
    "vbi":       r"$qV_{bi} = q\left(\Phi_m - \Phi_s\right) = q\Phi_{Bn} - \left(E_c - E_F\right)$",
    "barrier-p": r"$q\Phi_{Bp} = E_g - q\left(\Phi_m - \chi\right)$",
    # depletion region
    "W":         r"$W = \sqrt{\dfrac{2\varepsilon_s\left(V_{bi} - V\right)}{qN_D}}$",
    "Emax":      r"$\mathcal{E}_{\max} = \dfrac{qN_D W}{\varepsilon_s}$",
    "W-prop":    r"$W \propto \dfrac{1}{\sqrt{N_D}}$",
    "C":         r"$C = \dfrac{\varepsilon_s}{W}$",
    "image":     r"$\Delta\Phi = \sqrt{\dfrac{q\,\mathcal{E}_{\max}}{4\pi\varepsilon_s}}$",
    # current
    "J":         r"$J = J_s\left[\exp\!\left(\dfrac{qV}{\eta kT}\right) - 1\right]$",
    "Js":        r"$J_s = A^{*\!*}\,T^{2}\,\exp\!\left(-\dfrac{q\Phi_{Bn}}{kT}\right)$",
    "I":         r"$I = I_s\left[\exp\!\left(\dfrac{qV}{\eta kT}\right) - 1\right]$",
    "ohm":       r"$V = I R_c\,,\qquad R_c = \dfrac{\rho_c}{A}$",
    # worked numbers
    "ex-phis":   r"$E_c - E_F = (0.02585)\ln\!\left(\dfrac{2.8\times10^{25}}{1\times10^{22}}\right) = 0.205\ \mathrm{eV}$",
    "ex-phis2":  r"$\Phi_s = 4.05 + 0.205 = 4.26\ \mathrm{eV}$",
    "ex-au":     r"$\Phi_{Bn} = 5.10 - 4.05 = 1.05\ \mathrm{eV}$",
    "ex-au2":    r"$V_{bi} = 5.10 - 4.26 = 0.84\ \mathrm{V}$",
    "ex-W":      r"$W = \sqrt{\dfrac{2\,(1.04\times10^{-10})\,(0.84)}{(1.6\times10^{-19})\,(1\times10^{22})}} = 3.3\times10^{-7}\ \mathrm{m}$",
    "ex-Emax":   r"$\mathcal{E}_{\max} = \dfrac{(1.6\times10^{-19})(1\times10^{22})(3.3\times10^{-7})}{1.04\times10^{-10}} = 5.1\times10^{6}\ \mathrm{V\,m^{-1}}$",
    "ex-pinned": r"$\Phi_{Bn} = 4.70 - 4.05 = 0.65\ \mathrm{eV}$",
    "ex-I":      r"$I = (2\times10^{-6})\left[\exp\!\left(\dfrac{0.20}{0.02585}\right) - 1\right] = (2\times10^{-6})(2290) = 4.58\times10^{-3}\ \mathrm{A}$",
    "ex-W1":     r"$W = \sqrt{\dfrac{2\,(1.04\times10^{-10})\,(0.60)}{(1.6\times10^{-19})\,(1\times10^{22})}} = 2.79\times10^{-7}\ \mathrm{m}\ \ (279\ \mathrm{nm})$",
    "ex-W2":     r"$W = \sqrt{\dfrac{2\,(1.04\times10^{-10})\,(0.60)}{(1.6\times10^{-19})\,(1\times10^{25})}} = 8.8\times10^{-9}\ \mathrm{m}\ \ (8.8\ \mathrm{nm})$",
    "ex-p":      r"$\Phi_{Bp} = 1.12 - (4.28 - 4.05) = 0.89\ \mathrm{eV}$",
    # short symbols for slide text
    "cond-schottky": r"$\Phi_m > \Phi_s$",
    "cond-ohmic":    r"$\Phi_m < \Phi_s$",
    "flat":          r"$E_{F,m} = E_{F,s} = E_F$",
    "bias-fwd":      r"$q\left(V_{bi} - V\right)$",
    "bias-rev":      r"$q\left(V_{bi} + V_R\right)$",
    "ex-Wf":     r"$W_{\mathrm{fwd}} = \sqrt{\dfrac{2\,(1.04\times10^{-10})\,(0.84 - 0.30)}{(1.6\times10^{-19})\,(1\times10^{22})}} = 2.65\times10^{-7}\ \mathrm{m}$",
    "ex-Wr":     r"$W_{\mathrm{rev}} = \sqrt{\dfrac{2\,(1.04\times10^{-10})\,(0.84 + 5)}{(1.6\times10^{-19})\,(1\times10^{22})}} = 8.71\times10^{-7}\ \mathrm{m}$",
    "ex-Js":     r"$J_s = (1.1\times10^{6})(300)^{2}\exp\!\left(-\dfrac{0.80}{0.0259}\right) = 3.8\times10^{-3}\ \mathrm{A\,m^{-2}}$",
    "ex-V":      r"$V = (0.0259)\ln\!\left(\dfrac{1\times10^{4}}{3.8\times10^{-3}}\right) = (0.0259)(14.8) = 0.38\ \mathrm{V}$",
    "V-Js":      r"$V = \dfrac{kT}{q}\,\ln\!\left(\dfrac{J}{J_s}\right)$",
    "Astar":         r"$A^{*\!*}$",
    "W-sum":         r"$W(10^{22}\ \mathrm{m^{-3}}) = 279\ \mathrm{nm}\qquad W(10^{25}\ \mathrm{m^{-3}}) = 8.8\ \mathrm{nm}$",
}


def render(name, tex, size=40):
    fig = plt.figure(figsize=(0.01, 0.01))
    fig.text(0, 0, tex, fontsize=size, color=INK)
    for ext, kw in (("svg", {"transparent": True}), ("png", {"dpi": 200, "transparent": True})):
        fig.savefig(os.path.join(OUT, f"{name}.{ext}"), bbox_inches="tight", pad_inches=0.04, **kw)
    plt.close(fig)


if __name__ == "__main__":
    for k, v in EQ.items():
        render(k, v)
    print(len(EQ), "equations")
