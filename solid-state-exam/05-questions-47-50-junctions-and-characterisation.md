# Questions 47–50 — Junctions, Interfaces and Characterisation
<!-- group: The 50 questions, answered -->

Module 4: the p-n junction and its diode equation, metal–semiconductor contacts, and how devices are measured with I-V and C-V characterisation. These are long questions: practise writing them in full. Each question stands on its own: its key terms are defined with it, so you can start anywhere.

## Symbols and abbreviations used on this page

Every symbol, constant and abbreviation on this page is listed here, even if another page already defined it, so you can study this page on its own.

**Constants and units**

| Symbol | Meaning | Units / typical value |
|---|---|---|
| q | Magnitude of the electronic charge | 1.6×10⁻¹⁹ C |
| k | Boltzmann constant | 8.617×10⁻⁵ eV/K = 1.381×10⁻²³ J/K |
| kT | Thermal energy | 0.0259 eV (often 0.02585 eV) at 300 K |
| kT/q | Thermal voltage | 0.0259 V (about 26 mV) at 300 K |
| T | Absolute temperature | kelvin (K); room temperature = 300 K |
| ε_s (ε_si) | Permittivity of silicon, 11.7ε₀ | 1.04×10⁻¹⁰ F/m |
| eV | Electron-volt, a unit of energy | 1 eV = 1.6×10⁻¹⁹ J |
| μm | Micrometre (micron) | 1 μm = 10⁻⁶ m |

**Symbols**

| Symbol | Meaning | Units / typical value |
|---|---|---|
| E_c (E_C) | Energy of the bottom of the conduction band | eV |
| E_v (E_V) | Energy of the top of the valence band | eV |
| E_g | Band-gap energy, E_c − E_v | eV; Si 1.12, Ge 0.66, GaAs 1.42 at 300 K |
| E_F | Fermi level: the energy at which a state has a 50 % chance of being occupied | eV |
| E_i | Intrinsic Fermi level, close to mid-gap | eV |
| N_c | Effective density of states in the conduction band | m⁻³; Si 2.8×10²⁵ at 300 K |
| N_v | Effective density of states in the valence band | m⁻³; Si 1.04×10²⁵ at 300 K |
| n | Electron concentration (free electrons per m³) | m⁻³ |
| p | Hole concentration (holes per m³) | m⁻³ |
| n_i | Intrinsic carrier concentration (n = p = n_i in pure material) | m⁻³; Si ≈ 1×10¹⁶ at 300 K |
| p_n0, n_p0 | Equilibrium minority concentrations: holes on the n side, electrons on the p side | m⁻³; p_n0 = n_i²/N_D |
| N_D | Donor concentration | m⁻³ |
| N_A | Acceptor concentration | m⁻³ |
| N_D⁺, N_A⁻ | Concentrations of ionised donors and acceptors | m⁻³ |
| Δn, Δp | Excess electron and hole concentrations above equilibrium | m⁻³ |
| C(x, t) | Dopant concentration at depth x and time t | m⁻³ |
| R_s | Sheet resistance (or diode series resistance in Week 12) | Ω/□ (ohms per square); Ω |
| E (field) | Electric field (on band diagrams, E is energy instead) | V/m |
| μ, μ_n, μ_p | Mobility: drift velocity per unit field (electrons, holes) | m²/(V·s); Si μ_n 0.135, μ_p 0.048 |
| J, J_n, J_p | Current density (total, electrons, holes) | A/m² |
| D_n, D_p | Diffusion coefficients of electrons and holes | m²/s; Si 3.5×10⁻³ and 1.24×10⁻³ |
| G, G_L | Generation rate of electron–hole pairs (G_L: by light) | m⁻³s⁻¹ |
| τ, τ_n, τ_p | Minority-carrier lifetime (τ_eff: effective, including surfaces) | s; Si 1 ns – 1 ms |
| L, L_n, L_p | Diffusion length √(Dτ): distance a minority carrier travels before recombining | μm or m |
| V_bi | Built-in potential of a junction or Schottky contact | V; typically 0.5–1 V |
| V, V_a | Applied voltage (positive for forward bias) | V |
| W | Depletion-region width (in Week 13 W_B, W_E are base and emitter widths; in Week 14 W is channel width) | μm or m |
| x_n, x_p | Parts of the depletion region on the n side and on the p side | μm |
| E_max | Peak electric field, at the junction | V/m |
| I_s, J_s (I_S) | Saturation current (density) of a diode or transistor | A; A/m² |
| I | Current | A |
| A (area) | Device or contact area | m² |
| η | Ideality factor of a diode, 1 (ideal) to 2 | dimensionless |
| C, C_j | Capacitance (junction or depletion capacitance) | F (pF = 10⁻¹² F) |
| Φ_m | Work function of a metal | eV; Al 4.28, Au 5.1 |
| Φ_s | Work function of a semiconductor, χ + (E_c − E_F) | eV |
| χ | Electron affinity: energy from E_c up to the vacuum level | eV; Si 4.05 |
| Φ_B | Schottky barrier height seen from the metal | eV (or V) |
| A∗∗ | Effective Richardson constant | A/(m²·K²); n-Si ≈ 1.1×10⁶ |
| ρ_c | Specific contact resistance | Ω·m² |
| E_vac | Vacuum level: energy of an electron just free of the material | eV |
| n_n0, p_p0, p_n0, n_p0 | Equilibrium densities: majority (n_n0, p_p0) and minority (p_n0 holes on n side, n_p0 electrons on p side) | m⁻³ |
| Δp_n, Δn_p | Excess minority carriers at the depletion edges (holes on n side, electrons on p side) | m⁻³ |
| R_c | Contact resistance | Ω (specific: Ω·m²) |
| Φ_Bn, Φ_Bp | Schottky barrier height for electrons (n-type) and for holes (p-type) | eV |
| p_n, n_p | Minority-carrier density: holes on the n side, electrons on the p side | m⁻³ |
| N(x), N(W) | Doping concentration at depth x (or at the depletion edge W), from C-V profiling | m⁻³ |
| t | Time (or a thickness, where the text says so) | s (or m) |

**Abbreviations**

