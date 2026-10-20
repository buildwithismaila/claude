# Answer Key — All 50 Examination Questions
<!-- group: Revision & Practicals -->

The key point of every PGD examination answer in one or two lines. Cover the right-hand column, say the answer aloud, then check. The full worked answer is in the week shown in brackets.

## Symbols and abbreviations used on this page

Every symbol, constant and abbreviation on this page is listed here, even if an earlier week already defined it, so you can study this page on its own.

**Constants and units**

| Symbol | Meaning | Units / typical value |
|---|---|---|
| q | Magnitude of the electronic charge | 1.6×10⁻¹⁹ C |
| k | Boltzmann constant | 8.617×10⁻⁵ eV/K = 1.381×10⁻²³ J/K |
| kT | Thermal energy | 0.0259 eV (often 0.02585 eV) at 300 K |
| kT/q | Thermal voltage | 0.0259 V (about 26 mV) at 300 K |
| T | Absolute temperature | kelvin (K); room temperature = 300 K |
| ħ | Reduced Planck constant, h/2π | 1.055×10⁻³⁴ J·s |
| eV | Electron-volt, a unit of energy | 1 eV = 1.6×10⁻¹⁹ J |
| μm | Micrometre (micron) | 1 μm = 10⁻⁴ cm = 10⁻⁶ m |

**Symbols**

| Symbol | Meaning | Units / typical value |
|---|---|---|
| E_c (E_C) | Energy of the bottom of the conduction band | eV |
| E_v (E_V) | Energy of the top of the valence band | eV |
| E_g | Band-gap energy, E_c − E_v | eV; Si 1.12, Ge 0.66, GaAs 1.42 at 300 K |
| E_F | Fermi level: the energy at which a state has a 50 % chance of being occupied | eV |
| E_i | Intrinsic Fermi level, close to mid-gap | eV |
| E_t | Energy level of a trap (recombination centre) in the gap | eV |
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
| α (Kronig–Penney) | √(2mE)/ħ, set by the electron energy | m⁻¹ |
| P (Kronig–Penney) | Barrier strength mV₀ba/ħ² | dimensionless |
| λ | Wavelength | μm or nm; λ(μm) = 1.24/E(eV) |
| (h k l), {h k l} | Miller indices of a plane; family of equivalent planes | integers |
| C_s | Surface concentration of a diffusion (or solid concentration when freezing) | cm⁻³ |
| C(x, t) | Dopant concentration at depth x and time t | cm⁻³ |
| D | Diffusion coefficient (dopants in a furnace, or carriers) | cm²/s |
| D₀ | Diffusion constant in D = D₀e^{−E_a/kT} | cm²/s |
| F | Particle flux in Fick's law | particles/(cm²·s) |
| Q | Dose: dopant atoms per unit area (in Weeks 13–14, Q also means charge) | atoms/cm² (C or C/cm² for charge) |
| erfc | Complementary error function, erfc(u) = 1 − erf(u); read from a table | dimensionless |
| R_p | Projected range: average depth at which implanted ions stop | μm |
| R_s | Sheet resistance (or diode series resistance in Week 12) | Ω/□ (ohms per square); Ω |
| μ, μ_n, μ_p | Mobility: drift velocity per unit field (electrons, holes) | cm²/(V·s); Si μ_n 1350, μ_p 480 |
| v_d | Drift velocity | cm/s |
| v_sat | Saturation velocity at high field | ≈ 10⁷ cm/s in Si |
| σ | Conductivity, q(nμ_n + pμ_p) (in Week 8, σ is also a capture cross-section) | S/cm (siemens per cm) |
| ρ | Resistivity, 1/σ | Ω·cm |
| J, J_n, J_p | Current density (total, electrons, holes) | A/cm² |
| D_n, D_p | Diffusion coefficients of electrons and holes | cm²/s; Si 35 and 12.4 |
| T_e | Electron temperature of hot carriers | K |
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
| W | Depletion-region width (in Week 13 W_B, W_E are base and emitter widths; in Week 14 W is channel width) | μm or cm |
| I_s, J_s (I_S) | Saturation current (density) of a diode or transistor | A; A/cm² |
| I | Current | A |
| η | Ideality factor of a diode, 1 (ideal) to 2 | dimensionless |
| C, C_j | Capacitance (junction or depletion capacitance) | F (pF = 10⁻¹² F) |
| Φ_m | Work function of a metal | eV; Al 4.28, Au 5.1 |
| Φ_s | Work function of a semiconductor, χ + (E_c − E_F) | eV |
| χ | Electron affinity: energy from E_c up to the vacuum level | eV; Si 4.05 |
| Φ_B | Schottky barrier height seen from the metal | eV (or V) |
| β | Common-emitter current gain, I_C/I_B (also h_FE) | dimensionless; 50–500 |
| V_T (V_th) | Threshold voltage of a MOSFET | V |
| v_dn, v_dp | Drift velocity of electrons and holes | cm/s |
| μ_i, τ_i (μ_L, μ_I, N_I) | Mobility and scattering time for one scattering mechanism (L: lattice, I: ionised impurity); N_I = ionised-impurity density | cm²/(V·s); s; cm⁻³ |
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
| InP | Indium phosphide |
| SiO₂ | Silicon dioxide (silica), the oxide insulator |
| CB | Conduction band |
| VB | Valence band |
| III–V | Compound of Group III and Group V elements (e.g. GaAs) |
| MG-Si | Metallurgical-grade silicon (≈ 98 % pure) |
| EG-Si | Electronic-grade silicon (99.9999999 % or better) |
| CZ | Czochralski crystal growth |
| FZ | Float-zone crystal growth |
| CVD | Chemical vapour deposition |
| VPE | Vapour-phase epitaxy |
| LPE | Liquid-phase epitaxy |
| MBE | Molecular-beam epitaxy |
| MOCVD | Metal-organic chemical vapour deposition |
| UHV | Ultra-high vacuum (≈ 10⁻¹⁰ Torr) |
| SRH | Shockley–Read–Hall (trap-assisted) recombination |
| LDD | Lightly doped drain |
| I-V | Current–voltage (measurement or characteristic) |
| C-V | Capacitance–voltage (measurement or characteristic) |
| HEMT | High-electron-mobility transistor |
| BJT | Bipolar junction transistor |
| HBT | Heterojunction bipolar transistor |
| IC | Integrated circuit |
| VLSI | Very-large-scale integration |
| LED | Light-emitting diode |
| RF | Radio frequency |
| PGD | Postgraduate Diploma |
| LHS | Left-hand side (of an equation) |
| IR | Infrared |


