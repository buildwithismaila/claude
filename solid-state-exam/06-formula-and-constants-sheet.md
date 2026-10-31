# Formula and Constants Sheet
<!-- group: Revision tools -->

Every formula the 50 questions need, grouped by topic, with the question numbers that use it. Learn the boxed results of the derivations (Q27, Q37, Q48) by heart; the rest you should be able to rebuild from them. Every symbol is explained in the table that follows.

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
| Permittivity of free space | ε₀ | 8.854×10⁻¹⁴ F/cm |
| Electron-volt | 1 eV | 1.6×10⁻¹⁹ J |
| Photon wavelength | λ | 1.24/E μm, with E in eV |

## Material data at 300 K

| | Si | Ge | GaAs |
|---|---|---|---|
| Crystal structure | Diamond | Diamond | Zinc blende |
| Lattice constant a (Å) | 5.43 | 5.65 | 5.65 |
| Band gap E_g (eV) | 1.12, indirect | 0.66, indirect | 1.42, direct |
| n_i (cm⁻³) | 1×10¹⁰ | 2.4×10¹³ | 2×10⁶ |
| N_c (cm⁻³) | 2.8×10¹⁹ | 1.04×10¹⁹ | 4.7×10¹⁷ |
| N_v (cm⁻³) | 1.04×10¹⁹ | 6.0×10¹⁸ | 7.0×10¹⁸ |
| μ_n (cm²/V·s) | 1350 | 3900 | 8500 |
| μ_p (cm²/V·s) | 480 | 1900 | 400 |
| D_n, D_p (cm²/s) | 35, 12.4 | 101, 49 | 220, 10 |
| Relative permittivity ε_r | 11.7 | 16.0 | 12.9 |
| Electron affinity χ (eV) | 4.05 | 4.0 | 4.07 |
| Saturation velocity v_sat (cm/s) | 1×10⁷ | 6×10⁶ | about 1×10⁷ |
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
    High field: v_d → v_sat ≈ 1×10⁷ cm/s                                          (Q41)

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
    Ohmic by tunnelling:  N_D ≳ 10¹⁹ cm⁻³, so W = √(2ε_sV_bi/qN_D) is a few nm
    I-V:  I = I_s ( e^{qV/ηkT} − 1 );   η = (q/kT) dV/d(ln I)                        (Q50)
    C-V:  C = ε_sA/W;   1/C² = 2(V_bi − V)/(qε_sNA²);   N = 2/(qε_sA² |slope|);   V_bi = V-axis intercept

## Rules of thumb

- Each decade of doping moves E_F by 2.3kT ≈ 60 mV; each 60 mV of forward bias multiplies a diode's current by 10 (300 K).
- In silicon at room temperature, n_i roughly doubles for every 10 °C rise.
- 10¹⁶ cm⁻³ of dopant is 1 atom in 5×10⁶ silicon atoms (Si has 5×10²² atoms/cm³), yet it raises the conductivity nearly a million times (from 3×10⁻⁶ to 2.2 S/cm, n-type).
- Diffusion distances go as √(Dt): four times the time gives twice the depth.
