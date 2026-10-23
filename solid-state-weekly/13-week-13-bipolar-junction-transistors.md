# Week 13 — Bipolar Junction Transistors (BJTs)
<!-- group: Module 5 · Advanced Device Technology -->

**Plan:** operational physics; minority-carrier profiles in the active regions; emitter efficiency, base transport factor and current gains (α, β). This page follows your lecturer's Weeks 13–15 note (sections 13.1–13.13) and solves its review questions.

## Learning objectives

By the end of this week you should be able to:

1. Explain the structure and operating principle of NPN and PNP transistors.
2. Describe injection, diffusion, recombination and collection in the forward-active region.
3. Sketch and explain the minority-carrier profiles.
4. Define emitter injection efficiency and base transport factor.
5. Derive α and β and relate them to γ and α_T.
6. Solve problems on transistor currents and gains.

## Symbols and abbreviations used this week

Every symbol, constant and abbreviation on this page is listed here, even if an earlier week already defined it, so you can study this page on its own.

**Constants and units**

| Symbol | Meaning | Units / typical value |
|---|---|---|
| q | Magnitude of the electronic charge | 1.6×10⁻¹⁹ C |
| k | Boltzmann constant | 8.617×10⁻⁵ eV/K = 1.381×10⁻²³ J/K |
| kT | Thermal energy | 0.0259 eV (often 0.02585 eV) at 300 K |
| kT/q | Thermal voltage | 0.0259 V (about 26 mV) at 300 K |
| μm | Micrometre (micron) | 1 μm = 10⁻⁴ cm = 10⁻⁶ m |

**Symbols**

| Symbol | Meaning | Units / typical value |
|---|---|---|
| n_i | Intrinsic carrier concentration (n = p = n_i in pure material) | cm⁻³; Si ≈ 1×10¹⁰ at 300 K |
| p_n0, n_p0 | Equilibrium minority concentrations: holes on the n side, electrons on the p side | cm⁻³; p_n0 = n_i²/N_D |
| N_B (C_B) | Background doping of the wafer (in Week 13, N_B is the base doping) | cm⁻³ |
| μ, μ_n, μ_p | Mobility: drift velocity per unit field (electrons, holes) | cm²/(V·s); Si μ_n 1350, μ_p 480 |
| J, J_n, J_p | Current density (total, electrons, holes) | A/cm² |
| D_n, D_p | Diffusion coefficients of electrons and holes | cm²/s; Si 35 and 12.4 |
| τ, τ_n, τ_p | Minority-carrier lifetime (τ_eff: effective, including surfaces) | s; Si 1 ns – 1 ms |
| L, L_n, L_p | Diffusion length √(Dτ): distance a minority carrier travels before recombining | μm or cm |
| V, V_a | Applied voltage (positive for forward bias) | V |
| I_s, J_s (I_S) | Saturation current (density) of a diode or transistor | A; A/cm² |
| A (area) | Device or contact area | cm² |
| I_E, I_B, I_C | Emitter, base and collector currents | A (mA) |
| V_BE, V_CE, V_CB | Base–emitter, collector–emitter and collector–base voltages | V |
| α | Common-base current gain, I_C/I_E | dimensionless; 0.98–0.999 |
| β | Common-emitter current gain, I_C/I_B (also h_FE) | dimensionless; 50–500 |
| γ (BJT) | Emitter injection efficiency | dimensionless, close to 1 |
| α_T | Base transport factor | dimensionless, close to 1 |
| N_E, W_E, D_E; N_B, W_B, D_B | Doping, width and minority diffusion coefficient of the emitter; of the base | cm⁻³; μm; cm²/s |
| V_A | Early voltage | V |
| r_o | Output resistance | Ω |
| τ_B | Base transit time, W_B²/2D_n | s |
| f_T | Transition (cut-off) frequency | Hz |
| n_n0, p_p0, p_n0, n_p0 | Equilibrium densities: majority (n_n0, p_p0) and minority (p_n0 holes on n side, n_p0 electrons on p side) | cm⁻³ |
| I_{E,n}, I_{E,p}, I_{C,n} | Electron and hole parts of the emitter and collector currents | A |
| n_B(x) | Minority-electron density in the base of an NPN transistor | cm⁻³ |
| V_EB, V_BC (V_CB) | Emitter–base and base–collector voltages | V |
| ΔV, ΔV_BE | A small change in a voltage | V |
| I_{C1}, I_{C2} | Collector currents at two operating points | A |

**Abbreviations**

| Abbreviation | Meaning |
|---|---|
| Si | Silicon |
| CB | Conduction band |
| MOSFET | Metal–oxide–semiconductor field-effect transistor |
| BJT | Bipolar junction transistor |
| NPN | BJT with n-type emitter, p-type base, n-type collector |
| PNP | BJT with p-type emitter, n-type base, p-type collector |
| E–B | Emitter–base (junction) |
| C–B | Collector–base (junction) |
| n⁺ | Very heavily doped n-type (similarly p⁺) |


## Key terms

Every important word used this week is defined here, so you can read this week on its own.

**Doping (N_E, N_B).** Adding a small, controlled amount of impurity atoms to a semiconductor. Donors give electrons and make it n-type; acceptors create holes and make it p-type. In a transistor, N_E and N_B are the doping concentrations of the emitter and the base (atoms per cm³).

**Majority and minority carriers.** The more numerous carrier in a region is the majority carrier (electrons in n-type, holes in p-type); the less numerous one is the minority carrier. Electrons injected into a p-type base are minority carriers there.

*Why it matters:* the main current of a BJT is carried by minority carriers crossing the base.

**p-n junction and depletion region.** The boundary between a p-type and an n-type region. Around it lies a thin depletion region, emptied of mobile carriers and containing a strong electric field.

**Forward and reverse bias.** A junction is forward biased when the p side is made positive with respect to the n side: the barrier is lowered and carriers are injected across it. It is reverse biased when the p side is made negative: the barrier rises, almost no current flows, and the field sweeps across any minority carriers that reach the depletion edge.

