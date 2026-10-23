# Week 10 — The p-n Junction Diode
<!-- group: Module 4 · Junctions, Interfaces & Characterisation -->

**Plan:** built-in potential, depletion width and electric-field profile; ideal diode (Shockley) equation derivation under forward and reverse bias.

## Learning objectives

By the end of this week you should be able to:

1. Explain the formation of the depletion region in a p-n junction.
2. Derive and calculate the built-in potential.
3. Calculate the depletion width and electric-field profile.
4. Explain the junction under forward and reverse bias and the law of the junction.
5. Derive and use the Shockley diode equation.
6. Explain breakdown and junction capacitance.

## Symbols and abbreviations used this week

Every symbol, constant and abbreviation on this page is listed here, even if an earlier week already defined it, so you can study this page on its own.

**Constants and units**

| Symbol | Meaning | Units / typical value |
|---|---|---|
| q | Magnitude of the electronic charge | 1.6×10⁻¹⁹ C |
| k | Boltzmann constant | 8.617×10⁻⁵ eV/K = 1.381×10⁻²³ J/K |
| kT | Thermal energy | 0.0259 eV (often 0.02585 eV) at 300 K |
| kT/q | Thermal voltage | 0.0259 V (about 26 mV) at 300 K |
| T | Absolute temperature | kelvin (K); room temperature = 300 K |
| ε_s (ε_si) | Permittivity of silicon, 11.7ε₀ | 1.04×10⁻¹² F/cm |
| eV | Electron-volt, a unit of energy | 1 eV = 1.6×10⁻¹⁹ J |
| μm | Micrometre (micron) | 1 μm = 10⁻⁴ cm = 10⁻⁶ m |

**Symbols**

| Symbol | Meaning | Units / typical value |
|---|---|---|
| E_c (E_C) | Energy of the bottom of the conduction band | eV |
| E_v (E_V) | Energy of the top of the valence band | eV |
| E_g | Band-gap energy, E_c − E_v | eV; Si 1.12, Ge 0.66, GaAs 1.42 at 300 K |
| E_F | Fermi level: the energy at which a state has a 50 % chance of being occupied | eV |
| E_i | Intrinsic Fermi level, close to mid-gap | eV |
| p | Hole concentration (holes per cm³) | cm⁻³ |
| n_i | Intrinsic carrier concentration (n = p = n_i in pure material) | cm⁻³; Si ≈ 1×10¹⁰ at 300 K |
| p_n0, n_p0 | Equilibrium minority concentrations: holes on the n side, electrons on the p side | cm⁻³; p_n0 = n_i²/N_D |
| N_D | Donor concentration | cm⁻³ |
| N_A | Acceptor concentration | cm⁻³ |
| N_D⁺, N_A⁻ | Concentrations of ionised donors and acceptors | cm⁻³ |
| Δn, Δp | Excess electron and hole concentrations above equilibrium | cm⁻³ |
| E (field) | Electric field (on band diagrams, E is energy instead) | V/cm |
| μ, μ_n, μ_p | Mobility: drift velocity per unit field (electrons, holes) | cm²/(V·s); Si μ_n 1350, μ_p 480 |
| J, J_n, J_p | Current density (total, electrons, holes) | A/cm² |
| D_n, D_p | Diffusion coefficients of electrons and holes | cm²/s; Si 35 and 12.4 |
| τ, τ_n, τ_p | Minority-carrier lifetime (τ_eff: effective, including surfaces) | s; Si 1 ns – 1 ms |
| L, L_n, L_p | Diffusion length √(Dτ): distance a minority carrier travels before recombining | μm or cm |
| V_bi | Built-in potential of a junction or Schottky contact | V; typically 0.5–1 V |
| V, V_a | Applied voltage (positive for forward bias) | V |
| W | Depletion-region width (in Week 13 W_B, W_E are base and emitter widths; in Week 14 W is channel width) | μm or cm |
| x_n, x_p | Parts of the depletion region on the n side and on the p side | μm |
| E_max | Peak electric field, at the junction | V/cm |
| I_s, J_s (I_S) | Saturation current (density) of a diode or transistor | A; A/cm² |
| I | Current | A |
| A (area) | Device or contact area | cm² |
| η | Ideality factor of a diode, 1 (ideal) to 2 | dimensionless |
| C, C_j | Capacitance (junction or depletion capacitance) | F (pF = 10⁻¹² F) |
| V_BR | Breakdown voltage | V |
| n_n0, p_p0, p_n0, n_p0 | Equilibrium densities: majority (n_n0, p_p0) and minority (p_n0 holes on n side, n_p0 electrons on p side) | cm⁻³ |
| Δp_n, Δn_p | Excess minority carriers at the depletion edges (holes on n side, electrons on p side) | cm⁻³ |
| p_n, n_p | Minority-carrier density: holes on the n side, electrons on the p side | cm⁻³ |
| ΔV, ΔV_BE | A small change in a voltage | V |

**Abbreviations**

| Abbreviation | Meaning |
|---|---|
| Si | Silicon |
| Ge | Germanium |
| C-V | Capacitance–voltage (measurement or characteristic) |
| MOSFET | Metal–oxide–semiconductor field-effect transistor |
| BJT | Bipolar junction transistor |
| LED | Light-emitting diode |
| n⁺ | Very heavily doped n-type (similarly p⁺) |


## Key terms

Every important word used this week is defined here, so you can read this week on its own.

**Band gap (E_g).** The range of energies between the top of the valence band (E_v) and the bottom of the conduction band (E_c) in which a perfect crystal has no allowed electron states. For silicon it is 1.12 eV at 300 K.

**Electron and hole.** An electron is a free negative charge carrier in the conduction band. A hole is an empty state left in the valence band when an electron leaves it; it moves like a positive charge carrier.

