# Week 4 — Energy Bands and Carrier Concentrations
<!-- group: Module 2 · Energy Bands & Carrier Statistics -->

**Plan:** quantum-mechanics foundations (Schrödinger equation overview, Kronig–Penney model); energy band gaps, allowed and forbidden states; intrinsic and extrinsic carrier concentrations.

Week 1 stated that atoms in a solid form bands. This week shows why, using quantum mechanics, and then counts how many electrons and holes the bands hold.

## Part A: Quantum-mechanics foundations

## Why quantum mechanics

Three results from early quantum theory are needed:

- **Energy is quantised.** Electrons bound in atoms occupy discrete levels (Planck, Bohr). A photon has energy E = hν.
- **Wave–particle duality.** An electron of momentum p behaves as a wave of wavelength λ = h/p (de Broglie). Write p = ħk, where k = 2π/λ is the wave vector.
- **Uncertainty principle.** Δx·Δp ≥ ħ/2: an electron's position and momentum cannot both be exact, so we describe it by a probability wave ψ.

Constants: h = 6.626×10⁻³⁴ J·s, ħ = h/2π = 1.055×10⁻³⁴ J·s, m₀ = 9.11×10⁻³¹ kg.

## The Schrödinger equation

The time-independent equation in one dimension:

    −(ħ²/2m) d²ψ/dx² + V(x) ψ = E ψ

In three dimensions, −(ħ²/2m)∇²ψ + Vψ = Eψ, or Ĥψ = Eψ.

- ψ(x) is the **wave function**. |ψ(x)|² dx is the probability of finding the electron between x and x + dx.
- The first term is the **kinetic energy** operator (p²/2m with p → −iħ d/dx).
- V(x) is the **potential energy**: the crystal potential seen by the electron.
- E is the **total energy**, an eigenvalue. Only certain E give acceptable solutions.

Conditions on ψ: finite, single-valued, continuous, with continuous dψ/dx where V is finite, and normalised (∫|ψ|²dx = 1).

**Free electron** (V = 0): ψ = A e^{ikx}, E = ħ²k²/2m. A parabola: any energy is allowed.

**Particle in a box** of width L (infinite walls): ψ = sin(nπx/L), E_n = n²π²ħ²/2mL². Confinement produces discrete levels, as in quantum wells.

## From atoms to bands

Bring N identical atoms together. When far apart, each has the same discrete levels. As they approach, their outer wave functions overlap and, by the Pauli exclusion principle, each level must **split into N closely spaced levels**. With N ≈ 5×10²² cm⁻³, these form an almost continuous **band**.

In Si, the 3s and 3p levels (4 electrons per atom, 8 states) hybridise. At the actual spacing they split into a lower band with 4N states (the **valence band**, completely full at 0 K) and an upper band with 4N states (the **conduction band**, empty at 0 K), separated by the gap E_g = 1.12 eV.

## Bloch's theorem

In a perfectly periodic potential V(x + a) = V(x), the solutions take the form

    ψ_k(x) = u_k(x) e^{ikx},   with u_k(x + a) = u_k(x)

A plane wave modulated by a function with the lattice period. An electron in a perfect crystal is therefore **not scattered** by the lattice itself; only departures from periodicity scatter it.

## The Kronig–Penney model

Kronig and Penney replaced the real crystal potential by a 1-D periodic array of **rectangular barriers**: wells of width a with V = 0, separated by barriers of height V₀ and width b, period (a + b).

They solved Schrödinger's equation in each region, joined the solutions with continuity of ψ and dψ/dx, and applied Bloch's theorem. In the limit of thin, high barriers (b → 0, V₀ → ∞ with V₀b finite), the condition for a solution is:

    P · sin(αa)/(αa) + cos(αa) = cos(ka)

    α = √(2mE)/ħ,      P = m V₀ b a / ħ²

P measures how strongly the electron is bound (barrier strength).

**How bands appear.** The right side, cos(ka), can only lie between −1 and +1. The left side, as a function of energy (through α), oscillates with an amplitude that exceeds 1. Energies for which the left side lies between ±1 are **allowed** (bands). Energies for which it lies outside are **forbidden** (gaps).