## Material physics and semiconductor growth (Q1–Q13)

| Q | Key answer |
|---|---|
| 1 (Week 1) | Conductivity between metal and insulator, controllable by doping, T, light. Metal: no gap, σ falls with T. Insulator: gap > 4 eV. Semiconductor: gap ≈ 1 eV, two carriers, σ rises with T. |
| 2 (Week 1) | Elemental: one element, Group IV, covalent, e.g. **Si, Ge**. Compound: two or more elements (III–V, II–VI), tunable and often direct gap, e.g. **GaAs, InP**. |
| 3 (Week 1) | Abundant and cheap; excellent native SiO₂; 1.12 eV gap gives low leakage to 150 °C; large perfect crystals; strong, good thermal conductor; well-understood doping. |
| 4 (Week 1) | Gaps 1.12 / 0.66 / 1.42 eV; indirect / indirect / direct; μ_n 1350 / 3900 / 8500. Si for ICs and power; Ge for IR and SiGe HBTs; GaAs for RF, LEDs, lasers. |
| 5 (Week 1) | Lattice = periodic array of points; crystal = lattice + basis. Structure sets bands and gap, mobility, anisotropy, doping sites, epitaxy, cleavage and defects. |
| 6 (Week 1) | Smallest integers proportional to reciprocals of intercepts. Steps: intercepts → reciprocals → clear fractions → (h k l). Infinite intercept → 0; negative → bar. |
| 7 (Week 1) | 2, 3, 1 → 1/2, 1/3, 1 → × 6 → **(3 2 6)**. In a cubic crystal d = a/7. |
| 8 (Week 1) | Covalent: shared pairs, directional. Ionic: electron transfer, Coulomb attraction. Metallic: electron sea. **Si is covalent**: four sp³ bonds, tetrahedral, 109.5°. |
| 9 (Week 2) | SiO₂ + 2C → MG-Si (98 %); Si + 3HCl → SiHCl₃ (300 °C); fractional distillation; Siemens CVD SiHCl₃ + H₂ → Si + 3HCl (1100 °C) → EG-Si (9N–11N) polysilicon; then CZ/FZ. |
| 10 (Week 2) | Seed dipped into melt at 1414 °C and slowly pulled (≈ 1 mm/min) with counter-rotation; melt freezes epitaxially on seed; Dash neck removes dislocations; shoulder, body, tail. |
| 11 (Week 2) | Advantages: large diameter, dislocation-free, controlled doping, low cost, oxygen strengthens and getters. Limitations: O and C contamination from crucible (limits resistivity), axial doping variation from segregation. |
| 12 (Week 2) | VPE: gas reacts on hot substrate (SiCl₄ + 2H₂ → Si + 4HCl). LPE: precipitation from cooling saturated melt. MBE: atomic beams in UHV with shutters, monolayer control. |
| 13 (Week 2) | Temperature VPE 1000–1250 °C > LPE 700–900 °C > MBE 500–650 °C. Precision MBE (atomic) > VPE > LPE. Uses: VPE production Si/MOCVD LEDs; LPE LEDs, thick layers; MBE quantum wells, HEMTs. |