**Diffusion.** The movement of carriers from where they are concentrated to where they are sparse, caused only by their random thermal motion. Its strength is measured by the diffusion coefficient D (cm²/s).

**Minority-carrier lifetime (τ_n, τ_p) and diffusion length (L_n, L_p).** The lifetime τ is the average time a minority carrier survives before it recombines with a majority carrier. The diffusion length is the average distance it diffuses in that time.

    L_n = √(D_n τ_n)

Where:

- L_n = electron diffusion length (cm)
- D_n = electron diffusion coefficient (cm²/s)
- τ_n = electron lifetime (s)

**Bipolar junction transistor (BJT).** A three-terminal device made of three alternately doped regions, emitter (E), base (B) and collector (C), forming two back-to-back p-n junctions. It is called bipolar because both electrons and holes carry current. It is built as NPN or PNP.

**Emitter, base and collector.** The emitter is the heavily doped region that injects carriers; the base is the thin, lightly doped middle region they cross; the collector is the moderately doped region that gathers them.

**Forward-active mode.** The normal amplifying condition: emitter–base junction forward biased, collector–base junction reverse biased. The collector current is then set by V_BE (or I_B) and hardly depends on the collector voltage.

**Emitter injection efficiency (γ).** The fraction of the emitter current that is carried by the useful carriers injected from the emitter into the base (electrons in an NPN), rather than by carriers injected backwards from the base into the emitter.

*Why it matters:* only the carriers injected into the base can reach the collector, so γ sets an upper limit on the gain.

**Base transport factor (α_T).** The fraction of the carriers injected into the base that cross it without recombining and reach the collector.

**Common-base current gain (α).** The ratio of collector current to emitter current, α = I_C/I_E. It is just below 1 (typically 0.98–0.999).

**Common-emitter current gain (β, h_FE).** The ratio of collector current to base current, β = I_C/I_B; typically 50–500.

    β = α / (1 − α)

Where:

- β = common-emitter current gain (dimensionless)
- α = common-base current gain (dimensionless)

*Why it matters:* because α is so close to 1, a tiny base current controls a collector current about β times larger, which is amplification.

**Saturation current of a transistor (I_S).** The scale factor in the collector-current law I_C = I_S e^{qV_BE/kT}. It is set by the base doping, base width and device area, and is typically 10⁻¹⁶–10⁻¹⁴ A.

**Early effect and Early voltage (V_A).** In the active mode, raising V_CE widens the collector depletion region into the base and makes the neutral base thinner, so I_C rises slightly. Extended backwards, the sloping output curves meet the V_CE axis at −V_A, the Early voltage.

**Output resistance (r_o).** The small-signal resistance seen looking into the collector, ΔV_CE/ΔI_C, approximately V_A/I_C. A large r_o means the transistor behaves like a good current source.

## The big picture

A transistor is a device in which a **small current or voltage controls a large current**. That is all amplification is.

In a BJT the trick is geometry. Two p-n junctions (Week 10) are built back to back, with a **very thin** middle layer. One junction pushes carriers into the thin layer; the other junction, a fraction of a micrometre away, pulls them out the other side. Because the middle layer is so thin, almost every carrier that goes in comes out at the far side. A small current into the middle layer (the base) is enough to keep this going, while a large current flows straight through. The physics is the minority-carrier diffusion you met in Weeks 7–9.

## 13.1 Introduction and BJT structure

A **bipolar junction transistor (BJT)** is a three-terminal semiconductor device in which **both electrons and holes** take part in current conduction. That is why it is called "bipolar". The three terminals are the **emitter (E)**, **base (B)** and **collector (C)**. A BJT contains two p-n junctions, arranged either as **NPN** or **PNP**.

| Region | Typical doping | Main function |
|---|---|---|
| Emitter | Heavily doped (n⁺ in an NPN) | Injects majority carriers into the base |
| Base | Lightly doped and very thin | Controls carrier transport and limits recombination |
| Collector | Moderately doped | Collects carriers and supports the voltage |

Why each choice?

- The **emitter is heavily doped** so that, when its junction is forward biased, it can inject a large concentration of carriers into the base, and so that the base injects very few carriers back into it.
- The **base is very thin** (often well under 1 μm) and lightly doped, so that most injected carriers cross it before they have time to recombine.
- The **collector is moderately doped** and physically larger, so that it can collect the carriers and withstand a relatively high reverse voltage without breaking down.

## 13.2 BJT biasing and operational physics

For normal **forward-active** operation of an NPN transistor:

- the **emitter–base junction is forward biased**;
- the **collector–base junction is reverse biased**.

What happens, step by step:

1. **Injection.** The forward-biased E–B junction lowers its barrier. Electrons flow from the n-type emitter into the p-type base. In the base they are **minority carriers**.
2. **Diffusion across the base.** There are many injected electrons at the emitter side of the base and almost none at the collector side, so they **diffuse** across. Because the base is thin, most of them get across.
3. **Recombination (a small loss).** A small fraction of the electrons meet holes in the base and recombine.
4. **Collection.** The electrons that reach the collector side are swept into the collector by the strong electric field of the reverse-biased C–B junction. They form most of the collector current.
5. **Base current.** The base current is mainly associated with (a) recombination in the base, which must be replaced by holes flowing in through the base lead, and (b) holes injected from the base into the emitter.

For a **PNP** transistor the carrier polarities are reversed: holes are injected from the p-type emitter into the n-type base and are collected by the p-type collector. All currents and voltages change sign.

| Feature | NPN | PNP |
|---|---|---|
| Layers (E–B–C) | n⁺ – p – n | p⁺ – n – p |
| Carriers injected into the base | Electrons (minority carriers in the p-type base) | Holes (minority carriers in the n-type base) |
| Main E-to-C current carried by | Electrons | Holes |
| Base current carried by | Holes (recombination and back-injection into the emitter) | Electrons |
| Forward-active bias | V_BE ≈ +0.7 V (base above emitter); V_CB > 0 | V_EB ≈ +0.7 V (emitter above base); V_BC > 0 |
| Conventional current | I_C and I_B flow in; I_E flows out of the emitter | I_E flows into the emitter; I_C and I_B flow out |
| Emitter arrow in the symbol | Points out | Points in |
| Speed and gain for the same size | Higher: electrons have the larger mobility and diffusion coefficient (D_n ≈ 35 against D_p ≈ 12.4 cm²/s in Si) | Lower |
| Typical use | Most amplifiers and switches; integrated circuits | Complementary (push–pull) stages with NPN, high-side switches, current sources and mirrors from the positive supply |