@fig figures/kronig-penney.svg | Graphical solution of the Kronig–Penney condition with P = 3π/2. Allowed bands (shaded) are the energies where the curve stays between −1 and +1.

**Conclusions:**

1. The energy spectrum is a series of **allowed bands separated by forbidden gaps**.
2. Band edges occur at ka = nπ, i.e. at the **Brillouin-zone boundaries** k = ±nπ/a.
3. Bands become **wider** at higher energy, and the gaps narrower.
4. **P → ∞** (strong binding): bands shrink to single lines, the discrete levels of isolated atoms.
5. **P → 0** (free electron): the gaps disappear and E = ħ²k²/2m.

## Part B: Band gaps, allowed and forbidden states

## E–k diagrams and effective mass

Plotting E against k gives the band structure. Near a band extremum, E is approximately parabolic, and the electron behaves as a free particle with an **effective mass**:

    1/m∗ = (1/ħ²) d²E/dk²

A strongly curved band means small m∗ and high mobility. Values: Si m_n∗ ≈ 1.08m₀ (density-of-states), m_p∗ ≈ 0.56m₀; GaAs m_n∗ = 0.067m₀. Near the top of the valence band the curvature is negative: a missing electron there behaves as a positive particle with positive mass, the **hole**.

## Valence band, conduction band and gap

- **Valence band:** highest band that is completely filled at 0 K. Its top is E_v. Electrons here are in the covalent bonds. Holes move in this band.
- **Conduction band:** next higher band, empty at 0 K. Its bottom is E_c. Electrons here are free to move and conduct.
- **Forbidden gap:** E_g = E_c − E_v. No electron states exist here in a perfect crystal; impurities and defects can add states inside it.

E_g decreases slightly with temperature (Varshni relation, E_g(T) = E_g(0) − αT²/(T + β)): for Si, 1.17 eV at 0 K, 1.12 eV at 300 K.

## Direct and indirect gaps

@fig figures/ek.svg | In a direct-gap material (GaAs) the conduction-band minimum and valence-band maximum are at the same k. In an indirect-gap material (Si) they are at different k, so a phonon must supply the momentum difference.

A photon has very little momentum (k_photon ≈ 10⁵ cm⁻¹ compared with a zone-edge k ≈ 10⁸ cm⁻¹), so an optical transition is essentially vertical on the E–k diagram.

- **Direct gap:** the transition is vertical and needs only a photon. Radiative recombination is fast (ns) and efficient. Strong absorption above E_g. GaAs, InP, GaN, InGaAs.
- **Indirect gap:** the electron must also change momentum, which requires a **phonon** (lattice vibration) to be absorbed or emitted at the same time. This three-particle process is unlikely, so radiative recombination is slow and inefficient; energy is lost as heat through traps instead. Si, Ge, GaP, AlAs.

The emission wavelength of a band-to-band transition:

    λ (μm) = 1.24 / E_g (eV)

GaAs: 1.24/1.42 = 0.873 μm (near-infrared). Si: 1.24/1.12 = 1.11 μm, which is also why Si photodetectors stop responding above about 1.1 μm.

## Part C: Intrinsic and extrinsic carrier concentrations

The electron concentration is the number of available states times the probability that each is filled. Week 5 develops both factors properly; here we use the results.

## Equilibrium carrier concentrations

Using the Boltzmann approximation and integrating:

    n₀ = N_c exp( −(E_c − E_F)/kT )
    p₀ = N_v exp( −(E_F − E_v)/kT )

with the **effective densities of states**

    N_c = 2 (2π m_n∗ kT / h²)^{3/2},     N_v = 2 (2π m_p∗ kT / h²)^{3/2}

At 300 K: Si N_c = 2.8×10¹⁹, N_v = 1.04×10¹⁹ cm⁻³; GaAs N_c = 4.7×10¹⁷, N_v = 7.0×10¹⁸ cm⁻³. Both scale as T^{3/2}.

N_c is the number of states you would need at the single energy E_c to hold the same number of electrons as the whole band.

## Intrinsic semiconductor

In a pure crystal every electron in the conduction band left a hole in the valence band, so n₀ = p₀ = n_i. The Fermi level in this case is the **intrinsic level E_i**, very close to mid-gap.

    n_i = √(N_c N_v) exp( −E_g / 2kT )

    E_i = (E_c + E_v)/2 + (3/4)kT ln( m_p∗ / m_n∗ )

