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

#### Example 10.1: built-in potential

**Question.** A silicon p-n junction has N_A = 1×10¹⁷ cm⁻³ on the p side and N_D = 1×10¹⁶ cm⁻³ on the n side. Calculate the built-in potential at 300 K.

**Given:** N_A = 1×10¹⁷ cm⁻³, N_D = 1×10¹⁶ cm⁻³, n_i = 1×10¹⁰ cm⁻³, kT/q = 0.0259 V.

**Find:** V_bi.

**Solution.**

    V_bi = (kT/q) ln(N_{A}N_D/n_i²) = 0.0259 × ln(10¹⁷ × 10¹⁶ / 10²⁰)

         = 0.0259 × ln(10¹³) = 0.0259 × 29.93 = 0.775 V

**Answer:** **V_bi = 0.775 V.**

You **cannot** measure V_bi with a voltmeter across a diode: where the wires meet the semiconductor, contact potentials appear that exactly cancel it. It is an internal barrier, not a battery.

## Depletion width and field: the depletion approximation

To calculate the width of the depletion region we make the **depletion approximation**: inside the region (from −x_p on the p side to x_n on the n side) there are no mobile carriers at all, only the fixed ions; outside it the material is neutral. Then Poisson's equation (the link between charge and field) gives:

**Charge balance.** The total negative charge equals the total positive charge:

    N_A x_p = N_D x_n

So the depletion region extends **further into the more lightly doped side**. If N_A = 10 × N_D, then x_n = 10 × x_p.

**Width.**

    W = x_n + x_p = √( (2ε_s/q)(V_bi − V_a)(1/N_A + 1/N_D) )

with x_n = W N_A/(N_A + N_D) and x_p = W N_D/(N_A + N_D). Here ε_s is the permittivity of silicon (11.7 × 8.854×10⁻¹⁴ = 1.04×10⁻¹² F/cm) and V_a the applied voltage (positive for forward bias).

**Peak field** (at the junction):

    E_max = qN_D x_n/ε_s = qN_A x_p/ε_s,   and   V_bi − V_a = ½ E_max W

For a **one-sided p⁺n junction** (N_A ≫ N_D), almost all of W is on the n side: W ≈ √(2ε_s(V_bi − V_a)/qN_D).

#### Example 10.2: depletion width and peak field

**Question.** For the junction of Example 10.1 at zero bias, calculate the total depletion width, how much of it lies on each side, and the peak electric field.

**Given:** V_bi = 0.775 V, N_A = 10¹⁷ cm⁻³, N_D = 10¹⁶ cm⁻³, ε_s = 1.04×10⁻¹² F/cm, q = 1.6×10⁻¹⁹ C, V_a = 0.

**Find:** W, x_n, x_p and E_max.

**Solution.**

Step 1. Total width:

    W = √( (2ε_s/q) V_bi (1/N_A + 1/N_D) )

      = √( 2 × 1.04×10⁻¹² × 0.775 × (10⁻¹⁷ + 10⁻¹⁶) / 1.6×10⁻¹⁹ ) = √(1.10×10⁻⁹) = 3.32×10⁻⁵ cm

Step 2. Split, using x_n = W N_A/(N_A + N_D):

    x_n = 0.332 × 10/11 = 0.30 μm,   x_p = 0.332 − 0.30 = 0.03 μm

Step 3. Peak field at the junction:

    E_max = qN_Dx_n/ε_s = 1.6×10⁻¹⁹ × 10¹⁶ × 3.0×10⁻⁵ / 1.04×10⁻¹² = 4.7×10⁴ V/cm

**Answer:** **W = 0.33 μm (0.30 μm on the n side, 0.03 μm on the p side), E_max = 4.7×10⁴ V/cm.** The region is narrow but the field in it is large.

## The junction under bias

**Forward bias** (p side made positive, V_a > 0). The applied voltage opposes the built-in voltage, so the barrier **falls** to V_bi − V_a and the depletion region **narrows**. Diffusion now wins over drift. Holes pour from p into n, and electrons from n into p. On arrival they are minority carriers: they are **injected**. They diffuse away from the junction and recombine (Week 9). The current rises steeply (exponentially) with voltage.