| Abbreviation | Meaning |
|---|---|
| Si | Silicon |
| Ge | Germanium |
| GaAs | Gallium arsenide |
| I-V | Current–voltage (measurement or characteristic) |
| C-V | Capacitance–voltage (measurement or characteristic) |
| LCR | Inductance–capacitance–resistance meter |
| MOSFET | Metal–oxide–semiconductor field-effect transistor |
| MESFET | Metal–semiconductor field-effect transistor |
| BJT | Bipolar junction transistor |
| RF | Radio frequency |
| DC | Direct current (steady) |
| AC | Alternating current (small signal) |
| n⁺ | Very heavily doped n-type (similarly p⁺) |


## Questions on this page

| Q | Question |
|---|---|
| 47 | Explain the formation of the depletion region and built-in potential in a p-n junction. |
| 48 | Derive the ideal Shockley diode equation and explain the effect of forward and reverse bias. |
| 49 | Differentiate between a Schottky barrier diode and an Ohmic contact. Explain their energy-band characteristics. |
| 50 | Explain the principles of I-V and C-V characterisation of semiconductor devices and describe how C-V measurements can be used to estimate doping concentration. |

## Model answers

### Q47. Explain the formation of the depletion region and built-in potential in a p-n junction.

> **Question type:** Explanation · **Topic:** p-n junction electrostatics · **Full notes:** Week 10 (The p-n Junction Diode)

**What the examiner wants.** "Explain" means give the physical cause-and-effect chain: diffusion, uncovered ions, field, drift that opposes diffusion, equilibrium with a flat Fermi level. Then state what the built-in potential is, derive its formula from the Fermi-level positions, and back it up with a labelled sketch and a typical number.

**Key terms.**

- **p-n junction:** the boundary between a p-type and an n-type region in one continuous crystal.
- **Acceptor and donor ions (N_A⁻, N_D⁺):** dopant atoms that have taken or given up an electron; they are charged and fixed in the lattice, so they cannot move.
- **Diffusion:** movement of carriers from where they are many to where they are few.
- **Drift:** movement of carriers pushed by an electric field.
- **Depletion region (space-charge region), width W:** the layer around the junction emptied of mobile carriers, containing only fixed ion charge.
- **Fermi level (E_F):** the energy at which a state has a 50 % chance of being occupied; in equilibrium it is flat (the same) throughout a connected system.
- **Built-in potential (V_bi):** the voltage across the depletion region in equilibrium; the barrier majority carriers must climb to cross the junction.
- **Intrinsic carrier concentration (n_i):** carrier density of pure silicon, 1×10¹⁶ m⁻³ at 300 K.

**Model answer.**

**1. Before equilibrium: diffusion.** When p-type silicon (holes p ≈ N_A) and n-type silicon (electrons n ≈ N_D) are formed in one crystal, there is a huge concentration difference across the boundary. Holes therefore diffuse from the p side into the n side, and electrons diffuse from the n side into the p side. Carriers that cross recombine with the majority carriers on the other side and disappear.

**2. Fixed charge is uncovered.** Each hole that leaves the p side leaves behind a negative acceptor ion; each electron that leaves the n side leaves behind a positive donor ion. These ions are locked in the lattice. A layer next to the junction is therefore stripped of mobile carriers and holds only fixed charge: **negative on the p side, positive on the n side**. This is the **depletion region**.

**3. Charge balance.** The two layers carry equal and opposite charge:

    N_A x_p = N_D x_n

Where:

- N_A, N_D = acceptor and donor concentrations (m⁻³)
- x_p, x_n = depth of the depletion region on the p side and on the n side (m)

So the region extends further into the **more lightly doped** side.

**4. A field builds up and drift opposes diffusion.** The positive and negative charge layers create an electric field pointing from the n side to the p side, largest at the junction. This field drives holes back to p and electrons back to n (a drift current), opposite to the diffusion current.

**5. Equilibrium.** The depletion region grows until, for holes and for electrons separately, drift exactly cancels diffusion. The net current is zero and the Fermi level is one flat line through the whole structure.

**6. The built-in potential.** The field across the depletion region corresponds to a potential difference V_bi, with the n side positive relative to the p side. In the band diagram the bands on the p side sit higher by qV_bi, a barrier that holds back the majority carriers. Because E_F must be flat, the bands bend by the sum of the Fermi-level offsets from the intrinsic level E_i on the two sides:

    qV_bi = kT ln(N_A/n_i) + kT ln(N_D/n_i)

    V_bi = (kT/q) ln( N_{A}N_D / n_i² )

Where:

- V_bi = built-in potential (V)
- q = electronic charge, 1.6×10⁻¹⁹ C
- kT = thermal energy, 0.0259 eV at 300 K, so kT/q = 0.0259 V
- N_A, N_D = acceptor and donor concentrations (m⁻³)
- n_i = intrinsic carrier concentration, 1×10¹⁶ m⁻³ for Si at 300 K

@fig figures/pn-junction.svg | Abrupt p-n junction in equilibrium: fixed negative and positive ion charge either side of the junction, the triangular field peaking at the junction, and bands bent by qV_bi under a flat Fermi level.

Sketch in the exam: three stacked graphs against x. (a) Charge density: a negative block of height qN_A from −x_p to 0, a positive block of height qN_D from 0 to x_n. (b) Field: a triangle, zero at both edges, peak E_max at x = 0. (c) Band diagram: E_c and E_v higher on the p side by qV_bi, a flat dashed E_F. Label W, x_p, x_n, qV_bi.

**7. Width and field (depletion approximation: no free carriers inside W, neutral outside).**

    W = x_n + x_p = √( (2ε_s/q) V_bi (1/N_A + 1/N_D) ),     E_max = qN_D x_n/ε_s

Where:

- W = total depletion width (m)
- ε_s = permittivity of silicon, 1.04×10⁻¹⁰ F/m
- E_max = peak electric field, at the junction (V/m)
- other symbols as above