For Si the shift of E_i from mid-gap is only about −0.01 eV.

Values of n_i at 300 K: Si ≈ 1×10¹⁰ cm⁻³ (the accurate modern value is 9.65×10⁹; older texts use 1.5×10¹⁰), Ge 2.4×10¹³, GaAs 2.1×10⁶ cm⁻³.

n_i rises very steeply with temperature, mainly through exp(−E_g/2kT). For Si it roughly doubles every 8 °C near room temperature.

## The mass-action law

Multiply n₀ and p₀:

    n₀ p₀ = N_c N_v exp( −E_g/kT ) = n_i²

This holds in thermal equilibrium for **any** non-degenerate semiconductor, doped or not. Adding donors raises n and lowers p in proportion.

Equivalent forms using E_i:

    n₀ = n_i exp( (E_F − E_i)/kT ),     p₀ = n_i exp( (E_i − E_F)/kT )

## Extrinsic semiconductor

**Charge neutrality:** p₀ + N_D⁺ = n₀ + N_A⁻. With full ionisation and the mass-action law:

    n₀ = (N_D − N_A)/2 + √( ((N_D − N_A)/2)² + n_i² )

Usual approximations:

- **n-type**, N_D ≫ n_i: n₀ ≈ N_D, p₀ = n_i²/N_D.
- **p-type**, N_A ≫ n_i: p₀ ≈ N_A, n₀ = n_i²/N_A.
- **Compensated**: use the net doping |N_D − N_A|.

### Temperature regions (n-type)

1. **Freeze-out** (low T, below about 100 K for Si): donors are not all ionised; n < N_D.
2. **Extrinsic** (about 150–450 K for Si at 10¹⁵ cm⁻³): n ≈ N_D, constant. Devices operate here.
3. **Intrinsic** (high T): n_i exceeds N_D and n ≈ n_i rises steeply; the device loses its doping-defined behaviour. Sets the upper operating temperature.

---

## Examination questions solved (Q22–Q29, Q34)

### Q22. Explain the basic assumptions of the quantum mechanical model of electrons in a semiconductor.

1. **Wave nature of electrons.** Each electron is described by a wave function ψ obeying the Schrödinger equation; |ψ|² gives the probability of finding it at a point. Energy and momentum (p = ħk) are related through the band structure E(k).
2. **Adiabatic (Born–Oppenheimer) approximation.** The nuclei are much heavier than electrons and are treated as fixed at their lattice sites. Their vibrations (phonons) are added later as a perturbation that causes scattering.
3. **Perfect periodic crystal.** The ion cores form an infinite, perfectly periodic lattice, so the potential energy is periodic, V(r + R) = V(r) for every lattice vector R. Surfaces, impurities and defects are treated separately.
4. **One-electron (independent-electron) approximation.** Each electron moves independently in an average periodic potential produced by the ion cores and all the other electrons (mean-field or Hartree approximation), so a many-body problem becomes a single-particle one.
5. **Bloch's theorem** follows: wave functions are modulated plane waves ψ = u_k(r)e^{ik·r}.
6. **Pauli exclusion principle.** Each quantum state (k and spin) holds at most one electron, so the states fill from the bottom up. This, with the Fermi–Dirac distribution, gives the occupation of the bands.
7. **Effective-mass approximation.** Near the band edges, electrons and holes respond to external forces as free particles with an effective mass m∗ that contains the effect of the crystal potential.
8. **Thermal equilibrium statistics.** In equilibrium, electrons are distributed among the available states according to the Fermi–Dirac function.

### Q23. State the time-independent Schrödinger equation and explain the physical meaning of its terms.

In one dimension:

    −(ħ²/2m) d²ψ(x)/dx² + V(x) ψ(x) = E ψ(x)

In three dimensions: −(ħ²/2m)∇²ψ(r) + V(r)ψ(r) = Eψ(r), compactly Ĥψ = Eψ.

**Meaning of each term:**

