# Module 06 — Doping and Thermal Diffusion

Lecture note §6 and §28, extended for Q14–Q19. Doping is how a semiconductor's conductivity and carrier type are set. Diffusion is the oldest way of getting the dopant into the wafer.

## 6.1 Doping

**Doping** is the deliberate, controlled addition of small amounts of specific impurity atoms (typically 10¹⁴–10²⁰ cm⁻³, i.e. one in 10⁸ to one in 500 host atoms) to change the type and concentration of carriers.

### Donors: n-type

A Group V atom (P, As, Sb) substitutes for Si. Four of its five valence electrons form bonds; the fifth is only weakly bound (about **0.045 eV** for P in Si, versus E_g = 1.12 eV) and at room temperature is released into the conduction band. The donor becomes a fixed positive ion N_D⁺.

In band terms the donor creates a level E_D just below E_c.

- Electrons: majority carriers. Holes: minority carriers.
- n ≈ N_D, p = n_i²/N_D.

### Acceptors: p-type

A Group III atom (B, Al, Ga, In) substitutes for Si. It has only three valence electrons, so one bond is incomplete. A neighbouring electron easily moves in (about **0.045 eV** for B), leaving a mobile **hole** in the valence band and making the acceptor a fixed negative ion N_A⁻.

In band terms the acceptor creates a level E_A just above E_v.

- Holes: majority. Electrons: minority.
- p ≈ N_A, n = n_i²/N_A.

@fig figures/donor-acceptor.svg | Donor levels sit just below the conduction band and give up electrons; acceptor levels sit just above the valence band and capture electrons, creating holes.

Ionisation energies in Si (eV): P 0.045, As 0.054, Sb 0.039; B 0.045, Al 0.067, Ga 0.072, In 0.16. Because these are only about 2kT, practically all shallow dopants are ionised at 300 K.

**In GaAs:** Group VI (S, Se, Te) on As sites are donors; Group II (Zn, Be, Mg) on Ga sites are acceptors; Group IV Si is **amphoteric** (a donor on a Ga site, an acceptor on an As site).

**Compensation.** If both donors and acceptors are present, they cancel: the net doping is |N_D − N_A|, but both still scatter carriers.

## 6.2 How dopants move: diffusion mechanisms

At high temperature (900–1200 °C for Si) atoms vibrate strongly and occasionally jump to a neighbouring site. Net movement goes from high to low concentration.

1. **Substitutional (vacancy) diffusion.** The dopant sits on a lattice site and can only move when a **vacancy** appears next to it; it then swaps into the vacancy. Slow, because it needs both a vacancy (formation energy) and a jump (migration energy): activation energy 3–4 eV. Main dopants B, P, As, Sb.
2. **Interstitial diffusion.** Small atoms squeeze between lattice sites without needing vacancies. Fast, activation energy 0.5–1.5 eV. Examples: Au, Cu, Fe, Li, H, Na. These metals are lifetime killers.
3. **Interstitialcy (kick-out) mechanism.** A Si self-interstitial pushes a substitutional dopant into an interstitial position, the dopant moves, then kicks a Si atom out. Important for B and P.

The diffusion coefficient follows an Arrhenius law:

    D = D₀ exp(−E_a / kT)

For B in Si: D₀ ≈ 0.76 cm²/s, E_a ≈ 3.46 eV, giving D ≈ 10⁻¹³ cm²/s at 1100 °C. A tiny change in T changes D a lot, so furnace temperature must be held to ±0.5 °C.

## 6.3 Fick's laws

**First law** (flux is proportional to the concentration gradient):

    F = −D ∂C/∂x

F is the flux (atoms per cm² per second), C the concentration (cm⁻³), D the diffusion coefficient (cm²/s). The minus sign means atoms flow **down** the gradient.

**Second law** (conservation of atoms combined with the first law):

    ∂C/∂t = −∂F/∂x = D ∂²C/∂x²

It gives how the concentration profile C(x, t) evolves in time. The two standard solutions correspond to the two steps of a real diffusion process.

