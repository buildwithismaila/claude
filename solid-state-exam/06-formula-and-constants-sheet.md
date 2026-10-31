# Formula and Constants Sheet
<!-- group: Revision tools -->

Every formula the 50 questions need, grouped by topic, with the question numbers that use it. Learn the boxed results of the derivations (Q27, Q37, Q48) by heart; the rest you should be able to rebuild from them. Every symbol is explained in the table that follows. All values are in SI units; energies are in electron-volts (eV), which SI accepts for use alongside its units.

## Symbols and abbreviations used on this page

Every symbol, constant and abbreviation on this page is listed here, even if another page already defined it, so you can study this page on its own.

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
| ε₀ | Permittivity of free space | 8.854×10⁻¹² F/m |
| ε_s (ε_si) | Permittivity of silicon, 11.7ε₀ | 1.04×10⁻¹⁰ F/m |
| ε_r | Relative permittivity (dielectric constant) | Si 11.7, SiO₂ 3.9, GaAs 12.9 |
| eV | Electron-volt, a unit of energy | 1 eV = 1.6×10⁻¹⁹ J |
| Å | Ångström, a unit of length | 1 Å = 10⁻¹⁰ m = 0.1 nm (not SI: this course uses nm) |
| μm | Micrometre (micron) | 1 μm = 10⁻⁶ m |

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
| g(E), g_c, g_v | Density of states: allowed states per unit energy per unit volume | states/(eV·m³) |
| N_c | Effective density of states in the conduction band | m⁻³; Si 2.8×10²⁵ at 300 K |
| N_v | Effective density of states in the valence band | m⁻³; Si 1.04×10²⁵ at 300 K |
| n | Electron concentration (free electrons per m³) | m⁻³ |
| p | Hole concentration (holes per m³) | m⁻³ |
| n_i | Intrinsic carrier concentration (n = p = n_i in pure material) | m⁻³; Si ≈ 1×10¹⁶ at 300 K |
| p_n0, n_p0 | Equilibrium minority concentrations: holes on the n side, electrons on the p side | m⁻³; p_n0 = n_i²/N_D |
| N_D | Donor concentration | m⁻³ |
| N_A | Acceptor concentration | m⁻³ |
| Δn, Δp | Excess electron and hole concentrations above equilibrium | m⁻³ |
| m∗, m_n∗, m_p∗ | Effective mass of electrons or holes | kg, or as a multiple of m₀ |
| ψ | Wave function (\|ψ\|² is the probability density) | — |
| V(x) | Potential energy in the Schrödinger equation | J or eV |
| k (wave vector) | Wave vector, 2π/λ; measures the electron's momentum, p = ħk | m⁻¹ |
| α (Kronig–Penney) | √(2mE)/ħ, set by the electron energy | m⁻¹ |
| P (Kronig–Penney) | Barrier strength mV₀ba/ħ² | dimensionless |
| λ | Wavelength | μm or nm; λ(μm) = 1.24/E(eV) |
| a | Lattice constant: edge length of the cubic unit cell | nm; Si 0.543, Ge and GaAs 0.565 |
| (h k l), {h k l} | Miller indices of a plane; family of equivalent planes | integers |
| d_hkl | Spacing between neighbouring (h k l) planes, a/√(h² + k² + l²) | nm |
| k₀ | Segregation coefficient, C_s/C_l at the freezing interface | dimensionless; B 0.8, P 0.35 |
| C_s | Surface concentration of a diffusion (or solid concentration when freezing) | m⁻³ |
| C_l, C₀ | Concentration in the melt (liquid); C₀ at the start | m⁻³ |
| C(x, t) | Dopant concentration at depth x and time t | m⁻³ |
| D | Diffusion coefficient (dopants in a furnace, or carriers) | m²/s |
| D₀ | Diffusion constant in D = D₀e^{−E_a/kT} | m²/s |
| F | Particle flux in Fick's law | particles/(m²·s) |
| Q | Dose: dopant atoms per unit area (in Weeks 13–14, Q also means charge) | atoms/m² (C or C/m² for charge) |
| Φ (dose) | Implanted dose (ions per m²) | m⁻² |
| erfc | Complementary error function, erfc(u) = 1 − erf(u); read from a table | dimensionless |
| x_j | Junction depth: where the dopant concentration equals the background | μm |
| N_B (C_B) | Background doping of the wafer (in Week 13, N_B is the base doping) | m⁻³ |
| R_p | Projected range: average depth at which implanted ions stop | μm |
| ΔR_p | Straggle: spread of the implanted ions' stopping depths | μm |
| E (field) | Electric field (on band diagrams, E is energy instead) | V/m |
| μ, μ_n, μ_p | Mobility: drift velocity per unit field (electrons, holes) | m²/(V·s); Si μ_n 0.135, μ_p 0.048 |
| μ_L, μ_I | Mobility limited by lattice scattering, by ionised-impurity scattering | m²/(V·s) |
| v_d | Drift velocity | m/s |
| v_sat | Saturation velocity at high field | ≈ 10⁵ m/s in Si |
| τ_m | Mean free time between collisions | s; about 0.1–1 ps |
| σ | Conductivity, q(nμ_n + pμ_p) (in Week 8, σ is also a capture cross-section) | S/m (siemens per metre) |
| ρ | Resistivity, 1/σ | Ω·m |
| J, J_n, J_p | Current density (total, electrons, holes) | A/m² |
| D_n, D_p | Diffusion coefficients of electrons and holes | m²/s; Si 3.5×10⁻³ and 1.24×10⁻³ |
| G, G_L | Generation rate of electron–hole pairs (G_L: by light) | m⁻³s⁻¹ |
| R | Recombination rate | m⁻³s⁻¹ |
| U | Net recombination rate, R − G | m⁻³s⁻¹ |
| τ, τ_n, τ_p | Minority-carrier lifetime (τ_eff: effective, including surfaces) | s; Si 1 ns – 1 ms |
| N_t | Density of traps (recombination centres) | m⁻³ |
| n₁, p₁ | SRH parameters n_ie^{(E_t − E_i)/kT} and n_ie^{(E_i − E_t)/kT} | m⁻³ |
| L, L_n, L_p | Diffusion length √(Dτ): distance a minority carrier travels before recombining | μm or m |
| S | Surface recombination velocity | m/s |
| N_st | Density of surface traps | m⁻² |
| U_s | Recombination rate per unit area at a surface | m⁻²s⁻¹ |
| V_bi | Built-in potential of a junction or Schottky contact | V; typically 0.5–1 V |
| W | Depletion-region width (in Week 13 W_B, W_E are base and emitter widths; in Week 14 W is channel width) | μm or m |
| x_n, x_p | Parts of the depletion region on the n side and on the p side | μm |
| E_max | Peak electric field, at the junction | V/m |
| I_s, J_s (I_S) | Saturation current (density) of a diode or transistor | A; A/m² |
| I | Current | A |
| η | Ideality factor of a diode, 1 (ideal) to 2 | dimensionless |
| C, C_j | Capacitance (junction or depletion capacitance) | F (pF = 10⁻¹² F) |
| Φ_m | Work function of a metal | eV; Al 4.28, Au 5.1 |
| Φ_s | Work function of a semiconductor, χ + (E_c − E_F) | eV |
| χ | Electron affinity: energy from E_c up to the vacuum level | eV; Si 4.05 |
| Φ_B | Schottky barrier height seen from the metal | eV (or V) |
| A∗∗ | Effective Richardson constant | A/(m²·K²); n-Si ≈ 1.1×10⁶ |
| μ_i, τ_i (μ_L, μ_I, N_I) | Mobility and scattering time for one scattering mechanism (L: lattice, I: ionised impurity); N_I = ionised-impurity density | m²/(V·s); s; m⁻³ |
| G_n, G_p, R_n, R_p | Generation and recombination rates of electrons and holes | m⁻³s⁻¹ |
| τ_b (τ_bulk), τ_surface | Lifetime from bulk recombination only; from surface recombination only | s |
| U_s, p_s, Δp_s | Surface recombination rate; hole density and excess at the surface | m⁻²s⁻¹; m⁻³ |
| n_n0, p_p0, p_n0, n_p0 | Equilibrium densities: majority (n_n0, p_p0) and minority (p_n0 holes on n side, n_p0 electrons on p side) | m⁻³ |
| p_n, n_p | Minority-carrier density: holes on the n side, electrons on the p side | m⁻³ |
| erfc(u), erfc⁻¹ | Complementary error function, 1 − erf(u), and its inverse (read from a table) | dimensionless |
| N(x), N(W) | Doping concentration at depth x (or at the depletion edge W), from C-V profiling | m⁻³ |

