# Module 08 — Quantum Mechanics and Energy Bands

Lecture note §5, extended for Q22–Q26. Classical physics cannot explain why some solids conduct and others do not. Quantum mechanics, applied to an electron in a periodic crystal, produces bands and gaps directly.

## 8.1 Why quantum mechanics

Three results from early quantum theory are needed:

- **Energy is quantised.** Electrons bound in atoms occupy discrete levels (Planck, Bohr). A photon has energy E = hν.
- **Wave–particle duality.** An electron of momentum p behaves as a wave of wavelength λ = h/p (de Broglie). Write p = ħk, where k = 2π/λ is the wave vector.
- **Uncertainty principle.** Δx·Δp ≥ ħ/2: an electron's position and momentum cannot both be exact, so we describe it by a probability wave ψ.

Constants: h = 6.626×10⁻³⁴ J·s, ħ = h/2π = 1.055×10⁻³⁴ J·s, m₀ = 9.11×10⁻³¹ kg.

## 8.2 The Schrödinger equation

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

## 8.3 From atoms to bands

Bring N identical atoms together. When far apart, each has the same discrete levels. As they approach, their outer wave functions overlap and, by the Pauli exclusion principle, each level must **split into N closely spaced levels**. With N ≈ 5×10²² cm⁻³, these form an almost continuous **band**.

In Si, the 3s and 3p levels (4 electrons per atom, 8 states) hybridise. At the actual spacing they split into a lower band with 4N states (the **valence band**, completely full at 0 K) and an upper band with 4N states (the **conduction band**, empty at 0 K), separated by the gap E_g = 1.12 eV.

## 8.4 Bloch's theorem

In a perfectly periodic potential V(x + a) = V(x), the solutions take the form

    ψ_k(x) = u_k(x) e^{ikx},   with u_k(x + a) = u_k(x)

A plane wave modulated by a function with the lattice period. An electron in a perfect crystal is therefore **not scattered** by the lattice itself; only departures from periodicity scatter it.

## 8.5 The Kronig–Penney model

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

## 8.6 E–k diagrams and effective mass

Plotting E against k gives the band structure. Near a band extremum, E is approximately parabolic, and the electron behaves as a free particle with an **effective mass**:

    1/m∗ = (1/ħ²) d²E/dk²

A strongly curved band means small m∗ and high mobility. Values: Si m_n∗ ≈ 1.08m₀ (density-of-states), m_p∗ ≈ 0.56m₀; GaAs m_n∗ = 0.067m₀. Near the top of the valence band the curvature is negative: a missing electron there behaves as a positive particle with positive mass, the **hole**.

## 8.7 Valence band, conduction band and gap

- **Valence band:** highest band that is completely filled at 0 K. Its top is E_v. Electrons here are in the covalent bonds. Holes move in this band.
- **Conduction band:** next higher band, empty at 0 K. Its bottom is E_c. Electrons here are free to move and conduct.
- **Forbidden gap:** E_g = E_c − E_v. No electron states exist here in a perfect crystal; impurities and defects can add states inside it.

E_g decreases slightly with temperature (Varshni relation, E_g(T) = E_g(0) − αT²/(T + β)): for Si, 1.17 eV at 0 K, 1.12 eV at 300 K.

## 8.8 Direct and indirect gaps

@fig figures/ek.svg | In a direct-gap material (GaAs) the conduction-band minimum and valence-band maximum are at the same k. In an indirect-gap material (Si) they are at different k, so a phonon must supply the momentum difference.

A photon has very little momentum (k_photon ≈ 10⁵ cm⁻¹ compared with a zone-edge k ≈ 10⁸ cm⁻¹), so an optical transition is essentially vertical on the E–k diagram.

- **Direct gap:** the transition is vertical and needs only a photon. Radiative recombination is fast (ns) and efficient. Strong absorption above E_g. GaAs, InP, GaN, InGaAs.
- **Indirect gap:** the electron must also change momentum, which requires a **phonon** (lattice vibration) to be absorbed or emitted at the same time. This three-particle process is unlikely, so radiative recombination is slow and inefficient; energy is lost as heat through traps instead. Si, Ge, GaP, AlAs.

The emission wavelength of a band-to-band transition:

    λ (μm) = 1.24 / E_g (eV)

GaAs: 1.24/1.42 = 0.873 μm (near-infrared). Si: 1.24/1.12 = 1.11 μm, which is also why Si photodetectors stop responding above about 1.1 μm.

---

## Exam questions solved

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