**Intrinsic carrier concentration (n_i).** The density of electrons (equal to the density of holes) in a pure, undoped semiconductor, created by heat alone. For silicon at 300 K it is about 1×10¹⁰ cm⁻³; it rises very steeply with temperature.

**Doping (N_D, N_A).** Adding small, controlled amounts of impurity atoms. Donors (density N_D) give electrons and make the material n-type; acceptors (density N_A) take electrons, create holes and make it p-type. Once they have given up or taken an electron, the donor and acceptor ions are charged and fixed in the crystal.

**Majority and minority carriers.** In n-type material electrons are the majority carriers and holes the minority carriers; in p-type material it is the other way round. In equilibrium the minority density follows from the mass-action law np = n_i².

    p_n0 = n_i²/N_D,     n_p0 = n_i²/N_A

Where:

- p_n0 = equilibrium hole (minority) density on the n side (cm⁻³)
- n_p0 = equilibrium electron (minority) density on the p side (cm⁻³)
- n_i = intrinsic carrier concentration (cm⁻³)
- N_D, N_A = donor and acceptor concentrations (cm⁻³)

*Why it matters:* the diode current is carried by minority carriers, so it is set by these tiny densities.

**Fermi level (E_F).** The energy at which an electron state has a 50 % chance of being occupied. In n-type material it lies near E_c, in p-type near E_v. In equilibrium it is flat (the same energy) everywhere in a connected system.

**Drift and diffusion.** The two ways carriers move. Drift is motion pushed by an electric field; diffusion is the spreading of carriers from where there are many to where there are few.

**p-n junction.** The boundary between a p-type region and an n-type region in one continuous crystal. On its own it forms a diode, which conducts easily in one direction only (rectification).

**Depletion region (W).** The thin layer on both sides of the junction that has lost almost all its mobile carriers, leaving only the fixed charged donor and acceptor ions. It is also called the space-charge region and is typically 0.1–10 μm wide.

*Why it matters:* all the applied voltage appears across this region, and its width sets the junction capacitance and the breakdown voltage.

**Built-in potential (V_bi).** The voltage that appears across the depletion region in equilibrium, created by the fixed ion charges. It is the barrier that stops further diffusion of majority carriers.

    V_bi = (kT/q) ln( N_{A}N_D / n_i² )

Where:

- V_bi = built-in potential (V)
- kT/q = thermal voltage, 0.0259 V at 300 K
- N_A, N_D = acceptor and donor concentrations (cm⁻³)
- n_i = intrinsic carrier concentration, 1×10¹⁰ cm⁻³ for Si at 300 K

**Depletion approximation.** The simplifying assumption that the depletion region contains no mobile carriers at all and has sharp edges, while the regions outside it are exactly neutral.

**Forward and reverse bias (V_a).** Forward bias makes the p side positive (V_a > 0) and lowers the barrier to V_bi − V_a; reverse bias makes the p side negative (V_a < 0) and raises the barrier to V_bi + |V_a|.

**Minority-carrier injection (law of the junction).** Under forward bias, majority carriers cross the lowered barrier and become minority carriers on the other side. The minority density at the edge of the depletion region rises exponentially with voltage.

    p_n(x_n) = p_n0 e^{qV_a/kT}

Where:

- p_n(x_n) = hole density at the n-side edge of the depletion region (cm⁻³)
- p_n0 = equilibrium hole density on the n side (cm⁻³)
- V_a = applied voltage (V), positive for forward bias
- kT/q = 0.0259 V at 300 K

**Minority-carrier lifetime and diffusion length (τ, L).** The lifetime τ is the average time an injected minority carrier survives before it recombines; the diffusion length L = √(Dτ) is the average distance it diffuses in that time (D is the diffusion coefficient, cm²/s).

**Saturation current (I_s).** The small, almost voltage-independent current that flows under reverse bias, carried by minority carriers that diffuse to the depletion region and are swept across. In small silicon diodes it is about 10⁻¹⁵–10⁻¹² A.

**Shockley (ideal diode) equation.** The current–voltage law of an ideal p-n junction, obtained by adding up the minority-carrier diffusion currents on both sides.

    I = I_s ( e^{qV/kT} − 1 )

Where:

- I = diode current (A), positive in the forward direction
- I_s = saturation current (A)
- V = applied voltage (V), positive for forward bias
- kT/q = thermal voltage, 0.0259 V at 300 K

*Why it matters:* it explains rectification: current grows tenfold for every 60 mV of forward bias but stays at −I_s in reverse.

**Breakdown (V_BR).** The sudden, large rise of reverse current at a high enough reverse voltage V_BR, caused either by avalanche multiplication or by Zener tunnelling. It is not destructive if the current is limited.

**Junction capacitance (C_j).** The capacitance of the depletion region, which acts like a parallel-plate capacitor whose plate spacing W grows with reverse bias.

    C_j = ε_sA/W

Where:

- C_j = junction (depletion) capacitance (F)
- ε_s = permittivity of silicon, 1.04×10⁻¹² F/cm
- A = junction area (cm²)
- W = depletion width (cm)

## The big picture

A **p-n junction** is what you get when one part of a single crystal is p-type and the part next to it is n-type. It is the most important structure in electronics: it is a diode on its own, two of them make a bipolar transistor, and it appears in every MOSFET, solar cell, LED and laser.

Its key property is that it conducts easily one way and hardly at all the other way (**rectification**). This week explains why, using only ideas you already have:

1. **Diffusion** (Week 7) makes carriers cross the junction, leaving fixed charges behind.
2. Those charges create an **electric field and a built-in voltage**, which stops further diffusion.
3. An applied voltage raises or lowers that barrier. Lowering it lets minority carriers be **injected**, and they **diffuse and recombine** (Weeks 8–9). Adding up that diffusion gives the diode equation.

## Forming the junction: where the depletion region comes from

