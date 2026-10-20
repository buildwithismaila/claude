# Week 5 — Carrier Statistics
<!-- group: Module 2 · Energy Bands & Carrier Statistics -->

**Plan:** the Fermi–Dirac distribution function; density of states; Fermi energy level calculation as a function of temperature and doping.

To find how many electrons and holes there are, multiply **how many states exist** at each energy (density of states) by **the probability each is occupied** (Fermi–Dirac function), and integrate over the band:

    n = ∫ g_c(E) f(E) dE      (over the conduction band)
    p = ∫ g_v(E) [1 − f(E)] dE   (over the valence band)

## The Fermi–Dirac distribution

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

## Density of states

The **density of states** g(E) is the number of allowed electron states per unit energy per unit volume (cm⁻³eV⁻¹). For parabolic bands with effective masses m_n∗ and m_p∗:

    g_c(E) = (4π (2m_n∗)^{3/2} / h³) √(E − E_c)     for E ≥ E_c
    g_v(E) = (4π (2m_p∗)^{3/2} / h³) √(E_v − E)     for E ≤ E_v

It is zero inside the gap and grows as the square root of the energy measured into each band.

**Origin (sketch).** In a cube of side L, the allowed wave vectors form a grid with one point per (2π/L)³ of k-space. Counting points in a spherical shell of radius k, including two spin states, and using E − E_c = ħ²k²/2m_n∗, gives the √(E − E_c) form.

## Position of the Fermi level

    n-type:  E_c − E_F = kT ln(N_c / N_D),    E_F − E_i = kT ln(N_D / n_i)
    p-type:  E_F − E_v = kT ln(N_v / N_A),    E_i − E_F = kT ln(N_A / n_i)

@fig figures/fermi-level.svg | The Fermi level moves towards the conduction band with donor doping and towards the valence band with acceptor doping. Each factor of 10 in doping shifts it by kT ln10 = 60 mV at 300 K.

- The heavier the doping, the closer E_F gets to the band edge. When it comes within about 3kT of the edge (above about 10¹⁸–10¹⁹ cm⁻³ in Si) the semiconductor is **degenerate** and behaves almost like a metal.
- As temperature rises, n_i grows and E_F moves back towards E_i.
- **In equilibrium E_F is constant throughout any system**, including across junctions. This single fact sets up the built-in voltage of a p-n junction (Week 10).

## Fermi level against temperature

The Fermi level depends on temperature through n_i(T) and through the ionisation of dopants.

    n_i(T) = √(N_c N_v) e^{−E_g/2kT},   with N_c, N_v ∝ T^{3/2}

For n-type material with complete ionisation, solve charge neutrality exactly:

    n = N_D/2 + √( (N_D/2)² + n_i² ),     E_F − E_i = kT ln(n/n_i)

| Region | Condition | n | E_F |
|---|---|---|---|
| Freeze-out (low T) | kT ≪ E_c − E_D | n < N_D, donors not ionised | Between E_D and E_c |
| Extrinsic (normal operation) | n_i ≪ N_D | n ≈ N_D | E_F − E_i = kT ln(N_D/n_i), slowly falling with T |
| Intrinsic (high T) | n_i ≥ N_D | n ≈ n_i | E_F → E_i (mid-gap) |

### Worked example: Fermi level against temperature

Si with N_D = 10¹⁵ cm⁻³. Here n_i(T) is calculated from n_i ∝ T^{3/2}e^{−E_g(T)/2kT}, with the band gap shrinking slightly with temperature (E_g = 1.12 eV at 300 K, 1.03 eV at 600 K) and scaled to n_i = 1×10¹⁰ cm⁻³ at 300 K.

| T (K) | kT (eV) | n_i (cm⁻³) | n (cm⁻³) | E_F − E_i = kT ln(n/n_i) (eV) |
|---|---|---|---|---|
| 300 | 0.0259 | 1.0×10¹⁰ | 1.00×10¹⁵ | 0.0259 × ln(1.0×10⁵) = 0.298 |
| 400 | 0.0345 | 5.3×10¹² | 1.00×10¹⁵ | 0.0345 × ln(189) = 0.181 |
| 500 | 0.0431 | 2.6×10¹⁴ | 1.06×10¹⁵ | 0.0431 × ln(4.16) = 0.061 |
| 600 | 0.0517 | 3.7×10¹⁵ | 4.18×10¹⁵ | 0.0517 × ln(1.15) = 0.007 |

As T rises, E_F moves back towards mid-gap. Above about 550 K, n_i exceeds N_D and the material is effectively intrinsic: the doping no longer controls it. The Laboratory page simulates this curve in Python (Practical 1).

@fig figures/fermi-vs-t.svg | Fermi level relative to E_i against temperature for silicon at four donor concentrations (cm⁻³). Heavier doping keeps the Fermi level away from mid-gap up to a higher temperature.

### Worked example: Fermi level against doping

Si at 300 K. Find E_F for (a) N_D = 10¹⁷ cm⁻³ and (b) N_A = 5×10¹⁵ cm⁻³, relative to E_i and to the nearest band edge (N_c = 2.8×10¹⁹, N_v = 1.04×10¹⁹ cm⁻³).

    (a) E_F − E_i = 0.0259 ln(10¹⁷/10¹⁰) = 0.0259 × 16.12 = 0.417 eV
        E_c − E_F = 0.0259 ln(2.8×10¹⁹/10¹⁷) = 0.0259 × 5.63 = 0.146 eV

    (b) E_i − E_F = 0.0259 ln(5×10¹⁵/10¹⁰) = 0.0259 × 13.12 = 0.340 eV
        E_F − E_v = 0.0259 ln(1.04×10¹⁹/5×10¹⁵) = 0.0259 × 7.64 = 0.198 eV

Check (a): 0.417 + 0.146 = 0.563 eV ≈ E_g/2 = 0.56 eV. ✓

---

## Examination questions solved (Q30–Q33)

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

**As T increases**, the step softens over a range of about ±3kT: some states just below E_F become empty and some just above become filled. This tail reaching into the conduction band is what produces free electrons at room temperature. At E = E_F, f = ½ always. (See the Fermi–Dirac figure above.)

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

(See the Fermi-level figure above.)
