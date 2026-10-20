# Week 3 — Impurity Control and Doping
<!-- group: Module 1 · Material Physics & Semiconductor Growth -->

**Plan:** diffusion and ion implantation mechanisms; controlled doping profiles and evaluation of impurity distribution.

Week 1 explained what donors and acceptors do. This week explains how they are put into the wafer, what profile they end up with, and how that profile is measured.

## Doping

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

## Part A: Thermal diffusion

## How dopants move: diffusion mechanisms

At high temperature (900–1200 °C for Si) atoms vibrate strongly and occasionally jump to a neighbouring site. Net movement goes from high to low concentration.

1. **Substitutional (vacancy) diffusion.** The dopant sits on a lattice site and can only move when a **vacancy** appears next to it; it then swaps into the vacancy. Slow, because it needs both a vacancy (formation energy) and a jump (migration energy): activation energy 3–4 eV. Main dopants B, P, As, Sb.
2. **Interstitial diffusion.** Small atoms squeeze between lattice sites without needing vacancies. Fast, activation energy 0.5–1.5 eV. Examples: Au, Cu, Fe, Li, H, Na. These metals are lifetime killers.
3. **Interstitialcy (kick-out) mechanism.** A Si self-interstitial pushes a substitutional dopant into an interstitial position, the dopant moves, then kicks a Si atom out. Important for B and P.

The diffusion coefficient follows an Arrhenius law:

    D = D₀ exp(−E_a / kT)

For B in Si: D₀ ≈ 0.76 cm²/s, E_a ≈ 3.46 eV, giving D ≈ 10⁻¹³ cm²/s at 1100 °C. A tiny change in T changes D a lot, so furnace temperature must be held to ±0.5 °C.

## Fick's laws

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

## The two-step process

1. **Predeposition** (≈ 900–1000 °C, short): constant source, shallow erfc profile, sets the dose.
2. **Drive-in** (≈ 1000–1200 °C, longer, often oxidising): limited source, Gaussian profile, sets the junction depth and lowers surface concentration.

Sources: solid (BN discs, P₂O₅ glass), liquid (POCl₃, BBr₃ bubbled with N₂) or gas (B₂H₆, PH₃). SiO₂ masks the diffusion, which is how patterned junctions are made.

## Part B: Ion implantation

## Principle

Dopant atoms are **ionised**, **accelerated** through a high voltage (typically 1 keV to several MeV) and **fired into** the wafer. The ions lose their energy by collisions with the lattice electrons (electronic stopping) and nuclei (nuclear stopping) and come to rest at some depth. A subsequent **anneal** repairs the damage and moves the dopants onto substitutional sites where they become electrically active.

## The implanter

1. **Ion source:** a gas such as BF₃, PH₃ or AsH₃ is ionised in a plasma (arc chamber).
2. **Extraction:** ions are pulled out by an extraction voltage (≈ 20–40 kV).
3. **Mass analyser:** a magnet bends the beam. Only ions with the selected mass-to-charge ratio pass through the slit, so the beam is isotopically pure (e.g. ¹¹B⁺ only).
4. **Acceleration tube:** raises the ions to the final energy.
5. **Scanning and focusing:** electrostatic or mechanical scanning spreads the beam uniformly over the wafer.
6. **Target chamber and dose measurement:** a **Faraday cup** collects the beam current, and integrating it gives the dose.

Dose (ions per cm²):

    Φ = (1/qA) ∫ I dt = I·t / (q·A)       (singly charged ions)

**Example.** Beam current 10 μA for 100 s over a 200 mm wafer (A = 314 cm²): Φ = (10×10⁻⁶ × 100)/(1.602×10⁻¹⁹ × 314) = 2.0×10¹³ ions/cm².

## The implanted profile

To first order the profile is **Gaussian**, centred at the **projected range** R_p with **straggle** (standard deviation) ΔR_p:

    N(x) = ( Φ / (√(2π) ΔR_p) ) · exp( −(x − R_p)² / 2ΔR_p² )

    Peak concentration  N_p = Φ / (√(2π) ΔR_p) ≈ 0.4 Φ / ΔR_p

R_p increases with ion energy and decreases with ion mass. Rough values in Si at 100 keV: B, R_p ≈ 0.30 μm; P, 0.12 μm; As, 0.06 μm.