- **ψ(x), the wave function**: the amplitude of the electron's probability wave. It has no direct physical meaning, but |ψ(x)|² dx is the probability of finding the electron between x and x + dx. ψ must be finite, single-valued, continuous and normalised.
- **ħ = h/2π**, the reduced Planck constant (1.055×10⁻³⁴ J·s); **m**, the electron mass (or the effective mass m∗ in a crystal).
- **−(ħ²/2m) d²ψ/dx²**: the **kinetic-energy** term. It comes from p²/2m with the momentum operator p = −iħ d/dx. The more sharply ψ curves, the higher the kinetic energy.
- **V(x)ψ**: the **potential-energy** term. V(x) is the potential energy of the electron at x, e.g. the periodic potential of the crystal ions, a barrier, or a well.
- **E**: the **total energy** of the electron, a constant (the equation is valid for stationary states whose energy does not change with time). Acceptable solutions exist only for particular values of E (eigenvalues), which is how quantisation arises.
- The left-hand side as a whole is the **Hamiltonian operator** Ĥ acting on ψ.

The full time-dependent wave function is Ψ(x, t) = ψ(x)e^{−iEt/ħ}; the time-independent equation is obtained when V does not depend on time.

### Q24. Explain the basic principle of the Kronig-Penney model and how it leads to the formation of energy bands.

**Principle.** The real periodic potential of a crystal is complicated. Kronig and Penney (1931) replaced it with the simplest periodic potential that can be solved exactly: a one-dimensional infinite array of **rectangular potential wells and barriers**. Each well (V = 0, width a) represents the region near an ion; each barrier (height V₀, width b) represents the region between ions. The period is a + b.

**Method.**

1. Solve Schrödinger's equation separately in a well (oscillating solutions, α² = 2mE/ħ²) and in a barrier (exponential solutions, β² = 2m(V₀ − E)/ħ²).
2. Apply continuity of ψ and dψ/dx at each boundary.
3. Apply **Bloch's theorem**, ψ(x + (a + b)) = e^{ik(a+b)}ψ(x), because the potential is periodic.
4. A non-trivial solution exists only if a determinant vanishes. Taking the limit of narrow, high barriers (b → 0, V₀ → ∞, with V₀b finite) gives:

    P · sin(αa)/(αa) + cos(αa) = cos(ka),     P = mV₀ba/ħ²

**How bands form.** The right-hand side, cos(ka), must lie between −1 and +1 for real k. Plot the left-hand side f(αa) against αa (i.e. against energy). It starts at 1 + P, oscillates like a damped cosine, and repeatedly rises above +1 and falls below −1. Only the energy ranges where −1 ≤ f(αa) ≤ +1 are solutions: these are the **allowed energy bands**. The ranges where |f| > 1 have no real k and therefore no electron states: these are the **forbidden energy gaps**.

**Results:**

- The spectrum consists of alternating allowed bands and forbidden gaps.
- Discontinuities in E(k) occur at k = nπ/a (Brillouin-zone boundaries), where Bragg reflection of the electron wave occurs.
- The width of allowed bands increases with energy (because the 1/αa factor damps the oscillation).
- As P → ∞ (electrons tightly bound), bands shrink to discrete atomic levels. As P → 0 (free electrons), the gaps vanish and E = ħ²k²/2m.

The model explains in a simple way why solids have bands and gaps, which is the basis of the classification into metals, semiconductors and insulators.

### Q25. Distinguish between valence band, conduction band, and forbidden energy gap.

| | Valence band | Conduction band | Forbidden energy gap |
|---|---|---|---|
| What it is | The highest band that is completely filled with electrons at 0 K | The lowest band above the valence band, empty at 0 K | The energy range between E_v and E_c in which no electron states exist (in a perfect crystal) |
| Edge | Top at E_v | Bottom at E_c | Width E_g = E_c − E_v |
| Electrons | Bound in covalent bonds; cannot conduct while the band is full | Free; move through the crystal and conduct | None (only impurity or defect levels) |
| Carriers | Holes (empty states) conduct here | Electrons conduct here | — |
| Origin | Bonding combinations of the atomic sp³ orbitals | Antibonding combinations | Splitting of bonding and antibonding states |
| Values | — | — | Si 1.12 eV, Ge 0.66 eV, GaAs 1.42 eV, SiO₂ ≈ 9 eV |

