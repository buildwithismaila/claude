# Week 9 — Continuity Equation and Surface Phenomena
<!-- group: Module 3 · Carrier Transport & Injection Phenomena -->

**Plan:** derivation and application of the minority-carrier continuity equation; semiconductor surface states and surface recombination velocity.

## Learning objectives

By the end of this week you should be able to:

1. Derive the continuity equation for holes and electrons.
2. Write and interpret the minority-carrier diffusion equation.
3. Solve the diffusion equation for the standard cases.
4. Calculate diffusion lengths and explain their importance.
5. Explain surface states and surface recombination velocity.
6. Calculate the effective lifetime of a wafer with recombining surfaces.

## Symbols and abbreviations used this week

Every symbol, constant and abbreviation on this page is listed here, even if an earlier week already defined it, so you can study this page on its own.

**Constants and units**

| Symbol | Meaning | Units / typical value |
|---|---|---|
| q | Magnitude of the electronic charge | 1.6×10⁻¹⁹ C |
| eV | Electron-volt, a unit of energy | 1 eV = 1.6×10⁻¹⁹ J |
| μm | Micrometre (micron) | 1 μm = 10⁻⁴ cm = 10⁻⁶ m |

**Symbols**

| Symbol | Meaning | Units / typical value |
|---|---|---|
| E_g | Band-gap energy, E_c − E_v | eV; Si 1.12, Ge 0.66, GaAs 1.42 at 300 K |
| n | Electron concentration (free electrons per cm³) | cm⁻³ |
| p | Hole concentration (holes per cm³) | cm⁻³ |
| N_D | Donor concentration | cm⁻³ |
| Δn, Δp | Excess electron and hole concentrations above equilibrium | cm⁻³ |
| D | Diffusion coefficient (dopants in a furnace, or carriers) | cm²/s |
| R_p | Projected range: average depth at which implanted ions stop | μm |
| μ, μ_n, μ_p | Mobility: drift velocity per unit field (electrons, holes) | cm²/(V·s); Si μ_n 1350, μ_p 480 |
| v_th | Thermal velocity of carriers | ≈ 10⁷ cm/s at 300 K |
| J, J_n, J_p | Current density (total, electrons, holes) | A/cm² |
| D_n, D_p | Diffusion coefficients of electrons and holes | cm²/s; Si 35 and 12.4 |
| G, G_L | Generation rate of electron–hole pairs (G_L: by light) | cm⁻³s⁻¹ |
| R | Recombination rate | cm⁻³s⁻¹ |
| U | Net recombination rate, R − G | cm⁻³s⁻¹ |
| τ, τ_n, τ_p | Minority-carrier lifetime (τ_eff: effective, including surfaces) | s; Si 1 ns – 1 ms |
| σ_n, σ_p | Capture cross-section of a trap for electrons, holes | cm² |
| L, L_n, L_p | Diffusion length √(Dτ): distance a minority carrier travels before recombining | μm or cm |
| S | Surface recombination velocity | cm/s |
| N_st | Density of surface traps | cm⁻² |
| U_s | Recombination rate per unit area at a surface | cm⁻²s⁻¹ |
| W | Depletion-region width (in Week 13 W_B, W_E are base and emitter widths; in Week 14 W is channel width) | μm or cm |
| x_n, x_p | Parts of the depletion region on the n side and on the p side | μm |
| A (area) | Device or contact area | cm² |
| N_E, W_E, D_E; N_B, W_B, D_B | Doping, width and minority diffusion coefficient of the emitter; of the base | cm⁻³; μm; cm²/s |
| G_th, R_th | Thermal generation and recombination rates (equal in equilibrium) | cm⁻³s⁻¹ |
| G_n, G_p, R_n, R_p | Generation and recombination rates of electrons and holes | cm⁻³s⁻¹ |
| τ_b (τ_bulk), τ_surface | Lifetime from bulk recombination only; from surface recombination only | s |
| U_s, p_s, Δp_s | Surface recombination rate; hole density and excess at the surface | cm⁻²s⁻¹; cm⁻³ |

**Abbreviations**

| Abbreviation | Meaning |
|---|---|
| Si | Silicon |
| SiO₂ | Silicon dioxide (silica), the oxide insulator |
| SRH | Shockley–Read–Hall (trap-assisted) recombination |
| MOS | Metal–oxide–semiconductor |
| MOSFET | Metal–oxide–semiconductor field-effect transistor |
| BJT | Bipolar junction transistor |
| TCAD | Technology computer-aided design (device simulation software) |


## Key terms

Every important word used this week is defined here, so you can read this week on its own.

**Band gap (E_g).** The range of energies between the top of the valence band and the bottom of the conduction band in which a perfect crystal has no allowed electron states. For silicon it is 1.12 eV at 300 K.

**Electron and hole.** An electron is a free negative charge carrier in the conduction band. A hole is an empty state left in the valence band when an electron leaves it; it moves like a positive charge carrier.

**Doping (n-type, p-type).** Adding small, controlled amounts of impurity atoms to a semiconductor. Donor atoms give electrons and make the material n-type; acceptor atoms take electrons, create holes and make it p-type.

