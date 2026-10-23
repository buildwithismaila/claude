# Week 6 — Continuous Assessment Test 1 and Review
<!-- group: Module 2 · Energy Bands & Carrier Statistics -->

**Plan:** mid-module evaluation of crystal structures and carrier statistics (Weeks 1–5).

## Learning objectives

By the end of this week you should be able to:

1. Revise crystal structures, Miller indices and bonding (Week 1).
2. Revise energy bands and direct/indirect gaps (Week 4).
3. Calculate occupation probabilities with the Fermi–Dirac function (Week 5).
4. Calculate n, p and E_F for doped and compensated silicon and germanium (Weeks 4–5).

This page has a one-screen review of what CAT 1 covers, followed by a practice test with full solutions. The questions are written in the style of the lecturer's revision questions and the PGD exam paper. They are practice questions, not the actual CAT.

## Symbols and abbreviations used this week

Every symbol, constant and abbreviation on this page is listed here, even if an earlier week already defined it, so you can study this page on its own.

**Constants and units**

| Symbol | Meaning | Units / typical value |
|---|---|---|
| q | Magnitude of the electronic charge | 1.6×10⁻¹⁹ C |
| k | Boltzmann constant | 8.617×10⁻⁵ eV/K = 1.381×10⁻²³ J/K |
| kT | Thermal energy | 0.0259 eV (often 0.02585 eV) at 300 K |
| T | Absolute temperature | kelvin (K); room temperature = 300 K |
| h | Planck constant | 6.626×10⁻³⁴ J·s |
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
| f(E) | Fermi–Dirac function: probability that a state at energy E is occupied | dimensionless, 0 to 1 |
| N_c | Effective density of states in the conduction band | cm⁻³; Si 2.8×10¹⁹ at 300 K |
| N_v | Effective density of states in the valence band | cm⁻³; Si 1.04×10¹⁹ at 300 K |
| n | Electron concentration (free electrons per cm³) | cm⁻³ |
| p | Hole concentration (holes per cm³) | cm⁻³ |
| n_i | Intrinsic carrier concentration (n = p = n_i in pure material) | cm⁻³; Si ≈ 1×10¹⁰ at 300 K |
| N_D | Donor concentration | cm⁻³ |
| N_A | Acceptor concentration | cm⁻³ |
| k (wave vector) | Wave vector, 2π/λ; measures the electron's momentum, p = ħk | m⁻¹ or cm⁻¹ |
| α (Kronig–Penney) | √(2mE)/ħ, set by the electron energy | m⁻¹ |
| P (Kronig–Penney) | Barrier strength mV₀ba/ħ² | dimensionless |
| λ | Wavelength | μm or nm; λ(μm) = 1.24/E(eV) |
| a | Lattice constant: edge length of the cubic unit cell | Å; Si 5.43, Ge and GaAs 5.65 |
| (h k l), {h k l} | Miller indices of a plane; family of equivalent planes | integers |
| d_hkl | Spacing between neighbouring (h k l) planes, a/√(h² + k² + l²) | Å |
| r_nn | Nearest-neighbour distance | Å; Si 2.35 |
| f (growth) | Fraction of the melt already solidified | 0 to 1 |
| μ, μ_n, μ_p | Mobility: drift velocity per unit field (electrons, holes) | cm²/(V·s); Si μ_n 1350, μ_p 480 |
| σ | Conductivity, q(nμ_n + pμ_p) (in Week 8, σ is also a capture cross-section) | S/cm (siemens per cm) |
| ρ | Resistivity, 1/σ | Ω·cm |
| λ_max | Longest wavelength a material absorbs, 1.24/E_g (μm, E_g in eV) | μm |
| σ_i, ρ_i | Conductivity and resistivity of intrinsic (undoped) material; σ_doped after doping | S/cm; Ω·cm |

**Abbreviations**

| Abbreviation | Meaning |
|---|---|
| Si | Silicon |
| Ge | Germanium |
| GaAs | Gallium arsenide |
| GaN | Gallium nitride |
| InP | Indium phosphide |
| CB | Conduction band |
| VB | Valence band |
| APF | Atomic packing factor |
| LED | Light-emitting diode |
| CAT | Continuous Assessment Test |
| PGD | Postgraduate Diploma |


## Key terms

Every important word used this week is defined here, so you can read this week on its own.

**Crystal lattice.** A regular, endlessly repeating pattern of points in space; placing the same group of atoms (the basis) at every point builds the crystal.