An electron needs at least E_g to jump from the valence to the conduction band; it then leaves a hole behind. The width of the gap decides whether a material is a metal (no gap), a semiconductor (small gap) or an insulator (large gap).

### Q26. Explain the difference between a direct band-gap and an indirect band-gap semiconductor.

On the E–k diagram, look at where the **conduction-band minimum** and the **valence-band maximum** occur.

| | Direct band gap | Indirect band gap |
|---|---|---|
| Band-edge positions | CB minimum and VB maximum at the **same k** (usually k = 0, the Γ point) | CB minimum at a **different k** from the VB maximum |
| Transition across the gap | Vertical: an electron can drop and emit a photon directly, conserving momentum | Needs a change of momentum, which a photon cannot supply; a **phonon** must take part |
| Process | Two-particle (electron + photon) | Three-particle (electron + photon + phonon), much less probable |
| Radiative recombination | Fast, efficient; lifetime ≈ ns | Slow, inefficient; recombination is mostly non-radiative via traps; lifetime μs–ms |
| Absorption near E_g | Sharp, strong (α ≈ 10⁴ cm⁻¹ just above E_g) | Weak, gradual; thicker material needed to absorb light |
| Examples | GaAs (1.42 eV), InP, GaN, InGaAs, CdTe | Si (1.12 eV), Ge (0.66 eV), GaP, AlAs, SiC |
| Applications | LEDs, laser diodes, efficient thin-film solar cells, fast photodetectors | ICs, transistors, power devices, Si solar cells and photodiodes (absorb but do not emit well) |

The emitted wavelength is λ = hc/E_g, i.e. λ(μm) = 1.24/E_g(eV). GaAs emits at 0.87 μm. Silicon's indirect gap is why there is no practical silicon laser.

### Q27. What is meant by an intrinsic semiconductor? Derive the expression for intrinsic carrier concentration.

**Intrinsic semiconductor.** A pure semiconductor crystal with no significant impurities or defects, in which free carriers are produced **only** by thermal excitation of electrons from the valence band to the conduction band. Each excited electron leaves a hole, so

    n = p = n_i

and the Fermi level lies at the intrinsic level E_i, very near the middle of the gap.

**Derivation.**

*Step 1: electrons.* The electron concentration is the density of states times the occupation probability, integrated over the conduction band:

    n = ∫_{E_c}^{∞} g_c(E) f(E) dE,     g_c(E) = (4π(2m_n∗)^{3/2}/h³) √(E − E_c)

*Step 2: Boltzmann approximation.* For E_c − E_F ≫ kT, f(E) ≈ exp(−(E − E_F)/kT). Then

    n = (4π(2m_n∗)^{3/2}/h³) exp(−(E_c − E_F)/kT) ∫₀^{∞} √x · e^{−x/kT} dx,   x = E − E_c

*Step 3: the integral.* ∫₀^{∞} x^{1/2} e^{−x/kT} dx = (kT)^{3/2} Γ(3/2) = (kT)^{3/2} (√π/2). Hence

    n = N_c exp( −(E_c − E_F)/kT ),     N_c = 2(2πm_n∗kT/h²)^{3/2}

*Step 4: holes.* Similarly, with 1 − f(E) ≈ exp(−(E_F − E)/kT) in the valence band,

    p = N_v exp( −(E_F − E_v)/kT ),     N_v = 2(2πm_p∗kT/h²)^{3/2}

*Step 5: the intrinsic condition.* Multiply n and p. E_F cancels:

    n p = N_c N_v exp( −(E_c − E_v)/kT ) = N_c N_v exp( −E_g/kT )

In an intrinsic semiconductor n = p = n_i, so n·p = n_i², and

    n_i = √(N_c N_v) · exp( −E_g / 2kT )

Substituting N_c and N_v gives the explicit temperature dependence:

    n_i = 2 (2πkT/h²)^{3/2} (m_n∗ m_p∗)^{3/4} exp( −E_g / 2kT )   ∝ T^{3/2} e^{−E_g/2kT}

*Step 6: the intrinsic Fermi level.* Setting n = p and solving:

    E_i = (E_c + E_v)/2 + (kT/2) ln(N_v/N_c) = (E_c + E_v)/2 + (3kT/4) ln(m_p∗/m_n∗)