**Example.** Φ = 1×10¹⁵ cm⁻² of As with ΔR_p = 0.02 μm = 2×10⁻⁶ cm gives N_p = 0.4 × 10¹⁵/2×10⁻⁶ = 2×10²⁰ cm⁻³.

@fig figures/implant.svg | An implanted profile peaks below the surface at the projected range R_p, unlike a diffused profile, which always peaks at the surface.

## Practical effects

- **Lattice damage.** Each heavy ion displaces thousands of Si atoms. High doses turn the surface **amorphous**.
- **Annealing** repairs damage and activates dopants: furnace anneal (900–1000 °C, 30 min) or **rapid thermal anneal** (RTA, ≈ 1000–1100 °C for a few seconds) which limits further diffusion. Laser and flash anneals use even shorter times.
- **Channelling.** Ions entering along a low-index direction (e.g. ⟨110⟩) travel down open "channels" in the crystal and go much deeper than predicted. Prevented by **tilting the wafer about 7°**, rotating it, implanting through a thin screen oxide, or pre-amorphising the surface.
- **Masking.** Photoresist, SiO₂, Si₃N₄ or polysilicon stops the ions where doping is not wanted. A thick enough mask is a few R_p + ΔR_p.
- **Self-aligned gates.** In a MOSFET the polysilicon gate itself masks the channel while the source and drain are implanted, which aligns them to the gate automatically.

## Part C: Evaluating the impurity distribution

Once a wafer has been doped, the process engineer must check that the dose, the profile and the junction depth are what was intended. The main methods:

| Method | What it measures | How |
|---|---|---|
| Four-point probe | Sheet resistance R_s (Ω/□) | Current through the outer two of four collinear probes, voltage across the inner two |
| Junction staining / groove-and-stain | Junction depth x_j | Bevel or groove the wafer, stain (e.g. HF + HNO₃ darkens p-type), measure under a microscope |
| Spreading resistance profiling (SRP) | Carrier concentration against depth | Step two probes down a shallow bevel, measuring resistance at each point |
| C-V profiling | Doping against depth | Capacitance of a junction or Schottky contact against reverse bias (Week 12) |
| Secondary-ion mass spectrometry (SIMS) | Total atomic concentration against depth (active or not) | Sputter the surface with an ion beam and mass-analyse the ejected ions |
| Hall measurement | Carrier type, concentration and mobility | Hall voltage in a magnetic field (Week 7) |

### Sheet resistance

For a doped layer of thickness (junction depth) x_j:

    R_s = ρ / x_j = 1 / ( q ∫₀^{x_j} μ(x) N(x) dx ) ≈ 1 / (q μ̄ Q)     [Ω/□]

where Q is the dose of active dopant per cm². A resistor of length L and width W made from the layer has R = R_s (L/W): the resistance depends only on the number of "squares".

Four-point probe on a large, thin sample (probe spacing s ≫ x_j):

    R_s = (π / ln 2) · V/I = 4.532 · V/I