**Majority and minority carriers.** In n-type material electrons are the majority carriers and holes the minority carriers; in p-type material it is the other way round. Minority carriers are few, but they control most device currents.

*Why it matters:* the continuity equation this week is almost always solved for the minority carriers.

**Excess carriers (Δn, Δp).** Carriers present above the equilibrium (dark, no-bias) number, for example created by light or injected by a junction.

    Δp = p − p_0

Where:

- Δp = excess hole concentration (cm⁻³)
- p = actual hole concentration (cm⁻³)
- p_0 = hole concentration in thermal equilibrium (cm⁻³)

**Low-level injection.** The condition in which the excess carrier density is much smaller than the majority-carrier density, so the majority density is hardly changed. It makes the recombination rate simply proportional to the excess, Δp/τ.

**Generation and recombination (G, R).** Generation is the creation of electron–hole pairs (by heat or light); recombination is their destruction when an electron drops back into a hole. Both are counted per cm³ per second.

**Trap (SRH recombination).** A defect or impurity with an energy level inside the band gap that captures an electron and then a hole, so that the pair recombines in two easy steps. This Shockley–Read–Hall process is the main recombination route in silicon.

**Minority-carrier lifetime (τ).** The average time an excess minority carrier survives before it recombines. In silicon it ranges from about 1 ns to 1 ms, depending on how many traps there are.

*Why it matters:* the lifetime, together with the diffusion coefficient, sets how far carriers travel and hence how much current a diode or transistor carries.

**Drift and diffusion.** The two ways carriers move. Drift is motion pushed by an electric field; diffusion is the spreading of carriers from where there are many to where there are few, with no field needed.

**Diffusion coefficient (D).** A measure of how quickly carriers spread out by diffusion, in cm²/s. For lightly doped silicon D_n ≈ 35 cm²/s and D_p ≈ 12 cm²/s.

**Continuity equation.** The book-keeping equation for carriers: in any small volume, the rate of change of the carrier density equals the net inflow carried by current, plus generation, minus recombination.

    ∂p/∂t = −(1/q) ∂J_p/∂x + G_p − R_p

Where:

- ∂p/∂t = rate of change of hole concentration with time (cm⁻³s⁻¹)
- q = electronic charge, 1.6×10⁻¹⁹ C
- J_p = hole current density (A/cm²); ∂J_p/∂x is its change with position x (cm)
- G_p, R_p = generation and recombination rates of holes (cm⁻³s⁻¹)

*Why it matters:* every diode and transistor current in this course comes from solving this equation.

**Minority-carrier diffusion equation.** The continuity equation written for minority carriers in a region with almost no electric field (a quasi-neutral region), using diffusion for the current and Δp/τ for the recombination.

**Diffusion length (L).** The average distance an excess minority carrier diffuses before it recombines.

    L_p = √(D_p τ_p)

Where:

- L_p = hole diffusion length (cm)
- D_p = hole diffusion coefficient (cm²/s)
- τ_p = hole lifetime (s)

*Why it matters:* a device region much shorter than L lets almost every carrier cross it; a region much longer than L loses most of them.

**Surface states (dangling bonds).** Energy levels inside the band gap located at a surface, caused mainly by surface atoms whose bonds point out into nothing (dangling bonds). They act as traps.

**Surface recombination velocity (S).** A measure, in cm/s, of how fast a surface destroys excess carriers: the recombination per unit area equals S times the excess density at the surface.

    U_s = S Δp(0)

Where:

- U_s = recombination rate per unit area of surface (cm⁻²s⁻¹)
- S = surface recombination velocity (cm/s)
- Δp(0) = excess minority density at the surface (cm⁻³)

*Why it matters:* a poor surface (large S) can destroy carriers faster than the whole bulk does.

**Effective lifetime (τ_eff).** The lifetime actually measured in a sample, which includes losses both in the bulk and at the surfaces. It is always shorter than the bulk lifetime.

**Passivation.** Treating a surface (for example growing an oxide or depositing a nitride film) so that its dangling bonds are tied up and S becomes small.

## The big picture

Weeks 7 and 8 gave us all the separate pieces: carriers **flow** (drift and diffusion), and carriers are **created and destroyed** (generation and recombination). The **continuity equation** puts the pieces together into one equation.

It is nothing more than **book-keeping**, like a bank account:

    change in balance = money in − money out + interest earned − charges paid

For carriers in a small slice of semiconductor:

    change in carriers = carriers flowing in − carriers flowing out + carriers generated − carriers recombined

Solve this equation and you know where the carriers are and how they change with time. That is how we will get the diode equation in Week 10 and the transistor currents in Week 13.

The second half of the week is about **surfaces**, where the crystal ends and carriers get lost much faster than inside.

## Deriving the continuity equation

Take a thin slice of semiconductor between x and x + dx, with cross-section area A. Count the holes in it. The number changes for three reasons:

1. **Flow.** Holes enter at x carried by the current J_p(x), and leave at x + dx carried by J_p(x + dx). Dividing a current by q turns it into a number of carriers per second, so the net inflow is [J_p(x) − J_p(x + dx)]A/q.
2. **Generation** inside the slice: G_p per cm³ per second, times the volume A dx.
3. **Recombination** inside the slice: R_p per cm³ per second, times A dx.