**Abbreviations**

| Abbreviation | Meaning |
|---|---|
| Si | Silicon |
| Ge | Germanium |
| GaAs | Gallium arsenide |
| SiO₂ | Silicon dioxide (silica), the oxide insulator |
| MG-Si | Metallurgical-grade silicon (≈ 98 % pure) |
| EG-Si | Electronic-grade silicon (99.9999999 % or better) |
| CZ | Czochralski crystal growth |
| CVD | Chemical vapour deposition |
| VPE | Vapour-phase epitaxy |
| SRH | Shockley–Read–Hall (trap-assisted) recombination |
| I-V | Current–voltage (measurement or characteristic) |
| C-V | Capacitance–voltage (measurement or characteristic) |


## Physical constants

| Quantity | Symbol | Value |
|---|---|---|
| Electronic charge | q | 1.6×10⁻¹⁹ C |
| Boltzmann constant | k | 8.617×10⁻⁵ eV/K = 1.381×10⁻²³ J/K |
| Thermal energy at 300 K | kT | 0.0259 eV |
| Thermal voltage at 300 K | kT/q | 0.0259 V (about 26 mV) |
| Planck constant | h | 6.626×10⁻³⁴ J·s |
| Reduced Planck constant | ħ = h/2π | 1.055×10⁻³⁴ J·s |
| Free-electron mass | m₀ | 9.11×10⁻³¹ kg |
| Permittivity of free space | ε₀ | 8.854×10⁻¹² F/m |
| Electron-volt | 1 eV | 1.6×10⁻¹⁹ J |
| Photon wavelength | λ | 1.24/E μm (1.24×10⁻⁶/E m), with E in eV |
| Speed of light | c | 3×10⁸ m/s |