**Numerical check for Si at 300 K:** √(2.8×10¹⁹ × 1.04×10¹⁹) = 1.71×10¹⁹; exp(−1.12/(2 × 0.0259)) = exp(−21.6) = 4.1×10⁻¹⁰; n_i ≈ 7×10⁹ cm⁻³, the same order as the accepted 1×10¹⁰ cm⁻³ (the difference comes from the exact values of E_g and the effective masses).

### Q28. Explain the difference between intrinsic and extrinsic carrier concentrations.

| | Intrinsic carrier concentration | Extrinsic carrier concentration |
|---|---|---|
| Material | Pure (undoped) semiconductor | Doped semiconductor |
| Source of carriers | Thermal breaking of covalent bonds only (band-to-band excitation) | Mainly ionised dopants (donors or acceptors), plus a small thermal contribution |
| Electron vs hole | n = p = n_i | Unequal: n ≫ p (n-type) or p ≫ n (p-type); majority and minority carriers |
| Formula | n_i = √(N_cN_v) exp(−E_g/2kT) | n ≈ N_D, p = n_i²/N_D (n-type); p ≈ N_A, n = n_i²/N_A (p-type) |
| Typical value (Si, 300 K) | 1×10¹⁰ cm⁻³ | 10¹⁴–10²⁰ cm⁻³ majority |
| Temperature dependence | Very strong, exponential | Nearly constant over the extrinsic range; becomes intrinsic at high T |
| Controlled by | Material (E_g) and temperature | Doping level, chosen by the designer |
| Fermi level | At E_i, near mid-gap | Shifted toward E_c (n-type) or E_v (p-type) |
| Conductivity | Low (σ ≈ 3×10⁻⁶ S/cm for Si) | Much higher, set by doping |

The two are linked by the mass-action law **np = n_i²**: doping increases one carrier type and decreases the other so that their product equals the intrinsic value squared.

### Q29. Silicon has an intrinsic carrier concentration of approximately 1.0 × 10¹⁰ cm⁻³ at a specified temperature. If the electron and hole concentrations are equal, determine the electron and hole concentrations.

If n = p, the semiconductor is intrinsic (undoped, or exactly compensated). From the mass-action law:

    n · p = n_i²   and   n = p   ⇒   n² = n_i²   ⇒   n = n_i

**n = p = n_i = 1.0×10¹⁰ cm⁻³**

Check: n·p = (1.0×10¹⁰)² = 1.0×10²⁰ cm⁻⁶ = n_i². ✓

At this concentration, using μ_n = 1350 and μ_p = 480 cm²/V·s, the intrinsic conductivity would be σ = qn_i(μ_n + μ_p) = 1.602×10⁻¹⁹ × 10¹⁰ × 1830 = 2.9×10⁻⁶ S/cm, i.e. ρ ≈ 3.4×10⁵ Ω·cm.

### Q34. An n-type semiconductor has a donor concentration of 5 × 10¹⁶ cm⁻³. Assuming complete ionization, determine the approximate majority-carrier concentration.

With complete ionisation and N_D ≫ n_i (5×10¹⁶ ≫ 10¹⁰), every donor contributes one electron:

    n₀ ≈ N_D = 5 × 10¹⁶ cm⁻³

**Majority-carrier (electron) concentration ≈ 5×10¹⁶ cm⁻³.**

Additional results (assuming silicon at 300 K, n_i = 1×10¹⁰ cm⁻³):

    Minority holes:  p₀ = n_i²/n₀ = (10¹⁰)² / (5×10¹⁶) = 2×10³ cm⁻³

    Fermi level:  E_F − E_i = kT ln(n₀/n_i) = 0.0259 × ln(5×10⁶) = 0.0259 × 15.42 = 0.40 eV above E_i

    Conductivity:  σ ≈ q n₀ μ_n = 1.602×10⁻¹⁹ × 5×10¹⁶ × 1350 ≈ 10.8 S/cm  (ρ ≈ 0.093 Ω·cm)

The thermal contribution n_i is negligible, which is why the majority-carrier density is simply the donor density. (Mobility falls at this doping to about 1000 cm²/V·s, so the real σ is nearer 8 S/cm.)
