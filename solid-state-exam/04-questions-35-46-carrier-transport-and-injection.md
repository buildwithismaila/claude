# Questions 35–46 — Carrier Transport and Injection
<!-- group: The 50 questions, answered -->

Module 3: how carriers move (drift, mobility, scattering, diffusion, the Einstein relation, high fields) and how excess carriers are generated, recombine and flow (SRH, lifetime, continuity, surfaces). Each question stands on its own: its key terms are defined with it, so you can start anywhere.

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
| h | Planck constant | 6.626×10⁻³⁴ J·s |
| m₀ | Free-electron mass | 9.11×10⁻³¹ kg |
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
| E_t | Energy level of a trap (recombination centre) in the gap | eV |
| n | Electron concentration (free electrons per m³) | m⁻³ |
| p | Hole concentration (holes per m³) | m⁻³ |
| n_i | Intrinsic carrier concentration (n = p = n_i in pure material) | m⁻³; Si ≈ 1×10¹⁶ at 300 K |
| n₀, p₀ | Equilibrium electron and hole concentrations | m⁻³ |
| N_D | Donor concentration | m⁻³ |
| N_A | Acceptor concentration | m⁻³ |
| Δn, Δp | Excess electron and hole concentrations above equilibrium | m⁻³ |
| m∗, m_n∗, m_p∗ | Effective mass of electrons or holes | kg, or as a multiple of m₀ |
| ν, hν | Frequency of light, and photon energy | Hz; eV |
| C(x, t) | Dopant concentration at depth x and time t | m⁻³ |
| D | Diffusion coefficient (dopants in a furnace, or carriers) | m²/s |
| F | Particle flux in Fick's law | particles/(m²·s) |
| Q | Dose: dopant atoms per unit area (in Weeks 13–14, Q also means charge) | atoms/m² (C or C/m² for charge) |
| R_p | Projected range: average depth at which implanted ions stop | μm |
| E (field) | Electric field (on band diagrams, E is energy instead) | V/m |
| μ, μ_n, μ_p | Mobility: drift velocity per unit field (electrons, holes) | m²/(V·s); Si μ_n 0.135, μ_p 0.048 |
| μ_L, μ_I | Mobility limited by lattice scattering, by ionised-impurity scattering | m²/(V·s) |
| v_d | Drift velocity | m/s |
| v_th | Thermal velocity of carriers | ≈ 10⁵ m/s at 300 K |
| v_sat | Saturation velocity at high field | ≈ 10⁵ m/s in Si |
| τ_m | Mean free time between collisions | s; about 0.1–1 ps |
| σ | Conductivity, q(nμ_n + pμ_p) (in Week 8, σ is also a capture cross-section) | S/m (siemens per metre) |
| ρ | Resistivity, 1/σ | Ω·m |
| J, J_n, J_p | Current density (total, electrons, holes) | A/m² |
| D_n, D_p | Diffusion coefficients of electrons and holes | m²/s; Si 3.5×10⁻³ and 1.24×10⁻³ |
| T_e | Electron temperature of hot carriers | K |
| G, G_L | Generation rate of electron–hole pairs (G_L: by light) | m⁻³s⁻¹ |
| R | Recombination rate | m⁻³s⁻¹ |
| U | Net recombination rate, R − G | m⁻³s⁻¹ |
| τ, τ_n, τ_p | Minority-carrier lifetime (τ_eff: effective, including surfaces) | s; Si 1 ns – 1 ms |
| N_t | Density of traps (recombination centres) | m⁻³ |
| σ_n, σ_p | Capture cross-section of a trap for electrons, holes | m² |
| n₁, p₁ | SRH parameters n_ie^{(E_t − E_i)/kT} and n_ie^{(E_i − E_t)/kT} | m⁻³ |
| L, L_n, L_p | Diffusion length √(Dτ): distance a minority carrier travels before recombining | μm or m |
| S | Surface recombination velocity | m/s |
| N_st | Density of surface traps | m⁻² |
| U_s | Recombination rate per unit area at a surface | m⁻²s⁻¹ |
| W | Depletion-region width (in Week 13 W_B, W_E are base and emitter widths; in Week 14 W is channel width) | μm or m |
| I_s, J_s (I_S) | Saturation current (density) of a diode or transistor | A; A/m² |
| A (area) | Device or contact area | m² |
| α | Common-base current gain, I_C/I_E | dimensionless; 0.98–0.999 |
| β | Common-emitter current gain, I_C/I_B (also h_FE) | dimensionless; 50–500 |
| N_E, W_E, D_E; N_B, W_B, D_B | Doping, width and minority diffusion coefficient of the emitter; of the base | m⁻³; μm; m²/s |
| f_T | Transition (cut-off) frequency | Hz |
| V_T (V_th) | Threshold voltage of a MOSFET | V |
| V_GS, V_DS, V_SB, V_G | Gate–source, drain–source, source–body and gate voltages | V |
| σ_i, ρ_i | Conductivity and resistivity of intrinsic (undoped) material; σ_doped after doping | S/m; Ω·m |
| F_n, F_p | Particle flux of electrons and holes (carriers crossing 1 m² per second) | m⁻²s⁻¹ |
| B_z, I_x, V_H | Hall effect: magnetic field (z), current (x) and Hall voltage | T (tesla); A; V |
| v_dn, v_dp | Drift velocity of electrons and holes | m/s |
| μ_i, τ_i (μ_L, μ_I, N_I) | Mobility and scattering time for one scattering mechanism (L: lattice, I: ionised impurity); N_I = ionised-impurity density | m²/(V·s); s; m⁻³ |
| J_drift, J_diff | Drift and diffusion parts of the current density | A/m² |
| G_th, R_th | Thermal generation and recombination rates (equal in equilibrium) | m⁻³s⁻¹ |
| G_n, G_p, R_n, R_p | Generation and recombination rates of electrons and holes | m⁻³s⁻¹ |
| f_t, e_n, e_p | Probability a trap is occupied by an electron; emission rates of electrons and holes from traps | dimensionless; s⁻¹ |
| r_a, r_b, r_c, r_d | SRH rates: electron capture, electron emission, hole capture, hole emission | m⁻³s⁻¹ |
| τ_b (τ_bulk), τ_surface | Lifetime from bulk recombination only; from surface recombination only | s |
| U_s, p_s, Δp_s | Surface recombination rate; hole density and excess at the surface | m⁻²s⁻¹; m⁻³ |
| I_gen, J_gen | Generation current (density) from carriers generated in the depletion region | A; A/m² |
| τ₀ (τ_g) | Effective generation lifetime in a depletion region | s |
| t | Time (or a thickness, where the text says so) | s (or m) |

**Abbreviations**

| Abbreviation | Meaning |
|---|---|
| Si | Silicon |
| GaAs | Gallium arsenide |
| SiO₂ | Silicon dioxide (silica), the oxide insulator |
| SRH | Shockley–Read–Hall (trap-assisted) recombination |
| LDD | Lightly doped drain |
| MOS | Metal–oxide–semiconductor |
| MOSFET | Metal–oxide–semiconductor field-effect transistor |
| CMOS | Complementary MOS (n- and p-channel MOSFETs together) |
| BJT | Bipolar junction transistor |
| LED | Light-emitting diode |
| IGBT | Insulated-gate bipolar transistor |
| TCAD | Technology computer-aided design (device simulation software) |


## Questions on this page

| Q | Question |
|---|---|
| 35 | Define carrier mobility and explain the factors that affect electron and hole mobility in semiconductors. |
| 36 | Explain the mechanisms responsible for carrier scattering in semiconductor materials. |
| 37 | Derive the expression for drift current density due to electrons and holes. |
| 38 | A semiconductor has an electron concentration of 2 × 10¹⁶ cm⁻³, electron mobility of 1350 cm²/V·s, and an electric field of 10 V/cm. Calculate the electron drift current density. |
| 39 | Explain diffusion current in a semiconductor and state Fick's law. |
| 40 | State and explain the Einstein relation between carrier mobility and diffusion coefficient. |
| 41 | Explain velocity saturation and hot-carrier effects in semiconductors. |
| 42 | What is meant by generation and recombination of charge carriers? |
| 43 | Explain the Shockley-Read-Hall (SRH) recombination mechanism. |
| 44 | Define minority-carrier lifetime and explain its significance in semiconductor devices. |
| 45 | Explain the continuity equation for minority carriers and discuss its application to semiconductor devices. |
| 46 | What is surface recombination velocity? Explain how semiconductor surface states affect carrier lifetime. |

## Model answers

### Q35. Define carrier mobility and explain the factors that affect electron and hole mobility in semiconductors.

> **Question type:** Definition and explanation · **Topic:** carrier mobility · **Full notes:** Week 7 (Drift and Diffusion Currents)

**What the examiner wants.** Two parts. First a precise definition of mobility, with its formula and unit. Then an explanation of each factor that changes mobility, saying *why* it does so (through the collision time or the effective mass), not just listing names.

**Key terms.**

- **Drift velocity (v_d):** the small average velocity carriers gain in the direction of an electric field (m/s).
- **Mobility (μ):** drift velocity per unit electric field, μ = v_d/E (m²/V·s).
- **Mean free time (τ_m):** the average time between two collisions of a carrier (about 0.1–1 ps).
- **Effective mass (m∗):** the mass a carrier appears to have when it is accelerated inside the crystal.
- **Scattering:** any collision that randomises a carrier's direction and destroys the velocity it gained from the field.
- **Phonon:** a quantum of lattice vibration; its number grows with temperature.
- **Matthiessen's rule:** when several scattering mechanisms act, 1/μ = 1/μ₁ + 1/μ₂ + …

**Model answer.**

#### Definition

Carrier mobility is the drift velocity a carrier gains per unit applied electric field. It measures how easily electrons or holes move through the crystal.

    μ = v_d / E = qτ_m / m∗

Where:

- μ = mobility (m²/V·s)
- v_d = drift velocity (m/s)
- E = electric field (V/m)
- q = electronic charge, 1.6×10⁻¹⁹ C
- τ_m = mean free time between collisions (s)
- m∗ = effective mass of the carrier (kg)

Electrons and holes have separate mobilities, μ_n and μ_p. In silicon at 300 K, μ_n = 0.135 and μ_p = 0.048 m²/V·s. The formula shows that mobility is high when collisions are rare (long τ_m) and the carrier is light (small m∗). Every factor below acts through one of these two quantities.

#### Factors affecting mobility

