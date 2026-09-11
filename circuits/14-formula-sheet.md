# Module 14 — Formula Sheet

## Basics
q = ∫i dt  |  i = dq/dt  |  v = dw/dq  |  p = vi  |  w = ∫p dt
Passive sign convention: current **into +** ⇒ p = vi is **absorbed**
Σ p_absorbed = 0 over the whole circuit
1 kWh = 3.6×10⁶ J

## Resistance
v = iR  |  G = 1/R  |  p = i²R = v²/R  |  R = ρℓ/A
Short: R = 0, v = 0. Open: R = ∞, i = 0.

## Series and parallel
R_series = R_1 + R_2 + …
1/R_parallel = 1/R_1 + 1/R_2 + …  |  two only: R_1R_2/(R_1+R_2)
n equal in parallel: R/n
Series R_eq > largest; parallel R_eq < smallest

## Dividers
Voltage: V_k = V_s R_k/ΣR          (load must be folded in first)
Current (two): I_1 = I_s R_2/(R_1+R_2),  I_2 = I_s R_1/(R_1+R_2)
Note the cross-over: current prefers the **smaller** resistance

## Delta–wye
Δ→Y: R_1 = R_bR_c/(R_a+R_b+R_c)  (and cyclic)
Y→Δ: R_a = (R_1R_2+R_2R_3+R_3R_1)/R_1  (and cyclic)
Balanced: R_Δ = 3R_Y
Bridge balance: R_1R_4 = R_2R_3

## Kirchhoff
KCL: Σi_in = 0 at a node (or any closed surface)
KVL: Σv = 0 around a loop
b branches, n nodes ⇒ (n−1) KCL + [b−(n−1)] KVL

## Nodal analysis
Current leaving node A through R: (V_A − V_B)/R
By inspection: G_kk = Σ conductances at node k; G_jk = −(conductance between j,k)
I_k = source currents entering node k
Voltage source to ground ⇒ node voltage known
Voltage source between two nodes ⇒ **supernode** + constraint V_A − V_B = V_s

## Mesh analysis
All mesh currents same direction (clockwise)
Shared resistor voltage: R(i_1 − i_2)
By inspection: R_kk = Σ resistances in mesh k; R_jk = −(shared resistance)
V_k = source rises driving mesh k
Current source in one mesh ⇒ mesh current known
Current source shared ⇒ **supermesh** + constraint i_1 − i_2 = I_s
Matrix is symmetric unless dependent sources are present

## Superposition
Voltage source off ⇒ **short**.  Current source off ⇒ **open**.
Dependent sources **always stay active**.
Never superpose power — superpose v or i, then square.

## Source transformation
V_s = I_s R  |  I_s = V_s/R  |  R unchanged
Arrow points toward where the + terminal faced
Terminal behaviour preserved; internal power **not** preserved

## Thévenin and Norton
V_th = open-circuit voltage
I_N = short-circuit current
R_th = R_N = resistance looking in, **independent** sources off
R_th = V_oc/I_sc  |  I_N = V_th/R_th  |  V_th = I_N R_N

Finding R_th:
1. Reduce by series/parallel — only if no dependent sources
2. Test source (1 V ⇒ R = 1/I, or 1 A ⇒ R = V/1) — always valid
3. V_oc/I_sc — always valid, fails only if both are zero

Valid **only at the terminals**: internal v, i and p are not reproduced.

## Maximum power transfer
DC: R_L = R_th  |  P_max = V_th²/(4R_th) = I_N²R_th/4
Efficiency at match = **50%**
If R_th is the variable instead, make it as **small** as possible
AC: Z_L = Z_th* (R_L = R_th, X_L = −X_th)
  P_max = |V_th|²/(8R_th) amplitude, or V_rms²/(4R_th)
  |Z_L| fixed-angle case: |Z_L| = |Z_th|
  Purely resistive load: R_L = |Z_th|

## Other theorems
Millman: V_eq = ΣV_kG_k/ΣG_k,  R_eq = 1/ΣG_k
Reciprocity: I_B/V_A = I_A/V_B (linear, passive, bilateral, single source)
Substitution: replace a branch by anything with the same v and i
Compensation: ΔR in a branch carrying I ⇒ equivalent source V_c = I·ΔR opposing
Tellegen: Σv_k i_k = 0 (needs only KCL and KVL)

## AC steady state
V = V_m∠φ  |  ω = 2πf  |  V_rms = V_m/√2
Z_R = R  |  Z_L = jωL  |  Z_C = 1/(jωC) = −j/(ωC)
Z = R + jX  |  Y = 1/Z = G + jB
d/dt → ×jω,  ∫dt → ÷jω
ELI the ICE man: inductor E leads I; capacitor I leads E

S = V_rms I_rms* = P + jQ
P = V_rms I_rms cos θ [W]  |  Q = V_rms I_rms sin θ [VAr]  |  |S| [VA]
pf = cos θ; lagging = inductive, leading = capacitive
pf correction: C = P(tan θ_1 − tan θ_2)/(ω V_rms²)

Different frequencies ⇒ solve separately, add **time-domain** waveforms
DC is ω = 0: inductor → short, capacitor → open

## Constants
ρ_copper = 1.72×10⁻⁸ Ω·m  |  ρ_aluminium = 2.82×10⁻⁸ Ω·m
e = 1.602×10⁻¹⁹ C