## Material data at 300 K

| | Si | Ge | GaAs |
|---|---|---|---|
| Crystal structure | Diamond | Diamond | Zinc blende |
| Lattice constant a (nm) | 0.543 | 0.565 | 0.565 |
| Band gap E_g (eV) | 1.12, indirect | 0.66, indirect | 1.42, direct |
| n_i (m⁻³) | 1×10¹⁶ | 2.4×10¹⁹ | 2×10¹² |
| N_c (m⁻³) | 2.8×10²⁵ | 1.04×10²⁵ | 4.7×10²³ |
| N_v (m⁻³) | 1.04×10²⁵ | 6.0×10²⁴ | 7.0×10²⁴ |
| μ_n (m²/V·s) | 0.135 | 0.39 | 0.85 |
| μ_p (m²/V·s) | 0.048 | 0.19 | 0.04 |
| D_n, D_p (m²/s) | 3.5×10⁻³, 1.24×10⁻³ | 1.01×10⁻², 4.9×10⁻³ | 2.2×10⁻², 1.0×10⁻³ |
| Relative permittivity ε_r | 11.7 | 16.0 | 12.9 |
| Permittivity ε_s = ε_rε₀ (F/m) | 1.04×10⁻¹⁰ | 1.42×10⁻¹⁰ | 1.14×10⁻¹⁰ |
| Atom density (m⁻³) | 5.0×10²⁸ | 4.4×10²⁸ | 4.4×10²⁸ |
| Electron affinity χ (eV) | 4.05 | 4.0 | 4.07 |
| Saturation velocity v_sat (m/s) | 1×10⁵ | 6×10⁴ | about 1×10⁵ |
| Melting point (°C) | 1414 | 937 | 1238 |

## Crystals (Q5–Q8)

    Miller indices: intercepts → reciprocals → clear fractions → (h k l)        (Q6, Q7)
    d_hkl = a / √(h² + k² + l²)                    spacing of (h k l) planes, cubic crystal
    Diamond lattice: 8 atoms per cell, 4 nearest neighbours, bond angle 109.5°  (Q8)

