# Week 5 — Carrier Statistics
<!-- group: Module 2 · Energy Bands & Carrier Statistics -->

**Plan:** the Fermi–Dirac distribution function; density of states; Fermi energy level calculation as a function of temperature and doping. This page follows the order of your lecturer's carrier-statistics note (sections 7–26) and adds the background those sections assume.

## Learning objectives

By the end of this week you should be able to:

1. Define and use the Fermi–Dirac distribution function.
2. Explain the physical meaning of the Fermi level and the shape of f(E) at 0 K.
3. Explain the density of states and the effective density of states.
4. Calculate electron and hole concentrations and apply the mass action law.
5. Determine the position of the Fermi level for given doping.
6. Apply the charge-neutrality condition, including compensated material.
7. Explain the effect of temperature on carrier concentration and the Fermi level.
8. Distinguish degenerate and non-degenerate semiconductors.

## Symbols and abbreviations used this week

Every symbol, constant and abbreviation on this page is listed here, even if an earlier week already defined it, so you can study this page on its own.

**Constants and units**

| Symbol | Meaning | Units / typical value |
|---|---|---|
| k | Boltzmann constant | 8.617×10⁻⁵ eV/K = 1.381×10⁻²³ J/K |
| kT | Thermal energy | 0.0259 eV (often 0.02585 eV) at 300 K |
| T | Absolute temperature | kelvin (K); room temperature = 300 K |
| h | Planck constant | 6.626×10⁻³⁴ J·s |
| ħ | Reduced Planck constant, h/2π | 1.055×10⁻³⁴ J·s |
| m₀ | Free-electron mass | 9.11×10⁻³¹ kg |
| eV | Electron-volt, a unit of energy | 1 eV = 1.6×10⁻¹⁹ J |

**Symbols**

| Symbol | Meaning | Units / typical value |
|---|---|---|
| E_c (E_C) | Energy of the bottom of the conduction band | eV |
| E_v (E_V) | Energy of the top of the valence band | eV |
| E_g | Band-gap energy, E_c − E_v | eV; Si 1.12, Ge 0.66, GaAs 1.42 at 300 K |
| E_F | Fermi level: the energy at which a state has a 50 % chance of being occupied | eV |
| E_i | Intrinsic Fermi level, close to mid-gap | eV |
| E_Fn, E_Fp | Quasi-Fermi levels for electrons and holes, used out of equilibrium | eV |
| E_D | Donor energy level, just below E_c | eV; E_c − E_D ≈ 0.045 eV for P in Si |
| f(E) | Fermi–Dirac function: probability that a state at energy E is occupied | dimensionless, 0 to 1 |
| g(E), g_c, g_v | Density of states: allowed states per unit energy per unit volume | states/(eV·cm³) |
| N_c | Effective density of states in the conduction band | cm⁻³; Si 2.8×10¹⁹ at 300 K |
| N_v | Effective density of states in the valence band | cm⁻³; Si 1.04×10¹⁹ at 300 K |
| n | Electron concentration (free electrons per cm³) | cm⁻³ |
| p | Hole concentration (holes per cm³) | cm⁻³ |
| n_i | Intrinsic carrier concentration (n = p = n_i in pure material) | cm⁻³; Si ≈ 1×10¹⁰ at 300 K |
| N_D | Donor concentration | cm⁻³ |
| N_A | Acceptor concentration | cm⁻³ |
| N_D⁺, N_A⁻ | Concentrations of ionised donors and acceptors | cm⁻³ |
| m∗, m_n∗, m_p∗ | Effective mass of electrons or holes | kg, or as a multiple of m₀ |
| k (wave vector) | Wave vector, 2π/λ; measures the electron's momentum, p = ħk | m⁻¹ or cm⁻¹ |

**Abbreviations**

| Abbreviation | Meaning |
|---|---|
| Si | Silicon |
| GaAs | Gallium arsenide |
| MOS | Metal–oxide–semiconductor |
| n⁺ | Very heavily doped n-type (similarly p⁺) |
| FD | Fermi–Dirac (distribution) |


## The big picture

**Carrier statistics** is the method for answering one question: **how many free electrons and holes does a piece of semiconductor contain?** Everything else in the course (conductivity, diodes, transistors) depends on that number.

Think of the conduction band as a large theatre:

- The **seats** are the allowed energy states. How many seats there are at each energy is the **density of states**.
- Whether a seat is **occupied** is a matter of probability. The probability is given by the **Fermi–Dirac function**.
- The number of electrons = (number of seats) × (probability each is filled), added up over all energies.

    number of electrons = Σ (states available) × (probability occupied)

The **Fermi level E_F** is the single number that sets those probabilities. Once you know where E_F sits in the band gap, you know n and p. That is why most of this week is about finding E_F.

## 1. The Fermi–Dirac distribution function

Electrons obey the **Pauli exclusion principle**: no two can occupy the same state. In thermal equilibrium, the probability that a state at energy E is occupied by an electron is:

    f(E) = 1 / ( 1 + e^{(E − E_F)/kT} )

| Symbol | Meaning |
|---|---|
| f(E) | probability (between 0 and 1) that a state at energy E holds an electron |
| E | energy of the state (eV) |
| E_F | the **Fermi energy** or Fermi level (eV) |
| k | Boltzmann constant, 8.617×10⁻⁵ eV/K |
| T | absolute temperature (K); kT = 0.02585 eV at 300 K |

