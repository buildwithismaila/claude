# Module 03 — Bonding and Crystal Defects

Lecture note §18–§20 and §27. The type of bond holding the atoms together decides how electrons behave in the solid. Defects decide how far real crystals fall short of the ideal.

## 3.1 The bonding mechanisms

**Ionic bonding.** One atom transfers electrons to another, producing positive and negative ions held together by electrostatic (Coulomb) attraction. Occurs between elements of very different electronegativity, e.g. Na⁺Cl⁻. The bond is strong but **non-directional**. Electrons are tightly bound to the ions, so ionic solids are insulators with large gaps; they are hard, brittle and have high melting points.

**Covalent bonding.** Neighbouring atoms **share** pairs of valence electrons, one electron from each, so each atom completes its outer shell (8 electrons). The bond is strong and **directional**, which fixes the crystal geometry (tetrahedral, 109.5°). Electrons are localised in bonds at low temperature but can be freed by modest energy, which gives semiconducting behaviour. Examples: Si, Ge, diamond.

**Metallic bonding.** Valence electrons leave their atoms and form a delocalised "sea" or gas of electrons shared by the whole crystal, holding a lattice of positive ion cores together. Non-directional. The free electron sea explains the high electrical and thermal conductivity, lustre and ductility of metals. Examples: Cu, Al, Na.

**Van der Waals bonding.** Weak attraction between fluctuating dipoles in neutral atoms or molecules. Important in layered materials (graphite, MoS₂) and noble-gas solids, not in Si or GaAs.

**Mixed ionic–covalent.** Real compound semiconductors lie between the ideal limits.

| | Ionic | Covalent | Metallic |
|---|---|---|---|
| Mechanism | Electron transfer, ion attraction | Electron-pair sharing | Shared electron sea |
| Directional? | No | Yes | No |
| Free electrons | None | Few (created thermally) | Very many |
| Electrical behaviour | Insulator | Semiconductor (or insulator) | Conductor |
| Example | NaCl | Si, Ge, C | Cu, Al |

## 3.2 Covalent bonding in Si and Ge

Each Si atom has 4 valence electrons (3s²3p²). They hybridise into four **sp³** orbitals pointing to the corners of a tetrahedron, and each overlaps with one from a neighbour to form a two-electron bond. Every atom ends up sharing 8 electrons.

At 0 K all electrons sit in bonds: none is free and the crystal is an insulator. At room temperature thermal energy breaks a small number of bonds. Each broken bond releases a **free electron** and leaves behind a **hole** (a missing bond electron), which neighbouring bond electrons can hop into, so the hole also moves. This is the bond picture of electron–hole pair generation; in band language, the bond energy needed is the band gap E_g.

## 3.3 Ionic character in GaAs

Ga contributes 3 electrons and As 5, so the bonds are still mainly covalent sp³. But **As is more electronegative** than Ga, so the shared electrons spend more time near As. Each bond is partly polar (As slightly negative, Ga slightly positive), giving about 30 % ionic character. Consequences: polar optical-phonon scattering, piezoelectricity, larger band gap than a purely covalent equivalent, and the Ga/As face polarity of (111) surfaces.

## 3.4 Defects in real crystals

| Type | Dimension | Examples | Effect |
|---|---|---|---|
| Point | 0-D | Vacancy, self-interstitial, substitutional or interstitial impurity, Frenkel pair (vacancy + interstitial) | Traps, recombination centres; vacancies assist diffusion |
| Line | 1-D | Edge and screw dislocations | Leakage paths, recombination along the line, enhanced diffusion |
| Planar | 2-D | Grain boundaries, stacking faults, twin boundaries, surfaces and interfaces | Scattering, interface traps, junction leakage |
| Volume | 3-D | Voids, precipitates (e.g. SiO₂ clusters), inclusions | Gettering sites if controlled, device failure if not |

Defects act as **scattering centres** (lower mobility), **recombination–generation centres** (shorter lifetime, more leakage), **traps** (charge storage and noise) and **diffusion paths**. Not all impurities are unwanted: deliberate dopants are substitutional point defects.

---

## Exam questions solved

### Q8. Explain the difference between covalent, ionic, and metallic bonding and identify the dominant bonding mechanism in silicon.

**Covalent bonding.** Adjacent atoms share pairs of valence electrons so that each completes a stable outer shell. The shared electrons are localised between the two atoms, making the bond strong and directional. Covalent solids are hard, have high melting points, and are semiconductors or insulators depending on how tightly the bonds hold their electrons.

**Ionic bonding.** An electropositive atom gives up valence electrons to an electronegative atom; the resulting positive and negative ions attract electrostatically. The bond is strong but non-directional, there are no free electrons, and ionic solids (NaCl, MgO) are brittle insulators that conduct only when molten or dissolved.

**Metallic bonding.** Each atom releases its valence electrons into a common delocalised electron gas that binds the positive ion cores. The bond is non-directional, and the mobile electron gas gives high electrical and thermal conductivity, ductility and metallic lustre.

**Key differences:** how the electrons are held (shared between pairs / transferred to ions / shared by all atoms), directionality (yes / no / no), and the resulting electrical behaviour (semiconductor or insulator / insulator / conductor).

**Bonding in silicon: covalent.** Si has four valence electrons. In the diamond-cubic lattice each Si atom forms four sp³ covalent bonds with four nearest neighbours at 109.5°, sharing one electron pair with each so that every atom has a full octet. Because Si–Si bonds are between identical atoms there is no ionic character. The modest bond strength (equivalent to E_g = 1.12 eV) is what lets thermal energy break a few bonds at room temperature, creating electron–hole pairs and giving silicon its semiconducting behaviour.