Imagine joining p-type silicon (lots of holes, doping N_A) and n-type silicon (lots of electrons, doping N_D) in one crystal.

1. **Diffusion starts.** There are many holes on the p side and very few on the n side, so holes diffuse from p into n. Electrons diffuse the other way, from n into p.
2. **Fixed charges are uncovered.** Each hole that leaves the p side leaves behind a negative acceptor ion (N_A⁻), which is locked in the crystal and cannot move. Each electron that leaves the n side leaves behind a positive donor ion (N_D⁺). The carriers that cross also recombine with the majority carriers on the other side and disappear.
3. **A charged layer forms.** Near the junction there is now a layer of **negative** ions on the p side and **positive** ions on the n side, with almost no mobile carriers in it. This is the **depletion region** (also called the space-charge region).
4. **The charges create a field.** Positive charge on the n side and negative on the p side create an electric field pointing from n to p.
5. **The field pushes back.** That field drives holes back to the p side and electrons back to the n side: a **drift** current opposite to the diffusion current.
6. **Balance.** The depletion region grows until, for each type of carrier, drift exactly cancels diffusion. Now no net current flows. The **Fermi level is flat** across the whole junction, as it must be in equilibrium (Week 5).

@fig figures/pn-junction.svg | The abrupt p-n junction in equilibrium. Top: the fixed charge in the depletion region (negative on the p side, positive on the n side). Middle: the electric field, strongest at the junction. Bottom: the band diagram; the Fermi level is flat and the bands bend by qV_bi.

> **In plain words.** Two crowds on either side of a line start mixing. But everyone who crosses leaves a tied-up dog behind, and the dogs bark at anyone trying to follow. Soon the barking (the field) is strong enough to stop the crossing. The strip full of dogs and empty of people is the depletion region.

## The built-in potential

The field in the depletion region corresponds to a voltage across it, the **built-in potential V_bi**. The n side is at a higher potential than the p side. In the band diagram, the bands on the p side sit higher than on the n side by qV_bi.

We can find V_bi from the Fermi-level positions of Week 5. On the p side, E_F is kT ln(N_A/n_i) below E_i. On the n side it is kT ln(N_D/n_i) above E_i. In the joined junction E_F is one flat line, so the bands must bend by the sum:

    qV_bi = kT ln(N_A/n_i) + kT ln(N_D/n_i)

    V_bi = (kT/q) ln( N_A N_D / n_i² )

Where:

- V_bi = built-in potential (V)
- kT/q = thermal voltage, 0.0259 V at 300 K (kT = 0.0259 eV is the thermal energy)
- N_A = acceptor concentration on the p side (cm⁻³)
- N_D = donor concentration on the n side (cm⁻³)
- n_i = intrinsic carrier concentration, 1×10¹⁰ cm⁻³ for Si at 300 K

#### Example 10.1: built-in potential

**Question.** A silicon p-n junction has N_A = 1×10¹⁷ cm⁻³ on the p side and N_D = 1×10¹⁶ cm⁻³ on the n side. Calculate the built-in potential at 300 K.

**Given:** N_A = 1×10¹⁷ cm⁻³, N_D = 1×10¹⁶ cm⁻³, n_i = 1×10¹⁰ cm⁻³, kT/q = 0.0259 V.

**Find:** V_bi.

**Formula:**

    V_bi = (kT/q) ln( N_{A}N_D / n_i² )

**Solution.**

    V_bi = (kT/q) ln(N_{A}N_D/n_i²) = 0.0259 × ln(10¹⁷ × 10¹⁶ / 10²⁰)

         = 0.0259 × ln(10¹³) = 0.0259 × 29.93 = 0.775 V

**Answer:** **V_bi = 0.775 V.**

**What this means:** a majority carrier must climb an energy barrier of 0.775 eV, about 30 times the thermal energy kT, to cross the junction, so in equilibrium almost none do. The barrier is less than the band gap (1.12 eV), as it always is for non-degenerate doping.

You **cannot** measure V_bi with a voltmeter across a diode: where the wires meet the semiconductor, contact potentials appear that exactly cancel it. It is an internal barrier, not a battery.

## Depletion width and field: the depletion approximation

To calculate the width of the depletion region we make the **depletion approximation**: inside the region (from −x_p on the p side to x_n on the n side) there are no mobile carriers at all, only the fixed ions; outside it the material is neutral. Then Poisson's equation (the link between charge and field) gives:

**Charge balance.** The total negative charge equals the total positive charge:

    N_A x_p = N_D x_n

Where:

- N_A, N_D = acceptor and donor concentrations (cm⁻³)
- x_p = width of the depletion region on the p side (cm)
- x_n = width of the depletion region on the n side (cm)

So the depletion region extends **further into the more lightly doped side**. If N_A = 10 × N_D, then x_n = 10 × x_p.

**Width.**

    W = x_n + x_p = √( (2ε_s/q)(V_bi − V_a)(1/N_A + 1/N_D) )

with x_n = W N_A/(N_A + N_D) and x_p = W N_D/(N_A + N_D).

Where:

- W = total depletion width, x_n + x_p (cm)
- ε_s = permittivity of silicon, 11.7 × 8.854×10⁻¹⁴ = 1.04×10⁻¹² F/cm
- q = electronic charge, 1.6×10⁻¹⁹ C
- V_bi = built-in potential (V)
- V_a = applied voltage (V), positive for forward bias, negative for reverse bias
- N_A, N_D = acceptor and donor concentrations (cm⁻³)

**Peak field** (at the junction):

    E_max = qN_D x_n/ε_s = qN_A x_p/ε_s,   and   V_bi − V_a = ½ E_max W

Where:

- E_max = peak electric field, at the metallurgical junction (V/cm)
- q, N_A, N_D, x_n, x_p, ε_s, V_bi, V_a, W = as above

