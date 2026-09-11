# Module 26 — Problem Set with Full Solutions

Twenty-eight problems spanning the whole course. Work each on paper before reading the
solution. All numerical answers have been checked independently.

---

**P1.** An element has 15 V across it, + on the left, and 3 A entering the right
terminal. Find the power absorbed and state what the element is doing.

*Solution.* Current enters the **−** terminal, so p = vi gives *delivered* power.

    p_delivered = 15 × 3 = 45 W   ⇒   p_absorbed = −45 W

The element **delivers** 45 W — it is acting as a source.

---

**P2.** Find R_eq at terminals a–b: 10 Ω in series with (20 Ω ∥ (5 Ω + 15 Ω)).

    5 + 15 = 20 Ω
    20 ∥ 20 = 10 Ω
    R_eq = 10 + 10 = 20 Ω

---

**P3.** A 60 V source feeds 4 Ω in series with 8 Ω. A 24 Ω load is then placed
across the 8 Ω. Find the load voltage before and after loading.

*Before:* V = 60 × 8/12 = **40 V**

*After:* 8 ∥ 24 = 192/32 = 6 Ω

    V = 60 × 6/(4+6) = 60 × 0.6 = 36 V

The 10% droop is the divider's Thévenin resistance (4 ∥ 8 = 2.667 Ω) acting
against the 24 Ω load.

---

**P4.** A delta network has R_a = 30 Ω, R_b = 20 Ω, R_c = 50 Ω. Find the
equivalent wye.

    Sum = 100 Ω
    R_1 = R_bR_c/100 = (20)(50)/100 = 10 Ω
    R_2 = R_aR_c/100 = (30)(50)/100 = 15 Ω
    R_3 = R_aR_b/100 = (30)(20)/100 = 6 Ω

---

**P5.** A single loop: 40 V source, then 5 Ω, then a 10 V source in opposition,
then 15 Ω. Find the current and check power balance.

KVL clockwise:

    40 − 5i − 10 − 15i = 0
    30 = 20i    ⇒   i = 1.5 A

Power: 40 V delivers 60 W; 10 V absorbs 15 W; resistors absorb
1.5²(5) + 1.5²(15) = 11.25 + 33.75 = 45 W.
Check: −60 + 15 + 45 = 0 ✓

---

**P6.** Nodal analysis. Node 1 has a 5 A source in, 4 Ω to ground, and 2 Ω to
node 2. Node 2 has 8 Ω to ground. Find V_1 and V_2.

    Node 1: V_1/4 + (V_1 − V_2)/2 = 5
    Node 2: (V_2 − V_1)/2 + V_2/8 = 0

From node 2: 4V_2 − 4V_1 + V_2 = 0 ⇒ 5V_2 = 4V_1 ⇒ V_2 = 0.8V_1
Node 1 ×4: V_1 + 2V_1 − 2V_2 = 20 ⇒ 3V_1 − 1.6V_1 = 20 ⇒ 1.4V_1 = 20

    V_1 = 14.29 V,   V_2 = 11.43 V

Check node 1: 14.29/4 + (14.29−11.43)/2 = 3.571 + 1.429 = 5.0 ✓

---

**P7.** Supernode. Nodes 1 and 2 are joined by a 6 V source (+ at 1). Node 1 has
5 Ω to ground, node 2 has 10 Ω to ground, and a 4 A source feeds node 2.

    Supernode: V_1/5 + V_2/10 = 4
    Constraint: V_1 − V_2 = 6  ⇒  V_1 = V_2 + 6

    (V_2 + 6)/5 + V_2/10 = 4
    2(V_2 + 6) + V_2 = 40
    3V_2 = 28    ⇒   V_2 = 9.333 V,  V_1 = 15.333 V

Check: 15.333/5 + 9.333/10 = 3.067 + 0.933 = 4.0 ✓

---

**P8.** Mesh analysis. Mesh 1: 20 V source, 3 Ω, shared 6 Ω. Mesh 2: shared 6 Ω,
9 Ω. Find both mesh currents and the current in the 6 Ω.

    (3+6)i_1 − 6i_2 = 20
    −6i_1 + (6+9)i_2 = 0   ⇒   i_1 = 2.5 i_2

    9(2.5i_2) − 6i_2 = 20  ⇒  22.5i_2 − 6i_2 = 20  ⇒  16.5i_2 = 20
    i_2 = 1.212 A,   i_1 = 3.030 A
    i_6 = i_1 − i_2 = 1.818 A

