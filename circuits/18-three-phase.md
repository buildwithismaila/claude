# Module 18 — Three-Phase Circuits

Nearly all bulk electrical power is generated, transmitted and consumed as three
phase. The reason is not tradition: three-phase delivers **constant instantaneous
power**, needs less conductor material for the same power, and produces a
rotating magnetic field that starts a motor without help.

## 18.1 Balanced three-phase sources

Three sinusoidal sources of equal magnitude, 120° apart.

**Positive (abc) sequence:**

    V_an = V_p ∠0°
    V_bn = V_p ∠−120°
    V_cn = V_p ∠+120°

**Negative (acb) sequence** reverses b and c. Sequence matters: it decides which
way a three-phase motor turns.

**Key property:** V_an + V_bn + V_cn = 0 for a balanced set. Three equal phasors
120° apart always sum to zero — which is why the neutral of a balanced system
carries no current.

## 18.2 Wye and delta

### Wye (Y, star)
Three phases share a common neutral point.

- **Phase voltage** V_p = line-to-neutral
- **Line voltage** V_L = line-to-line

    V_L = √3 V_p,   with V_L leading V_p by 30°
    I_L = I_p       (line and phase currents are the same)

The √3 comes from the phasor difference of two sources 120° apart:
|V_an − V_bn| = √3 V_p.

### Delta (Δ, mesh)
Three phases connected head to tail in a closed triangle. No neutral.

    V_L = V_p       (line and phase voltages are the same)
    I_L = √3 I_p,   with I_L lagging I_p by 30°

**The symmetry to remember:**

| | Wye | Delta |
|---|---|---|
| Voltage | V_L = √3 V_p | V_L = V_p |
| Current | I_L = I_p | I_L = √3 I_p |

√3 = 1.732 appears exactly once in each column, and never in both.

## 18.3 Balanced load analysis

Four combinations exist (Y–Y, Y–Δ, Δ–Y, Δ–Δ), but you never need four methods.

> **Per-phase method:** convert everything to an equivalent **Y–Y** system,
> analyse **one phase only** as a single-phase circuit, then infer the other two
> by ±120°.

Conversions:

    Δ load → Y load:   Z_Y = Z_Δ/3
    Y load → Δ load:   Z_Δ = 3Z_Y

For a balanced Y–Y system the neutral carries zero current, so you may connect
(or ignore) the neutral freely — it makes no difference. That is what licenses
the per-phase shortcut.

**Procedure:**
1. Convert any Δ source or load to its Y equivalent.
2. Draw one phase: V_p in series with the line impedance and Z_Y.
3. Solve for I_p.
4. Line currents and other phases follow by symmetry and the √3/30° rules.

## 18.4 Three-phase power

For a balanced load with phase angle θ (the impedance angle):

    P = 3 V_p I_p cos θ = √3 V_L I_L cos θ        [W]
    Q = 3 V_p I_p sin θ = √3 V_L I_L sin θ        [VAr]
    |S| = √3 V_L I_L                              [VA]

**The √3 V_L I_L form is the one used in practice**, because line quantities are
what you measure at a switchboard. Note it holds for **both** Y and Δ — the
connection cancels out of the product.

### Constant instantaneous power

The great advantage. For a balanced three-phase load:

    p(t) = 3 V_p I_p cos θ = constant

The three phases' pulsating powers sum to a steady value. A single-phase load
delivers power that pulses to zero twice per cycle; a three-phase motor
therefore produces smooth torque with no vibration at twice mains frequency.

### Power measurement — the two-wattmeter method

Two wattmeters suffice for any three-wire system, balanced or not:

    P = P_1 + P_2
    Q = √3 (P_1 − P_2)
    tan θ = √3 (P_1 − P_2)/(P_1 + P_2)

A negative reading on one wattmeter is normal when the power factor is below
0.5 — it is not a fault.

## 18.5 Unbalanced loads

If the load is not balanced:

- **Four-wire Y (with neutral):** each phase is independent — solve as three
  separate single-phase circuits. The neutral now carries
  I_N = I_a + I_b + I_c ≠ 0.