### Three things to remember about f(E)

1. **At E = E_F**, the exponent is zero, e⁰ = 1, and f = 1/(1 + 1) = **½**. The Fermi level is the energy where a state has a 50 % chance of being occupied, at any temperature.
2. **Below E_F** (E < E_F), the exponent is negative, so f is close to 1: states are almost certainly full.
3. **Above E_F** (E > E_F), the exponent is positive, so f is close to 0: states are almost certainly empty.

The change from "full" to "empty" happens over a few kT (about ±0.1 eV at room temperature).

**At absolute zero** (T = 0 K), kT → 0 and the change becomes instantaneous: f = 1 for every state below E_F and f = 0 for every state above. f(E) is a **sharp step**. A pure semiconductor at 0 K therefore has a full valence band, an empty conduction band, and no free carriers.

@fig figures/fermi.svg | The Fermi–Dirac function. At 0 K it is a step at E_F. At 300 K and 900 K the step is smoothed over a few kT. It always passes through ½ at E_F.

**Probability that a state is empty.** A state is either full or empty, so

    probability empty = 1 − f(E)

An empty state in the valence band is a **hole**, so 1 − f(E) is the probability of finding a hole.

### Calculating an occupation probability

At 300 K (kT = 0.02585 eV), a state 0.10 eV **above** E_F:

    (E − E_F)/kT = 0.10/0.02585 = 3.868
    f = 1/(1 + e^{3.868}) = 1/(1 + 47.85) = 0.0205

About a **2 % chance** of being occupied. A state 0.10 eV **below** E_F has f = 1/(1 + e^{−3.868}) = 0.980, a 98 % chance; its probability of being empty is 2 %. The function is symmetric about E_F.

### The Boltzmann approximation

If E − E_F is more than about 3kT (0.08 eV at 300 K), e^{(E−E_F)/kT} is much larger than 1, and we can drop the "1 +":

    f(E) ≈ e^{−(E − E_F)/kT}       (Maxwell–Boltzmann approximation)

This is accurate to better than 5 %. For the 0.10 eV example: e^{−3.868} = 0.0209, against the exact 0.0205. Almost every calculation in this course uses this approximation, because the conduction band is usually well above E_F.

## 2. Density of states

The **density of states** g(E) is the number of allowed electron states per unit energy, per unit volume, at energy E (units: states per eV per cm³).

    Conduction band:  g_c(E) ∝ (m_n∗)^{3/2} √(E − E_c)     for E above E_c
    Valence band:     g_v(E) ∝ (m_p∗)^{3/2} √(E_v − E)     for E below E_v
    In the gap:       g(E) = 0

In words: there are **no states in the gap**; just above E_c the number of states starts at zero and grows as the square root of how far you go into the band. The effective masses m_n∗ and m_p∗ describe the shape of each band; a heavier mass means more states.

### Effective density of states

Adding up "states × probability" over the whole conduction band (with the Boltzmann approximation) gives a very simple result. It is **as if** all the conduction-band states were squeezed into one level at E_c, with a total number N_c of them. N_c is the **effective density of states**:

    N_c = 2 (2π m_n∗ kT / h²)^{3/2},     N_v = 2 (2π m_p∗ kT / h²)^{3/2}

For silicon at 300 K: **N_c = 2.8×10¹⁹ cm⁻³**, **N_v = 1.04×10¹⁹ cm⁻³**. Both grow with temperature as T^{3/2}.

## 7. Electron concentration

The electron concentration in the conduction band is obtained by adding up available states × occupation probability:

    n = ∫ g_c(E) f(E) dE     (from E_c to the top of the band)

For a **non-degenerate** semiconductor, f(E) is replaced by the Maxwell–Boltzmann form, and the integral gives:

    n = N_c e^{−(E_c − E_F)/kT}

or, measuring from the intrinsic level E_i,

    n = n_i e^{(E_F − E_i)/kT}

**Reading it.** E_c − E_F is the distance from the Fermi level up to the conduction-band edge. The smaller that distance, the larger n, and the dependence is exponential: every 60 mV that E_F moves towards E_c multiplies n by 10.

## 8. Hole concentration

The probability that a valence-band state is **empty** is 1 − f(E). The hole concentration is

    p = ∫ g_v(E) [1 − f(E)] dE     (over the valence band)

For a non-degenerate semiconductor this gives:

    p = N_v e^{−(E_F − E_v)/kT}

and

    p = n_i e^{(E_i − E_F)/kT}

These four equations (two for n, two for p) are the fundamental equations of semiconductor carrier statistics.

## 9. Position of the Fermi level

Turn the electron equation round to find E_F when n is known. From n = N_c e^{−(E_c − E_F)/kT}, divide by N_c and take the natural logarithm:

    ln(n/N_c) = −(E_c − E_F)/kT

Therefore:

    E_c − E_F = kT ln(N_c/n)

Similarly, from the hole concentration:

    E_F − E_v = kT ln(N_v/p)

And, using the intrinsic level:

    E_F − E_i = kT ln(n/n_i),     E_i − E_F = kT ln(p/n_i)

These equations let the Fermi level be calculated when the carrier concentration is known.

