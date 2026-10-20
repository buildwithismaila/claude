// export.js <course.html> <out-dir>
// Renders every module of the built course into one print document, then writes
//   ELE717-Solid-State-Electronics.pdf   (Chromium print, vector figures)
//   ELE717-Solid-State-Electronics.docx  (pandoc from the same HTML, figures as PNG)
const path = require("path");
const fs = require("fs");
const { execFileSync, execSync } = require("child_process");
const { chromium } = require(execSync("npm root -g").toString().trim() + "/playwright");

const [src, outDir] = process.argv.slice(2);
const BASE = "ELE717-Solid-State-Electronics";
fs.mkdirSync(outDir, { recursive: true });

const PRINT_CSS = `
  @page { size: A4; margin: 18mm 16mm 18mm 16mm; }
  * { box-sizing: border-box; }
  body { font-family: "IBM Plex Serif", Georgia, "Times New Roman", serif; font-size: 10.5pt;
         line-height: 1.5; color: #17212B; background: #fff; margin: 0; }
  h1, h2, h3, h4 { font-family: "IBM Plex Sans Condensed", "Arial Narrow", Arial, sans-serif;
         color: #17212B; break-after: avoid; }
  .cover { height: 250mm; display: flex; flex-direction: column; justify-content: center; }
  .cover h1 { font-size: 30pt; margin: 0 0 8pt; }
  .cover p { font-size: 12pt; color: #5A6975; margin: 4pt 0; }
  .toc h2 { font-size: 16pt; }
  .toc ol { padding-left: 18pt; } .toc li { margin: 3pt 0; }
  .module { break-before: page; }
  .eyebrow { font-family: "IBM Plex Mono", monospace; font-size: 8.5pt; letter-spacing: .1em;
         text-transform: uppercase; color: #A2542A; margin: 0 0 4pt; }
  .module > h1 { font-size: 22pt; margin: 0 0 14pt; padding-bottom: 6pt; border-bottom: 1px solid #D9E1E6; }
  h2 { font-size: 14.5pt; margin: 18pt 0 6pt; }
  h3 { font-size: 12pt; margin: 14pt 0 5pt; }
  h4 { font-size: 11pt; margin: 12pt 0 4pt; color: #A2542A; }
  p { margin: 0 0 7pt; }
  ul, ol { margin: 0 0 8pt; padding-left: 18pt; } li { margin: 0 0 3pt; }
  table { border-collapse: collapse; width: 100%; margin: 4pt 0 10pt; font-size: 9.5pt; break-inside: avoid; }
  th, td { border: 1px solid #C9D3DA; padding: 3pt 5pt; text-align: left; vertical-align: top; }
  th { background: #EDF1F3; }
  .eq { font-family: "IBM Plex Serif", Georgia, serif; white-space: pre-wrap; margin: 6pt 0 8pt 18pt;
        line-height: 1.8; break-inside: avoid; }
  pre { font-family: "IBM Plex Mono", Consolas, monospace; font-size: 8.5pt; background: #F5F7F8;
        border: 1px solid #D9E1E6; padding: 6pt; white-space: pre-wrap; }
  blockquote { margin: 6pt 0 10pt; padding: 6pt 10pt; background: #E0EEF1; border-left: 3px solid #186A7B; }
  figure { margin: 8pt 0 12pt; text-align: center; break-inside: avoid; }
  figure svg, figure img { max-width: 100%; height: auto; }
  figcaption { font-family: Arial, sans-serif; font-size: 8.5pt; color: #5A6975; }
  sub, sup { font-size: 70%; line-height: 0; }
  hr { border: 0; border-top: 1px solid #D9E1E6; margin: 14pt 0; }
`;

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1000, height: 1200 } });
  await page.goto("file://" + path.resolve(src));
  await page.evaluate(() => document.documentElement.setAttribute("data-theme", "light"));

  // Collect each module's rendered HTML, using the course's own renderer.
  const mods = await page.evaluate(() => MODS.map((m, i) => {
    show(i);
    return {
      eyebrow: document.getElementById("eyebrow").textContent,
      title: document.getElementById("doctitle").textContent,
      html: document.getElementById("doc").innerHTML,
    };
  }));

  const cover = `<section class="cover"><p class="eyebrow">ELE 717 · Postgraduate Diploma · Nigerian Defence Academy</p>
    <h1>Solid State Electronics</h1><p>A week-by-week course following the 15-week Lecture 2 plan</p>
    <p>With learning objectives, worked examples, practice questions, the 50 PGD examination questions
    solved, CAT practice tests and laboratory practicals.</p></section>`;
  const toc = `<section class="toc"><h2>Contents</h2><ol>${mods.map(m =>
    `<li>${m.eyebrow ? m.eyebrow + " — " : ""}${m.title}</li>`).join("")}</ol></section>`;
  const body = mods.map(m => `<section class="module"><p class="eyebrow">${m.eyebrow}</p>
    <h1>${m.title}</h1>${m.html}</section>`).join("\n");
  const doc = `<!doctype html><html lang="en"><head><meta charset="utf-8">
    <title>ELE 717 Solid State Electronics</title><style>${PRINT_CSS}</style></head>
    <body>${cover}${toc}${body}</body></html>`;

  // ---- PDF -------------------------------------------------------------
  const pp = await browser.newPage();
  await pp.setContent(doc, { waitUntil: "load" });
  await pp.pdf({
    path: path.join(outDir, BASE + ".pdf"), format: "A4", printBackground: true,
    displayHeaderFooter: true,
    headerTemplate: "<span></span>",
    footerTemplate: `<div style="font-size:8px;width:100%;text-align:center;color:#8695A1;font-family:Arial">
      ELE 717 Solid State Electronics · page <span class="pageNumber"></span> of <span class="totalPages"></span></div>`,
    margin: { top: "16mm", bottom: "18mm", left: "16mm", right: "16mm" },
  });

  // ---- DOCX ------------------------------------------------------------
  // Word cannot show inline SVG: replace each figure with a PNG of itself,
  // and keep the line breaks of multi-line equations.
  const tmp = fs.mkdtempSync(path.join(outDir, ".docx-"));
  const svgs = await pp.$$("figure svg");
  for (let i = 0; i < svgs.length; i++) {
    const file = path.join(tmp, `fig${i}.png`);
    await svgs[i].screenshot({ path: file, omitBackground: false });
    await svgs[i].evaluate((el, f) => {
      const img = document.createElement("img");
      img.setAttribute("src", f);
      img.setAttribute("style", "width:15cm");
      el.replaceWith(img);
    }, path.basename(file));
  }
  await pp.evaluate(() => {
    document.querySelectorAll(".eq").forEach(e => { e.innerHTML = e.innerHTML.replace(/\n/g, "<br>"); });
    document.querySelectorAll(".cover, .toc").forEach(e => e.remove());
    // pandoc maps h1 to Heading 1; demote the per-module eyebrow to a plain paragraph
  });
  const docxHtml = path.join(tmp, "course.html");
  fs.writeFileSync(docxHtml, await pp.content());
  execFileSync("pandoc", [docxHtml, "-f", "html", "-t", "docx", "--toc", "--toc-depth=1",
    "--resource-path", tmp, "--metadata", "title=ELE 717 Solid State Electronics",
    "--metadata", "subtitle=A week-by-week course following the 15-week Lecture 2 plan",
    "-o", path.join(outDir, BASE + ".docx")]);
  fs.rmSync(tmp, { recursive: true, force: true });

  await browser.close();
  for (const ext of ["pdf", "docx"]) {
    const f = path.join(outDir, `${BASE}.${ext}`);
    console.log(f, fs.statSync(f).size, "bytes");
  }
})();