**Typical numbers (Si, N_A = 10²³ m⁻³, N_D = 10²² m⁻³, 300 K):** V_bi = 0.0259 × ln(10²³ × 10²²/10³²) = 0.0259 × ln(10¹³) = **0.775 V**; W = √((2 × 1.04×10⁻¹⁰/1.6×10⁻¹⁹) × 0.775 × (10⁻²³ + 10⁻²²)) = **3.3×10⁻⁷ m (0.33 μm)** (3.0×10⁻⁷ m on the n side, 3.0×10⁻⁸ m on the p side); E_max = 1.6×10⁻¹⁹ × 10²² × 3.03×10⁻⁷/1.04×10⁻¹⁰ ≈ **4.7×10⁶ V/m**.

**8. Remarks.** V_bi cannot be read with a voltmeter: contact potentials at the metal leads cancel it exactly, so it drives no external current. Applied bias changes the barrier to V_bi − V_a (V_a = applied voltage, positive for forward bias), which is the basis of rectification.

**Marking checklist.** The points a marker looks for. Tick each one off in your own answer:

- ✓ diffusion of holes p → n and electrons n → p, driven by the concentration gradient
- ✓ immobile ions uncovered: negative acceptors on p side, positive donors on n side
- ✓ field from n to p; drift opposes diffusion; equilibrium when they balance
- ✓ flat Fermi level in equilibrium
- ✓ V_bi = (kT/q) ln(N_{A}N_D/n_i²), with symbols defined
- ✓ N_A x_p = N_D x_n: wider on the lightly doped side
- ✓ labelled sketch (charge, field, band diagram)
- ✓ typical value (≈ 0.7–0.8 V for Si) and the point that it cannot be measured with a voltmeter

**Common mistakes.**

- Saying the depletion region contains "no charge". It contains no *mobile* carriers but a lot of fixed ion charge; that charge is the whole point.
- Getting the field direction backwards. The field points from the positive (n) side to the negative (p) side.
- Writing V_bi = (kT/q) ln(N_{A}N_D/n_i) (forgetting the square on n_i) or using log₁₀ instead of ln.
- Claiming V_bi can be larger than the band gap for normal doping: it is always less than E_g/q (1.12 V for Si).

**Remember it.** "Carriers leave, ions stay, the field says stop": diffusion uncovers ions, the ions' field stops further diffusion, and the voltage they leave behind is V_bi.

**Try a variant.** Calculate V_bi and say on which side most of the depletion region lies for a silicon junction with N_A = 1×10²⁴ m⁻³ and N_D = 1×10²¹ m⁻³ at 300 K. *Answer:* V_bi = 0.0259 × ln(10²⁴ × 10²¹/10³²) = 0.0259 × ln(10¹³) = **0.775 V**; since x_n/x_p = N_A/N_D = 1000, **almost all of W lies in the lightly doped n side** (a one-sided p⁺n junction).

---

### Q48. Derive the ideal Shockley diode equation and explain the effect of forward and reverse bias.

> **Question type:** Derivation · **Topic:** ideal diode equation · **Full notes:** Week 10 (The p-n Junction Diode); minority-carrier diffusion in Week 9

**What the examiner wants.** A full, ordered derivation: list the assumptions, obtain the minority densities at the depletion edges (law of the junction), solve the minority-carrier diffusion equation in each neutral region, find the diffusion currents at the depletion edges, add them, and identify J_s. Then use the result to explain forward and reverse bias, ideally with the I-V sketch.

**Key terms.**

- **Minority carrier:** the less numerous carrier (holes in n-type, electrons in p-type). Equilibrium values: p_n0 = n_i²/N_D on the n side, n_p0 = n_i²/N_A on the p side.
- **Excess carrier density (Δp, Δn):** the amount by which a carrier density exceeds its equilibrium value.
- **Low-level injection:** injected minority densities remain much smaller than the majority density.
- **Lifetime (τ_p, τ_n):** average time an excess minority carrier survives before recombining (s).
- **Diffusion coefficient (D_p, D_n):** how quickly carriers spread down a concentration gradient (m²/s).
- **Diffusion length (L_p, L_n):** average distance a minority carrier diffuses before recombining, L = √(Dτ) (m).
- **Saturation current (I_s, J_s):** the small reverse current of the diode, and the scale factor of the exponential (A, or A/m² for J_s).
- **Quasi-equilibrium:** carriers in the depletion region stay so close to equilibrium that Boltzmann statistics still link the densities on either side of it.

**Model answer.**

#### Assumptions

1. Abrupt junction; **depletion approximation**: no mobile carriers inside the depletion region (from x = −x_p to x = x_n), exact neutrality outside it.
2. Non-degenerate doping, so Boltzmann statistics apply.
3. **Low-level injection**: Δp ≪ N_D on the n side and Δn ≪ N_A on the p side, so majority densities are unchanged.
4. **No generation or recombination inside the depletion region**, so the electron and hole currents are each constant across it.
5. All the applied voltage V appears across the depletion region; the neutral regions carry no field (E = 0), so minority current there is pure diffusion.
6. Neutral regions much longer than the diffusion lengths, ending in ohmic contacts; steady state.

Take x = 0 at the junction, the n region for x > x_n and the p region for x < −x_p. V > 0 means forward bias (p side positive).

#### Step 1: law of the junction

In equilibrium the Boltzmann relation links the electron densities on the two sides of the barrier:

    n_n0 = n_p0 e^{qV_bi/kT}

Where:

- n_n0 = equilibrium electron (majority) density in the n region ≈ N_D (m⁻³)
- n_p0 = equilibrium electron (minority) density in the p region = n_i²/N_A (m⁻³)
- V_bi = built-in potential (V); kT/q = 0.0259 V at 300 K

With bias V the barrier becomes V_bi − V. Under quasi-equilibrium the same relation holds at the depletion edges with the new barrier, and by low-level injection n_n(x_n) ≈ n_n0:

    n_p(−x_p) = n_n0 e^{−q(V_bi − V)/kT} = n_p0 e^{qV/kT}

The same argument for holes gives p_n(x_n) = p_n0 e^{qV/kT}. The **excess** minority densities at the edges are therefore:

    Δp_n(x_n) = p_n0 ( e^{qV/kT} − 1 ),     Δn_p(−x_p) = n_p0 ( e^{qV/kT} − 1 )

Where:

- p_n0 = n_i²/N_D = equilibrium hole density in the n region (m⁻³)
- Δp_n(x_n), Δn_p(−x_p) = excess hole and electron densities at the n-side and p-side depletion edges (m⁻³)
- V = applied voltage (V)