#### Example 5.1: Fermi level from the electron concentration

**Question.** An n-type silicon sample at 300 K has an electron concentration of 1×10¹⁶ cm⁻³. Taking N_c = 2.8×10¹⁹ cm⁻³ and kT = 0.02585 eV, find how far the Fermi level lies below the conduction-band edge.

**Given:** n = 1×10¹⁶ cm⁻³, N_c = 2.8×10¹⁹ cm⁻³, kT = 0.02585 eV.

**Find:** E_c − E_F.

**Solution.**

Use E_c − E_F = kT ln(N_c/n):

    N_c/n = 2.8×10¹⁹ / 1×10¹⁶ = 2800,   ln(2800) = 7.94

    E_c − E_F = 0.02585 × 7.94 = 0.205 eV

**Answer:** **E_c − E_F = 0.205 eV**: the Fermi level is 0.205 eV below the conduction band.

## 10. Intrinsic semiconductor

A semiconductor with no intentional donor or acceptor doping is called **intrinsic**. Every free electron came from a broken bond that also left a hole, so

    n = p = n_i

where n_i is the **intrinsic carrier concentration**. Multiplying the n and p equations, E_F cancels out:

    n · p = N_c N_v e^{−(E_c − E_v)/kT} = N_c N_v e^{−E_g/kT}

and since n = p = n_i,

    n_i = √(N_c N_v) · e^{−E_g/2kT}

where E_g = E_c − E_v is the band-gap energy. This equation shows that the intrinsic carrier concentration depends strongly on temperature and on the band gap. For Si at 300 K, n_i ≈ 1×10¹⁰ cm⁻³ (many textbooks use 1.5×10¹⁰; the accurate modern value is 9.65×10⁹).

## 11. Intrinsic Fermi level

For an intrinsic semiconductor, n = p. Set the two expressions equal:

    N_c e^{−(E_c − E_i)/kT} = N_v e^{−(E_i − E_v)/kT}

Solving for E_i gives

    E_i = (E_c + E_v)/2 + (kT/2) ln(N_v/N_c)

If N_c and N_v were equal, the logarithm would be zero, and then

    E_i = (E_c + E_v)/2

Thus the intrinsic Fermi level is approximately at the **middle of the forbidden gap**. For Si the correction is (0.02585/2) ln(1.04/2.8) = −0.013 eV, only 13 meV below mid-gap.

## 12. Mass action law

For a semiconductor in thermal equilibrium:

    n · p = n_i²

This is the **mass action law**. It holds for intrinsic and doped (non-degenerate) material alike, because when we multiplied n by p above, E_F cancelled.

- For an **intrinsic** semiconductor n = p, therefore n = p = n_i.
- For an **n-type** semiconductor where n ≫ p: n ≈ N_D, and therefore **p = n_i²/N_D**.
- For a **p-type** semiconductor where p ≫ n: p ≈ N_A, and therefore **n = n_i²/N_A**.

> **In plain words.** n × p is fixed. Add donors, and the extra electrons fill in holes, so the hole count drops by exactly the same factor the electron count rises. Doping one carrier up pushes the other down.

## 13. Effect of doping on the Fermi level

Doping changes the concentration of carriers, and therefore shifts the Fermi level.

**N-type.** Donor atoms introduce additional electrons, so the Fermi level moves **towards the conduction band**:

    E_c − E_F = kT ln(N_c/n),     E_F − E_i = kT ln(n/n_i)

If donors are fully ionised and N_D ≫ n_i, then n ≈ N_D, and

    E_c − E_F = kT ln(N_c/N_D),     E_F − E_i = kT ln(N_D/n_i)

**P-type.** Acceptor atoms create holes, so the Fermi level moves **towards the valence band**:

    E_F − E_v = kT ln(N_v/p),     E_i − E_F = kT ln(p/n_i)

If acceptors are fully ionised, p ≈ N_A, so

    E_F − E_v = kT ln(N_v/N_A),     E_i − E_F = kT ln(N_A/n_i)

@fig figures/fermi-level.svg | Where the Fermi level sits: at mid-gap (E_i) when intrinsic, near E_c for n-type, near E_v for p-type.

**How big are the shifts?** Each factor of 10 in doping moves E_F by kT ln 10 = 0.0595 eV ≈ 60 mV at 300 K.

| Doping (Si, 300 K) | E_F − E_i | E_c − E_F |
|---|---|---|
| Intrinsic | 0 | 0.56 eV |
| N_D = 10¹⁴ cm⁻³ | 0.238 eV | 0.324 eV |
| N_D = 10¹⁶ cm⁻³ | 0.357 eV | 0.205 eV |
| N_D = 10¹⁸ cm⁻³ | 0.476 eV | 0.086 eV |

## 14. Charge neutrality in a doped semiconductor

A piece of semiconductor is electrically neutral overall. The positive charges (holes and ionised donors) must equal the negative charges (electrons and ionised acceptors):

    p + N_D⁺ = n + N_A⁻

where p is the hole concentration, n the electron concentration, N_D⁺ the concentration of ionised donors and N_A⁻ the concentration of ionised acceptors. If donors and acceptors are completely ionised (N_D⁺ = N_D, N_A⁻ = N_A):

    p + N_D = n + N_A

