# Module 10 — Drift, Mobility and High-Field Effects

Examined in Q35–Q38 and Q41. Drift is the motion of carriers pushed by an electric field. How easily they move is measured by mobility, and mobility is limited by scattering.

## 10.1 Thermal motion and drift

With no field, carriers move randomly at the thermal velocity

    v_th = √(3kT/m∗) ≈ 10⁷ cm/s   (Si electrons, 300 K)

colliding (scattering) every **mean free time** τ_m ≈ 0.1–1 ps. The random motion averages to zero, so there is no current.

Apply a field E. Between collisions each electron accelerates by −qE/m_n∗. On average it gains a velocity −qEτ_m/m_n∗ before a collision randomises it again. This small average velocity superimposed on the random motion is the **drift velocity**:

    v_dn = −(qτ_m/m_n∗) E = −μ_n E,      v_dp = +μ_p E

## 10.2 Mobility

    μ = qτ_m / m∗      [cm²/V·s]

Mobility is drift velocity per unit field. It is high when scattering is rare (long τ_m) and the effective mass is small.

| Material | μ_n (cm²/V·s) | μ_p (cm²/V·s) |
|---|---|---|
| Si | 1350 | 480 |
| Ge | 3900 | 1900 |
| GaAs | 8500 | 400 |

Electrons are faster than holes in all three, mainly because of their smaller effective mass.

## 10.3 Scattering mechanisms

1. **Lattice (phonon) scattering.** Thermal vibration of the lattice atoms disturbs the periodic potential. Acoustic phonons dominate at moderate temperatures; optical phonons at high temperature and high field. It increases with temperature: μ_L ∝ T^{−3/2}.
2. **Ionised-impurity (Coulomb) scattering.** Charged dopant ions deflect passing carriers. Fast carriers are deflected less, so it weakens with temperature and strengthens with doping: μ_I ∝ T^{3/2}/N_I, where N_I = N_D⁺ + N_A⁻ (compensating dopants still scatter).
3. **Neutral-impurity scattering.** Un-ionised dopants and other neutral atoms; important only at low temperature (freeze-out).
4. **Carrier–carrier scattering.** Electron–hole and electron–electron collisions at high carrier density (heavily injected regions).
5. **Defect scattering.** Dislocations, grain boundaries, vacancies and clusters.
6. **Surface (interface-roughness) scattering.** In MOSFET inversion layers, carriers pressed against the Si/SiO₂ interface by the gate field are scattered by roughness and interface charges, so channel mobility is only about half the bulk value.
7. **Polar-optical and piezoelectric scattering.** In compound semiconductors like GaAs, where bonds are partly ionic.
8. **Alloy scattering.** Random arrangement of atoms in alloys like AlGaAs and SiGe.

**Matthiessen's rule.** Independent mechanisms add as scattering rates, so

    1/μ = 1/μ_L + 1/μ_I + …

The lowest mobility dominates.

@fig figures/mobility.svg | Mobility against temperature. Impurity scattering limits mobility at low temperature, lattice scattering at high temperature, so mobility peaks between them. Heavier doping lowers and shifts the peak.

## 10.4 Factors affecting mobility

- **Temperature:** peaks, then falls as T^{−3/2} near and above room temperature (lattice-dominated).
- **Doping:** higher total impurity concentration lowers μ. In Si, μ_n falls from 1350 (light doping) to about 1000 at 10¹⁷ and about 100 cm²/V·s at 10²⁰ cm⁻³.
- **Effective mass:** smaller m∗ gives higher μ (GaAs electrons, 0.067m₀).
- **Electric field:** at high field μ falls (velocity saturation, §10.7).
- **Crystal quality and orientation:** defects and grain boundaries reduce μ; in MOSFETs electron mobility is highest on (100) and hole mobility on (110).
- **Strain:** tensile strain raises electron mobility in Si (used in modern CMOS).
- **Surfaces and interfaces.**

## 10.5 Drift current density

    J_drift = q(nμ_n + pμ_p) E = σE

    σ = q(nμ_n + pμ_p),     ρ = 1/σ

For n-type: σ ≈ qN_Dμ_n. For p-type: σ ≈ qN_Aμ_p.

Sheet resistance of a uniformly doped layer of thickness t: R_s = ρ/t (Ω/□), measured by a four-point probe.

