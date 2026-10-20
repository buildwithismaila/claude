# Module 02 — Crystal Lattices, Structures and Miller Indices

Lecture note §13–§17 and §21–§26. Semiconductor devices are made on single-crystal wafers, so you need the language of crystals: lattices, unit cells, and Miller indices for planes and directions.

## 2.1 Lattice, basis and crystal

- A **lattice** is an ideal mathematical array of points repeated periodically in space. Every point has identical surroundings.
- A **basis** (motif) is the atom or group of atoms attached to each lattice point.
- **Crystal = lattice + basis.**

Materials come in three forms:

- **Single crystal:** periodic order throughout the whole piece. Required for devices (wafers).
- **Polycrystalline:** many small crystals (grains) at random orientation, joined at grain boundaries. Used for MOSFET gates (poly-Si).
- **Amorphous:** no long-range order. Examples: SiO₂ films, a-Si:H in thin-film solar cells.

## 2.2 The unit cell

The **unit cell** is a volume which, when translated through the lattice, fills all space and regenerates the whole crystal. It is described by three edge lengths a, b, c and three angles α, β, γ.

- The **primitive cell** contains exactly one lattice point (smallest possible).
- The **conventional cell** is chosen for convenience and symmetry; for cubic crystals it is the cube, which may contain several lattice points.
- **Lattice constant:** in a cubic crystal, the edge length a.
- **Coordination number:** number of nearest neighbours of each atom.
- **Atomic packing factor:** APF = (volume of atoms in the cell) / (volume of the cell).

## 2.3 The cubic lattices

| Structure | Atoms per cell | Coordination no. | Nearest-neighbour distance | APF |
|---|---|---|---|---|
| Simple cubic (SC) | 1 | 6 | a | 0.52 |
| Body-centred cubic (BCC) | 2 | 8 | (√3/2)a | 0.68 |
| Face-centred cubic (FCC) | 4 | 12 | (√2/2)a | 0.74 |
| Diamond cubic | 8 | 4 | (√3/4)a | 0.34 |

Counting atoms in a cubic cell: a corner atom is shared by 8 cells (counts 1/8), a face atom by 2 (counts 1/2), a body atom by 1.

- SC: 8 × 1/8 = 1
- BCC: 8 × 1/8 + 1 = 2
- FCC: 8 × 1/8 + 6 × 1/2 = 4
- Diamond: 8 × 1/8 + 6 × 1/2 + 4 inside = 8

## 2.4 Diamond-cubic structure (Si, Ge, C)

The diamond lattice is **two interpenetrating FCC lattices**, one displaced from the other by one quarter of the body diagonal, (a/4, a/4, a/4). Its Bravais lattice is FCC with a two-atom basis.

- Each atom has **4 nearest neighbours** at the corners of a regular tetrahedron, bond angle 109.5°.
- Bonds are strongly directional and covalent (sp³ hybrid orbitals).
- Open structure: APF only 0.34. This open space is why interstitial impurities and diffusion are possible.

For Si, a = 5.43 Å:

    nearest-neighbour distance  r = (√3/4)a = (1.732/4)(5.43 Å) = 2.35 Å
    atom density  N = 8/a³ = 8/(5.43×10⁻⁸ cm)³ = 5.0×10²² atoms/cm³

The atom density is worth remembering: doping at 10¹⁶ cm⁻³ means one impurity per 5 million Si atoms.

## 2.5 Zinc-blende structure (GaAs, InP, GaP)

Geometrically identical to diamond, but the two FCC sublattices hold **different atoms**: one Ga, one As. Each Ga has four As nearest neighbours and vice versa.

Because the two atoms differ, the crystal has **polarity** and **mixed covalent–ionic** bonding. It also lacks inversion symmetry, which gives piezoelectric and polar-optical effects. Opposite (111) faces are chemically different (a Ga face and an As face) and etch differently.

## 2.6 Wurtzite structure (GaN, ZnO, CdS)