This is the **charge-neutrality condition**. Combined with np = n_i² it gives n exactly:

    n = (N_D − N_A)/2 + √( ((N_D − N_A)/2)² + n_i² )

When N_D − N_A ≫ n_i, this reduces to n ≈ N_D − N_A. When both dopants are present they partly cancel, which is called **compensation**.

## 15. N-type semiconductor

When silicon is doped with a donor impurity (phosphorus P, arsenic As, antimony Sb), it becomes n-type. A donor contributes an extra electron. If N_D ≫ n_i and all donors are ionised:

    n ≈ N_D

Using the mass action law np = n_i², we obtain:

    p ≈ n_i² / N_D

## 16. P-type semiconductor

When silicon is doped with an acceptor impurity (boron B, aluminium Al, gallium Ga), it becomes p-type. An acceptor creates a hole. If N_A ≫ n_i, then:

    p ≈ N_A

and:

    n ≈ n_i² / N_A

## 17. Fermi level as a function of temperature

Temperature has a major effect on carrier concentration and Fermi level. There are generally three regions:

**Region 1: Freeze-out region.** At very low temperature (below about 100 K in Si), donor and acceptor atoms are not fully ionised: there is not enough thermal energy to free the extra electron from each donor. Consequently there are relatively few free carriers, and n < N_D.

**Region 2: Extrinsic region.** At moderate temperature (roughly 150–450 K for Si), the dopants are fully ionised:

    n-type: n ≈ N_D          p-type: p ≈ N_A

The carrier concentration is set by the doping and hardly changes with temperature. This is the region used in most basic semiconductor calculations, and the region where devices operate.

**Region 3: Intrinsic region.** At sufficiently high temperature, thermally generated electron–hole pairs become dominant. Eventually

    n_i ≫ N_D   so   n ≈ p ≈ n_i

The semiconductor behaves more and more like an intrinsic semiconductor, and E_F returns to E_i. The doping no longer controls the material, which is why every device has a maximum operating temperature.

#### Example 5.2: Fermi level against temperature

**Question.** Silicon is doped with N_D = 1×10¹⁵ cm⁻³. Using the intrinsic concentrations in the table (n_i = 1×10¹⁰ cm⁻³ at 300 K, rising with temperature), calculate the electron concentration and the position of the Fermi level relative to E_i at 300, 400, 500 and 600 K. At what temperature does the material become effectively intrinsic?

**Given:** N_D = 1×10¹⁵ cm⁻³, complete ionisation; n_i(T) from n_i ∝ T^{3/2}e^{−E_g(T)/2kT}, scaled to 1×10¹⁰ cm⁻³ at 300 K.

**Find:** n and E_F − E_i at each temperature.

**Solution.** At each temperature use the exact charge-neutrality result, n = N_D/2 + √((N_D/2)² + n_i²), then E_F − E_i = kT ln(n/n_i).

| T (K) | kT (eV) | n_i (cm⁻³) | n (cm⁻³) | E_F − E_i = kT ln(n/n_i) (eV) |
|---|---|---|---|---|
| 300 | 0.0259 | 1.0×10¹⁰ | 1.00×10¹⁵ | 0.0259 × ln(1.0×10⁵) = 0.298 |
| 400 | 0.0345 | 5.3×10¹² | 1.00×10¹⁵ | 0.0345 × ln(189) = 0.181 |
| 500 | 0.0431 | 2.6×10¹⁴ | 1.06×10¹⁵ | 0.0431 × ln(4.16) = 0.061 |
| 600 | 0.0517 | 3.7×10¹⁵ | 4.18×10¹⁵ | 0.0517 × ln(1.15) = 0.007 |

**Answer:** E_F − E_i falls from **0.298 eV at 300 K to 0.007 eV at 600 K**. n_i passes N_D at about **550 K**; above that the material is effectively intrinsic and the doping no longer controls it.

@fig figures/fermi-vs-t.svg | Fermi level relative to E_i against temperature for silicon at four donor concentrations (cm⁻³). Heavier doping keeps the Fermi level away from mid-gap up to a higher temperature.

## 18. Worked example: n-type silicon

#### Example 5.3: majority and minority carriers

**Question.** Silicon at 300 K is doped with N_D = 1×10¹⁶ cm⁻³. Assuming n_i = 1×10¹⁰ cm⁻³ and complete donor ionisation, calculate the electron and hole concentrations and identify the majority and minority carriers.

**Given:** N_D = 1×10¹⁶ cm⁻³, n_i = 1×10¹⁰ cm⁻³, T = 300 K.

**Find:** n, p; majority and minority carriers.

**Solution.**

Step 1: electron concentration. Since N_D ≫ n_i (10¹⁶ ≫ 10¹⁰), every donor contributes one electron:

    n ≈ N_D = 1×10¹⁶ cm⁻³

Step 2: hole concentration, from the mass-action law:

    p = n_i²/n = (1×10¹⁰)² / (1×10¹⁶) = 10²⁰/10¹⁶ = 1×10⁴ cm⁻³

**Answer:** **n = 1×10¹⁶ cm⁻³, p = 1×10⁴ cm⁻³.** Electrons are the majority carriers, holes the minority carriers. (With n_i = 1.5×10¹⁰ cm⁻³, p = 2.25×10⁴ cm⁻³; the method is identical.)