**Reverse bias** (p side negative, V_a < 0). The applied voltage adds to the built-in voltage. The barrier **rises** to V_bi + |V_a| and the depletion region **widens**. Diffusion is shut off. The only current left is the tiny drift of the few minority carriers that happen to wander to the edge of the depletion region and get swept across. This is the **reverse saturation current**, almost independent of voltage, until breakdown.

**The law of the junction.** The barrier controls how many carriers can be injected. At the edges of the depletion region, the minority-carrier concentrations become:

    p_n(x_n) = p_n0 e^{qV_a/kT},     n_p(−x_p) = n_p0 e^{qV_a/kT}

p_n0 = n_i²/N_D and n_p0 = n_i²/N_A are the equilibrium minority concentrations. Forward bias multiplies them by e^{qV_a/kT}; reverse bias makes them almost zero. Every 60 mV of forward bias multiplies the injected minority carriers by 10.

## The ideal diode (Shockley) equation, in words

The full derivation is worked in exam question Q48 below. The idea in four steps:

1. **Injection.** The law of the junction gives the excess minority carriers at each edge of the depletion region: Δp = p_n0(e^{qV/kT} − 1) on the n side.
2. **Diffusion and recombination.** In each neutral region the excess decays exponentially over a diffusion length (Week 9): Δp(x) = Δp(x_n)e^{−(x − x_n)/L_p}.
3. **Current at the edge.** The diffusion current at the edge is qD_p × slope = (qD_p/L_p)Δp(x_n). Same for electrons on the p side.
4. **Add them.** The total current is the sum of the hole and electron diffusion currents:

    I = I_s ( e^{qV/kT} − 1 ),     I_s = qA n_i² ( D_p/(L_pN_D) + D_n/(L_nN_A) )

@fig figures/diode-iv.svg | The ideal diode characteristic. Forward current grows ten times for every 60 mV at 300 K; reverse current is a tiny −I_s.

**What the equation says:**

- **Forward** (V > about 0.1 V): the −1 is negligible and I ≈ I_s e^{qV/kT}. Because I_s is tiny (10⁻¹⁵–10⁻¹² A for small Si diodes), a noticeable current needs about 0.6–0.7 V in Si (0.2–0.3 V in Ge).
- **Reverse** (V negative, more than a few kT/q): e^{qV/kT} → 0 and I ≈ −I_s, tiny and constant.
- I_s ∝ n_i², so it rises steeply with temperature and is much larger in small-gap materials (Ge diodes leak far more than Si).

#### Example 10.3: saturation current and forward current of a diode

**Question.** A silicon p⁺n diode has N_D = 1×10¹⁶ cm⁻³ on the n side, hole diffusion coefficient D_p = 10 cm²/s, hole lifetime τ_p = 1 μs and area 10⁻⁴ cm². Calculate the saturation current, and the forward current at 0.6 V and at 0.7 V (300 K).

**Given:** N_D = 10¹⁶ cm⁻³, D_p = 10 cm²/s, τ_p = 10⁻⁶ s, A = 10⁻⁴ cm², n_i = 10¹⁰ cm⁻³, kT/q = 0.0259 V.

**Find:** I_s, I(0.6 V), I(0.7 V).

**Solution.**

Step 1. Diffusion length: L_p = √(D_pτ_p) = √(10 × 10⁻⁶) = 3.16×10⁻³ cm

Step 2. For a p⁺n diode only the hole term matters:

    I_s ≈ qAn_i²D_p/(L_pN_D) = 1.6×10⁻¹⁹ × 10⁻⁴ × 10²⁰ × 10 / (3.16×10⁻³ × 10¹⁶) = 5.1×10⁻¹⁶ A

