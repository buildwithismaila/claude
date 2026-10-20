# Module 19 — Rapid-Revision Answer Key (Q1–Q50)

The key point of every answer in one or two lines, for testing yourself the night before. Cover the right-hand column, say the answer aloud, then check. Full answers are in the module named in the first column.

## Material physics and semiconductor growth (Q1–Q13)

| Q | Key answer |
|---|---|
| 1 (M01) | Conductivity between metal and insulator, controllable by doping, T, light. Metal: no gap, σ falls with T. Insulator: gap > 4 eV. Semiconductor: gap ≈ 1 eV, two carriers, σ rises with T. |
| 2 (M01) | Elemental: one element, Group IV, covalent, e.g. **Si, Ge**. Compound: two or more elements (III–V, II–VI), tunable and often direct gap, e.g. **GaAs, InP**. |
| 3 (M01) | Abundant and cheap; excellent native SiO₂; 1.12 eV gap gives low leakage to 150 °C; large perfect crystals; strong, good thermal conductor; well-understood doping. |
| 4 (M01) | Gaps 1.12 / 0.66 / 1.42 eV; indirect / indirect / direct; μ_n 1350 / 3900 / 8500. Si for ICs and power; Ge for IR and SiGe HBTs; GaAs for RF, LEDs, lasers. |
| 5 (M02) | Lattice = periodic array of points; crystal = lattice + basis. Structure sets bands and gap, mobility, anisotropy, doping sites, epitaxy, cleavage and defects. |
| 6 (M02) | Smallest integers proportional to reciprocals of intercepts. Steps: intercepts → reciprocals → clear fractions → (h k l). Infinite intercept → 0; negative → bar. |
| 7 (M02) | 2, 3, 1 → 1/2, 1/3, 1 → × 6 → **(3 2 6)**. In a cubic crystal d = a/7. |
| 8 (M03) | Covalent: shared pairs, directional. Ionic: electron transfer, Coulomb attraction. Metallic: electron sea. **Si is covalent**: four sp³ bonds, tetrahedral, 109.5°. |
| 9 (M04) | SiO₂ + 2C → MG-Si (98 %); Si + 3HCl → SiHCl₃ (300 °C); fractional distillation; Siemens CVD SiHCl₃ + H₂ → Si + 3HCl (1100 °C) → EG-Si (9N–11N) polysilicon; then CZ/FZ. |
| 10 (M04) | Seed dipped into melt at 1414 °C and slowly pulled (≈ 1 mm/min) with counter-rotation; melt freezes epitaxially on seed; Dash neck removes dislocations; shoulder, body, tail. |
| 11 (M04) | Advantages: large diameter, dislocation-free, controlled doping, low cost, oxygen strengthens and getters. Limitations: O and C contamination from crucible (limits resistivity), axial doping variation from segregation. |
| 12 (M05) | VPE: gas reacts on hot substrate (SiCl₄ + 2H₂ → Si + 4HCl). LPE: precipitation from cooling saturated melt. MBE: atomic beams in UHV with shutters, monolayer control. |
| 13 (M05) | Temperature VPE 1000–1250 °C > LPE 700–900 °C > MBE 500–650 °C. Precision MBE (atomic) > VPE > LPE. Uses: VPE production Si/MOCVD LEDs; LPE LEDs, thick layers; MBE quantum wells, HEMTs. |

## Impurity control and doping (Q14–Q21)