The field is a triangle: zero at the edges of the depletion region, rising linearly to E_max at the junction. The area of that triangle, ½E_maxW, is the voltage across the region.

For a **one-sided p⁺n junction** (N_A ≫ N_D), almost all of W is on the n side: W ≈ √(2ε_s(V_bi − V_a)/qN_D).

#### Example 10.2: depletion width and peak field

**Question.** For the junction of Example 10.1 at zero bias, calculate the total depletion width, how much of it lies on each side, and the peak electric field.

**Given:** V_bi = 0.775 V, N_A = 10¹⁷ cm⁻³, N_D = 10¹⁶ cm⁻³, ε_s = 1.04×10⁻¹² F/cm, q = 1.6×10⁻¹⁹ C, V_a = 0.

**Find:** W, x_n, x_p and E_max.

**Formula:**

    W = √( (2ε_s/q)(V_bi − V_a)(1/N_A + 1/N_D) ),     x_n = W N_A/(N_A + N_D),     E_max = qN_D x_n/ε_s

**Solution.**

Step 1. Total width:

    W = √( (2ε_s/q) V_bi (1/N_A + 1/N_D) )

      = √( 2 × 1.04×10⁻¹² × 0.775 × (10⁻¹⁷ + 10⁻¹⁶) / 1.6×10⁻¹⁹ ) = √(1.10×10⁻⁹) = 3.32×10⁻⁵ cm

Step 2. Split, using x_n = W N_A/(N_A + N_D):

    x_n = 0.332 × 10/11 = 0.30 μm,   x_p = 0.332 − 0.30 = 0.03 μm

Step 3. Peak field at the junction:

    E_max = qN_Dx_n/ε_s = 1.6×10⁻¹⁹ × 10¹⁶ × 3.0×10⁻⁵ / 1.04×10⁻¹² = 4.7×10⁴ V/cm

**Answer:** **W = 0.33 μm (0.30 μm on the n side, 0.03 μm on the p side), E_max = 4.7×10⁴ V/cm.**

**What this means:** the region is only a third of a micrometre wide, and 90 % of it lies in the more lightly doped n side. Yet the field in it, 47 kV/cm (4.7 MV/m), is enormous by everyday standards; it is this strong field that sweeps any carrier arriving at the depletion region straight across.

## The junction under bias

**Forward bias** (p side made positive, V_a > 0). The applied voltage opposes the built-in voltage, so the barrier **falls** to V_bi − V_a and the depletion region **narrows**. Diffusion now wins over drift. Holes pour from p into n, and electrons from n into p. On arrival they are minority carriers: they are **injected**. They diffuse away from the junction and recombine (Week 9). The current rises steeply (exponentially) with voltage.

**Reverse bias** (p side negative, V_a < 0). The applied voltage adds to the built-in voltage. The barrier **rises** to V_bi + |V_a| and the depletion region **widens**. Diffusion is shut off. The only current left is the tiny drift of the few minority carriers that happen to wander to the edge of the depletion region and get swept across. This is the **reverse saturation current**, almost independent of voltage, until breakdown.

**The law of the junction.** The barrier controls how many carriers can be injected. At the edges of the depletion region, the minority-carrier concentrations become:

    p_n(x_n) = p_n0 e^{qV_a/kT},     n_p(−x_p) = n_p0 e^{qV_a/kT}

Where:

- p_n(x_n) = hole density at the n-side edge of the depletion region (cm⁻³)
- n_p(−x_p) = electron density at the p-side edge of the depletion region (cm⁻³)
- p_n0 = n_i²/N_D and n_p0 = n_i²/N_A = equilibrium minority concentrations (cm⁻³)
- V_a = applied voltage (V), positive for forward bias
- kT/q = thermal voltage, 0.0259 V at 300 K

Forward bias multiplies the minority densities by e^{qV_a/kT}; reverse bias makes them almost zero. Every 60 mV of forward bias multiplies the injected minority carriers by 10.

### Forward and reverse bias compared

The numbers in the depletion-width row are for the junction of Examples 10.1 and 10.2 (N_A = 10¹⁷, N_D = 10¹⁶ cm⁻³, V_bi = 0.775 V).

| | Forward bias | Reverse bias |
|---|---|---|
| Connection | p side positive, n side negative (V_a > 0) | p side negative, n side positive (V_a < 0) |
| Barrier height | Lowered to V_bi − V_a | Raised to V_bi + \|V_a\| |
| Depletion width | Narrower (0.20 μm at V_a = +0.5 V) | Wider (0.91 μm at V_a = −5 V); W ∝ √(V_bi + \|V_a\|) |
| Peak field | Smaller | Larger |
| Minority carriers at the depletion edges | Increased by e^{qV_a/kT}: carriers are injected | Reduced almost to zero: carriers are extracted |
| Dominant current | Diffusion of injected minority carriers | Drift of the few minority carriers that reach the depletion region |
| Current size | Large; rises tenfold every 60 mV, I ≈ I_s e^{qV/kT} | Tiny and nearly constant, I ≈ −I_s, until breakdown |
| Resistance | Low | Very high |
| Main capacitance | Diffusion capacitance (from stored minority carriers) | Junction (depletion) capacitance C_j = ε_sA/W, falling as \|V_a\| rises |
| Typical uses | Rectifier conduction, LEDs, the emitter junction of a BJT | Blocking in rectifiers, photodiodes, varactors, Zener regulators, the collector junction of a BJT |

## The ideal diode (Shockley) equation, in words

The full derivation is worked in exam question Q48 below. The idea in four steps:

1. **Injection.** The law of the junction gives the excess minority carriers at each edge of the depletion region: Δp = p_n0(e^{qV/kT} − 1) on the n side.
2. **Diffusion and recombination.** In each neutral region the excess decays exponentially over a diffusion length (Week 9): Δp(x) = Δp(x_n)e^{−(x − x_n)/L_p}.
3. **Current at the edge.** The diffusion current at the edge is qD_p × slope = (qD_p/L_p)Δp(x_n). Same for electrons on the p side.
4. **Add them.** The total current is the sum of the hole and electron diffusion currents:

    I = I_s ( e^{qV/kT} − 1 ),     I_s = qA n_i² ( D_p/(L_pN_D) + D_n/(L_nN_A) )

Where:

- I = diode current (A), positive in the forward direction
- I_s = saturation current (A)
- V = applied voltage (V), positive for forward bias
- kT/q = thermal voltage, 0.0259 V at 300 K
- q = electronic charge, 1.6×10⁻¹⁹ C
- A = junction area (cm²)
- n_i = intrinsic carrier concentration, 1×10¹⁰ cm⁻³ for Si at 300 K
- D_p, D_n = diffusion coefficients of holes (in the n region) and electrons (in the p region) (cm²/s)
- L_p, L_n = diffusion lengths of holes and electrons, √(D_pτ_p) and √(D_nτ_n) (cm)
- N_D, N_A = donor and acceptor concentrations (cm⁻³)

@fig figures/diode-iv.svg | The ideal diode characteristic. Forward current grows ten times for every 60 mV at 300 K; reverse current is a tiny −I_s.

**What the equation says:**

- **Forward** (V > about 0.1 V): the −1 is negligible and I ≈ I_s e^{qV/kT}. Because I_s is tiny (10⁻¹⁵–10⁻¹² A for small Si diodes), a noticeable current needs about 0.6–0.7 V in Si (0.2–0.3 V in Ge).
- **Reverse** (V negative, more than a few kT/q): e^{qV/kT} → 0 and I ≈ −I_s, tiny and constant.
- I_s ∝ n_i², so it rises steeply with temperature and is much larger in small-gap materials (Ge diodes leak far more than Si).

#### Example 10.3: saturation current and forward current of a diode

**Question.** A silicon p⁺n diode has N_D = 1×10¹⁶ cm⁻³ on the n side, hole diffusion coefficient D_p = 10 cm²/s, hole lifetime τ_p = 1 μs and area 10⁻⁴ cm². Calculate the saturation current, and the forward current at 0.6 V and at 0.7 V (300 K).

**Given:** N_D = 10¹⁶ cm⁻³, D_p = 10 cm²/s, τ_p = 10⁻⁶ s, A = 10⁻⁴ cm², n_i = 10¹⁰ cm⁻³, kT/q = 0.0259 V.

**Find:** I_s, I(0.6 V), I(0.7 V).

**Formula:**

    L_p = √(D_pτ_p),     I_s ≈ qAn_i²D_p/(L_pN_D)   (p⁺n: hole term only),     I ≈ I_s e^{qV/kT}

**Solution.**

Step 1. Diffusion length: L_p = √(D_pτ_p) = √(10 × 10⁻⁶) = 3.16×10⁻³ cm

Step 2. For a p⁺n diode only the hole term matters:

    I_s ≈ qAn_i²D_p/(L_pN_D) = 1.6×10⁻¹⁹ × 10⁻⁴ × 10²⁰ × 10 / (3.16×10⁻³ × 10¹⁶) = 5.1×10⁻¹⁶ A

Step 3. Forward current, I ≈ I_s e^{qV/kT}:

    I(0.6 V) = 5.1×10⁻¹⁶ × e^{0.6/0.0259} = 5.1×10⁻¹⁶ × 1.15×10¹⁰ = 5.9×10⁻⁶ A

    I(0.7 V) = 5.1×10⁻¹⁶ × e^{0.7/0.0259} = 5.1×10⁻¹⁶ × 5.45×10¹¹ = 2.8×10⁻⁴ A

**Answer:** **I_s = 5.1×10⁻¹⁶ A; I = 5.9 μA at 0.6 V and 280 μA at 0.7 V.** An extra 0.1 V multiplies the current by about 47.

**What this means:** the saturation current is less than a femtoampere, so nothing useful flows until the forward voltage reaches about 0.6 V. Above that the current rises so steeply that a silicon diode conducting anything from microamps to milliamps always shows a forward drop of roughly 0.6–0.7 V.

## Breakdown

At large reverse voltage the current suddenly rises. Two mechanisms:

- **Avalanche breakdown.** Carriers crossing the strong depletion field gain enough energy to knock new electron–hole pairs out of the lattice (impact ionisation, Week 8), which multiply in a chain reaction. Typical of lightly doped junctions; breakdown voltage above about 6 V; rises with temperature.
- **Zener breakdown.** In very heavily doped junctions the depletion region is extremely thin, and electrons **tunnel** straight through from the p-side valence band to the n-side conduction band. Breakdown voltage below about 4 V; falls with temperature. Used in Zener voltage regulators.

Between about 4 V and 6 V both mechanisms act together, and their opposite temperature effects nearly cancel; this is why diodes rated near 5–6 V have the most temperature-stable breakdown voltage.

### Avalanche and Zener breakdown compared

| | Avalanche breakdown | Zener breakdown |
|---|---|---|
| Mechanism | Impact ionisation: accelerated carriers knock out new electron–hole pairs, which multiply in a chain | Quantum-mechanical tunnelling of electrons straight through the thin barrier, from the p-side valence band to the n-side conduction band |
| Doping | Lightly or moderately doped (at least one side) | Very heavily doped on both sides (p⁺n⁺) |
| Depletion width | Wide; carriers need distance to gain energy | Very narrow (of order 10 nm) so tunnelling is possible |
| Breakdown voltage | Above about 6 V (up to thousands of volts) | Below about 4 V |
| Field needed | Of order 3×10⁵ V/cm in Si, reached over a wide region | About 10⁶ V/cm, reached across a very thin region |
| Temperature coefficient of V_BR | Positive: V_BR rises with temperature (more phonon scattering, carriers lose energy) | Negative: V_BR falls with temperature (band gap shrinks, tunnelling easier) |
| Onset | Sharp knee | Softer, more gradual knee |
| Uses | High-voltage rectifiers, avalanche photodiodes, surge-protection diodes | Low-voltage reference and regulator ("Zener") diodes |

