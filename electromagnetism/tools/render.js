/* Minimal markdown renderer, inlined so the page has no external dependencies. */
function mdToHtml(src){
  const esc = s => s.replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;");
  function inline(s){
    s = esc(s);
    const codes = [], figs = [];
    s = s.replace(/`([^`]+)`/g, function(m,c){ codes.push(c); return "\u0001" + (codes.length-1) + "\u0002"; });
    s = s.replace(/\*\*([^*]+)\*\*/g, "<strong>$1</strong>");
    s = s.replace(/\*([^*]+)\*/g, "<em>$1</em>");
    /* images: ![alt](src) — src is inlined as a data URI at build time */
    /* lazy alt so captions may contain brackets, e.g. "the sequence s[n]" */
    s = s.replace(/!\[([\s\S]*?)\]\(([^)\s]+)\)/g, function(m,alt,src){
      figs.push('<img src="' + src + '" alt="' + alt + '">');
      return "\u0005" + (figs.length-1) + "\u0006";
    });
    s = mathify(s);
    s = s.replace(/\u0005(\d+)\u0006/g, function(m,i){ return figs[+i]; });
    s = s.replace(/\u0001(\d+)\u0002/g, function(m,i){ return "<code>" + codes[+i] + "</code>"; });
    return s;
  }
  // Prose reflows; notation blocks (formula sheet, equation runs) keep their line breaks.
  function joinLines(arr){
    const mathy = arr.filter(x => /[=|⇒⟺→∮∫∇×·√]/.test(x)).length;
    const sep = (arr.length > 1 && mathy >= arr.length / 2) ? "<br>" : " ";
    // Join first, then parse inline markup, so **bold** spanning a source line
    // break is still closed correctly. \u0004 stands in for the join point.
    return inline(arr.join("\u0004")).split("\u0004").join(sep);
  }
  const lines = String(src).replace(/\r\n?/g,"\n").split("\n");
  const blank = l => !l.trim();
  const startsBlock = l =>
    /^#{1,6}\s/.test(l) || /^>\s?/.test(l) || /^```/.test(l) ||
    /^(---|\*\*\*|___)\s*$/.test(l) || /^\s*[-*]\s+/.test(l) ||
    /^\s*\d+\.\s+/.test(l) || /^\s*\|/.test(l) || /^ {4}\S/.test(l);
  const out = [];
  let i = 0;
  while(i < lines.length){
    const l = lines[i];
    if(blank(l)){ i++; continue; }

    if(/^```/.test(l)){
      const isMatrix = /^```\s*matrix\b/.test(l);
      const isFigure = /^```\s*figure\b/.test(l);
      i++; const buf = [];
      while(i < lines.length && !/^```/.test(lines[i])) buf.push(lines[i++]);
      i++;
      out.push(isMatrix ? matrixToHtml(buf.join("\n"), esc)
             : isFigure ? buf.join("\n")          /* already HTML, built locally */
                        : "<pre><code>" + esc(buf.join("\n")) + "</code></pre>");
      continue;
    }
    if(/^(---|\*\*\*|___)\s*$/.test(l)){ out.push("<hr>"); i++; continue; }

    const h = l.match(/^(#{1,6})\s+(.*)$/);
    if(h){ const n = h[1].length; out.push("<h"+n+">" + inline(h[2]) + "</h"+n+">"); i++; continue; }

    if(/^\s*\|/.test(l) && i+1 < lines.length && /^\s*\|[\s:|-]+\|\s*$/.test(lines[i+1])){
      // "\\|" is an escaped pipe (e.g. |A| for magnitude), not a cell separator.
      const cells = r => r.trim().replace(/\\\|/g,"\u0003").replace(/^\|/,"").replace(/\|$/,"")
                          .split("|").map(c => c.trim().replace(/\u0003/g,"|"));
      const head = cells(l); i += 2; const rows = [];
      while(i < lines.length && /^\s*\|/.test(lines[i])) rows.push(cells(lines[i++]));
      out.push("<table><thead><tr>" + head.map(c => "<th>"+inline(c)+"</th>").join("") +
        "</tr></thead><tbody>" +
        rows.map(r => "<tr>" + r.map(c => "<td>"+inline(c)+"</td>").join("") + "</tr>").join("") +
        "</tbody></table>");
      continue;
    }

    if(/^>\s?/.test(l)){
      const buf = [];
      while(i < lines.length && /^>\s?/.test(lines[i])) buf.push(lines[i++].replace(/^>\s?/,""));
      out.push("<blockquote>" + mdToHtml(buf.join("\n")) + "</blockquote>"); continue;
    }

    if(/^ {4}\S/.test(l)){
      const buf = [];
      while(i < lines.length && (/^ {4}/.test(lines[i]) ||
            (blank(lines[i]) && /^ {4}\S/.test(lines[i+1] || "")))){
        buf.push(lines[i].replace(/^ {4}/,"")); i++;
      }
      out.push('<div class="eq">' + mathify(esc(buf.join("\n"))) + "</div>"); continue;
    }

    if(/^\s*[-*]\s+/.test(l) || /^\s*\d+\.\s+/.test(l)){
      const ordered = /^\s*\d+\.\s+/.test(l);
      const re = ordered ? /^\s*\d+\.\s+/ : /^\s*[-*]\s+/;
      const items = [];
      while(i < lines.length && !blank(lines[i])){
        if(re.test(lines[i])){ items.push(lines[i].replace(re,"")); i++; }
        else if(/^\s+\S/.test(lines[i]) && items.length){ items[items.length-1] += "\n" + lines[i].trim(); i++; }
        else break;
      }
      const tag = ordered ? "ol" : "ul";
      out.push("<"+tag+">" + items.map(t => "<li>" + joinLines(t.split("\n")) + "</li>").join("") + "</"+tag+">");
      continue;
    }

    const buf = [];
    while(i < lines.length && !blank(lines[i]) && !startsBlock(lines[i])){ buf.push(lines[i]); i++; }
    if(!buf.length){ buf.push(lines[i]); i++; }
    out.push("<p>" + joinLines(buf) + "</p>");
  }
  return out.join("\n");
}