Hexagonal, but still **tetrahedrally** coordinated. The difference from zinc blende is the stacking of close-packed layers: wurtzite stacks ABABAB (hexagonal), zinc blende stacks ABCABC (cubic). Wurtzite crystals have built-in **spontaneous polarisation** and strong piezoelectric fields, which matter in GaN LEDs and HEMTs.

## 2.7 Miller indices for planes

Miller indices (h k l) identify a family of parallel crystal planes.

**Procedure:**

1. Find the intercepts of the plane on the x, y, z axes in units of a, b, c.
2. Take the **reciprocals**.
3. Clear fractions by multiplying by the lowest common denominator.
4. Reduce to the smallest set of integers (if needed).
5. Write in round brackets: (h k l).

Rules:

- A plane **parallel** to an axis meets it at infinity; 1/∞ = 0, so that index is **0**.
- A **negative** intercept gives a negative index, written with a bar over it. In plain text it is written as −1 or 1̄, e.g. (1 1̄ 0).
- If a plane passes through the origin, shift the origin to a neighbouring lattice point first.

### Notation summary

| Notation | Meaning |
|---|---|
| (h k l) | One specific plane (or set of parallel planes) |
| {h k l} | Family of all planes equivalent by symmetry, e.g. {100} = (100), (010), (001), (1̄00), (01̄0), (001̄) |
| [u v w] | One specific direction |
| ⟨u v w⟩ | Family of equivalent directions, e.g. ⟨111⟩ = the 8 body diagonals |

### Directions

A direction [u v w] is the vector from the start point to the end point, with components reduced to the smallest integers. [100] is the x-axis, [010] the y-axis, [001] the z-axis, [110] lies in the x–y plane, [111] is the body diagonal.

In **cubic** crystals only, the direction [h k l] is **perpendicular** to the plane (h k l).

@fig figures/planes.svg | The three most important planes in a cubic crystal. Silicon wafers for MOS ICs are cut on (100); bipolar and some power wafers use (111).

## 2.8 Interplanar spacing

The perpendicular distance between adjacent planes of the same (h k l) set in a cubic crystal:

    d_{hkl} = a / √(h² + k² + l²)

Higher indices mean more closely spaced, less densely populated planes.

## 2.9 Why orientation matters in processing

- **Surface atom density** differs by plane: in Si, (100) has 6.8×10¹⁴ atoms/cm², (111) has 7.8×10¹⁴ atoms/cm².
- **Oxidation rate:** (111) oxidises faster than (100).
- **Interface traps:** (100) gives the lowest Si/SiO₂ interface-state density, so **MOS technology uses (100) wafers**.
- **Anisotropic etching:** KOH etches (100) far faster than (111), giving V-grooves with 54.7° walls, used in MEMS.
- **Cleavage:** wafers break along {111} planes in Si and {110} in GaAs.
- **Epitaxy:** the substrate orientation and lattice constant set the orientation and quality of the grown layer.
- **Ion implantation channelling:** along low-index directions ions travel deep; wafers are tilted about 7° to avoid it.

## 2.10 Worked examples from the lecture note

| Intercepts | Reciprocals | Clear fractions | Miller indices |
|---|---|---|---|
| a, 2b, 3c | 1, 1/2, 1/3 | × 6 | (6 3 2) |
| 2a, 3b, c | 1/2, 1/3, 1 | × 6 | (3 2 6) |
| a, b, ∞ | 1, 1, 0 | — | (1 1 0) |
| ∞, b, c | 0, 1, 1 | — | (0 1 1) |
| 2a, ∞, 2c | 1/2, 0, 1/2 | × 2 | (1 0 1) |
| a, 2b, 4c | 1, 1/2, 1/4 | × 4 | (4 2 1) |

Directions: from (0,0,0) to (1,2,1) gives [121]. From (1,1,1) to (0,2,3) the change is (−1, 1, 2), giving [1̄12]. From (1,0,1) to (3,2,0) the change is (2, 2, −1), giving [221̄].

Spacing: for Si (a = 5.43 Å), d₁₁₁ = 5.43/√3 = 3.135 Å. For a = 5.65 Å, d₂₂₀ = 5.65/√8 = 1.998 Å.

