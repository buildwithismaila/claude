# Week 15 — Revision and Final Exam Preparation
<!-- group: Module 5 · Advanced Device Technology -->

**Plan:** overview of the entire curriculum, problem-solving clinic and past-question review. The sections follow the Week 15 headings in your lecturer's note: course overview, formula sheet, problem-solving clinic, past-question style exercises, final examination checklist and comprehensive revision questions.

## Learning objectives

By the end of this week you should be able to:

1. Summarise the whole course and how its ideas connect.
2. Recall and apply the key formulas.
3. Answer definitions, derivations and calculations in examination style.
4. Solve mixed past-question style problems.
5. Check readiness for the final examination.

## Symbols and abbreviations used this week

Every symbol, constant and abbreviation on this page is listed here, even if an earlier week already defined it, so you can study this page on its own.

**Constants and units**

| Symbol | Meaning | Units / typical value |
|---|---|---|
| q | Magnitude of the electronic charge | 1.6×10⁻¹⁹ C |
| k | Boltzmann constant | 8.617×10⁻⁵ eV/K = 1.381×10⁻²³ J/K |
| kT | Thermal energy | 0.0259 eV (often 0.02585 eV) at 300 K |
| kT/q | Thermal voltage | 0.0259 V (about 26 mV) at 300 K |
| h | Planck constant | 6.626×10⁻³⁴ J·s |
| ħ | Reduced Planck constant, h/2π | 1.055×10⁻³⁴ J·s |
| m₀ | Free-electron mass | 9.11×10⁻³¹ kg |
| ε₀ | Permittivity of free space | 8.854×10⁻¹⁴ F/cm |
| ε_s (ε_si) | Permittivity of silicon, 11.7ε₀ | 1.04×10⁻¹² F/cm |
| ε_ox | Permittivity of SiO₂, 3.9ε₀ | 3.45×10⁻¹³ F/cm |
| ε_r | Relative permittivity (dielectric constant) | Si 11.7, SiO₂ 3.9, GaAs 12.9 |
| eV | Electron-volt, a unit of energy | 1 eV = 1.6×10⁻¹⁹ J |
| Å | Ångström, a unit of length | 1 Å = 10⁻¹⁰ m = 0.1 nm |
| μm | Micrometre (micron) | 1 μm = 10⁻⁴ cm = 10⁻⁶ m |

**Symbols**