Check mesh 1: 20 − 3(3.030) − 6(1.818) = 20 − 9.091 − 10.909 = 0 ✓

---

**P9.** Supermesh. Meshes 1 and 2 share a 3 A source (from mesh 2 into mesh 1).
Mesh 1 has a 15 V source and 4 Ω; mesh 2 has 5 Ω and 6 Ω.

    Constraint: i_1 − i_2 = 3
    Supermesh: 15 − 4i_1 − 5i_2 − 6i_2 = 0  ⇒  15 − 4i_1 − 11i_2 = 0

    15 − 4(i_2 + 3) − 11i_2 = 0
    15 − 4i_2 − 12 − 11i_2 = 0
    3 = 15i_2    ⇒   i_2 = 0.2 A,   i_1 = 3.2 A

Check: 15 − 4(3.2) − 11(0.2) = 15 − 12.8 − 2.2 = 0 ✓

---

**P10.** Superposition. A 30 V source through 6 Ω and a 3 A source both feed a
node that has 12 Ω to ground. Find the node voltage.

*30 V alone* (3 A opened): V' = 30 × 12/(6+12) = 20 V
*3 A alone* (30 V shorted): 6 ∥ 12 = 4 Ω, so V'' = 3 × 4 = 12 V

    V = 20 + 12 = 32 V

Check by nodal: (V−30)/6 + V/12 = 3 ⇒ 2V − 60 + V = 36 ⇒ 3V = 96 ⇒ V = 32 ✓

---

**P11.** Using P10's answer, find the power in the 12 Ω — and show why adding
the two individual powers is wrong.

    P = V²/R = 32²/12 = 1024/12 = 85.3 W

Naive sum: 20²/12 + 12²/12 = 33.3 + 12 = 45.3 W — **wrong**, because power is
quadratic. Superpose voltage, then square.

---

**P12.** Source transformation. A 36 V source in series with 12 Ω is in parallel
with a 1 A source and 6 Ω. Reduce to a single practical source.

    36 V/12 Ω → 3 A ∥ 12 Ω
    Parallel current sources: 3 + 1 = 4 A
    12 ∥ 6 = 4 Ω

    Equivalent: 4 A ∥ 4 Ω,  or  16 V in series with 4 Ω

---

**P13.** Thévenin. A 48 V source in series with 8 Ω, with 24 Ω across the output
terminals a–b. Find V_th, R_th, and the current into a 10 Ω load.

    V_th = 48 × 24/(8+24) = 48 × 0.75 = 36 V
    R_th = 8 ∥ 24 = 192/32 = 6 Ω
    I_L = 36/(6+10) = 2.25 A

Direct check: with 10 Ω connected, 24 ∥ 10 = 240/34 = 7.059 Ω; total 15.059 Ω;
source current 48/15.059 = 3.188 A; node voltage 3.188 × 7.059 = 22.5 V;
I_10 = 22.5/10 = 2.25 A ✓

---

**P14.** Norton. Give the Norton equivalent of P13's network and verify
consistency.

    I_N = V_th/R_th = 36/6 = 6 A,  R_N = 6 Ω

Direct check of I_sc: shorting a–b removes the 24 Ω, so I_sc = 48/8 = 6 A ✓
Load current by divider: 6 × 6/(6+10) = 2.25 A ✓

---

**P15.** Thévenin by V_oc/I_sc. A network gives V_oc = 20 V and, when shorted,
I_sc = 5 A. A 6 Ω load is connected. Find the load power.

    R_th = 20/5 = 4 Ω
    I_L = 20/(4+6) = 2 A
    P_L = 2²(6) = 24 W

---

**P16.** Maximum power transfer. For the network of P13 (V_th = 36 V,
R_th = 6 Ω), find R_L for maximum power, that power, and the efficiency.

    R_L = 6 Ω
    P_max = V_th²/(4R_th) = 1296/24 = 54 W
    Check: I = 36/12 = 3 A, P = 9 × 6 = 54 W ✓
    R_th also dissipates 54 W, so η = 50%

Compare with the 10 Ω load of P13: P = 2.25²(10) = 50.6 W, which is 94% of the
maximum despite a 1.67:1 mismatch — the flat-peak effect.

---

**P17.** Thévenin with a dependent source. A network consists of a 10 V source
in series with 2 Ω to node x, a 4 Ω from x to ground, and a VCCS from x to
ground of value 0.25v_x, where v_x is the node-x voltage. Terminals a–b are at
node x.