- **Three-wire Y (no neutral):** the load's star point shifts away from the
  source neutral. Use Millman's theorem (Module 12) to find the displacement
  voltage, then each phase current.
- **Δ load:** each phase sees the full line voltage regardless of balance, so
  phase currents are independent; line currents follow by KCL.

Per-phase analysis is **invalid** for unbalanced systems — that shortcut relies
on symmetry.

## 18.6 Worked examples

**Example 1 — Y connection basics.** A balanced Y source has
V_an = 240∠0° V. Find all phase and line voltages.

    V_an = 240∠0°,  V_bn = 240∠−120°,  V_cn = 240∠120°
    V_L = √3(240) = 415.7 V
    V_ab = 415.7∠30°,  V_bc = 415.7∠−90°,  V_ca = 415.7∠150°

(That is the standard 240/415 V system used across much of the world.)

**Example 2 — balanced Y–Y load.**
A 415 V (line) balanced Y source feeds a balanced Y load of Z = 12 + j9 Ω per
phase. Find the line current and total power.

    V_p = 415/√3 = 239.6 V
    |Z| = √(144 + 81) = 15 Ω,  θ = tan⁻¹(9/12) = 36.87°
    I_p = 239.6/15 = 15.97 A = I_L

    P = √3 V_L I_L cos θ = √3(415)(15.97)(0.8) = 9184 W ≈ 9.18 kW
    Q = √3(415)(15.97)(0.6) = 6888 VAr
    |S| = √3(415)(15.97) = 11,480 VA

Check per-phase: P = 3I_p²R = 3(15.97²)(12) = 9183 W ✓

**Example 3 — delta load.**
The same source feeds a balanced Δ load of Z_Δ = 36 + j27 Ω per phase.

Convert: Z_Y = Z_Δ/3 = 12 + j9 Ω — identical to Example 2. So the line current
and total power are the same: **15.97 A and 9.18 kW**.

Directly in delta: V_p = V_L = 415 V, |Z_Δ| = 45 Ω, so
I_p = 415/45 = 9.22 A, and I_L = √3(9.22) = 15.97 A ✓

**Example 4 — two-wattmeter method.**
Two wattmeters read P_1 = 8 kW and P_2 = 2 kW. Find total power and power factor.

    P = 8 + 2 = 10 kW
    tan θ = √3(8 − 2)/(8 + 2) = √3(6)/10 = 1.0392
    θ = 46.1°
    pf = cos 46.1° = 0.693 lagging

**Example 5 — why three-phase uses less copper.**
Compare a single-phase and a three-phase system delivering the same power at the
same line voltage and power factor. Single-phase needs I = P/(V cos θ); three
phase needs I_L = P/(√3 V cos θ), i.e. **1/√3 of the current** — so conductor
cross-section (and copper mass) drops by the same factor, offset by needing
three conductors rather than two. The net saving is about 25%, which over
thousands of kilometres of transmission line is enormous.

## 18.7 Exercises

1. A balanced Δ load draws 12 A line current from a 400 V supply at 0.85 pf.
   Find P, Q and the phase current. (7.07 kW, 4.38 kVAr, 6.93 A)
2. A Y load of 20∠30° Ω per phase is fed from 415 V line. Find I_L and P.
   (11.98 A; 7.46 kW)
3. Convert a Δ load of 60∠40° Ω per phase to its Y equivalent. (20∠40° Ω)
4. Two wattmeters read 5 kW and −1 kW. Find total power and pf.
   (4 kW; pf = 0.359)
5. Explain why a balanced three-phase load needs no neutral conductor.

## Takeaways

- Balanced set sums to zero — hence no neutral current.
- Wye: V_L = √3V_p, I_L = I_p. Delta: V_L = V_p, I_L = √3I_p. The √3 sits in
  exactly one row of each.
- Convert Δ → Y (÷3), analyse **one phase**, infer the rest.
- P = √3 V_L I_L cos θ for both connections.
- Instantaneous power is constant — the reason three-phase motors run smoothly.
