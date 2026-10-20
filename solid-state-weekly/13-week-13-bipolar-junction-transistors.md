# Week 13 — Bipolar Junction Transistors (BJTs)
<!-- group: Module 5 · Advanced Device Technology -->

**Plan:** operational physics; minority-carrier profiles in the active regions; emitter efficiency, base transport factor and current gains (α, β).

A BJT is two p-n junctions (Week 10) sharing one thin middle region. The physics is the minority-carrier diffusion of Weeks 7–9.

## Structure

An **npn** transistor has a heavily doped n⁺ **emitter**, a thin, moderately doped p-type **base**, and a lightly doped n-type **collector**: N_E ≫ N_B > N_C. A pnp transistor reverses every type. The base width W_B is typically 0.05–1 μm, much shorter than the electron diffusion length L_n in the base (tens of μm).

## Modes of operation

| Mode | E–B junction | C–B junction | Use |
|---|---|---|---|
| Forward active | Forward | Reverse | Amplifier |
| Saturation | Forward | Forward | Switch ON |
| Cut-off | Reverse | Reverse | Switch OFF |
| Reverse active | Reverse | Forward | Rarely used (poor gain) |

## Operation in the forward-active mode (npn)

1. The forward-biased E–B junction lowers its barrier. Electrons are **injected** from the emitter into the base, where they are minority carriers. At the base edge, by the law of the junction, n_p(0) = n_p0 e^{qV_BE/kT}.
2. Because W_B ≪ L_n, almost every injected electron **diffuses across** the base without recombining.
3. At the reverse-biased C–B junction the minority concentration is held at nearly zero, n_p(W_B) ≈ 0. The depletion field **sweeps** the arriving electrons into the collector. This is the collector current.
4. At the same time the forward-biased E–B junction injects some **holes** from the base back into the emitter, and a few electrons **recombine** in the base. Both are supplied by the base current, which is small.

The collector current is controlled by V_BE but almost independent of V_CB: a small input (base current or V_BE) controls a large output current, which is amplification.

## Minority-carrier profiles

@fig figures/bjt-profile.svg | Minority-carrier profiles in an npn transistor in forward-active mode. Electrons injected into the base fall almost linearly from n_p(0) to zero at the collector edge; the slope sets the collector current. Holes injected into the emitter decay over the emitter.

**Base.** The continuity equation in the base (Week 9), with W_B ≪ L_n, gives a nearly **linear** profile:

    Δn_p(x) ≈ n_p0 (e^{qV_BE/kT} − 1)(1 − x/W_B)

The electron diffusion current is proportional to its slope:

    I_C ≈ qA D_n n_p0 e^{qV_BE/kT} / W_B = (qA D_n n_i² / (N_B W_B)) e^{qV_BE/kT} = I_S e^{qV_BE/kT}

**Emitter.** Holes injected into the emitter give the unwanted current

    I_pE = (qA D_E n_i² / (N_E W_E)) (e^{qV_BE/kT} − 1)       (short emitter, W_E ≪ L_pE)

**Collector.** Reverse-biased; only the small leakage I_CBO of minority carriers.

## Current components

    I_E = I_nE + I_pE               (electrons injected into base + holes injected into emitter)
    I_C = I_nC + I_CBO ≈ I_nC       (electrons reaching the collector)
    I_B = I_E − I_C = I_pE + (I_nE − I_nC) − I_CBO   (back-injection + base recombination)

## Emitter injection efficiency γ

The fraction of emitter current carried by the useful carriers (electrons in an npn):

    γ = I_nE / (I_nE + I_pE) = 1 / [ 1 + (D_E N_B W_B) / (D_B N_E W_E) ]

To make γ → 1, dope the emitter much more heavily than the base (N_E ≫ N_B). Heterojunction bipolar transistors (HBTs) use a wider-gap emitter to suppress I_pE further.

## Base transport factor α_T

The fraction of injected electrons that survive the trip across the base:

    α_T = I_nC / I_nE ≈ 1 − W_B² / (2L_n²)          (L_n = √(D_Bτ_n))

To make α_T → 1, make the base thin and the base lifetime long.

## Current gains

**Common-base gain α:**

    α = I_C / I_E = γ α_T     (typically 0.98–0.998)

**Common-emitter gain β:**

    β = I_C / I_B = α / (1 − α)      ⇒      1/β ≈ (D_E N_B W_B)/(D_B N_E W_E) + W_B²/(2L_n²)

Since α is close to 1, β is large (typically 50–500). Small changes in α make large changes in β: α = 0.99 gives β = 99; α = 0.995 gives β = 199.

Relations: I_E = I_C + I_B; I_C = βI_B; I_C = αI_E; α = β/(β + 1).

## Non-ideal effects