So:

    (rate of change of p) × A dx = [J_p(x) − J_p(x + dx)] A/q + (G_p − R_p) A dx

Divide by A dx. As dx → 0, [J_p(x) − J_p(x + dx)]/dx becomes −∂J_p/∂x:

    ∂p/∂t = −(1/q) ∂J_p/∂x + G_p − R_p

For electrons the sign of the flow term is opposite, because the electron charge is negative:

    ∂n/∂t = +(1/q) ∂J_n/∂x + G_n − R_n

Where:

- p, n = hole and electron concentrations (cm⁻³); t = time (s)
- q = electronic charge, 1.6×10⁻¹⁹ C
- J_p, J_n = hole and electron current densities (A/cm²); x = position (cm)
- G_p, G_n = generation rates of holes and electrons (cm⁻³s⁻¹)
- R_p, R_n = recombination rates of holes and electrons (cm⁻³s⁻¹)

**Reading it.** If more current flows into the slice than out of it (current decreasing with x), carriers pile up. If generation beats recombination, carriers build up. Otherwise they fall.

## The minority-carrier diffusion equation

Now apply it to the case that matters most: **holes as minority carriers in an n-type region**, with low-level injection.

- From Week 7, the hole current is J_p = qpμ_pE − qD_p ∂p/∂x.
- From Week 8, the net recombination is Δp/τ_p.
- In a neutral region of a device the field is small, so the drift term can usually be dropped.

Substituting gives the **minority-carrier diffusion equation**:

    ∂Δp/∂t = D_p ∂²Δp/∂x² − Δp/τ_p + G_L

Where:

- Δp = excess hole concentration (cm⁻³), a function of position x (cm) and time t (s)
- D_p = hole diffusion coefficient (cm²/s); about 12 cm²/s in lightly doped Si
- τ_p = hole (minority-carrier) lifetime (s)
- G_L = generation rate by external light (cm⁻³s⁻¹)

| Term | Meaning |
|---|---|
| ∂Δp/∂t | how fast the excess changes at this point |
| D_p ∂²Δp/∂x² | diffusion: carriers spread from where there are more to where there are fewer |
| −Δp/τ_p | recombination: excess carriers die off with lifetime τ_p |
| G_L | external generation, e.g. by light |

(If there is a field, add −μ_pE ∂Δp/∂x for drift.) For electrons in p-type: ∂Δn/∂t = D_n ∂²Δn/∂x² − Δn/τ_n + G_L.

### The four standard solutions

| Situation | Equation becomes | Solution |
|---|---|---|
| Uniform sample, light switched off at t = 0 | dΔp/dt = −Δp/τ_p | Δp(t) = Δp(0) e^{−t/τ_p} (exponential decay in time) |
| Uniform sample, steady light | 0 = G_L − Δp/τ_p | Δp = G_Lτ_p |
| Steady injection at x = 0 into a long sample | 0 = D_p d²Δp/dx² − Δp/τ_p | Δp(x) = Δp(0) e^{−x/L_p} (exponential decay in space) |
| Steady injection into a short sample, W ≪ L_p | d²Δp/dx² ≈ 0 | Δp(x) = Δp(0)(1 − x/W), a straight line |

(In the last row W is the length of the short sample, in cm.)

#### Example 9.1: steady illumination and decay after the light is switched off

**Question.** A uniform n-type silicon sample (N_D = 1×10¹⁶ cm⁻³) has a hole lifetime of 2 μs. It is illuminated uniformly so that light generates 1×10²⁰ electron–hole pairs per cm³ per second. Find the steady excess hole concentration, check that this is low-level injection, and find how long after the light is switched off the excess falls to 10 % of its steady value.

**Given:** τ_p = 2 μs = 2×10⁻⁶ s, G_L = 1×10²⁰ cm⁻³s⁻¹, N_D = 1×10¹⁶ cm⁻³ (so the electron density is about 10¹⁶ cm⁻³).

**Find:** Δp in the steady state; the time t at which Δp(t) = 0.1 Δp(0).

**Formula:** the first two rows of the table above (the sample is uniform, so there is no diffusion):

    Δp = G_L τ_p          (steady light)

    Δp(t) = Δp(0) e^{−t/τ_p}          (after switch-off)

**Solution.**

Step 1. Steady state:

    Δp = 1×10²⁰ × 2×10⁻⁶ = 2×10¹⁴ cm⁻³

Step 2. Low-level check: 2×10¹⁴ cm⁻³ is only 2 % of the electron density 10¹⁶ cm⁻³, so the injection is low-level and the simple Δp/τ_p recombination term is valid.

Step 3. Decay: set e^{−t/τ_p} = 0.1, so t = τ_p ln 10:

    t = 2×10⁻⁶ × 2.303 = 4.6×10⁻⁶ s

**Answer:** **Δp = 2×10¹⁴ cm⁻³** (low-level injection), and it falls to 10 % of this **4.6 μs** after the light is switched off.

**What this means:** the excess builds up until recombination (Δp/τ_p) exactly balances generation, so a longer lifetime gives a larger steady excess. Timing the decay after a light pulse is exactly how lifetime is measured (photoconductive decay): it takes about 2.3 lifetimes to fall by a factor of ten.

