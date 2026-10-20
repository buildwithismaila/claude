# Module 09 — Carrier Statistics and the Fermi Level

Lecture note §6, extended for Q27–Q34. To find how many electrons and holes there are, multiply **how many states exist** at each energy (density of states) by **the probability each is occupied** (Fermi–Dirac function), and integrate over the band.

    n = ∫ g_c(E) f(E) dE      (over the conduction band)
    p = ∫ g_v(E) [1 − f(E)] dE   (over the valence band)

## 9.1 Density of states

The **density of states** g(E) is the number of allowed electron states per unit energy per unit volume (cm⁻³eV⁻¹). For parabolic bands with effective masses m_n∗ and m_p∗:

    g_c(E) = (4π (2m_n∗)^{3/2} / h³) √(E − E_c)     for E ≥ E_c
    g_v(E) = (4π (2m_p∗)^{3/2} / h³) √(E_v − E)     for E ≤ E_v

It is zero inside the gap and grows as the square root of the energy measured into each band.

**Origin (sketch).** In a cube of side L, the allowed wave vectors form a grid with one point per (2π/L)³ of k-space. Counting points in a spherical shell of radius k, including two spin states, and using E − E_c = ħ²k²/2m_n∗, gives the √(E − E_c) form.

## 9.2 The Fermi–Dirac distribution

Electrons obey the Pauli principle, so the probability that a state at energy E is occupied in thermal equilibrium is:

    f(E) = 1 / ( 1 + exp((E − E_F)/kT) )

- **E_F, the Fermi level**: the energy at which the occupation probability is exactly ½.
- The probability that a state is **empty** (holds a hole) is 1 − f(E).
- k = 8.617×10⁻⁵ eV/K; kT = 0.0259 eV at 300 K.

**At T = 0 K**, f(E) is a **step**: f = 1 for E < E_F, f = 0 for E > E_F. All states below E_F are filled, all above are empty.

**At T > 0**, the step is rounded over a width of a few kT around E_F. Some electrons just below E_F move to states just above it. f(E_F) = ½ at every temperature.

**Boltzmann approximation.** When E − E_F > 3kT, exp(...) ≫ 1 and

    f(E) ≈ exp( −(E − E_F)/kT )

The error is under 5 % (at E − E_F = 3kT, f = 1/(1 + e³) = 0.0474 versus e⁻³ = 0.0498). Semiconductors in which E_F stays more than 3kT from both band edges are called **non-degenerate**, and this approximation makes the integrals easy.

@fig figures/fermi.svg | The Fermi–Dirac function at 0 K (a step) and at higher temperatures (smeared over a few kT). It always passes through ½ at E_F.

## 9.3 Equilibrium carrier concentrations

Using the Boltzmann approximation and integrating:

    n₀ = N_c exp( −(E_c − E_F)/kT )
    p₀ = N_v exp( −(E_F − E_v)/kT )

with the **effective densities of states**

    N_c = 2 (2π m_n∗ kT / h²)^{3/2},     N_v = 2 (2π m_p∗ kT / h²)^{3/2}

At 300 K: Si N_c = 2.8×10¹⁹, N_v = 1.04×10¹⁹ cm⁻³; GaAs N_c = 4.7×10¹⁷, N_v = 7.0×10¹⁸ cm⁻³. Both scale as T^{3/2}.

N_c is the number of states you would need at the single energy E_c to hold the same number of electrons as the whole band.

## 9.4 Intrinsic semiconductor

In a pure crystal every electron in the conduction band left a hole in the valence band, so n₀ = p₀ = n_i. The Fermi level in this case is the **intrinsic level E_i**, very close to mid-gap.

    n_i = √(N_c N_v) exp( −E_g / 2kT )

    E_i = (E_c + E_v)/2 + (3/4)kT ln( m_p∗ / m_n∗ )

For Si the shift of E_i from mid-gap is only about −0.01 eV.

Values of n_i at 300 K: Si ≈ 1×10¹⁰ cm⁻³ (the accurate modern value is 9.65×10⁹; older texts use 1.5×10¹⁰), Ge 2.4×10¹³, GaAs 2.1×10⁶ cm⁻³.

n_i rises very steeply with temperature, mainly through exp(−E_g/2kT). For Si it roughly doubles every 8 °C near room temperature.

## 9.5 The mass-action law

Multiply n₀ and p₀:

    n₀ p₀ = N_c N_v exp( −E_g/kT ) = n_i²

This holds in thermal equilibrium for **any** non-degenerate semiconductor, doped or not. Adding donors raises n and lowers p in proportion.

Equivalent forms using E_i:

    n₀ = n_i exp( (E_F − E_i)/kT ),     p₀ = n_i exp( (E_i − E_F)/kT )

## 9.6 Extrinsic semiconductor

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

