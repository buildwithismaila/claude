# Week 4 — Energy Bands and Carrier Concentrations
<!-- group: Module 2 · Energy Bands & Carrier Statistics -->

**Plan:** quantum-mechanics foundations (Schrödinger equation overview, Kronig–Penney model); energy band gaps, allowed and forbidden states; intrinsic and extrinsic carrier concentrations.

## The big picture

In Week 1 we simply stated that a solid has a **valence band**, a **conduction band** and a **gap** between them. This week explains **why**. The answer needs one idea from quantum mechanics: **an electron behaves like a wave, and a wave trapped in a region can only vibrate in certain ways**. In a single atom that gives sharp energy levels. In a crystal, where the electron wave runs through a regular row of atoms, it gives broad bands of allowed energies separated by forbidden gaps.

You do not need to solve hard equations for this course. You need to understand three steps:

1. Electrons are waves, described by the Schrödinger equation.
2. Trapped waves have only certain allowed energies.
3. A periodic crystal turns those allowed energies into bands with gaps (the Kronig–Penney model shows this).

Then Part C uses the bands to count the carriers.

## Part A: Quantum-mechanics foundations

### Why classical physics is not enough

Classical physics treats an electron as a tiny ball. That picture cannot explain why copper conducts and glass does not, or why an atom emits light only at certain colours. Three ideas from early quantum theory fix this:

- **Energy comes in packets (quanta).** Light of frequency ν comes in photons of energy E = hν. Electrons in atoms can only have certain energies.
- **Particles behave as waves.** An electron with momentum p behaves as a wave of wavelength λ = h/p (de Broglie). We often write p = ħk, where k = 2π/λ is the **wave vector**: k is just "how many waves per unit length", and it measures the electron's momentum.
- **Uncertainty.** We cannot know an electron's position and momentum exactly at the same time. So instead of a definite position we describe it by a **wave function** ψ, and |ψ|² tells us where it is likely to be found.

Constants: h = 6.626×10⁻³⁴ J·s, ħ = h/2π = 1.055×10⁻³⁴ J·s, electron mass m₀ = 9.11×10⁻³¹ kg.

### The Schrödinger equation

The time-independent Schrödinger equation (in one dimension) is

    −(ħ²/2m) d²ψ/dx² + V(x) ψ = E ψ

Read it as an energy balance: **kinetic energy + potential energy = total energy**.

| Term | Meaning |
|---|---|
| ψ(x) | the **wave function**. ψ itself is not measurable, but \|ψ(x)\|² dx is the probability of finding the electron between x and x + dx |
| −(ħ²/2m) d²ψ/dx² | the **kinetic energy** term. d²ψ/dx² measures how sharply the wave curves: a more tightly wiggling wave means more kinetic energy |
| V(x) ψ | the **potential energy** term. V(x) is the potential energy at each point (for example the pull of the atomic nuclei) |
| E | the **total energy**, a constant. The equation only has sensible solutions for certain values of E: that is how quantisation appears |

The wave function must be finite, single-valued and smooth (continuous, with a continuous slope), and the total probability must be 1.

### Two simple cases that explain everything

**A free electron** (no forces, V = 0). The solution is a travelling wave, ψ = Ae^{ikx}, with energy

    E = ħ²k²/2m

Any energy is allowed. The graph of E against k is a smooth parabola. This is the starting point for electrons in a solid.

**An electron in a box** of width L with walls it cannot pass. The wave must be zero at both walls, just as a guitar string is fixed at both ends. So only whole numbers of half-waves fit, and only certain energies are allowed:

    E_n = n²π²ħ²/2mL²,   n = 1, 2, 3, …

> **In plain words.** A guitar string can only play certain notes, because only certain wavelengths fit between its fixed ends. An electron trapped in a region is the same: only certain wavelengths fit, so only certain energies are allowed. That is what "quantised energy levels" means.

### From atoms to bands

One isolated silicon atom has sharp energy levels (1s, 2s, 2p, 3s, 3p). Now bring two atoms close together. Their outer wave functions overlap, and each level **splits into two** slightly different levels. (Two identical pendulums joined by a spring do the same: instead of one frequency they now have two, swinging together and swinging opposite.)

Bring **N atoms** together and each level splits into **N levels**. A crystal has about 5×10²² atoms per cm³, so each level splits into so many closely spaced levels that they form a practically continuous **band**. Between bands are ranges of energy where there are **no** levels at all: the **forbidden gaps**.

In silicon, the outer 3s and 3p levels (4 electrons per atom) mix and split into two bands:

- a lower band with room for 4 electrons per atom: the **valence band**. Silicon has exactly 4 outer electrons per atom, so this band is **completely full** at 0 K;
- an upper band, also with room for 4 per atom: the **conduction band**, **empty** at 0 K;
- separated by the band gap **E_g = 1.12 eV**.

### Bloch's theorem