### Constant-source (predeposition) diffusion: erfc profile

The surface is held at a fixed concentration C_s (equal to the solid solubility of the dopant at that temperature) by a gas or glass source. With boundary conditions C(0, t) = C_s, C(∞, t) = 0, C(x, 0) = 0:

    C(x, t) = C_s erfc( x / 2√(Dt) )

    Total dose  Q(t) = (2/√π) C_s √(Dt)   [atoms/cm²]

√(Dt) is the **diffusion length**; it sets the depth scale.

### Limited-source (drive-in) diffusion: Gaussian profile

A fixed dose Q is first deposited, the source is removed, and the wafer is heated to drive the dopant deeper:

    C(x, t) = ( Q / √(πDt) ) exp( −x² / 4Dt )

The surface concentration C_s = Q/√(πDt) **falls** with time while the total dose stays constant.

@fig figures/diffusion.svg | Normalised profiles. The erfc profile keeps its surface concentration fixed; the Gaussian has a fixed area (dose) and its surface value falls as it spreads.

### Junction depth

Diffusing into a substrate doped N_B of opposite type, the junction forms where C(x_j) = N_B:

    erfc:      x_j = 2√(Dt) · erfc⁻¹(N_B / C_s)
    Gaussian:  x_j = 2√(Dt) · √( ln( C_s / N_B ) )

## 6.4 The two-step process

1. **Predeposition** (≈ 900–1000 °C, short): constant source, shallow erfc profile, sets the dose.
2. **Drive-in** (≈ 1000–1200 °C, longer, often oxidising): limited source, Gaussian profile, sets the junction depth and lowers surface concentration.

Sources: solid (BN discs, P₂O₅ glass), liquid (POCl₃, BBr₃ bubbled with N₂) or gas (B₂H₆, PH₃). SiO₂ masks the diffusion, which is how patterned junctions are made.

---

## Exam questions solved

### Q14. What is semiconductor doping? Explain why doping is necessary in semiconductor device fabrication.

**Doping** is the intentional introduction of controlled, small quantities of specific impurity atoms into a pure (intrinsic) semiconductor to change its electrical properties. Group V donors (P, As, Sb) make silicon **n-type**; Group III acceptors (B, Al, Ga) make it **p-type**. Typical levels are 10¹⁴ to 10²⁰ cm⁻³.

**Why it is necessary:**

1. **Intrinsic conductivity is too low and uncontrolled.** Pure Si has only n_i ≈ 10¹⁰ cm⁻³ carriers, giving ρ = 1/(qn_i(μ_n + μ_p)) ≈ 3×10⁵ Ω·cm. Doping with 10¹⁶ cm⁻³ P raises n a million times, to ρ ≈ 0.5 Ω·cm.
2. **It sets the carrier type.** Devices depend on regions where electrons or holes dominate. Without n- and p-type regions there can be no p-n junction, no diode, no BJT and no MOSFET.
3. **Temperature stability.** In an extrinsic semiconductor the carrier density is fixed by N_D or N_A over a wide temperature range (the extrinsic region) instead of varying exponentially with T as n_i does.
4. **Device design.** Doping profiles set the built-in potential, depletion width, breakdown voltage, threshold voltage of MOSFETs, current gain of BJTs, sheet resistance of resistors and the quality of Ohmic contacts (heavily doped n⁺, p⁺ regions).
5. **Selective, local control.** Using masks, different areas of one chip can be given different doping, which is what makes integrated circuits possible.

### Q15. Differentiate between n-type and p-type semiconductors.