| Symbol | Meaning | Units / typical value |
|---|---|---|
| E_c (E_C) | Energy of the bottom of the conduction band | eV |
| E_v (E_V) | Energy of the top of the valence band | eV |
| E_g | Band-gap energy, E_c − E_v | eV; Si 1.12, Ge 0.66, GaAs 1.42 at 300 K |
| E_F | Fermi level: the energy at which a state has a 50 % chance of being occupied | eV |
| E_i | Intrinsic Fermi level, close to mid-gap | eV |
| E_a | Activation energy of dopant diffusion | eV; about 3–4 eV |
| f(E) | Fermi–Dirac function: probability that a state at energy E is occupied | dimensionless, 0 to 1 |
| g(E), g_c, g_v | Density of states: allowed states per unit energy per unit volume | states/(eV·cm³) |
| N_c | Effective density of states in the conduction band | cm⁻³; Si 2.8×10¹⁹ at 300 K |
| N_v | Effective density of states in the valence band | cm⁻³; Si 1.04×10¹⁹ at 300 K |
| n | Electron concentration (free electrons per cm³) | cm⁻³ |
| p | Hole concentration (holes per cm³) | cm⁻³ |
| n_i | Intrinsic carrier concentration (n = p = n_i in pure material) | cm⁻³; Si ≈ 1×10¹⁰ at 300 K |
| N_D | Donor concentration | cm⁻³ |
| N_A | Acceptor concentration | cm⁻³ |
| Δn, Δp | Excess electron and hole concentrations above equilibrium | cm⁻³ |
| m∗, m_n∗, m_p∗ | Effective mass of electrons or holes | kg, or as a multiple of m₀ |
| ψ | Wave function (\|ψ\|² is the probability density) | — |
| k (wave vector) | Wave vector, 2π/λ; measures the electron's momentum, p = ħk | m⁻¹ or cm⁻¹ |
| α (Kronig–Penney) | √(2mE)/ħ, set by the electron energy | m⁻¹ |
| P (Kronig–Penney) | Barrier strength mV₀ba/ħ² | dimensionless |
| λ | Wavelength | μm or nm; λ(μm) = 1.24/E(eV) |
| a | Lattice constant: edge length of the cubic unit cell | Å; Si 5.43, Ge and GaAs 5.65 |
| (h k l), {h k l} | Miller indices of a plane; family of equivalent planes | integers |
| d_hkl | Spacing between neighbouring (h k l) planes, a/√(h² + k² + l²) | Å |
| r_nn | Nearest-neighbour distance | Å; Si 2.35 |
| k₀ | Segregation coefficient, C_s/C_l at the freezing interface | dimensionless; B 0.8, P 0.35 |
| C_s | Surface concentration of a diffusion (or solid concentration when freezing) | cm⁻³ |
| C_l, C₀ | Concentration in the melt (liquid); C₀ at the start | cm⁻³ |
| C(x, t) | Dopant concentration at depth x and time t | cm⁻³ |
| D | Diffusion coefficient (dopants in a furnace, or carriers) | cm²/s |
| D₀ | Diffusion constant in D = D₀e^{−E_a/kT} | cm²/s |
| F | Particle flux in Fick's law | particles/(cm²·s) |
| Q | Dose: dopant atoms per unit area (in Weeks 13–14, Q also means charge) | atoms/cm² (C or C/cm² for charge) |
| Φ (dose) | Implanted dose (ions per cm²) | cm⁻² |
| erfc | Complementary error function, erfc(u) = 1 − erf(u); read from a table | dimensionless |
| x_j | Junction depth: where the dopant concentration equals the background | μm |
| N_B (C_B) | Background doping of the wafer (in Week 13, N_B is the base doping) | cm⁻³ |
| R_p | Projected range: average depth at which implanted ions stop | μm |
| ΔR_p | Straggle: spread of the implanted ions' stopping depths | μm |
| N_p | Peak concentration of an implanted profile | cm⁻³ |
| E (field) | Electric field (on band diagrams, E is energy instead) | V/cm |
| μ, μ_n, μ_p | Mobility: drift velocity per unit field (electrons, holes) | cm²/(V·s); Si μ_n 1350, μ_p 480 |
| μ_L, μ_I | Mobility limited by lattice scattering, by ionised-impurity scattering | cm²/(V·s) |
| v_d | Drift velocity | cm/s |
| v_sat | Saturation velocity at high field | ≈ 10⁷ cm/s in Si |
| τ_m | Mean free time between collisions | s; about 0.1–1 ps |
| σ | Conductivity, q(nμ_n + pμ_p) (in Week 8, σ is also a capture cross-section) | S/cm (siemens per cm) |
| ρ | Resistivity, 1/σ | Ω·cm |
| J, J_n, J_p | Current density (total, electrons, holes) | A/cm² |
| D_n, D_p | Diffusion coefficients of electrons and holes | cm²/s; Si 35 and 12.4 |
| G, G_L | Generation rate of electron–hole pairs (G_L: by light) | cm⁻³s⁻¹ |
| R | Recombination rate | cm⁻³s⁻¹ |
| U | Net recombination rate, R − G | cm⁻³s⁻¹ |
| τ, τ_n, τ_p | Minority-carrier lifetime (τ_eff: effective, including surfaces) | s; Si 1 ns – 1 ms |
| N_t | Density of traps (recombination centres) | cm⁻³ |
| n₁, p₁ | SRH parameters n_ie^{(E_t − E_i)/kT} and n_ie^{(E_i − E_t)/kT} | cm⁻³ |
| L, L_n, L_p | Diffusion length √(Dτ): distance a minority carrier travels before recombining | μm or cm |
| S | Surface recombination velocity | cm/s |
| N_st | Density of surface traps | cm⁻² |
| U_s | Recombination rate per unit area at a surface | cm⁻²s⁻¹ |
| V_bi | Built-in potential of a junction or Schottky contact | V; typically 0.5–1 V |
| V, V_a | Applied voltage (positive for forward bias) | V |
| W | Depletion-region width (in Week 13 W_B, W_E are base and emitter widths; in Week 14 W is channel width) | μm or cm |
| x_n, x_p | Parts of the depletion region on the n side and on the p side | μm |
| E_max | Peak electric field, at the junction | V/cm |
| I_s, J_s (I_S) | Saturation current (density) of a diode or transistor | A; A/cm² |
| I | Current | A |
| A (area) | Device or contact area | cm² |
| η | Ideality factor of a diode, 1 (ideal) to 2 | dimensionless |
| C, C_j | Capacitance (junction or depletion capacitance) | F (pF = 10⁻¹² F) |
| Φ_m | Work function of a metal | eV; Al 4.28, Au 5.1 |
| Φ_s | Work function of a semiconductor, χ + (E_c − E_F) | eV |
| χ | Electron affinity: energy from E_c up to the vacuum level | eV; Si 4.05 |
| Φ_B | Schottky barrier height seen from the metal | eV (or V) |
| A∗∗ | Effective Richardson constant | A/(cm²·K²); n-Si ≈ 110 |
| I_E, I_B, I_C | Emitter, base and collector currents | A (mA) |
| V_BE, V_CE, V_CB | Base–emitter, collector–emitter and collector–base voltages | V |
| α | Common-base current gain, I_C/I_E | dimensionless; 0.98–0.999 |
| β | Common-emitter current gain, I_C/I_B (also h_FE) | dimensionless; 50–500 |
| γ (BJT) | Emitter injection efficiency | dimensionless, close to 1 |
| α_T | Base transport factor | dimensionless, close to 1 |
| N_E, W_E, D_E; N_B, W_B, D_B | Doping, width and minority diffusion coefficient of the emitter; of the base | cm⁻³; μm; cm²/s |
| τ_B | Base transit time, W_B²/2D_n | s |
| C_ox | Gate-oxide capacitance per unit area, ε_ox/t_ox | F/cm² |
| t_ox | Gate-oxide thickness | nm |
| φ_F, ψ_s (φ_s) | Bulk Fermi potential (kT/q)ln(N_A/n_i); surface potential (band bending) | V |
| W_d, W_dmax, Q_dmax | MOS depletion width, its maximum at inversion, and the depletion charge then | μm; C/cm² |
| V_T (V_th) | Threshold voltage of a MOSFET | V |
| V_FB | Flat-band voltage | V |
| Φ_ms, Q_f | Gate–substrate work-function difference; fixed oxide charge | V; C/cm² |
| γ (MOSFET) | Body-effect coefficient √(2qε_siN_A)/C_ox | V^{1/2} |
| V_GS, V_DS, V_SB, V_G | Gate–source, drain–source, source–body and gate voltages | V |
| I_D | Drain current | A (mA) |
| W/L | Channel width-to-length ratio | dimensionless |
| g_m | Transconductance, ∂I_D/∂V_GS | S (A/V) |
| k (MOSFET) | Device parameter μ_nC_ox(W/L) | A/V² (mA/V²) |
| μ_i, τ_i (μ_L, μ_I, N_I) | Mobility and scattering time for one scattering mechanism (L: lattice, I: ionised impurity); N_I = ionised-impurity density | cm²/(V·s); s; cm⁻³ |
| J_drift, J_diff | Drift and diffusion parts of the current density | A/cm² |
| G_n, G_p, R_n, R_p | Generation and recombination rates of electrons and holes | cm⁻³s⁻¹ |
| τ_b (τ_bulk), τ_surface | Lifetime from bulk recombination only; from surface recombination only | s |
| U_s, p_s, Δp_s | Surface recombination rate; hole density and excess at the surface | cm⁻²s⁻¹; cm⁻³ |
| p_n, n_p | Minority-carrier density: holes on the n side, electrons on the p side | cm⁻³ |