## Junction capacitance

The depletion region is a layer of stored charge between two conducting regions, so it behaves as a **capacitor** with plate separation W:

    C_j = ε_sA/W

Where:

- C_j = junction (depletion) capacitance (F)
- ε_s = permittivity of silicon, 1.04×10⁻¹² F/cm
- A = junction area (cm²)
- W = depletion width at the operating voltage (cm)

Since W grows with reverse bias, C_j **falls** as the reverse voltage increases. Diodes used deliberately as voltage-controlled capacitors (in radio tuning) are called **varactors**. Measuring C_j against voltage is also how doping is measured (C-V profiling, Week 12). Under forward bias the stored minority carriers add a larger **diffusion capacitance**.

## Key points of Week 10

- Diffusion across the junction uncovers fixed ions: the depletion region, with a field from n to p.
- Equilibrium: drift balances diffusion, E_F is flat, and the bands bend by qV_bi = kT ln(N_{A}N_D/n_i²).
- N_Ax_p = N_Dx_n: the depletion region lies mostly on the lightly doped side. W = √((2ε_s/q)(V_bi − V)(1/N_A + 1/N_D)).
- Forward bias lowers the barrier and injects minority carriers (law of the junction); reverse bias raises it.
- Shockley equation: I = I_s(e^{qV/kT} − 1), from minority-carrier diffusion in the neutral regions.
- Breakdown by avalanche (lightly doped) or Zener tunnelling (heavily doped); C_j = ε_sA/W.

---

## Examination questions solved (Q47–Q48)

### Q47. Explain the formation of the depletion region and built-in potential in a p-n junction.

**Formation of the depletion region.**

1. When p-type and n-type regions are formed in one crystal, the p side has a high hole concentration (p_p0 ≈ N_A) and the n side a high electron concentration (n_n0 ≈ N_D). The steep concentration gradients cause holes to diffuse from p to n and electrons from n to p.
2. Holes leaving the p side near the junction leave behind **immobile negative acceptor ions**; electrons leaving the n side leave behind **immobile positive donor ions**. Diffusing carriers also recombine with the majority carriers on the other side.
3. A region on both sides of the metallurgical junction is therefore stripped of mobile carriers and contains only fixed ionic charge: **negative on the p side, positive on the n side**. This is the **depletion region** or space-charge region, typically 0.1–10 μm wide.
4. The two charge layers are equal in magnitude, N_A x_p = N_D x_n, so the depletion region extends further into the more lightly doped side.
5. The space charge produces an **electric field** directed from the positive (n) side to the negative (p) side, maximum at the junction: E_max = qN_D x_n/ε_s.
6. This field drives drift currents of holes back to p and electrons back to n, opposing the diffusion. The depletion region grows until **drift exactly balances diffusion** for both carriers and the net current is zero. In equilibrium the Fermi level is constant throughout.

**Built-in potential.** The field corresponds to an electrostatic potential difference across the depletion region, the **built-in potential V_bi**, with the n side positive with respect to the p side. In the band diagram, the bands bend by qV_bi so that the flat Fermi level is near E_v on the p side and near E_c on the n side. It forms a potential barrier that majority carriers must surmount to cross.

Its value follows from the Fermi-level positions: q V_bi = (E_i − E_F)_p + (E_F − E_i)_n = kT ln(N_A/n_i) + kT ln(N_D/n_i), so

    V_bi = (kT/q) ln( N_A N_D / n_i² )

Width of the depletion region:

    W = √( (2ε_s V_bi / q)(N_A + N_D)/(N_A N_D) )

**Example (Si, N_A = 10¹⁷, N_D = 10¹⁶ cm⁻³):** V_bi = 0.0259 ln(10¹³) = **0.775 V**; W = **0.33 μm**, of which 0.30 μm is on the n side; E_max ≈ 4.7×10⁴ V/cm.

The built-in potential cannot drive current in an external circuit, because in equilibrium it is exactly balanced by the contact potentials at the metal–semiconductor contacts. Applied bias changes the barrier to V_bi − V_a, which is the basis of rectification.

### Q48. Derive the ideal Shockley diode equation and explain the effect of forward and reverse bias.

**Assumptions (Shockley):**

1. Abrupt junction; depletion approximation (no carriers in the depletion region, neutral elsewhere).
2. Boltzmann statistics apply (non-degenerate).
3. **Low-level injection**: injected minority densities are much smaller than majority densities.
4. No generation or recombination inside the depletion region, so electron and hole currents are each constant across it.
5. All applied voltage V appears across the depletion region; neutral regions have negligible resistance (zero field).
6. Long neutral regions (longer than the diffusion lengths) terminated by Ohmic contacts.

**Step 1: law of the junction.** In equilibrium n_n0/n_p0 = exp(qV_bi/kT). With bias V the barrier becomes V_bi − V, and (quasi-equilibrium across the depletion region) the minority densities at its edges become:

    p_n(x_n) = p_n0 exp(qV/kT),     n_p(−x_p) = n_p0 exp(qV/kT)

So the excess minority densities at the edges are:

    Δp_n(x_n) = p_n0 [ exp(qV/kT) − 1 ],     Δn_p(−x_p) = n_p0 [ exp(qV/kT) − 1 ]

**Step 2: minority-carrier diffusion in the neutral n region.** With E = 0 and steady state, the continuity equation reduces to

    D_p d²Δp_n/dx² − Δp_n/τ_p = 0

