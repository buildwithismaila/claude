# Module 17 — Applying the Theorems to AC

Every theorem in Modules 07–12 holds unchanged for AC steady state. Only one
thing changes: **resistance R becomes impedance Z, a complex number.** Once you
accept complex arithmetic, nothing else is new.

## 13.1 Sinusoids and phasors

A sinusoid v(t) = V_m cos(ωt + φ) is represented by the **phasor**

    V = V_m ∠φ        (or V_rms ∠φ, if RMS convention is used)

with ω = 2πf understood throughout. Phasors turn differential equations into
algebra:

    d/dt  ⟶  × jω           ∫ dt  ⟶  ÷ jω

RMS values: for a sinusoid, V_rms = V_m/√2 = 0.7071 V_m. Power calculations use
RMS; most textbook phasors use amplitude. Be explicit about which you are using
— mixing them costs a factor of 2 in power.

## 13.2 Impedance

    Z = V/I = R + jX        [Ω]

| Element | Impedance | Note |
|---|---|---|
| Resistor R | Z = R | current in phase with voltage |
| Inductor L | Z = jωL | voltage **leads** current by 90° |
| Capacitor C | Z = 1/(jωC) = −j/(ωC) | voltage **lags** current by 90° |

- X > 0 → inductive; X < 0 → capacitive.
- **Admittance** Y = 1/Z = G + jB (siemens), the AC counterpart of conductance.

Series and parallel combination rules are **identical** to the resistive case,
using Z:

    Z_series = Z_1 + Z_2 + …
    1/Z_parallel = 1/Z_1 + 1/Z_2 + …

Mnemonic for phase: **ELI the ICE man** — in an inductor (L), E leads I; in a
capacitor (C), I leads E.

## 13.3 The theorems in AC form

| Theorem | AC statement |
|---|---|
| Nodal/mesh | Same equations with Z and complex V, I |
| Superposition | Same — and **mandatory** for sources at different frequencies |
| Source transformation | V_s = I_s Z, same Z |
| Thévenin | V_th = open-circuit phasor voltage; Z_th = impedance looking in |
| Norton | I_N = short-circuit phasor current; Z_N = Z_th |
| Maximum power | **Z_L = Z_th\*** (complex conjugate) |

### Different frequencies

Impedance depends on ω. If two sources operate at different frequencies you
**cannot** write a single phasor circuit — the impedances differ between them.
You must:

1. Solve the circuit at ω_1 with the ω_2 source deactivated.
2. Solve at ω_2 with the ω_1 source deactivated.
3. Convert each answer back to the time domain.
4. **Add the time-domain waveforms** — not the phasors.

A DC source counts as ω = 0, where an inductor is a short and a capacitor an
open. This is the one situation where superposition is not merely convenient but
unavoidable.

## 13.4 AC power

    S = V_rms I_rms* = P + jQ        [VA]

- **P** = real power [W] = V_rms I_rms cos θ — does actual work
- **Q** = reactive power [VAr] = V_rms I_rms sin θ — sloshes back and forth
- **|S|** = apparent power [VA]
- **cos θ** = power factor, with θ the angle by which voltage leads current

Lagging power factor = inductive load (the usual industrial case). Leading =
capacitive.

**Power factor correction:** adding shunt capacitance cancels inductive Q,
reducing the current drawn for the same real power, which cuts I²R losses in the
supply. The capacitance needed to move from pf angle θ_1 to θ_2 is

    C = P(tan θ_1 − tan θ_2) / (ω V_rms²)

## 13.5 Maximum power transfer in AC

With Z_th = R_th + jX_th, maximum power goes to the load when

    Z_L = Z_th*  =  R_th − jX_th

so the reactances **cancel** and the resistances **match**. Then

    P_max = |V_th|² / (8R_th)     for amplitude phasors
    P_max = V_th,rms² / (4R_th)   for RMS phasors

The reactance cancellation makes physical sense: reactive power does no work, so
the best thing to do with it is eliminate it, leaving a purely resistive match.

**Restricted cases:**
- If only |Z_L| may vary (fixed angle), the condition is |Z_L| = |Z_th|.
- If the load must be purely resistive, then R_L = |Z_th| = √(R_th² + X_th²).

## 13.6 Worked examples

**Example 1 — impedances.** Find Z for a 10 Ω resistor in series with a 20 mH
inductor at 50 Hz.

    ω = 2π(50) = 314.16 rad/s
    X_L = ωL = 314.16 × 0.02 = 6.283 Ω
    Z = 10 + j6.283 = 11.81 ∠32.14° Ω

**Example 2 — AC Thévenin.**
A 100∠0° V source in series with j10 Ω feeds terminals across a −j20 Ω
capacitor. Find the Thévenin equivalent.

*V_th* (voltage divider with impedances):

    V_th = 100 × (−j20)/(j10 − j20) = 100 × (−j20)/(−j10) = 200∠0° V

The divider ratio exceeds 1 — entirely normal in a resonant LC divider, and a
result that would be impossible with resistors.

*Z_th* (source shorted): j10 ∥ (−j20)

    Z_th = (j10)(−j20)/(j10 − j20) = (200)/(−j10) = j20 Ω

**Example 3 — conjugate matching.**
A source has Z_th = 6 + j8 Ω and V_th = 50∠0° V (amplitude). Find the load for
maximum power and the power delivered.

    Z_L = 6 − j8 Ω
    Total Z = 12 Ω (purely real)
    I = 50/12 = 4.167 A amplitude
    P = ½|I|²R_L = ½(4.167)²(6) = 52.1 W

Check with the formula: P_max = |V_th|²/(8R_th) = 2500/48 = 52.1 W ✓

**Example 4 — power factor.**
A load draws 5 kW at 0.7 lagging from a 240 V, 50 Hz supply. Find the current,
and the capacitance to correct to 0.95 lagging.

    |S| = P/pf = 5000/0.7 = 7143 VA
    I = 7143/240 = 29.8 A

    θ_1 = cos⁻¹(0.7) = 45.57°,  tan θ_1 = 1.0202
    θ_2 = cos⁻¹(0.95) = 18.19°, tan θ_2 = 0.3287
    C = 5000(1.0202 − 0.3287)/(314.16 × 240²)
      = 5000(0.6915)/(314.16 × 57600)
      = 3457.5/18,095,574 = 191 μF

New current: |S| = 5000/0.95 = 5263 VA ⇒ I = 21.9 A, a **26% reduction** for the
same real power. That is the whole commercial case for power factor correction.

## 13.7 Exercises

1. Find Z for 50 Ω in series with 100 μF at 60 Hz. (50 − j26.5 Ω)
2. A circuit has a 10 V DC source and a 5cos(1000t) V source. Explain why
   superposition is required, and state what the inductor looks like to each.
3. Z_th = 20 + j15 Ω, V_th = 100∠0° V amplitude. Find Z_L for max power and
   P_max. (20 − j15 Ω; 62.5 W)
4. A load takes 10 A at 0.8 lagging from 415 V. Find P, Q and |S|.
   (3.32 kW, 2.49 kVAr, 4.15 kVA)
5. Repeat Module 09 Example 1 with the 4 Ω replaced by j4 Ω and the 12 Ω by
   −j12 Ω.

## Takeaways

- Replace R by Z and every DC theorem carries over unchanged.
- Different frequencies ⇒ separate phasor circuits, then add in the time domain.
- Maximum power needs the **conjugate** match: resistances equal, reactances
  cancelled.
- Power factor correction reduces current, not real power — that is the point.
