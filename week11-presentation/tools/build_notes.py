#!/usr/bin/env python3
"""Build the Word notes so that every value shows in every viewer.

Word equation objects (OMML) vanish in viewers without equation support, so:
  * inline maths becomes ordinary formatted text: italic variables, real
    subscripts/superscripts, true minus signs and Unicode symbols;
  * display equations become 300 dpi images typeset with STIX maths, in a
    centred "Equation" paragraph.

    python3 tools/build_notes.py        (writes the .docx next to notes.md)
"""
import json, os, re, subprocess, zipfile, shutil
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "Week11-Metal-Semiconductor-Interfaces-Notes.docx")
EQDIR = os.path.join(ROOT, "build", "eq")
os.makedirs(EQDIR, exist_ok=True)
plt.rcParams.update({"mathtext.fontset": "stix", "font.family": "STIXGeneral"})

# ---------------------------------------------------------------- inline TeX -> pandoc inlines
SYM = {"times": "×", "Phi": "Φ", "chi": "χ", "eta": "η", "varepsilon": "ε", "epsilon": "ε", "rho": "ρ",
       "tau": "τ", "pi": "π", "Delta": "Δ", "Omega": "Ω", "mu": "μ", "propto": "∝", "approx": "≈",
       "le": "≤", "ge": "≥", "leq": "≤", "geq": "≥", "ln": "ln", "exp": "exp", "max": "max",
       "cdot": "·", "gg": "≫", "ll": "≪", "sim": "∼", "neq": "≠", "infty": "∞", "rightarrow": "→", "pm": "±"}
UPRIGHT_GREEK = set("ΦΔΩμ")   # μ is only used as the micro prefix
SPACE = {",": " ", " ": " ", "quad": " ", "qquad": "  ", ";": " ", "!": ""}
BINOPS = {"=", "+", "−", "×", "<", ">", "≈", "∝", "≤", "≥", "±", "→"}


def tokens(tex):
    i, out = 0, []
    while i < len(tex):
        c = tex[i]
        if c == "\\":
            m = re.match(r"\\([A-Za-z]+|.)", tex[i:])
            out.append("\\" + m.group(1)); i += len(m.group(0))
        elif c.isspace():
            i += 1
        else:
            out.append(c); i += 1
    return out


def S(t):
    return {"t": "Str", "c": t}


def group(toks, i):
    """Return (tokens of one argument, next index)."""
    if toks[i] == "{":
        depth, j = 1, i + 1
        while depth:
            depth += {"{": 1, "}": -1}.get(toks[j], 0); j += 1
        return toks[i + 1:j - 1], j
    return [toks[i]], i + 1


def conv(toks, roman=False):
    """Convert a token list to a list of pandoc inlines."""
    atoms, i = [], 0
    while i < len(toks):
        t = toks[i]
        if t in ("_", "^"):
            arg, i = group(toks, i + 1)
            inner = conv(arg, roman)
            atoms.append([{"t": "Subscript" if t == "_" else "Superscript", "c": inner}])
            continue
        if t == "{":
            arg, i = group(toks, i)
            atoms.append(conv(arg, roman)); continue
        if t.startswith("\\"):
            name = t[1:]
            i += 1
            if name in ("mathrm", "text", "operatorname"):
                arg, i = group(toks, i); atoms.append(conv(arg, True)); continue
            if name == "mathcal":
                arg, i = group(toks, i); atoms.append([S("ℰ" if arg == ["E"] else "".join(arg))]); continue
            if name == "frac":
                a, i = group(toks, i); b, i = group(toks, i)
                A, B = conv(a, roman), conv(b, roman)
                wrap = lambda x, raw: ([S("(")] + x + [S(")")]) if len(raw) > 1 and any(c in raw for c in "+-") else x
                atoms.append(wrap(A, a) + [S("/")] + wrap(B, b)); continue
            if name == "sqrt":
                a, i = group(toks, i)
                inner = conv(a, roman)
                atoms.append([S("√")] + (inner if len(a) == 1 else [S("(")] + inner + [S(")")])); continue
            if name in ("left", "right", "big", "Big", "bigl", "bigr"):
                continue
            if name in SPACE:
                atoms.append([S(SPACE[name])] if SPACE[name] else []); continue
            if name in SYM:
                ch = SYM[name]
                if len(ch) == 1 and ch.isalpha() and ch not in UPRIGHT_GREEK and not roman:
                    atoms.append([{"t": "Emph", "c": [S(ch)]}])
                elif ch in BINOPS:
                    atoms.append(("op", ch))
                else:
                    atoms.append([S(ch)])
                continue
            atoms.append([S(name)]); continue
        ch = "−" if t == "-" else t
        if ch in BINOPS:
            atoms.append(("op", ch))
        elif ch.isalpha() and not roman:
            atoms.append([{"t": "Emph", "c": [S(ch)]}])
        else:
            atoms.append([S(ch)])
        i += 1
    out = []
    for k, a in enumerate(atoms):
        if isinstance(a, tuple):
            unary = k == 0 or isinstance(atoms[k - 1], tuple)
            out.append(S(a[1] if unary else " " + a[1] + " ") if a[1] in "−+" else S(" " + a[1] + " "))
        else:
            out.extend(a)
    return out


