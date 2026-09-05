# Module 06 — Time-Varying Fields and Maxwell's Equations

Everything so far assumed nothing changes with time. Release that assumption and
electric and magnetic fields stop being two subjects and become one.

## 6.1 Faraday's law — changing B makes E

Experimental fact: a changing magnetic flux through a loop drives a current.

    emf = −dΨ/dt = −N dΨ/dt          [V]

The minus sign is **Lenz's law**: the induced current opposes the change that
created it. (If it did not, you would get free energy — the sign is required by
conservation of energy.)

In field terms:

    ∮_L E·dl = −d/dt ∫_S B·dS
    ∇ × E = −∂B/∂t                   (differential form)

**This kills electrostatics' central convenience.** ∮**E**·d**l** is no longer
zero, so **E** is no longer conservative and "the voltage at a point" is no longer
well-defined when fields vary in time. Circuit theory survives only because
loops are usually tiny compared to a wavelength.

### Three ways flux can change

emf = −∫ (∂**B**/∂t)·d**S**  +  ∮ (**u** × **B**)·d**l**
       ↑ transformer emf         ↑ motional emf

1. **Transformer emf** — stationary loop, time-varying B. The transformer.
2. **Motional emf** — moving conductor in a static B. The generator.
   For a rod of length ℓ moving at velocity u perpendicular to B: emf = Bℓu.
3. Both together — a rotating loop in a static field: Ψ = BS cos ωt, so
   emf = BSω sin ωt. That is the sinusoidal AC generator, derived in one line.

## 6.2 Displacement current — changing E makes B

Ampère's law ∇×**H** = **J** is **inconsistent** with charge conservation. Take
the divergence of both sides:

    ∇·(∇×H) = 0  ⇒  ∇·J = 0

But the continuity equation says ∇·**J** = −∂ρ_v/∂t, which is *not* zero when
charge accumulates.

**The physical paradox.** Apply Ampère's law to a loop around a wire feeding a
capacitor. Stretch a flat surface across the loop: current I passes through, so
∮**H**·d**l** = I. Now stretch a bulging surface that passes *between* the
capacitor plates: no conduction current crosses it, so ∮**H**·d**l** = 0. Same
loop, two answers. Something is missing.

**Maxwell's fix.** Add a term:

    ∇ × H = J + ∂D/∂t

**J**_d = ∂**D**/∂t is the **displacement current density**. Between the
capacitor plates, the changing E-field supplies exactly the missing current, and
both surfaces now give the same answer. Check:
∇·(∇×**H**) = ∇·**J** + ∂(∇·**D**)/∂t = −∂ρ_v/∂t + ∂ρ_v/∂t = 0 ✓

This term is not bookkeeping. It is the reason electromagnetic waves exist: a
changing E makes an H, whose change makes an E, and the pair walks off into
space needing no charges at all. Maxwell predicted light from this in 1865.

**Ratio of conduction to displacement current** (harmonic fields, e^{jωt}):

    |J_c|/|J_d| = σ/(ωε)         "loss tangent" tan δ

- σ/ωε ≫ 1 → good conductor (copper is a conductor up to optical frequencies)
- σ/ωε ≪ 1 → good dielectric
- The classification is **frequency-dependent**: wet soil is a conductor at 60 Hz
  and a dielectric at 10 GHz.

## 6.3 Maxwell's equations — the complete set

### Differential form (point form)

| Equation | Name | Says |
|---|---|---|
| ∇·**D** = ρ_v | Gauss's law | charge is the source of E-flux |
| ∇·**B** = 0 | Gauss's law (magnetic) | no magnetic charge |
| ∇×**E** = −∂**B**/∂t | Faraday | changing B curls E |
| ∇×**H** = **J** + ∂**D**/∂t | Ampère–Maxwell | current and changing D curl H |

### Integral form

| Equation |
|---|
| ∮_S **D**·d**S** = ∫_v ρ_v dv = Q_enc |
| ∮_S **B**·d**S** = 0 |
| ∮_L **E**·d**l** = −d/dt ∫_S **B**·d**S** |
| ∮_L **H**·d**l** = ∫_S (**J** + ∂**D**/∂t)·d**S** |

### Constitutive relations (the material's contribution)

    D = εE,    B = μH,    J = σE

Four field equations + three constitutive relations + boundary conditions =
a complete, solvable description of all classical electromagnetism.

### Time-harmonic (phasor) form
For fields varying as e^{jωt}, replace ∂/∂t → jω:

    ∇·D_s = ρ_vs
    ∇·B_s = 0
    ∇×E_s = −jωB_s
    ∇×H_s = J_s + jωD_s

Phasors turn PDEs in space-and-time into PDEs in space alone. This is how every
practical problem from Module 07 on is actually solved. Recover the real field
with **E**(t) = Re{**E**_s e^{jωt}}.

