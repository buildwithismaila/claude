# Week 9 — Continuity Equation and Surface Phenomena
<!-- group: Module 3 · Carrier Transport & Injection Phenomena -->

**Plan:** derivation and application of the minority-carrier continuity equation; semiconductor surface states and surface recombination velocity.

The continuity equation is the bookkeeping rule that ties together drift and diffusion (Week 7) with generation and recombination (Week 8). Surfaces add one more loss term to that bookkeeping.

## Deriving the continuity equation

Take a thin slab of area A between x and x + dx. The number of holes in it changes because of:

- holes flowing in at x and out at x + dx (current);
- generation inside it, G_p;
- recombination inside it, R_p.

    ∂p/∂t · A dx = [ J_p(x) − J_p(x + dx) ] A/q + (G_p − R_p) A dx

Divide by A dx and let dx → 0:

    ∂p/∂t = −(1/q) ∂J_p/∂x + G_p − R_p
    ∂n/∂t = +(1/q) ∂J_n/∂x + G_n − R_n

## The minority-carrier diffusion equation

For holes in n-type material, insert J_p = qpμ_pE − qD_p ∂p/∂x and R_p = Δp/τ_p. With low-level injection, uniform doping and a small or zero field:

    ∂Δp/∂t = D_p ∂²Δp/∂x² − μ_p E ∂Δp/∂x + G_L − Δp/τ_p

The terms are, in order: diffusion, drift, external generation, recombination.

### Standard solutions

| Situation | Equation | Solution |
|---|---|---|
| Uniform, no gradient, light off at t = 0 | dΔp/dt = −Δp/τ_p | Δp(t) = Δp(0)e^{−t/τ_p} |
| Uniform steady illumination | 0 = G_L − Δp/τ_p | Δp = G_Lτ_p |
| Steady injection at x = 0 into a long sample | 0 = D_p d²Δp/dx² − Δp/τ_p | Δp(x) = Δp(0)e^{−x/L_p} |
| Steady injection into a short sample of length W ≪ L_p | d²Δp/dx² ≈ 0 | Linear: Δp(x) = Δp(0)(1 − x/W) |

The **diffusion length**:

    L_p = √(D_p τ_p),     L_n = √(D_n τ_n)

is the average distance a minority carrier diffuses before recombining.

@fig figures/injection.svg | Steady-state minority-carrier profile when carriers are injected at x = 0 into a long n-type bar. The excess falls to 1/e in one diffusion length.

**Example.** n-Si with D_p = 12 cm²/s, τ_p = 1 μs: L_p = √(12 × 10⁻⁶) = 3.46×10⁻³ cm = 34.6 μm. The hole diffusion current at x = 0 is J_p = qD_pΔp(0)/L_p.

## Surfaces and surface states

At a surface the periodic lattice ends abruptly. Atoms there have unsatisfied bonds (**dangling bonds**), and adsorbed impurities and oxide defects add more. These create a high density of **surface states** (traps) distributed through the gap, typically 10¹⁰–10¹⁵ cm⁻². They:

- act as **SRH recombination centres**, so carriers recombine much faster at the surface than in the bulk;
- **trap charge**, bending the bands near the surface (depletion, accumulation or inversion) even with no applied bias;
- cause instability and noise, and in MOS devices shift the threshold voltage (interface trap density D_it).

### Surface recombination velocity

Because the recombination happens in an infinitesimally thin layer, it is described as a flux (per area), not a rate per volume:

    U_s = S · Δp(0)      [carriers cm⁻² s⁻¹]

S, the **surface recombination velocity** (cm/s), plays the role of a velocity with which excess carriers "flow into" the surface and disappear. With SRH statistics for surface traps of density N_st (cm⁻²):

    S = σ_p v_th N_st

The surface acts as a sink. Carriers diffuse towards it, so the boundary condition at the surface is

    D_p dΔp/dx |_{x=0} = S Δp(0)

Limits: S = 0 means a perfect, reflecting surface (no recombination); S → ∞ forces Δp(0) = 0, as at an Ohmic contact.

Typical values: bare or freshly etched Si 10⁴–10⁶ cm/s; thermally oxidised Si 10–100 cm/s; best passivated Si (Al₂O₃, SiNₓ, annealed SiO₂) below 10 cm/s.

### Effective lifetime

In a wafer of thickness W with both surfaces recombining:

    1/τ_eff = 1/τ_bulk + 2S/W          (for small S)

**Example.** τ_bulk = 100 μs, W = 300 μm = 0.03 cm, S = 100 cm/s: 2S/W = 6.7×10³ s⁻¹, 1/τ_bulk = 1×10⁴ s⁻¹, so τ_eff = 1/(1.67×10⁴) = 60 μs. Unpassivated (S = 10⁵ cm/s) it would fall to about 0.15 μs.

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

1. **Additional recombination path.** Mid-gap surface states are efficient SRH centres. Carriers that diffuse to the surface recombine there quickly, so the measured (effective) lifetime is lower than the bulk lifetime: 1/τ_eff = 1/τ_bulk + 1/τ_surface, with 1/τ_surface ≈ 2S/W for a wafer of thickness W recombining at both surfaces. In thin wafers and small devices surface recombination can dominate: a 300 μm wafer with τ_bulk = 100 μs falls to τ_eff ≈ 60 μs at S = 100 cm/s and below 1 μs at S = 10⁵ cm/s.
2. **Carrier depletion near the surface.** The excess carrier density falls towards the surface, creating a gradient that pulls more carriers there, so even carriers generated deep in the material are lost.
3. **Surface band bending.** Charge in surface states bends the bands, creating depletion or inversion layers. Under depletion, both electrons and holes are present in similar numbers near the surface, which maximises SRH recombination and generation.
4. **Leakage and noise.** Surface generation adds to reverse leakage current of junctions where they meet the surface; trapping and detrapping produces 1/f noise; charged states cause threshold-voltage drift and instability in MOS devices.
5. **Device performance.** High S reduces solar-cell efficiency (especially for blue light absorbed near the surface), reduces BJT current gain (surface recombination at the emitter–base perimeter), and degrades photodetector response.

**Reduction (passivation):** thermal oxidation (SiO₂) with forming-gas (H₂) anneal to tie up dangling bonds; silicon nitride and Al₂O₃ films with fixed charge for field-effect passivation; heavily doped surface layers (back-surface field) that repel minority carriers; and clean, damage-free surface preparation.