### The diffusion length

The third case introduces the **diffusion length**:

    L_p = √(D_p τ_p),     L_n = √(D_n τ_n)

Where:

- L_p, L_n = diffusion lengths of holes and electrons (cm; often quoted in μm)
- D_p, D_n = diffusion coefficients of holes and electrons (cm²/s)
- τ_p, τ_n = lifetimes of holes and electrons as minority carriers (s)

It is the average distance an injected minority carrier diffuses before it recombines. The excess falls to 1/e (37 %) at one diffusion length, and to under 1 % at five.

@fig figures/injection.svg | Steady-state profile when minority carriers are injected at x = 0 into a long n-type bar: an exponential decay with characteristic length L_p.

> **In plain words.** Inject carriers at one end of a bar and they spread out by diffusion, but they also keep dying by recombination. They spread a typical distance L_p before they die. The longer they live (τ) and the faster they spread (D), the further they get.

#### Example 9.2: diffusion length

**Question.** Holes are injected into n-type silicon in which D_p = 12 cm²/s and the hole lifetime is 1 μs. Calculate the hole diffusion length, and the fraction of the injected excess remaining 100 μm from the injection point.

**Given:** D_p = 12 cm²/s, τ_p = 1 μs = 1×10⁻⁶ s, x = 100 μm.

**Find:** L_p, and Δp(100 μm)/Δp(0).

**Formula:**

    L_p = √(D_pτ_p),     Δp(x) = Δp(0) e^{−x/L_p}

**Solution.**

Step 1. L_p = √(D_pτ_p) = √(12 × 10⁻⁶) = 3.46×10⁻³ cm = 34.6 μm

Step 2. Δp(x)/Δp(0) = e^{−x/L_p}:

    e^{−100/34.6} = e^{−2.89} = 0.056

**Answer:** **L_p = 34.6 μm**; only **5.6 %** of the excess survives 100 μm from the injection point.

**What this means:** a typical hole lives long enough to spread only about 35 μm, a third of the width of a human hair. A device region much thinner than this (such as a transistor base) is crossed by almost every carrier; a region several diffusion lengths long loses nearly all of them to recombination.

The hole current at the injection point comes from the slope of the profile there:

    J_p(0) = −qD_p dΔp/dx |₀ = qD_pΔp(0)/L_p

Where:

- J_p(0) = hole diffusion current density at the injection point (A/cm²)
- q = electronic charge, 1.6×10⁻¹⁹ C
- D_p = hole diffusion coefficient (cm²/s)
- Δp(0) = excess hole concentration at the injection point (cm⁻³)
- L_p = hole diffusion length (cm)

This is exactly the formula that, applied at the edge of a junction, gives the Shockley diode equation (Week 10). The fourth case (straight-line profile in a short region) is what happens in a transistor's thin base (Week 13).

### Where the continuity equation is used

- **Diodes:** the exponential profile in each neutral region gives the diode current (Week 10).
- **Bipolar transistors:** the straight-line profile in the thin base gives the collector current and the gain (Week 13).
- **Measuring lifetime:** the exponential decay after a light pulse (photoconductive decay) gives τ directly.
- **Haynes–Shockley experiment:** a pulse of carriers drifts and spreads; timing it gives μ, D and τ.
- **Solar cells and photodiodes:** with generation G_L(x) = G₀e^{−αx}, the solution gives how many carriers are collected.
- **Device simulators** solve these equations numerically for every chip design.

## Surfaces and surface states

### Why surfaces are special

Inside the crystal, every silicon atom is bonded to four neighbours. At a surface the crystal simply stops: the surface atoms have bonds pointing out into nothing, called **dangling bonds**. Adsorbed impurities and defects in any oxide on top add more problems.

These create a high density of **surface states**: energy levels inside the band gap, located at the surface (typically 10¹⁰–10¹⁵ per cm²). They:

- act as **SRH traps** (Week 8), so carriers recombine much faster at the surface than in the bulk;
- **trap charge**, which bends the bands near the surface even with no voltage applied;
- cause noise and instability, and shift the threshold voltage in MOSFETs.

### Surface recombination velocity

Recombination at a surface happens in an extremely thin layer, so it is counted **per unit area**, not per unit volume:

    U_s = S × Δp(0)      [carriers per cm² per second]

Where:

- U_s = recombination rate per unit area of surface (cm⁻²s⁻¹)
- S = **surface recombination velocity** (cm/s)
- Δp(0) = excess minority (here hole) concentration at the surface (cm⁻³)

> **In plain words.** Imagine the excess carriers near the surface rushing into it at speed S and vanishing. A surface with S = 100 cm/s swallows carriers as fast as if they flowed into a drain at 100 cm/s. A perfect surface has S = 0; a surface that destroys every carrier that reaches it has S → ∞.

For surface traps of density N_st (per cm²):

    S = σ_p v_th N_st

Where:

- S = surface recombination velocity (cm/s)
- σ_p = capture cross-section of a surface trap for holes (cm²); typically about 10⁻¹⁵ cm²
- v_th = thermal velocity of carriers, about 10⁷ cm/s at 300 K
- N_st = density of surface traps (cm⁻²)