## 9.7 Position of the Fermi level

    n-type:  E_c − E_F = kT ln(N_c / N_D),    E_F − E_i = kT ln(N_D / n_i)
    p-type:  E_F − E_v = kT ln(N_v / N_A),    E_i − E_F = kT ln(N_A / n_i)

@fig figures/fermi-level.svg | The Fermi level moves towards the conduction band with donor doping and towards the valence band with acceptor doping. Each factor of 10 in doping shifts it by kT ln10 = 60 mV at 300 K.

- The heavier the doping, the closer E_F gets to the band edge. When it comes within about 3kT of the edge (above about 10¹⁸–10¹⁹ cm⁻³ in Si) the semiconductor is **degenerate** and behaves almost like a metal.
- As temperature rises, n_i grows and E_F moves back towards E_i.
- **In equilibrium E_F is constant throughout any system**, including across junctions. This single fact sets up the built-in voltage of a p-n junction (Module 14).

---

## Exam questions solved

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

### Q30. Explain the Fermi-Dirac distribution function and its significance in semiconductor physics.

**The function.** Electrons are indistinguishable particles of half-integer spin that obey the Pauli exclusion principle (fermions). In thermal equilibrium at temperature T, the probability that an available state of energy E is occupied by an electron is given by Fermi–Dirac statistics:

    f(E) = 1 / ( 1 + exp((E − E_F)/kT) )

where E_F is the Fermi level and k is Boltzmann's constant.

**Properties:**

- 0 ≤ f(E) ≤ 1 (at most one electron per state).
- f(E_F) = ½ at any temperature: E_F is the energy with a 50 % chance of occupation.
- f is symmetric about E_F: the probability that a state ΔE above E_F is occupied equals the probability that a state ΔE below E_F is empty, so 1 − f(E_F + ΔE) = f(E_F − ΔE).
- The transition from 1 to 0 happens over a few kT (about 0.1 eV at 300 K).
- For E − E_F > 3kT it reduces to the Boltzmann factor exp(−(E − E_F)/kT).

**Significance:**

1. **Gives the carrier concentrations.** n = ∫g_c f dE and p = ∫g_v(1 − f)dE. Without f(E) we could not calculate n, p or n_i.
2. **Defines the Fermi level**, the single most useful quantity in device physics. Its position relative to E_c and E_v tells immediately whether the material is n-type, p-type or intrinsic and how heavily doped.
3. **Constant Fermi level in equilibrium.** E_F is flat across any system in equilibrium; this determines band bending and built-in potential in p-n junctions, Schottky contacts and MOS structures.
4. **Explains temperature dependence** of carrier concentration, intrinsic behaviour, freeze-out and degeneracy.
5. **Out of equilibrium**, the concept is extended to quasi-Fermi levels E_Fn and E_Fp, which are used to describe biased devices.

### Q31. Write the Fermi-Dirac distribution equation and explain what happens to the distribution at absolute zero.

    f(E) = 1 / ( 1 + e^{(E − E_F)/kT} )

**At T = 0 K**, kT → 0, so the exponent (E − E_F)/kT → ±∞:

- For **E < E_F**: (E − E_F)/kT → −∞, e^{−∞} = 0, so **f(E) = 1/(1 + 0) = 1**. Every state below E_F is certainly filled.
- For **E > E_F**: (E − E_F)/kT → +∞, e^{+∞} → ∞, so **f(E) = 0**. Every state above E_F is certainly empty.

The distribution becomes a **sharp rectangular step** at E = E_F. The Fermi level is then the boundary between completely filled and completely empty states: the highest occupied energy at 0 K.

For a semiconductor this means the valence band is completely full and the conduction band completely empty at 0 K. There are no free carriers, and **a pure semiconductor is a perfect insulator at absolute zero**.

**As T increases**, the step softens over a range of about ±3kT: some states just below E_F become empty and some just above become filled. This tail reaching into the conduction band is what produces free electrons at room temperature. At E = E_F, f = ½ always. (See the figure in §9.2.)

| E − E_F | f at 0 K | f at 300 K (kT = 0.0259 eV) |
|---|---|---|
| −0.1 eV | 1 | 0.979 |
| 0 | ½ (undefined step) | 0.500 |
| +0.1 eV | 0 | 0.021 |
| +0.3 eV | 0 | 9.3×10⁻⁶ |

### Q32. Define the density of states in a semiconductor and explain its importance in determining carrier concentration.

**Definition.** The density of states g(E) is the number of allowed electron energy states (including both spins) per unit energy interval per unit volume of the crystal, at energy E. Unit: cm⁻³eV⁻¹ (or m⁻³J⁻¹).

For the conduction and valence bands (parabolic band approximation):

    g_c(E) = (4π (2m_n∗)^{3/2} / h³) √(E − E_c),    E ≥ E_c
    g_v(E) = (4π (2m_p∗)^{3/2} / h³) √(E_v − E),    E ≤ E_v
    g(E) = 0  inside the gap