> **In plain words.** The emitter is a crowd pushing through a door (the forward-biased junction) into a narrow corridor (the base). At the other end of the corridor is a slide (the reverse-biased junction) that carries everyone who reaches it away. The corridor is so short that nearly everyone makes it. The base current is the small trickle of people who get lost in the corridor, plus a few who wander back the wrong way.

## 13.3 Minority-carrier concentration profiles

In a forward-active NPN transistor, electrons are minority carriers in the p-type base. Their concentration is **highest at the emitter side** of the base (because of injection) and **almost zero at the collector side** (because the collector removes them as fast as they arrive). In a thin, uniformly doped base with little recombination, the profile in between is approximately a **straight line**:

    n_B(x) ≈ n_B(0) − [ n_B(0) − n_B(W_B) ] x/W_B

| Symbol | Meaning |
|---|---|
| W_B | neutral base width |
| x | distance measured from the emitter side of the base |
| n_B(0) | minority-electron concentration at the emitter edge of the base, n_B(0) = n_p0 e^{qV_BE/kT} |
| n_B(W_B) | minority-electron concentration at the collector edge, ≈ 0 |

@fig figures/bjt-profile.svg | Minority carriers in an NPN transistor in the forward-active mode. Electrons in the base fall almost linearly from n_B(0) to about zero at the collector edge. Holes injected back into the emitter decay away from the junction.

The concentration gradient drives electron **diffusion** through the base. By Fick's law the electron diffusion current density is

    J_n = q D_n (dn/dx)

where q is the magnitude of the electronic charge and D_n the electron diffusion coefficient (the sign depends on the direction you take as positive). For the straight-line profile, dn/dx = −n_B(0)/W_B, so

    |J_n| = q D_n n_B(0) / W_B

Where:

- J_n = electron diffusion current density in the base (A/cm²)
- q = electronic charge, 1.6×10⁻¹⁹ C
- D_n = electron diffusion coefficient in the base (cm²/s)
- n_B(0) = electron concentration at the emitter edge of the base, n_p0 e^{qV_BE/kT} (cm⁻³)
- n_p0 = equilibrium electron concentration in the base, n_i²/N_B (cm⁻³)
- W_B = neutral base width (cm)

This is the collector current density. It is controlled by V_BE through n_B(0) = n_p0 e^{qV_BE/kT}, and it is larger for a thinner base.

At the collector–base junction, the electric field in the reverse-biased depletion region rapidly sweeps the carriers into the collector. Because the collector only has to collect whatever arrives, the collector current is **almost independent of the collector voltage** in the active region, provided the transistor stays away from breakdown and saturation. This is what makes the BJT behave like a current source.

## 13.4 Emitter injection efficiency γ

The emitter current is made of two parts:

- I_{E,n}: electrons injected from emitter into base (useful: these become the collector current);
- I_{E,p}: holes injected from base into emitter (wasted: they only add to base current).

**Emitter injection efficiency** γ (gamma) measures what fraction of the emitter current is the useful kind:

    γ = I_{E,n} / (I_{E,n} + I_{E,p})

Where:

- γ = emitter injection efficiency (dimensionless, just below 1)
- I_{E,n} = electron current injected from the emitter into the base (A)
- I_{E,p} = hole current injected from the base into the emitter (A)

A well-designed transistor has γ very close to 1. The electrons injected into the base are limited by the base doping, and the holes injected into the emitter by the emitter doping: the more heavily a side is doped, the fewer carriers the other side can inject into it. This gives

    γ ≈ 1 / [ 1 + (D_E N_B W_B) / (D_B N_E W_E) ]

Where:

- N_E, N_B = emitter and base doping concentrations (cm⁻³)
- W_E, W_B = neutral emitter and base widths (cm or μm; only their ratio matters)
- D_E = diffusion coefficient of the minority carriers in the emitter (holes in an NPN) (cm²/s)
- D_B = diffusion coefficient of the minority carriers in the base (electrons in an NPN) (cm²/s)

This form assumes both the emitter and the base are much thinner than their minority-carrier diffusion lengths. Making **N_E ≫ N_B** makes the fraction small and γ close to 1.

Factors that improve emitter efficiency:

- heavy emitter doping relative to base doping;
- appropriate semiconductor material and junction design (for example a wider-gap emitter in a heterojunction transistor);
- proper control of emitter and base widths;
- minimising unwanted carrier injection.

## 13.5 Base transport factor α_T

Of the electrons injected into the base, a few recombine before reaching the collector. The **base transport factor** α_T is the fraction that make it:

    α_T = I_{C,n} / I_{E,n}

Where:

- α_T = base transport factor (dimensionless, just below 1)
- I_{C,n} = electron current reaching the collector (A)
- I_{E,n} = electron current injected into the base by the emitter (A)

If recombination in the base is negligible, α_T approaches 1. If the base is thick, or the minority-carrier lifetime is short, more carriers recombine and α_T falls. Quantitatively,

    α_T ≈ 1 − W_B² / (2L_n²),     L_n = √(D_n τ_n)

Where:

- W_B = neutral base width (cm)
- L_n = diffusion length of electrons in the base (cm)
- D_n = electron diffusion coefficient in the base (cm²/s)
- τ_n = electron lifetime in the base (s)

The transport factor depends on base width W_B, the minority-carrier diffusion coefficient D_n and the minority-carrier lifetime τ_n. **A thin base and a long lifetime give α_T close to one.** For example W_B = 1 μm and L_n = 20 μm give α_T = 1 − 1/800 = 0.99875.

## 13.6 Common-base current gain α

The **common-base current gain** is the ratio of collector current to emitter current:

    α = I_C / I_E

