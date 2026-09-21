import json, os, re, html

import sys

# build.py <course-dir> <artifact-out.html> <title> <brand-html> <eyebrow>
# Both courses share this builder, tools/render.js and tools/math.js.
SRC   = sys.argv[1] if len(sys.argv) > 1 else "/home/user/claude/electromagnetism"
OUT   = sys.argv[2] if len(sys.argv) > 2 else "/tmp/claude-0/-home-user-claude/82e48124-ad46-5f41-8d03-fa32ec4b9498/scratchpad/em-course.html"
TITLE = sys.argv[3] if len(sys.argv) > 3 else "PGDEE Electromagnetism"
BRAND = sys.argv[4] if len(sys.argv) > 4 else "Electromagnetism<br>from Scratch"
EYEBR = sys.argv[5] if len(sys.argv) > 5 else "PGDEE"

import base64, re as _re

def _expand_svg(text):
    """@fig figures/x.svg | caption  ->  a ```figure fence holding the inline SVG."""
    out = []
    for line in text.split("\n"):
        m = _re.match(r"^@fig\s+(\S+\.svg)\s*(?:\|\s*(.*))?$", line.strip())
        if not m:
            out.append(line); continue
        path = os.path.join(SRC, m.group(1))
        cap = (m.group(2) or "").strip()
        if not os.path.exists(path):
            out.append(line); continue
        with open(path, encoding="utf-8") as fh:
            art = fh.read()
        cap_html = ('<figcaption>' + cap + '</figcaption>') if cap else ''
        out.append("```figure\n<figure class=\"fig\">" + art + cap_html + "</figure>\n```")
    return "\n".join(out)


def _inline_figures(text):
    """Replace ](figures/x.png) with a data URI so the page stays self-contained."""
    def sub(m):
        path = os.path.join(SRC, m.group(1))
        if not os.path.exists(path):
            return m.group(0)
        with open(path, "rb") as fh:
            b64 = base64.b64encode(fh.read()).decode("ascii")
        return "](data:image/png;base64," + b64 + ")"
    return _re.sub(r"\]\((figures/[^)]+\.png)\)", sub, text)

files = sorted(f for f in os.listdir(SRC) if f.endswith(".md"))
mods = []
for f in files:
    text = open(os.path.join(SRC, f), encoding="utf-8").read()
    m = re.search(r"^# (.+)$", text, re.M)
    raw = m.group(1)
    num = f[:2]
    # "Module 03 — Electrostatics" -> title "Electrostatics"
    t = re.sub(r"^Module \d+ [—-] ", "", raw)
    if num == "00": t = "Start Here"
    body = _expand_svg(_inline_figures(re.sub(r"^# .+\n", "", text, count=1)))
    mods.append({"num": num, "title": t, "body": body})

DATA = json.dumps(mods, ensure_ascii=False)