It enters the diffusion equation as a **boundary condition**: the carriers arriving at the surface by diffusion must equal the carriers recombining there,

    D_p dΔp/dx |surface = S Δp(0)

Where:

- D_p dΔp/dx |surface = diffusion flow of holes towards the surface, per cm² per second (D_p in cm²/s, dΔp/dx in cm⁻⁴)
- S Δp(0) = rate at which they recombine at the surface (cm⁻²s⁻¹)

#### Example 9.3: surface recombination velocity from the trap density

**Question.** A silicon surface has surface traps with a hole capture cross-section of 1×10⁻¹⁵ cm². Find the surface recombination velocity (a) for a well-oxidised surface with 1×10¹⁰ traps per cm², and (b) for a bare surface with 1×10¹³ traps per cm². For case (a), find the recombination rate per cm² if the excess hole concentration at the surface is 1×10¹³ cm⁻³.

**Given:** σ_p = 1×10⁻¹⁵ cm², v_th = 1×10⁷ cm/s, N_st = 10¹⁰ cm⁻² (a) and 10¹³ cm⁻² (b), Δp(0) = 1×10¹³ cm⁻³.

**Find:** S in each case; U_s for case (a).

**Formula:**

    S = σ_p v_th N_st,     U_s = S Δp(0)

**Solution.**

Step 1. Oxidised surface:

    S = 1×10⁻¹⁵ × 1×10⁷ × 1×10¹⁰ = 100 cm/s

Step 2. Bare surface:

    S = 1×10⁻¹⁵ × 1×10⁷ × 1×10¹³ = 1×10⁵ cm/s

Step 3. Recombination rate at the oxidised surface:

    U_s = 100 × 1×10¹³ = 1×10¹⁵ cm⁻²s⁻¹

**Answer:** **S = 100 cm/s for the oxidised surface and 1×10⁵ cm/s for the bare surface**; at the oxidised surface **U_s = 1×10¹⁵ carriers per cm² per second**.

**What this means:** S is simply proportional to the number of surface traps, so cutting the trap density a thousandfold by growing a good oxide cuts the surface loss a thousandfold. These two values match the "thermally oxidised" and "bare" rows of the table below.

| Surface | Typical S (cm/s) |
|---|---|
| Bare or freshly etched Si | 10⁴ – 10⁶ |
| Thermally oxidised Si | 10 – 100 |
| Best passivated Si (Al₂O₃, SiNₓ, annealed SiO₂) | below 10 |
| Ohmic metal contact | → ∞ (Δp forced to 0) |

### How surfaces shorten the lifetime

In a wafer of thickness W with both surfaces recombining, the measured (effective) lifetime combines bulk and surface losses:

    1/τ_eff = 1/τ_bulk + 2S/W          (for small S: SW/2D ≪ 1)

Where:

- τ_eff = effective (measured) lifetime of the wafer (s)
- τ_bulk = lifetime set by recombination in the bulk alone (s)
- S = surface recombination velocity, the same on both faces (cm/s)
- W = wafer thickness (cm)

The term 2S/W is 1/τ_surface: two surfaces, each removing carriers at speed S, shared over a thickness W.

**The diffusion limit.** The simple formula assumes carriers reach the surfaces easily, so the excess is almost uniform through the wafer. That is true only while SW/2D ≪ 1 (D is the minority-carrier diffusion coefficient). If S is very large, the surfaces swallow carriers faster than diffusion can bring them, and the loss is limited by the time carriers take to diffuse to a surface. A good approximation covering both cases is:

    τ_surface ≈ W/(2S) + W²/(π²D),     1/τ_eff = 1/τ_bulk + 1/τ_surface

Where:

- τ_surface = lifetime set by surface recombination alone (s)
- W/(2S) = time for the surfaces to remove the carriers once they arrive (s)
- W²/(π²D) = time for carriers to diffuse to the surfaces (s); it is the shortest τ_surface can ever be
- D = minority-carrier diffusion coefficient (cm²/s)

For small S the first term dominates and this reduces to 1/τ_surface = 2S/W.

#### Example 9.4: how surfaces reduce the lifetime

**Question.** An n-type silicon wafer 300 μm thick has a bulk lifetime of 100 μs and a hole diffusion coefficient of 12 cm²/s. Both surfaces are oxidised, giving a surface recombination velocity of 100 cm/s. Calculate the effective lifetime. Repeat for unprotected surfaces with S = 10⁵ cm/s.

**Given:** τ_bulk = 100 μs = 1×10⁻⁴ s, W = 300 μm = 0.03 cm, D_p = 12 cm²/s, S = 100 cm/s (then 10⁵ cm/s).

**Find:** τ_eff in each case.

**Formula:**

    1/τ_eff = 1/τ_bulk + 2S/W          (valid when SW/2D ≪ 1)

    τ_surface ≈ W/(2S) + W²/(π²D),     1/τ_eff = 1/τ_bulk + 1/τ_surface          (any S)

**Solution.**

Step 1. Oxidised surfaces. Check: SW/2D = 100 × 0.03/24 = 0.13, small, so the simple formula applies.

    2S/W = 2 × 100/0.03 = 6.7×10³ s⁻¹,   1/τ_bulk = 1×10⁴ s⁻¹

    1/τ_eff = 1.67×10⁴ s⁻¹   ⇒   τ_eff = 60 μs