#### Step 2: minority-carrier diffusion equation in the neutral n region

The hole continuity equation is ∂p/∂t = −(1/q) dJ_p/dx − Δp/τ_p. In steady state (∂p/∂t = 0) with no field, J_p = −qD_p dp/dx, so:

    D_p d²Δp_n/dx² − Δp_n/τ_p = 0,     or     d²Δp_n/dx² = Δp_n/L_p²,   L_p = √(D_pτ_p)

Where:

- D_p = hole diffusion coefficient (m²/s); τ_p = hole lifetime (s); L_p = hole diffusion length (m)
- J_p = hole current density (A/m²)

The general solution is a sum of e^{−(x − x_n)/L_p} and e^{+(x − x_n)/L_p}. In a long region Δp_n must fall to zero far from the junction, so the growing term is dropped. Using Step 1 as the boundary value:

    Δp_n(x) = Δp_n(x_n) e^{−(x − x_n)/L_p}     (x ≥ x_n)

@fig figures/injection.svg | Injected minority holes decay exponentially into the neutral n region with characteristic length L_p; the slope at the depletion edge sets the diffusion current.

#### Step 3: hole current at the n-side edge, x = x_n

    J_p(x_n) = −qD_p dΔp_n/dx |_{x_n} = (qD_p/L_p) Δp_n(x_n) = (qD_p p_n0/L_p)( e^{qV/kT} − 1 )

Where:

- J_p(x_n) = hole diffusion current density at the n-side depletion edge (A/m²), positive in the p → n direction
- dΔp_n/dx = −Δp_n(x_n)/L_p = slope of the excess-hole profile at x_n (m⁻⁴)

#### Step 4: electron current at the p-side edge, x = −x_p

The identical argument in the p region gives Δn_p(x) = Δn_p(−x_p) e^{(x + x_p)/L_n} for x ≤ −x_p, and J_n = +qD_n dn/dx, so:

    J_n(−x_p) = (qD_n n_p0/L_n)( e^{qV/kT} − 1 ),     L_n = √(D_nτ_n)

Where:

- D_n = electron diffusion coefficient (m²/s); τ_n = electron lifetime (s); L_n = electron diffusion length (m)

#### Step 5: add the two currents

The total current density J = J_n + J_p is the same at every x. By assumption 4, J_n does not change across the depletion region, so J_n(x_n) = J_n(−x_p). Evaluating the total at x = x_n:

    J = J_p(x_n) + J_n(−x_p) = ( qD_p p_n0/L_p + qD_n n_p0/L_n )( e^{qV/kT} − 1 )

Where:

- J = total current density (A/m²), the same at every point of the diode
- J_n(−x_p) = electron diffusion current density at the p-side depletion edge (A/m²)

#### Step 6: identify J_s

Substituting p_n0 = n_i²/N_D and n_p0 = n_i²/N_A, and multiplying by the area A:

**J = J_s ( e^{qV/kT} − 1 ),   J_s = q n_i² ( D_p/(L_pN_D) + D_n/(L_nN_A) ),   I = A J = I_s ( e^{qV/kT} − 1 )**

Where:

- J, I = diode current density (A/m²) and current (A), positive in the forward direction
- J_s, I_s = saturation current density (A/m²) and saturation current (A), I_s = AJ_s
- A = junction area (m²); n_i = 1×10¹⁶ m⁻³ for Si at 300 K
- N_A, N_D = acceptor and donor concentrations (m⁻³)

This is the **ideal Shockley diode equation**. Note that J_s ∝ n_i², and the term of the *lightly* doped side dominates.

#### Effect of forward bias (V > 0, p side positive)

- The barrier falls to V_bi − V and the depletion region narrows.
- Minority carriers are **injected**: edge densities rise by e^{qV/kT}.
- For V above about 0.1 V (≫ kT/q) the −1 is negligible: I ≈ I_s e^{qV/kT}. The current rises tenfold every (kT/q) ln 10 ≈ **60 mV**.
- Because I_s is tiny, appreciable current needs about 0.6–0.7 V in Si (0.2–0.3 V in Ge).

#### Effect of reverse bias (V < 0, p side negative)

- The barrier rises to V_bi + |V| and the depletion region widens.
- e^{qV/kT} → 0, so the edge minority densities fall almost to zero: carriers are **extracted**, not injected.
- For |V| more than a few kT/q: I ≈ **−I_s**, small and independent of voltage, carried by minority carriers generated within a diffusion length of the junction.

@fig figures/diode-iv.svg | Ideal diode characteristic: exponential forward current (a decade per 60 mV at 300 K) and a tiny constant reverse current −I_s.

Sketch in the exam: I against V; an exponential rising sharply near 0.6–0.7 V; a flat line just below the axis at −I_s for V < 0; label I_s and the cut-in voltage.

#### Numerical check

**Given:** Si, N_A = 10²³ m⁻³, N_D = 10²² m⁻³, D_p = 1.24×10⁻³ m²/s, D_n = 3.5×10⁻³ m²/s, τ_p = τ_n = 1 μs, A = 10⁻⁸ m², 300 K.

**Solution.** L_p = √(1.24×10⁻³ × 10⁻⁶) = 3.52×10⁻⁵ m; L_n = √(3.5×10⁻³ × 10⁻⁶) = 5.92×10⁻⁵ m.

    J_s = 1.6×10⁻¹⁹ × 10³² × ( 1.24×10⁻³/(3.52×10⁻⁵ × 10²²) + 3.5×10⁻³/(5.92×10⁻⁵ × 10²³) )
        = 1.6×10¹³ × (3.52×10⁻²¹ + 5.92×10⁻²²) = 6.6×10⁻⁸ A/m²

**Answer:** **I_s = AJ_s = 10⁻⁸ × 6.6×10⁻⁸ = 6.6×10⁻¹⁶ A**; I(0.6 V) ≈ 6.6×10⁻¹⁶ × e^{23.17} ≈ **7.6 μA**; I(0.7 V) ≈ **0.36 mA**; I(−5 V) = **−6.6×10⁻¹⁶ A**.