In a perfect crystal the potential energy repeats with the spacing of the atoms a: V(x + a) = V(x). Bloch showed that the electron wave in such a crystal is

    ψ_k(x) = u_k(x) e^{ikx},   with u_k(x + a) = u_k(x)

A travelling wave (e^{ikx}) multiplied by a pattern that repeats from atom to atom (u_k). The important consequence: **an electron in a perfect crystal travels without being scattered by the atoms**. The atoms are not obstacles; they just shape the wave. Only imperfections (vibrations, impurities, defects) scatter electrons. This is why carriers in a crystal can move so freely (Week 7).

### The Kronig–Penney model: how a periodic crystal makes bands and gaps

The real potential inside a crystal is complicated. Kronig and Penney (1931) replaced it with the simplest repeating potential that can be solved exactly: a row of **rectangular wells and barriers**.

- Each **well** (width a, V = 0) represents the region near an atom, where the electron is attracted.
- Each **barrier** (height V₀, width b) represents the region between atoms.
- The pattern repeats forever with period a + b.

**What they did:**

1. Solved the Schrödinger equation inside a well (where the solution oscillates) and inside a barrier (where it decays).
2. Joined the pieces smoothly at every edge (ψ and dψ/dx continuous).
3. Applied Bloch's theorem (the solution must repeat, up to a phase factor, from one period to the next).
4. Simplified by making the barriers very thin and very high.

**The result** is one condition that the energy must satisfy:

    P · sin(αa)/(αa) + cos(αa) = cos(ka)

    α = √(2mE)/ħ,     P = m V₀ b a / ħ²

| Symbol | Meaning |
|---|---|
| α | depends on the electron energy E: larger E, larger α |
| a | well width (the atomic spacing) |
| k | the electron's wave vector (momentum) |
| P | barrier strength: how strongly the electron is held by each atom |

**How to read it: the key step.** The right-hand side, cos(ka), is a cosine. **A cosine can only be between −1 and +1.** The left-hand side depends on the energy through α. So:

- for energies where the left-hand side is **between −1 and +1**, there is a k that satisfies the equation: these energies are **allowed**;
- for energies where the left-hand side is **greater than +1 or less than −1**, no real k works: these energies are **forbidden**.

Plot the left-hand side against αa (i.e. against energy). It wiggles like a fading cosine, starting above +1 and repeatedly overshooting the ±1 lines. Every time it is inside the ±1 strip you have a **band**; every time it pokes outside you have a **gap**.

@fig figures/kronig-penney.svg | The Kronig–Penney condition plotted against αa for P = 3π/2. Shaded strips are the energies where the curve stays between −1 and +1: the allowed bands. Where the curve goes outside ±1 there are no solutions: the forbidden gaps.

**What the model teaches:**