**Abbreviations**

| Abbreviation | Meaning |
|---|---|
| Si | Silicon |
| Ge | Germanium |
| GaAs | Gallium arsenide |
| SiO₂ | Silicon dioxide (silica), the oxide insulator |
| FCC | Face-centred cubic lattice |
| BCC | Body-centred cubic lattice |
| SC | Simple cubic lattice |
| APF | Atomic packing factor |
| MG-Si | Metallurgical-grade silicon (≈ 98 % pure) |
| EG-Si | Electronic-grade silicon (99.9999999 % or better) |
| CZ | Czochralski crystal growth |
| VPE | Vapour-phase epitaxy |
| LPE | Liquid-phase epitaxy |
| MBE | Molecular-beam epitaxy |
| SRH | Shockley–Read–Hall (trap-assisted) recombination |
| I-V | Current–voltage (measurement or characteristic) |
| C-V | Capacitance–voltage (measurement or characteristic) |
| MOS | Metal–oxide–semiconductor |
| MOSFET | Metal–oxide–semiconductor field-effect transistor |
| BJT | Bipolar junction transistor |
| PGD | Postgraduate Diploma |
| n⁺ | Very heavily doped n-type (similarly p⁺) |


## 15.1 Course overview

The whole course tells one story: **how do we make, control and use the free charges in a crystal?**

| Module | Weeks | The question it answers | The one idea to carry into the exam |
|---|---|---|---|
| 1. Material physics and growth | 1–3 | What is a semiconductor, and how do we make and dope it? | Conductivity is controllable because of a moderate band gap and doping. Crystals are grown pure by CZ and epitaxy, and doped by diffusion (erfc or Gaussian) or implantation (Gaussian at R_p). |
| 2. Bands and statistics | 4–6 | How many electrons and holes are there? | n = N_ce^{−(E_c−E_F)/kT}, p = N_ve^{−(E_F−E_v)/kT}, np = n_i². E_F moves 60 mV per decade of doping, and back to mid-gap when hot. |
| 3. Transport and injection | 7–9 | How do the carriers move, and how long do extra ones last? | J = qnμE + qD dn/dx, D/μ = kT/q. Excess minority carriers recombine with lifetime τ and spread over L = √(Dτ). |
| 4. Junctions and interfaces | 10–12 | What happens where two materials meet? | V_bi = (kT/q) ln(N_{A}N_D/n_i²); I = I_s(e^{qV/kT} − 1); Schottky Φ_B = Φ_m − χ; 1/C² against V gives the doping. |
| 5. Devices | 13–15 | How do transistors work? | BJT: β = α/(1 − α), α = γα_T. MOSFET: V_T = V_FB + 2φ_F + γ√(2φ_F); I_D(sat) = ½μC_ox(W/L)(V_GS − V_T)². |

**How the ideas connect.** Doping (Week 3) sets n and p (Week 5). n and p set conductivity (Week 7). Joining p and n regions creates a built-in field (Week 10). Forward bias injects minority carriers that diffuse and recombine (Weeks 7–9), which gives the diode equation. Two junctions close together give the BJT (Week 13); a field-induced inversion layer gives the MOSFET (Week 14).