**What this means:** 86 % of the current is holes injected into the lightly doped n side. At 0.6 V the injected hole density at x_n is 1.2×10²⁰ m⁻³, still ≪ N_D = 10²² m⁻³, so low-level injection holds.

**Real diodes** depart from this: recombination in the depletion region (low forward bias), high-level injection and series resistance (high current), generation current and breakdown (reverse). These are lumped into I = I_s(e^{qV/ηkT} − 1), with ideality factor η between 1 and 2.

**Marking checklist.** The points a marker looks for. Tick each one off in your own answer:

- ✓ assumptions listed: depletion approximation, low-level injection, no G–R in depletion region, Boltzmann statistics, E = 0 in neutral regions, long diodes
- ✓ law of the junction: p_n(x_n) = p_n0e^{qV/kT}, n_p(−x_p) = n_p0e^{qV/kT}, derived from the barrier V_bi − V
- ✓ diffusion equation D_p d²Δp/dx² − Δp/τ_p = 0 and its decaying-exponential solution with L_p = √(D_pτ_p)
- ✓ J_p(x_n) = (qD_pp_n0/L_p)(e^{qV/kT} − 1) and the matching electron term
- ✓ argument that the currents may be added at the depletion edges (J_n constant across W)
- ✓ boxed result with J_s = qn_i²(D_p/(L_pN_D) + D_n/(L_nN_A))
- ✓ forward bias: barrier lowered, injection, I ≈ I_se^{qV/kT}, 60 mV/decade
- ✓ reverse bias: barrier raised, extraction, I ≈ −I_s
- ✓ labelled I-V sketch

**Common mistakes.**

- Using total (not excess) minority density in the current: the "−1" comes from Δp = p_n0(e^{qV/kT} − 1); forgetting it gives zero reverse current and a wrong equation.
- Keeping the growing exponential e^{+x/L_p} in the long-diode solution; it must be dropped so Δp → 0 far away.
- Not justifying the addition of J_n and J_p: say explicitly that no recombination in the depletion region makes each constant across it.
- Swapping the doping in J_s: holes injected into the n side carry D_p/(L_pN_D), so the *lighter* doping dominates.

**Remember it.** "Inject, diffuse, add": the junction law injects, the diffusion equation spreads them over L, and the two slopes at the edges add up to I_s(e^{qV/kT} − 1).

**Try a variant.** For a p⁺n silicon diode (N_D = 10²² m⁻³ on the n side, D_p = 1.24×10⁻³ m²/s, τ_p = 1 μs, A = 10⁻⁸ m²), find I_s and the forward voltage for I = 1 mA. *Answer:* the electron term is negligible, so I_s ≈ qAn_i²D_p/(L_pN_D) = 1.6×10⁻¹⁹ × 10⁻⁸ × 10³² × 1.24×10⁻³/(3.52×10⁻⁵ × 10²²) = **5.6×10⁻¹⁶ A**; V = (kT/q) ln(I/I_s) = 0.0259 × ln(1.78×10¹²) = **0.73 V**.

---

### Q49. Differentiate between a Schottky barrier diode and an Ohmic contact. Explain their energy-band characteristics.

> **Question type:** Compare and explain · **Topic:** metal–semiconductor contacts · **Full notes:** Week 11 (Metal–Semiconductor Interfaces)

**What the examiner wants.** Both are metal–semiconductor contacts; the answer must show what makes one rectifying and the other not. Marks are for the band diagrams (before contact, at equilibrium, under bias for the Schottky diode), the barrier formulas, the two ways of making an ohmic contact, the I-V behaviour, and a comparison table.

**Key terms.**

- **Vacuum level (E_vac):** energy of an electron at rest just outside the material; the common reference.
- **Work function (Φ_m, Φ_s):** energy from the Fermi level up to the vacuum level, for the metal and the semiconductor (eV).
- **Electron affinity (χ):** energy from the conduction-band edge E_c up to the vacuum level; 4.05 eV for Si, independent of doping.
- **Schottky barrier height (Φ_B):** barrier an electron in the metal must climb to enter the semiconductor (eV); fixed by the interface.
- **Built-in potential (V_bi):** barrier an electron in the semiconductor must climb to reach the metal (V).
- **Depletion / accumulation layer:** a surface layer with fewer / more majority carriers than the bulk; bands bend up / down in n-type.
- **Thermionic emission:** carriers crossing *over* a barrier using thermal energy.
- **Tunnelling (field emission):** carriers passing *through* a barrier only a few nanometres thick.

**Model answer.**

A **Schottky barrier diode** is a metal–semiconductor contact with a significant barrier to majority carriers, so it **rectifies**. An **ohmic contact** has no barrier that limits the current, so it conducts equally in both directions with a linear I-V (V = IR_c). Both are explained with band diagrams using one rule: **at equilibrium the Fermi level is flat**. The cases below are for a metal on **n-type** silicon.

#### Before contact

Energies are measured down from the common vacuum level. The semiconductor work function depends on doping:

    Φ_s = χ + (E_c − E_F),     E_c − E_F = kT ln(N_c/N_D)

Where:

- Φ_s = semiconductor work function (eV); χ = electron affinity, 4.05 eV (Si)
- E_c − E_F = depth of the Fermi level below the conduction-band edge (eV)
- kT = 0.0259 eV at 300 K; N_c = 2.8×10²⁵ m⁻³ (Si); N_D = donor concentration (m⁻³)

@fig figures/ms-before.svg | Metal and n-type semiconductor before contact. With Φ_m > Φ_s the semiconductor's Fermi level lies higher by Φ_m − Φ_s, so electrons will flow into the metal on contact.

Whether E_F of the semiconductor lies above or below E_F of the metal decides which way electrons flow on contact, and hence the type of contact.

#### Schottky barrier (Φ_m > Φ_s, moderate doping)

**At equilibrium.**

1. On contact, electrons flow from the semiconductor (higher E_F) into the metal.
2. They leave behind positive donor ions: a **depletion region** forms in the semiconductor, with a thin sheet of negative charge on the metal surface.
3. The resulting field bends the bands **upward** towards the interface until the Fermi levels align.
4. Two barriers result:

    Φ_B = Φ_m − χ          (barrier seen from the metal; Schottky–Mott rule)

    V_bi = Φ_m − Φ_s = Φ_B − (E_c − E_F)/q          (barrier seen from the semiconductor)

    W = √( 2ε_s(V_bi − V)/qN_D )

