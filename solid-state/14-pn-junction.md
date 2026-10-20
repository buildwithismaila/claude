# Module 14 — The p-n Junction and the Shockley Diode

Examined in Q47–Q48. Everything so far (doping, Fermi level, drift, diffusion, recombination) meets in the p-n junction, the building block of diodes, transistors, solar cells and LEDs.

## 14.1 Forming the junction

Join p-type (acceptors N_A) and n-type (donors N_D) silicon in one crystal. Initially there is a huge concentration difference across the interface:

1. **Holes diffuse** from p to n, and **electrons diffuse** from n to p.
2. Each hole that leaves the p side uncovers a fixed negative acceptor ion N_A⁻; each electron that leaves the n side uncovers a fixed positive donor ion N_D⁺. Carriers crossing also recombine with the majority carriers on the far side.
3. A layer of **uncompensated fixed charge** builds up: negative on the p side, positive on the n side. This is the **depletion region** (space-charge region), almost empty of mobile carriers.
4. This charge creates an electric field pointing from n to p, which **drives drift currents** opposite to the diffusion currents.
5. Equilibrium is reached when drift exactly cancels diffusion for each carrier type; the Fermi level is then constant across the whole structure.

@fig figures/pn-junction.svg | The abrupt p-n junction in equilibrium: space charge, electric field, and the band diagram with a flat Fermi level and bands bent by qV_bi.

## 14.2 Built-in potential

The bands bend by qV_bi so that E_F lines up. On the p side E_i − E_F = kT ln(N_A/n_i); on the n side E_F − E_i = kT ln(N_D/n_i). Adding:

    V_bi = (kT/q) ln( N_A N_D / n_i² )

Equivalently, it follows from setting J_n = 0 (Einstein relation) and integrating: n_n0/n_p0 = exp(qV_bi/kT).

The built-in potential cannot be measured with a voltmeter: contact potentials at the metal leads cancel it exactly.

## 14.3 Depletion approximation

Assume the depletion region (−x_p to x_n) is completely free of carriers, with abrupt edges, and the regions outside are neutral. Poisson's equation:

    d²V/dx² = −ρ/ε_s,     ρ = −qN_A (−x_p < x < 0),   ρ = +qN_D (0 < x < x_n)

Results:

    Charge balance:  N_A x_p = N_D x_n
    Peak field (at x = 0):  E_max = qN_D x_n/ε_s = qN_A x_p/ε_s
    Total width:  W = x_n + x_p = √( (2ε_s/q)(V_bi − V_a)(1/N_A + 1/N_D) )
    x_n = W N_A/(N_A + N_D),   x_p = W N_D/(N_A + N_D)
    V_bi − V_a = ½ E_max W

V_a is the applied voltage (positive for forward bias). The depletion region extends mostly into the **more lightly doped** side. For a one-sided p⁺n junction, W ≈ √(2ε_s(V_bi − V_a)/qN_D).

**Worked example.** Si, N_A = 10¹⁷ cm⁻³, N_D = 10¹⁶ cm⁻³, n_i = 10¹⁰ cm⁻³, 300 K, ε_s = 11.7 × 8.854×10⁻¹⁴ = 1.036×10⁻¹² F/cm.

    V_bi = 0.0259 ln(10³³/10²⁰) = 0.0259 × 29.93 = 0.775 V

    W = √( 2(1.036×10⁻¹²)(0.775)(10⁻¹⁷ + 10⁻¹⁶) / 1.602×10⁻¹⁹ )
      = √(1.10×10⁻⁹) = 3.32×10⁻⁵ cm = 0.332 μm

    x_n = 0.332 × (10/11) = 0.302 μm,   x_p = 0.030 μm

    E_max = qN_D x_n/ε_s = (1.602×10⁻¹⁹)(10¹⁶)(3.02×10⁻⁵)/(1.036×10⁻¹²) = 4.7×10⁴ V/cm

## 14.4 Junction under bias

**Forward bias** (p positive, V_a > 0): the barrier falls to V_bi − V_a and the depletion region narrows. Diffusion now exceeds drift; majority carriers are **injected** across as minority carriers into the opposite sides, where they diffuse and recombine. Current rises exponentially.

**Reverse bias** (V_a < 0): the barrier rises to V_bi + |V_a| and W widens. Diffusion is suppressed. Only the small drift of minority carriers that wander to the depletion edge flows: the **reverse saturation current**, nearly independent of voltage, until breakdown.

**Law of the junction.** At the edges of the depletion region:

    p_n(x_n) = p_n0 exp(qV_a/kT),      n_p(−x_p) = n_p0 exp(qV_a/kT)

The minority-carrier density at each edge is raised (forward) or lowered (reverse) by the Boltzmann factor.

## 14.5 Breakdown

At large reverse bias the current rises sharply:

- **Avalanche breakdown:** carriers accelerated by the depletion field impact-ionise and multiply. Dominates in lightly doped junctions, V_BR > about 6 V, positive temperature coefficient.
- **Zener breakdown:** in heavily doped junctions (very thin W), electrons tunnel directly from the p-side valence band into the n-side conduction band. V_BR < about 4 V, negative temperature coefficient.

## 14.6 Junction capacitance

The depletion layer stores charge that changes with voltage, so it acts as a capacitor:

    C_j = ε_s A / W = A √( qε_s N_A N_D / (2(N_A + N_D)(V_bi − V_a)) )

Under forward bias the stored minority charge adds a **diffusion capacitance** C_d = (q/kT) I τ, which dominates at forward bias. Reverse-biased junctions are used as voltage-controlled capacitors (varactors). C–V measurement is in Module 16.

---

## Exam questions solved

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