## 15.2 Formula sheet

### Physical constants

| Quantity | Symbol | Value |
|---|---|---|
| Electronic charge | q | 1.602×10⁻¹⁹ C |
| Boltzmann constant | k | 1.381×10⁻²³ J/K = 8.617×10⁻⁵ eV/K |
| Thermal energy at 300 K | kT | 0.0259 eV |
| Thermal voltage at 300 K | kT/q | 0.0259 V (25.9 mV) |
| Planck constant | h | 6.626×10⁻³⁴ J·s |
| Reduced Planck constant | ħ | 1.055×10⁻³⁴ J·s |
| Free electron mass | m₀ | 9.109×10⁻³¹ kg |
| Permittivity of free space | ε₀ | 8.854×10⁻¹⁴ F/cm |
| Speed of light | c | 3×10¹⁰ cm/s |
| Electron-volt | 1 eV | 1.602×10⁻¹⁹ J |
| Photon wavelength | λ | 1.24/E (μm, with E in eV) |

### Material data at 300 K

| | Si | Ge | GaAs |
|---|---|---|---|
| Crystal | Diamond | Diamond | Zinc blende |
| Lattice constant a (Å) | 5.43 | 5.65 | 5.65 |
| Atoms/cm³ | 5.0×10²² | 4.4×10²² | 4.4×10²² |
| E_g (eV) | 1.12 (indirect) | 0.66 (indirect) | 1.42 (direct) |
| n_i (cm⁻³) | 1×10¹⁰ | 2.4×10¹³ | 2×10⁶ |
| N_c (cm⁻³) | 2.8×10¹⁹ | 1.04×10¹⁹ | 4.7×10¹⁷ |
| N_v (cm⁻³) | 1.04×10¹⁹ | 6.0×10¹⁸ | 7.0×10¹⁸ |
| μ_n (cm²/V·s) | 1350 | 3900 | 8500 |
| μ_p (cm²/V·s) | 480 | 1900 | 400 |
| D_n, D_p (cm²/s) | 35, 12.4 | 101, 49 | 220, 10 |
| ε_r | 11.7 | 16.0 | 12.9 |
| χ (eV) | 4.05 | 4.0 | 4.07 |
| v_sat (cm/s) | 1×10⁷ | 6×10⁶ | ≈ 1×10⁷ (peak 2×10⁷) |
| Melting point (°C) | 1414 | 937 | 1238 |

### Crystals and Miller indices

    Miller indices: intercepts → reciprocals → clear fractions → (h k l)
    d_{hkl} = a / √(h² + k² + l²)      (cubic)
    Diamond: 8 atoms/cell, coordination 4, r_nn = (√3/4)a, APF = 0.34
    SC 1, BCC 2, FCC 4 atoms/cell;  APF 0.52, 0.68, 0.74

### Growth and doping

    SiO₂ + 2C → Si + 2CO;   Si + 3HCl → SiHCl₃ + H₂;   SiHCl₃ + H₂ → Si + 3HCl
    Segregation: k₀ = C_s/C_l;   C_s = k₀C₀(1 − f)^{k₀ − 1}
    Fick 1: F = −D ∂C/∂x;   Fick 2: ∂C/∂t = D ∂²C/∂x²;   D = D₀ e^{−E_a/kT}
    Constant source: C = C_s erfc(x/2√(Dt));   Q = (2/√π)C_s√(Dt)
    Limited source: C = (Q/√(πDt)) exp(−x²/4Dt)
    Implant: N(x) = (Φ/√(2π)ΔR_p) exp(−(x − R_p)²/2ΔR_p²);   N_p ≈ 0.4Φ/ΔR_p;   Φ = It/qA

### Bands and statistics

    Schrödinger: −(ħ²/2m) d²ψ/dx² + Vψ = Eψ
    Kronig–Penney: P sin(αa)/(αa) + cos(αa) = cos(ka)
    1/m∗ = (1/ħ²) d²E/dk²
    f(E) = 1/(1 + e^{(E − E_F)/kT})
    g_c(E) = (4π(2m_n∗)^{3/2}/h³)√(E − E_c)
    n = N_c e^{−(E_c − E_F)/kT};   p = N_v e^{−(E_F − E_v)/kT}
    N_c = 2(2πm_n∗kT/h²)^{3/2}
    n_i = √(N_cN_v) e^{−E_g/2kT};   np = n_i²
    n = n_i e^{(E_F − E_i)/kT};   p = n_i e^{(E_i − E_F)/kT}
    n = (N_D − N_A)/2 + √(((N_D − N_A)/2)² + n_i²)
    E_F − E_i = kT ln(N_D/n_i);   E_i − E_F = kT ln(N_A/n_i)

### Transport

    v_d = μE;   μ = qτ_m/m∗;   1/μ = 1/μ_L + 1/μ_I
    J_drift = q(nμ_n + pμ_p)E;   σ = q(nμ_n + pμ_p);   ρ = 1/σ
    J_n = qnμ_nE + qD_n dn/dx;   J_p = qpμ_pE − qD_p dp/dx
    Einstein: D/μ = kT/q
    v_d = μE/[1 + (μE/v_sat)^β]^{1/β}