Where:

- α = common-base current gain (dimensionless)
- I_C = collector current (A)
- I_E = emitter current (A)

The collector current is slightly less than the emitter current (a little is lost to the base), so α is always less than 1, but for a good transistor it is very close to 1, typically **0.98–0.999**.

Physically, a current must survive two losses to get from emitter to collector: it must be the right kind of carrier (γ) and it must survive the trip (α_T). So

    α ≈ γ α_T

Where:

- α = common-base current gain
- γ = emitter injection efficiency
- α_T = base transport factor (all dimensionless)

#### Example 13.1: α from γ and α_T

**Question.** A transistor has an emitter injection efficiency of 0.995 and a base transport factor of 0.990. Estimate its common-base current gain.

**Given:** γ = 0.995, α_T = 0.990.

**Find:** α.

**Formula:**

    α ≈ γα_T

**Solution.**

    α ≈ γα_T = 0.995 × 0.990 = 0.98505

**Answer:** **α ≈ 0.985.**

**What this means:** about 1.5 % of the emitter current never reaches the collector: 0.5 % is lost as holes injected back into the emitter and about 1 % as electrons that recombine in the base. That missing 1.5 % is the base current.

## 13.7 Common-emitter current gain β

The **common-emitter current gain** β (also called h_FE under specified conditions) is the ratio of collector current to base current:

    β = I_C / I_B

Where:

- β = common-emitter current gain (dimensionless)
- I_C = collector current (A)
- I_B = base current (A)

**Deriving the relation between α and β.** Kirchhoff's current law at the transistor: everything that enters at the emitter leaves at the collector or the base,

    I_E = I_C + I_B

Start from α:

    α = I_C/I_E = I_C/(I_C + I_B)

Divide top and bottom by I_B, and use β = I_C/I_B:

    α = (I_C/I_B) / (I_C/I_B + 1) = β/(β + 1)

Solve for β: α(β + 1) = β ⇒ αβ + α = β ⇒ α = β(1 − α) ⇒

    β = α / (1 − α)

Where:

- β = common-emitter current gain, I_C/I_B (dimensionless)
- α = common-base current gain, I_C/I_E (dimensionless)

Because α is close to 1, the denominator 1 − α is a small number, so **a small change in α produces a large change in β**:

| α | 0.98 | 0.99 | 0.995 | 0.999 |
|---|---|---|---|---|
| β = α/(1 − α) | 49 | 99 | 199 | 999 |

#### Example 13.2: γ, α_T, α and β of a PNP transistor from its design

**Question.** A silicon p⁺np transistor has emitter doping N_E = 5×10¹⁸ cm⁻³ and base doping N_B = 1×10¹⁷ cm⁻³. The neutral emitter is 0.5 μm wide and the neutral base 0.8 μm. The electron diffusion coefficient in the emitter is 5 cm²/s, the hole diffusion coefficient in the base is 8 cm²/s, and the hole lifetime in the base is 0.5 μs. Find γ, α_T, α and β, and say which factor limits the gain.

**Given:** N_E = 5×10¹⁸ cm⁻³, N_B = 10¹⁷ cm⁻³, W_E = 0.5 μm, W_B = 0.8 μm = 8×10⁻⁵ cm, D_E = 5 cm²/s (electrons in the emitter), D_B = 8 cm²/s (holes in the base), τ_p = 0.5×10⁻⁶ s.

**Find:** γ, α_T, α, β.

**Formula:** the same as for an NPN, with the roles of electrons and holes swapped (the base minority carriers are now holes, so L_p replaces L_n):

    γ ≈ 1/[1 + (D_E N_B W_B)/(D_B N_E W_E)],     α_T ≈ 1 − W_B²/(2L_p²),     L_p = √(D_B τ_p)

    α ≈ γα_T,     β = α/(1 − α)

**Solution.**

Step 1. Emitter injection efficiency:

    (D_E N_B W_B)/(D_B N_E W_E) = (5 × 10¹⁷ × 0.8)/(8 × 5×10¹⁸ × 0.5) = 4×10¹⁷/2×10¹⁹ = 0.020
    γ = 1/1.020 = 0.9804

Step 2. Diffusion length and base transport factor:

    L_p = √(8 × 0.5×10⁻⁶) = 2.0×10⁻³ cm = 20 μm
    α_T = 1 − (0.8)²/(2 × 20²) = 1 − 0.64/800 = 0.9992

Step 3. Current gains:

    α = 0.9804 × 0.9992 = 0.9796
    β = 0.9796/(1 − 0.9796) = 0.9796/0.0204 ≈ 48

**Answer:** **γ = 0.980, α_T = 0.9992, α = 0.980, β ≈ 48.** The emitter injection efficiency limits the gain.

**What this means:** only 0.08 % of the holes are lost by recombination in the base, but 2 % of the emitter current is electrons injected backwards into the emitter, because the emitter is only 50 times more heavily doped than the base and is thin. Doping the emitter more heavily (or using a wider-band-gap emitter) would raise β far more than making the base thinner.

## 13.8 BJT current relationships

| Quantity | Expression | Meaning |
|---|---|---|
| Emitter current | I_E = I_C + I_B | Total transistor current at the emitter |
| Common-base gain | α = I_C/I_E | Collector current relative to emitter current |
| Common-emitter gain | β = I_C/I_B | Collector current relative to base current |
| Relation | β = α/(1 − α) | Converts α to β |
| Relation | α = β/(β + 1) | Converts β to α |
| Physics of α | α ≈ γα_T | Injection efficiency × transport factor |
| Collector current | I_C = I_S e^{qV_BE/kT} | Set by the base–emitter voltage |

The last line comes from multiplying the diffusion current density of section 13.3 by the emitter area, using n_B(0) = n_p0 e^{qV_BE/kT} and n_p0 = n_i²/N_B:

    I_C = I_S e^{qV_BE/kT},     I_S = q A D_B n_i² / (N_B W_B)

Where:

- I_C = collector current (A)
- I_S = saturation current of the transistor (A)
- V_BE = base–emitter voltage (V); kT/q = 0.0259 V at 300 K
- A = emitter (junction) area (cm²)
- D_B = minority-carrier diffusion coefficient in the base (cm²/s)
- n_i = intrinsic carrier concentration, 1×10¹⁰ cm⁻³ for Si
- N_B = base doping (cm⁻³); W_B = neutral base width (cm)

Because I_C depends exponentially on V_BE, every increase of (kT/q) ln 10 ≈ 60 mV in V_BE multiplies I_C by 10.

#### Example 13.3: collector and base currents from I_S and V_BE

**Question.** An NPN transistor has I_S = 5×10⁻¹⁶ A and β = 150. At V_BE = 0.68 V (300 K), find I_C, I_B and I_E. By how much must V_BE rise to increase I_C tenfold?

**Given:** I_S = 5×10⁻¹⁶ A, β = 150, V_BE = 0.68 V, kT/q = 0.0259 V.

**Find:** I_C, I_B, I_E and ΔV_BE for a ×10 change in I_C.

**Formula:**

    I_C = I_S e^{qV_BE/kT},     I_B = I_C/β,     I_E = I_C + I_B,     ΔV_BE = (kT/q) ln(I_{C2}/I_{C1})

**Solution.**

Step 1. Collector current:

    qV_BE/kT = 0.68/0.0259 = 26.25,   e^{26.25} = 2.53×10¹¹
    I_C = 5×10⁻¹⁶ × 2.53×10¹¹ = 1.26×10⁻⁴ A = 0.126 mA

Step 2. Base and emitter currents:

    I_B = 0.126 mA / 150 = 0.84 μA
    I_E = 0.126 + 0.00084 = 0.127 mA

Step 3. Voltage for a tenfold increase:

    ΔV_BE = 0.0259 × ln 10 = 0.0596 V ≈ 60 mV

**Answer:** **I_C ≈ 0.126 mA, I_B ≈ 0.84 μA, I_E ≈ 0.127 mA; V_BE must rise by about 60 mV (to 0.74 V) for 1.26 mA.**

**What this means:** the transistor is a very sensitive voltage-controlled device: a sub-microamp base current and a change of only 60 mV at the input change the output current by a factor of ten. This is why V_BE stays near 0.6–0.7 V over a wide range of collector currents.

## 13.9 Worked example 1: finding α

**Question.** A BJT has an emitter current of 5 mA and a collector current of 4.9 mA. Determine α and the base current.

**Given:** I_E = 5 mA, I_C = 4.9 mA.

**Find:** α and I_B.

**Formula:**

    α = I_C/I_E,     I_B = I_E − I_C

**Solution.**

    α = I_C/I_E = 4.9/5 = 0.98
    I_B = I_E − I_C = 5 − 4.9 = 0.1 mA

**Answer:** **α = 0.98, I_B = 0.1 mA.** (And β = 4.9/0.1 = 49.)

**What this means:** 98 % of the emitter current reaches the collector; the 2 % that flows out of the base lead is the "control" current, and 0.1 mA of it governs 4.9 mA of output.

## 13.10 Worked example 2: finding β from α

**Question.** A transistor has α = 0.98. Determine β. If the base current is 0.2 mA, determine the collector and emitter currents.

**Given:** α = 0.98, I_B = 0.2 mA.

**Find:** β, I_C, I_E.

**Formula:**

    β = α/(1 − α),     I_C = βI_B,     I_E = I_C + I_B

**Solution.**

    β = α/(1 − α) = 0.98/0.02 = 49
    I_C = βI_B = 49 × 0.2 mA = 9.8 mA
    I_E = I_C + I_B = 9.8 + 0.2 = 10.0 mA

**Answer:** **β = 49, I_C = 9.8 mA, I_E = 10 mA.**

**What this means:** in the common-emitter connection the 0.2 mA base current is amplified 49 times; a modest α of 0.98 already gives useful current gain.

## 13.11 Worked example 3: injection efficiency and transport factor

**Question.** An NPN transistor has emitter injection efficiency γ = 0.995 and base transport factor α_T = 0.990. Estimate α and β.

**Given:** γ = 0.995, α_T = 0.990.

**Find:** α and β.

**Formula:**

    α ≈ γα_T,     β = α/(1 − α)

**Solution.**

    α ≈ γα_T = 0.995 × 0.990 = 0.98505
    β = α/(1 − α) = 0.98505/0.01495 ≈ 65.9

**Answer:** **α ≈ 0.985, β ≈ 65.9.**

**What this means:** neither loss is large on its own (0.5 % and 1 %), yet together they hold β down to 66, because β depends on how small 1 − α is.

## Worked example 4: from device design to gain

**Question.** An NPN silicon transistor has N_E = 10¹⁹ cm⁻³, N_B = 10¹⁷ cm⁻³, W_E = 1 μm, W_B = 0.5 μm, D_E (holes in the emitter) = 2.5 cm²/s, D_B (electrons in the base) = 25 cm²/s, base lifetime τ_n = 1 μs and area 10⁻⁴ cm². Calculate the emitter injection efficiency γ, the base transport factor α_T, the current gains α and β, and the collector and base currents at V_BE = 0.65 V.

**Given:** the dopings, widths, diffusion coefficients and lifetime above; n_i = 10¹⁰ cm⁻³, kT/q = 0.0259 V.

**Find:** γ, α_T, α, β, I_C and I_B.

**Formula:**

    γ ≈ 1/[1 + (D_E N_B W_B)/(D_B N_E W_E)],     α_T ≈ 1 − W_B²/(2L_n²),     L_n = √(D_B τ_n)

    α ≈ γα_T,   β = α/(1 − α),   I_S = qAD_Bn_i²/(N_{B}W_B),   I_C = I_S e^{qV_BE/kT},   I_B = I_C/β