## 6.4 Boundary conditions, general form

    a_n × (E₁ − E₂) = 0          tangential E continuous
    a_n × (H₁ − H₂) = K          tangential H jumps by surface current
    a_n · (D₁ − D₂) = ρ_S        normal D jumps by surface charge
    a_n · (B₁ − B₂) = 0          normal B continuous

At a perfect conductor (σ→∞): E_t = 0, H_n = 0, D_n = ρ_S, H_t = K.

## 6.5 Poynting's theorem — where the energy goes

Take **E**·(∇×**H**) − **H**·(∇×**E**) and use the identity
∇·(**E**×**H**) = **H**·(∇×**E**) − **E**·(∇×**H**):

    −∮_S (E × H)·dS = ∂/∂t ∫_v ½(εE² + μH²) dv + ∫_v σE² dv

Read it right to left:
- ∫σE² dv = **ohmic power dissipated** inside the volume
- ∂/∂t ∫½(εE²+μH²) dv = **rate of increase of stored field energy**
- Therefore the left side is the **power flowing in through the surface**.

Define the **Poynting vector**:

    S = E × H         [W/m²]

It gives the instantaneous power flow per unit area, in the direction of
propagation. **E**, **H**, **S** form a right-handed triad.

For time-harmonic fields, the time-average is

    S_avg = ½ Re{E_s × H_s*}        [W/m²]

**Worth pausing on:** in a DC circuit, energy does not flow *through* the copper.
**E** points along the wire (driving current) and **H** circles it, so
**S** = **E**×**H** points radially *into* the wire from the surrounding space.
The energy travels in the field around the conductor and is absorbed into the
wire as heat. The wire guides; the field carries. Once you accept that, the
transmission line and the waveguide are the same idea taken seriously.

## 6.6 Worked examples

**Example 1.** A conducting bar slides at 10 m/s along rails 0.5 m apart in
**B** = 0.2**a**_z T (rails in the xy-plane, bar along y, moving along x).
Find the emf.

emf = Bℓu = 0.2 × 0.5 × 10 = **1 V**
Direction: **u**×**B** = 10**a**_x × 0.2**a**_z = −2**a**_y, so the emf drives
current in the −**a**_y direction in the bar.

**Example 2.** A parallel-plate capacitor, plate area 5 cm², spacing 3 mm,
ε_r = 2, has v(t) = 50 sin(10³t) V applied. Find the displacement current.

E = v/d, D = εE = ε₀ε_r v/d
J_d = ∂D/∂t = (ε₀ε_r/d) dv/dt
I_d = J_d S = (ε₀ε_r S/d)(dv/dt) = C dv/dt
C = (8.854e−12)(2)(5e−4)/3e−3 = 2.95×10⁻¹² F
I_d = 2.95e−12 × 50 × 10³ cos(10³t) = **0.1476 cos(10³t) nA**

Note the result *is* I = C dv/dt. Displacement current is exactly what makes a
capacitor pass AC — a fact you already used in circuit theory without knowing why.

**Example 3.** Show that **E** = E₀ sin(ωt − βz)**a**_x satisfies Faraday's law
and find **H**.

∇×**E** = −∂E_x/∂z **a**_y = βE₀cos(ωt−βz)**a**_y
Set equal to −∂**B**/∂t: ∂**B**/∂t = −βE₀cos(ωt−βz)**a**_y
**B** = −(βE₀/ω) sin(ωt−βz)**a**_y ... integrating with zero DC term:
**B** = (βE₀/ω) sin(ωt−βz)**a**_y (sign convention aside, the point stands)

So **H** is perpendicular to **E**, in phase with it, and E/H = ω/(βμ) = η.
**S** = **E**×**H** is along **a**_z: the wave carries power in the direction of
travel. That is Module 07 in one example.

## 6.7 Exercises

1. A circular loop of radius 10 cm lies in the xy-plane in
   **B** = 0.5 sin(100t)**a**_z T. Find the induced emf.
2. Seawater has σ = 4 S/m, ε_r = 81. At what frequency are the conduction and
   displacement currents equal? (σ = ωε ⇒ f = σ/(2πε) ≈ 888 MHz.)
3. Show that ∇·**J** + ∂ρ_v/∂t = 0 follows from Maxwell's equations.
4. Compute the Poynting vector inside a cylindrical resistor of radius a,
   length ℓ, carrying I with voltage V across it. Show ∮**S**·d**S** = −VI,
   i.e. exactly the dissipated power flows inward.
5. Write Maxwell's equations in phasor form for a source-free lossless medium
   and combine them into a single equation in **E**_s.

## Takeaways

- Faraday: changing B curls E. Ampère–Maxwell: current *and* changing D curl H.
- Displacement current is not a correction; it is the mechanism of radiation.
- The four equations plus **D**=ε**E**, **B**=μ**H**, **J**=σ**E** are complete.
- **S** = **E**×**H** tells you where the energy actually is: in the field,
  not in the wire.
