# Week 8 — High-Field Effects and Excess Carriers
<!-- group: Module 3 · Carrier Transport & Injection Phenomena -->

**Plan:** velocity saturation and hot-carrier effects; generation and recombination mechanisms (Shockley–Read–Hall theory); carrier lifetime and steady-state excess carrier injection.

## Learning objectives

By the end of this week you should be able to:

1. Explain velocity saturation and its effect on devices.
2. Explain hot-carrier effects and how they are reduced.
3. Explain excess carriers and low-level injection.
4. Describe the generation and recombination mechanisms.
5. Explain SRH recombination and calculate lifetime from trap data.
6. Calculate decay of excess carriers and steady-state injection levels.

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
| μm | Micrometre (micron) | 1 μm = 10⁻⁴ cm = 10⁻⁶ m |

**Symbols**

| Symbol | Meaning | Units / typical value |
|---|---|---|
| E_g | Band-gap energy, E_c − E_v | eV; Si 1.12, Ge 0.66, GaAs 1.42 at 300 K |
| E_F | Fermi level: the energy at which a state has a 50 % chance of being occupied | eV |
| E_i | Intrinsic Fermi level, close to mid-gap | eV |
| E_Fn, E_Fp | Quasi-Fermi levels for electrons and holes, used out of equilibrium | eV |
| E_t | Energy level of a trap (recombination centre) in the gap | eV |
| n | Electron concentration (free electrons per cm³) | cm⁻³ |
| p | Hole concentration (holes per cm³) | cm⁻³ |
| n_i | Intrinsic carrier concentration (n = p = n_i in pure material) | cm⁻³; Si ≈ 1×10¹⁰ at 300 K |
| n₀, p₀ | Equilibrium electron and hole concentrations | cm⁻³ |
| N_D | Donor concentration | cm⁻³ |
| N_A | Acceptor concentration | cm⁻³ |
| Δn, Δp | Excess electron and hole concentrations above equilibrium | cm⁻³ |
| ν, hν | Frequency of light, and photon energy | Hz; eV |
| Q | Dose: dopant atoms per unit area (in Weeks 13–14, Q also means charge) | atoms/cm² (C or C/cm² for charge) |
| μ, μ_n, μ_p | Mobility: drift velocity per unit field (electrons, holes) | cm²/(V·s); Si μ_n 1350, μ_p 480 |
| v_d | Drift velocity | cm/s |
| v_th | Thermal velocity of carriers | ≈ 10⁷ cm/s at 300 K |
| v_sat | Saturation velocity at high field | ≈ 10⁷ cm/s in Si |
| σ | Conductivity, q(nμ_n + pμ_p) (in Week 8, σ is also a capture cross-section) | S/cm (siemens per cm) |
| D_n, D_p | Diffusion coefficients of electrons and holes | cm²/s; Si 35 and 12.4 |
| T_e | Electron temperature of hot carriers | K |
| G, G_L | Generation rate of electron–hole pairs (G_L: by light) | cm⁻³s⁻¹ |
| R | Recombination rate | cm⁻³s⁻¹ |
| U | Net recombination rate, R − G | cm⁻³s⁻¹ |
| τ, τ_n, τ_p | Minority-carrier lifetime (τ_eff: effective, including surfaces) | s; Si 1 ns – 1 ms |
| N_t | Density of traps (recombination centres) | cm⁻³ |
| σ_n, σ_p | Capture cross-section of a trap for electrons, holes | cm² |
| n₁, p₁ | SRH parameters n_ie^{(E_t − E_i)/kT} and n_ie^{(E_i − E_t)/kT} | cm⁻³ |
| L, L_n, L_p | Diffusion length √(Dτ): distance a minority carrier travels before recombining | μm or cm |
| V, V_a | Applied voltage (positive for forward bias) | V |
| W | Depletion-region width (in Week 13 W_B, W_E are base and emitter widths; in Week 14 W is channel width) | μm or cm |
| I_s, J_s (I_S) | Saturation current (density) of a diode or transistor | A; A/cm² |
| A (area) | Device or contact area | cm² |
| β | Common-emitter current gain, I_C/I_B (also h_FE) | dimensionless; 50–500 |
| N_E, W_E, D_E; N_B, W_B, D_B | Doping, width and minority diffusion coefficient of the emitter; of the base | cm⁻³; μm; cm²/s |
| f_T | Transition (cut-off) frequency | Hz |
| V_T (V_th) | Threshold voltage of a MOSFET | V |
| V_GS, V_DS, V_SB, V_G | Gate–source, drain–source, source–body and gate voltages | V |
| E_sat | Field at which the drift velocity saturates, v_sat/μ | V/cm |
| G_th, R_th | Thermal generation and recombination rates (equal in equilibrium) | cm⁻³s⁻¹ |
| f_t, e_n, e_p | Probability a trap is occupied by an electron; emission rates of electrons and holes from traps | dimensionless; s⁻¹ |
| r_a, r_b, r_c, r_d | SRH rates: electron capture, electron emission, hole capture, hole emission | cm⁻³s⁻¹ |
| τ_SRH, τ_radiative, τ_Auger | Lifetimes set by trap (SRH), radiative and Auger recombination | s |
| I_gen, J_gen | Generation current (density) from carriers generated in the depletion region | A; A/cm² |

**Abbreviations**

| Abbreviation | Meaning |
|---|---|
| Si | Silicon |
| Ge | Germanium |
| GaAs | Gallium arsenide |
| GaN | Gallium nitride |
| InP | Indium phosphide |
| SiO₂ | Silicon dioxide (silica), the oxide insulator |
| CB | Conduction band |
| VB | Valence band |
| SRH | Shockley–Read–Hall (trap-assisted) recombination |
| LDD | Lightly doped drain |
| MOSFET | Metal–oxide–semiconductor field-effect transistor |
| CMOS | Complementary MOS (n- and p-channel MOSFETs together) |
| BJT | Bipolar junction transistor |
| LED | Light-emitting diode |
| IGBT | Insulated-gate bipolar transistor |
| PCD | Photoconductive decay (lifetime measurement) |