**Solution.**

    γ = 1 / [1 + (2.5 × 10¹⁷ × 0.5)/(25 × 10¹⁹ × 1)] = 1/(1 + 5×10⁻⁴) = 0.99950
    L_n = √(25 × 10⁻⁶) = 5×10⁻³ cm = 50 μm
    α_T = 1 − 0.5²/(2 × 50²) = 1 − 5×10⁻⁵ = 0.99995
    α = γα_T = 0.99945,   β = 0.99945/0.00055 ≈ 1800

    I_S = qAD_Bn_i²/(N_{B}W_B) = (1.6×10⁻¹⁹)(10⁻⁴)(25)(10²⁰)/(10¹⁷ × 5×10⁻⁵) = 8×10⁻¹⁵ A
    I_C = 8×10⁻¹⁵ × e^{0.65/0.0259} = 8×10⁻¹⁵ × 7.9×10¹⁰ = 0.63 mA,   I_B = I_C/β ≈ 0.35 μA

**Answer:** **γ = 0.9995, α_T = 0.99995, α = 0.99945, β ≈ 1800; I_C ≈ 0.63 mA and I_B ≈ 0.35 μA at V_BE = 0.65 V.**

**What this means:** here the emitter efficiency limits β: the back-injection loss (5×10⁻⁴) is ten times the recombination loss in the base (5×10⁻⁵). Real devices have lower β (typically 100–300) because of recombination in the E–B depletion region and other non-ideal effects.

## 13.12 BJT operating regions

| Region | Emitter–base junction | Collector–base junction | Typical use |
|---|---|---|---|
| Cut-off | Reverse biased | Reverse biased | OFF (switching) |
| Forward active | Forward biased | Reverse biased | Amplification |
| Saturation | Forward biased | Forward biased | ON (switching) |
| Reverse active | Reverse biased | Forward biased | Limited, reverse operation |

- **Cut-off:** no injection, so essentially no current flows: an open switch.
- **Forward active:** I_C = βI_B, controlled by the base: an amplifier.
- **Saturation:** both junctions inject; the collector can no longer collect everything independently, I_C < βI_B, and V_CE is small (about 0.2 V): a closed switch.
- **Reverse active:** emitter and collector swap roles; gain is poor because the collector was not designed to inject.

**Early effect.** In the active region, increasing V_CE widens the collector depletion region slightly into the base, making W_B smaller. A thinner base means a steeper profile and a larger I_C, so the output curves slope upward slightly. Extrapolated backwards they meet at −V_A, the **Early voltage**.

In the active region this is described by

    I_C = I_S e^{qV_BE/kT} (1 + V_CE/V_A),     r_o = ΔV_CE/ΔI_C ≈ V_A/I_C

Where:

- I_C = collector current (A); I_S = saturation current (A)
- V_BE = base–emitter voltage (V); kT/q = 0.0259 V at 300 K
- V_CE = collector–emitter voltage (V)
- V_A = Early voltage, typically 50–200 V (V)
- r_o = small-signal output resistance (Ω)

A large V_A (flat output curves) means a high output resistance, so the transistor is a better current source and an amplifier stage can have a higher voltage gain. A lightly doped base, which the collector depletion region can push into easily, gives a smaller V_A.

#### Example 13.4: Early voltage and output resistance from the output curve

**Question.** With the base current held constant, an NPN transistor carries I_C = 2.00 mA at V_CE = 2 V and I_C = 2.10 mA at V_CE = 7 V. Find its output resistance and Early voltage, and predict I_C at V_CE = 12 V.

**Given:** I_C = 2.00 mA at 2 V, 2.10 mA at 7 V, same base drive.

**Find:** r_o, V_A and I_C at 12 V.

**Formula:**

    r_o = ΔV_CE/ΔI_C,     V_A = I_C/(slope) − V_CE  (the extrapolated line meets I_C = 0 at V_CE = −V_A)

**Solution.**

Step 1. Slope of the output curve and output resistance:

    slope = ΔI_C/ΔV_CE = (2.10 − 2.00) mA / (7 − 2) V = 0.02 mA/V
    r_o = 1/slope = 1/(2×10⁻⁵ A/V) = 50 kΩ

Step 2. Extrapolate the straight line back to I_C = 0:

    I_C = 2.00 mA + 0.02 mA/V × (V_CE − 2 V) = 0   ⇒   V_CE = 2 − 100 = −98 V
    V_A = 98 V

Step 3. Current at 12 V (same straight line):

    I_C(12 V) = 2.00 + 0.02 × (12 − 2) = 2.20 mA

Check: V_A/I_C = 98 V / 2 mA = 49 kΩ, close to the measured r_o (the small difference is because the exact relation is r_o = (V_A + V_CE)/I_C).

**Answer:** **r_o = 50 kΩ, V_A ≈ 98 V, I_C ≈ 2.20 mA at 12 V.**

**What this means:** raising V_CE sixfold, from 2 V to 12 V, raises I_C by only 10 %, so the collector behaves almost like an ideal current source. The finite 50 kΩ output resistance is what limits the voltage gain of a single-transistor amplifier.

## 13.13 Summary of Week 13

- A BJT uses two p-n junctions and three semiconductor regions (emitter, base, collector).
- In forward-active operation the E–B junction is forward biased and the C–B junction reverse biased.
- The thin base lets most injected minority carriers reach the collector; their profile across the base is nearly a straight line.
- Emitter injection efficiency γ measures the desired carrier injection relative to the total emitter current.
- Base transport factor α_T measures the fraction of injected carriers that cross the base without recombining.
- α = I_C/I_E ≈ γα_T is the common-base gain; β = I_C/I_B is the common-emitter gain.
- The key relationship is **β = α/(1 − α)**.

---

## Review questions, Week 13, solved

### 1. Define a BJT and explain why it is called a bipolar device.

A bipolar junction transistor is a three-terminal semiconductor device consisting of two p-n junctions formed by three alternately doped regions, emitter, base and collector, arranged as NPN or PNP. A small base current (or base–emitter voltage) controls a much larger collector current, so it can amplify and switch. It is called **bipolar** because current is carried by both kinds of carrier: in an NPN, electrons carry the main emitter-to-collector current while holes carry the base current (recombination in the base and injection into the emitter). In contrast, a MOSFET is unipolar: its channel current is carried by one carrier type only.