**Unit cell.** The smallest block of the lattice that, repeated in all three directions, rebuilds the whole crystal. Atoms on its corners and faces are shared with neighbouring cells (a corner atom counts ⅛, a face atom ½).

**Lattice constant (a).** The edge length of the cubic unit cell, measured in ångströms (Å). For Si a = 5.43 Å; for Ge and GaAs a = 5.65 Å.

**Diamond cubic structure.** The crystal structure of Si and Ge: a cubic cell holding 8 atoms, each bonded covalently to 4 nearest neighbours (coordination number 4) at distance r_nn = (√3/4)a. Zinc blende, the structure of GaAs, is the same arrangement with two kinds of atom alternating.

**Miller indices (h k l).** Three whole numbers that name a crystal plane: take the plane's intercepts on the axes in units of a, take reciprocals, and clear fractions. An intercept at infinity gives 0; a negative intercept is written with a bar, e.g. 1̄.

    d_hkl = a / √(h² + k² + l²)

Where:

- d_hkl = spacing between neighbouring (h k l) planes (Å)
- a = lattice constant (Å)
- h, k, l = Miller indices (integers)

**Atomic packing factor (APF).** The fraction of the unit-cell volume filled by atoms, treated as hard spheres that touch their nearest neighbours.

    APF = (atoms per cell × (4/3)πr³) / a³

Where:

- r = atomic radius, half the nearest-neighbour distance (Å)
- a = lattice constant (Å)

**Valence band and conduction band (E_v, E_c).** The valence band is the highest range of electron energies that is normally full, holding the bonding electrons; its top edge is E_v. The conduction band is the next range above it, normally almost empty; its bottom edge is E_c. Electrons in the conduction band move freely and carry current.

**Band gap (E_g).** The range of energies between E_v and E_c in which no electron states exist in a perfect crystal; its width E_g = E_c − E_v is the energy needed to free an electron from a bond (1.12 eV for Si, 0.66 eV for Ge, 1.42 eV for GaAs).

*Why it matters:* a wider gap means far fewer thermally freed carriers, which is why intrinsic Si is about 10⁴ times more resistive than intrinsic Ge.

**Direct and indirect band gap.** In a direct-gap semiconductor (GaAs, GaN, InP) the conduction-band minimum and valence-band maximum occur at the same electron momentum (wave vector k), so an electron can fall across the gap and emit a photon on its own. In an indirect-gap semiconductor (Si, Ge) they occur at different k, so a lattice vibration (phonon) must also take part, and light emission is weak. The photon energy at the gap fixes the wavelength:

    λ = 1.24 / E_g

Where:

- λ = wavelength of light emitted or absorbed at the band edge (μm)
- E_g = band-gap energy (eV)

**Hole.** An empty state in the valence band, left when an electron leaves a bond. It behaves as a positive carrier of charge +q.

**Fermi level (E_F).** The energy at which an electron state has exactly a 50 % chance of being occupied. Its position between E_v and E_c sets how many electrons and holes there are.

**Fermi–Dirac function (f(E)).** The probability that an allowed state at energy E holds an electron in thermal equilibrium. When E − E_F is more than about 3kT it can be replaced by the Boltzmann approximation f ≈ e^{−(E − E_F)/kT}.

    f(E) = 1 / ( 1 + e^{(E − E_F)/kT} )

Where:

- f(E) = occupation probability, 0 to 1 (dimensionless)
- E = energy of the state (eV)
- E_F = Fermi level (eV)
- kT = thermal energy, 0.0259 eV at 300 K (k = 8.617×10⁻⁵ eV/K)

*Why it matters:* 1 − f(E) is the probability of a hole, and f combined with the number of states gives n and p.

**Intrinsic semiconductor (n_i).** A pure semiconductor whose free electrons and holes come only from broken bonds, so n = p = n_i, the intrinsic carrier concentration (1×10¹⁰ cm⁻³ for Si and 2.4×10¹³ cm⁻³ for Ge at 300 K). Its Fermi level, the intrinsic level E_i, lies close to mid-gap.

**Doping and compensation.** Doping is adding a small, controlled amount of impurity: donors (e.g. P) give electrons and make the material n-type; acceptors (e.g. B) create holes and make it p-type. When both are present they partly cancel (compensation), and the material behaves as if doped with the difference, N_D − N_A or N_A − N_D.