## Impurity control and doping (Q14–Q21)

| Q | Key answer |
|---|---|
| 14 (Week 3) | Controlled addition of impurities (10¹⁴–10²⁰ cm⁻³). Needed because intrinsic σ is too low and T-sensitive; sets carrier type, makes junctions, sets V_bi, V_T, β, contacts. |
| 15 (Week 3) | n-type: Group V donors, electrons majority, E_F near E_c, n ≈ N_D. p-type: Group III acceptors, holes majority, E_F near E_v, p ≈ N_A. |
| 16 (Week 3) | Donor: one extra valence electron, gives it to CB, becomes +, level near E_c (P, As, Sb). Acceptor: one fewer, takes an electron creating a hole, becomes −, level near E_v (B, Al, Ga, In). |
| 17 (Week 3) | Thermally activated jumps down a gradient. Vacancy (substitutional, slow: B, P, As), interstitial (fast: Au, Cu, Fe), interstitialcy. D = D₀e^{−E_a/kT}. Predeposition + drive-in. |
| 18 (Week 3) | First law F = −D∂C/∂x (flux ∝ gradient). Second law ∂C/∂t = D∂²C/∂x² (from continuity), gives the profile's time evolution. |
| 19 (Week 3) | Constant source → C = 10²⁰ erfc(x/2√(Dt)) cm⁻³. Maximum (10²⁰) at the surface, falling monotonically with depth; penetrates as √t; dose Q = (2/√π)C_s√(Dt). |
| 20 (Week 3) | Ionised, mass-selected dopant ions accelerated (keV–MeV) into the wafer; Gaussian profile at R_p; anneal. Advantages: precise dose, independent depth, low temperature, resist masks, shallow and buried profiles. |
| 21 (Week 3) | Diffusion: high T, surface-peaked erfc/Gaussian, coupled dose/depth, no damage, cheap batch. Implant: room T, peak at R_p, ±1 % dose, damage needs anneal, channelling, costly, standard for VLSI. |

## Energy bands and carrier statistics (Q22–Q34)

| Q | Key answer |
|---|---|
| 22 (Week 4) | Wave nature; fixed nuclei (Born–Oppenheimer); perfect periodic potential; independent electrons in average potential; Bloch functions; Pauli principle; effective mass; Fermi–Dirac statistics. |
| 23 (Week 4) | −(ħ²/2m)d²ψ/dx² + Vψ = Eψ. Kinetic-energy term + potential-energy term = total energy E; \|ψ\|² is probability density; E eigenvalues give quantisation. |
| 24 (Week 4) | Periodic square wells and barriers; Bloch condition gives P sin(αa)/αa + cos αa = cos ka. Only energies with LHS between ±1 are allowed → bands and gaps; edges at k = nπ/a. |
| 25 (Week 4) | VB: highest full band at 0 K (bond electrons, holes). CB: lowest empty band (free electrons). Gap E_g = E_c − E_v: no states. |
| 26 (Week 4) | Direct: CB min and VB max at same k, photon only, efficient light (GaAs). Indirect: different k, phonon needed, poor emitter (Si, Ge). λ = 1.24/E_g μm. |
| 27 (Week 4) | Pure, n = p = n_i. n = N_ce^{−(E_c−E_F)/kT}, p = N_ve^{−(E_F−E_v)/kT}; multiply: **n_i = √(N_cN_v) e^{−E_g/2kT}** ∝ T^{3/2}e^{−E_g/2kT}. |
| 28 (Week 4) | Intrinsic: thermal only, n = p = n_i, strongly T-dependent. Extrinsic: from dopants, n ≠ p, n ≈ N_D or p ≈ N_A, nearly T-independent. Linked by np = n_i². |
| 29 (Week 4) | n = p and np = n_i² ⇒ **n = p = 1.0×10¹⁰ cm⁻³**. |
| 30 (Week 5) | f(E) = 1/(1 + e^{(E−E_F)/kT}): occupation probability of a state; ½ at E_F. Gives n and p, defines E_F, constant E_F in equilibrium sets junction physics. |
| 31 (Week 5) | At 0 K f is a step: 1 below E_F, 0 above. VB full, CB empty, pure semiconductor is an insulator. |
| 32 (Week 5) | g(E) = states per unit energy per unit volume, g_c ∝ (m_n∗)^{3/2}√(E − E_c). n = ∫g f dE; gives N_c, N_v; zero in gap. |
| 33 (Week 5) | n-type: E_F rises toward E_c, E_F − E_i = kT ln(N_D/n_i). p-type: falls toward E_v. 60 mV per decade; degenerate at very high doping; returns to E_i at high T. |
| 34 (Week 4) | n ≈ N_D = **5×10¹⁶ cm⁻³**. (p = 2×10³ cm⁻³; E_F − E_i = 0.40 eV in Si.) |