## 19. Worked example: Fermi level of n-type silicon

#### Example 5.4: Fermi level of n-type silicon

**Question.** For the silicon of Example 5.3 (n = N_D = 1×10¹⁶ cm⁻³, n_i = 1×10¹⁰ cm⁻³) at 300 K, calculate the position of the Fermi level relative to the intrinsic level, and estimate how far it lies below the conduction band.

**Given:** n = 1×10¹⁶ cm⁻³, n_i = 1×10¹⁰ cm⁻³, kT = 0.02585 eV, E_g = 1.12 eV.

**Find:** E_F − E_i, and E_c − E_F.

**Solution.**

    E_F − E_i = kT ln(n/n_i) = 0.02585 × ln(10¹⁶/10¹⁰) = 0.02585 × ln(10⁶)

Since ln(10⁶) = 6 × 2.303 = 13.82,

    E_F − E_i = 0.02585 × 13.82 = 0.357 eV

E_i is close to mid-gap, 0.56 eV below E_c, so

    E_c − E_F ≈ 0.56 − 0.357 = 0.20 eV

**Answer:** **E_F = E_i + 0.357 eV**, about 0.20 eV below E_c: the Fermi level has moved up towards the conduction band. (With n_i = 1.5×10¹⁰ cm⁻³: E_F − E_i = 0.02585 ln(6.67×10⁵) = 0.347 eV.)

## 20. Worked example: p-type silicon

#### Example 5.5: carriers and Fermi level in p-type silicon

**Question.** Silicon at 300 K is doped with N_A = 1×10¹⁷ cm⁻³ boron atoms. Taking n_i = 1×10¹⁰ cm⁻³, calculate the hole and electron concentrations and the position of the Fermi level.

**Given:** N_A = 1×10¹⁷ cm⁻³, n_i = 1×10¹⁰ cm⁻³, kT = 0.02585 eV.

**Find:** p, n and E_i − E_F.

**Solution.**

    p ≈ N_A = 1×10¹⁷ cm⁻³
    n = n_i²/p = 10²⁰/10¹⁷ = 1×10³ cm⁻³
    E_i − E_F = kT ln(p/n_i) = 0.02585 × ln(10⁷) = 0.02585 × 16.12 = 0.417 eV

**Answer:** **p = 1×10¹⁷ cm⁻³, n = 1×10³ cm⁻³, E_F = E_i − 0.417 eV**: the Fermi level moves down towards the valence band, about 0.56 − 0.417 = 0.14 eV above E_v.

## 21. Degenerate and non-degenerate semiconductors

The Maxwell–Boltzmann approximation is valid only when the Fermi level is far enough from the band edges. For a **non-degenerate** semiconductor:

    E_c − E_F ≫ kT  (n-type),     E_F − E_v ≫ kT  (p-type)

In practice "≫" means more than about 3kT.

In a **degenerate** semiconductor the doping is very high (in Si, above about 10¹⁸–10¹⁹ cm⁻³) and the Fermi level approaches, or even enters, the conduction or valence band. Then the full Fermi–Dirac statistics must be used, and the material behaves almost like a metal. Degenerate n⁺ and p⁺ layers are used for Ohmic contacts (Week 11) and tunnel diodes.

| Feature | Non-degenerate | Degenerate |
|---|---|---|
| Doping | Relatively low or moderate | Very high |
| Statistics | Maxwell–Boltzmann approximation | Fermi–Dirac |
| Fermi level | Inside the band gap, more than 3kT from the edges | Near or inside a band |
| Carrier concentration | Simple exponential equations | More complex |

**Check.** For Si with N_D = 10¹⁸ cm⁻³, E_c − E_F = 0.02585 ln(2.8×10¹⁹/10¹⁸) = 0.086 eV = 3.3kT, just non-degenerate. At 10¹⁹ cm⁻³, E_c − E_F = 0.027 eV ≈ 1kT: degenerate.

## 22. Relationship between carrier concentration and Fermi level

The electron concentration increases exponentially as the Fermi level approaches the conduction band, n = N_c e^{−(E_c − E_F)/kT}. Similarly, the hole concentration increases as the Fermi level approaches the valence band, p = N_v e^{−(E_F − E_v)/kT}. Therefore:

- Fermi level closer to E_c → more electrons (n-type).
- Fermi level closer to E_v → more holes (p-type).
- Fermi level at E_i → n = p = n_i (intrinsic).

## 23. Temperature dependence of intrinsic carrier concentration

Recall n_i = √(N_cN_v) e^{−E_g/2kT}. Since N_c and N_v are each proportional to T^{3/2}, their product's square root is proportional to T^{3/2}, so approximately

    n_i ∝ T^{3/2} e^{−E_g/2kT}

The **exponential term** is especially important. As temperature increases, kT increases, the negative exponent −E_g/2kT gets smaller in magnitude, and e^{−E_g/2kT} increases rapidly. The T^{3/2} factor adds a smaller increase. For silicon, n_i roughly doubles every 8 °C near room temperature, and rises about 25,000 times between 300 K and 500 K.

Therefore semiconductor conductivity generally **increases with temperature**, because more electron–hole pairs are thermally generated.

## 24. Formula sheet for carrier statistics

