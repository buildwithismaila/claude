# Week 8 — High-Field Effects and Excess Carriers
<!-- group: Module 3 · Carrier Transport & Injection Phenomena -->

**Plan:** velocity saturation and hot-carrier effects; generation and recombination mechanisms (Shockley–Read–Hall theory); carrier lifetime and steady-state excess carrier injection.

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

Light creates electrons and holes in pairs, so usually Δn = Δp. Now np > n_i², recombination is faster than generation, and the extras start disappearing.

**Low-level injection** means the excess is much smaller than the majority concentration (Δp ≪ n₀ in n-type). Then:

- the **majority** concentration hardly changes;
- the **minority** concentration may change enormously.

**Example.** n-Si with N_D = 10¹⁶ cm⁻³ has p₀ = 10⁴ cm⁻³. Light adds Δn = Δp = 10¹⁴ cm⁻³. Electrons: 1.01×10¹⁶ (a 1 % change). Holes: 10¹⁴, ten billion times their equilibrium value. **This is why minority carriers control device behaviour**: they are the ones that change.

### How carriers are generated

1. **Thermal generation:** heat breaks a bond. Usually it happens in two small steps through a defect level in the gap, which is easier than one big jump.
2. **Optical generation:** a photon with energy hν ≥ E_g is absorbed and creates a pair. This is how photodiodes and solar cells work.
3. **Impact ionisation:** a hot carrier creates a pair (above).
4. **Tunnelling** across the gap at extremely high fields (Zener effect).

### How carriers recombine

@fig figures/recombination.svg | The three recombination paths. Band-to-band: the electron drops straight across and emits a photon. Shockley–Read–Hall: it drops in two steps via a trap in the gap, giving heat. Auger: the energy is handed to a third carrier.

1. **Direct (band-to-band, radiative).** An electron drops straight from the conduction band into a hole and emits a photon of energy ≈ E_g. Rate = B·np. Strong in direct-gap GaAs (LEDs, lasers); very weak in indirect-gap Si (Week 4).
2. **Indirect (trap-assisted, Shockley–Read–Hall, SRH).** The electron drops in two steps through a **trap**, a localised energy level in the gap created by a defect or an impurity atom such as gold, iron or copper. The energy goes into lattice vibrations (heat). **This is the dominant mechanism in silicon.**
3. **Auger.** The energy released is given to a third carrier, which is kicked high into its band and then cools down. Important at very high carrier densities.
4. **Surface recombination:** SRH through the many traps at a surface (Week 9).

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
| E_t | trap energy level |

**What the formula tells you:**

1. **The top line, np − n_i², is the driving force.** If np > n_i² (extra carriers), U is positive: net recombination. If np < n_i² (carriers removed, as in a reverse-biased depletion region), U is negative: net **generation**, which is the source of diode leakage current. In equilibrium, np = n_i² and U = 0.
2. **U is largest when E_t is near mid-gap.** Traps near a band edge just catch and re-release carriers. **Mid-gap traps are the effective recombination centres.** Gold sits close to mid-gap, which is why it is used deliberately to make fast-switching diodes.
3. **More traps, faster recombination:** τ ∝ 1/N_t.
4. **Low-level injection in n-type** (n ≫ p): the formula simplifies to

    U ≈ Δp / τ_p

   The recombination rate is set by how fast the **minority** carriers (holes) get captured.

**Example.** N_t = 10¹³ cm⁻³, σ_p = 10⁻¹⁵ cm², v_th = 10⁷ cm/s: τ_p = 1/(10⁻¹⁵ × 10⁷ × 10¹³) = 10⁻⁵ s = **10 μs**.

## Part C: Lifetime and steady-state injection

### Minority-carrier lifetime

Switch off the light at t = 0. With U = Δp/τ_p, the excess holes decay as

    dΔp/dt = −Δp/τ_p   ⇒   Δp(t) = Δp(0) e^{−t/τ_p}

τ_p is the **minority-carrier lifetime**: the average time an extra minority carrier survives before it recombines. After one lifetime, 37 % (1/e) of the excess remains; after five lifetimes, under 1 %.

Typical values: very pure Si, 1 μs to 1 ms; gold-doped Si for fast switching, 1–10 ns; GaAs, 1–10 ns (fast radiative recombination).

If several mechanisms act together, their rates add: 1/τ = 1/τ_SRH + 1/τ_radiative + 1/τ_Auger.

@fig figures/decay.svg | Under steady illumination the excess holds at Δp = G_Lτ_p. When the light is switched off it decays exponentially, falling to 1/e in one lifetime.

### Steady-state excess carrier injection

Now keep the light on, generating G_L pairs per cm³ per second uniformly. The excess builds up until recombination exactly balances generation:

    dΔp/dt = G_L − Δp/τ_p = 0   ⇒   Δp = Δn = G_Lτ_p

**The excess equals the generation rate times the lifetime.** A long lifetime lets a large excess build up.

The extra carriers raise the conductivity, called **photoconductivity**:

    Δσ = q(μ_n + μ_p) Δn = q(μ_n + μ_p) G_Lτ

**Example.** n-Si (N_D = 10¹⁵ cm⁻³, τ_p = 10 μs) under light with G_L = 10²⁰ cm⁻³s⁻¹:

    Δn = Δp = G_Lτ_p = 10²⁰ × 10⁻⁵ = 10¹⁵ cm⁻³
    Δσ = 1.6×10⁻¹⁹ × (1350 + 480) × 10¹⁵ = 0.293 S/cm
    dark conductivity σ₀ = qN_Dμ_n = 1.6×10⁻¹⁹ × 10¹⁵ × 1350 = 0.216 S/cm

The conductivity more than doubles in the light. This is how a light-dependent resistor works. (Here Δp equals n₀, so this is not low-level injection, and the single-lifetime formula is only approximate.)

### Quasi-Fermi levels

Out of equilibrium, np ≠ n_i², so a single Fermi level cannot describe both carriers. Instead we use **two**: one for electrons, E_Fn, and one for holes, E_Fp:

    n = n_i e^{(E_Fn − E_i)/kT},     p = n_i e^{(E_i − E_Fp)/kT},     np = n_i² e^{(E_Fn − E_Fp)/kT}

The **gap between them**, E_Fn − E_Fp, measures how far from equilibrium the material is. In a forward-biased diode it equals qV; in a solar cell it sets the open-circuit voltage. In equilibrium they merge back into one Fermi level.

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
