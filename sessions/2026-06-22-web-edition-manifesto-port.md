# Session — Web edition ported to the full manifesto (2026-06-22)

## What was asked

"Update the web version of the book with the new content. Be creative — explanatory diagrams, snapshots
from the Refine site, interactive illustrations." Two scoping decisions were taken with the author:

- **Content scope:** *Make it the full manifesto* — port the developed 20-chapter manuscript (with the new
  on-ramp, glossary, and chapter signposts) into the reader's shell. This supersedes the Chapter-1 preview.
- **Voice:** *Keep the manifesto voice* — first-person essayistic; no rewriting into documentary register.

The developed manuscript lives in the sister `refine` repo as `ROP_MANIFESTO_v0_1.md`; it was copied in as
`manuscript/rop-manifesto.md` so the build is self-contained.

## What was built

A small generator (no runtime build; the deployment artifact stays a single self-contained `index.html`):

- **`web/build.py`** — converts `manuscript/rop-manifesto.md` → `web/index.html`. Parses the manuscript into
  25 pages (Preface, Start-here, Ch 1–20, Coda, About, Glossary), converts Markdown → the reader's exact
  article structure (paragraphs, `## §` → subsection headings, lists, blockquotes with preserved line breaks,
  code, the italic chapter-signpost → a styled lede), generates overview cards + sidebar links + articles with
  `data-prev/next` wired, and wraps everything in the pristine shell. Idempotent.
- **`web/figures.py`** — six custom SVG diagrams (color inside figures only), injected into specific chapters:
  Ch 2 *line → refinement*, Ch 3 *tree → typed graph*, Ch 4 *the four-stage compiler / gate*, **Ch 5 an
  interactive cascade** (auto-plays on scroll-into-view; click/Replay; demonstrates early-cutoff with 4 dim
  downstream nodes), Ch 6 *Zero Trust access ∥ Refine change* (same loop, different object), Ch 8 an
  illustration of the Refine IDE's Cascade facet (labeled as an illustration, not a screenshot).
- **`web/shell.template.html`** — the reader's pristine shell (head + full stylesheet + routing script),
  extracted as a stable build input so re-running the build never reads its own output.

The reader's routing/font/print/keyboard JS is reused verbatim (it reads `data-slug/prev/next` from the DOM,
so generated articles "just work").

## Verification (browser preview, port 8732)

- Overview renders: AYOUNI wordmark, manifesto subtitle, first cards are Preface + Start-here.
- 25 articles / 25 sidebar links / 25 cards; prev/next continuous (Preface has no prev, Glossary no next).
- Interactive cascade auto-plays and renders correctly (14 ring-1 lit + 6 ring-2, 4 dim = early cutoff); the
  red `penalty_cap` core, the counter, the orange "click to watch" hint and Replay all present.
- All six figures present as inline SVG; subsection headings, serif prose, bold glossary terms, and the
  line-broken verdict blockquotes render; **console clean (no errors)**.
- `0` occurrences of the forbidden word "substrate"; body prose monochrome (color only inside figures).

## Notes / open items

- **`cover.png` is not in this checkout** (only `COVER_PLACEHOLDER.md`); the hero shows alt text until the
  author drops a real `cover.png` in `web/`. Pre-existing; not introduced here.
- The repo is **not a git repo** in this checkout (no `.git`). During the build I briefly overwrote the
  original preview `index.html`; it was fully reconstructed into `shell.template.html` (the corruption only
  *appended* a duplicate tail — the pristine head/CSS and routing script were intact). The build is now
  idempotent (reads the template, never its own output).
- To regenerate: `python web/build.py`. To re-verify visually: a static server on `web/` (e.g.
  `python -m http.server --directory web`).
- `CLAUDE.md` "Web reader" section carries the durable decision note so the web edition is not reverted to the
  documentary preview without a fresh instruction.