page = """<title>__TITLE__</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500&family=IBM+Plex+Sans+Condensed:wght@500;600;700&family=IBM+Plex+Serif:ital,wght@0,400;0,600;1,400&display=swap">
<style>
:root{
  --bg:#F5F7F8; --surface:#FFFFFF; --sidebar:#EDF1F3;
  --ink:#17212B; --ink-soft:#5A6975; --ink-faint:#8695A1;
  --rule:#D9E1E6; --rule-soft:#E7EDF0;
  --copper:#A2542A; --copper-soft:#F3E7DE;
  --teal:#186A7B; --teal-soft:#E0EEF1;
  --shadow:0 1px 2px rgba(23,33,43,.06);
}
@media (prefers-color-scheme: dark){
  :root:not([data-theme="light"]){
    --bg:#0D1319; --surface:#131C23; --sidebar:#101820;
    --ink:#E2E9ED; --ink-soft:#93A3AE; --ink-faint:#6B7B87;
    --rule:#22303A; --rule-soft:#1A252E;
    --copper:#DC8B57; --copper-soft:#2A1D14;
    --teal:#54B4C6; --teal-soft:#122730;
    --shadow:0 1px 2px rgba(0,0,0,.4);
  }
}
:root[data-theme="dark"]{
  --bg:#0D1319; --surface:#131C23; --sidebar:#101820;
  --ink:#E2E9ED; --ink-soft:#93A3AE; --ink-faint:#6B7B87;
  --rule:#22303A; --rule-soft:#1A252E;
  --copper:#DC8B57; --copper-soft:#2A1D14;
  --teal:#54B4C6; --teal-soft:#122730;
  --shadow:0 1px 2px rgba(0,0,0,.4);
}

*{box-sizing:border-box}
body{
  background:var(--bg); color:var(--ink);
  font-family:"IBM Plex Serif",Georgia,serif;
  font-size:16px; line-height:1.65;
  display:grid; grid-template-columns:272px 1fr; min-height:100vh;
}
::selection{background:var(--copper-soft); color:var(--ink)}
a{color:var(--teal)}
:focus-visible{outline:2px solid var(--copper); outline-offset:2px; border-radius:2px}

/* ---------- sidebar ---------- */
#nav{
  background:var(--sidebar); border-right:1px solid var(--rule);
  padding:26px 0 40px; position:sticky; top:0; height:100vh; overflow-y:auto;
  font-family:"IBM Plex Sans Condensed",system-ui,sans-serif;
}
.brand{padding:0 22px 20px; border-bottom:1px solid var(--rule); margin-bottom:14px}
.brand h1{
  font-size:19px; line-height:1.2; margin:0 0 6px; font-weight:700;
  letter-spacing:-.01em; text-wrap:balance;
}
.brand p{margin:0; font-size:12px; color:var(--ink-faint); letter-spacing:.04em; text-transform:uppercase}
.seclabel{
  padding:0 22px; margin:18px 0 8px; font-size:10.5px; letter-spacing:.13em;
  text-transform:uppercase; color:var(--ink-faint); font-weight:600;
}
.modlist{list-style:none; margin:0; padding:0}
.modlist button{
  width:100%; text-align:left; background:none; border:0; cursor:pointer;
  display:grid; grid-template-columns:26px 1fr 16px; gap:9px; align-items:baseline;
  padding:7px 22px; font:inherit; font-size:14px; color:var(--ink-soft);
  border-left:2px solid transparent;
}
.modlist button:hover{background:var(--rule-soft); color:var(--ink)}
.modlist button[aria-current="true"]{
  color:var(--ink); font-weight:600; border-left-color:var(--copper); background:var(--rule-soft);
}
.modnum{
  font-family:"IBM Plex Mono",monospace; font-size:11.5px; color:var(--ink-faint);
  font-variant-numeric:tabular-nums;
}
.modlist button[aria-current="true"] .modnum{color:var(--copper)}
.tick{font-size:12px; color:var(--teal); opacity:0; transition:opacity .15s}
.done .tick{opacity:1}
.done .modnum{text-decoration:line-through}

/* ---------- reading column ---------- */
main{padding:0; min-width:0}
.sheet{
  background:var(--surface); border-left:0; min-height:100vh;
  padding:46px 56px 96px; max-width:none;
}
.wrap{max-width:74ch; margin:0 auto}
.eyebrow{
  font-family:"IBM Plex Mono",monospace; font-size:12px; letter-spacing:.12em;
  text-transform:uppercase; color:var(--copper); margin:0 0 8px;
}
h2.doctitle{
  font-family:"IBM Plex Sans Condensed",sans-serif; font-weight:700;
  font-size:38px; line-height:1.1; letter-spacing:-.02em; margin:0 0 6px; text-wrap:balance;
}
.rule{height:1px; background:var(--rule); margin:26px 0 32px}

#doc h2{
  font-family:"IBM Plex Sans Condensed",sans-serif; font-size:23px; font-weight:600;
  letter-spacing:-.01em; margin:44px 0 12px; padding-top:14px;
  border-top:1px solid var(--rule-soft); text-wrap:balance;
}
#doc h3{
  font-family:"IBM Plex Sans Condensed",sans-serif; font-size:17px; font-weight:600;
  margin:28px 0 8px; color:var(--ink);
}
#doc p{margin:0 0 14px}
#doc strong{font-weight:600}
#doc ul,#doc ol{margin:0 0 16px; padding-left:22px}
#doc li{margin:0 0 6px}
#doc hr{border:0; border-top:1px solid var(--rule); margin:34px 0}

/* formulas + code */
#doc code{
  font-family:"IBM Plex Mono",monospace; font-size:.87em;
  background:var(--rule-soft); padding:1px 5px; border-radius:3px;
}
#doc pre{
  font-family:"IBM Plex Mono",monospace; font-size:13.5px; line-height:1.6;
  background:var(--surface); border:1px solid var(--rule);
  border-left:3px solid var(--copper);
  padding:14px 18px; overflow-x:auto; margin:0 0 18px; border-radius:0 3px 3px 0;
}
#doc pre code{background:none; padding:0; font-size:inherit}

/* blockquote = the "warning / think about this" voice */
#doc blockquote{
  margin:0 0 20px; padding:14px 18px; background:var(--teal-soft);
  border-left:3px solid var(--teal); font-style:normal;
}
#doc blockquote p:last-child{margin:0}

/* tables */
.tablewrap{overflow-x:auto; margin:0 0 20px}
#doc table{border-collapse:collapse; width:100%; font-size:14.5px}
#doc th{
  /* deliberately NOT uppercased: in this course a header may be a variable,
     and n, N, v, V, s, S are different quantities */
  font-family:"IBM Plex Sans Condensed",sans-serif; font-weight:600; text-align:left;
  font-size:12.5px; letter-spacing:.03em; color:var(--ink-soft);
  border-bottom:1px solid var(--rule); padding:8px 12px 6px;
}
#doc td{
  padding:8px 12px; border-bottom:1px solid var(--rule-soft); vertical-align:top;
  font-variant-numeric:tabular-nums;
}
#doc tbody tr:last-child td{border-bottom:1px solid var(--rule)}


/* ---------- mathematical typesetting ---------- */
#doc sub, #doc sup{
  font-size:.68em; line-height:0; position:relative; font-feature-settings:"tnum";
  padding-left:.04em;
}
#doc sub{ bottom:-.22em }
#doc sup{ top:-.42em }

/* display equations */
#doc .eq{
  font-family:"IBM Plex Serif",Georgia,serif;
  font-size:16.5px; line-height:2.15; white-space:pre-wrap;
  margin:22px auto; padding:2px 0; max-width:100%;
  width:max-content; text-align:left; overflow-x:auto;
  color:var(--ink);
}
#doc .eq sub{ bottom:-.2em }

/* matrices and determinants */
#doc .eqrow{
  display:flex; align-items:center; justify-content:center; gap:10px;
  margin:26px auto; overflow-x:auto; font-family:"IBM Plex Serif",Georgia,serif;
  font-size:16.5px;
}
#doc .eqlhs{ white-space:nowrap }
#doc .mat{ display:inline-block; position:relative; padding:2px 12px }
#doc .mat table{ border-collapse:collapse; width:auto; margin:0 }
#doc .mat table td,
#doc .mat tbody tr td,
#doc .mat tbody tr:last-child td{
  padding:5px 14px; text-align:center; border:0; white-space:nowrap;
  font-variant-numeric:normal; background:none;
}
#doc .mat::before, #doc .mat::after{
  content:""; position:absolute; top:0; bottom:0; width:1px; background:var(--ink);
}
#doc .mat::before{ left:0 } #doc .mat::after{ right:0 }
#doc .mat-bracket::before, #doc .mat-bracket::after{
  width:7px; background:none; border-top:1px solid var(--ink);
  border-bottom:1px solid var(--ink);
}
#doc .mat-bracket::before{ border-left:1px solid var(--ink) }
#doc .mat-bracket::after{ border-right:1px solid var(--ink) }

@media (max-width:860px){
  #doc .eq, #doc .eqrow{ font-size:15px }
  #doc .mat td{ padding:4px 9px }
}

/* ---------- piecewise definitions ---------- */
#doc .cases{ display:inline-flex; align-items:stretch; gap:8px }
#doc .cases .brace{ flex:0 0 auto; align-self:center; overflow:visible }
#doc .cases table{ border-collapse:collapse; width:auto; margin:0 }
#doc .cases table td,
#doc .cases tbody tr td,
#doc .cases tbody tr:last-child td{
  height:30px; padding:0 0 0 2px; border:0; background:none;
  vertical-align:middle; white-space:nowrap; text-align:left;
  font-variant-numeric:normal;
}
#doc .cases td.cval{ padding-right:22px }
#doc .cases td.ccond{ color:var(--ink-soft) }

/* ---------- figures ---------- */
#doc figure.fig{
  margin:26px 0; padding:0; text-align:center;
  color:var(--ink);
}
#doc figure.fig svg{ margin:0 auto 6px }
#doc figure.fig figcaption{
  font-family:"IBM Plex Sans Condensed",system-ui,sans-serif;
  font-size:12px; line-height:1.45; color:var(--ink-soft);
  max-width:60ch; margin:4px auto 0; text-wrap:balance;
}
#doc img{
  display:block; margin:20px auto; max-width:100%; height:auto;
  background:#fff; padding:10px; border:1px solid var(--rule); border-radius:2px;
}

/* ---------- footer nav ---------- */
.pager{
  display:flex; gap:12px; justify-content:space-between; align-items:stretch;
  margin-top:52px; padding-top:22px; border-top:1px solid var(--rule);
}
.pager button{
  flex:1; text-align:left; background:var(--surface); border:1px solid var(--rule);
  padding:12px 16px; cursor:pointer; font-family:"IBM Plex Sans Condensed",sans-serif;
  color:var(--ink); font-size:15px; line-height:1.3;
}
.pager button:hover{border-color:var(--copper)}
.pager button:disabled{opacity:.35; cursor:default}
.pager button.next{text-align:right}
.pager span{display:block; font-size:11px; letter-spacing:.1em; text-transform:uppercase; color:var(--ink-faint); margin-bottom:3px}

.readbtn{
  display:inline-flex; align-items:center; gap:8px; margin-top:26px;
  background:none; border:1px solid var(--rule); color:var(--ink-soft);
  font-family:"IBM Plex Sans Condensed",sans-serif; font-size:13.5px;
  padding:8px 14px; cursor:pointer;
}
.readbtn:hover{border-color:var(--teal); color:var(--ink)}
.readbtn[aria-pressed="true"]{border-color:var(--teal); color:var(--teal); background:var(--teal-soft)}

/* ---------- mobile ---------- */
#mobsel{display:none}
@media (max-width:860px){
  body{grid-template-columns:1fr}
  #nav{display:none}
  #mobsel{
    display:block; position:sticky; top:0; z-index:5; background:var(--sidebar);
    border-bottom:1px solid var(--rule); padding:12px 18px;
  }
  #mobsel select{
    width:100%; font-family:"IBM Plex Sans Condensed",sans-serif; font-size:15px;
    padding:9px 10px; background:var(--surface); color:var(--ink);
    border:1px solid var(--rule); border-radius:2px;
  }
  .sheet{padding:28px 20px 72px}
  h2.doctitle{font-size:28px}
}
@media (prefers-reduced-motion:reduce){*{transition:none!important}}
</style>

<nav id="nav">
  <div class="brand">
    <h1>__BRAND__</h1>
    <p>__EYEBROW__ &middot; __NMOD__ modules</p>
  </div>
  <div class="seclabel">Course</div>
  <ul class="modlist" id="modlist"></ul>
</nav>

<main>
  <div id="mobsel"><select id="sel" aria-label="Choose module"></select></div>
  <div class="sheet">
    <div class="wrap">
      <p class="eyebrow" id="eyebrow"></p>
      <h2 class="doctitle" id="doctitle"></h2>
      <div class="rule"></div>
      <article id="doc"></article>
      <button class="readbtn" id="readbtn" aria-pressed="false"></button>
      <div class="pager">
        <button id="prev"><span>Previous</span><b id="prevt"></b></button>
        <button id="next" class="next"><span>Next</span><b id="nextt"></b></button>
      </div>
    </div>
  </div>
</main>

<script>
__RENDERER__
const MODS = __DATA__;
const KEY = "pgdee-em-read";
let read = new Set();
try { read = new Set(JSON.parse(localStorage.getItem(KEY) || "[]")); } catch(e) {}
function save(){ try { localStorage.setItem(KEY, JSON.stringify([...read])); } catch(e) {} }

const list = document.getElementById("modlist");
const sel  = document.getElementById("sel");
let cur = 0;

MODS.forEach((m,i)=>{
  const li = document.createElement("li");
  const b  = document.createElement("button");
  b.innerHTML = '<span class="modnum">'+m.num+'</span><span>'+m.title+'</span><span class="tick">&#10003;</span>';
  b.onclick = ()=>show(i);
  li.appendChild(b); list.appendChild(li);
  const o = document.createElement("option");
  o.value = i; o.textContent = m.num + " · " + m.title;
  sel.appendChild(o);
});
sel.onchange = e => show(+e.target.value);

function show(i){
  cur = i;
  const m = MODS[i];
  document.getElementById("eyebrow").textContent =
    m.num === "00" ? "Orientation" : "Module " + m.num;
  document.getElementById("doctitle").textContent = m.title;
  const doc = document.getElementById("doc");
  doc.innerHTML = mdToHtml(m.body);
  doc.querySelectorAll("table").forEach(t=>{
    const w = document.createElement("div");
    w.className = "tablewrap";
    t.parentNode.insertBefore(w,t); w.appendChild(t);
  });

  [...list.querySelectorAll("button")].forEach((b,j)=>{
    b.setAttribute("aria-current", j===i ? "true" : "false");
    b.parentNode.classList.toggle("done", read.has(MODS[j].num));
  });
  sel.value = i;

  const rb = document.getElementById("readbtn");
  const isRead = read.has(m.num);
  rb.setAttribute("aria-pressed", isRead ? "true" : "false");
  rb.textContent = isRead ? "✓  Marked as read" : "Mark this module read";
  rb.onclick = ()=>{ read.has(m.num) ? read.delete(m.num) : read.add(m.num); save(); show(i); };

  const p = document.getElementById("prev"), n = document.getElementById("next");
  p.disabled = i===0; n.disabled = i===MODS.length-1;
  document.getElementById("prevt").textContent = i>0 ? MODS[i-1].title : "—";
  document.getElementById("nextt").textContent = i<MODS.length-1 ? MODS[i+1].title : "—";
  p.onclick = ()=>show(i-1); n.onclick = ()=>show(i+1);

  window.scrollTo(0,0);
}

document.addEventListener("keydown", e=>{
  if(e.target.tagName === "SELECT") return;
  if(e.key === "ArrowRight" && cur < MODS.length-1) show(cur+1);
  if(e.key === "ArrowLeft"  && cur > 0) show(cur-1);
});

show(0);
</script>
"""