| Q | Key answer |
|---|---|
| 14 (M06) | Controlled addition of impurities (10¹⁴–10²⁰ cm⁻³). Needed because intrinsic σ is too low and T-sensitive; sets carrier type, makes junctions, sets V_bi, V_T, β, contacts. |
| 15 (M06) | n-type: Group V donors, electrons majority, E_F near E_c, n ≈ N_D. p-type: Group III acceptors, holes majority, E_F near E_v, p ≈ N_A. |
| 16 (M06) | Donor: one extra valence electron, gives it to CB, becomes +, level near E_c (P, As, Sb). Acceptor: one fewer, takes an electron creating a hole, becomes −, level near E_v (B, Al, Ga, In). |
| 17 (M06) | Thermally activated jumps down a gradient. Vacancy (substitutional, slow: B, P, As), interstitial (fast: Au, Cu, Fe), interstitialcy. D = D₀e^{−E_a/kT}. Predeposition + drive-in. |
| 18 (M06) | First law F = −D∂C/∂x (flux ∝ gradient). Second law ∂C/∂t = D∂²C/∂x² (from continuity), gives the profile's time evolution. |
| 19 (M06) | Constant source → C = 10²⁰ erfc(x/2√(Dt)) cm⁻³. Maximum (10²⁰) at the surface, falling monotonically with depth; penetrates as √t; dose Q = (2/√π)C_s√(Dt). |
| 20 (M07) | Ionised, mass-selected dopant ions accelerated (keV–MeV) into the wafer; Gaussian profile at R_p; anneal. Advantages: precise dose, independent depth, low temperature, resist masks, shallow and buried profiles. |
| 21 (M07) | Diffusion: high T, surface-peaked erfc/Gaussian, coupled dose/depth, no damage, cheap batch. Implant: room T, peak at R_p, ±1 % dose, damage needs anneal, channelling, costly, standard for VLSI. |

## Energy bands and carrier statistics (Q22–Q34)

| Q | Key answer |
|---|---|
| 22 (M08) | Wave nature; fixed nuclei (Born–Oppenheimer); perfect periodic potential; independent electrons in average potential; Bloch functions; Pauli principle; effective mass; Fermi–Dirac statistics. |
| 23 (M08) | −(ħ²/2m)d²ψ/dx² + Vψ = Eψ. Kinetic-energy term + potential-energy term = total energy E; \|ψ\|² is probability density; E eigenvalues give quantisation. |
| 24 (M08) | Periodic square wells and barriers; Bloch condition gives P sin(αa)/αa + cos αa = cos ka. Only energies with LHS between ±1 are allowed → bands and gaps; edges at k = nπ/a. |
| 25 (M08) | VB: highest full band at 0 K (bond electrons, holes). CB: lowest empty band (free electrons). Gap E_g = E_c − E_v: no states. |
| 26 (M08) | Direct: CB min and VB max at same k, photon only, efficient light (GaAs). Indirect: different k, phonon needed, poor emitter (Si, Ge). λ = 1.24/E_g μm. |
| 27 (M09) | Pure, n = p = n_i. n = N_ce^{−(E_c−E_F)/kT}, p = N_ve^{−(E_F−E_v)/kT}; multiply: **n_i = √(N_cN_v) e^{−E_g/2kT}** ∝ T^{3/2}e^{−E_g/2kT}. |
| 28 (M09) | Intrinsic: thermal only, n = p = n_i, strongly T-dependent. Extrinsic: from dopants, n ≠ p, n ≈ N_D or p ≈ N_A, nearly T-independent. Linked by np = n_i². |
| 29 (M09) | n = p and np = n_i² ⇒ **n = p = 1.0×10¹⁰ cm⁻³**. |
| 30 (M09) | f(E) = 1/(1 + e^{(E−E_F)/kT}): occupation probability of a state; ½ at E_F. Gives n and p, defines E_F, constant E_F in equilibrium sets junction physics. |
| 31 (M09) | At 0 K f is a step: 1 below E_F, 0 above. VB full, CB empty, pure semiconductor is an insulator. |
| 32 (M09) | g(E) = states per unit energy per unit volume, g_c ∝ (m_n∗)^{3/2}√(E − E_c). n = ∫g f dE; gives N_c, N_v; zero in gap. |
| 33 (M09) | n-type: E_F rises toward E_c, E_F − E_i = kT ln(N_D/n_i). p-type: falls toward E_v. 60 mV per decade; degenerate at very high doping; returns to E_i at high T. |
| 34 (M09) | n ≈ N_D = **5×10¹⁶ cm⁻³**. (p = 2×10³ cm⁻³; E_F − E_i = 0.40 eV in Si.) |

## Carrier transport and injection (Q35–Q46)

