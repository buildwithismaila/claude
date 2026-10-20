# Week 6 — Continuous Assessment Test 1 and Review
<!-- group: Module 2 · Energy Bands & Carrier Statistics -->

**Plan:** mid-module evaluation of crystal structures and carrier statistics (Weeks 1–5).

This page has a one-screen review of what CAT 1 covers, followed by a practice test with full solutions. The questions are written in the style of the lecturer's revision questions and the PGD exam paper. They are practice questions, not the actual CAT.

## Review: what you must be able to do

**Crystals (Week 1)**

- Define lattice, basis, unit cell, lattice constant, coordination number, APF.
- State the structures: Si and Ge diamond cubic, GaAs zinc blende; 8 atoms per cell; 4 nearest neighbours.
- Find Miller indices from intercepts (intercepts → reciprocals → clear fractions); handle ∞ (index 0) and negative intercepts (bar).
- Use d_{hkl} = a/√(h² + k² + l²).

**Materials and bonding (Week 1)**

- Compare conductors, semiconductors and insulators; Si, Ge and GaAs.
- Explain covalent bonding, electron–hole pairs, n-type and p-type doping.

**Bands and statistics (Weeks 4–5)**

- Schrödinger equation terms; Kronig–Penney: allowed bands where |P sin(αa)/αa + cos αa| ≤ 1.
- Direct and indirect gaps; λ(μm) = 1.24/E_g(eV).
- f(E) = 1/(1 + e^{(E−E_F)/kT}); at 0 K a step; Boltzmann approximation for E − E_F > 3kT.
- n = N_c e^{−(E_c−E_F)/kT}, p = N_v e^{−(E_F−E_v)/kT}, n_i = √(N_cN_v)e^{−E_g/2kT}, np = n_i².
- Charge neutrality and compensation; E_F − E_i = kT ln(n/n_i).

## Practice test (60 minutes)

Use q = 1.6×10⁻¹⁹ C, kT = 0.0259 eV at 300 K, Si: n_i = 1×10¹⁰ cm⁻³, N_c = 2.8×10¹⁹ cm⁻³, μ_n = 1350, μ_p = 480 cm²/V·s; Ge: n_i = 2.4×10¹³ cm⁻³, μ_n = 3900, μ_p = 1900 cm²/V·s.

1. Silicon has lattice constant 5.43 Å. Calculate (a) the number of atoms per cm³ and (b) the nearest-neighbour distance.
2. Find the Miller indices of planes with intercepts (a) 3a, 2b, c and (b) a, −b, ∞. For (a), find the interplanar spacing in Si.
3. Show that the atomic packing factor of the diamond structure is 0.34.
4. State three differences between direct and indirect band-gap semiconductors and give the emission wavelength of GaAs.
5. Find the probability that a state (a) 0.1 eV above E_F and (b) kT above E_F is occupied at 300 K.
6. At what temperature is there a 10⁻⁴ probability that a state 0.30 eV above E_F is occupied?
7. In a Si sample at 300 K the Fermi level is 0.25 eV below E_c. Find n and p. Is it n- or p-type?
8. Si is doped with N_A = 1×10¹⁶ cm⁻³ and N_D = 3×10¹⁵ cm⁻³. Find n, p and the Fermi level position at 300 K.
9. Germanium is doped with N_D = 1×10¹⁵ cm⁻³. Find n and p at 300 K, without assuming n_i is negligible.
10. Calculate the conductivity and resistivity of intrinsic germanium at 300 K.

## Solutions

### 1. Atom density and nearest neighbours in Si

The diamond unit cell holds 8 atoms (8 corners × ⅛ + 6 faces × ½ + 4 inside).

    (a) N = 8/a³ = 8/(5.43×10⁻⁸ cm)³ = 8/(1.601×10⁻²² cm³) = 5.0×10²² atoms/cm³

    (b) r_nn = (√3/4)a = 0.433 × 5.43 Å = 2.35 Å

### 2. Miller indices

| | x | y | z |
|---|---|---|---|
| (a) Intercepts | 3 | 2 | 1 |
| Reciprocals | 1/3 | 1/2 | 1 |
| × 6 | 2 | 3 | 6 |

(a) **(2 3 6)**. d₂₃₆ = 5.43/√(4 + 9 + 36) = 5.43/7 = **0.776 Å**.