## Growth (Q9–Q13)

    SiO₂ + 2C → Si + 2CO                   (MG-Si, about 98 % pure, arc furnace)       (Q9)
    Si + 3HCl → SiHCl₃ + H₂                (trichlorosilane, about 300 °C)
    SiHCl₃ + H₂ → Si + 3HCl                (Siemens CVD, about 1100 °C → EG-Si)
    k₀ = C_s/C_l;    C_s = k₀C₀(1 − f)^{k₀ − 1}        (CZ segregation)              (Q10, Q11)
    SiCl₄ + 2H₂ → Si + 4HCl                (VPE of silicon)                            (Q12)

## Doping and diffusion (Q14–Q21)

    n ≈ N_D (n-type),   p ≈ N_A (p-type),   complete ionisation               (Q15, Q34)
    Fick's first law:   F = −D ∂C/∂x                                             (Q18, Q39)
    Fick's second law:  ∂C/∂t = D ∂²C/∂x²                                        (Q18)
    D = D₀ e^{−E_a/kT}                                                           (Q17)
    Constant source:    C(x, t) = C_s erfc( x / 2√(Dt) ),   Q = 2C_s√(Dt/π)         (Q19)
    Limited source:     C(x, t) = ( Q/√(πDt) ) e^{−x²/4Dt}
    Junction depth:     C(x_j) = N_B
    Implant:            N(x) = ( Φ/(√(2π)ΔR_p) ) e^{−(x − R_p)²/2ΔR_p²},   Φ = It/qA    (Q20)

## Bands and carrier statistics (Q22–Q34)

    Schrödinger:   −(ħ²/2m) d²ψ/dx² + V(x)ψ = Eψ                                (Q23)
    Kronig–Penney: P sin(αa)/(αa) + cos(αa) = cos(ka)                            (Q24)
    E_g = E_c − E_v;    λ = 1.24/E_g μm                                          (Q25, Q26)
    Fermi–Dirac:   f(E) = 1 / (1 + e^{(E − E_F)/kT})                             (Q30, Q31)
    g_c(E) = ( 4π(2m_n∗)^{3/2}/h³ ) √(E − E_c)                                   (Q32)
    n = N_c e^{−(E_c − E_F)/kT},     p = N_v e^{−(E_F − E_v)/kT}                 (Q27)
    n_i = √(N_cN_v) e^{−E_g/2kT}     (boxed result of Q27)
    np = n_i²                         (mass-action law)                          (Q28, Q29, Q34)
    E_F − E_i = kT ln(N_D/n_i)   (n-type);    E_i − E_F = kT ln(N_A/n_i)   (p-type)    (Q33, Q34)
    E_c − E_F = kT ln(N_c/N_D)

## Transport (Q35–Q41)

    v_d = μE;    μ = qτ_m/m∗;    1/μ = 1/μ_L + 1/μ_I   (Matthiessen)              (Q35, Q36)
    J = q(nμ_n + pμ_p)E;    σ = q(nμ_n + pμ_p);    ρ = 1/σ   (boxed result of Q37)   (Q37, Q38)
    J_n = qnμ_nE + qD_n dn/dx;    J_p = qpμ_pE − qD_p dp/dx                       (Q39)
    Einstein:  D/μ = kT/q                                                         (Q40)
    High field: v_d → v_sat ≈ 1×10⁵ m/s                                           (Q41)

## Recombination and continuity (Q42–Q46)

    SRH:   U = (np − n_i²) / [ τ_p(n + n₁) + τ_n(p + p₁) ],    τ = 1/(σv_thN_t)       (Q43)
    Low-level, n-type:  U = Δp/τ_p;    Δp(t) = Δp(0) e^{−t/τ_p}                     (Q42, Q44)
    Continuity:  ∂Δp/∂t = D_p ∂²Δp/∂x² − μ_pE ∂Δp/∂x + G_L − Δp/τ_p                (Q45)
    Steady state, no field:  Δp(x) = Δp(0) e^{−x/L_p},   L_p = √(D_pτ_p)
    Surface:  U_s = SΔp_s,   S = σv_thN_st                                         (Q46)
    1/τ_eff = 1/τ_b + 2S/W   (valid when SW/2D ≪ 1);   for large S, τ_surface ≈ W/2S + W²/(π²D)