RENDERER = (open(os.path.join(os.path.dirname(OUT), "math.js"), encoding="utf-8").read()
            + "\n" + open(os.path.join(os.path.dirname(OUT), "render.js"), encoding="utf-8").read())
page = (page.replace("__RENDERER__", RENDERER).replace("__DATA__", DATA)
            .replace("__TITLE__", TITLE).replace("__BRAND__", BRAND)
            .replace("__EYEBROW__", EYEBR).replace("__NMOD__", str(len(mods))))
open(OUT, "w", encoding="utf-8").write(page)

# standalone: same body, wrapped in a real document so it opens from the filesystem
head, rest = page.split("</style>", 1)
STANDALONE = (
  '<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
  '<meta name="viewport" content="width=device-width, initial-scale=1">\n'
  + head + "</style>\n"
  + "<style>html{color-scheme:light dark}body{margin:0}img{max-width:100%}[hidden]{display:none!important}</style>\n"
  + "</head>\n<body>" + rest + "</body>\n</html>\n"
)
SOUT = os.path.join(SRC, "course.html")
open(SOUT, "w", encoding="utf-8").write(STANDALONE)
print("artifact  :", OUT, os.path.getsize(OUT), "bytes")
print("standalone:", SOUT, os.path.getsize(SOUT), "bytes,", len(mods), "modules")