Step 2. Bare surfaces. Check: SW/2D = 10⁵ × 0.03/24 = 125, not small, so the simple formula would give a wrong answer (it predicts 0.15 μs). Use the full form:

    W/(2S) = 0.03/(2 × 10⁵) = 1.5×10⁻⁷ s = 0.15 μs

    W²/(π²D) = (0.03)²/(9.87 × 12) = 7.6×10⁻⁶ s = 7.6 μs

    τ_surface ≈ 0.15 + 7.6 = 7.75 μs

    1/τ_eff = 1/100 μs + 1/7.75 μs   ⇒   τ_eff ≈ 7.2 μs

**Answer:** **τ_eff = 60 μs with oxidised surfaces, but only about 7.2 μs with bare surfaces.**

**What this means:** with a good oxide the wafer keeps most of its bulk lifetime, but with bare surfaces the surfaces, not the bulk, control the lifetime. Once S is this large, making the surface even worse hardly matters: the loss is limited by how fast holes can diffuse 150 μm to the nearest surface.

**Reducing surface recombination (passivation):** grow thermal SiO₂ and anneal in hydrogen to tie up dangling bonds; deposit silicon nitride or aluminium oxide; add a heavily doped surface layer that repels minority carriers (a "back-surface field" in solar cells); and keep surfaces clean and damage-free.

### Bulk and surface recombination compared

| | Bulk recombination | Surface recombination |
|---|---|---|
| Where it happens | Throughout the volume of the crystal | In a very thin layer at the surface |
| Cause | Traps from impurities and crystal defects (SRH), plus band-to-band and Auger processes | Surface states, mainly dangling bonds, adsorbed impurities and oxide defects |
| How it is counted | Rate per unit volume, Δp/τ_bulk (cm⁻³s⁻¹) | Rate per unit area, U_s = SΔp(0) (cm⁻²s⁻¹) |
| Key parameter | Bulk lifetime τ_bulk (s) | Surface recombination velocity S (cm/s) |
| Where it enters the equations | The −Δp/τ_p term of the diffusion equation | A boundary condition: D_p dΔp/dx = SΔp(0) at the surface |
| Most important when | Thick devices, poor-quality or contaminated crystal | Thin wafers, small devices, light absorbed near the surface |
| How it is reduced | Purer crystal, gettering of impurities, fewer defects | Passivation: thermal oxide with H₂ anneal, SiNₓ or Al₂O₃ films, back-surface field |

## Key points of Week 9

- Continuity equation = carrier book-keeping: ∂p/∂t = −(1/q)∂J_p/∂x + G − R.
- Minority-carrier diffusion equation: ∂Δp/∂t = D_p∂²Δp/∂x² − Δp/τ_p + G_L.
- Standard solutions: decay in time e^{−t/τ}; steady light Δp = G_Lτ; long bar e^{−x/L}; short region a straight line.
- Diffusion length L = √(Dτ): how far a minority carrier travels before recombining.
- Surfaces have dangling bonds → surface states → fast recombination, measured by S (cm/s).
- 1/τ_eff = 1/τ_bulk + 2S/W for small S; for very large S the loss is limited by diffusion to the surfaces (τ_surface cannot fall below W²/π²D). Passivation keeps S small.

---

## Examination questions solved (Q45–Q46)

### Q45. Explain the continuity equation for minority carriers and discuss its application to semiconductor devices.

**Statement.** The continuity equation expresses conservation of carriers: in any small volume, the rate of increase of carrier concentration equals the net inflow due to current, plus generation, minus recombination.

    ∂p/∂t = −(1/q) ∂J_p/∂x + G_p − R_p      (holes)
    ∂n/∂t = +(1/q) ∂J_n/∂x + G_n − R_n      (electrons)

**Derivation.** For a slab of area A and thickness dx, the number of holes increases at the rate (1/q)[J_p(x) − J_p(x + dx)]A from current flow and at (G_p − R_p)A dx from generation and recombination. Dividing by A dx and taking the limit gives the equations above.

**Minority-carrier form.** For holes in an n-type region, substitute the hole current J_p = qμ_ppE − qD_p ∂p/∂x and, for low-level injection, the recombination rate R_p − G_th = Δp/τ_p. With uniform doping:

    ∂Δp/∂t = D_p ∂²Δp/∂x² − μ_pE ∂Δp/∂x − μ_p p ∂E/∂x + G_L − Δp/τ_p

In a quasi-neutral region E ≈ 0, giving the **ambipolar / minority-carrier diffusion equation**:

    ∂Δp/∂t = D_p ∂²Δp/∂x² − Δp/τ_p + G_L

For electrons in p-type material: ∂Δn/∂t = D_n ∂²Δn/∂x² − Δn/τ_n + G_L.

**Applications:**

