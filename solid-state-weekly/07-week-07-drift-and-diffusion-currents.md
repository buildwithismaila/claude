# Week 7 — Drift and Diffusion Currents
<!-- group: Module 3 · Carrier Transport & Injection Phenomena -->

**Plan:** carrier mobility, scattering mechanisms and conductivity; diffusion of carriers, Fick's law and the Einstein relation.

Carriers move in two ways: they **drift** when pushed by an electric field, and they **diffuse** when there are more of them in one place than another. Every device current is a mixture of the two.

## Part A: Drift, mobility and conductivity

## Thermal motion and drift

With no field, carriers move randomly at the thermal velocity

    v_th = √(3kT/m∗) ≈ 10⁷ cm/s   (Si electrons, 300 K)

colliding (scattering) every **mean free time** τ_m ≈ 0.1–1 ps. The random motion averages to zero, so there is no current.

Apply a field E. Between collisions each electron accelerates by −qE/m_n∗. On average it gains a velocity −qEτ_m/m_n∗ before a collision randomises it again. This small average velocity superimposed on the random motion is the **drift velocity**:

    v_dn = −(qτ_m/m_n∗) E = −μ_n E,      v_dp = +μ_p E

## Mobility

    μ = qτ_m / m∗      [cm²/V·s]

Mobility is drift velocity per unit field. It is high when scattering is rare (long τ_m) and the effective mass is small.

| Material | μ_n (cm²/V·s) | μ_p (cm²/V·s) |
|---|---|---|
| Si | 1350 | 480 |
| Ge | 3900 | 1900 |
| GaAs | 8500 | 400 |

Electrons are faster than holes in all three, mainly because of their smaller effective mass.

## Scattering mechanisms

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

## Factors affecting mobility

- **Temperature:** peaks, then falls as T^{−3/2} near and above room temperature (lattice-dominated).
- **Doping:** higher total impurity concentration lowers μ. In Si, μ_n falls from 1350 (light doping) to about 1000 at 10¹⁷ and about 100 cm²/V·s at 10²⁰ cm⁻³.
- **Effective mass:** smaller m∗ gives higher μ (GaAs electrons, 0.067m₀).
- **Electric field:** at high field μ falls (velocity saturation, Week 8).
- **Crystal quality and orientation:** defects and grain boundaries reduce μ; in MOSFETs electron mobility is highest on (100) and hole mobility on (110).
- **Strain:** tensile strain raises electron mobility in Si (used in modern CMOS).
- **Surfaces and interfaces.**

## Drift current density

    J_drift = q(nμ_n + pμ_p) E = σE

    σ = q(nμ_n + pμ_p),     ρ = 1/σ

For n-type: σ ≈ qN_Dμ_n. For p-type: σ ≈ qN_Aμ_p.

Sheet resistance of a uniformly doped layer of thickness t: R_s = ρ/t (Ω/□), measured by a four-point probe.

## Hall effect

A magnetic field B_z across a current I_x pushes carriers sideways, building a Hall voltage V_H. The Hall coefficient R_H = 1/qp (p-type, positive) or −1/qn (n-type, negative) gives the carrier type and density; combined with resistivity it gives mobility μ = |R_H|σ.

## Part B: Diffusion, Fick's law and the Einstein relation

## Diffusion