## Carrier transport and injection (Q35–Q46)

| Q | Key answer |
|---|---|
| 35 (Week 7) | μ = v_d/E = qτ/m∗. Depends on effective mass, temperature (lattice T^{−3/2}, impurity T^{3/2}), doping, field, defects, surfaces, orientation, strain. |
| 36 (Week 7) | Lattice (acoustic, optical, polar phonons), ionised impurity, neutral impurity, carrier–carrier, defects, surface roughness, alloy, intervalley. Matthiessen 1/μ = Σ1/μ_i. |
| 37 (Week 7) | v_dn = −μ_nE, v_dp = μ_pE; J = ρv: J_n = qnμ_nE, J_p = qpμ_pE; **J = q(nμ_n + pμ_p)E**, σ = q(nμ_n + pμ_p). |
| 38 (Week 7) | J = qnμE = 1.602×10⁻¹⁹ × 2×10¹⁶ × 1350 × 10 = **43.3 A/cm²**. |
| 39 (Week 7) | Current from carriers moving down a concentration gradient by random motion. Fick: F = −D dC/dx. J_n = qD_n dn/dx, J_p = −qD_p dp/dx. |
| 40 (Week 7) | **D/μ = kT/q** (0.0259 V). From zero equilibrium current in a non-uniform sample. Si: D_n = 35, D_p = 12.4 cm²/s. |
| 41 (Week 8) | High field: optical-phonon emission caps v_d at v_sat ≈ 10⁷ cm/s. Hot carriers (T_e ≫ T): impact ionisation, avalanche, oxide injection and V_T drift, substrate current; LDD as cure. |
| 42 (Week 8) | Generation creates e–h pairs (thermal, optical, impact); recombination annihilates them (radiative, SRH, Auger, surface). Equal in equilibrium; net U = Δp/τ. |
| 43 (Week 8) | Recombination via mid-gap trap: capture/emission of electrons and holes. U = (np − n_i²)/[τ_p(n + n₁) + τ_n(p + p₁)]; maximum for E_t ≈ E_i; τ = 1/σv_thN_t. |
| 44 (Week 8) | Average time an excess minority carrier survives: Δp(t) = Δp(0)e^{−t/τ}. Sets L = √(Dτ), diode leakage, switching speed, BJT gain, solar-cell efficiency. |
| 45 (Week 9) | ∂p/∂t = −(1/q)∂J_p/∂x + G − R; minority form ∂Δp/∂t = D∂²Δp/∂x² − Δp/τ + G. Used for diodes (exponential profile), BJTs, lifetime and Haynes–Shockley, solar cells. |
| 46 (Week 9) | S defined by U_s = SΔp_s (cm/s), S = σv_thN_st. Dangling-bond surface states are SRH centres: 1/τ_eff = 1/τ_b + 2S/W. Passivate with SiO₂, SiNₓ, Al₂O₃. |

## Junctions, interfaces and characterisation (Q47–Q50)

| Q | Key answer |
|---|---|
| 47 (Week 10) | Diffusion of carriers uncovers fixed ions → depletion region and field; drift balances diffusion; flat E_F. **V_bi = (kT/q) ln(N_{A}N_D/n_i²)**; W = √(2ε_sV_bi(N_A + N_D)/qN_{A}N_D). |
| 48 (Week 10) | Assumptions; law of junction p_n = p_n0e^{qV/kT}; diffusion equation → exponential decay over L_p; currents at edges; **I = I_s(e^{qV/kT} − 1)**, J_s = qn_i²(D_p/L_pN_D + D_n/L_nN_A). Forward: exponential rise; reverse: −I_s. |
| 49 (Week 11) | Schottky: Φ_m > Φ_s (n-type), upward bending, depletion, barrier Φ_B = Φ_m − χ, rectifying, thermionic, fast. Ohmic: Φ_m < Φ_s or heavy doping, accumulation or tunnelling, linear I-V. |
| 50 (Week 12) | I-V: ln I vs V gives I_s, η, R_s, breakdown, Φ_B. C-V: C = ε_sA/W; **1/C² = 2(V_bi − V)/(qε_sNA²)**; slope gives N = 2/(qε_sA²·slope), intercept gives V_bi; local slope gives profile N(W). |