| Q | Key answer |
|---|---|
| 35 (M10) | μ = v_d/E = qτ/m∗. Depends on effective mass, temperature (lattice T^{−3/2}, impurity T^{3/2}), doping, field, defects, surfaces, orientation, strain. |
| 36 (M10) | Lattice (acoustic, optical, polar phonons), ionised impurity, neutral impurity, carrier–carrier, defects, surface roughness, alloy, intervalley. Matthiessen 1/μ = Σ1/μ_i. |
| 37 (M10) | v_dn = −μ_nE, v_dp = μ_pE; J = ρv: J_n = qnμ_nE, J_p = qpμ_pE; **J = q(nμ_n + pμ_p)E**, σ = q(nμ_n + pμ_p). |
| 38 (M10) | J = qnμE = 1.602×10⁻¹⁹ × 2×10¹⁶ × 1350 × 10 = **43.3 A/cm²**. |
| 39 (M11) | Current from carriers moving down a concentration gradient by random motion. Fick: F = −D dC/dx. J_n = qD_n dn/dx, J_p = −qD_p dp/dx. |
| 40 (M11) | **D/μ = kT/q** (0.0259 V). From zero equilibrium current in a non-uniform sample. Si: D_n = 35, D_p = 12.4 cm²/s. |
| 41 (M10) | High field: optical-phonon emission caps v_d at v_sat ≈ 10⁷ cm/s. Hot carriers (T_e ≫ T): impact ionisation, avalanche, oxide injection and V_T drift, substrate current; LDD as cure. |
| 42 (M12) | Generation creates e–h pairs (thermal, optical, impact); recombination annihilates them (radiative, SRH, Auger, surface). Equal in equilibrium; net U = Δp/τ. |
| 43 (M12) | Recombination via mid-gap trap: capture/emission of electrons and holes. U = (np − n_i²)/[τ_p(n + n₁) + τ_n(p + p₁)]; maximum for E_t ≈ E_i; τ = 1/σv_thN_t. |
| 44 (M12) | Average time an excess minority carrier survives: Δp(t) = Δp(0)e^{−t/τ}. Sets L = √(Dτ), diode leakage, switching speed, BJT gain, solar-cell efficiency. |
| 45 (M13) | ∂p/∂t = −(1/q)∂J_p/∂x + G − R; minority form ∂Δp/∂t = D∂²Δp/∂x² − Δp/τ + G. Used for diodes (exponential profile), BJTs, lifetime and Haynes–Shockley, solar cells. |
| 46 (M13) | S defined by U_s = SΔp_s (cm/s), S = σv_thN_st. Dangling-bond surface states are SRH centres: 1/τ_eff = 1/τ_b + 2S/W. Passivate with SiO₂, SiNₓ, Al₂O₃. |

## Junctions, interfaces and characterisation (Q47–Q50)

| Q | Key answer |
|---|---|
| 47 (M14) | Diffusion of carriers uncovers fixed ions → depletion region and field; drift balances diffusion; flat E_F. **V_bi = (kT/q) ln(N_AN_D/n_i²)**; W = √(2ε_sV_bi(N_A + N_D)/qN_AN_D). |
| 48 (M14) | Assumptions; law of junction p_n = p_n0e^{qV/kT}; diffusion equation → exponential decay over L_p; currents at edges; **I = I_s(e^{qV/kT} − 1)**, J_s = qn_i²(D_p/L_pN_D + D_n/L_nN_A). Forward: exponential rise; reverse: −I_s. |
| 49 (M15) | Schottky: Φ_m > Φ_s (n-type), upward bending, depletion, barrier Φ_B = Φ_m − χ, rectifying, thermionic, fast. Ohmic: Φ_m < Φ_s or heavy doping, accumulation or tunnelling, linear I-V. |
| 50 (M16) | I-V: ln I vs V gives I_s, η, R_s, breakdown, Φ_B. C-V: C = ε_sA/W; **1/C² = 2(V_bi − V)/(qε_sNA²)**; slope gives N = 2/(qε_sA²·slope), intercept gives V_bi; local slope gives profile N(W). |