# ---------------------------------------------------------------- display TeX -> image
COUNT = [0]


def eq_image(tex):
    COUNT[0] += 1
    path = os.path.join(EQDIR, f"eq{COUNT[0]:03d}.png")
    t = re.sub(r"\\frac(?=\{)", r"\\dfrac", tex)
    fig = plt.figure(figsize=(0.01, 0.01))
    fig.text(0, 0, f"${t}$", fontsize=13, color="#14213D")
    fig.savefig(path, dpi=300, bbox_inches="tight", pad_inches=0.03, facecolor="white")
    plt.close(fig)
    from PIL import Image
    w, h = Image.open(path).size
    return path, w / 300, h / 300


def walk(x):
    if isinstance(x, list):
        out = []
        for el in x:
            r = walk(el)
            if isinstance(r, tuple) and r[0] == "splice":
                out.extend(r[1])
            else:
                out.append(r)
        return out
    if isinstance(x, dict):
        t = x.get("t")
        if t == "Para" and any(isinstance(e, dict) and e.get("t") == "Math" and e["c"][0]["t"] == "DisplayMath" for e in x["c"]):
            blocks, cur = [], []
            for e in x["c"]:
                if e.get("t") == "Math" and e["c"][0]["t"] == "DisplayMath":
                    if [c for c in cur if c.get("t") not in ("Space", "SoftBreak")]:
                        blocks.append({"t": "Para", "c": walk(cur)})
                    cur = []
                    path, w, h = eq_image(e["c"][1])
                    img = {"t": "Image", "c": [["", [], [["width", f"{w:.3f}in"], ["height", f"{h:.3f}in"]]], [], [path, ""]]}
                    blocks.append({"t": "Div", "c": [["", [], [["custom-style", "Equation"]]], [{"t": "Para", "c": [img]}]]})
                else:
                    cur.append(e)
            if [c for c in cur if c.get("t") not in ("Space", "SoftBreak")]:
                blocks.append({"t": "Para", "c": walk(cur)})
            return ("splice", blocks)
        if t == "Math":
            return ("splice", conv(tokens(x["c"][1])))
        return {k: walk(v) for k, v in x.items()}
    return x


def reference_doc():
    ref = os.path.join(ROOT, "build", "reference.docx")
    subprocess.run(["pandoc", "-o", ref, "--print-default-data-file", "reference.docx"], check=True)
    tmp = ref + ".tmp"
    style = ('<w:style w:type="paragraph" w:customStyle="1" w:styleId="Equation"><w:name w:val="Equation"/>'
             '<w:basedOn w:val="Normal"/><w:qFormat/><w:pPr><w:jc w:val="center"/>'
             '<w:spacing w:before="120" w:after="120"/></w:pPr></w:style>')
    with zipfile.ZipFile(ref) as zin, zipfile.ZipFile(tmp, "w", zipfile.ZIP_DEFLATED) as zout:
        for item in zin.infolist():
            data = zin.read(item.filename)
            if item.filename == "word/styles.xml":
                data = data.decode("utf-8").replace("</w:styles>", style + "</w:styles>").encode("utf-8")
            zout.writestr(item, data)
    shutil.move(tmp, ref)
    return ref


if __name__ == "__main__":
    ast = json.loads(subprocess.run(["pandoc", os.path.join(ROOT, "notes.md"), "-t", "json"],
                                    capture_output=True, check=True, text=True).stdout)
    ast["blocks"] = walk(ast["blocks"])
    ast["meta"] = walk(ast["meta"])
    src = os.path.join(ROOT, "build", "notes.json")
    with open(src, "w") as f:
        json.dump(ast, f)
    subprocess.run(["pandoc", src, "-f", "json", "-o", OUT, "--reference-doc", reference_doc(),
                    "--resource-path", ROOT], check=True, cwd=ROOT)
    print(OUT, COUNT[0], "display equations as images")
