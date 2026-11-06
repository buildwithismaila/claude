#!/usr/bin/env python3
"""Build a PowerPoint version of the deck with the animations embedded as video.

Each slide of slides-source/project is rendered in Chromium at 1920×1080 and placed
as a full-slide picture; slides with a video get the MP4 embedded on top of the
still (click to play in PowerPoint). Slides with step-by-step builds become one
slide per step. Speaker notes are copied across.

    python3 tools/build_pptx.py
"""
import json, os, re, subprocess, tempfile
from pptx import Presentation
from pptx.util import Emu

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DECK = os.path.join(ROOT, "slides-source", "project")
OUT = os.path.join(ROOT, "Week11-Metal-Semiconductor-Interfaces-Slides.pptx")
F, E, A = (os.path.join(ROOT, d) for d in ("figures", "equations", "animation"))

BLOBS = {  # uploaded asset id -> local file
    "1691dbeda7b9a6ff164fa8e84e24d4e0": f"{F}/before-contact.svg", "228d2904792a932c99dec5bd62e549c5": f"{F}/bias.svg",
    "41a6d0bd74a14395243e7e523ce20aea": f"{F}/depletion.svg", "0dd7d8564ed58f1ed2188f39288d119c": f"{F}/device.svg",
    "89f605da57ce498b1c46739d5ed744e3": f"{F}/equilibrium.svg", "e8cdbd7df01b28f1539ff5d68870fd89": f"{F}/iv.svg",
    "1f5dfb48a3c7504458435b4fd1125921": f"{F}/levels.svg", "8bf593ae0cc9646faaa30ddc1ad8cfa0": f"{F}/ohmic.svg",
    "7ee95220fac4c4230519e1465507429c": f"{F}/pinning.svg", "708253aa44822d140449a212d6fc2fe4": f"{F}/bias-eq.svg",
    "0be12a00203627ba0ef5a0383becd285": f"{F}/bias-fwd.svg", "ce5ac66d9c572b02f5f1feab243791dd": f"{F}/bias-rev.svg",
    "d01f529724f632ac9f8e4410377bc630": f"{A}/schottky-formation.mp4", "6813e70156cc0582e0209e34e8dcec1e": f"{A}/schottky-formation-still.png",
    "6a530a782d8f2442c035f9bc41d0215a": f"{A}/ohmic-formation.mp4", "3281a3cb96aa70c6a342e860a27d788c": f"{A}/ohmic-formation-still.png",
    "cf1f181419d29130a44e3d49c06709e1": f"{E}/C.svg", "1abb47116d60e97c183a1dc4599382cc": f"{E}/Emax.svg",
    "eb4938f8b732752b61bd3a30d18b8645": f"{E}/I.svg", "d99d3d60bfafec027e90de8414ee3db0": f"{E}/J.svg",
    "c0e474187e651574d7c2626d4445d739": f"{E}/Js.svg", "4689b7c4369af814e96b5e43495901b2": f"{E}/W-prop.svg",
    "9aa61c4d67745feb8ebe4a86fc5261d5": f"{E}/W-sum.svg", "882fb1e0e232e43ee2149009ec78a89f": f"{E}/W.svg",
    "a62d058e0f469f3645114f1059012626": f"{E}/affinity.svg", "b0a0cd589292512d459850fec73e9b0b": f"{E}/barrier-n.svg",
    "ea9665ca2ae28b3b70207d7e5b476f79": f"{E}/barrier-p.svg", "45a3a0095d128e72d1555ed86bb9bfbc": f"{E}/bias-fwd.svg",
    "92e0da38de2dbf3d0691a2db42992edd": f"{E}/bias-rev.svg", "fb57fd4a9356043dd99b262f184142bd": f"{E}/cond-ohmic.svg",
    "8500565e3da0c0fd6bfa73fe8380169f": f"{E}/cond-schottky.svg", "d58f8433f1f1142b18a22bcd9d6e7b18": f"{E}/ec-ef.svg",
    "57ca8dbbbfaad087a0d09ef11b8cc130": f"{E}/ef-align.svg", "bf2a90ecaed1d45d91e3823f3c4d358b": f"{E}/ex-Emax.svg",
    "3827b078aaedeb1edb617207233ab020": f"{E}/ex-I.svg", "1cb7b1ad03a15cdc69150f697d83a93d": f"{E}/ex-W.svg",
    "ef39ccf89881f72665347f86675ab9f3": f"{E}/ex-W1.svg", "29911f7df9c794af9591bcc51432a7a8": f"{E}/ex-W2.svg",
    "54ab9c50e413fdf001a929054fd99116": f"{E}/ex-au.svg", "af8c9cf6cae2ecbe2dfb044b40ac24c2": f"{E}/ex-au2.svg",
    "35dc76d94d6c04aac38745cd5efb6e19": f"{E}/ex-p.svg", "5c3db95485b18d0aa100d01e9995c9e0": f"{E}/ex-phis.svg",
    "6929556a222fc2d0030d50aef4bf2b2c": f"{E}/ex-phis2.svg", "3dc7bde3b783997a02e48ce4b434a361": f"{E}/ex-pinned.svg",
    "8bad4941d1e5894ff285ae964d8b7c43": f"{E}/flat.svg", "61b05e8b8729b884f09df1131bf68c4b": f"{E}/gap.svg",
    "0891bdfdb3d64352dfbe80e0a6baa782": f"{E}/image.svg", "df6d6782c857ce31ac30b80a1b4c3a52": f"{E}/ohm.svg",
    "02730bd2065d78191c51a5ac5e13f328": f"{E}/vbi.svg", "411ca88984680d63a08028280250c3bf": f"{E}/workfn-m.svg",
    "e2759b073827f8b5ac9416f07c3eca53": f"{E}/workfn-s.svg", "38d94d64a209c035a0ad4351d6825266": f"{E}/Astar.svg",
    "67fa2b9f87ea69ac29bfdde8e9e5809c": f"{E}/ex-Wf.svg", "5435acf405eb2983c8b92e942ca5f7c0": f"{E}/ex-Wr.svg",
    "4bb2fe0c729f77625804e0c379606663": f"{E}/ex-Js.svg", "5e14021987ce518fcb0c9f903f7b9d43": f"{E}/ex-V.svg",
    "00b3acc1b2f68418f14fa05779bc595e": f"{E}/V-Js.svg",
}