## 10.6 Hall effect

A magnetic field B_z across a current I_x pushes carriers sideways, building a Hall voltage V_H. The Hall coefficient R_H = 1/qp (p-type, positive) or −1/qn (n-type, negative) gives the carrier type and density; combined with resistivity it gives mobility μ = |R_H|σ.

## 10.7 Velocity saturation

At low field v_d = μE. At high field (above about 10⁴ V/cm in Si), carriers gain energy faster than they can lose it to acoustic phonons. They become energetic enough to emit **optical phonons** (≈ 63 meV in Si), which takes away energy very effectively. The drift velocity then levels off at the **saturation velocity**:

    v_sat ≈ 1×10⁷ cm/s   (Si electrons and holes, GaAs)

A useful empirical model (Caughey–Thomas):

    v_d = μE / [ 1 + (μE/v_sat)^β ]^{1/β}      (β ≈ 2 for Si electrons, 1 for holes)

**GaAs** behaves differently: electron velocity peaks at about 2×10⁷ cm/s near 3.5 kV/cm, then **falls** as electrons transfer to the heavier, lower-mobility L-valley. This **negative differential mobility** (transferred-electron effect) is used in Gunn diodes for microwave oscillators.

@fig figures/velocity.svg | Drift velocity against field. Silicon carriers saturate near 10⁷ cm/s. GaAs electrons overshoot, then fall as they transfer to a heavier valley.

## 10.8 Hot-carrier effects

When carriers gain energy from the field much faster than they lose it, their average energy (expressed as an electron temperature T_e) rises far above the lattice temperature. These are **hot carriers**. Effects:

1. **Velocity saturation** and reduced mobility (above).
2. **Impact ionisation.** A hot carrier with energy above about 1.5E_g collides with a bond and creates a new electron–hole pair. Repeated, this gives **avalanche multiplication** and avalanche breakdown (used in avalanche photodiodes and IMPATT diodes; limits breakdown voltage).
3. **Hot-carrier injection** into the gate oxide of MOSFETs. Carriers near the drain overcome the Si/SiO₂ barrier (3.1 eV for electrons), become trapped in the oxide or create interface states, shifting the threshold voltage and degrading transconductance over time. A major reliability problem; reduced by **lightly doped drain (LDD)** structures and lower supply voltages.
4. **Substrate current** from holes generated by impact ionisation, which can trigger parasitic bipolar action and latch-up.
5. **Velocity overshoot** in very short devices, where carriers cross before they reach steady state and briefly exceed v_sat.
6. **Light emission** and noise.

---

## Exam questions solved

### Q35. Define carrier mobility and explain the factors that affect electron and hole mobility in semiconductors.

**Definition.** Carrier mobility μ is the drift velocity acquired per unit applied electric field:

    μ = |v_d| / E = qτ_m / m∗      [cm²/V·s]

where τ_m is the mean free time between collisions and m∗ the effective mass. It measures how easily carriers move through the crystal under a field. Electron mobility μ_n and hole mobility μ_p are different (Si: 1350 and 480 cm²/V·s).

**Factors affecting mobility:**

1. **Effective mass.** μ ∝ 1/m∗. Electrons generally have lighter effective mass than holes, so μ_n > μ_p. GaAs electrons (m∗ = 0.067m₀) have μ_n ≈ 8500 cm²/V·s.
2. **Temperature.** Two opposing effects:
   (a) Lattice scattering increases with T, μ_L ∝ T^{−3/2}.
   (b) Ionised-impurity scattering decreases with T, μ_I ∝ T^{3/2}/N_I, since faster carriers are deflected less.
   Mobility therefore rises at low T, peaks, and falls at high T. Near room temperature lattice scattering usually dominates and μ falls as T rises.
3. **Doping (impurity) concentration.** More ionised impurities mean more Coulomb scattering: μ falls as N_D + N_A increases (Si μ_n ≈ 1350 at 10¹⁴ cm⁻³ but about 100 at 10²⁰ cm⁻³). Compensated material has low mobility even though net doping is small.
4. **Electric field.** At low field μ is constant. At high field carriers heat up, emit optical phonons, and drift velocity saturates, so the effective mobility v_d/E falls.
5. **Crystal defects** (dislocations, grain boundaries, vacancies) add scattering; polycrystalline and amorphous material have much lower mobility.
6. **Surface and interface scattering.** In MOSFET channels, roughness and interface charge reduce mobility to roughly half the bulk value, and it falls further with higher gate field.
7. **Crystal orientation and strain.** Mobility depends on direction in anisotropic bands; strain alters effective masses (strained-Si technology).
8. **Carrier concentration** at high injection (carrier–carrier scattering).

