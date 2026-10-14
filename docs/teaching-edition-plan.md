# The Teaching Edition — master refactoring plan

**Project:** *Refinement-Oriented Programming* — second edition of the book, superseding the manifesto edition
**Imprint:** AYOUNI · Tunis · Niamey · Paris · 2026
**Status:** Plan approved 2026-07-18 (author decisions recorded in §2). Phases 0–6 pending execution.
**Supersedes:** the manifesto edition as the published book (the manifesto manuscript remains in git history; the documentary "discipline" project in `manuscript/01-what-broke/` is a separate, on-hold project and is not touched by this program).

---

## 1. The directive (author, 2026-07-18)

Refine is a **commercial product built on an open-source foundation: the Softanza Engine and Library**. The book must be refactored so that:

1. **The narration is neutral with respect to the commercial product.** The paradigm is taught on the open-source Softanza foundation, illustrated through an `stz <command>` CLI experience. Refine (the product) is cited and illustrated essentially for its **visual IDE facets**, where a visual clarifies the narration.
2. **The book takes a stronger didactic approach to simplifying the jungle of current AI** — and positions Refinement-Oriented Programming as the gate that resolves that jungle in a fundamental and practical way.
3. **The style competes with the best simplifying, visually-illustrating authors** at the best-known publishers — and aims to do better: a memorable reading experience for everyone, not only technical programmers.
4. **Illustrations are carefully designed SVGs** shipped alongside the markdown: CLI snapshots, IDE snapshots, and well-thought diagrams.
5. **The writing copes with modern time constraints** — coherent, concise, respectful of readers who do not have a lot of time.
6. **A PDF edition is generated to world-class press standards** — cover (the giraffe; it represents Niger), back cover, and the full standard layout apparatus of a quality press.
7. **AYOUNI** is the press house for this and all upcoming books (the author's first book was with Apress: *Beginning Ring Programming*).

## 2. Author decisions (recorded 2026-07-18)

| Decision | Choice |
|---|---|
| Refactor depth | **Rebuild lean** — a new, tighter edition built *from* the manifesto's proven material, restructured around the didactic mission |
| Voice | **Teaching voice** — second-person didactic ("you type `stz cascade`, and this is what comes back"); the manifesto's first-person conviction survives in short chapter-opening passages |
| Length | **~40,000 words** — 200–240 pages at 6×9, chapters of 2,500–3,500 words each readable in one sitting, heavy illustration density |
| Web edition | **Replaces** the manifesto edition at ayouni.press — web reader and PDF generate from the same new manuscript |

## 3. Source-material policy (what the book is grounded in)

The book invents nothing. Every claim, mechanism, and illustration traces to one of:

- **The manifesto manuscript** (`git` history of `manuscript/rop-manifesto.md`) — the argument, the Sonibank scenes, the honest-boundaries discipline, the glossary pins. This is the quarry the new edition is cut from.
- **The Softanza intelligence architecture** (`stzlib/libraries/stzlib/base/doc/design/SOFTANZA_INTELLIGENCE_ARCHITECTURE.md`) — the open foundation's truths: the six laws; graph-primary knowledge; the `refine/` module (typed refinement points in 8 kinds, the 4-stage gate composed from graph rules, the cascade as `ImpactOf`, the reversibility timeline, trust postures); the Uter ladder (pattern → Regexuter → Softanzuter → agent); pi-agents vs LLM agents ("the mind is programmatic by default; an LLM is a pluggable faculty"); wise coding vs vibe coding; governance primitives G1–G10; "derivation replaces RAG"; the polyglot ruling ("the language is the authority in its own gate"); the platform-vs-product boundary.
- **The Refine corpus** (`refine/specs/`, `refine/prototype/`) — for the IDE facet illustrations and the concepts the product contributed (cascade-as-review-surface, the audit chain's two clocks, the experience dial), always presented through the neutral lens of §4.
- **The Sonibank grounding** (Amina, BCEAO, WAEMU) — retained as the running human thread; it is what keeps the book readable by non-programmers.

## 4. The naming and honesty contract

1. **Softanza is the open-source foundation** — the Engine (Zig, programming-language-agnostic) plus the Library. The book teaches on it. Free, local, no paid or remote dependency (Law 2 of the foundation).
2. **Refine is a commercial product built on that foundation** (author statement, 2026-07-18). The book says exactly this, cites it as *one* product, and shows its IDE facets where a visual teaches better than prose. Framing sentence pattern: *"Commercial tooling built on this foundation — Refine is one — renders this as …"* No license is named for either side; no pricing, no availability claims.
3. **The `stz` CLI sessions are illustrative.** One front-matter note (in "How to read this book") states plainly: the sessions show the open foundation's real machinery (points, gate, cascade, revert, why) in an idealized command form; exact command names and flags may differ as the tooling ships. After that note, sessions are presented cleanly with no per-figure hedging. Every session maps to machinery named in the architecture document — nothing is shown that the foundation does not describe.
4. **The standing hard rules hold:** never the word "substrate"; no invented metrics, benchmarks, endorsements, or dates; no yellow in the design system; body prose monochrome with color only inside figures; honest boundaries close the book; no emojis in book prose.

## 5. The `stz` illustration idiom (the running thread)

One session vocabulary, used consistently, always mapped to the foundation's named machinery:

```
stz lift pricing.py          # the lift: the code enters the graph (the language's
                             #   own parser is the authority — ast for Python)
stz points                   # the declared, typed change surface (8 kinds)
stz explain vat_rate         # kind, bounds, current value, lineage
stz refine vat_rate --to 0.20   # a TYPED PROPOSAL — not a diff
stz cascade                  # the blast radius, computed BEFORE anything lands
stz apply                    # the gate: structural → constraint → derivation
                             #   → governance; verdict with Why
stz revert                   # the typed inverse; the undo timeline
stz history                  # the audit chain; stz why <id> narrates any verdict
stz ask "raise the VAT rate to 20 percent"   # the natural door, same gate
```

Conventions: dark warm terminal panels (consistent with the reader's code-listing style); the prompt is `❯`; verdicts show the four gate stages with pass/refuse states; every refusal demonstrates the four-part grammar (what happened · why · what to do next · where to learn more). Agents appear in the same idiom (`stz agent …`) when Part III needs them — and the point is always the same: **the gate does not care who authored the proposal.**

## 6. Structure — 13 chapters in four parts (~40k words)

Every chapter: a one-line promise under the title → teach by showing (a scene, a session, or a diagram before any definition) → short numbered sections → a "What you now know" close (3–5 bullets, the honest not-established line kept where it matters). Sonibank appears in every chapter, even briefly.

**Front matter** — half-title · title · copyright · dedication · epigraph · contents · **How to read this book** (the promise, the map, the `stz` note, the 90-minute path) — ~1,200 words

**Part I — The jungle, and the way out**
1. **The jungle** — the AI landscape in one map (agents, harnesses, memory, RAG, skills, MCP, "governance"); why every word means three things; the one question under all of it: *can you trust what just changed?* — ~2,800 w · Fig: the jungle map (before)
2. **What broke** — writing stopped being the bottleneck; trusting became it; the Q3 letter lands on Amina's desk — ~2,600 w · Fig: the bottleneck moved
3. **The unit changed** — line → diff → **refinement**; the first full `stz` session, lift to apply — ~3,200 w · Figs: unit-changed diagram + 2 CLI panels

**Part II — The discipline** *(one mechanism per chapter)*
4. **The graph** — the codebase as a typed graph; `satisfies` edges; what the lift does — ~3,000 w · Figs: tree-vs-graph + CLI panel + IDE panel (graph facet)
5. **The gate** — four stages; verdicts that explain themselves; refusal as a feature — ~3,200 w · Figs: gate pipeline + verdict CLI panels (one landing, one refusing) + IDE panel (verdict)
6. **The cascade** — the blast radius you read *instead of* the diff; early cutoff — ~3,000 w · Figs: cascade diagram (interactive on web) + CLI panel + IDE panel (cascade facet)
7. **Reversibility and the audit chain** — the typed inverse; the two clocks; what the auditor asks — ~3,000 w · Figs: timeline + two-clocks + CLI panel (history/why)

**Part III — Agents in a governed world**
8. **Agents, demystified** — the industry loop is one special case; the ladder from pattern to agent; the mind is programmatic by default, an LLM is a pluggable faculty — ~3,200 w · Fig: the ladder + the two agent kinds
9. **The safest write surface** — typed proposals against declared knobs; trust postures; wise coding asks, vibe coding guesses — ~3,000 w · Figs: trust postures + wise-coding exchange CLI panel + IDE panel (Live Mode)
10. **The jungle, revisited** — every word from Chapter 1 gets its governed answer (memory → governed graph; RAG → derivation with provenance; skills → verified capabilities; harness → where agents run, not where change is governed); the map redrawn, legible — ~3,000 w · Fig: the jungle map (after) — the book's signature spread

**Part IV — The bigger picture**
11. **One gate, many worlds** — refinement is universal: code, UI, data; knowledge, models, plans; any language ("the language is the authority in its own gate") — ~2,800 w · Figs: cross-domain cascade + polyglot loop
12. **In the boardroom** — regulation now assesses what you can *prove*; the audit chain as the evidence backbone; the auditor's visit at Sonibank — ~2,600 w · Fig: IDE panel (audit chain / export)
13. **Honest boundaries** — what this is not; valid is not wise; the bet, stated plainly — ~2,400 w

**Coda** — the next letter (Amina, briefly) — ~400 w
**End matter** — the glossary, pinned (carried from the manifesto, updated to the neutral naming) · acknowledgements

Total: ~39,400 words + apparatus. The 90-minute path: Ch 1, 3, 5, 6, 10, 13.

## 7. The illustration program (all SVG, checked in beside the markdown)

Three figure families, one visual system (per `docs/design-system.md`: monochrome body, color only inside figures, no yellow, Inter for labels/numbers):

- **CLI panels** (~10): generated from a spec (command + output lines + verdict states) by a small Python helper (`web/figpanels.py`) so every terminal panel is identical in geometry, palette, and typography. Dark warm background matching the reader's code listings; pass/refuse states in the established green/red.
- **Diagrams** (~10): the jungle map before/after (the signature pair), the bottleneck, unit-changed, tree-vs-graph, gate pipeline, cascade (interactive on web, static in PDF), timeline + two clocks, the agent ladder, trust postures, cross-domain. Six existing SVGs in `web/figures.py` are adapted where they fit; the rest drawn new in the same hand.
- **IDE panels** (~6): clean SVG *redraws* of Refine facets (graph, verdict, cascade, Live Mode, audit export) — never raster screenshots — each captioned "An illustration of the Refine IDE's … facet" so the product's role is visible and honest.

All figures live in `assets/illustrations/` (source of truth) and are injected into the web reader by slug via `web/figures.py`; the PDF uses the same files. Every figure has a caption that teaches on its own (a reader flipping only through figures should still get the argument).

## 8. The pipeline (one manuscript, two editions)

- **Manuscript:** one markdown file, `manuscript/rop-book.md` (same single-file convention the proven build reads); front matter as structured sections.
- **Web:** `web/build.py` retargeted to the new manuscript; the existing reader shell (search, highlights, sidebar, font control, part pages) is reused as-is — it was hardened this month and carries over unchanged.
- **PDF:** a `--pdf` mode added to the build: emits a print-composed HTML (6×9 in trim, EB Garamond body ~10.5–11pt, running heads, folios, chapter openers on recto, front matter sequence, widow/orphan control via print CSS) and drives headless Chrome to `book.pdf`. Cover page composited from `web/cover.png` (the giraffe — a Sahel animal; it represents Niger; the patchwork coat echoes the graph of refinements); **back cover** designed new: blurb (~120 words), three reader-benefit lines, AYOUNI wordmark, cities line, ISBN placeholder box. Print QA checklist: no orphan headings, figures never split, TOC page numbers real, 0 "substrate", monochrome body.

## 9. Phases (execute in order; one per ask, as with the editorial program)

- **Phase 0 — Infrastructure.** `manuscript/rop-book.md` skeleton (front matter + 13 chapter stubs with promises); `web/figpanels.py` (CLI-panel generator) + the figure register (every figure: slug, family, status); build.py retargeting behind a flag so the manifesto edition stays live until Phase 5 flips it.
- **Phase 1 — Part I** (Ch 1–3) drafted with all figures. The jungle map and the first `stz` session are the proof of the whole concept — reviewed by the author before Phase 2.
- **Phase 2 — Part II** (Ch 4–7) + IDE panels begin.
- **Phase 3 — Part III** (Ch 8–10) + the jungle-map-after spread.
- **Phase 4 — Part IV** (Ch 11–13) + coda + glossary carry-over.
- **Phase 5 — Integration.** Full-book coherence pass (voice, terms, cross-references, figure captions); web edition flipped to the new manuscript; verification in the reader (desktop + mobile, search, figures).
- **Phase 6 — The PDF edition.** Print pipeline, cover + back cover, front-matter sequence, print QA; `book.pdf` shipped; session log + CLAUDE.md brought current.

## 10. Status ledger

| Phase | Content | Status |
|---|---|---|
| 0 | Infrastructure: manuscript skeleton · CLI-panel generator · figure register · build flag | **DONE 2026-07-18** — `manuscript/rop-book.md` (20 pages: start-here + 4 parts + 13 chapters + coda + glossary, promises + phase-tagged stubs); `web/figpanels.py` (spec-driven SVG terminal panels, one geometry/palette; demo `cli-first-session` drawn and verified in browser: 17 lines, 6 palette colors, clean parse); `docs/figure-register.md` (27 figures tracked); `build.py --teaching` → `web/teaching.html` (subtitle "A discipline…"; idempotent; substrate-clean; manifesto build byte-identical to before) |
| 1 | Part I (Ch 1–3) + figures — author reviews before Phase 2 | **DONE 2026-07-18** — "How to read this book" (537 w) + Ch 1 The jungle (1,663 w) + Ch 2 What broke (1,390 w) + Ch 3 The unit changed (1,775 w), full teaching voice; 5 figures drawn+placed (jungle-map-before, bottleneck-moved, unit-changed, cli-first-session, cli-explain); `{{fig:slug\|caption}}` directive added to build.py; verified in reader (headings, figures, captions, 6-color panels). Chapters run tighter than the plan's per-chapter targets (~60%) — flagged for the author's Part-I review: accept the tighter density (book lands ~30k) or deepen in integration |
| 2 | Part II (Ch 4–7) + IDE panels begin | **DONE 2026-07-18** — Ch 4 The graph (1,319 w) · Ch 5 The gate (1,350 w) · Ch 6 The cascade (1,152 w) · Ch 7 Reversibility and the audit chain (1,242 w); 13 figures placed (tree-vs-graph, cli-lift, ide-graph-facet, gate-pipeline, cli-verdict-pass, cli-verdict-refuse, ide-verdict, cascade-interactive [reused from web edition, animates], cli-cascade, ide-cascade-facet [reused], undo-timeline, two-clocks, cli-history-why); FIG_LEGACY embed mapping added to build.py; figures.py penalty-cap numbers aligned to canon (18 → 16, BCEAO-4.2) fixing a pre-existing manifesto inconsistency; 19 of 27 register figures placed |
| 3 | Part III (Ch 8–10) + jungle-map-after spread | **DONE 2026-07-18** — Ch 8 Agents, demystified (1,385 w) · Ch 9 The safest write surface (1,388 w) · Ch 10 The jungle, revisited (1,253 w); 6 figures placed (agent-ladder, two-agent-kinds, trust-postures, cli-wise-coding, ide-live-mode, **jungle-map-after** — the signature spread, 14 boxes around the governed center); 25 of 27 register figures placed; 24 figures in the built book |
| 4 | Part IV (Ch 11–13) + coda + glossary | **DONE 2026-07-18** — Ch 11 One gate, many worlds (960 w) · Ch 12 In the boardroom (988 w, the auditor's visit + "The institution was able to produce…") · Ch 13 Honest boundaries (984 w, five limits + Monday-morning five lines + the book's final established/not-established ledger) · Coda The next letter (136 w) · glossary (801 w, 28 pinned terms incl. Softanza/Refine/stz); last 3 figures placed (cross-domain-cascade, polyglot-loop, ide-audit-export) — **register 27/27**; manuscript complete at ~17.3k words, 27 figures, zero stub markers. NOTE for Phase 5: total is well under the 40k plan target — the tight density carried through; the author decides in integration whether to deepen or embrace the compact form |
| 5 | Integration: coherence pass, web edition flipped, verification | **DONE 2026-07-18** — coherence audit clean (all Chapter-N cross-refs resolve; 12 "What you now know" closes + Ch 13's final ledger; canon numbers consistent; no doubled words); **build flipped**: default `build.py` → rop-book.md → index.html ("A discipline…"); `--manifesto` flag rebuilds the superseded edition from its retained manuscript (repo not under git → the file is the record; deletion rule waived deliberately); web/teaching.html removed; verified live: 20 pages, 27 figures, cover, part labels, search over new content ("wise coding" → 7 hits), mobile 375px (no overflow, drawer, left-aligned) and desktop. The compact ~17.3k form is embraced (author proceeded without deepening) |
| 6 | The PDF edition: print pipeline, cover + back, QA | **DONE 2026-07-18** — `web/print.py`: composes the manuscript into 6×9in print HTML (front-matter sequence: half-title · title · copyright · dedication · epigraph · TOC with **real page numbers** via paged.js target-counter; running heads via string-set; folios; blank versos clean; widow/orphan control; figures break-inside avoid; cascade shown fully lit in print) and drives Chrome over the **DevTools protocol** (waits for paged.js to finish — the CLI --virtual-time-budget path proved unreliable under new headless) → **`web/book.pdf`: 106 pages, exactly 6×9in, substrate-clean**. Cover: the author's final flat giraffe artwork **as-is** (installed as web/cover.png + site/cover.png; hand-held mockup archived to assets/covers/archive/); the author's tagline *"Stop trying to govern the intelligence, and govern the change."* set in orange italic on the **back cover** (the composed front cover was dropped at the author's instruction). New back cover: blurb + tagline + three reader lines + author line + AYOUNI wordmark + ISBN-pending box. Bug fixed at source in build.py `inline()`: asterisks inside code spans (`policy/*`) no longer corrupt italic pairing (affected both editions; web rebuilt). **THE PROGRAM IS COMPLETE — phases 0–6 all done.** |

## 11. Honest boundaries of this plan

- The `stz` CLI does not ship today; the book says so once, plainly, and never pretends otherwise. Sessions are faithful to the architecture document's named machinery and to nothing else.
- The word-count and page targets are working targets, not promises; the PDF trim and typography will be tuned against real page proofs in Phase 6.
- The manifesto edition's deeper treatments (the full competitive collisions, the enterprise governance chapter, the two-answers essay) are *compressed or cut* in a 40k book; they remain in the manifesto manuscript in git history and in the Refine specs corpus. Cutting them is a feature of this edition, not a loss to the record.
- The documentary project (Amina book, `manuscript/01-what-broke/`) is untouched and remains on hold.
- Whether a French edition follows is not decided here.