CSS = """
html,body{margin:0;padding:0;background:#fff}
section{position:relative;width:1920px;height:1080px;box-sizing:border-box;overflow:hidden}
h1,h2,h3,p,ul,ol,table{margin:0}
h1{font-size:96px;font-weight:600;line-height:1.1} h2{font-size:64px;font-weight:600;line-height:1.15}
h3{font-size:44px;font-weight:600;line-height:1.2} p{font-size:32px;line-height:1.4}
div{box-sizing:border-box} div:not([style*="display"]){display:flex;flex-direction:column} p,h1,h2,h3{box-sizing:border-box}
ul,ol{padding-left:1.25em} li{margin-bottom:0.25em}
img{display:block}
table{border-collapse:collapse} th,td{padding:0.35em 0.6em;text-align:left;vertical-align:top;border-bottom:1px solid #C9D3DA}
th{font-weight:600;border-bottom:2px solid #14213D}
aside{display:none}
"""


def page(section, fonts):
    links = "".join(f'<link rel="stylesheet" href="{f["href"]}">' for f in fonts if "href" in f)
    return f'<!doctype html><html><head><meta charset="utf-8">{links}<style>{CSS}</style></head><body>{section}</body></html>'


def main():
    deck = json.load(open(os.path.join(DECK, "deck.json")))
    fonts = list(deck["faces"].values())
    jobs = []
    for sid in deck["order"]:
        html = open(os.path.join(DECK, "slides", sid + ".html"), encoding="utf-8").read()
        notes = re.search(r"<aside>(.*?)</aside>", html, re.S)
        missing = [b for b in re.findall(r"/_blob/([0-9a-f]{32})", html) if b not in BLOBS]
        if missing:
            raise SystemExit(f"{sid}: no local file for {missing}")
        html = re.sub(r'src="/_blob/([0-9a-f]{32})"', lambda m: f'src="file://{BLOBS[m.group(1)]}"', html)
        orders = sorted({int(n) for n in re.findall(r'data-build-in="\w+ (\d+)', html)})
        steps = orders or [None]
        for k in steps:
            jobs.append({"id": sid, "step": k, "html": page(html, fonts),
                         "notes": notes.group(1).strip() if notes else ""})
    tmp = tempfile.mkdtemp()
    spec = os.path.join(tmp, "jobs.json")
    json.dump([{"id": j["id"], "step": j["step"], "html": j["html"]} for j in jobs], open(spec, "w"))
    subprocess.run(["node", os.path.join(ROOT, "tools", "render_slides.js"), spec, tmp], check=True)
    boxes = json.load(open(os.path.join(tmp, "boxes.json")))

    prs = Presentation()
    prs.slide_width, prs.slide_height = Emu(12192000), Emu(6858000)
    px = 12192000 / 1920
    blank = prs.slide_layouts[6]
    for i, j in enumerate(jobs):
        s = prs.slides.add_slide(blank)
        s.shapes.add_picture(os.path.join(tmp, f"s{i:03d}.png"), 0, 0, prs.slide_width, prs.slide_height)
        for v in boxes[i]:
            mp4 = BLOBS[v["video"]]
            poster = v["still"]
            s.shapes.add_movie(mp4, Emu(int(v["x"] * px)), Emu(int(v["y"] * px)), Emu(int(v["w"] * px)),
                               Emu(int(v["h"] * px)), poster_frame_image=poster, mime_type="video/mp4")
        if j["notes"]:
            s.notes_slide.notes_text_frame.text = j["notes"]
    prs.save(OUT)
    print(OUT, len(jobs), "slides")


if __name__ == "__main__":
    main()