### Recombination and continuity

    SRH: U = (np − n_i²)/[τ_p(n + n₁) + τ_n(p + p₁)];   τ = 1/(σv_thN_t)
    Low-level, n-type: U = Δp/τ_p;   Δp(t) = Δp(0)e^{−t/τ_p}
    ∂Δp/∂t = D_p ∂²Δp/∂x² − μ_pE ∂Δp/∂x + G_L − Δp/τ_p
    L = √(Dτ);   Δp(x) = Δp(0)e^{−x/L_p}
    Surface: U_s = SΔp_s;   S = σv_thN_st;   1/τ_eff = 1/τ_b + 2S/W

### Junctions and contacts

    V_bi = (kT/q) ln(N_{A}N_D/n_i²)
    W = √((2ε_s/q)(V_bi − V)(1/N_A + 1/N_D));   N_Ax_p = N_Dx_n;   E_max = qN_Dx_n/ε_s
    I = I_s(e^{qV/kT} − 1);   J_s = qn_i²(D_p/(L_pN_D) + D_n/(L_nN_A))
    C_j = ε_sA/W;   1/C² = 2(V_bi − V)/(qε_sNA²);   N = 2/(qε_sA²|d(1/C²)/dV|)
    Schottky: Φ_B = Φ_m − χ;   V_bi = Φ_m − Φ_s;   J_s = A∗∗T²e^{−qΦ_B/kT}
    Ohmic (tunnelling): N_D ≳ 10¹⁹ cm⁻³

### Devices

    BJT:  I_C = I_S e^{qV_BE/kT},   I_S = qAD_Bn_i²/(N_{B}W_B)
          γ = 1/[1 + D_{E}N_{B}W_B/(D_{B}N_{E}W_E)],   α_T ≈ 1 − W_B²/2L_n²
          α = γα_T,   β = α/(1 − α),   I_E = I_C + I_B,   τ_B = W_B²/2D_B
    MOS:  C_ox = ε_ox/t_ox,   φ_F = (kT/q)ln(N_A/n_i),   W_dmax = √(4ε_sφ_F/qN_A)
          V_T = V_FB + 2φ_F + √(4qε_sN_Aφ_F)/C_ox,   V_FB = Φ_ms − Q_f/C_ox
          Linear: I_D = μC_ox(W/L)[(V_GS − V_T)V_DS − V_DS²/2]
          Saturation: I_D = ½μC_ox(W/L)(V_GS − V_T)²,   g_m = μC_ox(W/L)(V_GS − V_T)

### Rules of thumb

- Each decade of doping moves E_F by 60 mV; each 60 mV of forward bias raises diode current tenfold (300 K).
- n_i(Si) roughly doubles every 8 °C.
- Doping 10¹⁶ cm⁻³ in Si = 1 dopant per 5×10⁶ Si atoms; ρ ≈ 0.5 Ω·cm (n-type), 1.4 Ω·cm (p-type).
- Diffusion length in good Si: tens to hundreds of μm.

## 15.3 Problem-solving clinic

### How to answer each type of question

1. **Definitions** (2–3 marks). One clear sentence, then an example, then the formula if there is one. *"The Fermi level is the energy at which the probability of occupation is ½; in n-type Si it lies near E_c; E_F − E_i = kT ln(N_D/n_i)."*
2. **"Explain" and "describe"** questions want the **mechanism**, not just a list. Use the pattern: what happens physically → the equation → the consequence.
3. **Derivations.** List the assumptions first, number the steps, and box the final result. Examiners give marks for the assumptions.
4. **Calculations.** Write the formula, substitute **with units**, give the answer to 2–3 significant figures with units. Then sanity-check the size of the answer.
5. **Comparisons.** Use a table with three to six rows.
6. **Diagrams** earn marks: band diagrams, carrier profiles, the CZ puller, MOS band bending, BJT and MOSFET cross-sections, I-V curves.

### Unit traps that cost marks

| Trap | Fix |
|---|---|
| Mixing μm and cm | 1 μm = 10⁻⁴ cm. Convert depths and widths to cm before using cm²/s, cm⁻³ |
| Mixing eV and J | kT = 0.02585 eV at 300 K; only convert to joules (× 1.6×10⁻¹⁹) when multiplying by something in SI |
| Forgetting the factor ½ | I_D(sat) = **½**μC_ox(W/L)(V_GS − V_T)² |
| Using the wrong form of diffusion length | Use the form the question gives: √(Dt), √(2Dt) or 2√(Dt) |
| Natural log against log₁₀ | All the semiconductor formulas use ln. ln(10ⁿ) = 2.303n |
| Dose units | Dose is per cm² (atoms/cm²); concentration is per cm³ |

### Sanity checks