**Majority and minority carriers.** The majority carrier is the more numerous carrier type (electrons in n-type, holes in p-type); the minority carrier is the less numerous one.

**Mass action law.** In thermal equilibrium the product of electron and hole concentrations is fixed at a given temperature, whatever the doping.

    n p = n_i²

Where:

- n, p = electron and hole concentrations (cm⁻³)
- n_i = intrinsic carrier concentration (cm⁻³)

*Why it matters:* it gives the minority concentration as soon as the majority concentration is known.

**Mobility and conductivity (μ, σ).** Mobility is the drift speed a carrier reaches per unit electric field, in cm²/(V·s). Conductivity measures how easily the material carries current; resistivity ρ = 1/σ is its inverse.

    σ = q (n μ_n + p μ_p)

Where:

- σ = conductivity (S/cm); ρ = 1/σ (Ω·cm)
- q = electronic charge, 1.6×10⁻¹⁹ C
- n, p = electron and hole concentrations (cm⁻³)
- μ_n, μ_p = electron and hole mobilities (cm²/(V·s)); Si 1350 and 480, Ge 3900 and 1900

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

> **Also revise:** the lecturer's own mid-module evaluation (ten short-answer and five calculation questions on carrier statistics) is solved at the end of Week 5, section 26.

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

**Question.** Silicon has lattice constant 5.43 Å. Calculate (a) the number of atoms per cm³ and (b) the nearest-neighbour distance.

**Given:** a = 5.43 Å = 5.43×10⁻⁸ cm; diamond cubic structure, 8 atoms per unit cell.

**Find:** (a) atom density N, (b) nearest-neighbour distance r_nn.

**Formula:**

    N = (atoms per cell)/a³,     r_nn = (√3/4)a

**Solution.**

The diamond unit cell holds 8 atoms (8 corners × ⅛ + 6 faces × ½ + 4 inside).

    (a) N = 8/a³ = 8/(5.43×10⁻⁸ cm)³ = 8/(1.601×10⁻²² cm³) = 5.0×10²² atoms/cm³

    (b) r_nn = (√3/4)a = 0.433 × 5.43 Å = 2.35 Å

**Answer:** **(a) N = 5.0×10²² atoms/cm³; (b) r_nn = 2.35 Å.**

**What this means:** a typical doping of 10¹⁶ cm⁻³ replaces only one silicon atom in every 5 million, yet it changes the conductivity enormously. The 2.35 Å spacing is the length of each covalent Si–Si bond.

### 2. Miller indices

**Question.** Find the Miller indices of planes with intercepts (a) 3a, 2b, c and (b) a, −b, ∞. For (a), find the interplanar spacing in Si.

**Given:** intercepts (a) 3, 2, 1 and (b) 1, −1, ∞ (in units of a); a = 5.43 Å.

**Find:** the Miller indices of each plane, and d for plane (a).

**Formula:** take reciprocals of the intercepts and clear fractions; then

    d_hkl = a/√(h² + k² + l²)

**Solution.**

| | x | y | z |
|---|---|---|---|
| (a) Intercepts | 3 | 2 | 1 |
| Reciprocals | 1/3 | 1/2 | 1 |
| × 6 | 2 | 3 | 6 |

(a) **(2 3 6)**. d₂₃₆ = 5.43/√(4 + 9 + 36) = 5.43/7 = **0.776 Å**.

(b) Intercepts 1, −1, ∞ → reciprocals 1, −1, 0 → **(1 1̄ 0)**, a plane parallel to z.

**Answer:** **(a) (2 3 6), d₂₃₆ = 0.776 Å; (b) (1 1̄ 0).**

**What this means:** high-index planes such as (2 3 6) lie very close together (less than 1 Å apart, about a third of the bond length) but each holds few atoms, whereas low-index planes such as (1 1̄ 0) are widely spaced (5.43/√2 = 3.84 Å) and densely packed with atoms.

### 3. Packing factor of diamond

**Question.** Show that the atomic packing factor of the diamond structure is 0.34.

**Given:** diamond cubic cell with 8 atoms; nearest neighbours touch at distance (√3/4)a.

**Find:** APF.

**Formula:**

    APF = (atoms per cell × (4/3)πr³) / a³,     r = r_nn/2 = (√3/8)a

**Solution.**