1. **Effective mass.** μ ∝ 1/m∗. Electrons usually have a smaller effective mass than holes, so μ_n > μ_p (Si 0.135 vs 0.048 m²/V·s; GaAs electrons, m∗ = 0.067m₀, reach about 0.85 m²/V·s).
2. **Temperature (lattice scattering).** Atoms vibrate more as T rises, so carriers collide with phonons more often and τ_m falls: μ_L ∝ T^{−3/2}. Near room temperature mobility falls as temperature rises.
3. **Temperature (impurity scattering).** Slow carriers are deflected more by charged ions. At higher T carriers move faster and are deflected less, so μ_I ∝ T^{3/2}/N_I rises with T. This dominates at low temperature.
4. **Doping concentration.** More ionised donors and acceptors mean more Coulomb scattering centres, so mobility falls as N_D + N_A rises (Si electrons: about 0.135 m²/V·s at light doping, about 0.080 m²/V·s at 10²³ m⁻³, about 0.010 m²/V·s at 10²⁶ m⁻³). Compensated material has low mobility even if the net doping is small, because both ion types scatter.
5. **Electric field.** At low field μ is constant. At high field (above about 10⁶ V/m in Si) carriers emit optical phonons, the drift velocity saturates near 10⁵ m/s, and the effective mobility v_d/E falls.
6. **Crystal defects.** Dislocations, grain boundaries and vacancies add scattering; polycrystalline and amorphous material have much lower mobility than single crystal.
7. **Surface and interface scattering.** In a MOSFET channel, carriers are pressed against the rough Si/SiO₂ interface and its trapped charges; channel mobility is roughly half the bulk value.
8. **Orientation, strain and carrier density.** Mobility depends on crystal direction and can be raised by strain (strained silicon); at very high carrier densities carrier–carrier scattering lowers it.

The separate effects combine through Matthiessen's rule:

    1/μ = 1/μ_L + 1/μ_I + …

Where:

- μ = total mobility (m²/V·s)
- μ_L = mobility limited by lattice scattering alone (m²/V·s)
- μ_I = mobility limited by ionised-impurity scattering alone (m²/V·s)

The smallest term dominates, so mobility against temperature rises at low T (impurity-limited), peaks, then falls at high T (lattice-limited).

@fig figures/mobility.svg | Mobility against temperature for light and heavy doping. Impurity scattering limits the low-temperature side, lattice scattering the high-temperature side; heavier doping lowers the curve and moves the peak to a higher temperature.

Sketch: log μ against log T, a curve rising as T^{3/2} then falling as T^{−3/2}; label "impurity scattering" and "lattice scattering", and draw a lower curve labelled "higher N_I".

**Marking checklist.** The points a marker looks for. Tick each one off in your own answer:

- ✓ definition μ = v_d/E with unit m²/V·s
- ✓ μ = qτ_m/m∗, linking mobility to collision time and effective mass
- ✓ effective mass: why μ_n > μ_p, with Si values 0.135 and 0.048 m²/V·s
- ✓ lattice scattering, μ_L ∝ T^{−3/2}
- ✓ ionised-impurity scattering, μ_I ∝ T^{3/2}/N_I, and fall of μ with doping
- ✓ high-field effect (velocity saturation)
- ✓ at least one further factor: defects, surface scattering, strain
- ✓ Matthiessen's rule and/or the sketch of μ against T

**Common mistakes.**

- Saying "mobility increases with temperature" without qualification: near room temperature it decreases; it only increases at low T where impurity scattering dominates.
- Defining mobility as "the speed of a carrier": it is velocity *per unit field*, so its unit is m²/V·s, not m/s.
- Listing factors with no reason: always say whether the factor changes τ_m or m∗.
- Adding mobilities directly: it is the reciprocals that add.

**Remember it.** "Mobility = q τ over m": anything that shortens the time between bumps, or makes the carrier heavier, slows it down.

**Try a variant.** In a silicon sample the lattice-limited mobility is 0.135 m²/V·s and the impurity-limited mobility is 0.200 m²/V·s. Find the total electron mobility. *Answer:* 1/μ = 1/0.135 + 1/0.200 = 7.41 + 5.00 = 12.41 V·s/m², so **μ ≈ 0.0806 m²/V·s**, lower than either value alone.

---

### Q36. Explain the mechanisms responsible for carrier scattering in semiconductor materials.

> **Question type:** Explanation · **Topic:** carrier scattering · **Full notes:** Week 7 (Drift and Diffusion Currents)

**What the examiner wants.** Say what scattering is and why it happens (anything that breaks the perfect periodicity of the crystal), then explain each mechanism: its physical cause, when it dominates, and how it depends on temperature and doping. Finish with how the mechanisms combine.

**Key terms.**