| Quantity | Typical size |
|---|---|
| Carrier concentrations | 10⁴ – 10²⁰ cm⁻³ |
| n_i (Si, 300 K) | 10¹⁰ cm⁻³ |
| E_F − E_i | 0.2 – 0.5 eV |
| Diffusion coefficients (dopants in a furnace) | 10⁻¹⁵ – 10⁻¹² cm²/s |
| Carrier diffusion coefficients | 1 – 100 cm²/s |
| Built-in voltage | 0.5 – 1.0 V |
| Depletion width | 0.01 – 10 μm |
| BJT β | 20 – 500 |
| MOSFET V_T | 0.2 – 2 V |

## 15.4 Past-question style exercises (with solutions)

### E1. Find the Miller indices of a plane with intercepts 4a, 2b and ∞c.

Reciprocals 1/4, 1/2, 0. Multiply by 4: **(1 2 0)**. The plane is parallel to the z-axis.

### E2. Constant-source diffusion with C_s = 5×10¹⁹ cm⁻³, D = 2×10⁻¹³ cm²/s, t = 2 h. Find the concentration at 0.3 μm.

    t = 7200 s,   √(Dt) = √(2×10⁻¹³ × 7200) = √(1.44×10⁻⁹) = 3.79×10⁻⁵ cm
    u = x/2√(Dt) = 3×10⁻⁵ / (2 × 3.79×10⁻⁵) = 0.395
    erfc(0.395) = 0.576
    C = 5×10¹⁹ × 0.576 = 2.88×10¹⁹ cm⁻³

### E3. Silicon is doped with N_A = 2×10¹⁶ cm⁻³ at 300 K (n_i = 10¹⁰ cm⁻³). Find p, n and the Fermi level relative to E_i.

    p ≈ N_A = 2×10¹⁶ cm⁻³
    n = n_i²/p = 10²⁰/(2×10¹⁶) = 5×10³ cm⁻³
    E_i − E_F = kT ln(p/n_i) = 0.02585 ln(2×10⁶) = 0.02585 × 14.51 = 0.375 eV

E_F lies 0.375 eV below E_i.

### E4. Find the resistivity of n-type Si with N_D = 10¹⁵ cm⁻³ and μ_n = 1350 cm²/V·s.

    σ = qN_Dμ_n = 1.6×10⁻¹⁹ × 10¹⁵ × 1350 = 0.216 S/cm
    ρ = 1/σ = 4.63 Ω·cm

### E5. Holes in n-Si have μ_p = 450 cm²/V·s and lifetime 5 μs. Find D_p and the diffusion length L_p.

    D_p = (kT/q)μ_p = 0.02585 × 450 = 11.6 cm²/s
    L_p = √(D_pτ_p) = √(11.6 × 5×10⁻⁶) = 7.6×10⁻³ cm = 76 μm

### E6. A Si p⁺n junction has N_A = 10¹⁷ cm⁻³ and N_D = 10¹⁵ cm⁻³. Find V_bi and the zero-bias depletion width.

    V_bi = (kT/q) ln(N_{A}N_D/n_i²) = 0.02585 ln(10³²/10²⁰) = 0.02585 × 27.63 = 0.714 V

One-sided junction, so the depletion region is almost all on the lightly doped n side:

    W ≈ √(2ε_sV_bi/qN_D) = √(2 × 1.04×10⁻¹² × 0.714 / (1.6×10⁻¹⁹ × 10¹⁵)) = 9.6×10⁻⁵ cm = 0.96 μm

### E7. A diode has I_s = 2×10⁻¹⁴ A. Find the current at V = 0.65 V and 300 K.

    I = I_s(e^{qV/kT} − 1) = 2×10⁻¹⁴ × e^{0.65/0.02585} = 2×10⁻¹⁴ × 8.3×10¹⁰ = 1.66 mA

### E8. A BJT has β = 150 and I_B = 20 μA. Find I_C, I_E and α.

    I_C = βI_B = 150 × 20 μA = 3.00 mA
    I_E = I_C + I_B = 3.02 mA
    α = β/(β + 1) = 150/151 = 0.9934

### E9. An nMOS has μ_nC_ox(W/L) = 0.8 mA/V² and V_T = 0.7 V, with V_GS = 2 V. Find I_D for V_DS = 0.5 V and for V_DS = 3 V.

V_GS − V_T = 1.3 V.

    V_DS = 0.5 V < 1.3 V → linear:  I_D = 0.8 × [1.3 × 0.5 − 0.5²/2] = 0.8 × 0.525 = 0.42 mA
    V_DS = 3 V ≥ 1.3 V → saturation: I_D = ½ × 0.8 × 1.3² = 0.4 × 1.69 = 0.676 mA

## 15.5 Final examination checklist

**Before the exam, can you:**