## Junctions, contacts and characterisation (Q47–Q50)

    V_bi = (kT/q) ln( N_{A}N_D / n_i² )                                            (Q47)
    W = √( (2ε_s/q)(V_bi − V)(1/N_A + 1/N_D) );    N_{A}x_p = N_{D}x_n;   E_max = qN_{D}x_n/ε_s
    Law of the junction:  p_n(x_n) = p_n0 e^{qV/kT}                                 (Q48)
    I = I_s ( e^{qV/kT} − 1 ),    J_s = qn_i²( D_p/(L_pN_D) + D_n/(L_nN_A) )   (boxed result of Q48)
    Schottky:  Φ_B = Φ_m − χ;   V_bi = Φ_m − Φ_s;   J_s = A∗∗T² e^{−qΦ_B/kT}         (Q49)
    Ohmic by tunnelling:  N_D ≳ 10²⁵ m⁻³, so W = √(2ε_sV_bi/qN_D) is a few nm
    I-V:  I = I_s ( e^{qV/ηkT} − 1 );   η = (q/kT) dV/d(ln I)                        (Q50)
    C-V:  C = ε_sA/W;   1/C² = 2(V_bi − V)/(qε_sNA²);   N = 2/(qε_sA² |slope|);   V_bi = V-axis intercept

## Rules of thumb

- Each decade of doping moves E_F by 2.3kT ≈ 60 mV; each 60 mV of forward bias multiplies a diode's current by 10 (300 K).
- In silicon at room temperature, n_i roughly doubles for every 10 °C rise.
- 10²² m⁻³ of dopant is 1 atom in 5×10⁶ silicon atoms (Si has 5×10²⁸ atoms/m³), yet it raises the conductivity nearly a million times (from 2.9×10⁻⁴ to 216 S/m, n-type).
- Diffusion distances go as √(Dt): four times the time gives twice the depth.

## Converting from centimetre units

Textbooks, your lecturer's notes and some exam questions use centimetres. Convert to SI before you substitute:

| Quantity | cm-based unit | SI unit | Multiply by | Example |
|---|---|---|---|---|
| Length | cm | m | 10⁻² | 0.33 μm = 3.3×10⁻⁵ cm = 3.3×10⁻⁷ m |
| Concentration | cm⁻³ | m⁻³ | 10⁶ | 1×10¹⁶ cm⁻³ = 1×10²² m⁻³ |
| Dose, surface density | cm⁻² | m⁻² | 10⁴ | 1×10¹⁵ cm⁻² = 1×10¹⁹ m⁻² |
| Area | cm² | m² | 10⁻⁴ | 1×10⁻³ cm² = 1×10⁻⁷ m² |
| Mobility | cm²/V·s | m²/V·s | 10⁻⁴ | 1350 cm²/V·s = 0.135 m²/V·s |
| Diffusion coefficient | cm²/s | m²/s | 10⁻⁴ | 35 cm²/s = 3.5×10⁻³ m²/s |
| Velocity | cm/s | m/s | 10⁻² | 10⁷ cm/s = 10⁵ m/s |
| Electric field | V/cm | V/m | 10² | 10 V/cm = 1000 V/m |
| Current density | A/cm² | A/m² | 10⁴ | 43.2 A/cm² = 4.32×10⁵ A/m² |
| Permittivity | F/cm | F/m | 10² | 1.04×10⁻¹² F/cm = 1.04×10⁻¹⁰ F/m |
| Conductivity | S/cm | S/m | 10² | 2.16 S/cm = 216 S/m |
| Resistivity | Ω·cm | Ω·m | 10⁻² | 1 Ω·cm = 0.01 Ω·m |
| Capacitance per area | F/cm² | F/m² | 10⁴ | 3.45×10⁻⁷ F/cm² = 3.45×10⁻³ F/m² |
| Lattice spacing | Å | nm | 10⁻¹ | 5.43 Å = 0.543 nm |

A quick check: a concentration in m⁻³ is always a million times the number in cm⁻³ (n_i of silicon is 1×10¹⁰ cm⁻³ = 1×10¹⁶ m⁻³).