*V_th* (terminals open):

    (v_x − 10)/2 + v_x/4 + 0.25v_x = 0
    Multiply by 4:  2v_x − 20 + v_x + v_x = 0
    4v_x = 20   ⇒   V_th = 5 V

*R_th* by test source: deactivate the 10 V (short), apply 1 V at a–b.

    v_x = 1 V (terminals are node x)
    Current drawn from the test source = 1/2 + 1/4 + 0.25(1) = 0.5+0.25+0.25 = 1 A
    R_th = 1/1 = 1 Ω

*Check by V_oc/I_sc:* shorting a–b forces v_x = 0, so the dependent source
contributes nothing and I_sc = 10/2 = 5 A. Then R_th = 5/5 = 1 Ω ✓

Note that naive reduction would give 2 ∥ 4 = 1.33 Ω — wrong, because it deletes
the dependent source.

---

**P18.** Millman. Three practical sources in parallel: 20 V/5 Ω, 10 V/2 Ω, and
5 V/10 Ω. Find the equivalent, then the current into a 4 Ω load.

    Numerator = 20/5 + 10/2 + 5/10 = 4 + 5 + 0.5 = 9.5
    Denominator = 1/5 + 1/2 + 1/10 = 0.2 + 0.5 + 0.1 = 0.8
    V_eq = 9.5/0.8 = 11.875 V,   R_eq = 1/0.8 = 1.25 Ω
    I_L = 11.875/(1.25 + 4) = 11.875/5.25 = 2.262 A

---

**P19.** AC. A 100∠0° V (amplitude) source at ω = 1000 rad/s drives 30 Ω in
series with 40 mH. Find Z, the current phasor, and the real power.

    X_L = ωL = 1000 × 0.04 = 40 Ω
    Z = 30 + j40 = 50∠53.13° Ω
    I = 100∠0°/50∠53.13° = 2∠−53.13° A  (amplitude)

Real power (amplitude phasors, so use ½):

    P = ½|I|²R = ½(4)(30) = 60 W

Power factor = cos 53.13° = 0.6 lagging.

---

**P20.** AC maximum power. A source has V_th = 60∠0° V amplitude and
Z_th = 5 + j12 Ω. Find Z_L for maximum power and the power delivered. Then find
the best purely resistive load and the power it would receive.

*Conjugate match:*

    Z_L = 5 − j12 Ω
    Total Z = 10 Ω
    I = 60/10 = 6 A amplitude
    P = ½(36)(5) = 90 W
    Check: P_max = |V_th|²/(8R_th) = 3600/40 = 90 W ✓

*Purely resistive load:*

    R_L = |Z_th| = √(25 + 144) = 13 Ω
    Total Z = 18 + j12, |Z| = √(324+144) = √468 = 21.633 Ω
    |I| = 60/21.633 = 2.773 A
    P = ½(2.773)²(13) = ½(7.691)(13) = 50.0 W

The resistive-only load gets 50 W against 90 W available — a 44% shortfall.
Cancelling the reactance is worth a great deal.

---

---

**P21.** A 2 μF capacitor charged to 50 V discharges through 250 kΩ. Find τ,
v(t), the current at t = 0⁺, and the time to fall to 10 V.

    τ = RC = 250×10³ × 2×10⁻⁶ = 0.5 s
    v(t) = 50e^{−2t} V
    i(0⁺) = 50/250×10³ = 200 μA

For v = 10 V: e^{−2t} = 0.2 ⇒ −2t = ln 0.2 = −1.609

    t = 0.805 s

---

**P22.** An RL circuit (R = 20 Ω, L = 4 H) carries 3 A when the source is
switched from 60 V to 20 V at t = 0. Find i(t) and the time to reach 1.5 A.

    i(0⁺) = 3 A  (given, and continuous)
    i(∞) = 20/20 = 1 A
    τ = L/R = 4/20 = 0.2 s

    i(t) = 1 + (3 − 1)e^{−5t} = 1 + 2e^{−5t} A

For i = 1.5: 0.5 = 2e^{−5t} ⇒ e^{−5t} = 0.25 ⇒ t = ln4/5 = **0.277 s**

---

**P23.** A series RLC has R = 8 Ω, L = 1 H, C = 0.0625 F. Classify it and give
the form of the natural response.

    α = R/2L = 4
    ω_0 = 1/√(0.0625) = 4