1. **p-n junction diode.** In the neutral regions under steady forward bias, 0 = D_p d²Δp/dx² − Δp/τ_p gives Δp(x) = Δp(x_n)e^{−(x − x_n)/L_p}. The diffusion current at the depletion edge leads directly to the Shockley diode equation (Week 10).
2. **Bipolar transistor.** In a narrow base (W_B ≪ L_n), solving the equation gives a nearly linear minority-carrier profile; the slope gives collector current, and the small recombination loss gives the base transport factor and current gain.
3. **Photoconductive decay and lifetime measurement.** For uniform illumination switched off at t = 0, Δp(t) = Δp(0)e^{−t/τ_p}; measuring the decay of conductivity gives τ.
4. **Haynes–Shockley experiment.** A pulse of minority carriers drifts and spreads; the time-dependent solution, a moving and broadening Gaussian, gives μ_p, D_p and τ_p and was used to verify the Einstein relation.
5. **Solar cells and photodiodes.** With G_L(x) = G₀e^{−αx}, the solution gives the collection efficiency and photocurrent and shows why the diffusion length must exceed the absorption depth.
6. **Switching transients.** The time-dependent equation gives stored charge and the reverse-recovery time of diodes.
7. **Device simulation.** Together with Poisson's equation and the current equations, the continuity equations are solved numerically in every TCAD simulator.

### Q46. What is surface recombination velocity? Explain how semiconductor surface states affect carrier lifetime.

**Surface recombination velocity.** At a semiconductor surface, recombination happens in a very thin layer through surface states. It is described per unit area as

    U_s = S · Δp_s      (cm⁻² s⁻¹)

where Δp_s is the excess minority-carrier density at the surface and **S is the surface recombination velocity** (cm/s). It is the effective velocity at which excess carriers move into the surface and are annihilated. For surface traps of density N_st (cm⁻²) with capture cross-section σ_p:

    S = σ_p v_th N_st

S enters the boundary condition for the diffusion equation: D_p dΔp/dx = SΔp at the surface. S = 0 means an ideal surface; S → ∞ means every carrier arriving recombines (Δp_s = 0, like an Ohmic contact). Typical values: unpassivated Si 10⁴–10⁶ cm/s; thermally oxidised Si 10–10³ cm/s; well-passivated Si < 10 cm/s.

**Surface states.** The crystal periodicity ends at the surface, leaving unsaturated (dangling) bonds, as well as adsorbed atoms, oxide defects and contamination. These produce a high density of localised energy levels distributed throughout the band gap, many near mid-gap.

**How they affect lifetime:**

1. **Additional recombination path.** Mid-gap surface states are efficient SRH centres. Carriers that diffuse to the surface recombine there quickly, so the measured (effective) lifetime is lower than the bulk lifetime: 1/τ_eff = 1/τ_bulk + 1/τ_surface, with 1/τ_surface ≈ 2S/W for a wafer of thickness W recombining at both surfaces (valid while SW/2D ≪ 1; for very large S, τ_surface ≈ W/2S + W²/π²D, limited by diffusion to the surfaces). In thin wafers and small devices surface recombination can dominate: a 300 μm n-type wafer with τ_bulk = 100 μs falls to τ_eff ≈ 60 μs at S = 100 cm/s and to about 7 μs at S = 10⁵ cm/s (Example 9.4).
2. **Carrier depletion near the surface.** The excess carrier density falls towards the surface, creating a gradient that pulls more carriers there, so even carriers generated deep in the material are lost.
3. **Surface band bending.** Charge in surface states bends the bands, creating depletion or inversion layers. Under depletion, both electrons and holes are present in similar numbers near the surface, which maximises SRH recombination and generation.
4. **Leakage and noise.** Surface generation adds to reverse leakage current of junctions where they meet the surface; trapping and detrapping produces 1/f noise; charged states cause threshold-voltage drift and instability in MOS devices.
5. **Device performance.** High S reduces solar-cell efficiency (especially for blue light absorbed near the surface), reduces BJT current gain (surface recombination at the emitter–base perimeter), and degrades photodetector response.

**Reduction (passivation):** thermal oxidation (SiO₂) with forming-gas (H₂) anneal to tie up dangling bonds; silicon nitride and Al₂O₃ films with fixed charge for field-effect passivation; heavily doped surface layers (back-surface field) that repel minority carriers; and clean, damage-free surface preparation.

---

## Practice questions

These extra questions practise this week's ideas. Work each one on paper before reading the solution; the calculation questions follow the same Question, Given, Find, Solution, Answer layout as the worked examples.

#### Practice 9.1: electron diffusion length

**Question.** Electrons in p-type silicon have D_n = 25 cm²/s and τ_n = 10 μs. Find the diffusion length.

**Given:** D_n = 25 cm²/s, τ_n = 10⁻⁵ s.

**Find:** L_n.

**Solution.**

    L_n = √(D_nτ_n) = √(25 × 10⁻⁵) = 1.58×10⁻² cm = 158 μm

**Answer:** **L_n ≈ 160 μm.**

**What this means:** electrons in this p-type material survive long enough to cross a region about 0.16 mm thick, so a p-type layer a few micrometres thick loses almost none of them.

#### Practice 9.2: injected profile and current

**Question.** Holes are injected at x = 0 into a long n-type bar with Δp(0) = 1×10¹⁴ cm⁻³, D_p = 12 cm²/s and L_p = 30 μm. Find the hole current density at x = 0 and the excess hole concentration at x = 60 μm.