| Feature | n-type | p-type |
|---|---|---|
| Dopant added | Pentavalent (Group V): P, As, Sb | Trivalent (Group III): B, Al, Ga, In |
| Name of dopant | Donor | Acceptor |
| Effect of dopant | Donates a free electron to the conduction band | Accepts an electron, creating a hole in the valence band |
| Fixed ion left behind | Positive donor ion N_D⁺ | Negative acceptor ion N_A⁻ |
| Majority carriers | Electrons | Holes |
| Minority carriers | Holes | Electrons |
| Carrier densities | n ≈ N_D, p = n_i²/N_D | p ≈ N_A, n = n_i²/N_A |
| Impurity level | E_D just below E_c | E_A just above E_v |
| Fermi level | Above E_i, towards E_c | Below E_i, towards E_v |
| Conductivity | σ ≈ qN_Dμ_n | σ ≈ qN_Aμ_p |
| Hall coefficient | Negative | Positive |

Both remain electrically neutral overall: every free electron (or hole) is balanced by a fixed ion.

### Q16. Explain the difference between donor impurities and acceptor impurities, giving suitable examples.

**Donor impurities** have **one more** valence electron than the host atom they replace. In Si, Group V atoms such as **phosphorus, arsenic and antimony** have five valence electrons; four form covalent bonds with neighbouring Si atoms, and the fifth is bound only by about 0.04–0.05 eV. It is easily thermally released into the conduction band, leaving a positively charged, immobile donor ion. Donors introduce an energy level E_D just below the conduction band and make the material n-type.

**Acceptor impurities** have **one fewer** valence electron than the host. In Si, Group III atoms such as **boron, aluminium, gallium and indium** have three valence electrons and leave one bond incomplete. A nearby valence electron moves in with very little energy (≈ 0.045 eV for B), so the acceptor becomes a negative ion and a mobile hole is created in the valence band. Acceptors introduce a level E_A just above the valence band and make the material p-type.

| | Donor | Acceptor |
|---|---|---|
| Valence electrons (in Si) | 5 | 3 |
| Gives / takes | Gives an electron | Takes an electron (gives a hole) |
| Ionised charge | + | − |
| Level | Near E_c | Near E_v |
| Examples in Si | P, As, Sb | B, Al, Ga, In |
| Examples in GaAs | S, Se, Te (on As site); Si on Ga site | Zn, Be, Mg (on Ga site); C on As site |

### Q17. Describe the mechanism of dopant diffusion in a semiconductor.

Diffusion is the net movement of dopant atoms from a region of high concentration to one of low concentration, driven by random thermal jumps of the atoms in the lattice. At room temperature it is negligible; at 900–1200 °C (silicon) it is significant.

**Atomic mechanisms:**

1. **Vacancy (substitutional) diffusion.** Substitutional dopants (B, P, As, Sb) occupy lattice sites. A dopant can jump only when an adjacent lattice site is vacant. The rate depends on the vacancy concentration (which rises steeply with temperature) and the jump probability. High activation energy (≈ 3–4 eV), so D is small (10⁻¹⁵ to 10⁻¹² cm²/s).
2. **Interstitial diffusion.** Small atoms or those that do not bond into the lattice (Au, Cu, Fe, Na, Li, H) move between lattice sites through the open spaces of the diamond structure. Low activation energy (0.5–1.5 eV), so they diffuse many orders of magnitude faster. These are usually unwanted contaminants.
3. **Interstitialcy (kick-out) and dissociative mechanisms.** A dopant is pushed off its site by a silicon self-interstitial, travels interstitially, then returns to a substitutional site. This explains enhanced diffusion of B and P during oxidation (oxidation-enhanced diffusion).

**Temperature dependence.** D = D₀ exp(−E_a/kT), so D roughly doubles every 20–30 °C.

**Macroscopic description.** The flux obeys Fick's first law F = −D ∂C/∂x, and the profile evolves by Fick's second law ∂C/∂t = D ∂²C/∂x². In practice a two-step process is used: predeposition from a constant surface source (erfc profile) followed by drive-in of the fixed dose (Gaussian profile). Diffusion is masked by SiO₂ windows, and the dopant spreads sideways under the mask edge by about 0.8 of its depth (lateral diffusion).

### Q18. State and explain Fick's first and second laws of diffusion.

**Fick's first law.** The diffusion flux is proportional to the negative of the concentration gradient:

    F = −D ∂C/∂x