## Key terms

Every important word used this week is defined here, so you can read this week on its own.

**Band gap (E_g).** The range of energies that an electron in a crystal cannot have. It lies between the valence band (the band of energies occupied by the electrons that form the bonds between atoms) and the conduction band (the next band up, where electrons are free to move). For silicon E_g = 1.12 eV at 300 K.

**Electron and hole (carriers).** A free electron is an electron in the conduction band; a hole is an empty place left in the valence band, which behaves like a positive charge that can move. Together they are called carriers because they carry the current.

**Doping (N_D, N_A).** Adding small, controlled amounts of impurity atoms to a semiconductor. Donors (concentration N_D) give free electrons and make the material n-type; acceptors (concentration N_A) give holes and make it p-type.

**Majority and minority carriers.** The majority carriers are the more numerous type (electrons in n-type, holes in p-type); the minority carriers are the less numerous type.

*Why it matters:* this week shows that it is the minority carriers whose numbers change, and so they control how devices behave.

**Intrinsic carrier concentration (n_i).** The number of electrons (equal to the number of holes) per cm³ in pure, undoped material; about 1×10¹⁰ cm⁻³ in Si at 300 K. In thermal equilibrium (no light, no applied voltage, steady temperature) the electron and hole concentrations of any sample obey the mass-action law:

    n₀p₀ = n_i²

Where:

- n₀, p₀ = equilibrium electron and hole concentrations (cm⁻³)
- n_i = intrinsic carrier concentration (cm⁻³)

**Fermi level (E_F).** The energy at which an electron state has a 50 % chance of being occupied. In thermal equilibrium one Fermi level describes both electrons and holes, and it is the same everywhere in the material.

**Drift velocity and saturation velocity (v_d, v_sat).** The drift velocity is the average velocity carriers gain in an electric field; at low field it is v_d = μE, where μ is the mobility (cm²/V·s). At high field it stops rising and levels off at the saturation velocity v_sat, about 1×10⁷ cm/s in silicon.

*Why it matters:* the carriers in a modern short-channel transistor travel at v_sat, which limits its current and speed.

**Hot carriers.** Carriers whose average energy, gained from a strong electric field, is far above the normal thermal energy of the crystal. Their energy is described by an electron temperature T_e much higher than the lattice temperature T.

**Impact ionisation.** The process in which a hot carrier collides with the lattice hard enough to break a bond and create a new electron–hole pair. Repeated, it becomes an avalanche, which causes avalanche breakdown.

**Excess carriers (Δn, Δp).** Electrons and holes present in addition to the equilibrium numbers, for example created by light or injected by a forward-biased junction: n = n₀ + Δn and p = p₀ + Δp.

**Low-level injection.** The condition in which the excess carrier concentration is much smaller than the equilibrium majority concentration (Δp ≪ n₀ in n-type). The majority concentration is then almost unchanged.

**Generation and recombination (G, R, U).** Generation is the creation of an electron–hole pair; recombination is the loss of one, when a conduction-band electron falls back into a hole. G and R are rates in pairs per cm³ per second; U = R − G is the net recombination rate.

**Trap (recombination centre, N_t, E_t).** A localised energy level E_t inside the band gap, created by a crystal defect or an impurity atom such as gold or iron. It can capture an electron and then a hole, helping them recombine in two small steps. N_t is the density of traps (cm⁻³).

**Shockley–Read–Hall (SRH) recombination.** Recombination through traps. The energy is released as lattice vibrations (heat). It is the main recombination mechanism in silicon.

**Minority-carrier lifetime (τ).** The average time an excess minority carrier survives before it recombines. After the source of excess carriers is removed, the excess falls to 1/e (37 %) of its starting value in one lifetime.

    Δp(t) = Δp(0) e^{−t/τ_p}

Where:

- Δp(t) = excess hole concentration at time t (cm⁻³)
- Δp(0) = excess hole concentration when the light is switched off (cm⁻³)
- t = time since switch-off (s)
- τ_p = hole (minority-carrier) lifetime in n-type material (s)

*Why it matters:* lifetime decides how far minority carriers can travel, how fast a diode switches off and how efficient a solar cell is.

**Quasi-Fermi levels (E_{Fn}, E_{Fp}).** When the material is out of equilibrium (np ≠ n_i²), one Fermi level can no longer describe both carriers, so two are used: E_{Fn} gives the electron concentration and E_{Fp} the hole concentration. Their separation measures how far the material is from equilibrium.

## The big picture

This week covers two separate stories.

**Story 1: what happens at very high fields.** Week 7 said v_d = μE: double the field, double the speed. That stops being true at high fields. Carriers hit a **speed limit**, and the fastest ones become **"hot"** and start damaging things. This matters in modern transistors, which are so small that even a volt across them gives enormous fields.

**Story 2: what happens when we disturb the balance of carriers.** Light, or a forward-biased junction, can add **extra** electrons and holes beyond the equilibrium numbers. These extras do not last: they **recombine** and disappear. How long they last, the **lifetime**, controls how diodes switch, how transistors amplify and how well solar cells work.

## Part A: High-field effects

### Velocity saturation

At low fields carriers lose the energy they pick up from the field to small lattice vibrations, so they stay "cool" and v_d = μE.

At high fields (above about 10⁴ V/cm in Si) they pick up energy faster than they can lose it that way. Once a carrier has about 0.06 eV of extra energy (in Si), it can shake the lattice much harder by emitting an **optical phonon**, which takes that energy away in one go. So every time a carrier speeds up, it is quickly slowed down again. The drift velocity stops increasing and levels off at the **saturation velocity**:

    v_sat ≈ 1×10⁷ cm/s   (Si electrons and holes, at 300 K)

> **In plain words.** Pushing harder on a cyclist on a flat road makes them go faster, until air resistance grows so quickly that extra effort gives almost no extra speed. Optical phonons are the "air resistance" for carriers.