| Quantity | Formula |
|---|---|
| Fermi–Dirac function | f(E) = 1/(1 + e^{(E − E_F)/kT}) |
| Electron concentration | n = N_c e^{−(E_c − E_F)/kT} = n_i e^{(E_F − E_i)/kT} |
| Hole concentration | p = N_v e^{−(E_F − E_v)/kT} = n_i e^{(E_i − E_F)/kT} |
| Effective density of states | N_c = 2(2πm_n∗kT/h²)^{3/2}, N_v = 2(2πm_p∗kT/h²)^{3/2} |
| Intrinsic carrier concentration | n_i = √(N_cN_v) e^{−E_g/2kT} |
| Mass action law | np = n_i² |
| Intrinsic Fermi level | E_i = (E_c + E_v)/2 + (kT/2) ln(N_v/N_c) ≈ mid-gap |
| N-type Fermi level | E_F − E_i = kT ln(N_D/n_i) |
| P-type Fermi level | E_i − E_F = kT ln(N_A/n_i) |
| Charge neutrality | p + N_D⁺ = n + N_A⁻ |

## 25. Summary: what you should be able to do

1. Explain the concept of carrier statistics in semiconductors.
2. Define and use the Fermi–Dirac distribution function.
3. Explain the physical meaning of the Fermi energy level.
4. Calculate the probability of electron occupation of an energy state.
5. Explain the density of states in the conduction and valence bands.
6. Calculate electron and hole concentrations.
7. Calculate the intrinsic carrier concentration.
8. Apply the mass action law.
9. Determine the position of the Fermi level.
10. Explain the effect of donor and acceptor doping on the Fermi level.
11. Distinguish between intrinsic, n-type and p-type semiconductors.
12. Explain the effect of temperature on carrier concentration.
13. Distinguish between degenerate and non-degenerate semiconductors.
14. Apply the charge-neutrality equation to doped semiconductors.

---

## 26. Mid-module evaluation, solved

These are the lecturer's mid-module evaluation questions. The numerical values in the printed note did not come through in the copy provided, so the calculations below use the standard silicon values stated in each question. If your copy gives different numbers, follow the same steps.

### Part A: short-answer questions

**A1. Define carrier statistics.** Carrier statistics is the study of how electrons and holes are distributed among the allowed energy states of a semiconductor in thermal equilibrium. It combines the density of states with the Fermi–Dirac probability to calculate the electron and hole concentrations and the position of the Fermi level.

**A2. What is the Fermi energy level?** The Fermi level E_F is the energy at which the probability of a state being occupied by an electron is exactly one half. At 0 K it is the boundary between filled and empty states. Its position relative to E_c and E_v determines the electron and hole concentrations, and in equilibrium it is constant throughout a material or device.

**A3. State the Fermi–Dirac distribution function.** f(E) = 1/(1 + e^{(E − E_F)/kT}), where f(E) is the probability that a state of energy E is occupied, E_F the Fermi level, k Boltzmann's constant and T the absolute temperature.

**A4. What is the probability that a state at E = E_F is occupied?** Exactly **½ (50 %)**, because the exponent is zero: f = 1/(1 + e⁰) = 1/2. This is true at any temperature.

**A5. Define density of states.** The density of states g(E) is the number of allowed electron energy states per unit energy per unit volume at energy E (states/eV·cm³). In a parabolic band, g_c(E) ∝ √(E − E_c) in the conduction band and g_v(E) ∝ √(E_v − E) in the valence band; it is zero in the band gap.

**A6. What is meant by effective density of states?** The effective density of states (N_c for the conduction band, N_v for the valence band) is the number of states that, if all placed at the band edge, would give the same carrier concentration as the real distributed band. It lets the carrier concentration be written simply as n = N_ce^{−(E_c − E_F)/kT}. For Si at 300 K, N_c = 2.8×10¹⁹ and N_v = 1.04×10¹⁹ cm⁻³.

**A7. Distinguish between intrinsic and extrinsic semiconductors.** An intrinsic semiconductor is pure: its carriers come only from thermal breaking of bonds, so n = p = n_i and E_F ≈ E_i (mid-gap). An extrinsic semiconductor is doped with donors or acceptors: one carrier type dominates (n ≈ N_D or p ≈ N_A), E_F moves towards E_c or E_v, and the carrier concentration is set by the doping rather than by temperature.

**A8. Define majority and minority carriers.** Majority carriers are the more numerous carrier type in a doped semiconductor (electrons in n-type, holes in p-type). Minority carriers are the less numerous type (holes in n-type, electrons in p-type). In n-type Si with N_D = 10¹⁶ cm⁻³, there are 10¹⁶ majority electrons and only 10⁴ minority holes per cm³.

**A9. State the mass action law.** In thermal equilibrium the product of the electron and hole concentrations is constant at a given temperature: np = n_i², regardless of doping (for a non-degenerate semiconductor).

**A10. Explain why doping changes the Fermi level.** The Fermi level is tied to the carrier concentrations by n = n_ie^{(E_F − E_i)/kT}. Donors add electrons, so n rises above n_i; for the equation to hold, E_F must rise above E_i (towards E_c), by kT ln(N_D/n_i). Acceptors add holes, so p rises and E_F must fall towards E_v by kT ln(N_A/n_i). The heavier the doping, the larger the shift.

### Part B: calculation questions

