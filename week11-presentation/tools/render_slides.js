// render_slides.js <jobs.json> <out-dir>
// Renders each slide page at 1920×1080. For a build step k, pinned elements whose
// data-build-in order is above k are hidden. Writes s000.png… and boxes.json
// (the position of every video frame on each slide).
const fs = require("fs"), path = require("path");
const { execSync } = require("child_process");
const { chromium } = require(execSync("npm root -g").toString().trim() + "/playwright");

(async () => {
  const [spec, out] = process.argv.slice(2);
  const jobs = JSON.parse(fs.readFileSync(spec, "utf8"));
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1920, height: 1080 } });
  const boxes = [];
  for (let i = 0; i < jobs.length; i++) {
    const file = path.join(out, `page${i}.html`);
    fs.writeFileSync(file, jobs[i].html);
    await p.goto("file://" + file, { waitUntil: "networkidle" });
    await p.evaluate(() => document.fonts.ready);
    const step = jobs[i].step;
    boxes.push(await p.evaluate(step => {
      if (step !== null) document.querySelectorAll("[data-build-in]").forEach(el => {
        const n = +(el.getAttribute("data-build-in").split(" ")[1] || 0);
        if (n > step) el.style.visibility = "hidden";
      });
      return [...document.querySelectorAll("img[data-video]")].map(el => {
        const r = el.getBoundingClientRect();
        const id = s => (s.match(/[0-9a-f]{32}/) || [""])[0];
        return { x: r.x, y: r.y, w: r.width, h: r.height,
                 video: id(el.getAttribute("data-video")), still: el.getAttribute("src").replace("file://", "") };
      });
    }, step));
    await p.waitForTimeout(150);
    await p.screenshot({ path: path.join(out, `s${String(i).padStart(3, "0")}.png`) });
  }
  fs.writeFileSync(path.join(out, "boxes.json"), JSON.stringify(boxes));
  await b.close();
})();