Nearest neighbours touch along the body diagonal at distance (√3/4)a, so the atomic radius is r = (√3/8)a. With 8 atoms per cell:

    APF = 8 × (4/3)πr³ / a³ = 8 × (4/3)π (√3/8)³ = (32π/3)(3√3/512) = π√3/16 = 0.34

**Answer:** **APF = π√3/16 = 0.34.**

**What this means:** only 34 % of the volume is filled (compared with 74 % for close-packed metals), an open structure that allows interstitial impurities to fit between the atoms.

### 4. Direct and indirect gaps

**Question.** State three differences between direct and indirect band-gap semiconductors and give the emission wavelength of GaAs.

**Given:** E_g(GaAs) = 1.42 eV (direct gap).

**Find:** three differences; the emission wavelength λ of GaAs.

**Formula:**

    λ (μm) = 1.24 / E_g (eV)

**Solution.**

(1) In a direct gap the conduction-band minimum and valence-band maximum are at the same k; in an indirect gap they are at different k. (2) Direct transitions need only a photon; indirect transitions also need a phonon. (3) Direct-gap materials emit light efficiently (GaAs, GaN, InP: LEDs, lasers); indirect ones do not (Si, Ge). Also: absorption near E_g is strong in direct-gap and weak in indirect-gap material; radiative lifetime is ns in direct and much longer in indirect.

| Feature | Direct gap | Indirect gap |
|---|---|---|
| CB minimum and VB maximum | Same k | Different k |
| What a band-to-band transition needs | A photon only | A photon and a phonon |
| Light emission | Efficient | Very weak |
| Absorption near E_g | Strong | Weak |
| Radiative lifetime | Nanoseconds | Much longer |
| Examples | GaAs, GaN, InP | Si, Ge |

    GaAs: λ = 1.24/1.42 = 0.873 μm (near infrared)

**Answer:** see the table; **GaAs emits at λ = 0.873 μm**.

**What this means:** 0.873 μm is just beyond the red end of visible light (about 0.7 μm), which is why GaAs LEDs are used for infrared remote controls and optical links rather than for visible displays.

### 5. Occupation probabilities

**Question.** Find the probability that a state (a) 0.1 eV above E_F and (b) kT above E_F is occupied at 300 K.

**Given:** (a) E − E_F = 0.1 eV, (b) E − E_F = kT; kT = 0.0259 eV.

**Find:** f(E) in each case.

**Formula:**

    f(E) = 1/(1 + e^{(E − E_F)/kT})

**Solution.**

    (a) f = 1/(1 + e^{0.1/0.0259}) = 1/(1 + e^{3.861}) = 1/(1 + 47.5) = 0.0206
    (b) f = 1/(1 + e^{1}) = 1/3.718 = 0.269

**Answer:** **(a) f = 0.0206 (about 2 %); (b) f = 0.269 (about 27 %).**

**What this means:** moving from 1kT to about 4kT above E_F cuts the occupation probability more than tenfold; occupation falls off steeply within a tenth of an eV of the Fermi level.

### 6. Temperature for a given probability

**Question.** At what temperature is there a 10⁻⁴ probability that a state 0.30 eV above E_F is occupied?

**Given:** f = 10⁻⁴, E − E_F = 0.30 eV, k = 8.617×10⁻⁵ eV/K.

**Find:** T.

**Formula:**

    f ≈ e^{−(E − E_F)/kT}   ⇒   kT = (E − E_F)/ln(1/f)

**Solution.**

Since f is small, use the Boltzmann form: f ≈ e^{−(E − E_F)/kT} = 10⁻⁴.

    0.30/kT = ln(10⁴) = 9.21   ⇒   kT = 0.0326 eV
    T = 0.0326/8.617×10⁻⁵ = 378 K

(The exact form 1/(1 + e^{x}) = 10⁻⁴ gives x = 9.21 as well, to three figures.)

**Answer:** **T ≈ 378 K** (about 105 °C).

**What this means:** a modest rise above room temperature (300 K) is enough to make a state 0.3 eV above E_F noticeably occupied, showing how sensitive carrier numbers are to temperature.

### 7. Carrier densities from E_F

**Question.** In a Si sample at 300 K the Fermi level is 0.25 eV below E_c. Find n and p. Is it n- or p-type?

**Given:** E_c − E_F = 0.25 eV, N_c = 2.8×10¹⁹ cm⁻³, n_i = 1×10¹⁰ cm⁻³, kT = 0.0259 eV.

**Find:** n, p and the type.