- **Scattering:** a collision that changes a carrier's momentum and randomises the velocity it gained from a field.
- **Periodic potential:** the regularly repeating electric potential of a perfect crystal lattice; a carrier moves through it without scattering (Bloch's theorem).
- **Phonon:** a quantum of lattice vibration. *Acoustic* phonons are low-energy; *optical* phonons are high-energy (about 63 meV in Si).
- **Ionised impurity:** a donor (+) or acceptor (−) ion that has given up or taken an electron and so carries a charge.
- **Mean free time (τ_m):** the average time between collisions.
- **Mobility (μ):** drift velocity per unit field, μ = qτ_m/m∗ (m²/V·s).
- **Matthiessen's rule:** scattering rates add, so 1/μ = Σ 1/μ_i.

**Model answer.**

#### Why scattering happens

In a perfectly periodic, perfectly still crystal an electron would travel freely with no collisions (Bloch's theorem). Scattering happens whenever something breaks that perfect periodicity. Each scattering event randomises the carrier's direction, so it limits the mean free time τ_m and hence the mobility, μ = qτ_m/m∗.

#### The mechanisms

1. **Lattice (phonon) scattering.** Above 0 K the atoms vibrate about their sites and distort the periodic potential. Carriers exchange energy and momentum with these vibrations (phonons). *Acoustic-phonon* scattering is nearly elastic and dominates in lightly doped Si at room temperature. More vibration at higher T means more scattering, giving μ_L ∝ T^{−3/2}. *Optical-phonon* scattering (phonon energy about 63 meV in Si) becomes important at high temperature and high field, and causes velocity saturation.
2. **Polar-optical and piezoelectric scattering.** In compound semiconductors such as GaAs the bonds are partly ionic, so vibrating atoms create electric fields that scatter carriers strongly.
3. **Ionised-impurity scattering.** The Coulomb field of each charged donor or acceptor ion deflects a passing carrier, like a charged particle passing a nucleus (Rutherford scattering). A slow carrier spends longer near the ion and is deflected more. It is therefore strongest at low temperature and high doping: μ_I ∝ T^{3/2}/N_I, where N_I is the ionised-impurity concentration.
4. **Neutral-impurity scattering.** Un-ionised dopant atoms distort the lattice potential slightly. This is weak and matters only at very low temperature, when dopants are frozen out.
5. **Carrier–carrier scattering.** Electrons and holes repel or attract one another. Important only at very high carrier densities (heavily doped or strongly injected regions).
6. **Defect scattering.** Dislocations, grain boundaries, stacking faults and vacancies disturb the lattice; dislocations in n-type material can also be charged lines.
7. **Surface and interface scattering.** Carriers confined near a surface (a MOSFET channel at the Si/SiO₂ interface) are scattered by surface roughness, interface traps and oxide charge; channel mobility is about half the bulk value.
8. **Alloy scattering.** In alloys such as SiGe or Al_{x}Ga_{1−x}As the random placement of different atoms makes the potential non-periodic.
9. **Intervalley scattering.** A carrier absorbs or emits a phonon and moves to another conduction-band minimum; in GaAs this causes negative differential mobility (the Gunn effect).

#### Combining the mechanisms

The scattering rates add, 1/τ = Σ 1/τ_i, so the mobilities combine by Matthiessen's rule:

    1/μ = 1/μ_L + 1/μ_I + …

Where:

- μ = total mobility (m²/V·s)
- μ_L = lattice-limited mobility (m²/V·s)
- μ_I = ionised-impurity-limited mobility (m²/V·s)

The mechanism with the lowest mobility dominates. In lightly doped Si near 300 K this is lattice scattering; in heavily doped Si or at low temperature it is ionised-impurity scattering.

@fig figures/mobility.svg | The two main mechanisms compete: impurity scattering sets the rising, low-temperature side of the mobility curve and lattice scattering the falling, high-temperature side.

Sketch: log μ against log T with the T^{3/2} impurity branch and the T^{−3/2} lattice branch, and the actual curve passing under both.

**Marking checklist.** The points a marker looks for. Tick each one off in your own answer:

- ✓ scattering is caused by any departure from a perfect periodic lattice
- ✓ lattice (phonon) scattering, acoustic and optical, with μ_L ∝ T^{−3/2}
- ✓ ionised-impurity (Coulomb) scattering, with μ_I ∝ T^{3/2}/N_I
- ✓ neutral-impurity and carrier–carrier scattering, and when they matter
- ✓ defect and surface/interface scattering
- ✓ at least one of: polar, alloy, intervalley scattering
- ✓ Matthiessen's rule and which mechanism dominates where

**Common mistakes.**

- Saying the electron "collides with the atoms" of a perfect lattice: a perfect still lattice does not scatter; only vibrations and imperfections do.
- Getting the temperature dependence of impurity scattering backwards: it is *weaker* at high T, because fast carriers are deflected less.
- Giving only two mechanisms: the question says "mechanisms", so cover at least five with a reason for each.

**Remember it.** "Shake, charge, break": the lattice shakes (phonons), ions are charged (impurities), the crystal breaks (defects and surfaces).

**Try a variant.** Lattice-limited electron mobility in Si is 0.135 m²/V·s at 300 K. Estimate it at 400 K, assuming μ_L ∝ T^{−3/2}. *Answer:* μ_L = 0.135 × (400/300)^{−3/2} = 0.135 × 0.650 = **≈ 0.0877 m²/V·s**: heating by 100 K cuts the lattice-limited mobility by about a third.

---

### Q37. Derive the expression for drift current density due to electrons and holes.

> **Question type:** Derivation · **Topic:** drift current · **Full notes:** Week 7 (Drift and Diffusion Currents)

**What the examiner wants.** A step-by-step derivation starting from "current density = charge × concentration × velocity", showing how the drift velocity follows from the field (v_d = μE), handling the signs for electrons and holes, and ending with J = q(nμ_n + pμ_p)E, the conductivity σ and the resistivity ρ. State assumptions first and box the final result.

**Key terms.**

- **Drift:** carrier motion caused by an electric field.
- **Drift velocity (v_d):** the average velocity carriers gain from the field, on top of their random thermal motion (m/s).
- **Mobility (μ_n, μ_p):** drift velocity per unit field (m²/V·s).
- **Current density (J):** charge crossing unit area per unit time (A/m²).
- **Effective mass (m∗):** the apparent mass of a carrier accelerated inside the crystal.
- **Mean free time (τ_m):** average time between collisions (s).
- **Conductivity (σ):** J/E, the material's ability to carry current (S/m); resistivity ρ = 1/σ (Ω·m).

**Model answer.**

Sketch: a bar of semiconductor of cross-section A with the field E pointing in +x. Draw holes (⊕) drifting along +x and electrons (⊖) drifting along −x; draw both current arrows J_p and J_n pointing along +x.

#### Assumptions

- The semiconductor is uniform (n and p do not vary with position), so there is no diffusion current.
- Steady state, with a uniform field E in the +x direction.
- The field is low enough that carriers stay near thermal equilibrium, so v_d is proportional to E (no velocity saturation).
- Each carrier type has a constant effective mass m∗ and mean free time τ_m.

#### Derivation

**Step 1. Force on a carrier.** An electron (charge −q) feels F = −qE; a hole (charge +q) feels F = +qE.

**Step 2. Drift velocity of electrons.** In steady state the momentum each electron gains from the field per unit time equals the momentum lost in collisions, which on average is m_n∗v_dn/τ_mn:

    m_n∗ v_dn / τ_mn = −qE   ⇒   v_dn = −(qτ_mn / m_n∗) E = −μ_n E

Where:

- v_dn = electron drift velocity (m/s)
- m_n∗ = electron effective mass (kg)
- τ_mn = electron mean free time (s)
- μ_n = qτ_mn/m_n∗ = electron mobility (m²/V·s)
- E = electric field (V/m)

The minus sign shows electrons drift against the field.

**Step 3. Drift velocity of holes.** By the same argument with charge +q:

    v_dp = +(qτ_mp / m_p∗) E = +μ_p E

Holes drift along the field.

**Step 4. Current density from charge × velocity.** Take a plane of area A across the bar. In time dt, every carrier within a distance v_d·dt behind the plane crosses it: that is a volume v_d·dt·A. If the concentration is c and each carrier has charge Q, the charge crossing is Q·c·v_d·dt·A. Dividing by A and dt:

    J = Q c v_d

Where:

- J = current density (A/m²)
- Q = charge per carrier (C)
- c = carrier concentration (m⁻³)
- v_d = drift velocity (m/s)

**Step 5. Electron drift current.** Put Q = −q, c = n, v_d = −μ_nE:

    J_n = (−q)(n)(−μ_n E) = qnμ_n E

The two minus signs cancel: electrons move against E, but because they are negative their current flows along E.

**Step 6. Hole drift current.** Put Q = +q, c = p, v_d = +μ_pE:

    J_p = (+q)(p)(+μ_p E) = qpμ_p E

**Step 7. Total drift current.** Both components point along E, so they add:

    J_drift = J_n + J_p = qnμ_n E + qpμ_p E

**Step 8. Conductivity and resistivity.** Comparing with Ohm's law in the form J = σE:

    σ = q(nμ_n + pμ_p),     ρ = 1/σ = 1 / [q(nμ_n + pμ_p)]

#### Result

**J_drift = q(nμ_n + pμ_p)E, with σ = q(nμ_n + pμ_p) and ρ = 1/σ.**

Where:

- J_drift = total drift current density (A/m²)
- q = electronic charge, 1.6×10⁻¹⁹ C
- n, p = electron and hole concentrations (m⁻³)
- μ_n, μ_p = electron and hole mobilities (m²/V·s)
- E = electric field (V/m)
- σ = conductivity (S/m); ρ = resistivity (Ω·m)

#### Special cases

- n-type (n ≫ p): σ ≈ qN_Dμ_n. For N_D = 10²² m⁻³ in Si, σ = 1.6×10⁻¹⁹ × 10²² × 0.135 = 216 S/m.
- p-type (p ≫ n): σ ≈ qN_Aμ_p.
- Intrinsic (n = p = n_i): σ_i = qn_i(μ_n + μ_p) = 1.6×10⁻¹⁹ × 10¹⁶ × 0.183 = 2.93×10⁻⁴ S/m.

**Marking checklist.** The points a marker looks for. Tick each one off in your own answer:

- ✓ assumptions stated (uniform sample, low field, steady state)
- ✓ v_d = μE derived from force balance, with μ = qτ_m/m∗
- ✓ correct directions: electrons against E, holes along E
- ✓ J = (charge)(concentration)(velocity), justified by counting carriers crossing a plane
- ✓ J_n = qnμ_nE with the sign cancellation explained
- ✓ J_p = qpμ_pE
- ✓ boxed total J = q(nμ_n + pμ_p)E
- ✓ σ = q(nμ_n + pμ_p) and ρ = 1/σ, with n-type, p-type or intrinsic special case
- ✓ labelled sketch of carrier and current directions

**Common mistakes.**

- Writing J_n = −qnμ_nE and concluding the electron and hole currents cancel: they add, because the electron's negative charge and negative velocity cancel.
- Skipping the step J = (charge)(concentration)(velocity): it carries marks, so show the carrier-counting argument.
- Using the thermal velocity (about 10⁵ m/s) instead of the drift velocity: the random thermal motion averages to zero and carries no current.
- Forgetting to state the low-field assumption: v_d = μE fails at high field.

**Remember it.** "Charge × count × speed": J = (q)(n)(μE) for each carrier, and the two minus signs of the electron cancel.

**Try a variant.** Find the conductivity and resistivity of intrinsic silicon at 300 K. *Answer:* σ_i = qn_i(μ_n + μ_p) = 1.6×10⁻¹⁹ × 10¹⁶ × (0.135 + 0.048) = **2.93×10⁻⁴ S/m**, so ρ_i = 1/σ_i = **3.4×10³ Ω·m**.

---

### Q38. A semiconductor has an electron concentration of 2 × 10¹⁶ cm⁻³, electron mobility of 1350 cm²/V·s, and an electric field of 10 V/cm. Calculate the electron drift current density.

> **Question type:** Calculation · **Topic:** drift current · **Full notes:** Week 7 (Drift and Diffusion Currents)

**What the examiner wants.** A single-formula calculation. Marks come from writing the drift-current formula, substituting with units, and giving the answer with the correct unit (A/m²). A one-line comment on what the number means shows understanding.

**Key terms.**

- **Drift:** the motion of charge carriers caused by an electric field.
- **Mobility (μ_n):** how fast an electron drifts per unit field, v_d = μ_nE; unit m²/V·s.
- **Drift velocity (v_d):** the average velocity carriers gain from the field (m/s).
- **Current density (J):** current per unit cross-sectional area (A/m²).
- **Saturation velocity (v_sat):** the maximum drift velocity at high field, about 10⁵ m/s in Si.

**Model answer.**

**Given:** n = 2×10¹⁶ cm⁻³ = 2×10²² m⁻³, μ_n = 1350 cm²/V·s = 0.135 m²/V·s, E = 10 V/cm = 1000 V/m, q = 1.6×10⁻¹⁹ C.

**Find:** the electron drift current density J_n.

**Formula:**

    J_n = q n μ_n E

Where:

- J_n = electron drift current density (A/m²)
- q = electronic charge, 1.6×10⁻¹⁹ C
- n = electron concentration (m⁻³)
- μ_n = electron mobility (m²/V·s)
- E = electric field (V/m)

**Solution.**

Step 1. Drift velocity: v_d = μ_nE = 0.135 × 1000 = 135 m/s.

Step 2. Current density:

    J_n = 1.6×10⁻¹⁹ × 2×10²² × 0.135 × 1000 = 4.32×10⁵ A/m²

Step 3. Units check: C × m⁻³ × m²/(V·s) × V/m = C/(s·m²) = A/m².

**Answer:** **J_n = 4.32×10⁵ A/m²** (with q = 1.602×10⁻¹⁹ C, 4.33×10⁵ A/m²).

**What this means:** a field of only 1000 V/m drives 4.32×10⁵ A through every square metre; the drift velocity (135 m/s) is still far below the saturation velocity (10⁵ m/s), so the simple linear formula is valid.

**Marking checklist.** The points a marker looks for. Tick each one off in your own answer:

- ✓ J_n = qnμ_nE written down, with each symbol defined
- ✓ correct substitution with units
- ✓ answer 4.32×10⁵ A/m², with the unit
- ✓ comment that the field is low enough for v_d = μE to hold

**Common mistakes.**

- Mixing metres and centimetres: convert everything to SI first (m⁻³, m²/V·s, V/m) and the answer comes out in A/m².
- Forgetting q, and giving 2.7×10²⁴ as the "current".
- Giving the unit as A instead of A/m²: this is a current density, not a current.

**Remember it.** "J = q n μ E": charge × how many × how mobile × how hard you push.

**Try a variant.** p-type silicon has p = 5×10²¹ m⁻³ and μ_p = 0.048 m²/V·s in a field of 10⁴ V/m. Find the hole drift current density. *Answer:* J_p = qpμ_pE = 1.6×10⁻¹⁹ × 5×10²¹ × 0.048 × 10⁴ = **3.84×10⁵ A/m²**.

---

### Q39. Explain diffusion current in a semiconductor and state Fick's law.

> **Question type:** Explanation and statement · **Topic:** diffusion current · **Full notes:** Week 7 (Drift and Diffusion Currents)

**What the examiner wants.** Explain what causes diffusion current (random thermal motion plus a concentration gradient, no field needed), state Fick's law with its minus sign, and turn it into the electron and hole diffusion current densities with the correct signs. A labelled sketch and an example of where diffusion matters earn extra marks.

**Key terms.**

- **Diffusion:** net movement of particles from high to low concentration caused by their random thermal motion.
- **Concentration gradient (dn/dx, dp/dx):** the rate at which carrier concentration changes with position (m⁻⁴).
- **Flux (F):** number of particles crossing 1 m² per second (m⁻²s⁻¹).
- **Diffusion coefficient (D_n, D_p):** how fast carriers spread out (m²/s); in Si, D_n = 3.5×10⁻³ and D_p = 1.24×10⁻³ m²/s.
- **Diffusion current density:** the current carried by the diffusion flux of charged carriers (A/m²).
- **Minority carrier:** the less numerous carrier type (holes in n-type, electrons in p-type).

**Model answer.**

#### What diffusion current is

Carriers in a semiconductor move randomly at the thermal velocity (about 10⁵ m/s), changing direction at every collision. If the concentration is the same everywhere, as many carriers cross any plane from left to right as from right to left, and there is no net flow. If the concentration is higher on one side, more carriers cross from that side simply because there are more of them. The result is a net flow from high to low concentration, with no electric field needed. Because the carriers are charged, this flow is an electric current: the **diffusion current**.

Diffusion current is important wherever carrier gradients exist:

- in the neutral regions of a forward-biased p-n junction, where injected minority carriers diffuse away from the junction;
- in the base of a bipolar transistor;
- under non-uniform illumination (solar cells, photodetectors) and in non-uniformly doped material.

#### Fick's first law

The particle flux is proportional to the concentration gradient and flows down the gradient:

    F = −D dC/dx

Where:

- F = particle flux (m⁻²s⁻¹)
- D = diffusion coefficient (m²/s)
- C = particle concentration (m⁻³)
- dC/dx = concentration gradient (m⁻⁴)
- the minus sign = flow is from high to low concentration

For electrons and holes: F_n = −D_n dn/dx and F_p = −D_p dp/dx.

#### Diffusion current densities

Multiply each flux by the carrier's charge (−q for electrons, +q for holes):

    J_{n,diff} = (−q)(−D_n dn/dx) = +qD_n dn/dx
    J_{p,diff} = (+q)(−D_p dp/dx) = −qD_p dp/dx

Where:

- J_{n,diff}, J_{p,diff} = electron and hole diffusion current densities (A/m²)
- q = electronic charge, 1.6×10⁻¹⁹ C
- D_n, D_p = electron and hole diffusion coefficients (m²/s)
- n, p = electron and hole concentrations (m⁻³)

Both carriers flow down their gradient, but the electron current points *opposite* to the electron flow (negative charge), while the hole current points *with* the hole flow.

@fig figures/diffusion-current.svg | Electrons and holes both diffuse from high to low concentration; the electron current is opposite to the electron flow, the hole current is in the same direction as the hole flow.

Sketch: a concentration profile falling from left to right; draw the particle-flow arrows pointing right for both carriers, the hole current arrow pointing right and the electron current arrow pointing left.

**Example.** Electron concentration in Si falls linearly from 10²³ m⁻³ to zero over 1 μm (10⁻⁶ m). Then dn/dx = −10²⁹ m⁻⁴ and J_n = qD_n dn/dx = 1.6×10⁻¹⁹ × 3.5×10⁻³ × (−10²⁹) = −5.6×10⁷ A/m²: a large current, flowing in −x, from a modest gradient.

When a field is also present, the total currents are J_n = qnμ_nE + qD_n dn/dx and J_p = qpμ_pE − qD_p dp/dx.

**Marking checklist.** The points a marker looks for. Tick each one off in your own answer:

- ✓ cause: random thermal motion plus a concentration gradient; no field needed
- ✓ Fick's law F = −D dC/dx with the minus sign explained
- ✓ D defined with unit m²/s (Si values 3.5×10⁻³ and 1.24×10⁻³ m²/s)
- ✓ J_n = +qD_n dn/dx and J_p = −qD_p dp/dx with correct signs
- ✓ direction of electron current opposite to electron flow
- ✓ where diffusion matters (forward-biased diode, BJT base)
- ✓ labelled sketch or numerical example
- ✓ total current = drift + diffusion

**Common mistakes.**

- Giving both current densities the same sign: the electron one is +qD_n dn/dx, the hole one −qD_p dp/dx.
- Saying diffusion needs a field: it happens with no field at all.
- Stating Fick's law without the minus sign, which would send particles uphill.
- Confusing the diffusion of carriers (D about 10⁻³ m²/s) with dopant diffusion in a furnace (D about 10⁻¹⁷ m²/s).

**Remember it.** "Ink in water": carriers spread from crowded to empty; the electron's minus sign flips its current.

**Try a variant.** In n-type silicon the hole concentration falls linearly from 10²² m⁻³ to zero over 10 μm. Find the hole diffusion current density (D_p = 1.24×10⁻³ m²/s). *Answer:* dp/dx = −10²²/10⁻⁵ = −10²⁷ m⁻⁴, so J_p = −qD_p dp/dx = 1.6×10⁻¹⁹ × 1.24×10⁻³ × 10²⁷ = **1.98×10⁵ A/m²**, in the +x direction (with the hole flow).

---

### Q40. State and explain the Einstein relation between carrier mobility and diffusion coefficient.

> **Question type:** Statement and explanation · **Topic:** Einstein relation · **Full notes:** Week 7 (Drift and Diffusion Currents)

**What the examiner wants.** State the relation exactly for both carriers, say what kT/q is and its value at 300 K, explain *why* D and μ are linked (same collisions), and justify it, ideally with the equilibrium drift-equals-diffusion argument. A numerical use (finding D from μ) completes the answer.

**Key terms.**

- **Mobility (μ):** drift velocity per unit field (m²/V·s).
- **Diffusion coefficient (D):** constant in Fick's law, F = −D dC/dx (m²/s).
- **Thermal voltage (kT/q):** Boltzmann constant × temperature ÷ electronic charge; 0.0259 V at 300 K.
- **Thermal equilibrium:** no external bias or illumination; no net current flows and the Fermi level is flat.
- **Fermi level (E_F):** the energy at which the probability of occupation is one half.
- **Intrinsic level (E_i):** the Fermi level of the undoped material; it follows the band edges and the electrostatic potential.
- **Non-degenerate semiconductor:** doped lightly enough that Boltzmann statistics apply (E_F more than about 3kT from the band edges).

**Model answer.**

#### Statement

For a non-degenerate semiconductor, the ratio of diffusion coefficient to mobility equals the thermal voltage, for both electrons and holes:

    D_n / μ_n = D_p / μ_p = kT/q

Where:

- D_n, D_p = electron and hole diffusion coefficients (m²/s)
- μ_n, μ_p = electron and hole mobilities (m²/V·s)
- k = Boltzmann constant, 8.617×10⁻⁵ eV/K
- T = absolute temperature (K)
- q = electronic charge, 1.6×10⁻¹⁹ C
- kT/q = thermal voltage, 0.0259 V at 300 K

#### Why μ and D are linked

Drift (response to a field) and diffusion (response to a gradient) are done by the same carriers and are limited by the same collisions. Mobility is μ = qτ_m/m∗. Diffusion depends on how far a carrier travels between collisions, D = v_th²τ_m/3, and with (1/2)m∗v_th² = (3/2)kT this is D = kTτ_m/m∗. Dividing, the collision time τ_m and the effective mass m∗ cancel:

    D/μ = (kTτ_m/m∗) / (qτ_m/m∗) = kT/q

So a carrier that rarely collides both drifts easily and spreads quickly, and the ratio depends only on temperature.

#### Equilibrium proof

Take an n-type sample with non-uniform doping, in thermal equilibrium.

Step 1. Electrons diffuse from the high-doped side and uncover positive donor ions, creating an internal field E.

Step 2. That field drives a drift current back. With no external circuit the net current is zero:

    J_n = qnμ_nE + qD_n dn/dx = 0

Step 3. In equilibrium E_F is flat and n = n_i e^{(E_F − E_i)/kT}. E_i follows the electrostatic potential, dE_i/dx = qE, so

    dn/dx = −(n/kT) dE_i/dx = −(qn/kT) E

Step 4. Substituting into the zero-current condition:

    qnμ_nE − qD_n(qn/kT)E = 0   ⇒   D_n = (kT/q) μ_n

The same argument with holes gives D_p = (kT/q)μ_p.

#### Use and significance

- Mobility is easy to measure (Hall effect, conductivity), so D follows: Si electrons D_n = 0.0259 × 0.135 = 3.50×10⁻³ m²/s; holes D_p = 0.0259 × 0.048 = 1.24×10⁻³ m²/s.
- It links the drift and diffusion terms of the current equations and is needed for diffusion lengths L = √(Dτ) and diode saturation currents.
- In degenerate (very heavily doped) material Boltzmann statistics fail and D/μ is larger than kT/q.

**Marking checklist.** The points a marker looks for. Tick each one off in your own answer:

- ✓ D/μ = kT/q stated for both electrons and holes
- ✓ kT/q named the thermal voltage, 0.0259 V (about 26 mV) at 300 K
- ✓ physical reason: the same scattering limits both drift and diffusion
- ✓ equilibrium argument: drift current cancels diffusion current
- ✓ use of flat E_F and Boltzmann statistics to get dn/dx = −(qn/kT)E
- ✓ numerical example: D_n = 3.5×10⁻³ m²/s, D_p = 1.24×10⁻³ m²/s for Si
- ✓ limitation to non-degenerate material

**Common mistakes.**

- Writing μ/D = kT/q (upside down): check units, D/μ has units (m²/s)/(m²/V·s) = V.
- Using kT = 0.0259 J: it is 0.0259 eV, so kT/q = 0.0259 V.
- Forgetting the temperature dependence: kT/q scales with T, so at 350 K it is 0.0302 V, not 0.0259 V.
- Stating it without saying when it is valid (thermal equilibrium physics, non-degenerate doping).

**Remember it.** "D over μ is kT over q": spread over push equals thermal voltage, 26 mV at room temperature.

**Try a variant.** Electrons in a sample at 350 K have mobility 0.100 m²/V·s. Find their diffusion coefficient. *Answer:* kT/q = 8.617×10⁻⁵ × 350 = 0.0302 V, so D_n = (kT/q)μ_n = 0.0302 × 0.100 = **3.02×10⁻³ m²/s**.

---

### Q41. Explain velocity saturation and hot-carrier effects in semiconductors.

> **Question type:** Explanation · **Topic:** high-field effects · **Full notes:** Week 8 (High-Field Effects and Excess Carriers)

**What the examiner wants.** Two linked parts. Explain why drift velocity stops rising at high field (energy loss by optical-phonon emission), give v_sat for Si and sketch v_d against E. Then explain what hot carriers are and list their effects (impact ionisation, oxide injection, substrate current, velocity overshoot) with device consequences and cures.

**Key terms.**

- **Drift velocity (v_d):** average velocity carriers gain from a field; v_d = μE at low field.
- **Saturation velocity (v_sat):** the limiting drift velocity at high field, about 10⁵ m/s in Si at 300 K.
- **Optical phonon:** a high-energy lattice vibration (about 0.063 eV in Si) that can absorb a large amount of carrier energy in one collision.
- **Hot carrier:** a carrier whose average energy is far above the thermal value (3/2)kT; described by an electron temperature T_e much greater than the lattice temperature T.
- **Impact ionisation:** a hot carrier breaks a covalent bond and creates a new electron–hole pair.
- **Negative differential mobility:** a field range where more field gives less drift velocity (GaAs electrons).
- **LDD (lightly doped drain):** a MOSFET drain extension with lower doping that reduces the peak field.

**Model answer.**

#### Velocity saturation

At low field carriers lose the energy they gain from the field to acoustic phonons and stay close to thermal equilibrium, so the drift velocity is proportional to field: v_d = μE.

At high field (above about 10⁶ V/m in Si) carriers gain energy faster than acoustic-phonon scattering can remove it. Once a carrier's extra energy reaches the optical-phonon energy (about 0.063 eV in Si), it emits an optical phonon and loses that energy in one collision. Each time it speeds up it is knocked back, so the drift velocity stops growing and levels off at the saturation velocity:

    v_sat ≈ 1×10⁵ m/s   (Si electrons and holes, 300 K)

An empirical formula (Caughey–Thomas) joins the two regimes:

    v_d = μE / [1 + (μE/v_sat)^β]^{1/β}

Where:

- v_d = drift velocity (m/s)
- μ = low-field mobility (m²/V·s); Si μ_n = 0.135, μ_p = 0.048
- E = electric field (V/m)
- v_sat = saturation velocity (m/s)
- β = fitting exponent, about 2 for Si electrons and 1 for holes (dimensionless)

At low field this gives μE; at high field, v_sat. The effective mobility v_d/E therefore falls at high field.

**GaAs** behaves differently: electrons reach about 2×10⁵ m/s near 3.5×10⁵ V/m (350 kV/m), then slow down as they transfer to a heavier conduction-band valley (negative differential mobility, used in Gunn diodes).

@fig figures/velocity.svg | Drift velocity against electric field: silicon carriers rise linearly then level off near 10⁵ m/s; GaAs electrons peak near 2×10⁵ m/s and then fall.

Sketch: v_d against E on log axes; a straight line of slope μ at low field bending over to a flat line at v_sat = 10⁵ m/s; label the "ohmic region (v = μE)" and "saturation region".

**Consequences.** In short-channel MOSFETs carriers travel at v_sat over most of the channel, so drain current becomes proportional to (V_GS − V_T) instead of (V_GS − V_T)², and the speed is limited to f_T ≈ v_sat/(2πL); for a channel length L = 100 nm this is about 160 GHz.

#### Hot-carrier effects

When the field is high, the carriers' average kinetic energy rises far above (3/2)kT; they are "hot", with an effective temperature T_e much higher than the lattice temperature. Hot carriers cause:

1. **Impact ionisation and avalanche breakdown.** A carrier with energy above about 1.5E_g knocks an electron out of a bond, creating an electron–hole pair. The new carriers are also accelerated and do the same, giving avalanche multiplication and junction breakdown (used deliberately in avalanche photodiodes).
2. **Hot-carrier injection into the gate oxide.** Near a MOSFET drain some electrons exceed the 3.1 eV Si/SiO₂ barrier, enter the oxide and are trapped or create interface traps. The threshold voltage drifts and transconductance falls over the device's life: a major reliability problem.
3. **Substrate and gate currents.** Holes from impact ionisation flow into the substrate; this can forward-bias source junctions and trigger parasitic bipolar action or CMOS latch-up.
4. **Velocity overshoot.** In very short channels carriers cross before scattering brings them to steady state, briefly exceeding v_sat.
5. **Extra noise and light emission** from the hot-carrier region.

**Cures:** lightly doped drain (LDD) structures to spread the voltage drop and lower the peak field, lower supply voltages, graded junctions, and hardened (nitrided) gate oxides.

**Marking checklist.** The points a marker looks for. Tick each one off in your own answer:

- ✓ low field: v_d = μE, carriers near equilibrium
- ✓ mechanism of saturation: optical-phonon emission (about 0.063 eV in Si)
- ✓ v_sat ≈ 10⁵ m/s for Si, with a sketch of v_d against E
- ✓ GaAs peak and negative differential mobility (intervalley transfer)
- ✓ definition of hot carriers (energy ≫ (3/2)kT, T_e ≫ T)
- ✓ impact ionisation and avalanche breakdown
- ✓ hot-carrier injection into the oxide and threshold-voltage drift
- ✓ device consequences (short-channel MOSFET current, f_T) and cures (LDD)

**Common mistakes.**

- Saying carriers "cannot go faster than v_sat because of relativity" or "because the mobility becomes zero": the cause is optical-phonon emission, and μ is only *effectively* reduced.
- Calling hot carriers "carriers in a hot crystal": the crystal can be at room temperature; only the carriers are hot.
- Confusing v_sat (about 10⁵ m/s, the high-field drift limit) with the thermal velocity (also about 10⁵ m/s, random motion that carries no current).
- Listing hot-carrier effects without device consequences or cures.

**Remember it.** "Push too hard and the lattice pushes back": optical phonons cap the speed at 10⁵ m/s, and the excess energy makes carriers hot enough to break bonds and burrow into the oxide.

**Try a variant.** Using the Caughey–Thomas formula with β = 2, find the electron drift velocity in Si at E = 10⁶ V/m and compare it with the low-field prediction (μ_n = 0.135 m²/V·s, v_sat = 10⁵ m/s). *Answer:* μE = 1.35×10⁵ m/s, so v_d = 1.35×10⁵/√(1 + 1.35²) = 1.35×10⁵/1.68 = **8.0×10⁴ m/s**, about 40 % below the linear value of 1.35×10⁵ m/s. The linear formula already fails at this field (the crossover field v_sat/μ_n is only 7.4×10⁵ V/m).

---

### Q42. What is meant by generation and recombination of charge carriers?

> **Question type:** Definition / explanation · **Topic:** generation and recombination · **Full notes:** Week 8 (High-Field Effects and Excess Carriers)

**What the examiner wants.** "What is meant by" asks you to define both terms precisely, then show you understand them: name the mechanisms of each, state how they balance in equilibrium and what happens when they do not, and say why they matter in devices. A sketch of the recombination paths earns extra marks.

**Key terms.**

- **Conduction band / valence band:** the band of energies where electrons move freely / the band of energies occupied by the bonding electrons; they are separated by the band gap E_g (1.12 eV in Si).
- **Electron–hole pair:** a free electron in the conduction band together with the empty state (hole) it left in the valence band.
- **Generation rate (G):** number of electron–hole pairs created per unit volume per unit time (m⁻³s⁻¹).
- **Recombination rate (R):** number of electron–hole pairs destroyed per unit volume per unit time (m⁻³s⁻¹).
- **Trap:** a defect or impurity with an energy level inside the band gap that helps electrons and holes recombine.
- **Thermal equilibrium:** no light, no applied voltage, steady temperature; then n₀p₀ = n_i².
- **Minority-carrier lifetime (τ):** average time an excess minority carrier survives before it recombines.

**Model answer.**

#### Generation

Generation is any process that gives an electron enough energy to leave the valence band (or a level in the gap) and enter the conduction band, creating a free electron and a free hole. Its rate is G (m⁻³s⁻¹). The mechanisms are:

- **Thermal generation:** lattice vibrations (heat) supply the energy, either across the whole gap or in two steps through a trap level.
- **Optical generation:** a photon with energy hν ≥ E_g is absorbed and creates a pair (photodiodes, solar cells).
- **Impact ionisation:** a carrier accelerated by a strong field hits the lattice hard enough to break a bond (avalanche breakdown).
- **Tunnelling (Zener) generation:** at very high fields an electron tunnels straight from the valence band to the conduction band.

#### Recombination

Recombination is the reverse: a conduction-band electron falls back into an empty valence-band state, so one electron and one hole disappear together. The energy released (about E_g) leaves as a photon, as heat (phonons, i.e. lattice vibrations), or as kinetic energy of a third carrier. Its rate is R (m⁻³s⁻¹). The mechanisms are:

- **Direct (band-to-band, radiative):** the electron drops straight across the gap and emits a photon; dominant in direct-gap materials such as GaAs (LEDs, lasers).
- **Indirect (trap-assisted, Shockley–Read–Hall, SRH):** the electron drops in two steps via a trap level and gives off heat; dominant in silicon.
- **Auger:** the energy is handed to a third carrier; important at very high carrier densities.
- **Surface recombination:** SRH recombination through states at the surface.

@fig figures/recombination.svg | The three recombination paths: band-to-band (photon emitted), trap-assisted SRH (two steps via a gap level, heat released) and Auger (energy passed to a third carrier).

Sketch in the exam: E_c and E_v as two horizontal lines, a short dashed trap level E_t near mid-gap; draw a straight downward arrow (band-to-band, label "hν"), a two-step arrow via E_t (label "SRH, heat") and an upward arrow from E_v to E_c (label "generation").

#### Balance and imbalance

In thermal equilibrium thermal generation and recombination are equal, so the carrier densities stay constant:

    G_th = R_th   and   n₀p₀ = n_i²

Where:

- G_th, R_th = thermal generation and recombination rates (m⁻³s⁻¹)
- n₀, p₀ = equilibrium electron and hole concentrations (m⁻³)
- n_i = intrinsic carrier concentration, 1×10¹⁶ m⁻³ in Si at 300 K

When the balance is disturbed, the net rate U = R − G always acts to restore equilibrium:

- **Excess carriers (np > n_i²)**, e.g. from light or forward bias: U > 0, net recombination.
- **Carrier deficit (np < n_i²)**, e.g. in a reverse-biased depletion region: U < 0, net generation.

For low-level injection (excess much smaller than the majority density) in n-type material the net rate is proportional to the excess:

    U = Δp/τ_p

Where:

- U = net recombination rate (m⁻³s⁻¹)
- Δp = p − p₀ = excess hole (minority-carrier) concentration (m⁻³)
- τ_p = minority-carrier (hole) lifetime (s)

#### Why it matters

Generation and recombination set the reverse leakage current of diodes, the photocurrent of solar cells and photodetectors, the light output of LEDs, the current gain of bipolar transistors and the switching speed of p-n junctions.

**Marking checklist.** The points a marker looks for. Tick each one off in your own answer:

- ✓ generation defined as creation of electron–hole pairs, with rate G in m⁻³s⁻¹
- ✓ recombination defined as annihilation of a pair, energy released as photon, heat or to a third carrier
- ✓ at least three generation mechanisms (thermal, optical hν ≥ E_g, impact ionisation, tunnelling)
- ✓ the recombination mechanisms: direct, SRH (trap-assisted), Auger, surface
- ✓ equilibrium G_th = R_th with n₀p₀ = n_i²
- ✓ net recombination when np > n_i², net generation when np < n_i²
- ✓ U = Δp/τ for low-level injection
- ✓ labelled band diagram and one or two device examples

**Common mistakes.**

- Saying generation "creates electrons" only: generation across the gap always creates electrons and holes in pairs.
- Writing that recombination stops in equilibrium: both processes continue at equal rates; only the *net* rate is zero.
- Claiming direct recombination dominates in silicon: Si has an indirect gap, so trap-assisted (SRH) recombination dominates.
- Forgetting the units: G, R and U are per unit volume per unit time (m⁻³s⁻¹), not per second.

**Remember it.** Generation makes pairs, recombination breaks pairs, and nature always pushes np back towards n_i².

**Try a variant.** n-type silicon is uniformly illuminated, producing G_L = 1×10²⁶ m⁻³s⁻¹ pairs, and the hole lifetime is 1 μs. Find the steady-state excess hole concentration. *Answer:* in steady state generation equals net recombination, G_L = Δp/τ_p, so Δp = G_Lτ_p = 10²⁶ × 10⁻⁶ = **1×10²⁰ m⁻³**.

---

### Q43. Explain the Shockley-Read-Hall (SRH) recombination mechanism.

> **Question type:** Explanation · **Topic:** SRH (trap-assisted) recombination · **Full notes:** Week 8 (High-Field Effects and Excess Carriers)

**What the examiner wants.** Explain how a trap level in the band gap helps an electron and a hole recombine: the four capture and emission processes, the SRH rate equation with every symbol defined, and what it tells us (mid-gap traps are most effective, lifetime ∝ 1/N_t, low-level and depletion-region limits). A labelled energy diagram and a device application complete the answer.

**Key terms.**

- **Trap (recombination centre):** a localised energy level E_t inside the band gap caused by a defect or impurity (Au, Fe, Cu, vacancies, dislocations); N_t is its density (m⁻³).
- **Capture cross-section (σ_n, σ_p):** the effective target area a trap presents to an electron or a hole (m²).
- **Thermal velocity (v_th):** the average random speed of carriers, about 1×10⁵ m/s at 300 K.
- **Capture / emission:** a trap taking a carrier from a band / giving a carrier back to a band.
- **Intrinsic level (E_i):** the Fermi level of undoped material, close to mid-gap.
- **Phonon:** a quantum of lattice vibration; the energy given to the lattice as heat.
- **Low-level injection:** excess carrier density much smaller than the majority density.

**Model answer.**

#### 1. Principle

In an indirect-gap semiconductor such as silicon an electron cannot easily drop straight across the gap, because it would have to change its momentum and emit a photon at the same time. Instead it recombines in two smaller steps through a trap level E_t in the gap, a process analysed by Shockley, Read and Hall. The energy is released as heat (phonons), not light.

@fig figures/recombination.svg | SRH recombination (middle) uses a trap level in the gap as a stepping stone; band-to-band and Auger recombination are shown for comparison.

Sketch in the exam: E_c and E_v, a trap level E_t near mid-gap, and four arrows labelled (a) to (d) as in the table below.

#### 2. The four processes at a trap

| Process | What happens | Rate (m⁻³s⁻¹) |
|---|---|---|
| (a) Electron capture | a conduction-band electron drops into an empty trap | r_a = σ_n v_th n N_t(1 − f_t) |
| (b) Electron emission | a trapped electron is thermally lifted back to the conduction band | r_b = e_n N_t f_t |
| (c) Hole capture | the trapped electron drops to the valence band and fills a hole | r_c = σ_p v_th p N_t f_t |
| (d) Hole emission | a valence electron jumps into an empty trap, leaving a hole | r_d = e_p N_t(1 − f_t) |

Here f_t is the probability that a trap is occupied by an electron, and e_n, e_p are emission coefficients (s⁻¹). **Recombination is (a) followed by (c); generation is (d) followed by (b).**

#### 3. The SRH rate

In steady state the trap occupation does not change, so the net electron capture equals the net hole capture: r_a − r_b = r_c − r_d = U. Detailed balance in equilibrium gives e_n = σ_n v_th n₁ and e_p = σ_p v_th p₁. Solving for f_t and substituting gives the SRH net recombination rate:

    U = (np − n_i²) / [ τ_p(n + n₁) + τ_n(p + p₁) ]

    τ_n = 1/(σ_n v_th N_t),   τ_p = 1/(σ_p v_th N_t)

    n₁ = n_i e^{(E_t − E_i)/kT},   p₁ = n_i e^{(E_i − E_t)/kT}

Where:

- U = net recombination rate (m⁻³s⁻¹); negative U means net generation
- n, p = actual electron and hole concentrations (m⁻³)
- n_i = intrinsic carrier concentration, 1×10¹⁶ m⁻³ in Si
- τ_n, τ_p = electron and hole lifetimes (s)
- σ_n, σ_p = capture cross-sections (m²); v_th = thermal velocity (m/s); N_t = trap density (m⁻³)
- n₁, p₁ = the electron and hole densities there would be if E_F were at E_t (m⁻³)
- E_t, E_i = trap level and intrinsic level (eV); kT = 0.0259 eV at 300 K

#### 4. What the equation tells us

- **Driving force (np − n_i²).** Positive with excess carriers (recombination), negative when carriers are depleted (generation), zero in equilibrium.
- **Mid-gap traps are most effective.** If E_t is near a band edge, n₁ or p₁ becomes large, the denominator grows and U falls: a shallow trap just captures a carrier and re-emits it. Deep levels near E_i (such as gold in Si) are the efficient recombination centres.
- **U ∝ N_t.** More traps mean shorter lifetime, τ = 1/(σv_thN_t).
- **Low-level injection in n-type** (n ≫ p, n₁, p₁): U = Δp/τ_p. The rate is limited by the capture of the scarce minority carrier.
- **Reverse-biased depletion region** (n, p ≈ 0, E_t = E_i): U = −n_i/(τ_n + τ_p) = −n_i/2τ₀ with τ₀ = τ_n = τ_p, a net generation that gives the generation leakage current J_gen = qn_iW/2τ₀ (W = depletion width). For W = 1 μm (10⁻⁶ m) and τ₀ = 1 μs, J_gen = 1.6×10⁻¹⁹ × 10¹⁶ × 10⁻⁶/(2 × 10⁻⁶) = 8×10⁻⁴ A/m².

#### 5. Example and applications

With N_t = 1×10¹⁹ m⁻³, σ_p = 1×10⁻¹⁹ m² and v_th = 1×10⁵ m/s: τ_p = 1/(10⁻¹⁹ × 10⁵ × 10¹⁹) = 1×10⁻⁵ s = 10 μs.

- **Lifetime killing:** gold or platinum diffusion, or electron irradiation, adds mid-gap traps on purpose to cut τ to nanoseconds in fast-switching diodes and thyristors.
- **Lifetime preservation:** clean processing and gettering remove traps to keep τ long in solar cells, CCD imagers and low-leakage devices.

**Marking checklist.** The points a marker looks for. Tick each one off in your own answer:

- ✓ recombination through a trap level E_t in the gap, two steps, energy released as phonons
- ✓ why it dominates in Si (indirect gap makes direct recombination unlikely)
- ✓ the four processes (electron capture/emission, hole capture/emission) with a labelled diagram
- ✓ SRH equation U = (np − n_i²)/[τ_p(n + n₁) + τ_n(p + p₁)] with symbols defined
- ✓ τ = 1/(σv_thN_t)
- ✓ mid-gap traps most effective; shallow traps ineffective
- ✓ low-level limit U = Δp/τ_p; depletion-region generation −n_i/2τ₀
- ✓ an application (gold doping for fast diodes, or gettering for long lifetime)

**Common mistakes.**

- Saying SRH emits light: the energy goes to the lattice as heat; photons come from band-to-band recombination.
- Claiming the shallowest traps are the most effective: it is the deep, mid-gap traps.
- Writing τ = σv_thN_t instead of its inverse: more traps must give a *shorter* lifetime.
- Leaving out the generation case: the same equation with np < n_i² explains diode leakage current.

**Remember it.** An electron crossing a wide river uses a stepping stone in the middle; stones near the banks are no help.

**Try a variant.** n-type Si has N_D = 1×10²¹ m⁻³ and τ_n = τ_p = 1 μs, but the traps lie 0.3 eV above E_i instead of at mid-gap. Find the effective low-level lifetime. *Answer:* n₁ = n_i e^{0.3/0.0259} = 10¹⁶ × e^{11.58} = 1.07×10²¹ m⁻³ (p₁ ≈ 9×10¹⁰ m⁻³ is negligible). With n ≈ N_D ≫ p, U ≈ Δp × N_D/[τ_p(N_D + n₁)], so τ_eff = τ_p(1 + n₁/N_D) = 1 μs × (1 + 1.07) ≈ **2.1 μs**: moving the trap 0.3 eV off mid-gap roughly halves its effectiveness.

---

### Q44. Define minority-carrier lifetime and explain its significance in semiconductor devices.

> **Question type:** Definition and explanation · **Topic:** minority-carrier lifetime · **Full notes:** Week 8 (High-Field Effects and Excess Carriers)

**What the examiner wants.** A precise definition (with the equation U = Δp/τ and the exponential decay), how lifetime depends on traps, and then a list of devices where lifetime controls performance, each with the reason. Quote a number (for example a diffusion length) to show depth.

**Key terms.**

- **Minority carrier:** the less numerous carrier type: holes in n-type, electrons in p-type material.
- **Excess carrier concentration (Δp, Δn):** the carrier density above its equilibrium value, Δp = p − p₀ (m⁻³).
- **Low-level injection:** Δp much smaller than the majority-carrier density, so the majority density hardly changes.
- **Recombination rate (U):** net number of electron–hole pairs destroyed per m³ per second.
- **Diffusion coefficient (D):** how quickly carriers spread by diffusion (m²/s); D_p = 1.24×10⁻³ m²/s for holes in Si.
- **Diffusion length (L):** average distance a minority carrier diffuses before recombining, L = √(Dτ).
- **Trap density (N_t):** concentration of recombination centres in the gap (m⁻³).

**Model answer.**

#### Definition

The minority-carrier lifetime is the average time an excess minority carrier survives in a semiconductor before it recombines with a majority carrier. Under low-level injection it is defined by the recombination rate:

    U = Δp/τ_p      (holes in n-type);   U = Δn/τ_n      (electrons in p-type)

If the source of excess carriers (for example light) is removed at t = 0, the excess decays exponentially:

    Δp(t) = Δp(0) e^{−t/τ_p}

Where:

- U = net recombination rate (m⁻³s⁻¹)
- Δp(t) = excess hole concentration at time t (m⁻³); Δp(0) = its value at t = 0
- τ_p, τ_n = hole and electron minority-carrier lifetimes (s)
- t = time after the source is removed (s)

So τ is the time for the excess to fall to 1/e (37 %) of its starting value.

@fig figures/decay.svg | Under steady light the excess holds at Δp = G_Lτ_p; after the light is switched off it decays exponentially, falling to 1/e of its value in one lifetime τ_p.

Sketch in the exam: Δp against t, flat at G_Lτ_p, then an exponential fall after "light off", with τ_p marked where the curve reaches 0.37 of the start.

**What sets τ.** For trap-assisted (SRH) recombination, τ_p = 1/(σ_p v_th N_t), where σ_p is the trap capture cross-section (m²), v_th ≈ 10⁵ m/s the thermal velocity and N_t the trap density. Lifetime is inversely proportional to the trap density, so it is a sensitive measure of crystal purity: about 1 ns to 1 ms in silicon.

#### Significance in devices

1. **Diffusion length.** Carriers spread a distance L = √(Dτ) before recombining. For holes in Si with D_p = 1.24×10⁻³ m²/s and τ_p = 1 μs, L_p = √(1.24×10⁻³ × 10⁻⁶) = 3.5×10⁻⁵ m (35 μm). L decides how thick device regions can be.
2. **Diode current.** The saturation current J_s = qn_i²[D_p/(L_pN_D) + D_n/(L_nN_A)] depends on τ through L, and the depletion-region generation current qn_iW/2τ₀ is inversely proportional to τ. Short lifetime means more leakage.
3. **Switching speed.** A forward-biased diode stores minority charge Q = Iτ, which must be removed before it can turn off, so the reverse-recovery time is of the order of τ. Fast-recovery diodes are gold- or platinum-doped to cut τ to nanoseconds.
4. **Bipolar transistor gain.** Electrons injected into the base must cross it before recombining. The base transport factor is about 1 − W_B²/2L_n² (W_B = base width), so a long lifetime (L_n ≫ W_B) gives a high current gain β.
5. **Solar cells and photodetectors.** Photogenerated carriers must diffuse to the junction before they recombine; a longer L collects more of them, raising photocurrent and efficiency.
6. **LEDs and lasers.** The share of recombination that is radiative, and the maximum modulation speed (bandwidth roughly ∝ 1/τ), depend on lifetime.
7. **Power devices.** In p-i-n diodes and IGBTs a long lifetime gives conductivity modulation and a low on-state voltage but slow turn-off: a design trade-off.
8. **Material quality.** Because τ reacts strongly to metal contamination, it is measured (photoconductive decay) to monitor crystal growth and process cleanliness.

**Marking checklist.** The points a marker looks for. Tick each one off in your own answer:

- ✓ definition: average time an excess minority carrier exists before recombining
- ✓ U = Δp/τ_p under low-level injection
- ✓ Δp(t) = Δp(0)e^{−t/τ}; τ is the 1/e time
- ✓ τ = 1/(σv_thN_t): lifetime falls as trap density rises
- ✓ L = √(Dτ) with a numerical example
- ✓ at least four devices explained: diode leakage, switching speed, BJT gain, solar cells
- ✓ the speed-versus-gain/efficiency trade-off (gold doping)

**Common mistakes.**

- Defining lifetime for majority carriers: it is the *minority* carriers whose excess decays with τ, because their relative change is large.
- Saying "long lifetime is always good": it is good for gain and efficiency but bad for switching speed.
- Writing L = Dτ instead of L = √(Dτ): check the unit, √(m²/s × s) = m.
- Stating that τ is the time for all excess carriers to disappear: after one τ, 37 % are still there.

**Remember it.** Lifetime is how long, diffusion length is how far: L = √(Dτ).

**Try a variant.** Excess holes in n-type Si have τ_p = 1 μs. How long after the light is switched off does Δp fall to 10 % of its initial value? *Answer:* 0.1 = e^{−t/τ_p}, so t = τ_p ln 10 = 1 μs × 2.303 = **2.3 μs**.

---

### Q45. Explain the continuity equation for minority carriers and discuss its application to semiconductor devices.

> **Question type:** Explanation with derivation · **Topic:** continuity equation · **Full notes:** Week 9 (Continuity Equation and Surface Phenomena)

**What the examiner wants.** State the continuity equation as carrier conservation, derive it from a thin slab, reduce it to the minority-carrier diffusion equation with the assumptions stated, then show how it is solved and used in real devices (diode, BJT, solar cell, lifetime measurement). Standard solutions with their equations earn the "discuss application" marks.

**Key terms.**

- **Continuity equation:** a book-keeping statement that carriers are conserved: change = net inflow + generation − recombination.
- **Current density (J_p, J_n):** hole and electron current per unit area (A/m²).
- **Drift and diffusion:** carrier motion driven by an electric field E, and by a concentration gradient.
- **Excess carrier concentration (Δp):** p − p₀, the density above equilibrium (m⁻³).
- **Quasi-neutral region:** a region outside the depletion layer where the net charge, and so the field, is nearly zero.
- **Lifetime (τ_p):** average survival time of an excess minority carrier (s).
- **Diffusion length (L_p):** L_p = √(D_pτ_p), how far minority carriers travel before recombining (m).

**Model answer.**

#### 1. Statement

In any small volume, the rate at which the carrier density increases equals the net inflow due to current, plus generation, minus recombination. In one dimension:

    ∂p/∂t = −(1/q) ∂J_p/∂x + G_p − R_p

    ∂n/∂t = +(1/q) ∂J_n/∂x + G_n − R_n

Where:

- p, n = hole and electron concentrations (m⁻³); t = time (s); x = position (m)
- J_p, J_n = hole and electron current densities (A/m²)
- q = electronic charge, 1.6×10⁻¹⁹ C
- G_p, G_n = generation rates; R_p, R_n = recombination rates (m⁻³s⁻¹)

The signs differ because electrons carry negative charge: electron flow is opposite to J_n.

#### 2. Derivation (holes)

Take a slab of area A between x and x + dx.

- Holes flowing in at x per second: J_p(x)A/q. Holes flowing out at x + dx: J_p(x + dx)A/q.
- Holes created per second: G_pA dx; holes lost: R_pA dx.
- Rate of change of the number in the slab: (∂p/∂t)A dx = (1/q)[J_p(x) − J_p(x + dx)]A + (G_p − R_p)A dx.
- Using J_p(x + dx) − J_p(x) = (∂J_p/∂x)dx and dividing by A dx gives the hole equation above.

#### 3. Minority-carrier diffusion equation

For holes in uniformly doped n-type material, substitute the current J_p = qμ_ppE − qD_p ∂p/∂x and, for low-level injection, R_p − G_th = Δp/τ_p, with G_L the extra generation by light. Assume:

- low-level injection (Δp ≪ n₀), so recombination is Δp/τ_p;
- a quasi-neutral region, so E ≈ 0 and drift is negligible;
- uniform doping, so p₀ does not vary with x.

Then:

    ∂Δp/∂t = D_p ∂²Δp/∂x² − Δp/τ_p + G_L

Where:

- D_p = hole diffusion coefficient (m²/s), 1.24×10⁻³ m²/s in Si
- τ_p = hole (minority-carrier) lifetime (s)
- G_L = generation rate by light (m⁻³s⁻¹)

**This is the minority-carrier diffusion equation.** For electrons in p-type: ∂Δn/∂t = D_n ∂²Δn/∂x² − Δn/τ_n + G_L. Each term has a meaning: diffusion spreads carriers, recombination removes them, light creates them.

#### 4. Standard solutions and applications

- **Uniform light switched off (photoconductive decay):** no x-dependence and G_L = 0 give Δp(t) = Δp(0)e^{−t/τ_p}. Measuring the fall in conductivity gives the lifetime.
- **Steady uniform light:** ∂/∂t = 0 and no gradient give Δp = G_Lτ_p (photoconductors, light-dependent resistors).
- **p-n junction diode (long neutral region):** steady state, no light: D_p d²Δp/dx² = Δp/τ_p gives Δp(x) = Δp(0)e^{−x/L_p}. The diffusion current at the depletion edge, J_p = qD_pΔp(0)/L_p, leads to the Shockley diode equation.
- **Bipolar transistor (short base, W_B ≪ L_n):** recombination is negligible, the profile is almost a straight line, and its slope gives the collector current; the small recombination loss gives the base transport factor and current gain.
- **Solar cells and photodiodes:** with G_L(x) = G₀e^{−αx} (α = absorption coefficient) the solution gives the collected photocurrent and shows that L must be longer than the absorption depth 1/α.
- **Haynes–Shockley experiment:** a pulse of injected carriers drifts and spreads as a moving Gaussian; its speed gives μ_p, its spreading gives D_p, its shrinking area gives τ_p, confirming the Einstein relation.
- **Switching transients:** the time-dependent equation gives the stored charge and the reverse-recovery time of diodes.
- **Device simulation:** with Poisson's equation and the current equations, the continuity equations are solved numerically in every TCAD simulator.

@fig figures/injection.svg | Steady-state solution for holes injected at x = 0 into a long n-type bar: the excess decays exponentially with characteristic length L_p.

Sketch in the exam: Δp against x, starting at Δp(0) and decaying exponentially; mark L_p where it has fallen to 0.37 Δp(0).

**Worked number.** Holes injected into a long n-type Si bar with Δp(0) = 1×10²⁰ m⁻³, D_p = 1.24×10⁻³ m²/s, τ_p = 1 μs: L_p = √(1.24×10⁻³ × 10⁻⁶) = 3.52×10⁻⁵ m (35.2 μm), and J_p(0) = qD_pΔp(0)/L_p = 1.6×10⁻¹⁹ × 1.24×10⁻³ × 10²⁰/3.52×10⁻⁵ = 5.6×10² A/m².

**Marking checklist.** The points a marker looks for. Tick each one off in your own answer:

- ✓ physical statement: conservation of carriers (inflow + generation − recombination)
- ✓ ∂p/∂t = −(1/q)∂J_p/∂x + G − R and the electron form with the opposite sign
- ✓ slab derivation
- ✓ assumptions stated (low-level injection, E ≈ 0, uniform doping)
- ✓ minority-carrier diffusion equation ∂Δp/∂t = D_p∂²Δp/∂x² − Δp/τ_p + G_L
- ✓ standard solutions: e^{−t/τ}, G_Lτ, e^{−x/L_p}, linear profile in a short region
- ✓ at least three device applications (diode, BJT, solar cell, lifetime measurement)
- ✓ L_p = √(D_pτ_p) defined

**Common mistakes.**

- Getting the sign of the current term wrong for electrons: it is +(1/q)∂J_n/∂x because electrons are negative.
- Dropping the drift term without saying why: state that the region is quasi-neutral (E ≈ 0).
- Writing the recombination term as Δp × τ_p instead of Δp/τ_p.
- Using the long-region exponential for a narrow BJT base: when W ≪ L the profile is a straight line.

**Remember it.** "What comes in, plus what is made, minus what dies, is what piles up."

**Try a variant.** For the same bar (Δp(0) = 1×10²⁰ m⁻³, L_p = 35.2 μm), find the excess hole concentration at x = 2L_p. *Answer:* Δp = Δp(0)e^{−2} = 10²⁰ × 0.135 = **1.35×10¹⁹ m⁻³**: after two diffusion lengths only 13.5 % of the injected holes remain.

---

### Q46. What is surface recombination velocity? Explain how semiconductor surface states affect carrier lifetime.

> **Question type:** Definition and explanation · **Topic:** surface recombination · **Full notes:** Week 9 (Continuity Equation and Surface Phenomena)

**What the examiner wants.** Define S with its equation and unit, explain where surface states come from, then explain how they lower the effective lifetime, with the τ_eff formula and its limit of validity. A short number example and the ways of reducing S (passivation) complete a full-mark answer.

**Key terms.**

- **Surface states:** localised energy levels in the band gap at a surface, caused by broken (dangling) bonds, adsorbed atoms and oxide defects.
- **Dangling bond:** an unpaired bond left on a surface atom because the crystal ends there.
- **Surface recombination velocity (S):** the rate of recombination per unit area divided by the excess minority density at the surface (m/s).
- **Bulk lifetime (τ_bulk):** the lifetime set by recombination inside the volume alone (s).
- **Effective lifetime (τ_eff):** the lifetime actually measured, including both bulk and surface losses (s).
- **Diffusion coefficient (D):** how fast minority carriers spread by diffusion (m²/s); D_p = 1.2×10⁻³ m²/s for holes is used below.
- **Passivation:** treating a surface so that it has few active surface states.

**Model answer.**

#### 1. Surface recombination velocity

At a surface, recombination takes place in a very thin layer, so it is counted per unit area rather than per unit volume:

    U_s = S Δp_s

Where:

- U_s = surface recombination rate (m⁻²s⁻¹)
- S = surface recombination velocity (m/s)
- Δp_s = excess minority-carrier (hole) concentration at the surface (m⁻³)

S has the units of a velocity: it is the effective speed at which excess carriers flow into the surface and are annihilated. For surface traps of density N_st (m⁻²) with capture cross-section σ_p (m²):

    S = σ_p v_th N_st

with v_th ≈ 1×10⁵ m/s the thermal velocity. S appears in the diffusion equation as a boundary condition at the surface: carriers arriving by diffusion equal carriers recombining there, D_p dΔp/dx = SΔp_s.

- S = 0: an ideal surface, no recombination.
- S → ∞: every arriving carrier recombines, Δp_s = 0 (like an Ohmic contact).
- Typical values: bare Si 10²–10⁴ m/s; thermally oxidised Si 0.1–10 m/s; well-passivated Si below 0.1 m/s.

#### 2. Origin of surface states

The periodic crystal ends at the surface. Surface atoms have dangling bonds; there are also adsorbed impurities, oxide defects and contamination. Together they create a high density of localised levels spread through the band gap, many near mid-gap, which are exactly the levels that make efficient Shockley–Read–Hall (SRH, trap-assisted) recombination centres.

#### 3. How surface states affect lifetime

- **An extra recombination path.** Carriers that reach the surface recombine there quickly, so the measured lifetime is shorter than the bulk lifetime. The rates add:

    1/τ_eff = 1/τ_bulk + 1/τ_surface

- **Small S (SW/2D ≪ 1).** Carriers reach the surfaces easily and the excess is nearly uniform across a wafer of thickness W with both faces recombining, so 1/τ_surface = 2S/W.
- **Large S (diffusion limit).** The surfaces swallow carriers faster than diffusion can bring them, so the loss is limited by the time to diffuse to a surface. A good approximation for any S is:

    τ_surface ≈ W/(2S) + W²/(π²D)

Where:

- τ_eff, τ_bulk, τ_surface = effective, bulk and surface-limited lifetimes (s)
- W = wafer thickness (m)
- D = minority-carrier diffusion coefficient (m²/s)
- W/(2S) = time for the surfaces to remove carriers once they arrive; W²/(π²D) = time for carriers to diffuse to the surfaces, the shortest τ_surface can ever be

For small S the first term dominates and the formula reduces to 1/τ_surface = 2S/W.

- **Depletion of carriers near the surface.** Δp falls towards the surface, and the gradient keeps pulling carriers there, so even carriers generated deep inside are lost.
- **Surface band bending.** Charge in surface states bends the bands. Under depletion, electron and hole densities near the surface become similar, which maximises SRH recombination and generation.
- **Leakage, noise and instability.** Surface generation adds to junction leakage where the junction meets the surface; trapping and release of carriers gives 1/f noise; charged states shift MOS threshold voltages.
- **Device performance.** High S lowers solar-cell efficiency (especially for blue light absorbed near the surface), lowers BJT gain through recombination at the emitter edge, and weakens photodetector response.

#### 4. Worked example

**Given:** n-type Si wafer, W = 300 μm = 3×10⁻⁴ m, τ_bulk = 100 μs, D_p = 1.2×10⁻³ m²/s; oxidised faces S = 1 m/s; bare faces S = 10³ m/s.

**Find:** τ_eff in each case.

**Solution.**

Step 1. Oxidised: SW/2D = 1 × 3×10⁻⁴/(2.4×10⁻³) = 0.13 (small), so the simple formula applies.

    1/τ_eff = 1/10⁻⁴ + 2 × 1/(3×10⁻⁴) = 1.0×10⁴ + 6.7×10³ = 1.67×10⁴ s⁻¹   ⇒   τ_eff = 60 μs

Step 2. Bare: SW/2D = 10³ × 3×10⁻⁴/(2.4×10⁻³) = 125 (not small), so use the full form. W/(2S) = 3×10⁻⁴/(2 × 10³) = 0.15 μs; W²/(π²D) = (3×10⁻⁴)²/(9.87 × 1.2×10⁻³) = 7.6 μs; τ_surface ≈ 7.75 μs.

    1/τ_eff = 1/100 μs + 1/7.75 μs   ⇒   τ_eff ≈ 7.2 μs

**Answer:** **τ_eff = 60 μs (oxidised) and about 7.2 μs (bare).** The simple formula would wrongly give 0.15 μs for the bare wafer.

**What this means:** a good oxide keeps most of the bulk lifetime; with bare surfaces the surfaces control the lifetime, and the loss is then limited by how fast holes can diffuse 150 μm to the nearest face.

#### 5. Reducing surface recombination (passivation)

- Thermal SiO₂ followed by a forming-gas (H₂) anneal, which ties up dangling bonds.
- Silicon nitride or Al₂O₃ films whose fixed charge repels minority carriers (field-effect passivation).
- A heavily doped surface layer (back-surface field) that keeps minority carriers away from the surface.
- Clean, damage-free surface preparation.

Sketch in the exam: Δp against x across a wafer, flat-topped for small S and dropping towards both faces for large S; label the faces "S".

**Marking checklist.** The points a marker looks for. Tick each one off in your own answer:

- ✓ U_s = SΔp_s with S in m/s, and S = σ_pv_thN_st
- ✓ boundary condition D_p dΔp/dx = SΔp_s; limits S = 0 and S → ∞
- ✓ origin of surface states: dangling bonds, adsorbates, oxide defects, levels near mid-gap
- ✓ 1/τ_eff = 1/τ_bulk + 1/τ_surface
- ✓ 1/τ_surface = 2S/W only when SW/2D ≪ 1; diffusion limit τ_surface ≈ W/(2S) + W²/(π²D) for large S
- ✓ band bending and leakage/noise effects
- ✓ a numerical example or typical values of S
- ✓ passivation methods

**Common mistakes.**

- Using 1/τ_eff = 1/τ_bulk + 2S/W for a bare surface: when SW/2D is large it predicts absurdly short lifetimes; diffusion to the surface sets the limit W²/(π²D).
- Giving S the unit s⁻¹ or m⁻²s⁻¹: S is a velocity, m/s; U_s is the per-area rate.
- Adding lifetimes instead of rates: it is the *inverses* (1/τ) that add.
- Treating surface states as single levels near the band edges: they are spread through the gap, with many near mid-gap, which is why they recombine so well.

**Remember it.** The surface is a carrier trapdoor: S says how wide it opens, diffusion says how fast carriers can reach it.

**Try a variant.** Repeat the 300 μm wafer (τ_bulk = 100 μs, D_p = 1.2×10⁻³ m²/s) for a poorly passivated surface with S = 10² m/s. *Answer:* SW/2D = 10² × 3×10⁻⁴/(2.4×10⁻³) = 12.5, not small. τ_surface ≈ 3×10⁻⁴/(2 × 10²) + 7.6 μs = 1.5 μs + 7.6 μs = 9.1 μs; 1/τ_eff = 1/100 + 1/9.1 (μs⁻¹), so **τ_eff ≈ 8.3 μs** (the simple formula would wrongly give 1.5 μs).