Where:

- Φ_m = metal work function (eV), e.g. Au 5.1 eV
- W = depletion width (m); ε_s = 1.04×10⁻¹⁰ F/m; q = 1.6×10⁻¹⁹ C
- V = applied voltage (V), positive for forward bias (metal positive)

**Example (Au on n-Si, N_D = 10²² m⁻³):** E_c − E_F = 0.0259 ln(2.8×10²⁵/10²²) = 0.0259 ln(2800) = 0.21 eV, Φ_s = 4.26 eV, Φ_B = 5.1 − 4.05 = **1.05 eV**, V_bi = 5.1 − 4.26 = **0.84 V**, W = √(2 × 1.04×10⁻¹⁰ × 0.84/(1.6×10⁻¹⁹ × 10²²)) = **3.3×10⁻⁷ m (0.33 μm)**: far too thick to tunnel through. (Real interfaces are **Fermi-level pinned**, so Au on n-Si actually measures Φ_B ≈ 0.8 eV.)

@fig figures/schottky.svg | Schottky contact at equilibrium: flat E_F, bands bent upward in the semiconductor, barrier qΦ_B seen from the metal and qV_bi seen from the semiconductor.

**Under bias.** qΦ_B is fixed by the interface and never changes; the applied voltage appears across the depletion region and changes only the semiconductor-side barrier.

- **Forward bias** (metal +): the semiconductor E_F rises by qV, the band bending falls to q(V_bi − V), W narrows, and electrons pour over the barrier into the metal; current rises exponentially.
- **Reverse bias** (metal −): bending rises to q(V_bi + |V|), W widens, the semiconductor-to-metal flow is cut off, and only the small metal-to-semiconductor flow over the fixed Φ_B remains: the saturation current.

@fig figures/schottky-bias.svg | The Schottky contact at equilibrium, forward bias and reverse bias: qΦ_B stays fixed while the semiconductor-side barrier falls to q(V_bi − V) or rises to q(V_bi + |V|).

Current is by **thermionic emission** of majority carriers:

    J = J_s ( e^{qV/ηkT} − 1 ),     J_s = A∗∗ T² e^{−qΦ_B/kT}

Where:

- J, J_s = current density and saturation current density (A/m²)
- A∗∗ = effective Richardson constant, about 1.1×10⁶ A/m²K² for n-Si
- T = temperature (K); η = ideality factor (1.0–1.1 for a good Schottky diode)

For Φ_B = 0.8 eV: J_s = 1.1×10⁶ × 300² × e^{−0.8/0.0259} = 3.8×10⁻³ A/m² and 10⁴ A/m² flows at only about 0.0259 × ln(10⁴/3.8×10⁻³) = **0.38 V**, against about 0.7 V for a Si p-n diode. No minority charge is stored, so it switches very fast.

#### Ohmic contact: the two mechanisms

**(a) Low-barrier metal, accumulation (Φ_m < Φ_s on n-type).** Before contact the metal's E_F is higher, so on contact electrons flow from the metal **into** the semiconductor. They pile up in an **accumulation layer**; the bands bend **downward** at the interface. There is no barrier to electrons in either direction, so current flows freely both ways. (For p-type the condition is reversed: Φ_m > Φ_s.) In practice Fermi-level pinning makes suitable metals rare on Si and GaAs.

**(b) Heavy doping, tunnelling (the practical method).** The surface under the contact is doped n⁺ (above about 10²⁵ m⁻³). The barrier height is unchanged, but since W ∝ 1/√N_D the barrier becomes only a few nanometres thick, and electrons **tunnel** through it in both directions. Example: for a 0.60 V barrier, W = 2.79×10⁻⁷ m (279 nm) at N_D = 10²² m⁻³ (rectifying) but only **8.8×10⁻⁹ m (8.8 nm)** at 10²⁵ m⁻³ (ohmic).

@fig figures/ohmic-contacts.svg | The two routes to an ohmic contact on n-type silicon: (a) Φ_m < Φ_s, downward band bending into an accumulation layer with no barrier; (b) heavy doping, a barrier so thin that electrons tunnel through it.

An ohmic contact is judged by its specific contact resistance ρ_c = R_cA (Ω·m²; R_c = contact resistance in Ω, A = area in m²); good contacts reach 10⁻¹⁰–10⁻¹² Ω·m². Silicides (TiSi₂, NiSi) on Si and alloyed Au–Ge–Ni on n-GaAs are standard.

Sketch in the exam: for each case draw E_vac, metal E_F, and the semiconductor E_c, E_F, E_v; mark qΦ_m, qΦ_s, qχ before contact; after contact show the flat E_F, the upward bend with qΦ_B and qV_bi (Schottky), the downward bend (accumulation) and the thin barrier with a tunnelling arrow (heavy doping).

#### Comparison

| Feature | Schottky barrier diode | Ohmic contact |
|---|---|---|
| Work-function condition (n-type) | Φ_m > Φ_s | Φ_m < Φ_s, or any metal on n⁺ |
| Doping under contact | Moderate (10²¹–10²³ m⁻³) | Heavy (> 10²⁵ m⁻³) |
| Band bending (n-type) | Upward: depletion layer | Downward (accumulation) or a very thin barrier |
| Barrier to majority carriers | Yes: qΦ_B and qV_bi | None, or thin enough to tunnel through |
| Transport | Thermionic emission over the barrier | Free flow, or tunnelling (field emission) |
| I-V | Exponential, rectifying | Linear, symmetric, V = IR_c |
| Resistance | Depends on bias polarity | Small and constant |
| Effect of bias on bands | Semiconductor-side barrier changes, qΦ_B fixed | Negligible: no barrier to modulate |
| Use | Fast rectifiers, RF detectors, clamps, MESFET gates | Connecting every device to the circuit |

**Marking checklist.** The points a marker looks for. Tick each one off in your own answer:

- ✓ definitions: rectifying barrier vs linear, symmetric, low-resistance contact
- ✓ Φ_s = χ + (E_c − E_F); comparison of Φ_m and Φ_s decides the contact type
- ✓ Schottky formation: electrons to metal, depletion region, upward bending, Fermi levels align
- ✓ Φ_B = Φ_m − χ and V_bi = Φ_m − Φ_s
- ✓ band diagrams before contact, at equilibrium and under forward/reverse bias, with qΦ_B fixed
- ✓ thermionic emission J = A∗∗T²e^{−qΦ_B/kT}(e^{qV/ηkT} − 1)
- ✓ ohmic route 1: accumulation, downward bending, no barrier
- ✓ ohmic route 2: heavy doping, W ∝ 1/√N_D, tunnelling
- ✓ comparison table

**Common mistakes.**

- Saying an ohmic contact "has no barrier". The practical (n⁺) ohmic contact has a barrier; it is simply thin enough to tunnel through.
- Reversing the conditions for p-type: there a Schottky barrier needs Φ_m < Φ_s and an ohmic contact Φ_m > Φ_s.
- Drawing Φ_B changing with bias. Only the semiconductor-side barrier (V_bi ∓ V) changes.
- Mixing up Φ_B and V_bi: Φ_B is measured from the metal Fermi level, V_bi from the semiconductor conduction band; they differ by (E_c − E_F).

**Remember it.** "Schottky climbs over, ohmic walks through": over a fixed barrier by thermionic emission, or through a paper-thin one by tunnelling.

**Try a variant.** Platinum (Φ_m = 5.65 eV) is deposited on p-type silicon with N_A = 1×10²² m⁻³. Is the ideal contact rectifying or ohmic? *Answer:* E_F − E_v = 0.0259 ln(N_v/N_A) = 0.0259 ln(1.04×10²⁵/10²²) = 0.0259 ln(1040) = 0.18 eV, so Φ_s = χ + E_g − 0.18 = 4.05 + 1.12 − 0.18 = **4.99 eV**. Φ_m > Φ_s on **p-type**, so electrons leave the semiconductor, holes accumulate at the surface and the bands bend upward with no hole barrier: the contact is **ohmic** (by contrast Al, 4.28 eV, gives a hole barrier Φ_{Bp} = 1.12 − (4.28 − 4.05) = 0.89 eV, a Schottky contact).

---

### Q50. Explain the principles of I-V and C-V characterisation of semiconductor devices and describe how C-V measurements can be used to estimate doping concentration.

> **Question type:** Explanation with calculation · **Topic:** device characterisation · **Full notes:** Week 12 (Interface Characterisation)

**What the examiner wants.** For each technique: what is applied, what is measured, which equation links them, and which plot turns the data into a straight line. Then a step-by-step description of extracting doping (and V_bi) from a Mott–Schottky plot, best shown with a worked numerical example and a note on limitations.

**Key terms.**

- **I-V characterisation:** measuring current as the DC voltage is stepped, to extract saturation current, ideality factor, series resistance, leakage, breakdown and barrier height.
- **Ideality factor (η):** 1 for pure diffusion (or thermionic emission) current, up to 2 when depletion-region recombination dominates.
- **Series resistance (R_s):** resistance of the bulk, contacts and leads in series with the junction (Ω).
- **C-V characterisation:** measuring small-signal capacitance as the DC reverse bias is stepped, to find doping and V_bi.
- **Depletion capacitance (C):** capacitance of the carrier-free depletion layer, C = ε_sA/W (F).
- **One-sided junction:** p⁺n, n⁺p or Schottky diode; the depletion region lies almost entirely in the lightly doped side.
- **Mott–Schottky plot:** 1/C² against V; straight for uniform doping.
- **Doping profile N(x):** doping concentration as a function of depth below the surface.

**Model answer.**

#### 1. I-V characterisation

**Principle.** A source-measure unit applies a DC voltage in steps from reverse to forward bias and records the current (picoamps to amps, often on a probe station, sometimes at several temperatures). The data are compared with the diode law:

    I = I_s ( e^{qV/ηkT} − 1 )   ⇒   ln I = ln I_s + (q/ηkT) V     (V > about 0.1 V)

Where:

- I = diode current (A); I_s = saturation current (A)
- V = applied voltage, positive for forward bias (V)
- η = ideality factor (dimensionless); kT/q = 0.0259 V at 300 K

A **semi-log plot** of ln I against V is a straight line:

- intercept at V = 0 → **I_s**;
- slope = q/(ηkT) → **η = (q/kT)/slope**;
- bending below the line at high current → **series resistance**, R_s = (extra voltage)/I;
- reverse branch → **leakage** and **breakdown voltage**;
- for a Schottky diode, **barrier height** Φ_B = (kT/q) ln(A∗∗AT²/I_s), with A = area (m²), A∗∗ ≈ 1.1×10⁶ A/m²K² for n-Si, T in K;
- a straight, symmetric line through the origin between two contacts confirms an **ohmic contact**.

Transistors are characterised the same way (threshold voltage and mobility from MOSFET curves, current gain from BJT curves).

#### 2. C-V characterisation

**Principle.** An LCR meter superimposes a small AC signal (10–50 mV, about 1 MHz) on a DC **reverse** bias and measures the capacitance as the bias is stepped. A reverse-biased one-sided junction or Schottky diode is a parallel-plate capacitor whose "gap" is the depletion region:

    C = ε_s A / W,     W = √( 2ε_s(V_bi − V)/qN )

Where:

- C = depletion capacitance (F); A = junction area (m²)
- ε_s = permittivity of silicon, 1.04×10⁻¹⁰ F/m; q = 1.6×10⁻¹⁹ C
- W = depletion width (m); V_bi = built-in potential (V)
- V = applied voltage, negative for reverse bias (V); N = doping of the lightly doped side (m⁻³)

As reverse bias grows, W widens and C falls.

#### 3. Estimating doping from C-V

Eliminating W and squaring:

    1/C² = 2(V_bi − V) / (qε_s N A²)

So the procedure is:

- Measure C at a series of reverse biases (0, −1, … −5 V).
- Plot **1/C² against V**. For uniform doping the points lie on a straight line.
- The **slope** is −2/(qε_sNA²), so:

    N = 2 / ( qε_s A² |slope| )