- [Week 1] compare conductors, semiconductors and insulators; Si, Ge and GaAs; find Miller indices including ∞ and negative intercepts?
- [Week 2] describe MG-Si → EG-Si, the CZ method with its advantages and limitations, and compare VPE, LPE, MBE?
- [Week 3] state Fick's laws; use the erfc and Gaussian profiles; calculate junction depth, implant peak and dose?
- [Week 4] state the Schrödinger equation and explain the Kronig–Penney model; compare direct and indirect gaps; derive n_i?
- [Week 5] use the Fermi–Dirac function; calculate n, p and E_F for any doping; explain the three temperature regions?
- [Week 7] calculate drift current and conductivity; explain scattering; state and use the Einstein relation?
- [Week 8] explain velocity saturation, hot carriers, SRH recombination and lifetime?
- [Week 9] write the continuity equation and solve it for steady injection; explain surface recombination velocity?
- [Week 10] explain the depletion region; calculate V_bi and W; derive the Shockley equation?
- [Week 11] draw Schottky and Ohmic band diagrams in equilibrium and under bias?
- [Week 12] extract doping and V_bi from a 1/C² plot; extract I_s and η from an I-V plot?
- [Week 13] explain BJT operation and minority-carrier profiles; use γ, α_T, α, β?
- [Week 14] explain accumulation, depletion, inversion; use V_T; calculate I_D in each region?

**On the day:** bring a scientific calculator (with e^x and ln), a ruler for diagrams, and spare pens. Read every question first, start with the one you know best, and leave 10 minutes to check units.

## 15.6 Comprehensive revision questions

Work through these without notes, then check against the week shown. Full worked answers for the 50 PGD examination questions are on the next page (the answer key) and in each week.

1. Define a semiconductor and explain why its conductivity rises with temperature. (Week 1)
2. Explain covalent bonding in silicon and electron–hole pair generation. (Week 1)
3. Find the Miller indices of planes with intercepts (a) a, 2b, 3c; (b) 2a, 3b, ∞c. (Week 1)
4. Describe the conversion of MG-Si to EG-Si and the Czochralski method. (Week 2)
5. Compare VPE, LPE and MBE. (Week 2)
6. State Fick's first and second laws and the two diffusion profiles. (Week 3)
7. Compare diffusion and ion implantation. Find the junction depth of an implant with N_p = 10¹⁸ cm⁻³, R_p = 0.2 μm, ΔR_p = 0.04 μm into N_B = 10¹⁶ cm⁻³. (Week 3; answer x_j = 0.2 + 0.04√(2 ln 100) = 0.321 μm)
8. Explain the Kronig–Penney model and how it gives energy bands. (Week 4)
9. Derive n_i = √(N_cN_v)e^{−E_g/2kT}. (Week 4)
10. Write the Fermi–Dirac function and describe it at 0 K and 300 K. (Week 5)
11. Find n, p and E_F for Si with N_D = 5×10¹⁵ cm⁻³. (Week 5; n = 5×10¹⁵, p = 2×10⁴ cm⁻³, E_F − E_i = 0.339 eV)
12. Derive the drift current density and the Einstein relation. (Week 7)
13. Explain SRH recombination and define minority-carrier lifetime. (Week 8)
14. Derive the minority-carrier continuity equation and solve it for steady injection into a long bar. (Week 9)
15. Explain the formation of the depletion region; derive the Shockley diode equation. (Week 10)
16. Distinguish Schottky and Ohmic contacts with band diagrams. (Week 11)
17. Explain how C-V measurements give the doping concentration. (Week 12)
18. Explain BJT operation and derive β = α/(1 − α). (Week 13)
19. Explain accumulation, depletion and inversion; derive the saturation condition of a MOSFET. (Week 14)
20. Compare a BJT and a MOSFET. (Week 14)

---

## Practice questions

These extra questions practise this week's ideas. Work each one on paper before reading the solution; the calculation questions follow the same Question, Given, Find, Solution, Answer layout as the worked examples.

#### Practice 15.1: one sample, every property

**Question.** n-type silicon has N_D = 2×10¹⁶ cm⁻³, μ_n = 1200 cm²/V·s, μ_p = 420 cm²/V·s and τ_p = 2 μs. At 300 K find (a) n and p, (b) E_F − E_i, (c) the conductivity, (d) D_p and (e) the hole diffusion length.

**Given:** N_D = 2×10¹⁶ cm⁻³, n_i = 10¹⁰ cm⁻³, μ_n = 1200, μ_p = 420 cm²/V·s, τ_p = 2×10⁻⁶ s.

**Find:** n, p, E_F − E_i, σ, D_p, L_p.

**Solution.**

    (a) n = 2×10¹⁶ cm⁻³,  p = 10²⁰/2×10¹⁶ = 5×10³ cm⁻³
    (b) E_F − E_i = 0.0259 ln(2×10⁶) = 0.376 eV
    (c) σ = qnμ_n = 1.6×10⁻¹⁹ × 2×10¹⁶ × 1200 = 3.84 S/cm
    (d) D_p = 0.0259 × 420 = 10.9 cm²/s
    (e) L_p = √(10.9 × 2×10⁻⁶) = 4.66×10⁻³ cm = 46.6 μm

**Answer:** **n = 2×10¹⁶, p = 5×10³ cm⁻³; E_F = E_i + 0.376 eV; σ = 3.84 S/cm; D_p = 10.9 cm²/s; L_p = 47 μm.**

#### Practice 15.2: a diode made from that sample