Random thermal motion produces a net flow from high to low concentration. With a gradient dn/dx, more carriers cross a plane from the crowded side than from the sparse side. The particle flux is proportional to the gradient (Fick's first law, Week 3):

    Φ_n = −D_n dn/dx,      Φ_p = −D_p dp/dx

D_n and D_p are the **diffusion coefficients** (cm²/s). In Si at 300 K, D_n ≈ 35 and D_p ≈ 12 cm²/s.

## Diffusion current densities

Multiply the flux by the carrier charge:

    J_{n,diff} = (−q)(−D_n dn/dx) = +q D_n dn/dx
    J_{p,diff} = (+q)(−D_p dp/dx) = −q D_p dp/dx

Note the signs. Electrons and holes both flow down their gradients, but the electron's negative charge makes electron current flow **up** the electron gradient.

@fig figures/diffusion-current.svg | Carriers diffuse from high to low concentration. Because the electron charge is negative, the electron diffusion current points the opposite way to the electron flow.

## The total current equations

When both a field and gradients are present:

    J_n = q n μ_n E + q D_n dn/dx
    J_p = q p μ_p E − q D_p dp/dx
    J = J_n + J_p

These two equations, together with the continuity equations (Week 9) and Poisson's equation, are the full set of **semiconductor device equations**.

## The Einstein relation

    D_n / μ_n = D_p / μ_p = kT/q

kT/q = 0.0259 V at 300 K is the **thermal voltage** V_T.

**Derivation.** Take a non-uniformly doped n-type sample, N_D(x), in equilibrium with no external connection.

**Step 1.** Electrons diffuse away from the heavily doped side, uncovering positive donor ions. This builds an internal field E that pulls them back.

**Step 2.** In equilibrium no net current flows, so drift balances diffusion:

    0 = q n μ_n E + q D_n dn/dx

**Step 3.** In equilibrium the Fermi level is flat, while E_c (and E_i) follow the electrostatic potential: E = (1/q) dE_c/dx. Using n = N_c exp(−(E_c − E_F)/kT):

    dn/dx = −(n/kT) dE_c/dx = −(n/kT) qE

**Step 4.** Substitute into step 2:

    0 = qnμ_n E − q D_n (nq/kT) E   ⇒   D_n/μ_n = kT/q

The same argument for holes gives D_p/μ_p = kT/q. The relation holds for any non-degenerate semiconductor in or near equilibrium.

**Meaning.** Diffusion and drift are both limited by the same scattering processes. A carrier that scatters rarely both drifts easily (high μ) and spreads quickly (high D). Once one is known, the other follows.

| | μ (cm²/V·s) | D = μkT/q (cm²/s) |
|---|---|---|
| Si electrons | 1350 | 35.0 |
| Si holes | 480 | 12.4 |
| GaAs electrons | 8500 | 220 |
| Ge electrons | 3900 | 101 |

---

## Examination questions solved (Q35–Q40)

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

### Q39. Explain diffusion current in a semiconductor and state Fick's law.

**Diffusion current** is the current produced by the net movement of carriers from a region of higher concentration to one of lower concentration, caused by their random thermal motion. No electric field is needed. If the concentration varies with position, more carriers cross any plane from the high-concentration side than from the low side simply because there are more of them, so a net flux results. Because the carriers are charged, this flux is a current.

Diffusion current is important wherever carrier gradients exist: in the neutral regions of a forward-biased p-n junction (injected minority carriers diffusing away from the junction), in the base of a bipolar transistor, under non-uniform illumination, and in non-uniformly doped material.

**Fick's (first) law.** The particle flux is proportional to the negative of the concentration gradient:

    F = −D dC/dx

where D is the diffusion coefficient (cm²/s). Applied to electrons and holes:

    Electron flux:  F_n = −D_n dn/dx       Hole flux:  F_p = −D_p dp/dx

**Diffusion current densities** (multiply by the charge, −q for electrons, +q for holes):

    J_{n,diff} = +q D_n dn/dx
    J_{p,diff} = −q D_p dp/dx

In three dimensions, J_n = qD_n∇n and J_p = −qD_p∇p.

**Example.** If the electron concentration falls linearly from 10¹⁷ cm⁻³ to 0 over 1 μm in Si (D_n = 35 cm²/s):

    dn/dx = −10¹⁷/10⁻⁴ = −10²¹ cm⁻⁴
    J_n = q D_n dn/dx = (1.602×10⁻¹⁹)(35)(−10²¹) = −5.6×10³ A/cm²

The negative sign means the current flows in the −x direction, while the electrons themselves flow in +x (down their gradient).

Total current when a field is present: J_n = qnμ_nE + qD_n dn/dx and J_p = qpμ_pE − qD_p dp/dx.

### Q40. State and explain the Einstein relation between carrier mobility and diffusion coefficient.

**Statement.**

    D_n/μ_n = kT/q,      D_p/μ_p = kT/q

The ratio of diffusion coefficient to mobility equals the thermal voltage kT/q (0.0259 V at 300 K), for both electrons and holes, in a non-degenerate semiconductor.

**Explanation.** Drift and diffusion are two responses of the same carriers, both limited by the same random scattering events. Mobility describes the response to an electric field (μ = qτ_m/m∗); diffusion describes the response to a concentration gradient (D = v_th²τ_m/3 ≈ kTτ_m/m∗). Dividing gives D/μ = kT/q: the scattering time and mass cancel, leaving only temperature.

**Derivation (equilibrium argument).** In a non-uniformly doped sample in thermal equilibrium, an internal field E develops such that the drift and diffusion currents cancel exactly:

    J_n = qnμ_nE + qD_n dn/dx = 0

In equilibrium E_F is constant and n = n_i exp((E_F − E_i)/kT). Since E_i varies with the electrostatic potential, dE_i/dx = qE, so

    dn/dx = −(n/kT) dE_i/dx = −(qn/kT) E

Substituting:

    qnμ_nE − qD_n(qn/kT)E = 0   ⇒   D_n = (kT/q)μ_n

**Uses.**

1. One measurement gives the other: mobility is easy to measure (Hall effect, conductivity), so D follows. Si electrons: D_n = 0.0259 × 1350 = **35 cm²/s**; holes: D_p = 0.0259 × 480 = **12.4 cm²/s**.
2. It links the drift and diffusion terms in the current equations and is needed to calculate diffusion lengths L = √(Dτ) and diode saturation currents.
3. It shows why the built-in voltage of a junction is set by kT/q times a logarithm of a concentration ratio.

For degenerate semiconductors the relation is modified (D/μ > kT/q), because carriers then obey Fermi–Dirac rather than Boltzmann statistics.