**Formula:**

    n = N_c e^{−(E_c − E_F)/kT},     p = n_i²/n

**Solution.**

    n = N_c e^{−(E_c−E_F)/kT} = 2.8×10¹⁹ × e^{−0.25/0.0259} = 2.8×10¹⁹ × e^{−9.65}
      = 2.8×10¹⁹ × 6.4×10⁻⁵ = 1.8×10¹⁵ cm⁻³
    p = n_i²/n = 10²⁰/1.8×10¹⁵ = 5.6×10⁴ cm⁻³

**Answer:** **n = 1.8×10¹⁵ cm⁻³, p = 5.6×10⁴ cm⁻³.** n ≫ p, so the sample is **n-type** (doped with about 1.8×10¹⁵ cm⁻³ donors).

**What this means:** the Fermi level sits about 0.31 eV above mid-gap, which corresponds to light n-type doping; the electrons outnumber the holes by about 3×10¹⁰ to one.

### 8. Compensated silicon

**Question.** Si is doped with N_A = 1×10¹⁶ cm⁻³ and N_D = 3×10¹⁵ cm⁻³. Find n, p and the Fermi level position at 300 K.

**Given:** N_A = 1×10¹⁶ cm⁻³, N_D = 3×10¹⁵ cm⁻³, n_i = 1×10¹⁰ cm⁻³, kT = 0.0259 eV.

**Find:** n, p and E_i − E_F.

**Formula:**

    p ≈ N_A − N_D,     n = n_i²/p,     E_i − E_F = kT ln(p/n_i)

**Solution.**

N_A > N_D, so the material is p-type with net doping N_A − N_D = 7×10¹⁵ cm⁻³ ≫ n_i.

    p ≈ 7×10¹⁵ cm⁻³
    n = n_i²/p = 10²⁰/7×10¹⁵ = 1.4×10⁴ cm⁻³
    E_i − E_F = kT ln(p/n_i) = 0.0259 × ln(7×10⁵) = 0.0259 × 13.46 = 0.349 eV

**Answer:** **p = 7×10¹⁵ cm⁻³, n = 1.4×10⁴ cm⁻³; the Fermi level is 0.349 eV below E_i.**

**What this means:** the donors cancel 30 % of the acceptors, so the sample behaves as p-type silicon with 7×10¹⁵ cm⁻³ acceptors. Both dopants still scatter carriers, however, so the mobility is that for 1.3×10¹⁶ cm⁻³ total impurities.

### 9. Lightly doped germanium

**Question.** Germanium is doped with N_D = 1×10¹⁵ cm⁻³. Find n and p at 300 K, without assuming n_i is negligible.

**Given:** N_D = 1×10¹⁵ cm⁻³, N_A = 0, n_i(Ge) = 2.4×10¹³ cm⁻³.

**Find:** n and p.

**Formula:**

    n = N_D/2 + √( (N_D/2)² + n_i² ),     p = n_i²/n

**Solution.**

n_i = 2.4×10¹³ is not negligible compared with N_D = 10¹⁵, so use the exact neutrality solution:

    n = N_D/2 + √((N_D/2)² + n_i²) = 5×10¹⁴ + √(2.5×10²⁹ + 5.76×10²⁶)
      = 5×10¹⁴ + 5.006×10¹⁴ = 1.0006×10¹⁵ cm⁻³
    p = n_i²/n = 5.76×10²⁶/1.0006×10¹⁵ = 5.76×10¹¹ cm⁻³

**Answer:** **n = 1.0006×10¹⁵ cm⁻³ ≈ N_D, p = 5.76×10¹¹ cm⁻³.**

**What this means:** n is still essentially N_D, but the minority concentration (5.8×10¹¹ cm⁻³) is about 6×10⁶ times larger than in silicon with the same doping (10⁵ cm⁻³): this is why Ge diodes leak so much.

### 10. Intrinsic germanium

**Question.** Calculate the conductivity and resistivity of intrinsic germanium at 300 K.

**Given:** n = p = n_i = 2.4×10¹³ cm⁻³, μ_n = 3900, μ_p = 1900 cm²/V·s, q = 1.6×10⁻¹⁹ C.

**Find:** σ_i and ρ_i.

**Formula:**

    σ_i = q n_i (μ_n + μ_p),     ρ_i = 1/σ_i

