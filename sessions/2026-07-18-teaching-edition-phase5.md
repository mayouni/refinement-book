# Session — 2026-07-18 · Teaching Edition Phase 5: integration — the edition flipped

Phase 5 of `docs/teaching-edition-plan.md` executed. **The Teaching Edition is now the book at
`web/index.html`.**

## Coherence pass

Audited the complete manuscript: every Chapter-N cross-reference resolves to the right chapter (including
the glossary's 28 chapter pointers); 12 "What you now know" closes + Chapter 13's "What this book has
established" final ledger = all 13 chapters close correctly; canon numbers consistent throughout
(penalty cap 18 → 16, BCEAO-4.2, vat_rate 0.18 → 0.20 within 0.00..0.25, rfn-0207/0208 across Ch 5–7 and
the audit figure); the ten jungle words of Ch 1 all return in Ch 10; the 90-minute path's chapters all
exist; no doubled-word slips. No edits were needed — the phases were written against the same canon sheet.

## The flip

- `build.py` default now reads `manuscript/rop-book.md` → `web/index.html` with subtitle "A discipline for
  software in the agentic era". Verified idempotent (281,721 bytes twice), substrate-clean.
- **Git-less repo caveat honored:** ayouni is NOT under git, so CLAUDE.md's "delete the predecessor,
  git is the record" rule was deliberately waived for the manuscript — `manuscript/rop-manifesto.md`
  stays on disk as the record of the superseded edition, rebuildable via `python web/build.py --manifesto`
  → `web/manifesto.html` (verified working: 28 pages). Generated artifacts `teaching.html` and the
  verification `manifesto.html` were removed; deployment remains index.html + cover.png.
- CLAUDE.md brought current (the Phase-5 state note).

## Verification (live, desktop + mobile)

Overview: cover renders, subtitle correct, 20 chapter cards. Reader: 4 part labels ("Part N — Title"),
27 figures, search works over the new content ("wise coding" → 7 passages, first hit Chapter 9), Esc
behavior intact. Mobile 375px: no horizontal overflow, all figures fit the viewport, body text
left-aligned, drawer sidebar. Desktop restored after.

## State

The book: ~17,300 words, 13 chapters in 4 parts + Start here + coda + 28-term glossary, 27 SVG figures
(10 CLI panels from figpanels.py, 11 diagrams, 5 IDE illustrations + 2 legacy embeds incl. the animated
cascade). The author embraced the compact density by proceeding without deepening.

## Next

**Phase 6** — the final phase: the PDF edition. Print-composed HTML at 6×9 (front-matter sequence:
half-title, title, copyright, dedication, epigraph, contents; running heads; folios; chapter openers),
the giraffe cover + a newly designed back cover, headless-Chrome `book.pdf`, and the print QA checklist.
