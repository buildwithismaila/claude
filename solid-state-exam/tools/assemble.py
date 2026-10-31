"""Assemble the five question pages from parts/qNN-MM.md.

    python3 tools/assemble.py
"""
import os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GROUP = "The 50 questions, answered"
PAGES = [
    ("01-questions-01-13-material-physics-and-growth.md", "Questions 1–13 — Material Physics and Semiconductor Growth",
     ["q01-07.md", "q08-13.md"],
     "Module 1, part 1: what a semiconductor is, the main materials, crystal structure and Miller indices, bonding, "
     "and how silicon is purified and grown into crystals and epitaxial layers."),
    ("02-questions-14-21-impurity-control-and-doping.md", "Questions 14–21 — Impurity Control and Doping",
     ["q14-21.md"],
     "Module 1, part 2: why and how semiconductors are doped: donors and acceptors, diffusion and Fick's laws, "
     "the diffusion profile, and ion implantation."),
    ("03-questions-22-34-energy-bands-and-carrier-statistics.md", "Questions 22–34 — Energy Bands and Carrier Statistics",
     ["q22-28.md", "q29-34.md"],
     "Module 2: the quantum model of electrons in a crystal, how energy bands form, direct and indirect gaps, "
     "intrinsic and extrinsic carriers, Fermi–Dirac statistics, the density of states and the Fermi level."),
    ("04-questions-35-46-carrier-transport-and-injection.md", "Questions 35–46 — Carrier Transport and Injection",
     ["q35-41.md", "q42-46.md"],
     "Module 3: how carriers move (drift, mobility, scattering, diffusion, the Einstein relation, high fields) "
     "and how excess carriers are generated, recombine and flow (SRH, lifetime, continuity, surfaces)."),
    ("05-questions-47-50-junctions-and-characterisation.md", "Questions 47–50 — Junctions, Interfaces and Characterisation",
     ["q47-50.md"],
     "Module 4: the p-n junction and its diode equation, metal–semiconductor contacts, and how devices are "
     "measured with I-V and C-V characterisation. These are long questions: practise writing them in full."),
]

for fname, title, parts, intro in PAGES:
    body = "\n".join(open(os.path.join(ROOT, "parts", p), encoding="utf-8").read().strip() + "\n" for p in parts)
    qs = re.findall(r"^### Q(\d+)\. (.+)$", body, flags=re.M)
    index = ["| Q | Question |", "|---|---|"] + [f"| {n} | {t} |" for n, t in qs]
    old = os.path.join(ROOT, fname)
    keep = ""
    if os.path.exists(old):        # keep the generated symbols table, if any
        m = re.search(r"^## Symbols and abbreviations used.*?(?=^## (?!Symbols and))", open(old, encoding="utf-8").read(), flags=re.S | re.M)
        keep = m.group(0) if m else ""
    text = (f"# {title}\n<!-- group: {GROUP} -->\n\n{intro} Each question stands on its own: its key terms are defined "
            f"with it, so you can start anywhere.\n\n{keep}## Questions on this page\n\n" + "\n".join(index) +
            "\n\n## Model answers\n\n" + body.rstrip().rstrip("-").rstrip() + "\n")
    open(old, "w", encoding="utf-8").write(text)
    print(fname, len(qs), "questions")