**Solution.**

    σ_i = q n_i (μ_n + μ_p) = 1.6×10⁻¹⁹ × 2.4×10¹³ × (3900 + 1900)
        = 1.6×10⁻¹⁹ × 1.392×10¹⁷ = 0.0223 S/cm
    ρ_i = 1/σ_i = 44.9 Ω·cm

**Answer:** **σ_i = 0.0223 S/cm, ρ_i = 44.9 Ω·cm.**

**What this means:** for comparison, intrinsic Si is about 3×10⁵ Ω·cm, nearly 10⁴ times higher, because its band gap is larger (1.12 eV against 0.66 eV) and so far fewer carriers are thermally freed.

---

## Practice questions

These extra questions practise this week's ideas. Work each one on paper before reading the solution; the calculation questions follow the same Question, Given, Find, Solution, Answer layout as the worked examples.

#### Practice 6.1: intercepts from Miller indices

**Question.** A plane has Miller indices (1 2 3). Find a set of intercepts it makes on the axes.

**Given:** (h k l) = (1 2 3).

**Find:** intercepts.

**Solution.** Intercepts are the reciprocals of the indices: 1, 1/2, 1/3. Multiplying by 6 to clear fractions gives an equivalent parallel plane.

**Answer:** **a, b/2, c/3 (or, equivalently, 6a, 3b, 2c).**

#### Practice 6.2: band gap from an absorption edge

**Question.** A semiconductor stops absorbing light at wavelengths longer than 1.1 μm. Estimate its band gap.

**Given:** λ_max = 1.1 μm.

**Find:** E_g.

**Solution.**

    E_g = 1.24/λ = 1.24/1.1 = 1.13 eV

**Answer:** **E_g ≈ 1.13 eV** (silicon).

#### Practice 6.3: hole concentration from the Fermi level

**Question.** In p-type silicon at 300 K the Fermi level is 0.10 eV above the valence band. Find the hole concentration.

**Given:** E_F − E_v = 0.10 eV, N_v = 1.04×10¹⁹ cm⁻³, kT = 0.0259 eV.

**Find:** p.

**Solution.**

    p = N_v e^{−(E_F − E_v)/kT} = 1.04×10¹⁹ × e^{−3.86} = 1.04×10¹⁹ × 0.0211 = 2.2×10¹⁷ cm⁻³

**Answer:** **p = 2.2×10¹⁷ cm⁻³.**

#### Practice 6.4: probability of a hole

**Question.** What is the probability that a state 0.05 eV below the Fermi level is empty (holds a hole) at 300 K?

**Given:** E = E_F − 0.05 eV, kT = 0.0259 eV.

**Find:** 1 − f(E).

**Solution.**

    1 − f = 1 − 1/(1 + e^{−0.05/0.0259}) = 1/(1 + e^{0.05/0.0259}) = 1/(1 + 6.89) = 0.127

**Answer:** **12.7 %.**

#### Practice 6.5: short-answer revision

**Question.** (a) State the mass-action law. (b) What is the coordination number of the diamond structure? (c) Name the structure of GaAs. (d) Which carrier is the minority carrier in boron-doped silicon?

**Answer.** **(a)** np = n_i² in thermal equilibrium. **(b)** 4. **(c)** Zinc blende. **(d)** Electrons.

---

## Objectives check

Use this table to confirm you have met this week's objectives. Cover the Answer column and answer each check question from memory. If you cannot, go back to the section in the last column before moving on.

| # | Objective | Check yourself | Answer | Where it is taught |
|---|---|---|---|---|
| 1 | Revise crystal structures, Miller indices and bonding (Week 1). | Find the Miller indices for intercepts 2a, 2b, 4c. | 1/2, 1/2, 1/4 → × 4 → (2 2 1). | Review; practice Q1–Q3 |
| 2 | Revise energy bands and direct/indirect gaps (Week 4). | State one property that distinguishes a direct-gap semiconductor. | Efficient light emission (also: CB minimum and VB maximum at the same k). | Practice Q4 |
| 3 | Calculate occupation probabilities with the Fermi–Dirac function (Week 5). | What is f at E = E_F + kT? | 1/(1 + e) = 0.269. | Practice Q5–Q6 |
| 4 | Calculate n, p and E_F for doped and compensated silicon and germanium (Weeks 4–5). | Si with E_F 0.25 eV below E_c: n-type or p-type? | n-type (n = 1.8×10¹⁵ cm⁻³). | Practice Q7–Q10 |
