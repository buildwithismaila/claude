# Module 11 — Maximum Power Transfer

## 11.1 The question

Given a source network with a fixed Thévenin equivalent (V_th, R_th), what load
resistance R_L extracts the most power?

This is a genuinely different question from "what load gets the most voltage"
(answer: an open circuit) or "the most current" (answer: a short circuit).
Neither of those extremes delivers any power at all — one has no current, the
other no voltage. The maximum sits between them.

## 11.2 Derivation

With the load connected:

    I = V_th/(R_th + R_L)
    P_L = I²R_L = V_th² R_L / (R_th + R_L)²

Differentiate with respect to R_L and set to zero. Using the quotient rule:

    dP/dR_L = V_th² [(R_th + R_L)² − R_L · 2(R_th + R_L)] / (R_th + R_L)⁴
            = V_th² [(R_th + R_L) − 2R_L] / (R_th + R_L)³
            = V_th² (R_th − R_L) / (R_th + R_L)³

This is zero when

    R_L = R_th

and the second derivative is negative there, confirming a maximum.

## 11.3 The result

> **Maximum power is transferred to the load when R_L = R_th.**

The maximum power itself:

    P_max = V_th² R_th / (2R_th)² = V_th² / (4R_th)

Equivalently, in terms of the Norton form, P_max = I_N² R_th/4.

## 11.4 Efficiency — the part that matters in practice

At the matched condition, the load and R_th carry the same current and have the
same resistance, so they dissipate **equal power**. Therefore:

    η = P_L/P_total = 50%

**Half the energy is wasted inside the source.** This is why matched loading is
used in signal and communications systems — where the signal is precious and the
power is negligible — and **never** in power systems, where wasting half the
generated energy would be catastrophic.

A power distribution network deliberately operates with R_L ≫ R_th, sacrificing
maximum power transfer for efficiency in the 90%+ range. The two goals are in
direct conflict, and knowing which one applies is an engineering judgement, not
a formula.

### Shape of the curve

The peak is **broad and flat**. Because P depends on the ratio R_L/R_th:

| R_L/R_th | P/P_max |
|---|---|
| 0.5 | 0.889 |
| 0.8 | 0.988 |
| 1.0 | 1.000 |
| 1.25 | 0.988 |
| 2.0 | 0.889 |
| 5.0 | 0.556 |

So a mismatch of ±25% costs barely 1% of the available power. Precise matching
matters far less than people assume — a useful practical fact.

## 11.5 Variants worth knowing

**Fixed load, variable source resistance.** If R_L is fixed and R_th can vary,
the answer is *not* R_th = R_L — it is **R_th as small as possible**, because
every ohm of R_th only wastes power. The symmetric-looking answer is wrong here.
Read the question carefully to see which resistance is the free variable.

**Constrained range.** If R_L is restricted to a range that excludes R_th,
P_L is monotonic over that range, so pick whichever endpoint is closest to R_th.

**AC circuits.** With impedances, maximum power transfer requires the **complex
conjugate** match:

    Z_L = Z_th*        i.e.   R_L = R_th  and  X_L = −X_th

The reactance is cancelled, not matched. If only the magnitude |Z_L| may vary
with a fixed angle, the condition becomes |Z_L| = |Z_th| instead. See Module 17.

## 11.6 Worked examples

**Example 1.** A network has V_th = 24 V, R_th = 8 Ω. Find R_L for maximum
power, that power, and the efficiency.

    R_L = 8 Ω
    P_max = V_th²/(4R_th) = 576/32 = 18 W
    Check: I = 24/16 = 1.5 A, P_L = 1.5²(8) = 18 W ✓
    Power in R_th = 18 W, total = 36 W, η = 50%

**Example 2.** For Module 09 Example 1 (V_th = 9 V, R_th = 3 Ω), find the
maximum power available and compare with the 6 Ω load used there.

    P_max = 81/12 = 6.75 W at R_L = 3 Ω
    With 6 Ω: I = 9/9 = 1 A, P = 1²(6) = 6 W

So the 6 Ω load, though mismatched 2:1, still gets 6/6.75 = **89%** of the
available power — exactly as the table in §11.4 predicts.

**Example 3.** A 12 V battery with 0.5 Ω internal resistance. What load draws
maximum power, and would you ever use it?

    R_L = 0.5 Ω,  P_max = 144/2 = 72 W

But the battery itself would also dissipate 72 W, at 24 A. It would overheat
rapidly and the efficiency would be 50%. In practice you would never load a
battery this way — this is the classic illustration that maximum power transfer
is a signal-engineering criterion, not a power-engineering one.

**Example 4 — the variable-source-resistance trap.**
A fixed 10 Ω load is fed by a source whose internal resistance can be chosen
anywhere from 2 Ω to 40 Ω. What value maximises load power?

Not 10 Ω. Choose **R_th = 2 Ω**, the smallest available, since

    P_L = V_th²(10)/(R_th + 10)²

decreases monotonically as R_th grows.

## 11.7 Exercises

1. V_th = 40 V, R_th = 20 Ω. Find R_L, P_max and η. (20 Ω, 20 W, 50%)
2. A source delivers 100 W to a matched load. What is V_th if R_th = 25 Ω?
   (100 V)
3. A network's Norton equivalent is 3 A ∥ 12 Ω. Find P_max. (27 W)
4. Show that at R_L = 4R_th the load receives 64% of P_max.
5. Explain why a 400 kV transmission line is not operated at matched load.

## Takeaways

- R_L = R_th for maximum power; P_max = V_th²/(4R_th).
- Efficiency at match is exactly 50% — fine for signals, unacceptable for power.
- The peak is flat: ±25% mismatch costs about 1%.
- If it is R_th that varies rather than R_L, the answer flips to "make R_th as
  small as possible".
