# Session — 2026-07-18 · Teaching Edition Phase 2: Part II drafted

Phase 2 of `docs/teaching-edition-plan.md` executed — the four mechanism chapters, with 13 figures.

## Prose (manuscript/rop-book.md)

- **Ch 4 — The graph** (1,319 w): opens on Amina's notebook page as a hand-computed graph traversal ("the most
  valuable map in the company is a folklore document"); tree-vs-graph; the satisfies edge as the compliance
  query-maker; the lift (files stay put, "each language's own parser is the authority", gaps reported not
  papered over); everything else demystified as graph operations; honest limit (the graph knows only the
  declared, but improves monotonically).
- **Ch 5 — The gate** (1,350 w): opens on Kofi's refused rename (the canon rename_score_function story —
  "a refusal is the fastest honest answer you can get"); the four stages walked with their questions; the
  landing verdict as "an argument, four sentences long"; the refusal grammar (what/why/next/learn) and its
  team effect ("the gate is strict so that people can be bold"); determinism + the honest limit (proves the
  declared, judges neither the undeclared nor the unwise).
- **Ch 6 — The cascade** (1,152 w): the review problem in Amina's numbers; the interactive cascade (reused);
  reading a cascade (depths, gates, **early cutoff** — "proven harmless, not assumed harmless"); what review
  becomes (the reviewer reads consequences, not bytes; judgment spent only where needed).
- **Ch 7 — Reversibility and the audit chain** (1,242 w): the Thursday-regulator callback; the stored typed
  inverse ("a return path, packed before departure"; revert is governed too); the chain as workflow exhaust
  ("the audit is not something the team prepares; the system already contains it"); the two clocks with the
  retroactive-circular case; Part II assembled (graph → cascade → gate → chain; five properties by
  construction, author-blind) — handoff to Part III.

## Figures

- **New diagrams:** tree-vs-graph (emoji-free redraw), gate-pipeline (stage questions under each box),
  undo-timeline (stored inverses + one orange revert arc), two-clocks (world clock vs system clock, the
  July-circular-effective-April case).
- **New IDE panels:** ide-graph-facet (graph canvas + inspector, "Refine this point…"), ide-verdict (the
  rfn-0207 card, four green stages, revert within reach). Both captioned as illustrations, not screenshots.
- **New CLI panels (figpanels.py):** cli-lift, cli-verdict-pass, cli-verdict-refuse (the four-part refusal
  grammar rendered), cli-cascade (depths + early cutoff), cli-history-why (biography + narrated verdict +
  the as-of line that plants the two clocks).
- **Legacy embeds:** `FIG_LEGACY` mapping in build.py reuses complete figure blocks from figures.py —
  `cascade-interactive` (the animated ripple; verified: click lights 14 nodes + counter) and
  `ide-cascade-facet`.

## Canon fix

figures.py carried stale penalty-cap numbers (0.20 → 0.16, "BCEAO 4.5 · cap 20→16%") inconsistent with the
book canon (Listing 2.1: 18 → 16 under BCEAO-4.2). Fixed in figures.py; both editions now agree; manifesto
edition rebuilt with the correction.

## Verification

Teaching build idempotent (201,656 bytes twice, 20 pages), substrate-clean. In the reader: all four chapters
with correct §-headings and figure counts (3/4/3/3), 18 figures total in the book, interactive cascade
animates, panels render with the early-cutoff line. Register: 19 of 27 figures placed. Ledger updated.

## Next

**Phase 3** on the author's go: Part III (Ch 8 Agents demystified · Ch 9 The safest write surface · Ch 10
The jungle revisited) + the agent-ladder, two-agent-kinds, trust-postures diagrams, the wise-coding panel,
the Live Mode IDE panel, and the signature jungle-map-after spread.