α = ω_0 ⇒ **critically damped**, repeated root s = −4.

    x(t) = (A_1 + A_2 t)e^{−4t}

If R were reduced to 4 Ω: α = 2 < 4, underdamped, ω_d = √(16−4) = 3.46 rad/s.

---

**P24.** Invert F(s) = (3s + 10)/[s(s + 5)].

    A = (3s+10)/(s+5) at s=0 = 10/5 = 2
    B = (3s+10)/s at s=−5 = (−15+10)/(−5) = 1

    F(s) = 2/s + 1/(s+5)
    f(t) = 2 + e^{−5t}

Check final value: lim sF(s) = 10/5 = 2 ✓, and f(∞) = 2 ✓

---

**P25.** A series RL circuit (R = 4 Ω, L = 2 H) is driven by a 20 V step from
rest. Solve in the s-domain.

    I(s) = (20/s)/(4 + 2s) = 20/[s(2s + 4)] = 10/[s(s + 2)]

    A = 10/(s+2) at s=0 = 5;   B = 10/s at s=−2 = −5

    I(s) = 5/s − 5/(s+2)
    i(t) = 5(1 − e^{−2t}) A

Check: i(∞) = 20/4 = 5 A ✓; τ = L/R = 0.5 s, matching e^{−2t} ✓

---

**P26.** For H(s) = 50/(s² + 6s + 25), find the poles, state stability, and give
ω_0, α and ω_d.

    s = [−6 ± √(36 − 100)]/2 = −3 ± j4

Both poles have Re = −3 < 0 ⇒ **stable**.

    α = 3,  ω_d = 4,  ω_0 = √(9 + 16) = 5 rad/s
    ζ = α/ω_0 = 0.6, underdamped

DC gain: H(0) = 50/25 = 2.

---

**P27.** A balanced Y-connected load of 15 + j20 Ω per phase is fed from a
400 V (line) three-phase supply. Find the line current, power factor, P, Q
and |S|.

    V_p = 400/√3 = 230.9 V
    |Z| = √(225 + 400) = 25 Ω,  θ = tan⁻¹(20/15) = 53.13°
    I_L = I_p = 230.9/25 = 9.24 A
    pf = cos 53.13° = 0.6 lagging

    |S| = √3(400)(9.24) = 6400 VA
    P = 6400 × 0.6 = 3840 W
    Q = 6400 × 0.8 = 5120 VAr

Check per-phase: P = 3I²R = 3(9.24²)(15) = 3841 W ✓

---

**P28.** Find the ABCD parameters of a T network with series 20 Ω, shunt 40 Ω,
series 20 Ω, and verify reciprocity.

Cascade three elements: series 20, shunt 1/40 = 0.025 S, series 20.

Series 20: [1, 20; 0, 1]. Shunt: [1, 0; 0.025, 1].

First two:

    A = 1 + 20(0.025) = 1.5,  B = 20,  C = 0.025,  D = 1

Now multiply by the final series 20 element [1, 20; 0, 1]:

    A = 1.5(1) + 20(0) = 1.5
    B = 1.5(20) + 20(1) = 50
    C = 0.025(1) + 1(0) = 0.025
    D = 0.025(20) + 1(1) = 1.5

    AD − BC = 1.5(1.5) − 50(0.025) = 2.25 − 1.25 = 1 ✓

Reciprocal, and A = D confirms it is symmetric — as it must be, since the two
series arms are equal.

---

## Self-assessment

| Struggled on | Revisit |
|---|---|
| P1, P5 | Module 01 (sign convention), 04 |
| P2, P3, P4 | Module 03 |
| P6, P7 | Module 05 |
| P8, P9 | Module 06 |
| P10, P11 | Module 07 |
| P12 | Module 08 |
| P13, P14, P15, P17 | Modules 09–10 |
| P16 | Module 11 |
| P18 | Module 12 |
| P19, P20 | Module 17 |
| P21, P22 | Modules 13, 15 |
| P23 | Module 16 |
| P24, P25 | Modules 19, 20 |
| P26 | Module 21 |
| P27 | Module 18 |
| P28 | Module 23 |

Twenty-two or more unaided means you are exam-ready. Fewer than fourteen means
go back to Modules 04–06: almost every later failure traces to shaky nodal or
mesh work. If P24–P26 were the problem, the gap is partial fractions rather than
circuits — fix that first, since Modules 19–21 are unusable without it.