---

## Exam questions solved

### Q5. What is a crystal lattice? Explain the significance of crystal structure in semiconductor materials.

**Crystal lattice.** A crystal lattice is an infinite, periodic three-dimensional array of points in space such that every point has identical surroundings. It is generated by repeating a unit cell (edges a, b, c and angles α, β, γ) by translation. Attaching a basis of one or more atoms to each lattice point gives the real crystal: crystal = lattice + basis. Si, for example, is an FCC lattice with a two-atom basis, which produces the diamond structure.

**Significance of crystal structure.**

1. **It produces the energy bands.** The periodic potential of the lattice splits the atomic levels into allowed bands and forbidden gaps (Bloch's theorem, Kronig–Penney model). The size and type (direct or indirect) of the band gap depend on the structure and the atomic spacing.
2. **Carrier mobility.** In a perfect periodic lattice electrons move without scattering; departures from periodicity (vibrations, impurities, defects, grain boundaries) cause scattering. Single crystals therefore have much higher mobility than polycrystalline or amorphous material.
3. **Anisotropy.** Properties such as surface atom density, oxidation rate, etch rate, interface trap density, piezoelectric response and mobility differ with crystal direction. Wafer orientation ((100) or (111)) is chosen accordingly.
4. **Doping and diffusion.** Dopant atoms sit on substitutional lattice sites to become active. Open structures (diamond, APF 0.34) allow interstitial diffusion.
5. **Epitaxy and heterostructures.** Layers can be grown defect-free only on substrates with matching structure and lattice constant (e.g. AlGaAs on GaAs).
6. **Mechanical behaviour.** Cleavage planes, hardness and how wafers are diced all follow from the structure and bond directions.
7. **Defects.** Departures from the ideal structure (vacancies, dislocations) create states in the gap that act as traps and recombination centres, shortening carrier lifetime.

### Q6. Define Miller indices and explain how they are used to identify crystal planes.

**Definition.** Miller indices are a set of three smallest integers (h k l), proportional to the **reciprocals of the intercepts** a plane makes on the crystal axes (measured in units of the lattice constants), that specify the orientation of that plane and all planes parallel to it.

**How they identify a plane (procedure):**

1. Choose the origin at a lattice point not on the plane. Find the intercepts on x, y, z in units of a, b, c: say p, q, r.
2. Take reciprocals 1/p, 1/q, 1/r. A plane parallel to an axis has an infinite intercept and so a zero index.
3. Multiply by the lowest common multiple of the denominators to obtain integers.
4. Reduce to the smallest integers and enclose in round brackets (h k l). Negative indices carry a bar.

**Use and notation.** (h k l) names a particular plane; {h k l} the family of symmetry-equivalent planes; [u v w] a direction and ⟨u v w⟩ a family of directions. In cubic crystals [h k l] is normal to (h k l), and the spacing between planes is d = a/√(h² + k² + l²). Miller indices are used to specify wafer orientation ((100) for MOS, (111) for bipolar), etch planes, cleavage planes and X-ray diffraction peaks.

**Example.** Intercepts a, 2b, 3c → reciprocals 1, 1/2, 1/3 → × 6 → **(6 3 2)**.

### Q7. Determine the Miller indices of a crystal plane having intercepts of 2a, 3b, and 1c.

| Step | x | y | z |
|---|---|---|---|
| Intercepts (in units of a, b, c) | 2 | 3 | 1 |
| Reciprocals | 1/2 | 1/3 | 1/1 |
| Multiply by the LCM of the denominators, 6 | 3 | 2 | 6 |

**Miller indices = (3 2 6).**

Check: the integers 3, 2, 6 have no common factor, so no further reduction is possible. If the crystal is cubic with lattice constant a, the spacing of these planes is d₃₂₆ = a/√(9 + 4 + 36) = a/√49 = **a/7**.

@fig figures/miller-326.svg | The (3 2 6) plane, cutting the axes at 2a, 3b and 1c.