**Question.** A p⁺n diode (N_A = 1×10¹⁹ cm⁻³, area 1×10⁻³ cm²) is made on the silicon of Practice 15.1. Find V_bi, the zero-bias depletion width, I_s and the current at 0.65 V.

**Given:** N_A = 10¹⁹, N_D = 2×10¹⁶ cm⁻³, D_p = 10.9 cm²/s, L_p = 4.66×10⁻³ cm, A = 10⁻³ cm².

**Find:** V_bi, W, I_s, I(0.65 V).

**Solution.**

    V_bi = 0.0259 ln(10¹⁹ × 2×10¹⁶/10²⁰) = 0.0259 ln(2×10¹⁵) = 0.913 V
    W ≈ √(2ε_sV_bi/qN_D) = √(2 × 1.04×10⁻¹² × 0.913/(1.6×10⁻¹⁹ × 2×10¹⁶)) = 2.44×10⁻⁵ cm = 0.24 μm
    J_s ≈ qn_i²D_p/(L_pN_D) = 1.6×10⁻¹⁹ × 10²⁰ × 10.9/(4.66×10⁻³ × 2×10¹⁶) = 1.87×10⁻¹² A/cm²
    I_s = 1.87×10⁻¹⁵ A
    I(0.65 V) = 1.87×10⁻¹⁵ × e^{0.65/0.0259} = 1.87×10⁻¹⁵ × 7.9×10¹⁰ = 0.15 mA

**Answer:** **V_bi = 0.91 V, W = 0.24 μm, I_s = 1.9×10⁻¹⁵ A, I(0.65 V) = 0.15 mA.**

#### Practice 15.3: a complete MOSFET calculation

**Question.** An nMOS has N_A = 1×10¹⁷ cm⁻³, t_ox = 5 nm, V_FB = −0.9 V, μ_n = 350 cm²/V·s and W/L = 20. Find V_T and the saturation current at V_GS = 1.2 V.

**Given:** N_A = 10¹⁷ cm⁻³, t_ox = 5×10⁻⁷ cm, V_FB = −0.9 V, μ_n = 350 cm²/V·s, W/L = 20.

**Find:** V_T and I_D(sat).

**Solution.**

    C_ox = 3.45×10⁻¹³/5×10⁻⁷ = 6.9×10⁻⁷ F/cm²
    φ_F = 0.417 V,  2φ_F = 0.834 V
    γ = √(2qε_siN_A)/C_ox = 1.824×10⁻⁷/6.9×10⁻⁷ = 0.264 V^{1/2},  γ√(2φ_F) = 0.241 V
    V_T = −0.9 + 0.834 + 0.241 = 0.18 V
    k = μ_nC_ox(W/L) = 350 × 6.9×10⁻⁷ × 20 = 4.83 mA/V²
    I_D(sat) = ½ × 4.83 × (1.2 − 0.18)² = 2.5 mA

**Answer:** **V_T ≈ 0.18 V, I_D(sat) ≈ 2.5 mA.**

#### Practice 15.4: essay practice

**Question.** In about one page, explain how a p-n junction diode rectifies, starting from the formation of the depletion region and ending with the Shockley equation. (Use the structure of Week 10 and Q47–Q48.)

**Answer outline.** (1) Diffusion of holes and electrons across the junction uncovers fixed ions: the depletion region and its field. (2) Equilibrium: drift balances diffusion, E_F is flat, V_bi = (kT/q) ln(N_{A}N_D/n_i²). (3) Forward bias lowers the barrier; minority carriers are injected (law of the junction, p_n = p_n0e^{qV/kT}). (4) They diffuse and recombine over L_p, L_n; the diffusion currents at the depletion edges add to give I = I_s(e^{qV/kT} − 1). (5) Reverse bias raises the barrier: only the tiny −I_s flows. Hence rectification. Include the band diagram and the I-V sketch.

---

## Objectives check

Use this table to confirm you have met this week's objectives. Cover the Answer column and answer each check question from memory. If you cannot, go back to the section in the last column before moving on.

| # | Objective | Check yourself | Answer | Where it is taught |
|---|---|---|---|---|
| 1 | Summarise the whole course and how its ideas connect. | Trace the chain from doping to the diode equation in one sentence. | Doping sets n and p; a p-n junction forms a barrier; forward bias injects minority carriers that diffuse and recombine, giving I = I_s(e^{qV/kT} − 1). | 15.1 |
| 2 | Recall and apply the key formulas. | Write the mass-action law, the Einstein relation and the saturation MOSFET current. | np = n_i²; D/μ = kT/q; I_D = ½μC_ox(W/L)(V_GS − V_T)². | 15.2 |
| 3 | Answer definitions, derivations and calculations in examination style. | What should a derivation answer begin with? | A list of the assumptions. | 15.3 |
| 4 | Solve mixed past-question style problems. | Find V_bi for N_A = 10¹⁷ and N_D = 10¹⁵ cm⁻³ in Si. | 0.714 V. | 15.4, E6 |
| 5 | Check readiness for the final examination. | Can you tick every line of the checklist in 15.5? | If not, revise the week named on that line. | 15.5–15.6 |