**B1. At 300 K, find the probability that a state 0.10 eV above the Fermi level is occupied (kT = 0.02585 eV).**

    f = 1/(1 + e^{0.10/0.02585}) = 1/(1 + e^{3.868}) = 1/(1 + 47.85) = 0.0205

The probability is **0.0205, about 2 %**.

**B2. Silicon has N_D = 1×10¹⁶ cm⁻³ and n_i = 1×10¹⁰ cm⁻³. Assuming complete ionisation, find (a) n, (b) p, (c) the majority carrier.**

    (a) n ≈ N_D = 1×10¹⁶ cm⁻³
    (b) p = n_i²/n = 10²⁰/10¹⁶ = 1×10⁴ cm⁻³
    (c) Electrons are the majority carriers (n-type).

**B3. P-type silicon has N_A = 5×10¹⁶ cm⁻³ and n_i = 1×10¹⁰ cm⁻³. Find (a) p, (b) n, (c) the minority carrier.**

    (a) p ≈ N_A = 5×10¹⁶ cm⁻³
    (b) n = n_i²/p = 10²⁰/(5×10¹⁶) = 2×10³ cm⁻³
    (c) Electrons are the minority carriers.

**B4. At 300 K an n-type semiconductor has N_D = 1×10¹⁷ cm⁻³ and n_i = 1×10¹⁰ cm⁻³. Find the Fermi level relative to the intrinsic level.**

    E_F − E_i = kT ln(N_D/n_i) = 0.02585 × ln(10⁷) = 0.02585 × 16.12 = 0.417 eV

The Fermi level is **0.417 eV above E_i**.

**B5. Explain, using equations, why increasing temperature increases the intrinsic carrier concentration.**

    n_i = √(N_cN_v) e^{−E_g/2kT},   with N_c, N_v ∝ T^{3/2}   ⇒   n_i ∝ T^{3/2} e^{−E_g/2kT}

Two factors increase with T. The T^{3/2} factor grows slowly: more states become effectively available as the electrons' thermal energy spreads. The exponential grows very fast: E_g/2kT becomes smaller as T increases, so e^{−E_g/2kT} increases steeply. Physically, a higher temperature gives more electrons enough thermal energy to cross the band gap, breaking more covalent bonds and creating more electron–hole pairs. For Si, n_i is about 10¹⁰ cm⁻³ at 300 K, 5×10¹² at 400 K and 2.6×10¹⁴ at 500 K.

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
5. **Out of equilibrium**, the concept is extended to quasi-Fermi levels E_{Fn} and E_{Fp}, which are used to describe biased devices.

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

---

## Practice questions

These extra questions practise this week's ideas. Work each one on paper before reading the solution; the calculation questions follow the same Question, Given, Find, Solution, Answer layout as the worked examples.

#### Practice 5.1: accuracy of the Boltzmann approximation

**Question.** Calculate the occupation probability of a state 3kT above the Fermi level using (a) the Fermi–Dirac function and (b) the Boltzmann approximation. What is the error?

**Given:** E − E_F = 3kT.

**Find:** f(FD), f(Boltzmann) and the percentage error.

**Solution.**

    (a) f = 1/(1 + e³) = 1/21.09 = 0.0474
    (b) f ≈ e^{−3} = 0.0498
    error = (0.0498 − 0.0474)/0.0474 = 5 %

**Answer:** **0.0474 against 0.0498, a 5 % error**: this is why "more than 3kT from E_F" is the rule for using the Boltzmann approximation.

#### Practice 5.2: carriers from the Fermi-level position

**Question.** In silicon at 300 K the Fermi level is 0.30 eV below the conduction band. Find the probability that a state at E_c is occupied, and the electron concentration.

**Given:** E_c − E_F = 0.30 eV, kT = 0.0259 eV, N_c = 2.8×10¹⁹ cm⁻³.

**Find:** f(E_c) and n.

**Solution.**

    f(E_c) ≈ e^{−0.30/0.0259} = e^{−11.58} = 9.3×10⁻⁶
    n = N_c e^{−(E_c − E_F)/kT} = 2.8×10¹⁹ × 9.3×10⁻⁶ = 2.6×10¹⁴ cm⁻³

**Answer:** **f = 9.3×10⁻⁶, n = 2.6×10¹⁴ cm⁻³.**

#### Practice 5.3: doping for a chosen Fermi level

**Question.** What donor concentration places the Fermi level of silicon 0.20 eV above the intrinsic level at 300 K?

**Given:** E_F − E_i = 0.20 eV, n_i = 10¹⁰ cm⁻³, kT = 0.02585 eV.

**Find:** N_D.

**Solution.**

    N_D = n_i e^{(E_F − E_i)/kT} = 10¹⁰ × e^{0.20/0.02585} = 10¹⁰ × e^{7.74} = 2.3×10¹³ cm⁻³

**Answer:** **N_D ≈ 2.3×10¹³ cm⁻³**, a very light doping.

#### Practice 5.4: compensated p-type silicon

**Question.** Silicon is doped with N_A = 3×10¹⁶ cm⁻³ and N_D = 1×10¹⁶ cm⁻³. Find p, n and the Fermi-level position at 300 K.

**Given:** N_A = 3×10¹⁶, N_D = 10¹⁶, n_i = 10¹⁰ cm⁻³, kT = 0.02585 eV.