### 2. Draw and label an NPN transistor and indicate the direction of conventional current and electron flow.

Draw three blocks side by side: **n⁺ emitter | p base | n collector**, with terminal leads E, B and C. Mark the E–B junction "forward biased" (base positive with respect to emitter, V_BE ≈ 0.7 V) and the C–B junction "reverse biased" (collector positive with respect to base).

- **Electron flow:** from the emitter, through the thin base, into the collector (left to right). A small number recombine with holes in the base; the holes they use up flow in through the base lead.
- **Conventional current:** opposite to electron flow. I_C flows **into** the collector, I_B flows **into** the base, and I_E = I_C + I_B flows **out of** the emitter. In the circuit symbol, the arrow on the emitter points **outwards** for an NPN, showing the direction of conventional emitter current.

### 3. Explain the operation of a BJT in the forward-active region.

With the E–B junction forward biased, the emitter barrier is lowered and the heavily doped n⁺ emitter injects a large number of electrons into the p-type base, where they become minority carriers with concentration n_B(0) = n_p0e^{qV_BE/kT} at the emitter edge. The reverse-biased collector holds the electron concentration at the collector edge of the base at almost zero. The resulting nearly linear concentration gradient makes the electrons diffuse across the thin base. Since the base is much thinner than the diffusion length, only a small fraction recombine. On reaching the C–B depletion region, the electrons are swept into the collector by its electric field, forming the collector current I_C = αI_E. The base supplies holes to replace those lost in recombination and those injected into the emitter, which is the small base current I_B = I_C/β. Because I_C depends on V_BE but hardly on V_CB, the transistor acts as a controlled current source, which allows amplification.

### 4. What is emitter injection efficiency? Why should it be close to unity?

Emitter injection efficiency γ = I_{E,n}/(I_{E,n} + I_{E,p}) is the fraction of the emitter current carried by carriers injected from the emitter into the base (electrons in an NPN), rather than by carriers injected from the base back into the emitter (holes). It should be close to unity because only the injected electrons can reach the collector and form useful output current; the back-injected holes simply add to the base current without contributing to I_C. Since α ≈ γα_T and β = α/(1 − α), even a small reduction of γ below 1 sharply reduces the current gain. γ is made close to 1 by doping the emitter much more heavily than the base.

### 5. Define the base transport factor and state two factors that affect it.

The base transport factor α_T = I_{C,n}/I_{E,n} is the fraction of minority carriers injected into the base that cross it without recombining and reach the collector. It is approximately α_T ≈ 1 − W_B²/(2L_n²). Factors that affect it (any two):

1. **Base width W_B**: a thinner base gives fewer recombinations and a higher α_T.
2. **Minority-carrier lifetime τ_n** in the base: a longer lifetime (fewer traps, cleaner material) increases L_n and α_T.
3. **Minority-carrier diffusion coefficient D_n**: faster diffusion means less time in the base and higher α_T.
4. **Base doping**: heavier doping shortens lifetime and lowers mobility, reducing α_T.

### 6. Derive β = α/(1 − α) from the definitions of α and β.

Definitions: α = I_C/I_E and β = I_C/I_B. By Kirchhoff's current law, I_E = I_C + I_B.

    α = I_C/I_E = I_C/(I_C + I_B)

Dividing numerator and denominator by I_B:

    α = (I_C/I_B)/(I_C/I_B + 1) = β/(β + 1)

Rearranging: α(β + 1) = β ⇒ αβ + α = β ⇒ α = β − αβ = β(1 − α), so

    β = α/(1 − α)

### 7. A transistor has I_E = 12 mA and I_C = 11.76 mA. Calculate α, I_B and β.

**Question.** A transistor has I_E = 12 mA and I_C = 11.76 mA. Calculate α, I_B and β.

**Given:** I_E = 12 mA, I_C = 11.76 mA.

**Find:** α, I_B, β.

**Formula:**

    α = I_C/I_E,     I_B = I_E − I_C,     β = I_C/I_B

**Solution.**

    α = I_C/I_E = 11.76/12 = 0.98
    I_B = I_E − I_C = 12 − 11.76 = 0.24 mA
    β = I_C/I_B = 11.76/0.24 = 49

Check: α/(1 − α) = 0.98/0.02 = 49. ✓

**Answer:** **α = 0.98, I_B = 0.24 mA, β = 49.**

**What this means:** a base current of a quarter of a milliamp controls almost 12 mA; any two of the three currents fix the third, and α and β always satisfy β = α/(1 − α).

### 8. Explain the difference between cut-off, active and saturation regions.

| | Cut-off | Forward active | Saturation |
|---|---|---|---|
| E–B junction | Reverse (or zero) biased | Forward biased | Forward biased |
| C–B junction | Reverse biased | Reverse biased | Forward biased |
| Currents | I_B ≈ 0, I_C ≈ 0 (leakage only) | I_C = βI_B | I_C < βI_B; I_C set by the external circuit |
| V_CE | Large (≈ supply voltage) | Intermediate | Small, V_CE(sat) ≈ 0.1–0.3 V |
| Behaves as | Open switch (OFF) | Current-controlled current source | Closed switch (ON) |
| Use | Digital OFF state | Amplifiers | Digital ON state |

In cut-off there is no injection, so no carriers cross the base. In the active region the collector collects all carriers that arrive, independently of its voltage. In saturation the collector junction is also forward biased and starts injecting carriers back into the base, so the collector current can no longer rise with base current; the transistor is fully ON.

---

## Practice questions

These extra questions practise this week's ideas. Work each one on paper before reading the solution; the calculation questions follow the same Question, Given, Find, Solution, Answer layout as the worked examples.

#### Practice 13.1: currents from β

**Question.** A transistor has β = 80 and I_C = 4 mA. Find I_B, I_E and α.

**Given:** β = 80, I_C = 4 mA.

**Find:** I_B, I_E, α.

**Solution.**

    I_B = I_C/β = 4/80 = 0.05 mA = 50 μA
    I_E = I_C + I_B = 4.05 mA
    α = β/(β + 1) = 80/81 = 0.988

