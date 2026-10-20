# Module 18 — Formula Sheet and Constants

## Physical constants

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

## Material data at 300 K

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

## Crystals and Miller indices

    Miller indices: intercepts → reciprocals → clear fractions → (h k l)
    d_{hkl} = a / √(h² + k² + l²)      (cubic)
    Diamond: 8 atoms/cell, coordination 4, r_nn = (√3/4)a, APF = 0.34
    SC 1, BCC 2, FCC 4 atoms/cell;  APF 0.52, 0.68, 0.74

## Growth and doping

    SiO₂ + 2C → Si + 2CO;   Si + 3HCl → SiHCl₃ + H₂;   SiHCl₃ + H₂ → Si + 3HCl
    Segregation: k₀ = C_s/C_l;   C_s = k₀C₀(1 − f)^{k₀ − 1}
    Fick 1: F = −D ∂C/∂x;   Fick 2: ∂C/∂t = D ∂²C/∂x²;   D = D₀ e^{−E_a/kT}
    Constant source: C = C_s erfc(x/2√(Dt));   Q = (2/√π)C_s√(Dt)
    Limited source: C = (Q/√(πDt)) exp(−x²/4Dt)
    Implant: N(x) = (Φ/√(2π)ΔR_p) exp(−(x − R_p)²/2ΔR_p²);   N_p ≈ 0.4Φ/ΔR_p;   Φ = It/qA

## Bands and statistics

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

## Transport

    v_d = μE;   μ = qτ_m/m∗;   1/μ = 1/μ_L + 1/μ_I
    J_drift = q(nμ_n + pμ_p)E;   σ = q(nμ_n + pμ_p);   ρ = 1/σ
    J_n = qnμ_nE + qD_n dn/dx;   J_p = qpμ_pE − qD_p dp/dx
    Einstein: D/μ = kT/q
    v_d = μE/[1 + (μE/v_sat)^β]^{1/β}

## Recombination and continuity

    SRH: U = (np − n_i²)/[τ_p(n + n₁) + τ_n(p + p₁)];   τ = 1/(σv_thN_t)
    Low-level, n-type: U = Δp/τ_p;   Δp(t) = Δp(0)e^{−t/τ_p}
    ∂Δp/∂t = D_p ∂²Δp/∂x² − μ_pE ∂Δp/∂x + G_L − Δp/τ_p
    L = √(Dτ);   Δp(x) = Δp(0)e^{−x/L_p}
    Surface: U_s = SΔp_s;   S = σv_thN_st;   1/τ_eff = 1/τ_b + 2S/W

## Junctions and contacts

    V_bi = (kT/q) ln(N_AN_D/n_i²)
    W = √((2ε_s/q)(V_bi − V)(1/N_A + 1/N_D));   N_Ax_p = N_Dx_n;   E_max = qN_Dx_n/ε_s
    I = I_s(e^{qV/kT} − 1);   J_s = qn_i²(D_p/(L_pN_D) + D_n/(L_nN_A))
    C_j = ε_sA/W;   1/C² = 2(V_bi − V)/(qε_sNA²);   N = 2/(qε_sA²|d(1/C²)/dV|)
    Schottky: Φ_B = Φ_m − χ;   V_bi = Φ_m − Φ_s;   J_s = A∗∗T²e^{−qΦ_B/kT}
    Ohmic (tunnelling): N_D ≳ 10¹⁹ cm⁻³

## Devices

    BJT: I_C = I_Se^{qV_BE/kT};   α_T ≈ 1 − W_B²/2L_n²;   β = α/(1 − α)
    MOSFET: V_T = V_FB + 2φ_F + √(4qε_sN_Aφ_F)/C_ox
    I_D(sat) = (μC_ox/2)(W/L)(V_GS − V_T)²

## Rules of thumb

- Each decade of doping moves E_F by 60 mV; each 60 mV of forward bias raises diode current tenfold (300 K).
- n_i(Si) roughly doubles every 8 °C.
- Doping 10¹⁶ cm⁻³ in Si = 1 dopant per 5×10⁶ Si atoms; ρ ≈ 0.5 Ω·cm (n-type), 1.4 Ω·cm (p-type).
- Diffusion length in good Si: tens to hundreds of μm.
