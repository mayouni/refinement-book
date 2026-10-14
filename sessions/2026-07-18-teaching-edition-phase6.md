# Session — 2026-07-18 · Teaching Edition Phase 6: the PDF edition — PROGRAM COMPLETE

Phase 6 of `docs/teaching-edition-plan.md` executed. **`web/book.pdf` exists: 106 pages, exactly 6×9in,
cover to back cover.** Phases 0–6 are all done; the Teaching Edition program is complete.

## The pipeline (`web/print.py`)

- Imports `build.py` (reusing its parsed pages + figure inlining) and composes `web/print.html`: the cover,
  half-title, title page, copyright (updated to "First edition: 2026 — the Teaching Edition"; CC BY-NC-ND /
  CC BY-NC-SA / MIT lines; ISBN pending), dedication and epigraph (reused from the front-matter drafts —
  both fit this book), a Contents page, the 20 body pages, and a newly designed back cover.
- Print CSS: 6×9in trim; EB Garamond body ~10.8pt justified with hyphenation and widow/orphan control;
  Inter chapter openers on recto; running heads via `string-set`; folios via `@bottom-center`; blank versos
  cleaned by `@page :blank`; figures `break-inside: avoid` (the interactive cascade renders fully lit via
  print overrides); **TOC with real page numbers** via paged.js `target-counter` (verified: "Start here 15 ·
  1 The jungle 19 · 2 What broke 27 …").
- **PDF generation lesson:** `--print-to-pdf` with `--virtual-time-budget` is unreliable under `--headless=new`
  (printed after 1 page at any budget). The working approach drives Chrome over the **DevTools protocol**
  (websocket-client + `--remote-debugging-port` + `--remote-allow-origins=*`): poll
  `.pagedjs_page` count until stable (~106 pages, ~20 s), then `Page.printToPDF` with `preferCSSPageSize`.

## The cover (author decision mid-phase)

The author supplied the **final flat cover artwork** (the clean giraffe illustration — found as
`refine-book-cover (1).png` in Downloads) and instructed: use it **as-is**; forget the HTML-composed cover
page I had begun (which would have carried the tagline on the front). Installed as `web/cover.png` +
`site/cover.png`; the old hand-held mockup photo archived to `assets/covers/archive/2026-06-handheld-mockup.png`;
the interim `print-giraffe.png` crop deleted; covers README updated. The author's requested sentence —
**"Stop trying to govern the intelligence, and govern the change."** — lives on the **back cover**, set in
orange italic at the close of the blurb (verified present in the PDF; pypdf's italic extraction shows it with
kerning gaps, which is an extraction artifact, not a rendering one).

## Bug fixed at source (both editions)

Asterisks inside code spans (e.g. `policy/*`) leaked into the italic regex pairing in `build.py inline()`,
corrupting one Ch 5 paragraph ("cares </em>what authority*…"). Fixed by stashing code spans behind
placeholders before emphasis processing. Web edition rebuilt; PDF regenerated; verified in both.

## QA (pypdf)

106 pages · 6.0×9.0in · substrate-clean · page 1 = the artwork, image-only · TOC p13 with real folio
targets · running heads + folios on body pages ("THE WORDS, PINNED 103") · blank versos truly empty ·
back cover = blurb + tagline + three reader lines + author line + AYOUNI wordmark + ISBN-pending box.

## Deployment artifacts

`web/index.html` + `web/cover.png` + `web/book.pdf` (print.html is a rebuildable intermediate; PDF builds
need network for fonts + paged.js CDN, and the `websocket-client` package).

## The program, closed

Phases 0–6 all DONE (ledger in the plan §10). The book: 13 chapters in 4 parts + Start here + coda +
28-term glossary; ~17.3k words; 27 SVG figures; web reader + 106-page press PDF from one manuscript;
taught on the open Softanza foundation via the `stz` idiom; Refine present as one commercial product's
IDE illustrations; Sonibank and Amina carrying every chapter. Remaining for the author (not Claude tasks):
artist credit on the copyright page, a real ISBN, and the day ayouni.press goes live.