**Given:** Δp(0) = 10¹⁴ cm⁻³, D_p = 12 cm²/s, L_p = 3×10⁻³ cm.

**Find:** J_p(0) and Δp(60 μm).

**Solution.**

    J_p(0) = qD_pΔp(0)/L_p = 1.6×10⁻¹⁹ × 12 × 10¹⁴ / 3×10⁻³ = 0.064 A/cm²
    Δp(60 μm) = Δp(0) e^{−60/30} = 10¹⁴ × e^{−2} = 1.35×10¹³ cm⁻³

**Answer:** **J_p(0) = 64 mA/cm², Δp(60 μm) = 1.35×10¹³ cm⁻³.**

#### Practice 9.3: diffusion across a short region

**Question.** Electrons are injected into a p-type region only 2 μm wide (much shorter than L_n), with Δn = 1×10¹⁵ cm⁻³ at one side and Δn = 0 at the other. Find the electron current density (D_n = 25 cm²/s).

**Given:** W = 2×10⁻⁴ cm, Δn(0) = 10¹⁵ cm⁻³, Δn(W) = 0, D_n = 25 cm²/s.

**Find:** J_n.

**Solution.** In a short region the profile is a straight line, so the gradient is Δn(0)/W:

    J_n = qD_nΔn(0)/W = 1.6×10⁻¹⁹ × 25 × 10¹⁵ / 2×10⁻⁴ = 20 A/cm²

**Answer:** **J_n = 20 A/cm².** This is exactly the situation in a BJT base (Week 13).

#### Practice 9.4: how good must the surface be?

**Question.** A 200 μm thick wafer has a bulk lifetime of 200 μs. What surface recombination velocity can be tolerated if the effective lifetime must be at least 50 μs?

**Given:** τ_bulk = 2×10⁻⁴ s, τ_eff = 5×10⁻⁵ s, W = 0.02 cm.

**Find:** S.

**Solution.**

    2S/W = 1/τ_eff − 1/τ_bulk = 2×10⁴ − 5×10³ = 1.5×10⁴ s⁻¹
    S = 1.5×10⁴ × 0.02 / 2 = 150 cm/s

**Answer:** **S ≤ 150 cm/s**, achievable with a good thermal oxide.

**What this means:** for silicon (D ≈ 12–35 cm²/s), SW/2D = 150 × 0.02/(2D) is at most about 0.13, so the simple formula is valid here. Even a "good" surface takes away three quarters of the lifetime of a 200 μm wafer.

#### Practice 9.5: surface recombination current

**Question.** At a surface with S = 1000 cm/s the excess hole concentration is 1×10¹³ cm⁻³. Find the recombination rate per unit area and the equivalent current density lost to the surface.

**Given:** S = 10³ cm/s, Δp_s = 10¹³ cm⁻³.

**Find:** U_s and J = qU_s.

**Solution.**

    U_s = SΔp_s = 10³ × 10¹³ = 10¹⁶ cm⁻²s⁻¹
    J = qU_s = 1.6×10⁻¹⁹ × 10¹⁶ = 1.6×10⁻³ A/cm²

**Answer:** **U_s = 10¹⁶ cm⁻²s⁻¹, J = 1.6 mA/cm².**

#### Practice 9.6: no recombination

**Question.** What does the steady-state minority-carrier profile look like if the lifetime is infinite (no recombination) and there is no field or generation? Why?

**Answer.** The diffusion equation reduces to D_p d²Δp/dx² = 0, so the second derivative is zero and **Δp is a straight line**. With no recombination, every carrier that enters a slice must leave it, so the current, and hence the slope, is the same everywhere.

---

## Objectives check

Use this table to confirm you have met this week's objectives. Cover the Answer column and answer each check question from memory. If you cannot, go back to the section in the last column before moving on.

| # | Objective | Check yourself | Answer | Where it is taught |
|---|---|---|---|---|
| 1 | Derive the continuity equation for holes and electrons. | Write the continuity equation for holes. | ∂p/∂t = −(1/q)∂J_p/∂x + G_p − R_p. | Deriving the continuity equation |
| 2 | Write and interpret the minority-carrier diffusion equation. | What does the term −Δp/τ_p represent? | Loss of excess holes by recombination. | The minority-carrier diffusion equation |
| 3 | Solve the diffusion equation for the standard cases. | What is the steady-state profile for injection into a long bar? | Δp(x) = Δp(0)e^{−x/L_p}. | The four standard solutions; Example 9.1 |
| 4 | Calculate diffusion lengths and explain their importance. | Find L_n for D_n = 30 cm²/s, τ_n = 10 μs. | L_n = √(30 × 10⁻⁵) = 1.7×10⁻² cm = 173 μm. | Diffusion length; Example 9.2 |
| 5 | Explain surface states and surface recombination velocity. | What value of S corresponds to an Ohmic metal contact? | S → ∞ (Δp forced to zero). | Surfaces and surface states; Example 9.3 |
| 6 | Calculate the effective lifetime of a wafer with recombining surfaces. | Write 1/τ_eff for a wafer of thickness W (small S). | 1/τ_eff = 1/τ_bulk + 2S/W, valid while SW/2D ≪ 1. | How surfaces shorten the lifetime; Example 9.4 |