**Find:** p, n and E_i − E_F.

**Solution.**

    p ≈ N_A − N_D = 2×10¹⁶ cm⁻³
    n = n_i²/p = 10²⁰/2×10¹⁶ = 5×10³ cm⁻³
    E_i − E_F = kT ln(p/n_i) = 0.02585 × ln(2×10⁶) = 0.375 eV

**Answer:** **p = 2×10¹⁶ cm⁻³, n = 5×10³ cm⁻³, E_F = E_i − 0.375 eV.**

#### Practice 5.5: lightly doped germanium

**Question.** Germanium (n_i = 2.4×10¹³ cm⁻³) is doped with N_D = 1×10¹⁴ cm⁻³. Find n and p using the full charge-neutrality equation.

**Given:** N_D = 10¹⁴ cm⁻³, N_A = 0, n_i = 2.4×10¹³ cm⁻³.

**Find:** n and p.

**Solution.**

    n = N_D/2 + √((N_D/2)² + n_i²) = 5×10¹³ + √(2.5×10²⁷ + 5.76×10²⁶)
      = 5×10¹³ + 5.55×10¹³ = 1.05×10¹⁴ cm⁻³
    p = n_i²/n = 5.76×10²⁶ / 1.05×10¹⁴ = 5.5×10¹² cm⁻³

**Answer:** **n = 1.05×10¹⁴ cm⁻³, p = 5.5×10¹² cm⁻³.** Thermal generation adds 5 % to the electron count, so n ≈ N_D is only approximate here.

#### Practice 5.6: is it degenerate?

**Question.** Silicon is doped with N_D = 5×10¹⁸ cm⁻³. Find E_c − E_F and decide whether the Boltzmann approximation is valid.

**Given:** N_D = 5×10¹⁸ cm⁻³, N_c = 2.8×10¹⁹ cm⁻³, kT = 0.02585 eV.

**Find:** E_c − E_F in eV and in units of kT.

**Solution.**

    E_c − E_F = kT ln(N_c/N_D) = 0.02585 × ln(5.6) = 0.02585 × 1.72 = 0.045 eV = 1.7kT

**Answer:** **0.045 eV, only 1.7kT**: less than 3kT, so the material is (nearly) degenerate and full Fermi–Dirac statistics should be used.

#### Practice 5.7: where exactly is E_i?

**Question.** Show that the intrinsic level of silicon lies slightly below mid-gap, and by how much.

**Given:** E_i = (E_c + E_v)/2 + (kT/2) ln(N_v/N_c), N_c = 2.8×10¹⁹, N_v = 1.04×10¹⁹ cm⁻³.

**Find:** E_i − mid-gap.

**Solution.**

    (kT/2) ln(N_v/N_c) = (0.02585/2) × ln(1.04/2.8) = 0.0129 × (−0.990) = −0.0128 eV

**Answer:** **E_i is 13 meV below mid-gap**, because the valence band has fewer effective states (N_v < N_c), so E_F must sit a little closer to it to make p equal n.

---

## Objectives check

Use this table to confirm you have met this week's objectives. Cover the Answer column and answer each check question from memory. If you cannot, go back to the section in the last column before moving on.

| # | Objective | Check yourself | Answer | Where it is taught |
|---|---|---|---|---|
| 1 | Define and use the Fermi–Dirac distribution function. | Find the probability that a state 0.2 eV above E_F is occupied at 300 K. | f = 1/(1 + e^{0.2/0.02585}) = 1/(1 + 2290) = 4.4×10⁻⁴. | Section 1 |
| 2 | Explain the physical meaning of the Fermi level and the shape of f(E) at 0 K. | What is f(E) below and above E_F at 0 K? | 1 below E_F, 0 above: a sharp step. | Section 1 |
| 3 | Explain the density of states and the effective density of states. | Why are there no carriers in the band gap even though f(E) is not zero there? | The density of states is zero in the gap: there are no states to occupy. | Section 2 |
| 4 | Calculate electron and hole concentrations and apply the mass action law. | Si with N_A = 10¹⁵ cm⁻³: find p and n (n_i = 10¹⁰ cm⁻³). | p = 10¹⁵, n = 10⁵ cm⁻³. | Sections 7–8, 12, 15–16; Examples 5.3, 5.5 |
| 5 | Determine the position of the Fermi level for given doping. | Find E_F − E_i for N_D = 10¹⁴ cm⁻³. | 0.02585 ln(10⁴) = 0.238 eV. | Sections 9, 13; Examples 5.1, 5.4 |
| 6 | Apply the charge-neutrality condition, including compensated material. | Si has N_D = 5×10¹⁶ and N_A = 2×10¹⁶ cm⁻³. Find n. | n ≈ N_D − N_A = 3×10¹⁶ cm⁻³. | Section 14 |
| 7 | Explain the effect of temperature on carrier concentration and the Fermi level. | Name the three temperature regions and what n equals in the middle one. | Freeze-out, extrinsic (n ≈ N_D), intrinsic. | Sections 17, 23; Example 5.2 |
| 8 | Distinguish degenerate and non-degenerate semiconductors. | When must full Fermi–Dirac statistics be used instead of the Boltzmann approximation? | When E_F is within about 3kT of a band edge (very heavy doping). | Section 21 |