(b) Intercepts 1, −1, ∞ → reciprocals 1, −1, 0 → **(1 1̄ 0)**, a plane parallel to z.

### 3. Packing factor of diamond

Nearest neighbours touch along the body diagonal at distance (√3/4)a, so the atomic radius is r = (√3/8)a. With 8 atoms per cell:

    APF = 8 × (4/3)πr³ / a³ = 8 × (4/3)π (√3/8)³ = (32π/3)(3√3/512) = π√3/16 = 0.34

Only 34 % of the volume is filled, an open structure that allows interstitial impurities.

### 4. Direct and indirect gaps

(1) In a direct gap the conduction-band minimum and valence-band maximum are at the same k; in an indirect gap they are at different k. (2) Direct transitions need only a photon; indirect transitions also need a phonon. (3) Direct-gap materials emit light efficiently (GaAs, GaN, InP: LEDs, lasers); indirect ones do not (Si, Ge). Also: absorption near E_g is strong in direct-gap and weak in indirect-gap material; radiative lifetime is ns in direct and much longer in indirect.

    GaAs: λ = 1.24/1.42 = 0.873 μm (near infrared)

### 5. Occupation probabilities

    (a) f = 1/(1 + e^{0.1/0.0259}) = 1/(1 + e^{3.861}) = 1/(1 + 47.5) = 0.0206
    (b) f = 1/(1 + e^{1}) = 1/3.718 = 0.269

### 6. Temperature for a given probability

Since f is small, use the Boltzmann form: f ≈ e^{−(E − E_F)/kT} = 10⁻⁴.

    0.30/kT = ln(10⁴) = 9.21   ⇒   kT = 0.0326 eV
    T = 0.0326/8.617×10⁻⁵ = 378 K

(The exact form 1/(1 + e^{x}) = 10⁻⁴ gives x = 9.21 as well, to three figures.)

### 7. Carrier densities from E_F

    n = N_c e^{−(E_c−E_F)/kT} = 2.8×10¹⁹ × e^{−0.25/0.0259} = 2.8×10¹⁹ × e^{−9.65}
      = 2.8×10¹⁹ × 6.4×10⁻⁵ = 1.8×10¹⁵ cm⁻³
    p = n_i²/n = 10²⁰/1.8×10¹⁵ = 5.6×10⁴ cm⁻³

n ≫ p, so the sample is **n-type** (doped with about 1.8×10¹⁵ cm⁻³ donors).

### 8. Compensated silicon

N_A > N_D, so the material is p-type with net doping N_A − N_D = 7×10¹⁵ cm⁻³ ≫ n_i.

    p ≈ 7×10¹⁵ cm⁻³
    n = n_i²/p = 10²⁰/7×10¹⁵ = 1.4×10⁴ cm⁻³
    E_i − E_F = kT ln(p/n_i) = 0.0259 × ln(7×10⁵) = 0.0259 × 13.46 = 0.349 eV

The Fermi level is 0.349 eV below E_i. Both dopants still scatter carriers, so mobility is that for 1.3×10¹⁶ cm⁻³ total impurities.

### 9. Lightly doped germanium

n_i = 2.4×10¹³ is not negligible compared with N_D = 10¹⁵, so use the exact neutrality solution:

    n = N_D/2 + √((N_D/2)² + n_i²) = 5×10¹⁴ + √(2.5×10²⁹ + 5.76×10²⁶)
      = 5×10¹⁴ + 5.006×10¹⁴ = 1.0006×10¹⁵ cm⁻³
    p = n_i²/n = 5.76×10²⁶/1.0006×10¹⁵ = 5.76×10¹¹ cm⁻³

n is still essentially N_D, but the minority concentration (5.8×10¹¹) is 10⁷ times larger than in silicon with the same doping (10⁵): this is why Ge diodes leak so much.

### 10. Intrinsic germanium

    σ_i = q n_i (μ_n + μ_p) = 1.6×10⁻¹⁹ × 2.4×10¹³ × (3900 + 1900)
        = 1.6×10⁻¹⁹ × 1.392×10¹⁷ = 0.0223 S/cm
    ρ_i = 1/σ_i = 44.9 Ω·cm

For comparison, intrinsic Si is about 3×10⁵ Ω·cm, nearly 10⁴ times higher, because its band gap is larger.