**Answer:** **I_B = 50 μA, I_E = 4.05 mA, α = 0.988.**

#### Practice 13.2: from doping to gain

**Question.** An NPN transistor has N_E = 5×10¹⁸ cm⁻³, N_B = 5×10¹⁶ cm⁻³, equal emitter and base widths, D_E = 3 cm²/s and D_B = 20 cm²/s. Its base transport factor is 0.995. Find γ, α and β.

**Given:** N_E, N_B, D_E, D_B above, W_E = W_B, α_T = 0.995.

**Find:** γ, α, β.

**Solution.**

    D_{E}N_{B}W_B/(D_{B}N_{E}W_E) = (3 × 5×10¹⁶)/(20 × 5×10¹⁸) = 1.5×10⁻³
    γ = 1/(1 + 1.5×10⁻³) = 0.9985
    α = γα_T = 0.9985 × 0.995 = 0.9935
    β = α/(1 − α) = 0.9935/0.0065 = 153

**Answer:** **γ = 0.9985, α = 0.9935, β ≈ 153.**

**What this means:** the recombination loss in the base (0.5 %) is more than three times the back-injection loss (0.15 %), so here a thinner base or a longer lifetime would raise β most.

#### Practice 13.3: base transport factor

**Question.** A BJT has a base width of 1 μm and an electron diffusion length in the base of 10 μm. Find α_T. What base width would give α_T = 0.999?

**Given:** W_B = 1 μm, L_n = 10 μm.

**Find:** α_T, and W_B for α_T = 0.999.

**Solution.**

    α_T = 1 − W_B²/(2L_n²) = 1 − 1/(2 × 100) = 0.995
    For 0.999: W_B²/(2L_n²) = 0.001  ⇒  W_B = L_n√0.002 = 10 × 0.0447 = 0.45 μm

**Answer:** **α_T = 0.995; a 0.45 μm base gives 0.999.**

#### Practice 13.4: collector current and V_BE

**Question.** A transistor has I_S = 1×10⁻¹⁵ A. Find I_C at V_BE = 0.70 V, and the V_BE needed for I_C = 5 mA.

**Given:** I_S = 10⁻¹⁵ A, kT/q = 0.0259 V.

**Find:** I_C(0.70 V) and V_BE(5 mA).

**Solution.**

    I_C = I_S e^{V_BE/0.0259} = 10⁻¹⁵ × e^{27.03} = 10⁻¹⁵ × 5.5×10¹¹ = 0.55 mA
    V_BE = 0.0259 ln(5×10⁻³/10⁻¹⁵) = 0.0259 × 29.24 = 0.757 V

**Answer:** **I_C = 0.55 mA at 0.70 V; V_BE = 0.76 V for 5 mA.**

**What this means:** a ninefold rise in current needs only about 57 mV more on the base, the familiar 60 mV per decade of a BJT.

#### Practice 13.5: the Early effect

**Question.** A transistor has an Early voltage of 100 V and I_C = 1 mA at V_CE = 5 V. Find its output resistance and I_C at V_CE = 10 V (same base drive).

**Given:** V_A = 100 V, I_C(5 V) = 1 mA.

**Find:** r_o and I_C(10 V).

**Solution.**

    r_o = V_A/I_C = 100/10⁻³ = 100 kΩ
    I_C(10 V) = I_C(5 V) × (1 + 10/100)/(1 + 5/100) = 1 × 1.10/1.05 = 1.048 mA

**Answer:** **r_o = 100 kΩ; I_C rises to 1.05 mA.**

#### Practice 13.6: base transit time

**Question.** An NPN transistor has a 0.2 μm base and D_n = 20 cm²/s. Find the base transit time and the upper limit it places on f_T.

**Given:** W_B = 2×10⁻⁵ cm, D_n = 20 cm²/s.

**Find:** τ_B and f_T.

**Solution.**

    τ_B = W_B²/(2D_n) = (2×10⁻⁵)²/40 = 1×10⁻¹¹ s
    f_T ≲ 1/(2πτ_B) = 1.6×10¹⁰ Hz

**Answer:** **τ_B = 10 ps, f_T up to about 16 GHz.** Thin bases make fast transistors.

#### Practice 13.7: why the reverse-active gain is poor

**Question.** Explain why a BJT has a much lower current gain in the reverse-active mode.

**Answer.** In reverse-active mode the collector acts as the emitter. But the collector is only moderately (lightly) doped and much larger, while the base is more heavily doped than it. The injection efficiency is therefore poor (the base injects many holes back into the collector), and the collector-side geometry collects carriers badly. The result is a reverse β of typically only 1–5.

---

## Objectives check

Use this table to confirm you have met this week's objectives. Cover the Answer column and answer each check question from memory. If you cannot, go back to the section in the last column before moving on.

| # | Objective | Check yourself | Answer | Where it is taught |
|---|---|---|---|---|
| 1 | Explain the structure and operating principle of NPN and PNP transistors. | Why is the base made very thin? | So that injected carriers cross it before they recombine. | 13.1–13.2; NPN vs PNP table |
| 2 | Describe injection, diffusion, recombination and collection in the forward-active region. | Which junction is forward biased in forward-active operation? | The emitter–base junction (collector–base is reverse biased). | 13.2 |
| 3 | Sketch and explain the minority-carrier profiles. | What shape is the electron profile in a thin base, and what does its slope set? | Almost a straight line; its slope sets the collector current. | 13.3; 13.8 (I_C = I_S e^{qV_BE/kT}) |
| 4 | Define emitter injection efficiency and base transport factor. | How is γ made close to 1? | By doping the emitter much more heavily than the base. | 13.4–13.5; Example 13.2 |
| 5 | Derive α and β and relate them to γ and α_T. | Write β in terms of α. | β = α/(1 − α). | 13.6–13.8 |
| 6 | Solve problems on transistor currents and gains. | β = 100, I_C = 5 mA: find I_B and I_E. | I_B = 50 μA, I_E = 5.05 mA. | Examples 13.1–13.4; worked examples 1–4; review Q7 |