Step 3. Forward current, I ≈ I_s e^{qV/kT}:

    I(0.6 V) = 5.1×10⁻¹⁶ × e^{0.6/0.0259} = 5.1×10⁻¹⁶ × 1.15×10¹⁰ = 5.9×10⁻⁶ A

    I(0.7 V) = 5.1×10⁻¹⁶ × e^{0.7/0.0259} = 5.1×10⁻¹⁶ × 5.45×10¹¹ = 2.8×10⁻⁴ A

**Answer:** **I_s = 5.1×10⁻¹⁶ A; I = 5.9 μA at 0.6 V and 280 μA at 0.7 V.** An extra 0.1 V multiplies the current by about 47.

## Breakdown

At large reverse voltage the current suddenly rises. Two mechanisms:

- **Avalanche breakdown.** Carriers crossing the strong depletion field gain enough energy to knock new electron–hole pairs out of the lattice (impact ionisation, Week 8), which multiply in a chain reaction. Typical of lightly doped junctions; breakdown voltage above about 6 V; rises with temperature.
- **Zener breakdown.** In very heavily doped junctions the depletion region is extremely thin, and electrons **tunnel** straight through from the p-side valence band to the n-side conduction band. Breakdown voltage below about 4 V; falls with temperature. Used in Zener voltage regulators.

## Junction capacitance

The depletion region is a layer of stored charge between two conducting regions, so it behaves as a **capacitor** with plate separation W:

    C_j = ε_sA/W

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

**Numerical example.** A Si p⁺n diode with N_D = 10¹⁶ cm⁻³, D_p = 10 cm²/s, τ_p = 1 μs, area 10⁻⁴ cm²: L_p = √(10 × 10⁻⁶) = 3.16×10⁻³ cm; J_s ≈ qn_i²D_p/(L_pN_D) = (1.602×10⁻¹⁹)(10²⁰)(10)/(3.16×10⁻³ × 10¹⁶) = 5.1×10⁻¹² A/cm², so I_s = 5.1×10⁻¹⁶ A. At V = 0.6 V, I = I_s e^{0.6/0.0259} = 5.1×10⁻¹⁶ × 1.15×10¹⁰ ≈ 5.9 μA, and at 0.7 V it is about 280 μA.

**Real diodes** deviate: recombination in the depletion region at low forward bias (I ∝ e^{qV/2kT}), high-level injection at high current, series resistance, and generation current and breakdown in reverse. These are summarised by I = I_s(e^{qV/ηkT} − 1), with ideality factor η between 1 and 2.

---

## Objectives check

Use this table to confirm you have met this week's objectives. Cover the Answer column and answer each check question from memory. If you cannot, go back to the section in the last column before moving on.

| # | Objective | Check yourself | Answer | Where it is taught |
|---|---|---|---|---|
| 1 | Explain the formation of the depletion region in a p-n junction. | Why is the depletion region empty of mobile carriers? | Carriers diffused across and recombined, leaving only fixed donor and acceptor ions. | Forming the junction |
| 2 | Derive and calculate the built-in potential. | Find V_bi for N_A = N_D = 10¹⁶ cm⁻³ in Si. | 0.0259 ln(10¹²) = 0.716 V. | The built-in potential; Example 10.1 |
| 3 | Calculate the depletion width and electric-field profile. | If N_A = 100 N_D, where does most of the depletion region lie? | On the n side (x_n = 100 x_p). | Depletion approximation; Example 10.2 |
| 4 | Explain the junction under forward and reverse bias and the law of the junction. | By what factor does forward bias of 0.12 V multiply the injected minority carriers? | e^{0.12/0.0259} ≈ 100. | The junction under bias |
| 5 | Derive and use the Shockley diode equation. | Write the ideal diode equation and its saturation current density. | I = I_s(e^{qV/kT} − 1); J_s = qn_i²(D_p/L_pN_D + D_n/L_nN_A). | Shockley equation; Example 10.3; Q48 |
| 6 | Explain breakdown and junction capacitance. | Which breakdown mechanism occurs in very heavily doped junctions? | Zener (tunnelling) breakdown. | Breakdown; junction capacitance |
