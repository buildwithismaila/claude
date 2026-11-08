# Reference verification report

Date of checks: 2026-11-08
Checked by: automated session, live page fetches only.

## Method and its limits — read this first

Every statement below is drawn from a page that was actually opened in this
session. Nothing is filled in from memory, and nothing is taken from a search
engine snippet. Where a field could not be read, it is marked
`NOT ESTABLISHED` rather than guessed.

**A large part of this reference list could not be verified, because most of
the relevant publishers refused the request.** The session's network policy
allows the publisher hosts, so this is not a policy block; the publishers
themselves served refusals to this client:

| Host | What happened when opened |
|---|---|
| `www.frontiersin.org` | **200 OK, full page** — usable |
| `arxiv.org` | **200 OK, full page** — usable |
| `standards.ieee.org` | **200 OK, full page** — usable |
| `www.mdpi.com` | HTTP 403, Akamai `Access Denied` body (ref #18.c4680117.1794119351.b536716a) |
| `onlinelibrary.wiley.com` | HTTP 403, Cloudflare `Just a moment...` interstitial |
| `www.sciencedirect.com` | HTTP 403; an 833 kB body is returned but it is the Elsevier bot-challenge shell, with no `citation_*` metadata and no article text |
| `link.springer.com` | HTTP 303 redirect to `idp.springer.com`, which is **not** in the allowlist and does not resolve |
| `ieeexplore.ieee.org` | HTTP 202 with an empty body (JavaScript wall); the `/rest/document/<id>/metadata` endpoint returns the HTML shell, not JSON |
| `www.semanticscholar.org` | HTTP 202 empty body; `/paper/DOI:...` returns HTTP 403 |
| `api.crossref.org`, `api.semanticscholar.org`, `idp.springer.com`, `joss.theoj.org` | Blocked by the session network policy (proxy `CONNECT` 403 / DNS failure) — **not in the allowlist** |

No attempt was made to disguise this client as a browser in order to get past
the challenge pages.

**To finish entries 2, 3, 4, 5, 6, 9, 10, 12 and 13, either open those pages
from a normal browser, or add `api.crossref.org` (and ideally
`joss.theoj.org`, `idp.springer.com`, `www.jmlr.org`, `www.nature.com`) to the
session's allowed hosts.** `api.crossref.org` alone would settle almost all of
the outstanding volume/issue/page fields, because it serves the publisher-
deposited record for any DOI.

### Status summary

| # | Entry | Status |
|---|---|---|
| 1 | IEEE Std 1159 | **VERIFIED** |
| 2 | Mishra, review, ITEES | **NOT VERIFIED** (secondary note) |
| 3 | Wang/Xu/Che, Applied Sciences | **NOT VERIFIED** — open question left unresolved |
| 4 | Khokhar et al., Measurement | **NOT VERIFIED** (secondary note) |
| 5 | Review, Comput. Electr. Eng. 2025 | **NOT VERIFIED** |
| 6 | Kapoor & Narayanan, Patterns | **PARTIAL** |
| 7 | Harris et al., NumPy | **PARTIAL** (substantially confirmed) |
| 8 | Pedregosa et al., scikit-learn | **PARTIAL** |
| 9 | Lee et al., PyWavelets, JOSS | **PARTIAL** — DOI is registered; record not opened |
| 10 | Huang et al., Neurocomputing | **NOT VERIFIED** |
| 11 | Li et al., Front. Energy Res. | **VERIFIED** |
| 12 | Shukla, Mishra & Singh, IEEE TPWRD | **PARTIAL** — it does exist |
| 13 | HHT + SVM, Electr. Eng. (Springer) | **NOT VERIFIED** |
| 14 | DWT + ELM, Front. Energy Res. 2024 | **VERIFIED** — your title was wrong |
| 15 | Synthetic PQD signal models | **VERIFIED, via a different source** |

---

## 1. IEEE Std 1159 — VERIFIED

**Current edition is still 1159-2019. No 2025 revision has been published.**

Citation as established:

> IEEE Std 1159-2019, *IEEE Recommended Practice for Monitoring Electric Power
> Quality*, IEEE, 2019.

URLs opened:
- `https://standards.ieee.org/standard/1159-2019.html`
- `https://standards.ieee.org/ieee/1159/11088/`

What the pages said:
- The 1159-2019 page gives the designation **"IEEE 1159-2019"**, the title
  **"IEEE Recommended Practice for Monitoring Electric Power Quality"**, status
  **"Active Standard"**, superseding 1159-2009.
- The project page gives **"P1159"**, title **"Recommended Practice for
  Monitoring Electric Power Quality"**, status **"Active PAR"**, PAR approval
  **2022-11-10**, superseding **1159-2019**.

Discrepancy against your list: none. On your parenthetical question — a
revision *project* exists (P1159, PAR approved 2022-11-10) but it is an
approved project, not a published standard. **Do not cite a 2025 edition.**
Note that the working-group section of the project page reads "No Active
Projects", which is inconsistent with the P1159 entry on the same page; if the
revision matters to the manuscript, re-check closer to submission.

---

## 2. Mishra, "Power quality disturbance detection and classification …" — NOT VERIFIED

URLs attempted:
- `https://onlinelibrary.wiley.com/doi/10.1002/2050-7038.12008` — HTTP 403,
  Cloudflare challenge page, both via the page fetcher and via a direct
  request. No metadata returned.
- `https://doi.org/...` content negotiation for Crossref metadata — the DOI
  resolver redirects to `api.crossref.org`, which the session policy blocks
  (proxy `CONNECT` 403).

**Full author list, volume, issue and article number/pages: NOT ESTABLISHED.**

Secondary note — *not* a verification, offered only because you flagged this
entry as needing an author list. In the reference list of a paper that *was*
opened (arXiv:1904.02836, reference [1]) this work is cited as:

> M. Mishra, "Power quality disturbance detection and classification using
> signal processing and soft computing techniques: A comprehensive review",
> *Int. Trans. Electr. Energy Syst.*, Wiley, pp. 1-42, Dec. 2018.

That is a third party's bibliography, not the publisher's record. It suggests
a **single author** (which would make "Mishra" correct without "et al.") and
an **online-first date of December 2018** with the issue year 2019 — which
would reconcile your "2019" with a 2018 first appearance. It gives pp. 1-42
and no volume or issue. **Do not put these numbers in the manuscript on this
basis.**

---

## 3. Wang, Xu, Che, Applied Sciences 9(11) 2315 — NOT VERIFIED

URLs attempted:
- `https://www.mdpi.com/2076-3417/9/11/2315` — HTTP 403, Akamai
  "Access Denied" body, via both the page fetcher and a direct request.
- `https://doi.org/10.3390/app9112315` — resolves to the same MDPI URL, same
  403.
- `https://www.semanticscholar.org/paper/DOI:10.3390/app9112315` — HTTP 403.

**Authors, exact title, and the discrete-vs-empirical wavelet question: ALL
NOT ESTABLISHED.**

This is the most consequential gap in this report. You flagged that the
abstract reportedly says **empirical** wavelet transform while the title says
**discrete**, and that the difference matters. **That question is still open.**
If the manuscript leans on this reference as a DWT baseline, the claim is
currently unsupported. Open the MDPI page in a browser before submission — MDPI
is fully open access, so the abstract will be visible immediately, and the
answer will take one minute.

---

## 4. Khokhar et al., Measurement — NOT VERIFIED

URL attempted:
- `https://www.sciencedirect.com/science/article/pii/S0263224116305619` —
  HTTP 403. A body was returned but it is the Elsevier bot-challenge shell:
  no `citation_*` meta tags, no `__NEXT_DATA__`, no occurrence of
  "power quality" anywhere in 833 kB.

**Author list, volume and pages: NOT ESTABLISHED from the publisher.**

Secondary note — from the reference list of arXiv:2407.04739 (reference [23]),
a page that was opened:

> S. Khokhar, A. A. M. Zin, A. P. Memon, and A. S. Mokhtar, "A new optimal
> feature selection algorithm for classification of power quality disturbances
> using discrete wavelet transform and probabilistic neural network,"
> *Measurement*, vol. 95, pp. 246–259, 2017.

Four authors, vol. 95, pp. 246–259, 2017. Again: a third party's bibliography,
so treat it as a lead to confirm, not as a verified citation.

---

## 5. "Comprehensive review of power quality disturbance detection and classification techniques", Comput. Electr. Eng., 2025 — NOT VERIFIED

URL attempted:
- `https://www.sciencedirect.com/science/article/pii/S0045790625004550` —
  HTTP 403, Elsevier bot-challenge shell as above.

**Authors, volume, pages, and even the exact title: NOT ESTABLISHED.** Nothing
confirms this article exists; equally, nothing shows it does not. The PII is
well formed and consistent with a 2025 Elsevier article, but that is a
guess about a numbering scheme, not evidence.

---

## 6. Kapoor & Narayanan, Patterns 4(9) 100804, 2023 — PARTIAL

**The work and its two authors are confirmed. The published Patterns record is
not.**

URL opened:
- `https://arxiv.org/abs/2207.07048`

What that page gives:
- Title (preprint): **"Leakage and the Reproducibility Crisis in ML-based
  Science"**
- Authors: **Sayash Kapoor and Arvind Narayanan** — exactly two, in that order
- arXiv DOI 10.48550/arXiv.2207.07048, submitted 14 July 2022
- No journal reference shown on the arXiv page

NOT ESTABLISHED: the journal title you listed ("… machine-learning-based
science"), the journal name Patterns, volume 4, issue 9, article 100804, and
the year 2023. The Patterns version sits on Cell Press/ScienceDirect, which
returned the 403 described above.

Note the preprint title differs from the title you listed — preprint and
published titles commonly differ here, and yours looks like the published
form, but that could not be confirmed. Confirm the published title, volume,
issue and article number before submission.

---

## 7. Harris et al., "Array programming with NumPy" — PARTIAL (substantially confirmed)

URL opened:
- `https://arxiv.org/abs/2006.10256`

Confirmed from that page's `citation_*` metadata:
- **DOI 10.1038/s41586-020-2649-2** — matches your entry exactly
- Journal reference: **"Nature 585, 357 (2020)"** — volume **585**, first page
  **357**, year **2020** all match
- Full author list, in order: Charles R. Harris, K. Jarrod Millman,
  Stéfan J. van der Walt, Ralf Gommers, Pauli Virtanen, David Cournapeau,
  Eric Wieser, Julian Taylor, Sebastian Berg, Nathaniel J. Smith, Robert Kern,
  Matti Picus, Stephan Hoyer, Marten H. van Kerkwijk, Matthew Brett,
  Allan Haldane, Jaime Fernández del Río, Mark Wiebe, Pearu Peterson,
  Pierre Gérard-Marchant, Kevin Sheppard, Tyler Reddy, Warren Weckesser,
  Hameer Abbasi, Christoph Gohlke, Travis E. Oliphant

Citation as established:

> C. R. Harris *et al.*, "Array programming with NumPy," *Nature*, vol. 585,
> p. 357, 2020, doi: 10.1038/s41586-020-2649-2.

Two small things NOT ESTABLISHED, because `www.nature.com` is not in the
allowlist and was not opened:
- **The end page.** Your entry says 357-362; the arXiv journal reference gives
  only the start page 357. 357-362 is very likely right but was not read.
- **Title capitalisation.** arXiv renders it "Array **P**rogramming with
  NumPy"; you have lowercase "programming", which is the usual Nature style.
  Not confirmed either way.

---

## 8. Pedregosa et al., "Scikit-learn: Machine Learning in Python" — PARTIAL

URL opened:
- `https://arxiv.org/abs/1201.0490`

Confirmed from that page:
- Title: **"Scikit-learn: Machine Learning in Python"** — matches
- Journal reference: **"Journal of Machine Learning Research (2011)"** —
  journal and year match
- Full author list, in order: Fabian Pedregosa, Gaël Varoquaux,
  Alexandre Gramfort, Vincent Michel, Bertrand Thirion, Olivier Grisel,
  Mathieu Blondel, Andreas Müller, Joel Nothman, Gilles Louppe,
  Peter Prettenhofer, Ron Weiss, Vincent Dubourg, Jake Vanderplas,
  Alexandre Passos, David Cournapeau, Matthieu Brucher, Matthieu Perrot,
  Édouard Duchesnay

NOT ESTABLISHED: **volume 12 and pages 2825-2830.** The arXiv journal
reference carries the year only, with no volume or page numbers, and
`www.jmlr.org` is not in the allowlist. Those two fields in your entry remain
unchecked.

---

## 9. Lee et al., "PyWavelets", JOSS — PARTIAL (the DOI is registered)

You marked this uncorroborated. The position now:

**The DOI exists and is registered.** `https://doi.org/10.21105/joss.01237`
was opened and returned **HTTP 302 Found** with
`Location: http://joss.theoj.org/papers/10.21105/joss.01237`. A DOI that
resolves to a specific JOSS paper URL is strong evidence the paper exists:
unregistered DOIs return 404 from the resolver, not a redirect.

**But the record itself was not read.** `joss.theoj.org` is **not in the
session allowlist** and does not resolve, so the target page could not be
opened. Authors, title, volume, issue, article number and year are therefore
all **NOT ESTABLISHED**, including whether the five authors you list
(Lee, Gommers, Waselewski, Wohlfahrt, O'Leary) are complete and correctly
ordered, and whether volume 4, issue 36 and article 1237 are right.

This is the cheapest remaining gap to close: add `joss.theoj.org` to the
allowlist, or open the URL above in a browser.

---

## 10. Huang, Xu, Liu, Lin, Neurocomputing 98, 12-23, 2012 — NOT VERIFIED

URL attempted:
- `https://www.sciencedirect.com/science/article/pii/...` could not be used
  because no PII was supplied for this entry, and ScienceDirect's search and
  article pages both return the HTTP 403 bot-challenge described above.
  ScienceDirect is the only allowed host that carries Neurocomputing.

**Author initials, volume and pages: NOT ESTABLISHED.** No corroboration of
any kind was found for this entry in any page opened during this session.
Nothing shows it does not exist, but nothing supports it either.

Caution: several papers cite a closely related and much better known work —
S. Mishra, C. N. Bhende and B. K. Panigrahi, "Detection and classification of
power quality disturbances using S-transform and probabilistic neural
network", *IEEE Trans. Power Delivery*, vol. 23, no. 1, pp. 280-287, 2008
(seen in the reference list of arXiv:1904.02836, reference [16]). The title is
nearly identical to your entry 10. **Check that entry 10 is not a garbled
version of that IEEE paper** before trusting it.

---

## 11. Li, Liu, Wang, Bi, Frontiers in Energy Research — VERIFIED

URL opened:
- `https://www.frontiersin.org/journals/energy-research/articles/10.3389/fenrg.2021.708131/full`

Read directly from the page's `citation_*` metadata:

> J. Li, H. Liu, D. Wang, and T. Bi, "Classification of Power Quality
> Disturbance Based on S-Transform and Convolution Neural Network,"
> *Frontiers in Energy Research*, vol. 9, art. 708131, 2021,
> doi: 10.3389/fenrg.2021.708131.

- Authors, in order: **Li, Jinsong; Liu, Hao; Wang, Dengke; Bi, Tianshu**
- **Volume 9**, `citation_firstpage` / article number **708131**
- Published 28 June 2021 (online 7 June 2021)

Discrepancy against your list: none. The surnames and order you gave
("Li, Liu, Wang, Bi") and the title are confirmed exactly as listed. The two
fields you asked for are **volume 9** and **article number 708131**; the full
given names are Jinsong, Hao, Dengke and Tianshu respectively.

---

## 12. Shukla, Mishra & Singh, IEEE Trans. Power Delivery, 2009 — PARTIAL

**This paper does exist.** It is not a phantom reference.

URL attempted for the publisher record:
- `https://ieeexplore.ieee.org/...` — IEEE Xplore returns HTTP 202 with an
  empty body to this client, and its `/rest/document/<id>/metadata` endpoint
  returns the HTML shell rather than JSON. The authoritative record could not
  be opened.

Evidence that it exists, read on pages that *were* opened — the reference
lists of both versions of arXiv:1904.02836
(`https://arxiv.org/html/1904.02836v1`, `https://arxiv.org/html/1904.02836v2`),
which are differently typeset bibliographies and agree on every field:

> v1, reference [21]: Stuti Shukla, S. Mishra and Bhim Singh, "Empirical mode
> decomposition with Hilbert transform for power-quality assesment",
> *IEEE Trans. on Power Del.*, vol. 24, no. 4, pp. 2159-2165, Oct. 2009.

> v2, reference [21]: Shukla, S., Mishra, S., Singh, B.: 'Empirical-mode
> decomposition with hilbert transform for power-quality assessment',
> *IEEE Transactions on Power Delivery*, 2009, 24, (4), pp. 2159-2165

Best citation available:

> S. Shukla, S. Mishra, and B. Singh, "Empirical-mode decomposition with
> Hilbert transform for power-quality assessment," *IEEE Trans. Power
> Delivery*, vol. 24, no. 4, pp. 2159-2165, Oct. 2009.

Initials established as **S. Shukla** (Stuti Shukla), **S. Mishra**,
**B. Singh** (Bhim Singh); volume **24**, issue **4**, pages **2159-2165**,
year **2009** — consistent across both bibliographies.

Why this is PARTIAL and not VERIFIED: this is still the same class of evidence
you were right to distrust — other papers' reference lists. The two
bibliographies come from one paper, so they are one source, not two
independent ones. The agreement across two different reference formats, and
the fact that one of those authors (S. Mishra) is a co-author of several
other confirmed IEEE TPWRD papers, make a fabricated citation very unlikely.
Confirm on IEEE Xplore before submission. Note v1 misspells "assesment"; the
correct spelling is "assessment", per v2.

---

## 13. HHT + SVM, Electrical Engineering (Springer), 2020 — NOT VERIFIED

URLs attempted:
- `https://link.springer.com/article/10.1007/s00202-020-00987-8` — HTTP 303
  redirect to
  `https://idp.springer.com/authorize?response_type=cookie&client_id=springerlink&redirect_uri=...`
- `https://link.springer.com/content/pdf/10.1007/s00202-020-00987-8.pdf` —
  same 303 to the same identity provider
- `https://idp.springer.com/authorize?...` — **`idp.springer.com` is not in
  the allowlist and does not resolve**, so the redirect chain is a dead end

**Authors, volume and pages: NOT ESTABLISHED. Whether the paper compares HHT
against S-transform and wavelet methods under noise: NOT ESTABLISHED.** The
abstract was never seen, so the comparison claim is unsupported. If the
manuscript states that this paper benchmarks HHT against S-transform and
wavelet methods under noise, that statement currently rests on nothing.

Adding `idp.springer.com` to the allowed hosts should be enough — the redirect
normally bounces straight back to the article page and the abstract is free to
read.

---

## 14. DWT + ELM, Frontiers in Energy Research, 2024 — VERIFIED (your title was wrong)

URL opened:
- `https://www.frontiersin.org/journals/energy-research/articles/10.3389/fenrg.2024.1435704/full`

Read directly from the page's `citation_*` metadata:

> R. J. J. Molu, W. F. Mbasso, K. T. Saatong, S. R. Dzonde Naoussi,
> M. Alruwaili, A. Elrashidi, and W. Nureldeen, "Enhancing power quality
> monitoring with discrete wavelet transform and extreme learning machine: a
> dual-stage pattern recognition approach," *Frontiers in Energy Research*,
> vol. 12, art. 1435704, 2024, doi: 10.3389/fenrg.2024.1435704.

- Exact title: **"Enhancing power quality monitoring with discrete wavelet
  transform and extreme learning machine: a dual-stage pattern recognition
  approach"**
- Authors, in order: **Molu, Reagan Jean Jacques; Mbasso, Wulfran Fendzi;
  Saatong, Kenfack Tsobze; Dzonde Naoussi, Serge Raoul; Alruwaili, Mohammed;
  Elrashidi, Ali; Nureldeen, Waleed** — **seven** authors
- **Volume 12**, `citation_firstpage` / article number **1435704**
- Published 20 September 2024 (online 21 June 2024)

Discrepancy against your list: you had no title and no authors for this entry,
only a description ("a dual-stage DWT and extreme learning machine
framework"). Both are now established. Note the paper is an FPGA
implementation study (validated on a Xilinx Zynq-7000 SoC, 1.5 ms latency,
1.8 W) reporting 99.69% accuracy against STFT+SVM at 97.22% and FFT+ANN at
99.30% — if you cite it as a pure algorithm paper, that framing is incomplete.

---

## 15. Synthetic PQD signal models — VERIFIED, via a different source

### Your candidate: NOT VERIFIED

`https://www.sciencedirect.com/science/article/pii/S2667305324001200` — HTTP
403, Elsevier bot-challenge shell. Nothing about this article was read: not
its title, not its authors, not its parameter ranges. **Do not cite it on the
strength of this report.**

### A source that was opened, read and can be quoted

> F. Hafiz and C. Shahnaz, "A Machine Learning Based Classification Approach
> for Power Quality Disturbances Exploiting Higher Order Statistics in the EMD
> Domain," arXiv:1904.02836, 2019. doi: 10.48550/arXiv.1904.02836.

URLs opened: `https://arxiv.org/abs/1904.02836`,
`https://arxiv.org/html/1904.02836v1`, `https://arxiv.org/html/1904.02836v2`
(v1 submitted 5 Apr 2019, v2 14 Aug 2019; 8 pages, 13 figures; no journal
reference listed).

This is the better fit for the manuscript's needs than your candidate would
have been, because its Table I covers **all** the classes the generator uses,
**including notch and the sag/swell-with-harmonics combinations** — which the
alternative source below does not.

**Table I, "Models of power quality disturbance signals", quoted verbatim.**
`E` is the amplitude, `f` the fundamental at 50 Hz, `u(t)` the unit step, `T`
the fundamental period:

| Disturbance | Equation | Parameters |
|---|---|---|
| Normal | `v(t) = E sin ω_c t` | `u(t)` is the unit function |
| Sag | `v(t) = E[1 − β{u(t−t₁) − u(t−t₂)}] sin ω_c t` | `0.1 ≤ β ≤ 0.9`, `T ≤ (t₂−t₁) ≤ 9T` |
| Swell | `v(t) = E[1 + β{u(t−t₁) − u(t−t₂)}] sin ω_c t` | `0.1 ≤ β ≤ 0.9`, `T ≤ (t₂−t₁) ≤ 9T` |
| Flicker | `v(t) = E[1 + β sin(2πα t)] sin ω_c t` | `0.1 ≤ β ≤ 0.2`, `5 Hz ≤ α ≤ 20 Hz` |
| Interruption | `v(t) = E[1 − β{u(t−t₁) − u(t−t₂)}] sin ω_c t` | `0.9 ≤ β ≤ 1`, `T ≤ (t₂−t₁) ≤ 9T` |
| Transient | `v(t) = E[sin ω_c t + β e^((t−t₁)/τ) sin{2π f_n (t−t₁)}{u(t₂) − u(t₁)}]` | `0.1 ≤ β ≤ 0.9`, `0.5T ≤ (t₂−t₁) ≤ 3T`, `300 Hz ≤ f_n ≤ 900 Hz`, `8 ms ≤ τ ≤ 40 ms` |
| Harmonics | `v(t) = E[sin ω_c t + β₃ sin 3ω_c t + β₅ sin 5ω_c t]` | `0.1 ≤ β ≤ 0.9` *(see note)*, `0.05 ≤ β₃, β₅ ≤ 0.15` |
| Sag with harmonics | `v(t) = E[1 − β{u(t−t₁) − u(t−t₂)}] * [sin ω_c t + β₃ sin 3ω_c t + β₅ sin 5ω_c t]` | `0.1 ≤ β ≤ 0.9`, `T ≤ (t₂−t₁) ≤ 9T`, `0.05 ≤ β₃, β₅ ≤ 0.15` |
| Swell with harmonics | `v(t) = E[1 + β{u(t−t₁) − u(t−t₂)}] * [sin ω_c t + β₃ sin 3ω_c t + β₅ sin 5ω_c t]` | `0.1 ≤ β ≤ 0.9`, `T ≤ (t₂−t₁) ≤ 9T`, `0.05 ≤ β₃, β₅ ≤ 0.15` |
| Spike | `v(t) = E[sin ω_c t − sign(sin ω_c t) × {Σ_{n=0}^{9} κ × {u(t−(t₁+0.02n)) − u(t−(t₂+0.02n))}}]` | `0.1 ≤ κ ≤ 0.4`, `0 ≤ (t₂, t₁) ≤ 0.5T`, `0.01T ≤ (t₂−t₁) ≤ 0.05T` |
| Notch | `v(t) = E[sin ω_c t + sign(sin ω_c t) × {Σ_{n=0}^{9} κ × {u(t−(t₁+0.02n)) − u(t−(t₂+0.02n))}}]` | `0.1 ≤ κ ≤ 0.4`, `0 ≤ (t₂, t₁) ≤ 0.5T`, `0.01T ≤ (t₂−t₁) ≤ 0.05T` |

The eleven classes are named on the page as: C1 Normal, C2 Sag, C3 Swell,
C4 Fluctuation, C5 Interruption, C6 Transient, C7 Harmonics, Sag with
harmonics, Swell with harmonics, Spike, Notch. **Sampling frequency 2 kHz**
(stated in v2 alongside Table I).

*Note on two apparent errors in the source, reported as read:* the plain
Harmonics row lists `0.1 ≤ β ≤ 0.9` although no bare `β` appears in its
equation, and the Transient equation as typeset reads `β e^((t−t₁)/τ)` with a
positive exponent, which would grow rather than decay. Both look like
typesetting slips in the paper. Do not propagate them.

### A second source, also opened, with a 50 Hz single/compound split

> S. Pan, X. Nie, X. Zhai, B. Wang, H. Ge, C. He, and Z. Ding,
> "Classification of Power Quality Disturbances Using Resnet with Channel
> Attention Mechanism," arXiv:2407.04739, 2024.
> doi: 10.48550/arXiv.2407.04739.

URLs opened: `https://arxiv.org/abs/2407.04739`,
`https://arxiv.org/html/2407.04739v1` (submitted 2 Jul 2024). The page states
its Table I "is in adherence to IEEE standards", fixes the fundamental at
**50 Hz**, and draws parameters randomly within the stated ranges. Quoted:

| Label | Type | Parameters |
|---|---|---|
| V1 | Harmonic — `V(t) = sin(ωt) + α₃sin(3ωt+φ₃) + α₅sin(5ωt+φ₅) + α₇sin(7ωt+φ₇)` | `α₃ = 0∼0.15`, `α₅ = 0∼0.15`, `α₇ = 0∼0.15`, `φ₃, φ₅, φ₇ = 0∼2π` |
| V2 | sag — `V(t) = (1 − α(u(t−t₁) − u(t−t₂))) sin(ωt)` | `α = 0.1∼0.9`, `t₂−t₁ = 4T∼9T` |
| V3 | swell | `α = 0.1∼0.9`, `t₂−t₁ = 4T∼9T` |
| V4 | interrupt | `α = 0.9∼0.1` *(as printed; evidently 0.9∼1.0)*, `t₂−t₁ = 4T∼9T` |
| V5 | flicker — `V(t) = (1 + α_f sin(βωt)) sin(ωt)` | `α_f = 0.3∼0.5`, `β = 0.1∼0.4` |
| V6 | Oscillatory transient — `V(t) = sin(ωt) + α₂ e^(−(t−t₃)/τ) sin{ω_n(t−t₃)} · {u(t−t₃) − u(t−t₄)}` | `α₂ = 0.1∼0.8`, `τ = 0.008∼0.04`, `t₄−t₃ = 0.05T∼3T`, `f_n = 300∼900 Hz` |
| V7 | Impulsive transient — `V(t) = sin(ωt) + α₂ e^(−(t−t₃)/τ){u(t−t₃) − u(t−t₄)}` | `α₂ = 1∼10`, `τ = 0.008∼0.04`, `t₄−t₃ = 0.05T∼3T` |

Its compound classes V8–V18 are listed by name only (harmonics+sag,
harmonics+swell, interruption+harmonics, impulsive transient+sag/+swell/
+flicker/+harmonics, and three- and four-way combinations); **the compound
equations and ranges are not given in Table II on the page**, whose caption is
in fact mislabelled "ENVIRONMENT REQUIRED FOR THE EXPERIMENT". **This source
has no notch class.** Its flicker range (`α_f = 0.3∼0.5`) is far wider than
the other source's `0.1 ≤ β ≤ 0.2`, so the two do not agree; prefer
arXiv:1904.02836 as the primary citation and note the disagreement if both are
cited.

### Check against `pqclass/signals.py`

Comparing the quoted arXiv:1904.02836 ranges against the generator as it
currently stands. The file's own docstring already warns that its ranges are
unsourced; this is that check, as far as one openable source allows.

| Class | `signals.py` | arXiv:1904.02836 Table I | Verdict |
|---|---|---|---|
| normal | `sin(2πf₀t + φ)` | `E sin ω_c t` | **matches** |
| sag | `α ∈ [0.1, 0.9]`, duration 1–9 cycles | `0.1 ≤ β ≤ 0.9`, `T ≤ (t₂−t₁) ≤ 9T` | **matches exactly** |
| swell | `α ∈ [0.1, 0.8]`, duration 1–9 cycles | `0.1 ≤ β ≤ 0.9`, `T ≤ (t₂−t₁) ≤ 9T` | **upper bound differs** — code 0.8, source 0.9 |
| interruption | `α ∈ [0.9, 1.0]`, duration 1–9 cycles | `0.9 ≤ β ≤ 1`, `T ≤ (t₂−t₁) ≤ 9T` | **matches exactly** |
| harmonics | 3rd, 5th **and 7th**, each `∈ [0.05, 0.15]`, amplitudes renormalised so total power = 1 p.u. | 3rd and 5th only, `0.05 ≤ β₃, β₅ ≤ 0.15` | **differs** — the source has no 7th harmonic and no renormalisation. The 0.05–0.15 coefficient range matches. (arXiv:2407.04739 *does* carry a 7th harmonic, at `0∼0.15`.) |
| flicker | `α ∈ [0.1, 0.2]`, `β ∈ [5, 20]` Hz | `0.1 ≤ β ≤ 0.2`, `5 Hz ≤ α ≤ 20 Hz` | **matches exactly** (symbols swapped) |
| osc_transient | `α ∈ [0.1, 0.8]`, `f_n ∈ [300, 900]` Hz, `τ ∈ [8, 40]` ms, 0.5–3 cycles | `0.1 ≤ β ≤ 0.9`, `300–900 Hz`, `8–40 ms`, `0.5T–3T` | **upper bound differs** — code 0.8, source 0.9. All else matches exactly. |
| notch | multiplicative zeroing, `depth ∈ [0.4, 1.0]`, width 2–6 samples (≈`0.03T–0.09T`), **twice per cycle** | additive `sign(sin)` term, `0.1 ≤ κ ≤ 0.4`, width `0.01T–0.05T`, **once per cycle** (`Σ_{n=0}^{9}`, 0.02 s spacing) | **differs in form, depth and repetition rate** — the largest single discrepancy |
| sag_harmonics | sag envelope × harmonic signal, `α ∈ [0.1, 0.9]` | `E[1 − β{…}] * [sin ω_c t + β₃ sin 3ω_c t + β₅ sin 5ω_c t]`, same ranges | **matches in form and ranges**, apart from the 7th-harmonic difference above |

Also worth noting: `signals.py` samples at **3200 Hz** (64 samples/cycle) over
10 cycles, while arXiv:1904.02836 states **2 kHz**. That is a design choice
rather than an error, but if the manuscript cites that paper for the signal
models it should not also imply its sampling rate.

**Recommended changes if the manuscript is to cite arXiv:1904.02836 for the
generator:** widen `swell` to `α ∈ [0.1, 0.9]` and `osc_transient` to
`α ∈ [0.1, 0.9]`; decide explicitly whether to keep the 7th harmonic and the
power renormalisation (both are departures from the cited source, and the
renormalisation in particular interacts with the amplitude/RMS leakage issue
already documented in `generate_base`); and either adopt the source's additive
notch model with `κ ∈ [0.1, 0.4]` at one notch per cycle, or state in the
manuscript that the notch model is the authors' own and cite nothing for it.