- F: number of atoms crossing unit area per unit time (cm⁻²s⁻¹).
- C(x, t): impurity concentration (cm⁻³).
- D: diffusion coefficient (cm²/s), D = D₀exp(−E_a/kT).
- The minus sign: atoms move from high to low concentration. If there is no gradient, there is no net flux.

It describes the flux at one instant but not how the profile changes.

**Fick's second law.** Consider a thin slice of thickness dx. Atoms entering minus atoms leaving equals the increase stored (continuity, no generation or loss):

    ∂C/∂t = −∂F/∂x

Substituting the first law (with D constant):

    ∂C/∂t = D ∂²C/∂x²

This is the diffusion equation. It says the concentration rises where the profile is curved upward (concave) and falls where it is curved downward, so diffusion always smooths the profile. Its solutions, set by the boundary conditions, are the complementary-error-function profile (constant surface source) and the Gaussian profile (fixed dose) described in §6.3.

### Q19. A semiconductor is doped by diffusion with a constant surface concentration of 1 × 10²⁰ cm⁻³. Explain how the impurity concentration varies with depth.

A constant surface concentration is the **predeposition** (unlimited source) case. Solve Fick's second law with:

- C(0, t) = C_s = 1×10²⁰ cm⁻³ (held fixed for all t)
- C(∞, t) = 0 (deep in the wafer)
- C(x, 0) = 0 (no dopant at the start)

The solution is the **complementary error function**:

    C(x, t) = C_s erfc( x / 2√(Dt) ) = 1×10²⁰ · erfc( x / 2√(Dt) )   cm⁻³

**How it varies with depth:**

1. At the surface (x = 0), erfc(0) = 1, so C = 1×10²⁰ cm⁻³, independent of time.
2. The concentration **decreases monotonically** with depth. Near the surface it falls almost linearly; deeper it falls faster than exponentially, because erfc(u) ≈ e^{−u²}/(u√π) for large u.
3. The depth scale is the diffusion length 2√(Dt). At x = 2√(Dt), erfc(1) = 0.157, so C = 1.57×10¹⁹ cm⁻³. At x = 4√(Dt), erfc(2) = 4.7×10⁻³, so C = 4.7×10¹⁷ cm⁻³.
4. As time increases, the profile penetrates deeper (as √t) while the surface stays at 10²⁰ cm⁻³, so the total dose grows: Q = (2/√π)C_s√(Dt).
5. If the wafer has background doping N_B of the opposite type, a junction forms where C(x_j) = N_B.

**Worked illustration** (assume boron into n-Si with N_B = 1×10¹⁶ cm⁻³, D = 1×10⁻¹³ cm²/s at about 1100 °C, t = 1 h = 3600 s):

    √(Dt) = √(1×10⁻¹³ × 3600) = 1.90×10⁻⁵ cm = 0.190 μm
    2√(Dt) = 0.379 μm

    Junction: erfc(u) = N_B/C_s = 10¹⁶/10²⁰ = 10⁻⁴  ⇒  u ≈ 2.75
    x_j = 2.75 × 0.379 μm ≈ 1.04 μm

    Dose: Q = (2/√π)(1×10²⁰)(1.90×10⁻⁵) = 2.14×10¹⁵ atoms/cm²

| Depth x (μm) | u = x/2√(Dt) | erfc(u) | C (cm⁻³) |
|---|---|---|---|
| 0 | 0 | 1 | 1.0×10²⁰ |
| 0.19 | 0.5 | 0.480 | 4.8×10¹⁹ |
| 0.38 | 1.0 | 0.157 | 1.6×10¹⁹ |
| 0.57 | 1.5 | 0.034 | 3.4×10¹⁸ |
| 0.76 | 2.0 | 4.7×10⁻³ | 4.7×10¹⁷ |
| 1.04 | 2.75 | 1.0×10⁻⁴ | 1.0×10¹⁶ (junction) |

So the impurity concentration is highest at the surface and falls off as an erfc curve, reaching the background doping about 1 μm below the surface for these conditions.
