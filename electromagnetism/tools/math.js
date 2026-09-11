/* ---- Mathematical typesetting -------------------------------------------
   Turns the plain-text notation used in the source files into real typographic
   subscripts and superscripts:

     a_x        -> a with subscript x
     E_t1       -> E with subscript t1
     e^{-jBz}   -> e with superscript -jBz
     r2 / 10-12 written with Unicode super/subscript characters is normalised
     to the same markup, so one mechanism handles everything.

   Runs after bold/italic and before code spans are restored, so code stays
   literal.                                                                  */

const SUP_CHARS = { "⁰":"0","¹":"1","²":"2","³":"3","⁴":"4",
  "⁵":"5","⁶":"6","⁷":"7","⁸":"8","⁹":"9",
  "⁻":"−","⁺":"+","ⁿ":"n" };
const SUB_CHARS = { "₀":"0","₁":"1","₂":"2","₃":"3","₄":"4",
  "₅":"5","₆":"6","₇":"7","₈":"8","₉":"9",
  "₋":"−","₊":"+","ₓ":"x","ᵧ":"y" };

const SUP_RE = /[⁰¹²³⁴-⁹⁺⁻ⁿ]+/g;
const SUB_RE = /[₀-₉₊₋ₓᵧ]+/g;

/* letters (incl. Greek), digits, and a leading sign are allowed in a bare run */
const RUN = "[A-Za-z0-9\\u0370-\\u03FF]";

function normaliseUnicodeScripts(s){
  s = s.replace(SUP_RE, m => "^{" + Array.from(m).map(c => SUP_CHARS[c]).join("") + "}");
  s = s.replace(SUB_RE, m => "_{" + Array.from(m).map(c => SUB_CHARS[c]).join("") + "}");
  return s;
}

/* Resolve marker{...} with brace counting, so a group may contain nested braces
   (Unicode normalisation injects them: e^{jω₀t} becomes e^{j_{0}t} first). */
function braced(s, marker, tag){
  let out = "", i = 0;
  for(;;){
    const j = s.indexOf(marker + "{", i);
    if(j < 0){ out += s.slice(i); return out; }
    out += s.slice(i, j);
    let depth = 0, k = j + 1;
    for(; k < s.length; k++){
      if(s[k] === "{") depth++;
      else if(s[k] === "}" && --depth === 0) break;
    }
    if(k >= s.length){ out += s.slice(j); return out; }   // unbalanced: leave alone
    out += "<" + tag + ">" + mathify(s.slice(j + 2, k)) + "</" + tag + ">";
    i = k + 1;
  }
}

function mathify(s){
  /* explicit groups first, recursing into their contents */
  s = braced(s, "^", "sup");
  s = braced(s, "_", "sub");
  /* then Unicode scripts, which become groups of their own */
  s = normaliseUnicodeScripts(s);
  s = braced(s, "^", "sup");
  s = braced(s, "_", "sub");
  /* finally bare runs: a_x, ^2 */
  s = s.replace(new RegExp("\\^(" + RUN + "+)", "g"), (m,c) => "<sup>" + c + "</sup>");
  s = s.replace(new RegExp("_("  + RUN + "+)", "g"), (m,c) => "<sub>" + c + "</sub>");
  return s;
}

/* ---- Matrices ------------------------------------------------------------
   ```matrix
   lhs: A x B  =
   style: det          (det = vertical bars, bracket = square brackets)
   a_x ; a_y ; a_z
   A_x ; A_y ; A_z
   ```                                                                       */
function matrixToHtml(body, esc){
  let lhs = "", style = "det";
  const rows = [];
  body.split("\n").forEach(line => {
    if(!line.trim()) return;
    const d = line.match(/^\s*(lhs|style)\s*:\s*(.*)$/i);
    if(d){ if(d[1].toLowerCase() === "lhs") lhs = d[2]; else style = d[2].trim(); return; }
    rows.push(line.split(";").map(c => c.trim()));
  });
  const body_ = rows.map(r =>
    "<tr>" + r.map(c => "<td>" + mathify(esc(c)) + "</td>").join("") + "</tr>").join("");
  return '<div class="eqrow">' +
      (lhs ? '<span class="eqlhs">' + mathify(esc(lhs)) + "</span>" : "") +
      '<span class="mat mat-' + (style === "bracket" ? "bracket" : "det") + '">' +
      "<table>" + body_ + "</table></span></div>";
}
