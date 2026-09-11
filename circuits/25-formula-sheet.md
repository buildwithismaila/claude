# Module 25 — Formula Sheet

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

## Storage elements
i = C dv/dt  |  v = L di/dt
w_C = ½Cv²  |  w_L = ½Li²
**v_C and i_L cannot change instantaneously**
DC steady state: C → open, L → short
At t = 0⁺: uncharged C → short, unenergised L → open
C series: 1/C_eq = Σ1/C_k; C parallel: C_eq = ΣC_k  (opposite to R)
L series: L_eq = ΣL_k; L parallel: 1/L_eq = Σ1/L_k  (like R)

## Elementary signals
u(t) step  |  r(t) = t·u(t) ramp  |  δ(t) impulse
δ = du/dt, u = dr/dt  |  sifting: ∫f(t)δ(t−a)dt = f(a)
Pulse a→b of height A: A[u(t−a) − u(t−b)]
1τ → 63.2%, 3τ → 95%, **5τ → done**
F_rms = √((1/T)∫f²dt); sinusoid A/√2; square wave A

## First-order circuits
τ = R_th C   or   τ = L/R_th     (R_th seen by the element)

    x(t) = x(∞) + [x(0⁺) − x(∞)] e^{−t/τ}      x = v_C or i_L only

Initial value from pre-switch steady state; final from post-switch.

## Second-order circuits
Series RLC: α = R/2L     Parallel RLC: α = 1/(2RC)
Both: ω_0 = 1/√(LC),  ζ = α/ω_0,  Q = ω_0/2α
s = −α ± √(α² − ω_0²)

| Case | Condition | Form |
|---|---|---|
| Overdamped | α > ω_0 | A_1e^{s_1t} + A_2e^{s_2t} |
| Critically damped | α = ω_0 | (A_1 + A_2t)e^{−αt} |
| Underdamped | α < ω_0 | e^{−αt}(A_1cos ω_dt + A_2sin ω_dt) |

ω_d = √(ω_0² − α²)
Second initial condition: dv_C/dt(0⁺) = i_L(0⁺)/C, or di_L/dt(0⁺) = v_C(0⁺)/L

## Three-phase
Balanced set sums to zero
Wye: V_L = √3 V_p (leading 30°), I_L = I_p
Delta: V_L = V_p, I_L = √3 I_p (lagging 30°)
Z_Y = Z_Δ/3
P = √3 V_L I_L cos θ  |  Q = √3 V_L I_L sin θ  |  |S| = √3 V_L I_L
Instantaneous power is constant
Two wattmeters: P = P_1 + P_2, tan θ = √3(P_1 − P_2)/(P_1 + P_2)

## Laplace transform
F(s) = ∫₀^∞ f(t)e^{−st}dt

| f(t) | F(s) | | f(t) | F(s) |
|---|---|---|---|---|
| δ(t) | 1 | | e^{−at} | 1/(s+a) |
| u(t) | 1/s | | te^{−at} | 1/(s+a)² |
| t | 1/s² | | sin ωt | ω/(s²+ω²) |
| t^n | n!/s^{n+1} | | cos ωt | s/(s²+ω²) |
| e^{−at}sin ωt | ω/((s+a)²+ω²) | | e^{−at}cos ωt | (s+a)/((s+a)²+ω²) |

ℒ{df/dt} = sF(s) − f(0⁻)
ℒ{d²f/dt²} = s²F(s) − sf(0⁻) − f′(0⁻)
ℒ{∫f} = F(s)/s  |  ℒ{f(t−a)u(t−a)} = e^{−as}F(s)  |  ℒ{e^{−at}f} = F(s+a)
f(0⁺) = lim_{s→∞} sF(s)  |  f(∞) = lim_{s→0} sF(s)  (only if it settles)
Residue (simple pole): k_i = [(s + p_i)F(s)] at s = −p_i

## s-domain circuits
R → R  |  L → sL  |  C → 1/(sC)
Inductor IC: series source Li(0⁻), or parallel source i(0⁻)/s
Capacitor IC: series source v(0⁻)/s, or parallel source Cv(0⁻)
Phasors are the s-domain at s = jω

## Transfer functions and stability
H(s) = Y(s)/X(s) with zero initial conditions;  h(t) = ℒ⁻¹{H(s)}
y(t) = h(t) * x(t)  ⟷  Y(s) = H(s)X(s)
Poles set the response shape; zeros do not affect stability
**Stable ⟺ all poles strictly in the left half plane**
Simple poles on the jω axis → marginally stable; repeated → unstable
Passive RLC is always stable
2nd order s² + a_1s + a_0: stable ⟺ a_1 > 0 and a_0 > 0
Frequency response: H(jω); |H|_dB = 20log₁₀|H|; cutoff at 0.707 (−3 dB)
RC filter: ω_c = 1/RC, f_c = 1/(2πRC)

## Fourier
f(t) = a_0 + Σ[a_n cos nω_0t + b_n sin nω_0t],  ω_0 = 2π/T
a_0 = (1/T)∫f dt  |  a_n = (2/T)∫f cos nω_0t dt  |  b_n = (2/T)∫f sin nω_0t dt
A_n = √(a_n² + b_n²)
Even ⇒ b_n = 0. Odd ⇒ a_0 = a_n = 0. Half-wave ⇒ even harmonics vanish.
Square wave: (4A/π)[sin ω_0t + ⅓sin 3ω_0t + ⅕sin 5ω_0t + …]
P = V_dc I_dc + Σ(V_n I_n/2)cos θ_n
F_rms = √(F_dc² + Σ F_n²/2)  |  THD = √(Σ_{n≥2}F_n²)/F_1
F(ω) = ∫f(t)e^{−jωt}dt = F(s)|_{s=jω} for causal f
Narrow in time ⟺ wide in frequency

## Two-port networks
z: V_1 = z_11I_1 + z_12I_2, V_2 = z_21I_1 + z_22I_2 (open-circuit)
y = z⁻¹ (short-circuit)
h: V_1 = h_11I_1 + h_12V_2, I_2 = h_21I_1 + h_22V_2  (h_21 = transistor β)
ABCD: V_1 = AV_2 − BI_2, I_1 = CV_2 − DI_2
Reciprocal ⟺ z_12 = z_21 ⟺ AD − BC = 1; symmetric ⟺ z_11 = z_22 ⟺ A = D
Series ⇒ z adds. Parallel ⇒ y adds. Cascade ⇒ ABCD multiply.
Series Z: A=1, B=Z, C=0, D=1.  Shunt Y: A=1, B=0, C=Y, D=1.
Z_in = z_11 − z_12z_21/(z_22 + Z_L)

## Constants
ρ_copper = 1.72×10⁻⁸ Ω·m  |  ρ_aluminium = 2.82×10⁻⁸ Ω·m
e = 1.602×10⁻¹⁹ C
