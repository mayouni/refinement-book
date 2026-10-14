# Session — 2026-07-18 · Teaching Edition Phase 1: Part I drafted

Phase 1 of `docs/teaching-edition-plan.md` executed — Part I written in full, with all five figures.

## Prose (manuscript/rop-book.md)

- **Start here — How to read this book** (537 w): the promise, the two audiences, the `stz` honesty note
  (open Softanza foundation; idealized command rendering; Refine cited as one commercial product whose screens
  illustrate), the four-part map, the 90-minute path (1, 3, 5, 6, 10, 13), the honesty pledge.
- **Ch 1 — The jungle** (1,663 w): opens on the vendor pitch at Sonibank and Amina's unanswered question
  ("who checked that change, against which rule, and how do I undo it?"); §1 the ten words with three meanings
  each (governance's three objects — model/actor/change — as the worst case); §2 why the jungle grew (the field
  outran its language — no villain); §3 the map walked (arrows are folklore); §4 the question underneath (every
  box answers a fragment about the model/actor/pipeline; nothing governs the change itself); §5 the way out
  previewed (govern the change; not an AI tool; free; small). Close + honest not-shown line.
- **Ch 2 — What broke** (1,390 w): the Q3 letter scene (BCEAO, penalty cap 18 → 16, ninety days, the notebook
  list); §1 what was new (the afternoon draft); §2 the symmetry broke (approval decouples from understanding —
  "the signature certifies less and less"); §3 the instruments assume a vanished world (diff/PR/meeting/VCS);
  §4 trust as five checkable properties of the change (validated · scoped · attributed · reversible ·
  explainable) — "the list never mentions the author."
- **Ch 3 — The unit changed** (1,775 w): line → diff → refinement; the definition (typed, declared point);
  refinement points ("a system that knows its own knobs"); the first session walked command by command
  (lift → points → explain → refine → cascade → apply, four gate stages); §5 the payoff — the five properties
  produced in ninety seconds, and "the gate examines proposals, not authors"; expression is free, admission is
  governed. Close + roadmap into Part II.

## Figures (all drawn + placed)

- `jungle-map-before.svg` — 10 term boxes each carrying its three contested meanings, crossing dashed arrows
  labeled "contains? replaces? same thing?", the orange question line beneath. The signature opener (pairs with
  Ch 10's jungle-map-after).
- `bottleneck-moved.svg` — THEN (one change, a comfortable reviewer, green "read, understood, approved") vs
  NOW (six machine-speed changes funneling orange into the same reviewer; "approved… unread?").
- `unit-changed.svg` — the diff vs the refinement card (adapted from the web edition's ch2 figure; values
  aligned to canon: 18 → 16).
- `cli-explain` — new figpanels.py panel (the point's biography: kind/value/bounds/policy/history/cascade).
- `cli-first-session` — already drawn in Phase 0, now placed.

## Infrastructure

- **`{{fig:slug|caption}}` directive** added to build.py's converter: cli-* slugs render live from figpanels.py;
  other slugs inline `assets/illustrations/diagrams/<slug>.svg`; caption becomes a "Fig." figcaption.
- Lesson: in this converter body `##` → h3.subsection-h and `###` → h4 — section headings in the manuscript use
  `## §N — Title` (safe: only Preface/Start here/About/Appendix `##` forms are page boundaries).

## Verification

Built twice — byte-identical (131,262 bytes, 20 pages), substrate-clean; manifesto build untouched. In the
reader (cache-busted): all six §-headings per chapter render at 17.6px; five figures render with captions;
the terminal panel shows all six palette colors; no oversized SVGs. Browser screenshot capture still stuck
(the known renderer hiccup) — DOM verification used throughout.

## For the author's Part-I review (the Phase-2 gate)

1. The **voice and density**: chapters run ~60% of the plan's per-chapter word targets — complete arguments,
   tightly told. Accept the tighter density (whole book lands ~30k words) or ask for deepening.
2. The **jungle map** and **first session** — the two proof-of-concept artifacts this phase was gated on.
3. The Ch 1 opening scene (the vendor pitch) — invented for this edition (consistent with the documentary
   grounding sheet, but new); confirm Amina may carry it.

Next: **Phase 2** (Ch 4–7, the four mechanisms, + first IDE panels) on the author's go.