These are combined using Matthiessen's rule, 1/μ = 1/μ_L + 1/μ_I + …

### Q36. Explain the mechanisms responsible for carrier scattering in semiconductor materials.

In a perfectly periodic, motionless lattice an electron would move without scattering (Bloch's theorem). Scattering happens whenever something breaks that perfect periodicity. The main mechanisms:

1. **Lattice (phonon) scattering.** Above 0 K the atoms vibrate about their positions, distorting the periodic potential. Carriers exchange energy and momentum with these lattice vibrations (phonons). *Acoustic-phonon* scattering is low-energy and nearly elastic, dominant at room temperature in Si; its rate increases with T, giving μ_L ∝ T^{−3/2}. *Optical-phonon* scattering involves high-energy phonons (63 meV in Si); it matters at high temperatures and high fields and causes velocity saturation. *Polar-optical and piezoelectric* scattering occur in compound semiconductors (GaAs), where the vibrating ionic bonds create electric fields that scatter carriers strongly.
2. **Ionised-impurity scattering.** Ionised donors (+) and acceptors (−) have Coulomb fields that deflect passing carriers (Rutherford-like scattering). Slower carriers spend more time near the ion and are deflected more, so it is strongest at low temperature and high doping: μ_I ∝ T^{3/2}/N_I.
3. **Neutral-impurity scattering.** Non-ionised impurity atoms scatter weakly by their distorted potential. Matters only at low temperatures when dopants are frozen out.
4. **Carrier–carrier scattering.** Coulomb interactions between carriers. Important at very high carrier densities (heavily doped or highly injected regions, e.g. in power devices and solar cells).
5. **Defect scattering.** Dislocations (charged lines in n-type material), grain boundaries, stacking faults, vacancies and clusters disturb the lattice and scatter carriers.
6. **Surface and interface scattering.** At surfaces and at the Si/SiO₂ interface, surface roughness, interface traps and oxide charges scatter carriers confined near the interface (MOSFET channels).
7. **Alloy scattering.** In alloys such as Al_{x}Ga_{1−x}As or SiGe, the random distribution of different atoms makes the potential non-periodic.
8. **Intervalley scattering.** Carriers move between equivalent or non-equivalent conduction-band minima by absorbing or emitting phonons (basis of the Gunn effect).

The total rate is the sum of the individual rates, 1/τ = Σ 1/τ_i, giving Matthiessen's rule 1/μ = Σ 1/μ_i. Near room temperature in lightly doped Si, lattice scattering dominates; in heavily doped Si or at low temperature, ionised-impurity scattering dominates.

### Q37. Derive the expression for drift current density due to electrons and holes.

**Assumptions:** uniform semiconductor, steady state, uniform field E in the +x direction, low enough field that v_d ∝ E.

**Step 1: drift velocity.** An electron experiences force F = −qE. Between collisions (mean free time τ_m), it accelerates by a = −qE/m_n∗. Averaging over all electrons, momentum gained from the field equals momentum lost in collisions:

    m_n∗ v_dn / τ_m = −qE   ⇒   v_dn = −(qτ_m/m_n∗) E = −μ_n E

Similarly, holes (charge +q) drift with the field:

    v_dp = +(qτ_mp/m_p∗) E = +μ_p E

**Step 2: current density from charge flow.** Current density is charge density × velocity. Consider a bar of cross-section A. In time dt, all carriers within distance v_d·dt of a cross-section pass through it; that is (v_d dt A) × concentration carriers.

For electrons, charge density −qn and velocity v_dn:

    J_n = (−qn)(v_dn) = (−qn)(−μ_n E) = qnμ_n E

For holes, charge density +qp and velocity v_dp:

    J_p = (+qp)(+μ_p E) = qpμ_p E

Electrons move against the field but carry negative charge, so their current is in the same direction as the hole current: both are along E.

**Step 3: total drift current density.**

    J_drift = J_n + J_p = q( nμ_n + pμ_p ) E

Comparing with Ohm's law J = σE:

    σ = q( nμ_n + pμ_p ),     ρ = 1/σ = 1 / [ q(nμ_n + pμ_p) ]

For an n-type sample (n ≫ p), σ ≈ qnμ_n ≈ qN_Dμ_n; for p-type, σ ≈ qN_Aμ_p. For an intrinsic sample, σ_i = qn_i(μ_n + μ_p).

### Q38. A semiconductor has an electron concentration of 2 × 10¹⁶ cm⁻³, electron mobility of 1350 cm²/V·s, and an electric field of 10 V/cm. Calculate the electron drift current density.

**Given:** n = 2×10¹⁶ cm⁻³, μ_n = 1350 cm²/V·s, E = 10 V/cm, q = 1.602×10⁻¹⁹ C.

    J_n = q n μ_n E
        = (1.602×10⁻¹⁹ C)(2×10¹⁶ cm⁻³)(1350 cm²/V·s)(10 V/cm)
        = (1.602×10⁻¹⁹)(2.7×10²⁰)   A/cm²
        = 43.3 A/cm²

**J_n ≈ 43.3 A/cm²** (= 4.33×10⁵ A/m²).

**Units check:** C · cm⁻³ · cm²/(V·s) · V/cm = C/(s·cm²) = A/cm². ✓

Supporting quantities:

- Drift velocity v_d = μ_nE = 1350 × 10 = 1.35×10⁴ cm/s (well below v_sat = 10⁷ cm/s, so the linear model is valid).
- Conductivity σ = qnμ_n = 4.33 S/cm, resistivity ρ = 0.231 Ω·cm, and J = σE = 4.33 × 10 = 43.3 A/cm². ✓

### Q41. Explain velocity saturation and hot-carrier effects in semiconductors.

**Velocity saturation.** At low fields, drift velocity is proportional to the field, v_d = μE, because carriers lose the energy they gain from the field to the lattice (acoustic phonons) and stay near thermal equilibrium. As the field increases (above about 10³–10⁴ V/cm in Si), carriers gain energy faster than acoustic-phonon scattering can remove it. Once their energy reaches the optical-phonon energy (≈ 0.063 eV in Si), they emit optical phonons very rapidly, which transfers energy to the lattice efficiently and limits further gain. The drift velocity therefore stops increasing and approaches a **saturation velocity**:

    v_sat ≈ 10⁷ cm/s  (Si, 300 K)

and is described empirically by v_d = μE/[1 + (μE/v_sat)^β]^{1/β}. The effective mobility v_d/E falls at high field. In GaAs the electron velocity peaks at about 2×10⁷ cm/s then decreases (negative differential mobility) because electrons transfer to the heavier L-valley.

**Consequences:** in short-channel MOSFETs the drain current becomes proportional to (V_GS − V_T) rather than (V_GS − V_T)², and the maximum transconductance and transit-time-limited speed are set by v_sat: f_T ≈ v_sat/(2πL).

**Hot-carrier effects.** Under high fields, carriers acquire an average kinetic energy far greater than the thermal value (3/2)kT; they are described by an effective electron temperature T_e ≫ T. These "hot" carriers cause:

1. **Impact ionisation**: carriers with energy above about 1.5E_g break bonds and create electron–hole pairs, leading to avalanche multiplication and **avalanche breakdown** of junctions.
2. **Hot-carrier injection into gate oxides**: hot electrons near the drain of a MOSFET surmount the 3.1 eV Si/SiO₂ barrier, become trapped in the oxide or create interface traps. The threshold voltage shifts and transconductance degrades over the device's life (hot-carrier degradation).
3. **Substrate and gate currents**: impact-generated holes flow to the substrate, which can forward-bias source junctions and trigger parasitic bipolar action or CMOS latch-up.
4. **Velocity overshoot**: in very short channels carriers transit before scattering brings them to steady state, briefly exceeding v_sat.
5. **Increased noise and light emission.**

**Mitigation:** lightly doped drain (LDD) structures to reduce the peak field, reduced supply voltage, graded junctions, and nitrided or hardened gate oxides.
