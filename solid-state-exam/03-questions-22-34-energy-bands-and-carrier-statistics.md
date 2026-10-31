# Questions 22–34 — Energy Bands and Carrier Statistics
<!-- group: The 50 questions, answered -->

Module 2: the quantum model of electrons in a crystal, how energy bands form, direct and indirect gaps, intrinsic and extrinsic carriers, Fermi–Dirac statistics, the density of states and the Fermi level. Each question stands on its own: its key terms are defined with it, so you can start anywhere.

## Symbols and abbreviations used on this page

Every symbol, constant and abbreviation on this page is listed here, even if another page already defined it, so you can study this page on its own.

**Constants and units**

| Symbol | Meaning | Units / typical value |
|---|---|---|
| q | Magnitude of the electronic charge | 1.6×10⁻¹⁹ C |
| k | Boltzmann constant | 8.617×10⁻⁵ eV/K = 1.381×10⁻²³ J/K |
| kT | Thermal energy | 0.0259 eV (often 0.02585 eV) at 300 K |
| T | Absolute temperature | kelvin (K); room temperature = 300 K |
| h | Planck constant | 6.626×10⁻³⁴ J·s |
| ħ | Reduced Planck constant, h/2π | 1.055×10⁻³⁴ J·s |
| m₀ | Free-electron mass | 9.11×10⁻³¹ kg |
| eV | Electron-volt, a unit of energy | 1 eV = 1.6×10⁻¹⁹ J |
| μm | Micrometre (micron) | 1 μm = 10⁻⁶ m |

**Symbols**

| Symbol | Meaning | Units / typical value |
|---|---|---|
| E_c (E_C) | Energy of the bottom of the conduction band | eV |
| E_v (E_V) | Energy of the top of the valence band | eV |
| E_g | Band-gap energy, E_c − E_v | eV; Si 1.12, Ge 0.66, GaAs 1.42 at 300 K |
| E_F | Fermi level: the energy at which a state has a 50 % chance of being occupied | eV |
| E_i | Intrinsic Fermi level, close to mid-gap | eV |
| E_D | Donor energy level, just below E_c | eV; E_c − E_D ≈ 0.045 eV for P in Si |
| E_A | Acceptor energy level, just above E_v | eV; E_A − E_v ≈ 0.045 eV for B in Si |
| E_n | Allowed energy of level n of a particle in a box | J or eV |
| f(E) | Fermi–Dirac function: probability that a state at energy E is occupied | dimensionless, 0 to 1 |
| g(E), g_c, g_v | Density of states: allowed states per unit energy per unit volume | states/(eV·m³) |
| N_c | Effective density of states in the conduction band | m⁻³; Si 2.8×10²⁵ at 300 K |
| N_v | Effective density of states in the valence band | m⁻³; Si 1.04×10²⁵ at 300 K |
| n | Electron concentration (free electrons per m³) | m⁻³ |
| p | Hole concentration (holes per m³) | m⁻³ |
| n_i | Intrinsic carrier concentration (n = p = n_i in pure material) | m⁻³; Si ≈ 1×10¹⁶ at 300 K |
| n₀, p₀ | Equilibrium electron and hole concentrations | m⁻³ |
| N_D | Donor concentration | m⁻³ |
| N_A | Acceptor concentration | m⁻³ |
| m∗, m_n∗, m_p∗ | Effective mass of electrons or holes | kg, or as a multiple of m₀ |
| ψ | Wave function (\|ψ\|² is the probability density) | — |
| V(x) | Potential energy in the Schrödinger equation | J or eV |
| k (wave vector) | Wave vector, 2π/λ; measures the electron's momentum, p = ħk | m⁻¹ |
| α (Kronig–Penney) | √(2mE)/ħ, set by the electron energy | m⁻¹ |
| P (Kronig–Penney) | Barrier strength mV₀ba/ħ² | dimensionless |
| V₀ | Height of a potential barrier | J or eV |
| λ | Wavelength | μm or nm; λ(μm) = 1.24/E(eV) |
| ν, hν | Frequency of light, and photon energy | Hz; eV |
| a | Lattice constant: edge length of the cubic unit cell | nm; Si 0.543, Ge and GaAs 0.565 |
| f (growth) | Fraction of the melt already solidified | 0 to 1 |
| μ, μ_n, μ_p | Mobility: drift velocity per unit field (electrons, holes) | m²/(V·s); Si μ_n 0.135, μ_p 0.048 |
| σ | Conductivity, q(nμ_n + pμ_p) (in Week 8, σ is also a capture cross-section) | S/m (siemens per metre) |
| V, V_a | Applied voltage (positive for forward bias) | V |
| α | Common-base current gain, I_C/I_E | dimensionless; 0.98–0.999 |
| β | Common-emitter current gain, I_C/I_B (also h_FE) | dimensionless; 50–500 |
| λ_max | Longest wavelength a material absorbs, 1.24/E_g (μm, E_g in eV) | μm |
| ψ_k(x), u_k(x) | Bloch wavefunction of an electron, and its part that repeats with the lattice | — |

**Abbreviations**

| Abbreviation | Meaning |
|---|---|
| Si | Silicon |
| Ge | Germanium |
| GaAs | Gallium arsenide |
| GaN | Gallium nitride |
| InP | Indium phosphide |
| GaP | Gallium phosphide |
| SiO₂ | Silicon dioxide (silica), the oxide insulator |
| CB | Conduction band |
| VB | Valence band |
| MOS | Metal–oxide–semiconductor |
| IC | Integrated circuit |
| LED | Light-emitting diode |
| n⁺ | Very heavily doped n-type (similarly p⁺) |


## Questions on this page

| Q | Question |
|---|---|
| 22 | Explain the basic assumptions of the quantum mechanical model of electrons in a semiconductor. |
| 23 | State the time-independent Schrödinger equation and explain the physical meaning of its terms. |
| 24 | Explain the basic principle of the Kronig-Penney model and how it leads to the formation of energy bands. |
| 25 | Distinguish between valence band, conduction band, and forbidden energy gap. |
| 26 | Explain the difference between a direct band-gap and an indirect band-gap semiconductor. |
| 27 | What is meant by an intrinsic semiconductor? Derive the expression for intrinsic carrier concentration. |
| 28 | Explain the difference between intrinsic and extrinsic carrier concentrations. |
| 29 | Silicon has an intrinsic carrier concentration of approximately 1.0 × 10¹⁰ cm⁻³ at a specified temperature. If the electron and hole concentrations are equal, determine the electron and hole concentrations. |
| 30 | Explain the Fermi-Dirac distribution function and its significance in semiconductor physics. |
| 31 | Write the Fermi-Dirac distribution equation and explain what happens to the distribution at absolute zero. |
| 32 | Define the density of states in a semiconductor and explain its importance in determining carrier concentration. |
| 33 | Explain how the Fermi energy level changes with doping in n-type and p-type semiconductors. |
| 34 | An n-type semiconductor has a donor concentration of 5 × 10¹⁶ cm⁻³. Assuming complete ionization, determine the approximate majority-carrier concentration. |

## Model answers

### Q22. Explain the basic assumptions of the quantum mechanical model of electrons in a semiconductor.

> **Question type:** Explanation · **Topic:** quantum model of electrons in a crystal · **Full notes:** Week 4 (Energy Bands and Carrier Concentrations)

**What the examiner wants.** "Explain the assumptions" means list each simplifying assumption the model makes AND say in a sentence why it is made or what it allows. A full answer names about six assumptions, from the wave nature of the electron to the statistics that fill the bands, and ends by saying what the model predicts (energy bands).

**Key terms.**

- **Wave function (ψ):** the mathematical wave that describes an electron; |ψ|² gives the probability of finding it at a point.
- **Schrödinger equation:** the wave equation whose solutions give the allowed wave functions and energies of an electron.
- **Lattice:** the regular, repeating arrangement of atoms in a crystal; its repeat distance is the lattice period a.
- **Periodic potential:** a potential energy V(x) that repeats with the lattice period, V(x + a) = V(x).
- **Phonon:** a quantum (packet) of lattice vibration.
- **Effective mass (m∗):** the mass a carrier appears to have when pushed by a force inside the crystal.
- **Fermi–Dirac distribution f(E):** the probability that an electron state of energy E is occupied in thermal equilibrium.

**Model answer.**

A crystal contains about 5×10²⁸ atoms per m³ and even more electrons, all interacting. This many-body problem cannot be solved exactly, so the quantum mechanical model makes the following assumptions.

**1. Electrons behave as waves.** Each electron is described by a wave function ψ that obeys the Schrödinger equation. Its momentum is written p = ħk, where k = 2π/λ is the wave vector and ħ = h/2π = 1.055×10⁻³⁴ J·s. This replaces the classical "small ball" picture, which cannot explain why some solids conduct and others do not.

**2. The nuclei are fixed (adiabatic or Born–Oppenheimer approximation).** A silicon nucleus is about 50 000 times heavier than an electron and moves far more slowly, so the ion cores are treated as stationary at their lattice sites. Their vibrations (phonons) are added back later as a small disturbance that scatters carriers.

**3. The crystal is perfect and infinite.** The ion cores form a perfectly regular lattice that extends forever, so the potential energy seen by an electron is exactly periodic:

    V(x + a) = V(x)

Where:

- V(x) = potential energy of an electron at position x (eV)
- a = lattice period, the spacing of the repeating unit (m; for Si a = 0.543 nm)

Surfaces, impurities and defects are ignored at first and treated separately later (as donor, acceptor or trap levels).

**4. Each electron moves independently (one-electron approximation).** Instead of tracking every electron–electron repulsion, each electron is assumed to move in an *average* periodic potential created by all the ion cores and all the other electrons. The many-body problem becomes a single-particle problem that can be solved.

**5. Pauli exclusion principle.** Each quantum state (one value of k and one spin) can hold at most one electron. The states are therefore filled from the lowest energy upwards, which is why a band can be "full" or "empty".

**6. Thermal-equilibrium statistics.** At temperature T the electrons are shared among the available states according to the Fermi–Dirac function f(E). This decides how many electrons sit in the conduction band and how many holes are left in the valence band.

**7. Effective-mass approximation.** Near the edge of a band, an electron (or hole) responds to an applied force as if it were a free particle with an effective mass m∗. The whole effect of the crystal potential is packed into this one number, so device equations can treat carriers as simple particles.

**What the assumptions lead to.** Assumptions 3 and 4 give **Bloch's theorem**: the electron wave in a periodic potential is a travelling wave multiplied by a function with the period of the lattice, ψ_k(x) = u_k(x)e^{ikx}. Solving the Schrödinger equation with this form (for example in the Kronig–Penney model) gives **allowed energy bands separated by forbidden gaps**, the basis of all semiconductor physics.

**Marking checklist.** The points a marker looks for. Tick each one off in your own answer:

- ✓ electron described by a wave function ψ obeying the Schrödinger equation
- ✓ nuclei treated as fixed (Born–Oppenheimer); vibrations added later as phonons
- ✓ perfect, infinite periodic lattice with V(x + a) = V(x)
- ✓ one-electron (independent-electron, average-potential) approximation
- ✓ Pauli exclusion principle fills states from the bottom up
- ✓ Fermi–Dirac statistics in thermal equilibrium
- ✓ effective-mass approximation near band edges
- ✓ conclusion: Bloch waves and energy bands with gaps

**Common mistakes.**

- Listing the assumptions with no explanation. The command word is "explain": add one sentence on why each is made.
- Calling Bloch's theorem an assumption. It is a *result* of assuming a periodic potential; say so.
- Confusing "periodic potential" with "periodic wave function". The potential repeats exactly; the Bloch wave function repeats only up to a phase factor e^{ika}.

**Remember it.** "Wave, Fixed, Perfect, Alone, Pauli, Fermi, Effective": the electron is a wave, nuclei are fixed, the crystal is perfect, each electron is alone in an average field, Pauli fills the states, Fermi sets the occupation, and m∗ hides the crystal.

**Try a variant.** Why does an electron in a perfect crystal travel without being scattered by the atoms, and what does scatter it? *Answer:* in a perfectly periodic potential the solutions are Bloch waves, ψ_k = u_k(x)e^{ikx}, which are travelling waves that extend through the whole crystal; the atoms only shape the wave (through u_k) and do not deflect it. Scattering comes only from departures from perfect periodicity: lattice vibrations (phonons), ionised impurities, defects and surfaces. This is why mobility falls when temperature or doping rises.

---

### Q23. State the time-independent Schrödinger equation and explain the physical meaning of its terms.

> **Question type:** Statement and explanation · **Topic:** Schrödinger equation · **Full notes:** Week 4 (Energy Bands and Carrier Concentrations)

**What the examiner wants.** Write the equation correctly (one-dimensional form is enough, the 3-D form earns credit), then explain every term: the wave function, the kinetic-energy term, the potential-energy term and the energy E. Mention the conditions ψ must satisfy and how quantisation follows.

**Key terms.**

- **Wave function (ψ):** the amplitude of the electron's probability wave; |ψ|² dx is the probability of finding it between x and x + dx.
- **Stationary state:** a state whose energy and probability distribution do not change with time.
- **Hamiltonian (Ĥ):** the total-energy operator, kinetic plus potential.
- **Eigenvalue:** an allowed value of E for which the equation has an acceptable solution.
- **Reduced Planck constant (ħ):** ħ = h/2π = 1.055×10⁻³⁴ J·s.

**Model answer.**

**The equation.** In one dimension, for an electron of mass m in a potential energy V(x) that does not change with time:

    −(ħ²/2m) d²ψ(x)/dx² + V(x) ψ(x) = E ψ(x)

Where:

- ψ(x) = wave function of the electron (for a 1-D problem its unit is m^{−1/2})
- ħ = reduced Planck constant, h/2π = 1.055×10⁻³⁴ J·s
- m = electron mass, 9.11×10⁻³¹ kg (in a crystal, the effective mass m∗)
- x = position (m)
- V(x) = potential energy of the electron at x (J)
- E = total energy of the electron (J)

In three dimensions, −(ħ²/2m)∇²ψ(r) + V(r)ψ(r) = Eψ(r), written compactly as **Ĥψ = Eψ**.

**Physical meaning of each term.** The equation is an energy balance: **kinetic energy + potential energy = total energy**.

- **ψ(x), the wave function.** ψ itself cannot be measured. Its square, |ψ(x)|² dx, is the probability of finding the electron between x and x + dx. Where |ψ|² is large, the electron is likely to be found.
- **−(ħ²/2m) d²ψ/dx², the kinetic-energy term.** It comes from the classical kinetic energy p²/2m with the momentum replaced by the operator p = −iħ d/dx. The second derivative measures how sharply ψ curves: a wave that wiggles tightly (short wavelength) has high momentum and high kinetic energy.
- **V(x)ψ, the potential-energy term.** V(x) describes the forces acting on the electron: the attraction of the ion cores in a crystal, a barrier, or a well. In a crystal V(x) is periodic.
- **E, the total energy.** A constant, because the equation describes stationary states. Acceptable solutions exist only for certain values of E, the **eigenvalues**. This is how energy quantisation (and, in a crystal, energy bands) appears.
- **The left-hand side as a whole** is the Hamiltonian operator Ĥ acting on ψ.

**Conditions on ψ.** ψ must be finite, single-valued and continuous, with a continuous slope dψ/dx wherever V is finite, and normalised, ∫|ψ|² dx = 1 (the electron is certainly somewhere). These conditions are what pick out the allowed energies.

**Link to time.** The full wave function is Ψ(x, t) = ψ(x) e^{−iEt/ħ}. Because |e^{−iEt/ħ}|² = 1, the probability |Ψ|² does not change with time, which is why these are called stationary states.

**Two quick illustrations.**

- Free electron (V = 0): ψ = Ae^{ikx} and E = ħ²k²/2m. Any energy is allowed.
- Electron in a box of width L with impassable walls: ψ must be zero at both walls, so only E_n = n²π²ħ²/2mL² (n = 1, 2, 3 …) are allowed. Confinement produces quantisation.

**Marking checklist.** The points a marker looks for. Tick each one off in your own answer:

- ✓ correct equation −(ħ²/2m)d²ψ/dx² + Vψ = Eψ (and/or Ĥψ = Eψ)
- ✓ ψ explained, with |ψ|² as probability density
- ✓ first term identified as kinetic energy, linked to p = −iħ d/dx
- ✓ V(x)ψ identified as potential energy, with an example (periodic crystal potential)
- ✓ E is the constant total energy; only eigenvalues allowed, giving quantisation
- ✓ conditions on ψ (finite, continuous, normalised)
- ✓ "time-independent" explained: V independent of t, stationary states

**Common mistakes.**

- Dropping the minus sign or writing ħ²/m instead of ħ²/2m. Check by the free-electron result: ψ = e^{ikx} must give E = ħ²k²/2m.
- Saying ψ is the probability. It is |ψ|² that is the probability density.
- Writing E as a variable that changes with x. E is a single constant for each solution.

**Remember it.** "Curvature is kinetic, V is potential, E is the total": KE + PE = E, written for waves.

**Try a variant.** Find the lowest three energy levels of an electron confined in a one-dimensional box of width 1 nm. *Answer:* E_n = n²π²ħ²/2mL². E₁ = π² × (1.055×10⁻³⁴)² / (2 × 9.11×10⁻³¹ × (10⁻⁹)²) = 6.03×10⁻²⁰ J = **0.377 eV**; E₂ = 4E₁ = **1.51 eV**; E₃ = 9E₁ = **3.39 eV**. The levels are discrete and spread further apart as n rises; halving the box to 0.5 nm makes E₁ four times larger (1.51 eV).

---

### Q24. Explain the basic principle of the Kronig-Penney model and how it leads to the formation of energy bands.

> **Question type:** Explanation · **Topic:** Kronig–Penney model and energy bands · **Full notes:** Week 4 (Energy Bands and Carrier Concentrations)