An empirical formula that joins the two regimes smoothly (Caughey–Thomas):

    v_d = μE / [ 1 + (μE/v_sat)^β ]^{1/β}      (β ≈ 2 for Si electrons, about 1 for holes)

Where:

- v_d = drift velocity (cm/s)
- μ = low-field mobility (cm²/V·s); Si μ_n = 1350, μ_p = 480
- E = electric field (V/cm)
- v_sat = saturation velocity, about 1×10⁷ cm/s in Si
- β = fitting exponent that sets how sharply the curve bends (dimensionless; not the transistor gain β)

At low field it reduces to μE; at high field to v_sat.

**GaAs is different.** Its electrons speed up to about 2×10⁷ cm/s near 3.5 kV/cm, and then actually **slow down** at higher fields, because they jump into a different part of the conduction band where they are heavier. A region where more field gives less current is called **negative differential mobility**; it is used in Gunn diodes to make microwave oscillators.

@fig figures/velocity.svg | Drift velocity against field. Silicon carriers level off near 10⁷ cm/s. GaAs electrons overshoot to about 2×10⁷ cm/s, then fall as they transfer to a heavier valley.

**Why it matters:** in a short-channel MOSFET the carriers are at v_sat across most of the channel, so the current depends on (V_GS − V_T) rather than (V_GS − V_T)² (Week 14), and the transistor speed is limited to about v_sat/(2πL).

### Hot-carrier effects