For a long region (Δp → 0 as x → ∞) the solution is

    Δp_n(x) = Δp_n(x_n) exp( −(x − x_n)/L_p ),     L_p = √(D_pτ_p)

**Step 3: hole diffusion current at x = x_n.** With no field, the hole current is pure diffusion:

    J_p(x_n) = −qD_p dΔp_n/dx |_{x_n} = (qD_p/L_p) Δp_n(x_n) = (qD_p p_n0/L_p) [ exp(qV/kT) − 1 ]

**Step 4: electron current at x = −x_p.** Similarly in the p region:

    J_n(−x_p) = (qD_n n_p0/L_n) [ exp(qV/kT) − 1 ]

**Step 5: total current.** With no recombination in the depletion region, J_n is the same at x_n as at −x_p, so the total current (constant everywhere) is the sum of the two minority diffusion currents at the depletion edges:

    J = J_p(x_n) + J_n(−x_p) = [ qD_p p_n0/L_p + qD_n n_p0/L_n ] [ exp(qV/kT) − 1 ]

Using p_n0 = n_i²/N_D and n_p0 = n_i²/N_A:

    J = J_s [ exp(qV/kT) − 1 ],     J_s = q n_i² ( D_p/(L_p N_D) + D_n/(L_n N_A) )

or, for area A, **I = I_s [ exp(qV/kT) − 1 ]** with I_s = AJ_s. This is the ideal Shockley diode equation.

@fig figures/diode-iv.svg | Ideal diode characteristic. Forward current grows by a factor of 10 for every 60 mV at 300 K; reverse current saturates at −I_s.

**Effect of forward bias (V > 0, p side positive):**

- The barrier is lowered to V_bi − V and the depletion region narrows.
- Minority carriers are injected: the edge densities increase by exp(qV/kT).
- For V ≫ kT/q (above about 0.1 V) the −1 is negligible: I ≈ I_s exp(qV/kT). Current increases by a decade every 2.3kT/q ≈ 60 mV.
- Significant current flows only above the "cut-in" voltage (≈ 0.6–0.7 V in Si, ≈ 0.2–0.3 V in Ge), because I_s is so small.

**Effect of reverse bias (V < 0):**

- The barrier rises to V_bi + |V|; the depletion region widens.
- The edge minority densities fall almost to zero (exp(qV/kT) → 0). Carriers are extracted rather than injected.
- For |V| ≫ kT/q: I ≈ −I_s, a small, voltage-independent **reverse saturation current** (Si, about 10⁻¹⁵–10⁻¹² A for small diodes) carried by minority carriers generated within a diffusion length of the junction.
- In real diodes, generation in the depletion region adds a current ∝ W ∝ √|V|, and at large |V| avalanche or Zener breakdown occurs.

**Numerical example.** A Si p⁺n diode with N_D = 10¹⁶ cm⁻³, D_p = 10 cm²/s, τ_p = 1 μs, area 10⁻⁴ cm²: L_p = √(10 × 10⁻⁶) = 3.16×10⁻³ cm; J_s ≈ qn_i²D_p/(L_pN_D) = (1.6×10⁻¹⁹)(10²⁰)(10)/(3.16×10⁻³ × 10¹⁶) = 5.1×10⁻¹² A/cm², so I_s = 5.1×10⁻¹⁶ A. At V = 0.6 V, I = I_s e^{0.6/0.0259} = 5.1×10⁻¹⁶ × 1.15×10¹⁰ ≈ 5.9 μA, and at 0.7 V it is about 280 μA.

**Real diodes** deviate: recombination in the depletion region at low forward bias (I ∝ e^{qV/2kT}), high-level injection at high current, series resistance, and generation current and breakdown in reverse. These are summarised by I = I_s(e^{qV/ηkT} − 1), with ideality factor η between 1 and 2.

---

## Practice questions

These extra questions practise this week's ideas. Work each one on paper before reading the solution; the calculation questions follow the same Question, Given, Find, Solution, Answer layout as the worked examples.

#### Practice 10.1: built-in potential of a germanium junction

**Question.** A germanium junction has N_A = N_D = 1×10¹⁶ cm⁻³. Find V_bi at 300 K (n_i = 2.4×10¹³ cm⁻³) and compare with silicon.

**Given:** N_A = N_D = 10¹⁶ cm⁻³, n_i = 2.4×10¹³ cm⁻³, kT/q = 0.0259 V.

**Find:** V_bi.

**Solution.**

    V_bi = 0.0259 ln(10³²/5.76×10²⁶) = 0.0259 ln(1.74×10⁵) = 0.0259 × 12.06 = 0.31 V

**Answer:** **V_bi = 0.31 V**, against 0.72 V for silicon with the same doping: the smaller gap gives a smaller barrier.

#### Practice 10.2: reverse-biased depletion width and field

**Question.** A silicon p⁺n junction has N_D = 1×10¹⁵ cm⁻³ and V_bi = 0.7 V. Find the depletion width and peak field at a reverse bias of 5 V.

**Given:** N_D = 10¹⁵ cm⁻³, V_bi − V = 0.7 + 5 = 5.7 V, ε_s = 1.04×10⁻¹² F/cm.

**Find:** W and E_max.

**Solution.**

    W = √(2ε_s(V_bi − V)/qN_D) = √(2 × 1.04×10⁻¹² × 5.7 / (1.6×10⁻¹⁹ × 10¹⁵)) = 2.72×10⁻⁴ cm
    E_max = 2(V_bi − V)/W = 2 × 5.7/2.72×10⁻⁴ = 4.2×10⁴ V/cm

**Answer:** **W = 2.7 μm, E_max = 4.2×10⁴ V/cm.**

