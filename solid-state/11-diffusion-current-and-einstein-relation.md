# Module 11 — Diffusion Current and the Einstein Relation

Examined in Q39–Q40. Carriers also move without any field, simply because there are more of them in one place than another. This is the current that flows in the neutral regions of a diode and the base of a transistor.

## 11.1 Diffusion

Random thermal motion produces a net flow from high to low concentration. With a gradient dn/dx, more carriers cross a plane from the crowded side than from the sparse side. The particle flux is proportional to the gradient (Fick's first law, Module 06):

    Φ_n = −D_n dn/dx,      Φ_p = −D_p dp/dx

D_n and D_p are the **diffusion coefficients** (cm²/s). In Si at 300 K, D_n ≈ 35 and D_p ≈ 12 cm²/s.

## 11.2 Diffusion current densities

Multiply the flux by the carrier charge:

    J_{n,diff} = (−q)(−D_n dn/dx) = +q D_n dn/dx
    J_{p,diff} = (+q)(−D_p dp/dx) = −q D_p dp/dx

Note the signs. Electrons and holes both flow down their gradients, but the electron's negative charge makes electron current flow **up** the electron gradient.

@fig figures/diffusion-current.svg | Carriers diffuse from high to low concentration. Because the electron charge is negative, the electron diffusion current points the opposite way to the electron flow.

## 11.3 The total current equations

When both a field and gradients are present:

    J_n = q n μ_n E + q D_n dn/dx
    J_p = q p μ_p E − q D_p dp/dx
    J = J_n + J_p

These two equations, together with the continuity equations (Module 13) and Poisson's equation, are the full set of **semiconductor device equations**.

## 11.4 The Einstein relation

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

## Exam questions solved

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
