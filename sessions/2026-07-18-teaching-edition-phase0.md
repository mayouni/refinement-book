# Session — 2026-07-18 · Teaching Edition Phase 0: infrastructure

Phase 0 of `docs/teaching-edition-plan.md` executed. Four deliverables:

1. **`manuscript/rop-book.md`** — the skeleton: title block, "Start here" front-matter stub (promise · map ·
   the `stz` note · 90-minute path, tagged for Phase 1), four part pages with real teaching-voice intros,
   13 chapter stubs each carrying its italic promise line and a phase-tagged content abstract, coda + glossary
   stubs. Heading conventions match `build.py`'s existing boundary grammar exactly (`# Part N —`,
   `# Chapter N —`, `# Coda —`, `## Start here —`, `## Appendix —`), so the proven parser needed no changes.
2. **`web/figpanels.py`** — the CLI-panel generator: every terminal figure is generated from a spec (segments
   of typed color kinds: prompt/cmd/flag/out/field/ok/fail/dim/num) so all panels share one geometry (760px,
   24px line height, rounded panel, neutral-dot title bar — no traffic-light yellow) and the reader's
   code-listing palette. Warns when a line exceeds the panel width. Demo panel **`cli-first-session`**
   (Ch 3's lift → points → refine → cascade → apply session) written to `assets/illustrations/cli/` and
   verified in the browser: clean SVG parse, 17 text lines, 49 tspans, all six palette colors.
3. **`docs/figure-register.md`** — 27 figures tracked (10 CLI · 11 diagrams · 5 IDE redraws + adapt notes
   for the six existing web-edition SVGs), with status flow planned → spec'd → drawn → placed and the
   captioning conventions.
4. **`build.py --teaching`** — builds `manuscript/rop-book.md` → `web/teaching.html` with subtitle
   "A discipline for software in the agentic era"; the default build is untouched (manifesto edition stays
   live at index.html until Phase 5 flips it). Verified: 20 pages (start-here + 4 parts + 13 chapters +
   coda + glossary), correct slugs and "Part N — Title" sidebar labels, idempotent (75,484 bytes twice),
   substrate-clean, and the manifesto build still byte-identical (28 pages, 525,056 bytes).

Plan ledger updated (§10: Phase 0 DONE). Screenshot capture in the preview pane was stuck again (the known
renderer hiccup) — verification done via DOM/JS inspection instead, as in prior sessions.

## Next

**Phase 1** on the author's go: draft Part I (Ch 1 The jungle · Ch 2 What broke · Ch 3 The unit changed)
in the teaching voice with all Part-I figures (jungle-map-before, bottleneck-moved, unit-changed,
cli-first-session already drawn, cli-explain), and the full "How to read this book" front matter. The
jungle map and the first `stz` session are the proof of concept — author review gates Phase 2.