**Example.** A boron predeposition gives V = 2.0 mV for I = 1.0 mA on a four-point probe. R_s = 4.532 × 2.0 = 9.06 Ω/□. If x_j = 1.0 μm, the average resistivity is ρ = R_s x_j = 9.06 × 10⁻⁴ = 9.1×10⁻⁴ Ω·cm, which (from Irvin's curves) corresponds to an average boron concentration of a few times 10¹⁹ cm⁻³.

### Junction depth from the profile

Measured x_j and R_s are compared with theory:

    erfc profile:     x_j = 2√(Dt) · erfc⁻¹(N_B/C_s)
    Gaussian profile: x_j = 2√(Dt) · √(ln(C_s/N_B))
    Implant:          x_j = R_p + ΔR_p √(2 ln(N_p/N_B))

**Irvin's curves** relate surface concentration, background doping and the average conductivity (1/R_sx_j) of erfc and Gaussian layers, so a measured R_s and x_j give C_s.

### Groove-and-stain junction depth

A cylindrical groove of radius R is ground into the surface and stained. If the widths of the stained chord at the surface and at the junction are a and b:

    x_j ≈ (a² − b²) / (8R)        (a, b ≪ R)

---

## Examination questions solved (Q14–Q21)

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

This is the diffusion equation. It says the concentration rises where the profile is curved upward (concave) and falls where it is curved downward, so diffusion always smooths the profile. Its solutions, set by the boundary conditions, are the complementary-error-function profile (constant surface source) and the Gaussian profile (fixed dose) described in Part A above.

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

### Q20. Explain the principle of ion implantation and identify its major advantages over thermal diffusion.

**Principle.** Ion implantation introduces dopant atoms into a semiconductor by bombarding it with a beam of energetic dopant ions. The dopant is ionised in an ion source, the ions are extracted, selected by mass in a magnetic analyser, accelerated to an energy of a few keV to MeV and scanned uniformly across the wafer. Each ion penetrates the crystal, losing energy by nuclear and electronic collisions, and stops at a depth that depends on its energy and mass. The resulting distribution is approximately Gaussian, peaking at the projected range R_p with straggle ΔR_p. The dose is measured exactly by integrating the beam current in a Faraday cup (Φ = It/qA). Because the impact damages the lattice and leaves dopants on non-lattice sites, the wafer is then annealed (furnace or RTA) to repair the damage and electrically activate the dopants.

**Advantages over thermal diffusion:**

1. **Precise, reproducible dose control** (±1 % or better) over a very wide range, 10¹¹ to 10¹⁶ cm⁻², by measuring charge. Diffusion dose depends on solid solubility, time and temperature and is much less accurate.
2. **Independent control of depth and dose.** Depth is set by energy, dose by charge. In diffusion both depend on the same Dt product.
3. **Low-temperature process.** Implantation is done near room temperature; only a short anneal is needed. Existing profiles are not disturbed and the thermal budget is small, which is vital for shallow junctions.
4. **Wide choice of masks**, including photoresist, which diffusion cannot use.
5. **Buried and retrograde profiles.** The peak can be placed below the surface (e.g. retrograde wells, buried layers); diffusion always peaks at the surface.
6. **Very shallow junctions** with low-energy implants.
7. **Less lateral spread** under the mask edge, allowing smaller devices and self-aligned structures.
8. **Purity.** Mass separation guarantees only the chosen species is implanted.
9. **Not limited by solid solubility**: concentrations above solubility can be obtained (though not all are activated).
10. **Uniformity** across large wafers, and the process is clean (vacuum, dry).

### Q21. Compare diffusion and ion implantation as semiconductor doping techniques.

| Feature | Thermal diffusion | Ion implantation |
|---|---|---|
| Principle | Dopant moves in from a surface source by random thermal jumps (Fick's laws) | Energetic ions are driven into the crystal and stop by collisions |
| Process temperature | High, 900–1200 °C | Room temperature, plus anneal (RTA ≈ 1000 °C for seconds) |
| Profile shape | erfc or Gaussian, always maximum at the surface | Gaussian peaking at R_p below the surface; buried and retrograde profiles possible |
| Dose control | Limited (± 5–10 %), set by solubility, T and t | Excellent (± 1 %), set by measured charge |
| Depth control | Coupled to dose through Dt | Independent: set by energy |
| Junction depth | Relatively deep; hard to make very shallow junctions | Very shallow junctions possible |
| Lateral spread | Large (≈ 0.8 × depth) | Small (≈ straggle) |
| Masking | SiO₂, Si₃N₄ (must survive high T) | Photoresist, oxide, nitride, polysilicon |
| Lattice damage | None | Significant; needs annealing; amorphisation at high dose |
| Channelling | Not applicable | Must be avoided (7° tilt, screen oxide) |
| Throughput and cost | Batch of 100+ wafers, cheap equipment | Single wafer or small batch, expensive equipment |
| Purity | Depends on source and furnace cleanliness | Mass-analysed, very pure |
| Concentration limit | Limited by solid solubility | Can exceed solubility |
| Typical use today | Drive-in, deep wells, solar cells, emitter diffusion in older processes | Source/drain, threshold-adjust, wells, LDD, channel stops in all modern CMOS |

**Summary:** diffusion is simple, cheap and damage-free but gives coarse, coupled control of dose and depth and needs high temperature. Ion implantation gives precise, independent, low-temperature control of dose and depth and is the standard technique for modern VLSI, at the cost of expensive equipment and lattice damage that must be annealed. In practice the two are often combined: implant to set the dose, then a thermal drive-in to set the depth.