- The **voltage-axis intercept** (where 1/C² = 0) is **V_bi**. For a Schottky diode, Φ_B = V_bi + (kT/q) ln(N_c/N).
- If the plot curves, the doping is non-uniform; use the local slope and the depth W = ε_sA/C to obtain a **profile**: N(W) = 2/(qε_sA²|d(1/C²)/dV|).

Where:

- |slope| = magnitude of the slope of the 1/C² line (F⁻²V⁻¹)
- N_c = conduction-band effective density of states, 2.8×10²⁵ m⁻³ (Si)

@fig figures/cv.svg | Mott–Schottky plot: 1/C² falls linearly towards the forward-bias side and meets the voltage axis at V_bi; the slope gives the doping.

Sketch in the exam: 1/C² on the vertical axis, V on the horizontal with reverse bias to the left; a straight line falling to the right and cutting the V axis at +V_bi; label the slope −2/(qε_sNA²).

#### 4. Worked example: doping and V_bi from a 1/C² line

**Given:** a Schottky diode on n-type Si, A = 1.0×10⁻⁷ m², 300 K, with readings:

| V (V) | 0 | −1 | −2 | −3 | −4 | −5 |
|---|---|---|---|---|---|---|
| C (pF) | 37.2 | 22.8 | 17.9 | 15.2 | 13.4 | 12.2 |
| 1/C² (F⁻²) | 7.2×10²⁰ | 1.92×10²¹ | 3.12×10²¹ | 4.33×10²¹ | 5.57×10²¹ | 6.72×10²¹ |

**Find:** N_D, V_bi, the depletion depth at −5 V and the barrier height.

**Formula:** N_D = 2/(qε_sA²|slope|); V_bi from 1/C² = 0; W = ε_sA/C; Φ_B = V_bi + (kT/q) ln(N_c/N_D).

**Solution.**

Step 1. The 1/C² values rise by about 1.2×10²¹ F⁻² per volt: the line is straight, so the doping is uniform. Slope from the end points:

    slope = (6.72×10²¹ − 7.2×10²⁰)/(−5 − 0) = −1.20×10²¹ F⁻²V⁻¹

Step 2. Doping:

    N_D = 2 / (1.6×10⁻¹⁹ × 1.04×10⁻¹⁰ × (10⁻⁷)² × 1.20×10²¹) = 2 / 2.0×10⁻²² = 1.0×10²² m⁻³

Step 3. Intercept: at V = 0, 1/C² = 7.2×10²⁰, and it falls by 1.20×10²¹ per volt of forward bias, so it reaches zero at

    V_bi = 7.2×10²⁰ / 1.20×10²¹ = 0.60 V

Step 4. Depth probed at −5 V:

    W = ε_sA/C = 1.04×10⁻¹⁰ × 10⁻⁷ / 12.2×10⁻¹² = 8.5×10⁻⁷ m = 0.85 μm

Step 5. Barrier height: (kT/q) ln(N_c/N_D) = 0.0259 × ln(2.8×10²⁵/10²²) = 0.0259 × ln(2800) = 0.21 V, so Φ_B = 0.60 + 0.21 = 0.81 eV.

**Answer:** **N_D = 1.0×10²² m⁻³, V_bi = 0.60 V**, W(−5 V) = 8.5×10⁻⁷ m (0.85 μm), Φ_B ≈ 0.81 eV.

**What this means:** the doping was measured electrically, without cutting or etching the wafer, and is uniform at least to 0.85 μm below the contact. A 0.81 eV barrier is typical of a good Schottky contact on n-Si.

#### 5. Accuracy and limits

- Measure only in reverse bias (forward bias adds a large diffusion capacitance).
- Correct for stray (pad and probe) capacitance and series resistance; keep the AC signal small.
- Know the area accurately: N ∝ 1/A², so a 10 % area error gives a 20 % doping error.
- C-V sees only the lightly doped side, only to depths reached before breakdown; deep traps can distort the result at the wrong frequency.

| | I-V | C-V |
|---|---|---|
| Applied | DC voltage, reverse to forward | DC reverse bias + small AC signal |
| Measured | Current | Capacitance |
| Straight-line plot | ln I against V | 1/C² against V |
| Slope gives | η | Doping N |
| Intercept gives | I_s (and Φ_B) | V_bi (and Φ_B) |

**Marking checklist.** The points a marker looks for. Tick each one off in your own answer:

- ✓ I-V principle: voltage stepped, current measured, I = I_s(e^{qV/ηkT} − 1)
- ✓ semi-log plot: intercept → I_s, slope → η; R_s, leakage, breakdown, Φ_B
- ✓ C-V principle: reverse bias + small AC signal, C = ε_sA/W, C falls with reverse bias
- ✓ derivation of 1/C² = 2(V_bi − V)/(qε_sNA²)
- ✓ N = 2/(qε_sA²|slope|) and V_bi from the voltage intercept
- ✓ profiling: local slope and W = ε_sA/C for non-uniform doping
- ✓ worked numbers: N ≈ 1×10²² m⁻³, V_bi = 0.60 V
- ✓ labelled Mott–Schottky sketch and at least two practical limitations

**Common mistakes.**

- Plotting C or 1/C against V: only 1/C² gives a straight line for uniform doping.
- Leaving the area unsquared, or mixing units (area in mm² or μm² with ε_s in F/m): keep everything in SI (A in m², ε_s in F/m), and remember A².
- Reading V_bi from the 1/C² axis instead of the voltage axis, or giving it a negative sign: the line crosses at a positive (forward) voltage.
- Applying it to a symmetric p-n junction without saying so: then N is the combined N_{A}N_D/(N_A + N_D), not a single doping.

**Remember it.** "Slope gives the dopants, intercept gives the barrier": 1/C² against V is a straight line whose steepness is 2/(qε_sNA²) and whose zero is V_bi.

**Try a variant.** A one-sided Si junction of area 2×10⁻⁷ m² gives a 1/C² plot with slope magnitude 4.0×10²⁰ F⁻²V⁻¹. Find the doping of the lightly doped side. *Answer:* N = 2/(qε_sA²|slope|) = 2/(1.6×10⁻¹⁹ × 1.04×10⁻¹⁰ × 4×10⁻¹⁴ × 4.0×10²⁰) = **7.5×10²¹ m⁻³**. (Doubling the area quarters the slope for the same doping.)