**What this means:** light doping and reverse bias together make the depletion region several micrometres wide, which is why lightly doped junctions can withstand large reverse voltages before the field reaches the avalanche level.

#### Practice 10.3: junction capacitance

**Question.** Find the junction capacitance of the diode in Practice 10.2 if its area is 1×10⁻³ cm².

**Given:** W = 2.72×10⁻⁴ cm, A = 10⁻³ cm², ε_s = 1.04×10⁻¹² F/cm.

**Find:** C_j.

**Solution.**

    C_j = ε_sA/W = 1.04×10⁻¹² × 10⁻³ / 2.72×10⁻⁴ = 3.8×10⁻¹² F

**Answer:** **C_j = 3.8 pF.**

**What this means:** increasing the reverse bias widens W and lowers C_j further; this voltage-controlled capacitance is what a varactor diode uses to tune a radio circuit.

#### Practice 10.4: saturation current with both sides

**Question.** A silicon diode has N_A = 1×10¹⁷ cm⁻³, N_D = 1×10¹⁶ cm⁻³, D_n = 20 cm²/s, L_n = 20 μm, D_p = 10 cm²/s, L_p = 10 μm. Find J_s and the fraction carried by holes.

**Given:** the values above, n_i = 10¹⁰ cm⁻³.

**Find:** J_s and the hole fraction.

**Solution.**

    D_p/(L_pN_D) = 10/(10⁻³ × 10¹⁶) = 1.0×10⁻¹²
    D_n/(L_nN_A) = 20/(2×10⁻³ × 10¹⁷) = 1.0×10⁻¹³
    J_s = qn_i²(1.0×10⁻¹² + 1.0×10⁻¹³) = 1.6×10⁻¹⁹ × 10²⁰ × 1.1×10⁻¹² = 1.76×10⁻¹¹ A/cm²
    hole fraction = 1.0/1.1 = 91 %

**Answer:** **J_s = 1.8×10⁻¹¹ A/cm², 91 % carried by holes injected into the lightly doped n side.**

#### Practice 10.5: temperature and the saturation current

**Question.** By roughly what factor does I_s of a silicon diode increase when the temperature rises from 300 K to 310 K? (Take I_s ∝ n_i² and ignore other temperature effects.)

**Given:** n_i ∝ T^{3/2}e^{−E_g/2kT}, E_g = 1.12 eV.

**Find:** I_s(310)/I_s(300).

**Solution.**

    n_i(310)/n_i(300) = (310/300)^{3/2} × exp[6499 × (1/300 − 1/310)] = 1.050 × e^{0.699} = 2.11
    I_s ratio = 2.11² = 4.5

**Answer:** **about 4.5 times for a 10 K rise**: reverse leakage is very temperature-sensitive.

#### Practice 10.6: forward voltage per decade

**Question.** How much must the forward voltage of an ideal diode increase to multiply the current by 10 at 300 K? If I = 1 mA at 0.60 V, what is I at 0.66 V?

**Given:** I ∝ e^{qV/kT}, kT/q = 0.0259 V.

**Find:** ΔV per decade; I at 0.66 V.

**Solution.**

    ΔV = (kT/q) ln 10 = 0.0259 × 2.303 = 59.6 mV
    I(0.66) = 1 mA × e^{0.06/0.0259} = 1 × 10.1 = 10.1 mA

**Answer:** **about 60 mV per decade; I ≈ 10 mA at 0.66 V.**

#### Practice 10.7: avalanche or Zener?

**Question.** A diode breaks down at 3.3 V and its breakdown voltage falls as it warms up. Another breaks down at 50 V and its breakdown voltage rises with temperature. Identify the mechanism in each and explain the temperature behaviour.

**Answer.** The **3.3 V diode is Zener breakdown**: it is heavily doped, its depletion region is very thin, and electrons tunnel across the gap. Heating shrinks the band gap, making tunnelling easier, so V_BR falls. The **50 V diode is avalanche breakdown**: carriers gain energy across a wide depletion region and impact-ionise. Heating increases lattice vibration, so carriers lose more energy to phonons between collisions and need a larger field to ionise, so V_BR rises.

---

## Objectives check

Use this table to confirm you have met this week's objectives. Cover the Answer column and answer each check question from memory. If you cannot, go back to the section in the last column before moving on.

| # | Objective | Check yourself | Answer | Where it is taught |
|---|---|---|---|---|
| 1 | Explain the formation of the depletion region in a p-n junction. | Why is the depletion region empty of mobile carriers? | Carriers diffused across and recombined, leaving only fixed donor and acceptor ions. | Forming the junction |
| 2 | Derive and calculate the built-in potential. | Find V_bi for N_A = N_D = 10¹⁶ cm⁻³ in Si. | 0.0259 ln(10¹²) = 0.716 V. | The built-in potential; Example 10.1 |
| 3 | Calculate the depletion width and electric-field profile. | If N_A = 100 N_D, where does most of the depletion region lie? | On the n side (x_n = 100 x_p). | Depletion approximation; Example 10.2 |
| 4 | Explain the junction under forward and reverse bias and the law of the junction. | By what factor does forward bias of 0.12 V multiply the injected minority carriers? | e^{0.12/0.0259} ≈ 100. | The junction under bias; Forward and reverse bias compared |
| 5 | Derive and use the Shockley diode equation. | Write the ideal diode equation and its saturation current density. | I = I_s(e^{qV/kT} − 1); J_s = qn_i²(D_p/L_pN_D + D_n/L_nN_A). | Shockley equation; Example 10.3; Q48 |
| 6 | Explain breakdown and junction capacitance. | Which breakdown mechanism occurs in very heavily doped junctions, and how does its V_BR change with temperature? | Zener (tunnelling) breakdown; V_BR falls as temperature rises. | Breakdown; Avalanche and Zener breakdown compared; junction capacitance |