**Physical origin.** In a crystal of volume V, the allowed wave vectors k are quantised, each occupying (2π)³/V of k-space. The number of states with energy up to E is the volume of the sphere of radius k divided by that, times 2 for spin. Differentiating with respect to E, using E − E_c = ħ²k²/2m∗, gives the square-root law. The effective mass enters because it describes the band's curvature: heavier mass means more states per unit energy.

**Importance in determining carrier concentration:**

1. The carrier concentration is the product of **available states** and **probability of occupation**: n = ∫g_c(E)f(E)dE, p = ∫g_v(E)[1 − f(E)]dE. The Fermi function alone says nothing about how many electrons there are; g(E) supplies the number of places they can go.
2. It produces the **effective densities of states** N_c and N_v, which appear in every carrier-concentration formula (n = N_c e^{−(E_c−E_F)/kT}).
3. Because g(E) is zero in the gap, no carriers exist there even though f(E) is non-zero, which explains why the gap is "forbidden".
4. It explains differences between materials. GaAs has a small m_n∗ (0.067m₀), so its N_c (4.7×10¹⁷ cm⁻³) is 60 times smaller than Si's; for the same doping its Fermi level sits much closer to E_c and it becomes degenerate at lower doping.
5. It sets the T^{3/2} factor in N_c, N_v and n_i, and determines where the Fermi level lies relative to mid-gap (E_i shifts by (3/4)kT ln(m_p∗/m_n∗)).
6. It also governs optical absorption and the density of electrons available for tunnelling and contact behaviour.

### Q33. Explain how the Fermi energy level changes with doping in n-type and p-type semiconductors.

In an intrinsic semiconductor E_F = E_i, near mid-gap. Doping shifts it so that the carrier concentrations satisfy n = n_i e^{(E_F − E_i)/kT} and p = n_i e^{(E_i − E_F)/kT}.

**n-type (donor doping N_D).** n ≈ N_D > n_i, so E_F moves **up, towards E_c**:

    E_F − E_i = kT ln(N_D/n_i),     E_c − E_F = kT ln(N_c/N_D)

**p-type (acceptor doping N_A).** p ≈ N_A > n_i, so E_F moves **down, towards E_v**:

    E_i − E_F = kT ln(N_A/n_i),     E_F − E_v = kT ln(N_v/N_A)

**Behaviour:**

1. The shift is **logarithmic**: each tenfold increase in doping moves E_F by kT ln10 ≈ 0.06 eV at 300 K.
2. **Heavier doping → closer to the band edge.** At very high doping (≈ N_c or N_v) E_F reaches or enters the band and the semiconductor becomes **degenerate** (n⁺, p⁺).
3. **Compensation** (both N_D and N_A) shifts E_F according to the net doping N_D − N_A.
4. **Temperature:** as T rises, n_i increases and E_F moves back toward E_i; at high enough T every semiconductor becomes intrinsic. At very low T (freeze-out) E_F rises above E_D in n-type material.
5. In equilibrium the Fermi level must be the same everywhere; when n and p regions meet, bands bend to keep E_F flat.

**Example (Si, 300 K, n_i = 10¹⁰ cm⁻³):**

| Doping | E_F position |
|---|---|
| Intrinsic | E_F = E_i |
| N_D = 10¹⁵ cm⁻³ | E_F − E_i = 0.0259 ln(10⁵) = 0.298 eV |
| N_D = 10¹⁷ cm⁻³ | E_F − E_i = 0.0259 ln(10⁷) = 0.417 eV |
| N_A = 10¹⁶ cm⁻³ | E_i − E_F = 0.0259 ln(10⁶) = 0.358 eV |

(See the figure in §9.7.)

### Q34. An n-type semiconductor has a donor concentration of 5 × 10¹⁶ cm⁻³. Assuming complete ionization, determine the approximate majority-carrier concentration.

With complete ionisation and N_D ≫ n_i (5×10¹⁶ ≫ 10¹⁰), every donor contributes one electron:

    n₀ ≈ N_D = 5 × 10¹⁶ cm⁻³

**Majority-carrier (electron) concentration ≈ 5×10¹⁶ cm⁻³.**

Additional results (assuming silicon at 300 K, n_i = 1×10¹⁰ cm⁻³):

    Minority holes:  p₀ = n_i²/n₀ = (10¹⁰)² / (5×10¹⁶) = 2×10³ cm⁻³

    Fermi level:  E_F − E_i = kT ln(n₀/n_i) = 0.0259 × ln(5×10⁶) = 0.0259 × 15.42 = 0.40 eV above E_i

    Conductivity:  σ ≈ q n₀ μ_n = 1.602×10⁻¹⁹ × 5×10¹⁶ × 1350 ≈ 10.8 S/cm  (ρ ≈ 0.093 Ω·cm)

The thermal contribution n_i is negligible, which is why the majority-carrier density is simply the donor density. (Mobility falls at this doping to about 1000 cm²/V·s, so the real σ is nearer 8 S/cm.)