**What the examiner wants.** Two parts: (1) the principle, meaning the idealised periodic potential the model uses and how it is solved (Schrödinger equation, boundary conditions, Bloch's theorem); (2) how bands follow, meaning the final condition and the argument that cos(ka) must lie between −1 and +1. A labelled sketch of the potential and of the condition plotted against αa earns marks.

**Key terms.**

- **Periodic potential:** a potential energy that repeats with the lattice period.
- **Bloch's theorem:** in a periodic potential the wave function satisfies ψ(x + L) = e^{ikL}ψ(x), where L is the period; it is a travelling wave times a periodic function.
- **Wave vector (k):** k = 2π/λ; it measures the electron's momentum, p = ħk.
- **Allowed band:** a range of energies for which electron states exist.
- **Forbidden gap:** a range of energies for which no electron states exist.
- **Brillouin-zone boundary:** the values k = ±nπ/a where the electron wave is Bragg-reflected by the lattice and band edges occur.
- **Barrier strength (P):** a dimensionless number measuring how tightly each atom holds its electrons.

**Model answer.**

**1. The principle.** The real potential in a crystal is complicated. Kronig and Penney (1931) replaced it with the simplest *periodic* potential that can be solved exactly: an infinite one-dimensional row of **rectangular wells and barriers**.

- Each **well** (V = 0, width a) represents the region near an ion core, where the electron is attracted.
- Each **barrier** (height V₀, width b) represents the region between ions.
- The pattern repeats with period a + b.

Sketch: a square-wave potential V(x) against x, wells of width a at V = 0, barriers of height V₀ and width b, period (a + b) marked.

**2. The method.**

- Solve the Schrödinger equation in a well, where the solution oscillates, with α² = 2mE/ħ².
- Solve it in a barrier, where the solution grows or decays exponentially, with β² = 2m(V₀ − E)/ħ².
- Make ψ and dψ/dx continuous at every edge.
- Apply Bloch's theorem: the solution in one period equals that in the next multiplied by e^{ik(a+b)}.
- Take the limit of very thin, very high barriers (b → 0, V₀ → ∞, with V₀b finite). A non-trivial solution then exists only if

    P · sin(αa)/(αa) + cos(αa) = cos(ka),     α = √(2mE)/ħ,     P = mV₀ba/ħ²

Where:

- α = a quantity that rises with electron energy E (m⁻¹)
- a = well width, effectively the atomic spacing (m)
- k = electron wave vector (m⁻¹)
- P = barrier strength (dimensionless)
- m = electron mass, 9.11×10⁻³¹ kg; E = electron energy (J)
- V₀ = barrier height (J); b = barrier width (m)
- ħ = reduced Planck constant, 1.055×10⁻³⁴ J·s

**3. How bands form.** The right-hand side, cos(ka), is a cosine, so for any real k it must lie **between −1 and +1**. The left-hand side, f(αa), depends only on the energy. Plot f(αa) against αa (that is, against energy):

- it starts at 1 + P (above +1) at αa = 0 and then oscillates like a fading cosine;
- where **−1 ≤ f(αa) ≤ +1**, a real k exists: these energies are **allowed bands**;
- where **|f(αa)| > 1**, no real k exists, so no electron wave can travel: these energies are **forbidden gaps**.

@fig figures/kronig-penney.svg | The left-hand side of the Kronig–Penney condition against αa for P = 3π/2. Shaded strips, where the curve stays between −1 and +1, are the allowed bands; where it leaves the strip there are no states and a forbidden gap appears.

Sketch: f(αa) against αa with horizontal lines at +1 and −1; shade the allowed bands and label the gaps.

**4. What the model shows.**

- The energy spectrum is a series of **allowed bands separated by forbidden gaps**.
- Band edges occur at ka = nπ, i.e. k = ±nπ/a, the **Brillouin-zone boundaries**. There the electron wave is Bragg-reflected by the rows of atoms, standing waves form, and the energy splits to open a gap.
- Allowed bands get **wider at higher energy**, because the sin(αa)/(αa) term fades as αa grows.
- If **P → ∞** (electrons tightly bound), each band shrinks to a single sharp level, as in an isolated atom.
- If **P → 0** (no barriers), the gaps close and the free-electron result E = ħ²k²/2m returns.

So the model shows that bands and gaps are a direct result of an electron wave moving through a periodic potential. Whether the highest occupied band is full or partly full, and how wide the gap above it is, then decides whether a solid is a metal, semiconductor or insulator.

**Marking checklist.** The points a marker looks for. Tick each one off in your own answer:

- ✓ periodic array of rectangular wells (width a) and barriers (V₀, width b) described or sketched
- ✓ Schrödinger equation solved in each region; continuity of ψ and dψ/dx
- ✓ Bloch's theorem applied
- ✓ final condition P sin(αa)/(αa) + cos(αa) = cos(ka), with α and P defined
- ✓ argument: |cos ka| ≤ 1, so only energies with |f(αa)| ≤ 1 are allowed
- ✓ sketch of f(αa) with ±1 lines, bands and gaps labelled
- ✓ gaps at k = nπ/a (Bragg reflection)
- ✓ limits P → ∞ (atomic levels) and P → 0 (free electron)

**Common mistakes.**

- Stating the equation without the key argument. The marks are in "cos(ka) cannot exceed 1 in magnitude, so some energies have no solution".
- Plotting f against k instead of against αa (energy). The allowed/forbidden test is made along the energy axis.
- Mixing up the limits: large P means tight binding (narrow bands), not free electrons.

**Remember it.** "A cosine can't beat one": wherever the left-hand side goes beyond ±1, there is a gap.

**Try a variant.** Explain what happens to the band structure in the Kronig–Penney model as the barrier strength P is increased from zero to a very large value. *Answer:* at P = 0 the condition becomes cos(αa) = cos(ka), so α = k and E = ħ²k²/2m for every energy: no gaps, free electron. As P increases, the curve f(αa) rises above +1 and below −1 over wider ranges, so the forbidden gaps widen and the allowed bands narrow. As P → ∞, the bands become allowed only where sin(αa) = 0, i.e. αa = nπ, giving discrete levels E_n = n²π²ħ²/2ma², the levels of an isolated well (electrons tightly bound to each atom).

---

### Q25. Distinguish between valence band, conduction band, and forbidden energy gap.

> **Question type:** Distinction · **Topic:** energy bands · **Full notes:** Week 4 (Energy Bands and Carrier Concentrations)

**What the examiner wants.** Define each of the three clearly, then contrast them point by point: occupancy at 0 K, band edge, role in conduction, carriers and typical values. A labelled band diagram and a comparison table secure full marks.

**Key terms.**

- **Energy band:** a range of closely spaced allowed electron energies, formed when the levels of many atoms split as they come together.
- **Electron-volt (eV):** the energy an electron gains across 1 V; 1 eV = 1.6×10⁻¹⁹ J.
- **E_c, E_v:** the energy of the bottom of the conduction band and the top of the valence band (eV).
- **Band gap (E_g):** E_g = E_c − E_v.
- **Hole:** an empty electron state in the valence band that behaves as a positive carrier.
- **Covalent bond:** a pair of electrons shared between neighbouring atoms (four per Si atom).

**Model answer.**

**How the bands arise.** An isolated silicon atom has sharp energy levels. When N atoms form a crystal, each level splits into N closely spaced levels, which merge into a band. In silicon the outer 3s and 3p levels (4 electrons per atom) split into a lower band and an upper band, each with room for 4 electrons per atom, separated by an energy range with no states.

**Valence band.** The highest energy band that is **completely filled** with electrons at absolute zero (0 K). Its top edge is E_v. Its electrons are the bonding electrons that hold the crystal together. A completely full band cannot carry current, because for every electron moving one way there is another moving the other way. When some electrons leave it, the empty states (holes) let the band conduct.

**Conduction band.** The next band above the valence band, **empty** at 0 K. Its bottom edge is E_c. An electron that reaches it is no longer tied to a bond and can move freely through the crystal, carrying current.

**Forbidden energy gap.** The range of energy between E_v and E_c in which a perfect crystal has **no allowed electron states**. Its width is

    E_g = E_c − E_v

Where:

- E_g = band-gap energy (eV): Si 1.12, Ge 0.66, GaAs 1.42 eV at 300 K
- E_c = bottom of the conduction band (eV)
- E_v = top of the valence band (eV)

An electron needs at least E_g (from heat or a photon) to jump from the valence band to the conduction band. Each jump creates **two** carriers: a free electron in the conduction band and a hole in the valence band. Impurities can place a few levels inside the gap (donor and acceptor levels), but a perfect crystal has none.

@fig figures/bands.svg | Band pictures of a metal, a semiconductor and an insulator. In the semiconductor a small forbidden gap separates the full valence band from the nearly empty conduction band, so a few electrons cross by thermal excitation.

Sketch: two horizontal shaded bands; label the lower "valence band (full at 0 K)" with top E_v, the upper "conduction band (empty at 0 K)" with bottom E_c, and the space between "forbidden gap E_g". Show one electron in the conduction band and the hole it left.

**Comparison.**

| | Valence band | Conduction band | Forbidden energy gap |
|---|---|---|---|
| Definition | Highest band completely full at 0 K | Lowest band above the valence band, empty at 0 K | Energy range between E_v and E_c with no allowed states |
| Edge | Top at E_v | Bottom at E_c | Width E_g = E_c − E_v |
| Electrons at 0 K | All states full | None | No states to hold any |
| Role of electrons | Bonding electrons, held in covalent bonds | Free electrons that move through the crystal | — |
| Carrier that conducts | Holes | Electrons | None (only impurity or defect levels in real crystals) |
| Origin | Bonding combinations of atomic orbitals | Antibonding combinations | Splitting between bonding and antibonding states |
| Values | — | — | Si 1.12 eV, Ge 0.66 eV, GaAs 1.42 eV, SiO₂ ≈ 9 eV |

**Why the gap matters.** Its width classifies solids: no gap (bands overlap or partly full) gives a metal; a small gap (about 0.1–3 eV) gives a semiconductor; a wide gap (above about 4 eV) gives an insulator.

**Marking checklist.** The points a marker looks for. Tick each one off in your own answer:

- ✓ valence band defined as the highest band full at 0 K, top E_v
- ✓ conduction band defined as the band above it, empty at 0 K, bottom E_c
- ✓ forbidden gap defined as the range with no states, E_g = E_c − E_v
- ✓ conduction in the conduction band by electrons and in the valence band by holes
- ✓ an electron needs at least E_g to cross; creates an electron–hole pair
- ✓ values: Si 1.12, Ge 0.66, GaAs 1.42 eV
- ✓ labelled band diagram
- ✓ comparison table

**Common mistakes.**

- Saying electrons "sit in the gap". In a perfect crystal there are no states in the gap at all.
- Saying the valence band never conducts. A full band does not, but once holes exist it does.
- Defining the bands only for room temperature. "Full" and "empty" refer to 0 K; at 300 K a few electrons have crossed.

**Remember it.** "Valence is the full house below, conduction the empty floor above, and the gap is the staircase that isn't there."

**Try a variant.** What is the longest wavelength of light that can lift an electron from the valence band to the conduction band in germanium (E_g = 0.66 eV)? *Answer:* the photon energy must be at least E_g, so λ_max (μm) = 1.24/E_g (eV) = 1.24/0.66 = **1.88 μm**. Longer wavelengths pass through without creating electron–hole pairs.

---

### Q26. Explain the difference between a direct band-gap and an indirect band-gap semiconductor.

> **Question type:** Comparison · **Topic:** direct and indirect band gaps · **Full notes:** Week 4 (Energy Bands and Carrier Concentrations)

**What the examiner wants.** Explain the difference using the E–k diagram (where the conduction-band minimum and valence-band maximum lie in k), explain why momentum conservation makes the phonon necessary in an indirect material, give the consequences for light emission and absorption, name examples and applications, and end with a comparison table. A sketch of both E–k diagrams earns marks.

**Key terms.**

- **Wave vector (k):** measures the electron's crystal momentum, p = ħk.
- **E–k diagram (band structure):** a graph of allowed electron energy E against k.
- **Conduction-band minimum / valence-band maximum:** the lowest point of the conduction band and the highest point of the valence band on the E–k diagram.
- **Photon:** a quantum of light; it carries energy hν but almost no momentum compared with an electron in a crystal.
- **Phonon:** a quantum of lattice vibration; little energy but large momentum.
- **Radiative recombination:** an electron falls into a hole and the energy leaves as a photon.

**Model answer.**

**The basis of the distinction.** When an electron moves between the conduction band and the valence band it must conserve both **energy** and **momentum**. A photon can supply or carry away energy of order E_g, but its momentum is tiny, so a photon alone can only cause a **vertical** transition on the E–k diagram (no change in k).

**Direct band gap.** The conduction-band minimum lies **at the same k** as the valence-band maximum (usually at k = 0, the Γ point). An electron at the bottom of the conduction band can drop straight down into a hole, emitting a photon of energy ≈ E_g. Only two particles are involved (electron and photon), so the process is fast and probable. Examples: **GaAs (1.42 eV)**, InP, GaN.

**Indirect band gap.** The conduction-band minimum lies **at a different k** from the valence-band maximum (in Si it is near the zone edge along the ⟨100⟩ direction). An electron dropping across the gap must also change its momentum, which a photon cannot supply. A **phonon** must be emitted or absorbed at the same instant. This three-particle event (electron, photon, phonon) is much less likely, so the electron usually loses its energy as heat through traps instead. Examples: **Si (1.12 eV)**, Ge (0.66 eV), GaP.

@fig figures/ek.svg | E–k diagrams. In GaAs (direct) the conduction-band minimum lies straight above the valence-band maximum, so an electron drops vertically and emits a photon. In Si (indirect) they are at different k, so a phonon must supply the momentum change.

Sketch: two E–k diagrams side by side. Direct: conduction-band parabola directly above the valence-band peak at k = 0, vertical arrow labelled "photon, hν = E_g". Indirect: conduction-band minimum shifted sideways; arrow with a vertical part (photon) and a horizontal part (phonon, Δk).

**The emitted (or absorbed) wavelength.**

    λ (μm) = 1.24 / E_g (eV)

Where:

- λ = wavelength of light emitted or just absorbed (μm)
- E_g = band-gap energy (eV)
- 1.24 = hc expressed in eV·μm

GaAs: 1.24/1.42 = 0.87 μm (near infrared). Si: 1.24/1.12 = 1.11 μm.

**Consequences.**

- **Light emission:** direct-gap materials emit efficiently, so LEDs and laser diodes are made from them. Silicon is a very poor emitter; there is no practical silicon laser.
- **Absorption:** direct-gap materials absorb strongly just above E_g (absorption coefficient about 10⁶ m⁻¹), so a few micrometres absorb most light. Indirect materials absorb weakly near E_g, so silicon solar cells must be much thicker.
- **Carrier lifetime:** radiative lifetime in direct-gap materials is about nanoseconds; in indirect-gap materials recombination is slow and mostly via traps, with lifetimes from microseconds to milliseconds.

**Comparison.**

| | Direct band gap | Indirect band gap |
|---|---|---|
| Band edges on E–k diagram | CB minimum and VB maximum at the same k | CB minimum at a different k from VB maximum |
| Transition across the gap | Vertical; photon alone | Needs a change of k; photon plus phonon |
| Particles involved | Two (electron, photon) | Three (electron, photon, phonon) |
| Probability of radiative recombination | High | Very low |
| Light emission | Efficient | Poor; energy lost mainly as heat |
| Absorption near E_g | Strong and sharp | Weak and gradual |
| Minority-carrier lifetime | Short (≈ ns) | Long (μs–ms) |
| Examples | GaAs (1.42 eV), InP, GaN | Si (1.12 eV), Ge (0.66 eV), GaP |
| Typical uses | LEDs, lasers, fast photodetectors, thin solar cells | ICs, transistors, power devices, Si photodiodes and solar cells |

**Marking checklist.** The points a marker looks for. Tick each one off in your own answer:

- ✓ definitions in terms of k-position of the CB minimum and VB maximum
- ✓ energy and momentum must both be conserved; photon carries negligible momentum
- ✓ phonon needed in an indirect transition
- ✓ two labelled E–k sketches
- ✓ consequence for light emission (LEDs/lasers use direct-gap materials)
- ✓ consequence for absorption and/or lifetime
- ✓ examples of each (GaAs; Si, Ge) with E_g values
- ✓ λ = 1.24/E_g and a worked value (GaAs 0.87 μm)
- ✓ comparison table

**Common mistakes.**

- Defining "direct" as "small gap" or "indirect" as "large gap". The difference is about k-position, not the size of E_g.
- Saying silicon cannot absorb light. It absorbs well above E_g (it is used in solar cells); it is emission that is poor.
- Saying a phonon supplies the energy. It mainly supplies the momentum; the photon carries almost all the energy.

**Remember it.** "Direct drops straight down; indirect needs a phonon to push it sideways."

**Try a variant.** An LED is needed at about 0.87 μm. Which of Si, Ge and GaAs is suitable, and why? *Answer:* the required gap is E_g = 1.24/0.87 = 1.42 eV, which matches GaAs. GaAs is also direct-gap, so it emits efficiently. Si (1.12 eV, emits near 1.11 μm) and Ge (0.66 eV, near 1.88 μm) have the wrong gap and are indirect, so they emit very weakly. **GaAs is the choice.**

---

### Q27. What is meant by an intrinsic semiconductor? Derive the expression for intrinsic carrier concentration.

> **Question type:** Definition and derivation · **Topic:** intrinsic carrier concentration · **Full notes:** Week 4 (Energy Bands and Carrier Concentrations); Week 5 (Carrier Statistics)

**What the examiner wants.** First a precise definition of an intrinsic semiconductor (pure, carriers only from thermal band-to-band excitation, n = p = n_i). Then a derivation: state the assumptions, start from the expressions for n and p, number every step, show that E_F cancels, and box the final result n_i = √(N_cN_v) e^{−E_g/2kT}. A numerical check for silicon and a comment on the temperature and band-gap dependence complete the answer.

**Key terms.**

- **Intrinsic semiconductor:** a pure crystal with no significant impurities, in which free carriers come only from thermal excitation across the gap.
- **Intrinsic carrier concentration (n_i):** the equal electron and hole concentration of an intrinsic semiconductor (m⁻³); 1×10¹⁶ m⁻³ for Si at 300 K.
- **Fermi level (E_F):** the energy at which a state has a 50 % chance of being occupied.
- **Effective density of states (N_c, N_v):** the number of states per m³ that, placed at the band edge, give the same carrier count as the whole band; Si at 300 K: N_c = 2.8×10²⁵, N_v = 1.04×10²⁵ m⁻³.
- **Boltzmann approximation:** replacing the Fermi–Dirac function by an exponential when E_F is more than about 3kT from the band edge.
- **Thermal energy (kT):** Boltzmann constant times absolute temperature; 0.0259 eV at 300 K.
- **Band gap (E_g):** E_g = E_c − E_v.

**Model answer.**

#### Part 1: Intrinsic semiconductor

An **intrinsic semiconductor** is a pure, undoped crystal (such as perfectly pure silicon) in which the number of impurity atoms is negligible. Its free carriers are produced **only** by thermal energy breaking covalent bonds, which lifts electrons from the valence band to the conduction band. Each electron that crosses leaves exactly one hole behind, so

    n = p = n_i

Where:

- n = concentration of electrons in the conduction band (m⁻³)
- p = concentration of holes in the valence band (m⁻³)
- n_i = intrinsic carrier concentration (m⁻³)

Its Fermi level, called the intrinsic level E_i, lies very close to the middle of the band gap.

@fig figures/si-bonds.svg | Two-dimensional picture of the silicon lattice. Thermal energy has broken one covalent bond, producing a free electron and a hole together; in an intrinsic crystal this is the only source of carriers, so n = p.

#### Part 2: Derivation

**Assumptions.**

- A. The semiconductor is in **thermal equilibrium** at absolute temperature T (no light, no applied voltage).
- B. It is **non-degenerate**: E_F lies more than about 3kT below E_c and above E_v, so the Boltzmann approximation holds. This gives the standard results

    n = N_c e^{−(E_c − E_F)/kT}          p = N_v e^{−(E_F − E_v)/kT}

Where:

- N_c, N_v = effective densities of states in the conduction and valence bands (m⁻³)
- E_c = bottom of the conduction band (eV)
- E_v = top of the valence band (eV)
- E_F = Fermi level (eV)
- k = Boltzmann constant, 8.617×10⁻⁵ eV/K; T = absolute temperature (K)

(These come from integrating density of states × occupation probability over each band; N_c = 2(2πm_n∗kT/h²)^{3/2} and N_v = 2(2πm_p∗kT/h²)^{3/2}, where m_n∗, m_p∗ are the electron and hole effective masses and h is Planck's constant.)

- C. The material is **intrinsic**: every free electron has a matching hole, so n = p = n_i.
- D. The band gap is E_g = E_c − E_v, and N_c, N_v and E_g are taken at the same temperature T.

**Step 1. Write the electron concentration.** From assumption B:

    n = N_c exp[ −(E_c − E_F)/kT ]

**Step 2. Write the hole concentration.** From assumption B:

    p = N_v exp[ −(E_F − E_v)/kT ]

**Step 3. Multiply the two.** Multiply n by p and combine the exponentials (e^A × e^B = e^{A+B}):

    n p = N_c N_v exp[ −(E_c − E_F)/kT − (E_F − E_v)/kT ]

**Step 4. Simplify the exponent: E_F cancels.** Inside the bracket, −(E_c − E_F) − (E_F − E_v) = −E_c + E_F − E_F + E_v = −(E_c − E_v). So

    n p = N_c N_v exp[ −(E_c − E_v)/kT ]

**Step 5. Introduce the band gap.** Using assumption D, E_c − E_v = E_g:

    n p = N_c N_v exp( −E_g/kT )

The product np depends only on the material (N_c, N_v, E_g) and the temperature, not on where the Fermi level is.

**Step 6. Apply the intrinsic condition.** By assumption C, n = p = n_i, so n p = n_i × n_i = n_i²:

    n_i² = N_c N_v exp( −E_g/kT )

**Step 7. Take the square root.** √(e^{−E_g/kT}) = e^{−E_g/2kT}, so:

    n_i = √(N_c N_v) · exp( −E_g / 2kT )

**Final result:** **n_i = √(N_cN_v) e^{−E_g/2kT}**

Where:

- n_i = intrinsic carrier concentration (m⁻³)
- N_c, N_v = effective densities of states (m⁻³)
- E_g = band gap (eV)
- kT = thermal energy (eV); 0.0259 eV at 300 K

**Step 8 (explicit temperature dependence).** Substituting N_c and N_v from assumption B:

    n_i = 2 (2πkT/h²)^{3/2} (m_n∗ m_p∗)^{3/4} exp( −E_g/2kT )   ∝   T^{3/2} exp( −E_g/2kT )

The exponential dominates: n_i rises very steeply with temperature and falls very steeply as E_g increases.

**Step 9 (position of the intrinsic Fermi level).** Setting n = p in Steps 1 and 2 and solving for E_F = E_i:

    E_i = (E_c + E_v)/2 + (kT/2) ln( N_v/N_c )

For Si: (0.0259/2) × ln(1.04/2.8) = −0.0128 eV, so E_i lies only about 13 meV below mid-gap.

#### Part 3: Numerical check for silicon at 300 K

**Given:** N_c = 2.8×10²⁵ m⁻³, N_v = 1.04×10²⁵ m⁻³, E_g = 1.12 eV, kT = 0.0259 eV.

**Find:** n_i.

**Solution.**

Step 1. √(N_cN_v) = √(2.8×10²⁵ × 1.04×10²⁵) = √(2.91×10⁵⁰) = 1.71×10²⁵ m⁻³.

Step 2. Exponent: E_g/2kT = 1.12/(2 × 0.0259) = 1.12/0.0518 = 21.62, so exp(−21.62) = 4.07×10⁻¹⁰.

Step 3. n_i = 1.71×10²⁵ × 4.07×10⁻¹⁰ = 6.95×10¹⁵ m⁻³.

**Answer:** **n_i ≈ 7×10¹⁵ m⁻³**, the same order as the accepted value 1×10¹⁶ m⁻³.

**What this means:** the formula gives the right size of n_i from just three material numbers. The small difference from 1×10¹⁶ m⁻³ comes from the exact values of E_g and the effective masses; because E_g sits in an exponent, a change of only 0.02 eV (to E_g ≈ 1.10 eV) would give exactly 1×10¹⁶ m⁻³.

**Marking checklist.** The points a marker looks for. Tick each one off in your own answer:

- ✓ definition: pure crystal, carriers only from thermal excitation, n = p = n_i
- ✓ assumptions stated (equilibrium, non-degenerate/Boltzmann, intrinsic n = p)
- ✓ n = N_c e^{−(E_c−E_F)/kT} and p = N_v e^{−(E_F−E_v)/kT}, symbols defined
- ✓ product np formed and E_F shown to cancel
- ✓ E_c − E_v replaced by E_g
- ✓ n = p = n_i used to write n_i² = N_cN_v e^{−E_g/kT}
- ✓ final boxed result n_i = √(N_cN_v) e^{−E_g/2kT}
- ✓ T^{3/2} e^{−E_g/2kT} dependence and/or E_i near mid-gap
- ✓ numerical check for Si giving ≈ 7×10¹⁵ (order 10¹⁶) m⁻³

**Common mistakes.**

- Losing the factor 2 in the exponent: the final exponent is −E_g/**2**kT, because of the square root. Using −E_g/kT gives 2.8×10⁶ m⁻³ for Si, which is absurd.
- Adding instead of multiplying n and p. Only the product makes E_F cancel.
- Sign errors in the exponents: n uses (E_c − E_F) and p uses (E_F − E_v), both positive in a non-degenerate semiconductor.
- Mixing units: if E_g is in eV, kT must be in eV (0.0259 eV), not in joules.

**Remember it.** "Multiply n and p, the Fermi level flees, and half the gap stays in the exponent."

**Try a variant.** For GaAs at 300 K, N_c = 4.7×10²³ m⁻³, N_v = 7.0×10²⁴ m⁻³ and E_g = 1.42 eV. Calculate n_i and compare with silicon. *Answer:* √(N_cN_v) = √(4.7×10²³ × 7.0×10²⁴) = 1.81×10²⁴ m⁻³; E_g/2kT = 1.42/0.0518 = 27.41, exp(−27.41) = 1.24×10⁻¹²; n_i = 1.81×10²⁴ × 1.24×10⁻¹² = **2.3×10¹² m⁻³**, about 3000 times smaller than in Si. The wider gap (by 0.30 eV) alone reduces the exponential by a factor e^{0.30/0.0518} ≈ 330, and the smaller N_c (light electron mass) accounts for the rest.

---

### Q28. Explain the difference between intrinsic and extrinsic carrier concentrations.

> **Question type:** Comparison · **Topic:** intrinsic and extrinsic carrier concentrations · **Full notes:** Week 4 (Energy Bands and Carrier Concentrations)

**What the examiner wants.** Explain what each concentration is, where the carriers come from, how each is calculated, how it depends on temperature, and how the two are linked by the mass-action law. Typical numbers for silicon and a closing comparison table secure full marks.

**Key terms.**

- **Intrinsic carrier concentration (n_i):** the equal electron and hole concentration in a pure semiconductor (m⁻³).
- **Extrinsic semiconductor:** a doped semiconductor whose carrier concentrations are set mainly by its dopants.
- **Donor / acceptor:** an impurity that gives an electron to the conduction band (e.g. P in Si; concentration N_D) / takes an electron from the valence band, creating a hole (e.g. B in Si; concentration N_A).
- **Complete ionisation:** every dopant atom has given up its electron (donor) or hole (acceptor); true for Si at room temperature.
- **Majority / minority carrier:** the carrier present in larger / smaller numbers (electrons / holes in n-type).
- **Mass-action law:** np = n_i² in thermal equilibrium, whatever the doping.
- **Fermi level (E_F) and intrinsic level (E_i):** the 50 %-occupancy energy, and its value in the pure material (near mid-gap).

**Model answer.**

**1. Intrinsic carrier concentration.** In a pure semiconductor, carriers come only from thermal excitation: heat breaks covalent bonds and lifts electrons from the valence band into the conduction band, each leaving a hole. Electrons and holes are therefore always equal:

    n = p = n_i = √(N_c N_v) e^{−E_g/2kT}

Where:

- n, p = electron and hole concentrations (m⁻³)
- n_i = intrinsic carrier concentration (m⁻³)
- N_c, N_v = effective densities of states in the conduction and valence bands (m⁻³); Si: 2.8×10²⁵ and 1.04×10²⁵
- E_g = band gap (eV); Si 1.12 eV
- kT = thermal energy, 0.0259 eV at 300 K

n_i is fixed by the material (through E_g) and the temperature; the designer cannot change it. For Si at 300 K, n_i = 1×10¹⁶ m⁻³, so only about one atom in 5×10¹² provides a carrier, and pure silicon is a poor conductor (σ = qn_i(μ_n + μ_p) = 1.6×10⁻¹⁹ × 10¹⁶ × 0.183 ≈ 2.9×10⁻⁴ S/m). n_i rises exponentially with temperature.

**2. Extrinsic carrier concentration.** In a doped semiconductor most carriers come from ionised dopant atoms, not from broken bonds. Electrons and holes are no longer equal. With complete ionisation and doping much greater than n_i:

    n-type:  n ≈ N_D,   p = n_i²/N_D          p-type:  p ≈ N_A,   n = n_i²/N_A

Where:

- N_D = donor concentration (m⁻³)
- N_A = acceptor concentration (m⁻³)
- n_i = intrinsic carrier concentration (m⁻³)

The majority-carrier concentration is set by the designer through the doping (typically 10²⁰–10²⁶ m⁻³ in Si) and stays nearly constant over a wide temperature range (the extrinsic range, roughly 150–450 K for moderately doped Si). At very low temperature the dopants are not all ionised (freeze-out); at very high temperature n_i overtakes the doping and the material behaves intrinsically again.

**3. The link: the mass-action law.** In thermal equilibrium,

    n p = n_i²

Where:

- n, p = equilibrium electron and hole concentrations (m⁻³)
- n_i = intrinsic carrier concentration (m⁻³)

Doping raises one carrier type and lowers the other so that the product is unchanged. Example, Si with N_D = 1×10²² m⁻³: n = 1×10²² m⁻³ and p = (10¹⁶)²/10²² = 1×10¹⁰ m⁻³. The electron concentration is 10⁶ times n_i and the hole concentration 10⁶ times smaller. Conductivity rises to σ = qnμ_n = 1.6×10⁻¹⁹ × 10²² × 0.135 ≈ 2.2×10² S/m, about 7×10⁵ times the intrinsic value.

**4. Position of the Fermi level.** In intrinsic material E_F = E_i, near mid-gap. In n-type material E_F moves up towards E_c; in p-type it moves down towards E_v.

@fig figures/fermi-level.svg | Fermi level position: at mid-gap (E_i) in intrinsic material, close to E_c in n-type and close to E_v in p-type.

Sketch: three band diagrams side by side (intrinsic, n-type, p-type), with E_F drawn at mid-gap, near E_c and near E_v.

**Comparison.**

| | Intrinsic carrier concentration | Extrinsic carrier concentration |
|---|---|---|
| Material | Pure (undoped) semiconductor | Doped semiconductor (n-type or p-type) |
| Source of carriers | Thermal breaking of bonds (band-to-band excitation) only | Mainly ionised donors or acceptors; small thermal contribution |
| Electrons vs holes | Equal: n = p = n_i | Unequal: majority and minority carriers |
| Formula | n_i = √(N_cN_v) e^{−E_g/2kT} | n ≈ N_D, p = n_i²/N_D (n-type); p ≈ N_A, n = n_i²/N_A (p-type) |
| Typical value, Si, 300 K | 1×10¹⁶ m⁻³ | Majority 10²⁰–10²⁶ m⁻³ |
| Set by | Material (E_g) and temperature | Doping level, chosen by the designer |
| Temperature dependence | Very strong, exponential | Almost constant in the extrinsic range; intrinsic again at high T |
| Fermi level | At E_i, near mid-gap | Towards E_c (n-type) or E_v (p-type) |
| Conductivity | Low (Si ≈ 3×10⁻⁴ S/m) | High, controlled by doping |

**Marking checklist.** The points a marker looks for. Tick each one off in your own answer:

- ✓ intrinsic: pure material, carriers from thermal excitation, n = p = n_i
- ✓ formula n_i = √(N_cN_v) e^{−E_g/2kT} with symbols defined; Si value 1×10¹⁶ m⁻³
- ✓ extrinsic: doped material, carriers mainly from ionised dopants, n ≠ p
- ✓ n ≈ N_D, p = n_i²/N_D (and the p-type equivalent)
- ✓ mass-action law np = n_i² linking the two
- ✓ temperature dependence contrasted (exponential vs nearly constant, then intrinsic at high T)
- ✓ Fermi-level positions
- ✓ a numerical example and a comparison table

**Common mistakes.**

- Thinking doping leaves the minority carriers unchanged. Doping *reduces* the minority concentration (np = n_i² stays fixed).
- Writing n = N_D + n_i as if the intrinsic electrons simply add. For N_D ≫ n_i, n ≈ N_D and the thermal electrons are negligible; the exact form needs the charge-neutrality formula.
- Saying extrinsic concentration "does not depend on temperature at all". It is constant only over the extrinsic range; freeze-out and intrinsic behaviour occur at the extremes.

**Remember it.** "Intrinsic is nature's choice, extrinsic is the designer's choice, and np = n_i² keeps them honest."

**Try a variant.** Silicon at 300 K is doped with N_A = 1×10²³ m⁻³ boron atoms. Find the hole and electron concentrations and say which is the majority carrier. *Answer:* p ≈ N_A = **1×10²³ m⁻³** (majority); n = n_i²/N_A = (1×10¹⁶)²/10²³ = **1×10⁹ m⁻³** (minority). The material is p-type, and its Fermi level lies close to E_v.

---

### Q29. Silicon has an intrinsic carrier concentration of approximately 1.0 × 10¹⁰ cm⁻³ at a specified temperature. If the electron and hole concentrations are equal, determine the electron and hole concentrations.

> **Question type:** Calculation · **Topic:** intrinsic carrier concentration and the mass-action law · **Full notes:** Week 4 (Energy Bands and Carrier Concentrations)

**What the examiner wants.** A short calculation. Marks come from recognising that n = p means the silicon is intrinsic, writing the mass-action law np = n_i², solving it to get n = p = n_i, and giving the value with its unit (m⁻³). A check and a one-line physical comment earn the final marks.

**Key terms.**

- **Electron concentration (n):** the number of free electrons in the conduction band per m³ (m⁻³).
- **Hole concentration (p):** the number of holes (empty bond states in the valence band) per m³ (m⁻³).
- **Intrinsic semiconductor:** a pure semiconductor whose free carriers come only from thermally broken bonds, so each broken bond gives one electron and one hole and n = p.
- **Intrinsic carrier concentration (n_i):** the common value of n and p in intrinsic material; for Si at 300 K, n_i = 1×10¹⁶ m⁻³.
- **Mass-action law:** in thermal equilibrium the product np equals n_i² at a given temperature, whatever the doping.
- **Thermal equilibrium:** the steady state of a sample at fixed temperature with no applied voltage, light or current.

**Model answer.**

**Given:** n_i = 1.0×10¹⁰ cm⁻³ = 1.0×10¹⁶ m⁻³; n = p.

**Find:** the electron concentration n and hole concentration p.

**Formula:** the mass-action law

    n p = n_i²

Where:

- n = electron concentration (m⁻³)
- p = hole concentration (m⁻³)
- n_i = intrinsic carrier concentration (m⁻³)

**Solution.**

Step 1. Set n = p in the mass-action law:

    n × n = n_i²   ⇒   n² = n_i²   ⇒   n = n_i   (the positive root, since a concentration cannot be negative)

Step 2. Substitute:

    n = p = 1.0×10¹⁶ m⁻³

Step 3. Check: np = (1.0×10¹⁶)(1.0×10¹⁶) = 1.0×10³² m⁻⁶ = n_i². ✓

**Answer:** **n = p = n_i = 1.0×10¹⁶ m⁻³.**

**What this means:** equal electron and hole concentrations are the signature of intrinsic (undoped) silicon, where every free electron came from a broken bond that also left a hole. Silicon has about 5×10²⁸ atoms per m³, so only about one atom in 5×10¹² has lost an electron. Pure silicon is therefore a poor conductor: σ = qn_i(μ_n + μ_p) = 1.6×10⁻¹⁹ × 10¹⁶ × (0.135 + 0.048) ≈ 2.9×10⁻⁴ S/m, a resistivity of about 3.4×10³ Ω·m.

Sketch (optional, for a fuller answer): a band diagram with E_c at the top and E_v at the bottom, a few electrons (dots) just above E_c and the same number of holes (circles) just below E_v, and E_F = E_i drawn as a dashed line near mid-gap.

**Marking checklist.** The points a marker looks for. Tick each one off in your own answer:

- ✓ n = p identified as the intrinsic condition
- ✓ mass-action law np = n_i² stated, with symbols defined
- ✓ algebra n² = n_i² ⇒ n = n_i shown
- ✓ answer n = p = 1.0×10¹⁶ m⁻³, with the unit
- ✓ check that np = 1.0×10³² m⁻⁶
- ✓ one-line physical comment (each broken bond gives one electron and one hole; very few carriers)

**Common mistakes.**

- Writing n = p = n_i/2 (thinking the carriers "share" n_i). n_i is the concentration of each carrier type, not the total; the total is 2n_i.
- Writing n = n_i² = 10³² m⁻³. That is the product np, in m⁻⁶, not a concentration.
- Leaving out the unit, or writing m³ instead of m⁻³ (per cubic metre).

**Remember it.** "Pure means equal": in intrinsic material n = p = n_i, because every broken bond makes one of each.

**Try a variant.** Germanium at 300 K has n_i = 2.4×10¹⁹ m⁻³. If it is undoped, find n, p and the product np. *Answer:* n = p = n_i = **2.4×10¹⁹ m⁻³**; np = (2.4×10¹⁹)² = **5.76×10³⁸ m⁻⁶**. Germanium has far more carriers than silicon because its band gap (0.66 eV) is smaller than silicon's (1.12 eV).

---

### Q30. Explain the Fermi-Dirac distribution function and its significance in semiconductor physics.

> **Question type:** Explain · **Topic:** Fermi–Dirac statistics · **Full notes:** Week 5 (Carrier Statistics)

**What the examiner wants.** "Explain" asks for the equation with every symbol defined, what the function means physically (a probability of occupation), its key properties, and then why it matters: how it is used to find carrier concentrations and why the Fermi level it defines is so important. A labelled sketch of f(E) earns marks.

**Key terms.**

- **Fermion:** a particle, such as the electron, that obeys the Pauli exclusion principle.
- **Pauli exclusion principle:** no two electrons can occupy the same quantum state (at most one electron per state, counting spin).
- **Allowed state:** an energy level that an electron may occupy in the crystal (in the conduction or valence band, not in the gap).
- **Fermi level (E_F):** the energy at which a state has exactly a 50 % chance of being occupied.
- **Thermal energy (kT):** Boltzmann's constant times absolute temperature; 0.0259 eV at 300 K.
- **Boltzmann approximation:** the simpler form f(E) ≈ e^{−(E − E_F)/kT}, valid when E − E_F is more than about 3kT.
- **Carrier concentration (n, p):** the number of free electrons (n) or holes (p) per m³.

**Model answer.**

#### 1. The function

Electrons are fermions: they obey the Pauli exclusion principle, so each allowed state can hold at most one electron. In thermal equilibrium at temperature T, the probability that an allowed state of energy E is occupied by an electron is the Fermi–Dirac distribution function:

    f(E) = 1 / ( 1 + e^{(E − E_F)/kT} )

Where:

- f(E) = probability that a state at energy E is occupied (dimensionless, 0 to 1)
- E = energy of the state (eV)
- E_F = Fermi level (eV)
- k = Boltzmann constant, 8.617×10⁻⁵ eV/K
- T = absolute temperature (K); kT = 0.0259 eV at 300 K

The probability that the state is **empty** is 1 − f(E). An empty state in the valence band is a hole, so 1 − f(E) is the probability of finding a hole.

#### 2. Properties

- **Bounded:** 0 ≤ f(E) ≤ 1, because a state holds at most one electron.
- **Half at E_F:** at E = E_F the exponent is zero, so f = 1/(1 + 1) = ½ at every temperature.
- **Symmetric about E_F:** a state ΔE above E_F is as likely to be full as a state ΔE below E_F is to be empty: f(E_F + ΔE) = 1 − f(E_F − ΔE).
- **Width of a few kT:** f changes from nearly 1 to nearly 0 over about ±3kT (±0.08 eV at 300 K). For example, at 300 K a state 0.1 eV above E_F has f = 0.021, and one 0.1 eV below has f = 0.979.
- **Boltzmann tail:** for E − E_F > 3kT, f(E) ≈ e^{−(E − E_F)/kT}, accurate to within 5 %. Most semiconductor calculations use this form.
- **At 0 K** it becomes a sharp step: f = 1 below E_F and f = 0 above.

@fig figures/fermi.svg | The Fermi–Dirac function f(E): a sharp step at E_F at 0 K, smoothed over a few kT at higher temperatures, and always equal to ½ at E_F.

Sketch: f(E) on the horizontal axis (0 to 1) against E on the vertical axis; mark E_F where f = ½; draw the 0 K step and a smooth 300 K curve crossing it at E_F.

#### 3. Significance in semiconductor physics

1. **It gives the carrier concentrations.** The number of electrons is "available states × probability occupied", summed over the conduction band; holes use 1 − f(E) over the valence band (see the equations below). Without f(E), n, p and n_i cannot be calculated.
2. **It defines the Fermi level.** The position of E_F between E_v and E_c tells at once whether the material is intrinsic (E_F near mid-gap), n-type (E_F near E_c) or p-type (E_F near E_v), and how heavily it is doped.
3. **Constant E_F in equilibrium.** In any system in equilibrium E_F is the same everywhere. This rule produces the band bending and built-in voltage of p-n junctions, metal–semiconductor contacts and MOS structures.
4. **It explains temperature effects:** more electrons in the high-energy tail as T rises, hence more carriers, intrinsic behaviour at high T and freeze-out at low T.
5. **Degeneracy:** when E_F comes within 3kT of a band edge (very heavy doping), the Boltzmann form fails and the full Fermi–Dirac function must be used.
6. **Out of equilibrium** (under bias or light) the idea is extended to separate quasi-Fermi levels for electrons and holes.

The carrier-concentration integrals are:

    n = ∫ g_c(E) f(E) dE,      p = ∫ g_v(E) [1 − f(E)] dE

Where:

- g_c(E), g_v(E) = density of states in the conduction and valence bands: allowed states per unit energy per unit volume (m⁻³eV⁻¹)
- the integrals run over the conduction band (for n) and the valence band (for p)

**Marking checklist.** The points a marker looks for. Tick each one off in your own answer:

- ✓ f(E) = 1/(1 + e^{(E − E_F)/kT}) written correctly, every symbol defined
- ✓ stated as the probability that a state at energy E is occupied; based on the Pauli principle
- ✓ f(E_F) = ½ at any temperature
- ✓ 1 − f(E) = probability of a hole
- ✓ step at 0 K, smoothed over a few kT at higher T (labelled sketch)
- ✓ Boltzmann approximation for E − E_F > 3kT
- ✓ use in n = ∫g_c f dE and p = ∫g_v(1 − f)dE
- ✓ E_F position indicates n-type, p-type or intrinsic; E_F is flat in equilibrium

**Common mistakes.**

- Saying f(E) is the number of electrons at energy E. It is only a probability; the number also needs the density of states g(E).
- Writing the exponent with the wrong sign, e^{(E_F − E)/kT}, which makes high-energy states full. Check: large E must give f → 0.
- Defining E_F as "the highest filled level" without saying this is true only at 0 K. At T > 0 the correct definition is the energy where f = ½.

**Remember it.** "Half full at the Fermi level": f(E) is a probability that falls from 1 to 0 across E_F over a few kT.

**Try a variant.** At 300 K, what is the probability that a state 3kT above the Fermi level is occupied, and how good is the Boltzmann approximation there? *Answer:* f = 1/(1 + e³) = 1/(1 + 20.09) = **0.047**; Boltzmann gives e⁻³ = **0.050**, about 5 % too high, which is why 3kT is taken as the limit of the approximation.

---

### Q31. Write the Fermi-Dirac distribution equation and explain what happens to the distribution at absolute zero.

> **Question type:** State and explain · **Topic:** Fermi–Dirac function at T = 0 K · **Full notes:** Week 5 (Carrier Statistics)

**What the examiner wants.** Write the equation and define every symbol, then show mathematically (by taking the limit kT → 0 for E below and above E_F) that f(E) becomes a step, and state what that means physically for a semiconductor: full valence band, empty conduction band, no free carriers. A sketch of the step and a remark on how it softens as T rises complete the answer.

**Key terms.**

- **Fermi–Dirac function (f(E)):** the probability that an allowed electron state at energy E is occupied in thermal equilibrium.
- **Fermi level (E_F):** the energy at which f = ½; at 0 K, the boundary between filled and empty states.
- **Absolute zero (0 K):** the lowest possible temperature, where thermal energy kT = 0.
- **Valence band (E_v):** the band of bond electrons, full at 0 K; E_v is its top edge.
- **Conduction band (E_c):** the band of free electrons, empty at 0 K; E_c is its bottom edge.
- **Free carrier:** an electron in the conduction band or a hole in the valence band, able to carry current.

**Model answer.**

#### The equation

    f(E) = 1 / ( 1 + e^{(E − E_F)/kT} )

Where:

- f(E) = probability that a state at energy E is occupied (dimensionless)
- E = energy of the state (eV)
- E_F = Fermi level (eV)
- k = Boltzmann constant, 8.617×10⁻⁵ eV/K
- T = absolute temperature (K)

#### At absolute zero

At T = 0 K, kT → 0, so the exponent (E − E_F)/kT goes to ±∞ depending on the sign of E − E_F.

**Case 1, states below E_F (E < E_F).** E − E_F is negative, so the exponent → −∞ and e^{−∞} = 0:

    f(E) = 1/(1 + 0) = 1

Every state below E_F is certainly filled.

**Case 2, states above E_F (E > E_F).** E − E_F is positive, so the exponent → +∞ and e^{+∞} → ∞:

    f(E) = 1/(1 + ∞) = 0

Every state above E_F is certainly empty.

So at 0 K the distribution is a **sharp rectangular step** at E = E_F. The Fermi level is then exactly the boundary between completely filled and completely empty states, which is why it is sometimes described as the highest occupied energy at 0 K. (At E = E_F itself the step is conventionally given the value ½.)

@fig figures/fermi.svg | At 0 K the Fermi–Dirac function is a step: every state below E_F is full and every state above is empty. At higher temperatures the step is rounded over a few kT but still passes through ½ at E_F.

Sketch: E on the vertical axis, f(E) from 0 to 1 on the horizontal axis; draw the 0 K curve as a vertical-sided step at E_F, and a smooth S-shaped curve for T > 0 crossing ½ at E_F.

#### Physical meaning for a semiconductor

In a semiconductor E_F lies inside the band gap. At 0 K every valence-band state (below E_F) is full and every conduction-band state (above E_F) is empty. There are no electrons in the conduction band and no holes in the valence band, so there are **no free carriers**: a pure semiconductor is a **perfect insulator at absolute zero**.

#### As the temperature rises

The step softens over about ±3kT around E_F: a few states just below E_F empty and a few just above fill. The high-energy tail reaches the conduction band and supplies free electrons; the matching empty states in the valence band are holes. That is why a semiconductor conducts at room temperature. f(E_F) = ½ at every temperature.

| E − E_F | f at 0 K | f at 300 K (kT = 0.0259 eV) |
|---|---|---|
| −0.1 eV | 1 | 0.979 |
| 0 | ½ (edge of step) | 0.500 |
| +0.1 eV | 0 | 0.021 |
| +0.3 eV | 0 | 9.3×10⁻⁶ |

**Marking checklist.** The points a marker looks for. Tick each one off in your own answer:

- ✓ f(E) = 1/(1 + e^{(E − E_F)/kT}) with every symbol defined
- ✓ limit for E < E_F: exponent → −∞, f = 1
- ✓ limit for E > E_F: exponent → +∞, f = 0
- ✓ "step function at E_F" stated, with a labelled sketch
- ✓ E_F is the boundary between filled and empty states at 0 K
- ✓ semiconductor at 0 K: valence band full, conduction band empty, no free carriers, insulator
- ✓ as T rises the step is smoothed over a few kT; f(E_F) = ½

**Common mistakes.**

- Only stating "f is a step" without showing the two limits; the explanation marks are for the mathematics (e^{−∞} = 0, e^{+∞} = ∞).
- Saying all electrons are "at" E_F at 0 K. They fill every state up to E_F; E_F is the top of the filled region, not where the electrons sit.
- Concluding that a semiconductor at 0 K conducts like a metal. The Fermi level is in the gap, where there are no states, so the filled band is completely full and cannot conduct.

**Remember it.** "At zero, the Fermi function is a cliff": everything below E_F full, everything above empty.

**Try a variant.** At 300 K, find the probability that a state 0.05 eV above the Fermi level is occupied, and the value at 0 K. *Answer:* (E − E_F)/kT = 0.05/0.0259 = 1.93; f = 1/(1 + e^{1.93}) = 1/(1 + 6.89) = **0.127** at 300 K; at 0 K the state is above E_F, so **f = 0**.

---

### Q32. Define the density of states in a semiconductor and explain its importance in determining carrier concentration.

> **Question type:** Define and explain · **Topic:** density of states · **Full notes:** Week 5 (Carrier Statistics)

**What the examiner wants.** A precise definition with units, the formulas for the conduction and valence bands (square-root dependence, zero in the gap), and an explanation of how g(E) combines with the Fermi–Dirac function to give n and p, leading to the effective densities of states N_c and N_v. A sketch of g(E) against E earns marks.

**Key terms.**

- **Allowed state:** an electron energy level permitted in the crystal; each can hold one electron (two per orbital, one for each spin).
- **Density of states (g(E)):** the number of allowed states per unit energy per unit volume at energy E (m⁻³eV⁻¹).
- **Effective mass (m_n∗, m_p∗):** the mass an electron or hole appears to have when it moves through the crystal; it describes the curvature of the band.
- **Fermi–Dirac function (f(E)):** the probability that a state at energy E is occupied.
- **Effective density of states (N_c, N_v):** the number of states which, if all placed at the band edge, would give the same carrier concentration as the real band; Si at 300 K: N_c = 2.8×10²⁵, N_v = 1.04×10²⁵ m⁻³.
- **Band gap (E_g = E_c − E_v):** the energy range between the top of the valence band E_v and the bottom of the conduction band E_c, where there are no allowed states.

**Model answer.**

#### Definition

The **density of states** g(E) is the number of allowed electron energy states (counting both spins) per unit energy interval, per unit volume of crystal, at energy E. Its unit is m⁻³eV⁻¹ (or m⁻³J⁻¹). So g(E)dE is the number of states per m³ with energies between E and E + dE.

For parabolic bands:

    g_c(E) = (4π (2m_n∗)^{3/2} / h³) √(E − E_c)     for E ≥ E_c
    g_v(E) = (4π (2m_p∗)^{3/2} / h³) √(E_v − E)     for E ≤ E_v
    g(E) = 0                                       for E_v < E < E_c

Where:

- g_c(E), g_v(E) = density of states in the conduction and valence bands (m⁻³J⁻¹ as written with SI values of m∗ and h; multiply by 1.6×10⁻¹⁹ J/eV to get m⁻³eV⁻¹)
- m_n∗, m_p∗ = density-of-states effective masses of electrons and holes (kg)
- h = Planck constant, 6.626×10⁻³⁴ J·s
- E_c = bottom of the conduction band, E_v = top of the valence band (eV)

In words: there are no states in the gap; just inside each band the number of states starts at zero and grows as the square root of the distance into the band. A heavier effective mass (a flatter band) gives more states per unit energy.

**Where it comes from (briefly).** The allowed electron wave vectors k in a crystal of volume V are evenly spaced, one per (2π)³/V of k-space. Counting the states inside a sphere of radius k (times 2 for spin), and using E − E_c = ħ²k²/2m_n∗ (ħ = h/2π), gives a number of states that grows as (E − E_c)^{3/2}; differentiating with respect to E gives the √(E − E_c) law.

Sketch: E on the vertical axis; g_c(E) as a half-parabola opening upward from zero at E_c; g_v(E) opening downward from zero at E_v; g = 0 in the gap between them. Optionally add f(E) beside it and shade the product g_c f (electrons, a narrow peak just above E_c) and g_v(1 − f) (holes, just below E_v).

#### Importance in determining carrier concentration

- **Carriers = states × probability.** The Fermi function gives only the probability that a state is occupied; g(E) gives how many states there are. The carrier concentrations are their product, summed over each band:

    n = ∫ g_c(E) f(E) dE,      p = ∫ g_v(E) [1 − f(E)] dE

Where:

- n, p = electron and hole concentrations (m⁻³)
- f(E) = Fermi–Dirac occupation probability; 1 − f(E) = probability a state is empty (a hole)

- **It produces N_c and N_v.** Doing the integral with the Boltzmann approximation gives

    n = N_c e^{−(E_c − E_F)/kT},      p = N_v e^{−(E_F − E_v)/kT}
    N_c = 2 (2π m_n∗ kT / h²)^{3/2},  N_v = 2 (2π m_p∗ kT / h²)^{3/2}

Where:

- N_c, N_v = effective densities of states (m⁻³); Si at 300 K: 2.8×10²⁵ and 1.04×10²⁵ m⁻³
- E_F = Fermi level (eV); kT = thermal energy (0.0259 eV at 300 K; in J inside the N_c formula)

These appear in every carrier-concentration formula, including n_i = √(N_cN_v) e^{−E_g/2kT}.

- **It explains the "forbidden" gap.** f(E) is not zero in the gap, but g(E) is, so no carriers can exist there.
- **It sets the temperature dependence.** N_c and N_v grow as T^{3/2}, which forms part of the temperature dependence of n_i.
- **It explains differences between materials.** GaAs has a small electron effective mass (0.067m₀), so its N_c (4.7×10²³ m⁻³) is about 60 times smaller than silicon's. For the same doping its Fermi level sits closer to E_c, and it becomes degenerate at lower doping.
- **It fixes the intrinsic level.** Because N_v ≠ N_c in Si, the intrinsic Fermi level E_i sits slightly below mid-gap.

**Marking checklist.** The points a marker looks for. Tick each one off in your own answer:

- ✓ definition: number of states per unit energy per unit volume, unit m⁻³eV⁻¹
- ✓ g_c ∝ √(E − E_c) and g_v ∝ √(E_v − E); g = 0 in the gap
- ✓ dependence on effective mass, (m∗)^{3/2}
- ✓ labelled sketch of g(E) against E
- ✓ n = ∫g_c f dE and p = ∫g_v(1 − f)dE
- ✓ leads to N_c, N_v and n = N_c e^{−(E_c − E_F)/kT}, with Si values
- ✓ at least two further points of importance (gap has no carriers, T^{3/2}, material differences)

**Common mistakes.**

- Confusing g(E) with the number of electrons. g(E) counts available places; most conduction-band states are empty.
- Drawing g(E) as non-zero in the band gap, or as linear rather than square-root in shape.
- Mixing up g(E) (per unit energy, m⁻³eV⁻¹) with N_c (a plain concentration, m⁻³).

**Remember it.** "Seats times chance": carriers = how many seats (g) × chance each seat is taken (f).

**Try a variant.** For silicon at 300 K the Fermi level is 0.25 eV below E_c. Using the effective density of states, find the electron concentration. *Answer:* n = N_c e^{−(E_c − E_F)/kT} = 2.8×10²⁵ × e^{−0.25/0.0259} = 2.8×10²⁵ × e^{−9.65} = **1.8×10²¹ m⁻³**.

---

### Q33. Explain how the Fermi energy level changes with doping in n-type and p-type semiconductors.

> **Question type:** Explain · **Topic:** Fermi level and doping · **Full notes:** Week 5 (Carrier Statistics)

**What the examiner wants.** Start from the intrinsic case (E_F = E_i near mid-gap), then show with equations that donors move E_F up towards E_c and acceptors move it down towards E_v, that the shift grows logarithmically with doping, and what happens at very heavy doping (degeneracy). A band diagram with three cases and a short numerical example earn full marks.

**Key terms.**

- **Fermi level (E_F):** the energy where a state has a 50 % chance of being occupied; its position fixes n and p.
- **Intrinsic level (E_i):** the Fermi level of undoped material, close to mid-gap (about 0.56 eV below E_c in Si).
- **Donor (N_D):** an impurity (P, As, Sb in Si) that gives an electron to the conduction band; N_D is donors per m³.
- **Acceptor (N_A):** an impurity (B, Al, Ga in Si) that takes an electron from the valence band, creating a hole; N_A is acceptors per m³.
- **Effective density of states (N_c, N_v):** Si at 300 K: 2.8×10²⁵ and 1.04×10²⁵ m⁻³.
- **Degenerate semiconductor:** one so heavily doped that E_F is within 3kT of a band edge or inside a band.
- **Compensation:** partial cancelling when both donors and acceptors are present.

**Model answer.**

#### Starting point: intrinsic material

In pure material n = p = n_i and E_F = E_i, very close to the middle of the gap. The carrier concentrations are linked to the Fermi level by

    n = n_i e^{(E_F − E_i)/kT},      p = n_i e^{(E_i − E_F)/kT}

Where:

- n, p = electron and hole concentrations (m⁻³)
- n_i = intrinsic carrier concentration (1×10¹⁶ m⁻³ for Si at 300 K)
- E_F − E_i = height of the Fermi level above the intrinsic level (eV)
- kT = thermal energy (0.0259 eV at 300 K)

So any change in n or p caused by doping must move E_F.

#### n-type: E_F moves up, towards E_c

Donors add electrons; with complete ionisation and N_D ≫ n_i, n ≈ N_D. Rearranging:

    E_F − E_i = kT ln(N_D/n_i),      E_c − E_F = kT ln(N_c/N_D)

Where:

- N_D = donor concentration (m⁻³)
- E_c − E_F = distance from E_F up to the conduction-band edge (eV)
- N_c = effective density of states in the conduction band (m⁻³)

More donors → larger ln(N_D/n_i) → E_F rises further above E_i and closer to E_c.

#### p-type: E_F moves down, towards E_v

Acceptors add holes; p ≈ N_A, so

    E_i − E_F = kT ln(N_A/n_i),      E_F − E_v = kT ln(N_v/N_A)

Where:

- N_A = acceptor concentration (m⁻³)
- E_F − E_v = height of E_F above the valence-band edge (eV)
- N_v = effective density of states in the valence band (m⁻³)

@fig figures/fermi-level.svg | Fermi-level position in silicon: at E_i near mid-gap when intrinsic, raised towards E_c by donors (n-type), lowered towards E_v by acceptors (p-type).

Sketch: three band diagrams side by side (intrinsic, n-type, p-type), each with E_c, E_v and a dashed E_i at mid-gap; draw E_F on E_i, just below E_c (with donor levels E_D marked as short dashes just under E_c), and just above E_v (with acceptor levels E_A just above E_v).

#### Key features

- **Logarithmic shift.** Each tenfold increase in doping moves E_F by kT ln 10 ≈ 0.06 eV at 300 K, so large doping changes produce modest shifts.
- **Heavy doping → degeneracy.** As N_D approaches N_c (or N_A approaches N_v), E_F reaches the band edge or enters the band (n⁺ or p⁺ material); the Boltzmann formulas above then fail.
- **Compensation.** With both dopants, E_F is set by the net doping: N_D − N_A (n-type) or N_A − N_D (p-type).
- **Temperature.** As T rises, n_i grows and E_F moves back towards E_i; at high enough T every semiconductor becomes intrinsic. At very low T (freeze-out) the donors are not all ionised and E_F rises to between E_D and E_c.
- **Equilibrium.** E_F is constant through a device in equilibrium, so where n and p regions meet the bands bend; this gives the built-in voltage of a p-n junction.

#### Numerical example (Si, 300 K, n_i = 10¹⁶ m⁻³)

| Doping | E_F − E_i (eV) | E_F distance from nearer band edge (eV) |
|---|---|---|
| Intrinsic | 0 | about 0.56 from each edge |
| N_D = 10²¹ m⁻³ | +0.298 | E_c − E_F = 0.265 |
| N_D = 10²³ m⁻³ | +0.417 | E_c − E_F = 0.146 |
| N_A = 10²² m⁻³ | −0.358 | E_F − E_v = 0.180 |

**Marking checklist.** The points a marker looks for. Tick each one off in your own answer:

- ✓ intrinsic: E_F = E_i near mid-gap
- ✓ n-type: E_F moves towards E_c; E_F − E_i = kT ln(N_D/n_i) or E_c − E_F = kT ln(N_c/N_D)
- ✓ p-type: E_F moves towards E_v; E_i − E_F = kT ln(N_A/n_i) or E_F − E_v = kT ln(N_v/N_A)
- ✓ labelled band diagram of the three cases
- ✓ shift is logarithmic (≈ 0.06 eV per decade at 300 K)
- ✓ very heavy doping → degenerate, E_F at or inside the band
- ✓ temperature or compensation effect mentioned
- ✓ numerical example

**Common mistakes.**

- Saying E_F moves "linearly" with doping or "to the donor level". The shift is logarithmic, and at room temperature E_F normally lies below E_D in non-degenerate n-type silicon.
- Getting the direction wrong for p-type: acceptors pull E_F **down** towards E_v.
- Using N_D in E_F − E_i = kT ln(N_D/n_i) when the material is compensated; use the net doping N_D − N_A.

**Remember it.** "Donors push up, acceptors pull down, by 60 meV per decade."

**Try a variant.** Silicon at 300 K is doped with N_A = 1×10²³ m⁻³. Where is the Fermi level? *Answer:* E_i − E_F = 0.0259 ln(10²³/10¹⁶) = **0.417 eV below E_i**; E_F − E_v = 0.0259 ln(1.04×10²⁵/10²³) = 0.0259 × 4.64 = **0.120 eV above E_v**.

---

### Q34. An n-type semiconductor has a donor concentration of 5 × 10¹⁶ cm⁻³. Assuming complete ionization, determine the approximate majority-carrier concentration.

> **Question type:** Calculation · **Topic:** carrier concentrations in doped semiconductors · **Full notes:** Week 4 (Energy Bands and Carrier Concentrations); Fermi level in Week 5 (Carrier Statistics)

**What the examiner wants.** Identify the majority carrier (electrons in n-type), state that with complete ionisation and N_D ≫ n_i each donor gives one electron so n₀ ≈ N_D, and give the value with its unit. Examiners often follow up with the minority-carrier concentration (mass-action law) and the Fermi-level position, so both are worked below, taking the material as silicon at 300 K.

**Key terms.**

- **n-type semiconductor:** one doped with donors, so electrons outnumber holes.
- **Donor concentration (N_D):** number of donor atoms per m³; each ionised donor gives one free electron.
- **Complete ionisation:** every donor has given up its electron (true for Si between about 150 K and 450 K).
- **Majority carrier:** the more numerous carrier (electrons in n-type); concentration n₀ (subscript 0 means thermal equilibrium).
- **Minority carrier:** the less numerous carrier (holes in n-type); concentration p₀.
- **Mass-action law:** n₀p₀ = n_i² in thermal equilibrium.
- **Fermi level (E_F) and intrinsic level (E_i):** E_F is the energy with a 50 % occupation probability; E_i is its position in undoped material, near mid-gap.

**Model answer.**

**Given:** N_D = 5×10¹⁶ cm⁻³ = 5×10²² m⁻³, complete ionisation. For the follow-ups: silicon at 300 K, n_i = 1×10¹⁶ m⁻³, kT = 0.0259 eV, N_c = 2.8×10²⁵ m⁻³.

**Find:** the majority-carrier concentration n₀; also the minority-carrier concentration p₀ and the Fermi-level position.

**Formula:**

    n₀ ≈ N_D          (complete ionisation, N_D ≫ n_i)
    p₀ = n_i² / n₀    (mass-action law)
    E_F − E_i = kT ln(n₀/n_i),     E_c − E_F = kT ln(N_c/n₀)

Where:

- n₀ = equilibrium electron (majority) concentration (m⁻³)
- p₀ = equilibrium hole (minority) concentration (m⁻³)
- N_D = donor concentration (m⁻³)
- n_i = intrinsic carrier concentration (m⁻³)
- kT = thermal energy (eV)
- N_c = effective density of states in the conduction band (m⁻³)
- E_c = conduction-band edge, E_F = Fermi level, E_i = intrinsic level (eV)

**Solution.**

Step 1. Check the approximation: N_D = 5×10²² ≫ n_i = 10¹⁶ m⁻³ (by a factor of 5×10⁶), so thermally generated electrons are negligible and every donor supplies one electron:

    n₀ ≈ N_D = 5×10²² m⁻³

Step 2 (follow-up). Minority holes from the mass-action law:

    p₀ = n_i²/n₀ = (1×10¹⁶)² / (5×10²²) = 1×10³² / 5×10²² = 2×10⁹ m⁻³

Step 3 (follow-up). Fermi level relative to the intrinsic level:

    E_F − E_i = 0.0259 × ln(5×10²² / 1×10¹⁶) = 0.0259 × ln(5×10⁶) = 0.0259 × 15.42 = 0.40 eV

Step 4 (follow-up). Fermi level relative to the conduction-band edge:

    E_c − E_F = 0.0259 × ln(2.8×10²⁵ / 5×10²²) = 0.0259 × ln(560) = 0.0259 × 6.33 = 0.164 eV

Check: (E_F − E_i) + (E_c − E_F) = 0.40 + 0.164 = 0.56 eV ≈ E_g/2, as expected since E_i is near mid-gap. E_c − E_F = 0.164 eV is more than 3kT (0.078 eV), so the material is non-degenerate and the Boltzmann formulas used are valid.

**Answer:** **Majority (electron) concentration n₀ ≈ 5×10²² m⁻³.** Follow-ups (Si, 300 K): **minority (hole) concentration p₀ = 2×10⁹ m⁻³**; **Fermi level 0.40 eV above E_i, i.e. about 0.16 eV below E_c.**

**What this means:** doping has raised the electron concentration by a factor of 5 million above the intrinsic value and, through np = n_i², cut the hole concentration by the same factor; there are about 2.5×10¹³ electrons for every hole. The Fermi level has moved most of the way from mid-gap up to the conduction band, which is the band-diagram picture of a strongly n-type sample.

@fig figures/fermi-level.svg | In n-type silicon the Fermi level lies above the intrinsic level, between E_i and E_c; for N_D = 5×10²² m⁻³ it is 0.40 eV above E_i and 0.16 eV below E_c.

Sketch: a band diagram with E_c and E_v, a dashed E_i near mid-gap, and E_F drawn 0.40 eV above E_i (0.16 eV below E_c), labelled with these values.

**Marking checklist.** The points a marker looks for. Tick each one off in your own answer:

- ✓ majority carriers identified as electrons
- ✓ n₀ ≈ N_D justified by complete ionisation and N_D ≫ n_i
- ✓ answer 5×10²² m⁻³ with the unit
- ✓ (follow-up) p₀ = n_i²/n₀ = 2×10⁹ m⁻³
- ✓ (follow-up) E_F − E_i = kT ln(n₀/n_i) = 0.40 eV, Fermi level above E_i, towards E_c
- ✓ (follow-up) E_c − E_F = kT ln(N_c/n₀) = 0.16 eV
- ✓ assumption stated: silicon at 300 K, n_i = 10¹⁶ m⁻³

**Common mistakes.**

- Adding n_i to N_D ("5×10²² + 10¹⁶") as if it mattered, or, worse, giving n_i as the answer. n_i is negligible here; n₀ ≈ N_D.
- Calculating p₀ = n_i/N_D or N_D/n_i instead of n_i²/N_D; check the units: (m⁻³)²/m⁻³ = m⁻³.
- Using log₁₀ instead of the natural log in E_F − E_i = kT ln(n₀/n_i): log₁₀(5×10⁶) = 6.70 would give 0.17 eV, which is wrong.
- Placing E_F below E_i for n-type material; donors raise E_F.

**Remember it.** "Majority = dopant, minority = n_i² over dopant, and E_F climbs kT ln(N_D/n_i) above mid-gap."

**Try a variant.** p-type silicon at 300 K has N_A = 2×10²¹ m⁻³ (complete ionisation). Find the majority and minority concentrations and the Fermi-level position. *Answer:* p₀ ≈ N_A = **2×10²¹ m⁻³** (holes); n₀ = n_i²/p₀ = 10³²/2×10²¹ = **5×10¹⁰ m⁻³** (electrons); E_i − E_F = 0.0259 ln(2×10⁵) = **0.316 eV below E_i**, i.e. E_F − E_v = 0.0259 ln(1.04×10²⁵/2×10²¹) = **0.222 eV above E_v**.