- **Early effect (base-width modulation).** Increasing V_CE widens the C–B depletion region into the base, shortening W_B. The slope of n_p(x) steepens, so I_C rises with V_CE. Extrapolated output curves meet at −V_A (the Early voltage); output resistance r_o = V_A/I_C.
- **High-level injection** at large I_C reduces β (the injected electrons approach N_B).
- **Recombination in the E–B depletion region** reduces β at low current.
- **Base resistance** and **emitter current crowding**.
- **Breakdown:** avalanche at the C–B junction (BV_CBO) and punch-through when the C–B depletion region reaches the emitter.
- **Base transit time** τ_B = W_B²/2D_n limits speed: f_T ≈ 1/(2πτ_B).

## Worked example

An npn Si transistor: N_E = 10¹⁹ cm⁻³, N_B = 10¹⁷ cm⁻³, W_E = 1 μm, W_B = 0.5 μm, D_E (holes in emitter) = 2.5 cm²/s, D_B (electrons in base) = 25 cm²/s, τ_n = 1 μs, area A = 10⁻⁴ cm². Find γ, α_T, α, β, I_C at V_BE = 0.65 V, and the base transit time.

    γ = 1 / [1 + (2.5 × 10¹⁷ × 0.5) / (25 × 10¹⁹ × 1)] = 1 / (1 + 5×10⁻⁴) = 0.99950

    L_n = √(25 × 10⁻⁶) = 5×10⁻³ cm = 50 μm
    α_T = 1 − (0.5)² / (2 × 50²) = 1 − 5×10⁻⁵ = 0.99995

    α = γα_T = 0.99945,     β = α/(1 − α) = 0.99945/0.00055 ≈ 1800

    I_S = qAD_Bn_i²/(N_BW_B) = (1.6×10⁻¹⁹)(10⁻⁴)(25)(10²⁰) / (10¹⁷ × 5×10⁻⁵) = 8×10⁻¹⁵ A
    I_C = 8×10⁻¹⁵ × e^{0.65/0.0259} = 8×10⁻¹⁵ × 7.9×10¹⁰ = 0.63 mA,   I_B = I_C/β ≈ 0.35 μA

    τ_B = W_B²/2D_B = (5×10⁻⁵)²/50 = 5×10⁻¹¹ s = 50 ps,   f_T ≲ 1/(2πτ_B) ≈ 3 GHz

Here γ limits β (5×10⁻⁴ against 5×10⁻⁵). Real devices have lower β because of depletion-region recombination, band-gap narrowing in the heavily doped emitter and surface recombination.

---

## Practice questions solved

### P1. Explain the operation of an npn transistor in the forward-active mode with the aid of minority-carrier profiles.

With the E–B junction forward biased and the C–B junction reverse biased, electrons are injected from the n⁺ emitter into the p base, raising the electron density at the emitter edge of the base to n_p0e^{qV_BE/kT}. The reverse-biased collector holds the electron density at the collector edge near zero. Because the base is much thinner than the electron diffusion length, the profile between these two values is nearly linear, and electrons diffuse down it to the collector with very little recombination. The collector current, I_C = qAD_nn_i²e^{qV_BE/kT}/(N_BW_B), is set by the slope of this line and so by V_BE, almost independent of V_CB. The base supplies only the holes injected back into the emitter (kept small by heavy emitter doping) and the holes lost to recombination in the base (kept small by the thin base), so I_B ≪ I_C and the device amplifies. (Sketch: the figure above.)

### P2. Define emitter injection efficiency and base transport factor and show how they determine α and β.

Emitter injection efficiency γ = I_nE/(I_nE + I_pE) is the fraction of emitter current carried by carriers injected into the base; γ = 1/[1 + D_EN_BW_B/(D_BN_EW_E)], so it approaches 1 when N_E ≫ N_B. Base transport factor α_T = I_nC/I_nE is the fraction of those carriers that reach the collector; α_T ≈ 1 − W_B²/2L_n², approaching 1 for a thin base and long lifetime. The common-base gain is their product, α = I_C/I_E = γα_T (ignoring collector multiplication), and the common-emitter gain is β = I_C/I_B = α/(1 − α). Since 1 − α ≈ (1 − γ) + (1 − α_T) is small, β ≈ 1/[(1 − γ) + (1 − α_T)] is large.

### P3. A transistor has α = 0.992. Find β. If I_B = 20 μA, find I_C and I_E.

    β = 0.992/(1 − 0.992) = 124
    I_C = βI_B = 124 × 20 μA = 2.48 mA
    I_E = I_C + I_B = 2.50 mA

### P4. What is the Early effect and why is it a problem?

Increasing V_CB widens the collector–base depletion region, part of which extends into the base, so the neutral base width W_B decreases. The minority-carrier gradient in the base, and hence I_C ∝ 1/W_B, increases with V_CE, so the output characteristics slope upward instead of being flat. Extrapolated, they meet at V_CE = −V_A, the Early voltage. It gives the transistor a finite output resistance r_o = V_A/I_C, limiting the voltage gain of amplifiers (A_v ≤ g_mr_o = V_A/V_T). It also increases β with V_CE and, in the extreme, leads to punch-through. It is reduced by doping the base more heavily than the collector.