1. The energy spectrum is a series of **allowed bands separated by forbidden gaps**.
2. The band edges occur at ka = nπ, i.e. k = ±nπ/a, the **Brillouin-zone boundaries**. Physically, at these wavelengths the electron wave reflects off the rows of atoms (Bragg reflection), forming standing waves, which split the energies and open a gap.
3. Bands get **wider** at higher energy (the curve's wiggles fade, so it spends longer inside ±1).
4. If the atoms hold their electrons very tightly (P → ∞), the bands shrink to the sharp levels of single atoms.
5. If the barriers vanish (P → 0), the gaps close and the electron is free: E = ħ²k²/2m.

> **In plain words.** A wave running through a regular row of obstacles is fine at most wavelengths, but at certain wavelengths the reflections from every row add up and the wave cannot travel. Those wavelengths correspond to the forbidden energies: the band gaps.

## Part B: Band gaps, allowed and forbidden states

### E–k diagrams and effective mass

The **band structure** of a material is a graph of the allowed energies E against the wave vector k. Near the bottom of the conduction band (and the top of the valence band) the curve looks like a parabola, just like a free electron's E = ħ²k²/2m, but with a different curvature. We describe that curvature by an **effective mass** m∗:

    1/m∗ = (1/ħ²) d²E/dk²

The electron then responds to forces **as if** it were a free particle of mass m∗. The effect of all the crystal's atoms is packed into this one number.

- A **sharply curved** band means small m∗: a light, fast, high-mobility carrier (GaAs electrons, m∗ = 0.067m₀).
- A **flatter** band means large m∗: a heavy, slow carrier (Si holes, about 0.56m₀).

Near the **top** of the valence band the curve bends downward. An electron there would have negative mass. It is simpler to describe the **missing** electron instead: it behaves as a positive particle with positive mass, the **hole**.

### Valence band, conduction band and forbidden gap

- **Valence band:** the highest band that is completely full at 0 K. Its top is E_v. Its electrons are the bonding electrons. A full band cannot carry current (for every electron moving one way there is one moving the other), but a band with a few **holes** can.
- **Conduction band:** the next band up, empty at 0 K. Its bottom is E_c. Electrons here move freely and carry current.
- **Forbidden gap:** E_g = E_c − E_v. In a perfect crystal there are no states here at all. Impurities and defects can add a few states inside it (donor, acceptor and trap levels).

The gap shrinks slightly with temperature: for Si, 1.17 eV at 0 K and 1.12 eV at 300 K.

### Direct and indirect band gaps

@fig figures/ek.svg | In a direct-gap material (GaAs) the bottom of the conduction band sits directly above the top of the valence band in k. In an indirect-gap material (Si) they are at different k, so an electron dropping across the gap must also change its momentum.

When an electron falls from the conduction band to the valence band it must lose energy **and** keep momentum balanced. A photon carries plenty of energy but almost no momentum. So on an E–k diagram, a photon can only make **vertical** jumps.

- **Direct gap** (GaAs, InP, GaN): the conduction-band minimum is directly above the valence-band maximum. The electron can drop straight down and give out a photon. Light emission is fast and efficient: **LEDs and lasers**.
- **Indirect gap** (Si, Ge): the minimum is at a different k. To drop across, the electron must also get rid of momentum, which needs a **phonon** (a lattice vibration) at the same instant. That is unlikely, so the electron usually loses its energy as heat instead. **Silicon is a poor light emitter.**

The wavelength of light from a band-to-band transition is

    λ (μm) = 1.24 / E_g (eV)

GaAs: 1.24/1.42 = 0.87 μm (near infrared). Si: 1.24/1.12 = 1.11 μm, which is also the longest wavelength a silicon photodetector can absorb.

## Part C: Intrinsic and extrinsic carrier concentrations

Now that we have bands, we can count carriers. The full method (Fermi–Dirac statistics, density of states) is Week 5. Here are the results you need this week.

### The two key equations

The number of electrons in the conduction band and holes in the valence band depend on how far the **Fermi level** E_F is from each band edge:

    n = N_c e^{−(E_c − E_F)/kT},       p = N_v e^{−(E_F − E_v)/kT}

N_c and N_v are the **effective densities of states** (Si at 300 K: 2.8×10¹⁹ and 1.04×10¹⁹ cm⁻³). The closer E_F is to E_c, the more electrons; the closer to E_v, the more holes.

### Intrinsic semiconductor

In pure silicon every free electron came from a broken bond, which also left a hole, so n = p = n_i. Multiply the two equations above; E_F cancels:

    n p = N_c N_v e^{−(E_c − E_v)/kT} = N_c N_v e^{−E_g/kT}

With n = p = n_i:

    n_i = √(N_c N_v) e^{−E_g/2kT}

For Si at 300 K, n_i ≈ 1×10¹⁰ cm⁻³. The Fermi level of an intrinsic semiconductor, E_i, is almost exactly at **mid-gap**.

**What controls n_i:** the band gap (exponentially: wider gap, far fewer carriers) and temperature (exponentially: hotter, far more carriers). Ge (0.66 eV) has n_i = 2.4×10¹³; GaAs (1.42 eV) has only about 2×10⁶ cm⁻³.

### The mass-action law

Because E_F cancelled, the product is the same whether or not the material is doped:

    n p = n_i²

### Extrinsic (doped) semiconductor

With full ionisation and doping well above n_i:

- **n-type:** n ≈ N_D, p = n_i²/N_D.
- **p-type:** p ≈ N_A, n = n_i²/N_A.
- **Both present (compensation):** use the net doping. The exact result from charge neutrality is

    n = (N_D − N_A)/2 + √( ((N_D − N_A)/2)² + n_i² )

**Example.** Si with N_D = 10¹⁶ cm⁻³: n = 10¹⁶, p = 10²⁰/10¹⁶ = 10⁴ cm⁻³. Doping raised the electrons by 10⁶ above n_i and lowered the holes by 10⁶.

**Temperature regions (n-type):** at very low temperature the donors are not all ionised (**freeze-out**, n < N_D); over the normal range n ≈ N_D (**extrinsic**); at high temperature n_i overtakes N_D and the material behaves as intrinsic (**intrinsic region**). Week 5 works through these in detail.

## Key points of Week 4

- Electrons are waves; the Schrödinger equation is kinetic + potential = total energy, and only certain energies give acceptable waves.
- Bringing N atoms together splits each level into N levels, forming bands; between them are forbidden gaps.
- Kronig–Penney: P sin(αa)/(αa) + cos(αa) = cos(ka). Energies where the left side is between ±1 are allowed (bands); elsewhere forbidden (gaps).
- Effective mass m∗ describes the band curvature. A missing electron near the top of the valence band acts as a positive hole.
- Direct gap: photon emission is efficient (GaAs). Indirect gap: a phonon is needed, so emission is poor (Si). λ = 1.24/E_g μm.
- n_i = √(N_cN_v)e^{−E_g/2kT}; np = n_i²; n ≈ N_D in n-type, p ≈ N_A in p-type.

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