When carriers gain energy much faster than they lose it, their average energy rises far above the normal thermal energy. They are called **hot carriers** (their energy is described by an "electron temperature" T_e much higher than the crystal's temperature). Hot carriers cause:

1. **Velocity saturation** and reduced mobility (above).
2. **Impact ionisation.** A carrier with energy above about 1.5E_g can knock an electron out of a covalent bond when it collides, creating a new electron–hole pair. The new carriers are accelerated too and do the same: an **avalanche**. This causes **avalanche breakdown** of junctions (Week 10) and is used deliberately in avalanche photodiodes.
3. **Hot-carrier injection** into the gate oxide of MOSFETs. Near the drain, some electrons gain enough energy (over 3.1 eV) to jump over the Si/SiO₂ barrier into the oxide, where they get trapped or create defects. The threshold voltage slowly shifts and the transistor degrades over months or years: a key **reliability** problem.
4. **Substrate current** from holes created by impact ionisation, which can trigger unwanted bipolar action or latch-up in CMOS.
5. **Velocity overshoot** in very short devices, where carriers cross before they have time to reach v_sat, briefly going faster.

**Cures:** the **lightly doped drain (LDD)** structure, which spreads the voltage drop and lowers the peak field; lower supply voltages; better oxides.

## Part B: Generation and recombination

### Equilibrium and excess carriers

In thermal equilibrium, electron–hole pairs are being created (**generated**) by heat and destroyed (**recombined**) all the time, at exactly equal rates. That balance is what keeps n₀p₀ = n_i².

Now shine light on the sample, or inject carriers through a junction. We get **excess carriers**:

    n = n₀ + Δn,     p = p₀ + Δp

Where:

- n, p = actual electron and hole concentrations (cm⁻³)
- n₀, p₀ = equilibrium concentrations, with n₀p₀ = n_i² (cm⁻³)
- Δn, Δp = excess electron and hole concentrations (cm⁻³)

Light creates electrons and holes in pairs, so usually Δn = Δp. Now np > n_i², recombination is faster than generation, and the extras start disappearing.

**Low-level injection** means the excess is much smaller than the majority concentration (Δp ≪ n₀ in n-type). Then:

- the **majority** concentration hardly changes;
- the **minority** concentration may change enormously.

#### Example 8.1: what low-level injection does to each carrier

**Question.** n-type silicon with N_D = 1×10¹⁶ cm⁻³ (so p₀ = 1×10⁴ cm⁻³) is illuminated, creating Δn = Δp = 1×10¹⁴ cm⁻³ excess carriers. Calculate the new electron and hole concentrations and the factor by which each has changed.

**Given:** n₀ = 1×10¹⁶ cm⁻³, p₀ = 1×10⁴ cm⁻³, Δn = Δp = 1×10¹⁴ cm⁻³.

**Find:** n, p and their change factors.

**Formula:**

    n = n₀ + Δn,     p = p₀ + Δp

**Solution.**

    n = n₀ + Δn = 1×10¹⁶ + 1×10¹⁴ = 1.01×10¹⁶ cm⁻³   (n/n₀ = 1.01)

    p = p₀ + Δp = 1×10⁴ + 1×10¹⁴ ≈ 1×10¹⁴ cm⁻³      (p/p₀ = 10¹⁰)

**Answer:** **The electrons change by only 1 %; the holes increase ten-billion-fold.**

**What this means:** the conductivity (set mainly by the electrons) barely changes, but the hole population, and so the hole recombination and hole diffusion, changes enormously. This is why minority carriers control device behaviour: they are the ones that change. Since Δp = 10¹⁴ is only 1 % of n₀, this is low-level injection.

### How carriers are generated

1. **Thermal generation:** heat breaks a bond. Usually it happens in two small steps through a defect level in the gap, which is easier than one big jump.
2. **Optical generation:** a photon with energy hν ≥ E_g is absorbed and creates a pair. This is how photodiodes and solar cells work.
3. **Impact ionisation:** a hot carrier creates a pair (above).
4. **Tunnelling** across the gap at extremely high fields (Zener effect).

### How carriers recombine

@fig figures/recombination.svg | The three recombination paths. Band-to-band: the electron drops straight across and emits a photon. Shockley–Read–Hall: it drops in two steps via a trap in the gap, giving heat. Auger: the energy is handed to a third carrier.

1. **Direct (band-to-band, radiative).** An electron drops straight from the conduction band into a hole and emits a photon of energy ≈ E_g. Rate = B·np, where B is the radiative recombination coefficient (cm³/s). Strong in direct-gap GaAs (LEDs, lasers); very weak in indirect-gap Si (Week 4).
2. **Indirect (trap-assisted, Shockley–Read–Hall, SRH).** The electron drops in two steps through a **trap**, a localised energy level in the gap created by a defect or an impurity atom such as gold, iron or copper. The energy goes into lattice vibrations (heat). **This is the dominant mechanism in silicon.**
3. **Auger.** The energy released is given to a third carrier, which is kicked high into its band and then cools down. Important at very high carrier densities.
4. **Surface recombination:** SRH through the many traps at a surface (Week 9).

### The three recombination mechanisms compared

| | Shockley–Read–Hall (trap-assisted) | Radiative (band-to-band) | Auger |
|---|---|---|---|
| How it happens | Electron drops in two steps via a trap level E_t in the gap | Electron drops straight across the gap into a hole | Electron and hole recombine and hand the energy to a third carrier |
| Where the energy goes | Heat (lattice vibrations, phonons) | A photon of energy ≈ E_g (light) | Kinetic energy of the third carrier, then heat |
| Net rate | U = (np − n_i²)/[τ_p(n + n₁) + τ_n(p + p₁)]; ≈ Δp/τ_p at low level in n-type | R = B(np − n_i²) | R = (C_{n}n + C_{p}p)(np − n_i²) |
| What it depends on | Trap density N_t: τ = 1/(σv_thN_t) | Material: B ≈ 10⁻¹⁰ cm³/s (GaAs), ≈ 10⁻¹⁴ cm³/s (Si) | Carrier density squared: C ≈ 10⁻³¹ cm⁶/s in Si |
| Lifetime (low-level, majority density N) | τ = 1/(σv_thN_t): 1 ns – 1 ms in Si, set by purity | τ = 1/(BN): about 10 ns in GaAs at N = 10¹⁸ cm⁻³; about 10 ms in Si at 10¹⁶ cm⁻³ | τ ≈ 1/(CN²): about 0.1 μs at 10¹⁹ cm⁻³, about 1 ns at 10²⁰ cm⁻³ in Si |
| Where it dominates | Indirect-gap Si and Ge at normal doping; depletion regions | Direct-gap GaAs, InP, GaN | Very heavy doping or very high injection (emitters, lasers, power devices) |
| Where it matters in practice | Leakage current; gold or platinum doping for fast-switching diodes; solar-cell efficiency | LEDs and lasers (the light output) | Limits lifetime in heavily doped emitters; efficiency "droop" of LEDs at high current |

So in silicon the lifetime is almost always set by SRH (traps), except in very heavily doped regions, where Auger takes over; radiative recombination is too slow to matter.

### Shockley–Read–Hall recombination: how it works

Picture a trap level E_t in the middle of the gap. It can be empty or hold one electron. Four things can happen to it:

| Step | What happens | Result |
|---|---|---|
| 1. Electron capture | A conduction-band electron falls into the empty trap | Trap now full |
| 2. Electron emission | The trapped electron is shaken back up into the conduction band | Trap empty again |
| 3. Hole capture | The trapped electron drops down into the valence band, filling a hole | A hole disappears; trap empty |
| 4. Hole emission | A valence-band electron jumps up into the empty trap | A hole appears; trap full |

**Recombination** = step 1 then step 3: an electron and a hole have both disappeared, via the trap. **Generation** = step 4 then step 2: an electron and a hole have both been created.

> **In plain words.** It is much easier to go down a staircase two steps at a time than to jump the whole flight. A trap in the middle of the gap is a landing half-way down. That is why a few impurity atoms can make recombination enormously faster.

Working out the balance of the four steps gives the **SRH recombination rate**:

    U = (np − n_i²) / [ τ_p(n + n₁) + τ_n(p + p₁) ]

    τ_n = 1/(σ_n v_th N_t),   τ_p = 1/(σ_p v_th N_t)
    n₁ = n_i e^{(E_t − E_i)/kT},   p₁ = n_i e^{(E_i − E_t)/kT}

| Symbol | Meaning |
|---|---|
| U | net recombination rate (pairs per cm³ per second) |
| N_t | trap density (cm⁻³) |
| σ_n, σ_p | capture cross-sections: how "big a target" the trap is for electrons, holes (cm²) |
| v_th | thermal velocity, about 10⁷ cm/s |
| E_t | trap energy level (eV) |
| n, p | electron and hole concentrations (cm⁻³) |
| n_i | intrinsic carrier concentration, 1×10¹⁰ cm⁻³ in Si at 300 K |
| τ_n, τ_p | electron and hole lifetimes set by the traps (s) |
| n₁, p₁ | the electron and hole concentrations there would be if E_F were at E_t (cm⁻³) |
| E_i | intrinsic Fermi level, close to mid-gap (eV) |
| kT | thermal energy, 0.0259 eV at 300 K |

**What the formula tells you:**

1. **The top line, np − n_i², is the driving force.** If np > n_i² (extra carriers), U is positive: net recombination. If np < n_i² (carriers removed, as in a reverse-biased depletion region), U is negative: net **generation**, which is the source of diode leakage current. In equilibrium, np = n_i² and U = 0.
2. **U is largest when E_t is near mid-gap.** Traps near a band edge just catch and re-release carriers. **Mid-gap traps are the effective recombination centres.** Gold sits close to mid-gap, which is why it is used deliberately to make fast-switching diodes.
3. **More traps, faster recombination:** τ ∝ 1/N_t.
4. **Low-level injection in n-type** (n ≫ p): the formula simplifies to the short form below. The recombination rate is set by how fast the **minority** carriers (holes) get captured.

    U ≈ Δp / τ_p

Where:

- U = net recombination rate (cm⁻³s⁻¹)
- Δp = excess hole (minority-carrier) concentration (cm⁻³)
- τ_p = hole lifetime, 1/(σ_p v_th N_t) (s)

#### Example 8.2: lifetime from the trap density

**Question.** An n-type silicon wafer contains 1×10¹³ cm⁻³ mid-gap recombination centres with a hole capture cross-section of 1×10⁻¹⁵ cm². The thermal velocity is 1×10⁷ cm/s. Calculate the minority-carrier (hole) lifetime.

**Given:** N_t = 1×10¹³ cm⁻³, σ_p = 1×10⁻¹⁵ cm², v_th = 1×10⁷ cm/s.

**Find:** τ_p.

**Formula:**

    τ_p = 1/(σ_p v_th N_t)

**Solution.**

    τ_p = 1/(σ_p v_th N_t) = 1 / (10⁻¹⁵ × 10⁷ × 10¹³) = 1/10⁵ = 1×10⁻⁵ s

**Answer:** **τ_p = 10 μs.** Doubling the trap density would halve the lifetime.

**What this means:** a trap density of 10¹³ cm⁻³ is less than one atom in a billion of silicon (5×10²² atoms per cm³), yet it fixes the lifetime at 10 μs. A hole in this wafer survives about 10 μs before a trap catches it, which is why chip and solar-cell makers keep metal contamination so low.

## Part C: Lifetime and steady-state injection

### Minority-carrier lifetime

Switch off the light at t = 0. With U = Δp/τ_p, the excess holes decay as

    dΔp/dt = −Δp/τ_p   ⇒   Δp(t) = Δp(0) e^{−t/τ_p}

Where:

- Δp(t) = excess hole concentration at time t (cm⁻³)
- Δp(0) = excess hole concentration at switch-off, t = 0 (cm⁻³)
- t = time (s)
- τ_p = minority-carrier (hole) lifetime (s)

τ_p is the **minority-carrier lifetime**: the average time an extra minority carrier survives before it recombines. After one lifetime, 37 % (1/e) of the excess remains; after five lifetimes, under 1 %.

Typical values: very pure Si, 1 μs to 1 ms; gold-doped Si for fast switching, 1–10 ns; GaAs, 1–10 ns (fast radiative recombination).

If several mechanisms act together, their rates add: 1/τ = 1/τ_SRH + 1/τ_radiative + 1/τ_{Auger}.

@fig figures/decay.svg | Under steady illumination the excess holds at Δp = G_Lτ_p. When the light is switched off it decays exponentially, falling to 1/e in one lifetime.

### Steady-state excess carrier injection

Now keep the light on, generating G_L pairs per cm³ per second uniformly. The excess builds up until recombination exactly balances generation:

    dΔp/dt = G_L − Δp/τ_p = 0   ⇒   Δp = Δn = G_Lτ_p

Where:

- Δp, Δn = steady-state excess hole and electron concentrations (cm⁻³)
- G_L = generation rate by light (pairs per cm³ per second, cm⁻³s⁻¹)
- τ_p = minority-carrier (hole) lifetime (s)

**The excess equals the generation rate times the lifetime.** A long lifetime lets a large excess build up.

The extra carriers raise the conductivity, called **photoconductivity**:

    Δσ = q(μ_n + μ_p) Δn = q(μ_n + μ_p) G_Lτ

Where:

- Δσ = increase in conductivity caused by the light (S/cm)
- q = electronic charge, 1.6×10⁻¹⁹ C
- μ_n, μ_p = electron and hole mobilities (cm²/V·s)
- Δn = excess carrier concentration, equal to Δp (cm⁻³)
- G_L = generation rate (cm⁻³s⁻¹)
- τ = minority-carrier lifetime (s)

#### Example 8.3: photoconductivity

**Question.** n-type silicon with N_D = 1×10¹⁵ cm⁻³ and τ_p = 10 μs is uniformly illuminated, generating G_L = 1×10²⁰ electron–hole pairs per cm³ per second. Calculate the steady-state excess carrier concentration, the increase in conductivity, and compare it with the dark conductivity.

**Given:** N_D = 1×10¹⁵ cm⁻³, τ_p = 10 μs = 1×10⁻⁵ s, G_L = 1×10²⁰ cm⁻³s⁻¹, μ_n = 1350, μ_p = 480 cm²/V·s.

**Find:** Δn, Δσ and σ₀.

**Formula:**

    Δn = Δp = G_Lτ_p,     Δσ = q(μ_n + μ_p)Δn,     σ₀ = qN_Dμ_n

**Solution.**

Step 1. Steady state, generation = recombination:

    Δn = Δp = G_Lτ_p = 10²⁰ × 10⁻⁵ = 1×10¹⁵ cm⁻³

Step 2. Extra conductivity:

    Δσ = q(μ_n + μ_p)Δn = 1.6×10⁻¹⁹ × (1350 + 480) × 10¹⁵ = 0.293 S/cm

Step 3. Dark conductivity:

    σ₀ = qN_Dμ_n = 1.6×10⁻¹⁹ × 10¹⁵ × 1350 = 0.216 S/cm

**Answer:** **Δn = 10¹⁵ cm⁻³, Δσ = 0.293 S/cm, against σ₀ = 0.216 S/cm**: the conductivity more than doubles in the light.

**What this means:** the total conductivity in the light is 0.216 + 0.293 = 0.509 S/cm, about 2.4 times the dark value, so the sample's resistance falls to about 40 % of its dark value. The 10 μs lifetime is what lets so many extra carriers build up; with a 1 μs lifetime the effect would be ten times smaller.

This is how a light-dependent resistor works. (Here Δp equals n₀, so this is not low-level injection, and the single-lifetime formula is only approximate.)

### Quasi-Fermi levels

Out of equilibrium, np ≠ n_i², so a single Fermi level cannot describe both carriers. Instead we use **two**: one for electrons, E_{Fn}, and one for holes, E_{Fp}:

    n = n_i e^{(E_{Fn} − E_i)/kT},     p = n_i e^{(E_i − E_{Fp})/kT},     np = n_i² e^{(E_{Fn} − E_{Fp})/kT}

Where:

- n, p = electron and hole concentrations out of equilibrium (cm⁻³)
- n_i = intrinsic carrier concentration, 1×10¹⁰ cm⁻³ in Si at 300 K
- E_{Fn}, E_{Fp} = quasi-Fermi levels for electrons and holes (eV)
- E_i = intrinsic Fermi level, close to mid-gap (eV)
- kT = thermal energy, 0.0259 eV at 300 K

The **gap between them**, E_{Fn} − E_{Fp}, measures how far from equilibrium the material is. In a forward-biased diode it equals qV; in a solar cell it sets the open-circuit voltage. In equilibrium they merge back into one Fermi level.

## Key points of Week 8

- At high fields drift velocity saturates at v_sat ≈ 10⁷ cm/s (optical-phonon emission).
- Hot carriers cause impact ionisation (avalanche) and oxide damage in MOSFETs; LDD reduces them.
- Excess carriers: n = n₀ + Δn. Under low-level injection only the minority concentration changes much.
- Recombination: band-to-band (light, GaAs), SRH via traps (heat, dominant in Si), Auger (high density).
- SRH rate U = (np − n_i²)/[τ_p(n + n₁) + τ_n(p + p₁)]: mid-gap traps are most effective; τ = 1/(σv_thN_t).
- Low-level n-type: U = Δp/τ_p; after switch-off Δp(t) = Δp(0)e^{−t/τ_p}; under steady light Δp = G_Lτ_p.

---

## Examination questions solved (Q41–Q44)

### Q41. Explain velocity saturation and hot-carrier effects in semiconductors.

**Velocity saturation.** At low fields, drift velocity is proportional to the field, v_d = μE, because carriers lose the energy they gain from the field to the lattice (acoustic phonons) and stay near thermal equilibrium. As the field increases (above about 10³–10⁴ V/cm in Si), carriers gain energy faster than acoustic-phonon scattering can remove it. Once their energy reaches the optical-phonon energy (≈ 0.063 eV in Si), they emit optical phonons very rapidly, which transfers energy to the lattice efficiently and limits further gain. The drift velocity therefore stops increasing and approaches a **saturation velocity**:

    v_sat ≈ 10⁷ cm/s  (Si, 300 K)

and is described empirically by v_d = μE/[1 + (μE/v_sat)^β]^{1/β}. The effective mobility v_d/E falls at high field. In GaAs the electron velocity peaks at about 2×10⁷ cm/s then decreases (negative differential mobility) because electrons transfer to the heavier L-valley.

**Consequences:** in short-channel MOSFETs the drain current becomes proportional to (V_GS − V_T) rather than (V_GS − V_T)², and the maximum transconductance and transit-time-limited speed are set by v_sat: f_T ≈ v_sat/(2πL).

**Hot-carrier effects.** Under high fields, carriers acquire an average kinetic energy far greater than the thermal value (3/2)kT; they are described by an effective electron temperature T_e ≫ T. These "hot" carriers cause:

1. **Impact ionisation**: carriers with energy above about 1.5E_g break bonds and create electron–hole pairs, leading to avalanche multiplication and **avalanche breakdown** of junctions.
2. **Hot-carrier injection into gate oxides**: hot electrons near the drain of a MOSFET surmount the 3.1 eV Si/SiO₂ barrier, become trapped in the oxide or create interface traps. The threshold voltage shifts and transconductance degrades over the device's life (hot-carrier degradation).
3. **Substrate and gate currents**: impact-generated holes flow to the substrate, which can forward-bias source junctions and trigger parasitic bipolar action or CMOS latch-up.
4. **Velocity overshoot**: in very short channels carriers transit before scattering brings them to steady state, briefly exceeding v_sat.
5. **Increased noise and light emission.**

**Mitigation:** lightly doped drain (LDD) structures to reduce the peak field, reduced supply voltage, graded junctions, and nitrided or hardened gate oxides.

### Q42. What is meant by generation and recombination of charge carriers?

**Generation** is any process that creates free electron–hole pairs (or a free carrier from a dopant or trap) by giving an electron enough energy to move from the valence band (or a localised state) into the conduction band. The rate G is the number of pairs created per unit volume per unit time (cm⁻³s⁻¹). Mechanisms:

- **Thermal generation** by lattice vibrations, directly or through trap levels in the gap.
- **Optical generation** by absorption of photons with hν ≥ E_g (photodetectors, solar cells).
- **Impact ionisation** by energetic carriers in high fields (avalanche).
- **Tunnelling** generation at very high fields (Zener).

**Recombination** is the reverse: a conduction-band electron falls back to the valence band and fills a hole, so both carriers are annihilated. The released energy E_g appears as a photon, as heat (phonons), or as kinetic energy of a third carrier. The rate R has the same units. Mechanisms:

- **Direct (band-to-band, radiative)** recombination, emitting a photon; dominant in direct-gap materials.
- **Indirect (trap-assisted, SRH)** recombination through defect or impurity levels in the gap, releasing heat; dominant in Si.
- **Auger** recombination, energy given to a third carrier; dominant at high carrier density.
- **Surface** recombination through surface states.

**Equilibrium and non-equilibrium.** In thermal equilibrium the two processes balance (G_th = R_th), giving n₀p₀ = n_i². If excess carriers are introduced (np > n_i²), net recombination U = R − G > 0 restores equilibrium; if carriers are removed (np < n_i², e.g. a reverse-biased depletion region), net generation occurs. For low-level injection the net recombination rate is U = Δp/τ_p (n-type), where τ_p is the minority-carrier lifetime.

Generation and recombination govern the leakage current of diodes, the operation of solar cells, LEDs and photodetectors, the gain of BJTs and the switching speed of p-n junctions.

### Q43. Explain the Shockley-Read-Hall (SRH) recombination mechanism.

**Principle.** SRH (trap-assisted or indirect) recombination occurs through localised energy levels E_t in the forbidden gap introduced by crystal defects or impurities (e.g. Au, Fe, Cu, vacancies, dislocations). Instead of crossing the whole gap in one step, which in an indirect semiconductor requires an unlikely phonon-assisted transition, the electron makes two smaller steps via the trap, and the energy is released as lattice vibrations (phonons).

**The four processes** at a trap (density N_t, occupation probability f_t):

| Process | Description | Rate |
|---|---|---|
| (a) Electron capture | CB electron captured by an empty trap | r_a = v_thσ_n n N_t(1 − f_t) |
| (b) Electron emission | Trapped electron emitted to CB | r_b = e_n N_t f_t |
| (c) Hole capture | Trapped electron drops to VB, annihilating a hole | r_c = v_thσ_p p N_t f_t |
| (d) Hole emission | VB electron captured by empty trap, leaving a hole | r_d = e_p N_t(1 − f_t) |

**Recombination** = (a) then (c). **Generation** = (d) then (b).

**Derivation outline.** In steady state the trap occupation is constant, so the net electron capture rate equals the net hole capture rate: r_a − r_b = r_c − r_d = U. The emission coefficients follow from detailed balance in equilibrium: e_n = v_thσ_n n₁ and e_p = v_thσ_p p₁. Solving for f_t and substituting gives:

    U = (np − n_i²) / [ τ_p(n + n₁) + τ_n(p + p₁) ]

with τ_n = 1/(σ_n v_th N_t), τ_p = 1/(σ_p v_th N_t), n₁ = n_i e^{(E_t − E_i)/kT}, p₁ = n_i e^{(E_i − E_t)/kT}.

**Interpretation.**

1. The driving force is (np − n_i²): positive for excess carriers (recombination), negative for depletion (generation), zero in equilibrium.
2. U is maximum when E_t is near mid-gap (E_t ≈ E_i). Shallow levels near a band edge just re-emit carriers and are ineffective. **Deep, mid-gap levels are the effective recombination centres.**
3. U ∝ N_t: more traps give faster recombination and shorter lifetime.
4. For low-level injection in n-type material (n ≫ p, n₁, p₁): U = (p − p₀)/τ_p = Δp/τ_p. The rate is limited by capture of the minority carrier.
5. In a reverse-biased depletion region (n, p ≈ 0): U = −n_i/(τ_p + τ_n) ≈ −n_i/2τ₀, a net generation that produces the generation leakage current J_gen = qn_iW/2τ₀.

**Applications:** gold or platinum doping, or electron irradiation, is deliberately used to reduce lifetime in fast-switching diodes and thyristors. Conversely, gettering and clean processing reduce trap densities for long lifetimes in solar cells, CCDs and low-leakage devices.

### Q44. Define minority-carrier lifetime and explain its significance in semiconductor devices.

**Definition.** The minority-carrier lifetime is the average time an excess minority carrier exists in a semiconductor before it recombines with a majority carrier. For low-level injection, τ_p (holes in n-type) or τ_n (electrons in p-type) is defined by

    U = Δp / τ_p

so that, when generation stops, the excess density decays exponentially:

    Δp(t) = Δp(0) e^{−t/τ_p}

τ_p is the time for the excess to fall to 1/e (37 %) of its initial value. With SRH recombination, τ_p = 1/(σ_p v_th N_t): lifetime is inversely proportional to the trap density. Typical values: 1 ns to 1 ms in Si depending on purity.

**Significance:**

1. **Diffusion length.** Injected minority carriers diffuse an average distance L = √(Dτ) before recombining. In Si with D_p = 12 cm²/s and τ_p = 1 μs, L_p = √(12 × 10⁻⁶) = 35 μm. L determines how far carriers travel and therefore device dimensions.
2. **Diode current.** The saturation current J_s = qn_i²(D_p/(L_pN_D) + D_n/(L_nN_A)) depends on lifetime through L. Short lifetime raises leakage; generation current in the depletion region is ∝ 1/τ.
3. **Switching speed.** When a forward-biased diode is turned off, the stored minority charge Q = Iτ must be removed; the reverse-recovery time is ≈ τ. Fast-recovery and switching diodes are gold- or platinum-doped to cut τ to nanoseconds.
4. **BJT current gain.** Electrons injected into a p-type base must cross it before recombining. The base transport factor ≈ 1 − W_B²/2L_n², so long lifetime (L_n ≫ W_B) gives high β.
5. **Solar cells and photodetectors.** Photogenerated carriers must reach the junction before recombining; long lifetime (long L) means higher collection efficiency, current and efficiency.
6. **LEDs and lasers.** The radiative fraction of recombination, and the modulation speed (bandwidth ∝ 1/τ), depend on lifetime.
7. **Power devices.** In p-i-n diodes and IGBTs, long lifetime gives conductivity modulation and low on-state voltage but slow switching; there is a design trade-off.
8. **Material quality indicator.** Lifetime is very sensitive to metallic contamination, so it is measured (photoconductive decay, μ-PCD) to monitor crystal growth and process cleanliness.

---

## Practice questions

These extra questions practise this week's ideas. Work each one on paper before reading the solution; the calculation questions follow the same Question, Given, Find, Solution, Answer layout as the worked examples.

#### Practice 8.1: when does velocity saturate?

**Question.** Estimate the field at which electron drift in silicon starts to saturate (μ_n = 1350 cm²/V·s, v_sat = 1×10⁷ cm/s). Is a 100 nm MOSFET channel with 1 V across it saturated?

**Given:** μ_n = 1350 cm²/V·s, v_sat = 10⁷ cm/s, V = 1 V over L = 100 nm = 10⁻⁵ cm.

**Find:** E where μE = v_sat; the channel field.

**Solution.**

    E_sat ≈ v_sat/μ_n = 10⁷/1350 = 7.4×10³ V/cm
    Channel field ≈ V/L = 1/10⁻⁵ = 10⁵ V/cm

**Answer:** **E_sat ≈ 7.4 kV/cm; the channel field (100 kV/cm) is over ten times larger, so the carriers are fully velocity-saturated.**

#### Practice 8.2: gold as a lifetime killer

**Question.** A switching diode is doped with 1×10¹⁵ cm⁻³ gold atoms (σ = 1×10⁻¹⁵ cm², v_th = 1×10⁷ cm/s). Find the minority-carrier lifetime.

**Given:** N_t = 10¹⁵ cm⁻³, σ = 10⁻¹⁵ cm², v_th = 10⁷ cm/s.

**Find:** τ.

**Solution.**

    τ = 1/(σv_thN_t) = 1/(10⁻¹⁵ × 10⁷ × 10¹⁵) = 10⁻⁷ s

**Answer:** **τ = 100 ns**, short enough for a fast-recovery diode.

#### Practice 8.3: how long until the excess is gone?

**Question.** After the light is switched off, excess holes in n-type silicon decay with τ_p = 5 μs. How long does it take for the excess to fall to 1 % of its initial value?

**Given:** τ_p = 5 μs, Δp(t)/Δp(0) = 0.01.

**Find:** t.

**Solution.**

    e^{−t/τ} = 0.01   ⇒   t = τ ln(100) = 5 μs × 4.61 = 23 μs

**Answer:** **t ≈ 23 μs (about 4.6 lifetimes).**

#### Practice 8.4: steady-state injection level

**Question.** n-type silicon (N_D = 1×10¹⁶ cm⁻³, τ_p = 20 μs) is uniformly illuminated with G_L = 5×10¹⁹ cm⁻³s⁻¹. Find Δp and decide whether this is low-level injection.

**Given:** G_L = 5×10¹⁹ cm⁻³s⁻¹, τ_p = 2×10⁻⁵ s, N_D = 10¹⁶ cm⁻³.

**Find:** Δp and Δp/n₀.

**Solution.**

    Δp = G_Lτ_p = 5×10¹⁹ × 2×10⁻⁵ = 1×10¹⁵ cm⁻³
    Δp/n₀ = 10¹⁵/10¹⁶ = 0.1

**Answer:** **Δp = 10¹⁵ cm⁻³, 10 % of n₀**: borderline but usually treated as low-level injection.

#### Practice 8.5: quasi-Fermi level splitting

**Question.** n-type silicon with N_D = 1×10¹⁶ cm⁻³ is illuminated so that Δn = Δp = 1×10¹⁴ cm⁻³. Find E_Fn − E_i, E_i − E_Fp and the splitting E_Fn − E_Fp at 300 K.

**Given:** n = 1.01×10¹⁶, p ≈ 10¹⁴ cm⁻³, n_i = 10¹⁰ cm⁻³, kT = 0.0259 eV.

**Find:** the quasi-Fermi levels and their splitting.

**Solution.**

    E_{Fn} − E_i = kT ln(n/n_i) = 0.0259 ln(1.01×10⁶) = 0.358 eV
    E_i − E_{Fp} = kT ln(p/n_i) = 0.0259 ln(10⁴) = 0.239 eV
    E_{Fn} − E_{Fp} = 0.358 + 0.239 = 0.597 eV

**Answer:** **E_{Fn} = E_i + 0.358 eV, E_{Fp} = E_i − 0.239 eV, splitting ≈ 0.60 eV.** The electron level hardly moves; the hole level moves a long way.

#### Practice 8.6: generation current in a depletion region

**Question.** A reverse-biased silicon junction has a depletion width of 1 μm, area 10⁻³ cm² and effective lifetime τ₀ = 1 μs. Estimate the generation leakage current, J_gen = qn_iW/2τ₀.

**Given:** W = 10⁻⁴ cm, A = 10⁻³ cm², τ₀ = 10⁻⁶ s, n_i = 10¹⁰ cm⁻³.

**Find:** J_gen and I_gen.

**Solution.**

    J_gen = qn_iW/(2τ₀) = 1.6×10⁻¹⁹ × 10¹⁰ × 10⁻⁴ / (2×10⁻⁶) = 8×10⁻⁸ A/cm²
    I_gen = J_genA = 8×10⁻¹¹ A

**Answer:** **J_gen = 8×10⁻⁸ A/cm², I_gen = 80 pA.** In silicon this generation current usually exceeds the ideal diffusion leakage.

#### Practice 8.7: Auger versus SRH

**Question.** Explain why Auger recombination is important in heavily doped emitters but not in lightly doped bulk silicon.

**Answer.** Auger recombination needs three carriers to meet (the recombining electron and hole plus a third carrier that takes the energy), so its rate grows as n²p or np², much faster than SRH, which grows only linearly with the excess. In lightly doped silicon carrier densities are low and three-carrier encounters are rare, so SRH dominates. In emitters doped to 10¹⁹–10²⁰ cm⁻³ the majority density is enormous, Auger becomes the fastest path and it limits the minority-carrier lifetime.

---

## Objectives check

Use this table to confirm you have met this week's objectives. Cover the Answer column and answer each check question from memory. If you cannot, go back to the section in the last column before moving on.

| # | Objective | Check yourself | Answer | Where it is taught |
|---|---|---|---|---|
| 1 | Explain velocity saturation and its effect on devices. | What is the saturation velocity in Si and what causes it? | About 10⁷ cm/s; optical-phonon emission by energetic carriers. | Velocity saturation |
| 2 | Explain hot-carrier effects and how they are reduced. | How does a hot carrier cause avalanche breakdown? | It impact-ionises, creating new pairs that are accelerated and do the same. | Hot-carrier effects |
| 3 | Explain excess carriers and low-level injection. | Under low-level injection in n-type material, which carrier concentration changes significantly? | The minority (hole) concentration. | Equilibrium and excess carriers; Example 8.1 |
| 4 | Describe the generation and recombination mechanisms. | Which recombination mechanism dominates in silicon? | Shockley–Read–Hall (trap-assisted). | Generation; recombination; the three recombination mechanisms compared |
| 5 | Explain SRH recombination and calculate lifetime from trap data. | Why are mid-gap traps the most effective recombination centres? | They capture electrons and holes with similar ease; shallow traps just re-emit carriers. | SRH; Example 8.2 |
| 6 | Calculate decay of excess carriers and steady-state injection levels. | With G_L = 10¹⁹ cm⁻³s⁻¹ and τ = 2 μs, find Δp. | Δp = G_Lτ = 2×10¹³ cm⁻³. | Part C; Example 8.3 |
