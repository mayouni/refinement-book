# CLAUDE.md — Refinement-Oriented Programming

> **Location (2026-10-08):** this book now lives at `ayouni/books/refinement-book/`, the first of the AYOUNI
> books. The second, *Softanza*, is at `ayouni/books/softanza-book/`. All paths below are relative to this folder.

> **The rewrite (2026-10-15, HOUSE-13):** this book is now the second of the AYOUNI books and is being rewritten radically; the author's
> rulings for the rewrite are in `DECISIONS.md` and override this file where they conflict. ROP-01: the bank is renamed **Softibank**, a
> fictional name; "Sonibank" below is the old name, kept until the rewrite replaces this file.

**Read this first.** This file is the durable working memory for the AYOUNI book project. Any new Claude Chat session that opens this repo should treat this document as authoritative for project context, locked decisions, hard constraints, and current state. It supersedes Claude's prior assumptions where they conflict.

---

## Project identity

**Book:** Refinement-Oriented Programming
**Subtitle:** A discipline for software in the agentic era
**Author:** Mansour Ayouni
**Imprint:** AYOUNI (independent imprint of Mansour Ayouni / Softanza Labs)
**Cities:** Tunis · Niamey · Paris · 2026
**Domain:** ayouni.press
**Manuscript version:** 0.1 (Chapter 1 drafted, preview edition shipped)
**ISBN:** pending

---

## What this book is

A practitioner's account of a discipline developed at a small commercial bank in Niamey to govern software change at agent throughput, in a regulated francophone West African banking context. The discipline is **Refinement-Oriented Programming**. Its production case is **Sonibank Niger** under BCEAO supervision in the WAEMU monetary zone.

This is **not** a tools book. It is a book about how a small team in the Global South arrived at review and governance practices the broader software industry is starting to recognize it needs. It is grounded — concrete bank, concrete regulator, concrete characters — and the narrative thread runs through eighteen months between Amina Bello receiving a Q3 letter from BCEAO and an auditor's visit eighteen months later confirming the discipline held.

The book has its own thesis ("when writing is no longer the bottleneck, review and governance become the design problem of the era") but its register is documentary, not polemical. It is the story of one bank's discipline, told carefully enough that the lesson generalizes.

---

## Hard constraints

These are decisions already made. Do not relitigate them. If a new instruction conflicts with one of these, ask before acting.

1. **All reference documents are Markdown (.md) only.** Never produce .docx for any spec, report, guide, or note. The manuscript itself is Markdown.
2. **Never use the word "substrate"** anywhere — in manuscript, docs, design notes, anything. Use *runtime*, *engine*, *graph model*, *system*, or another context-appropriate alternative.
3. **No yellow colors** anywhere in the design system. If a warm-light family is needed, use sand, olive, or warm beige.
4. **Body text is monochrome (black only).** Color is permitted only on (a) the cover image and (b) inside figure illustrations, where color may carry semantic meaning (e.g., the cascade diagram in Fig. 1.2).
5. **AYOUNI wordmark in the manuscript and reader interior is solid black**, set in Archivo Black with a floating dot above the I (CSS pseudo-element in HTML; manual circle in SVG). The cover image uses its own wordmark treatment (currently green-to-red gradient baked into `cover.png`) — do not try to replicate that gradient elsewhere in the book.
6. **Cover stroke belongs to the cover.png file**, never to CSS. Do not add a CSS border around `.cover-img`.
7. **Default body font size on screen: 22px EB Garamond.** Reader can adjust 18px–30px in 7 steps.
8. **The HTML book is a single self-contained file** (`web/index.html`) plus `web/cover.png`. No build step. Deployment is uploading two files to ayouni.press.
9. **Versioning discipline.** When a document supersedes another, delete the predecessor. No `_old`, `_backup`, `_v1`, `_v2` files lying around in the repo. Git history is the record.
10. **Honest boundaries.** Every spec ends with what is known, what is not yet known, and what is deliberately out of scope. Never invent metrics, prices, benchmarks, publication dates, sales numbers, or institutional endorsements.
11. **No emojis in the manuscript.** Emojis are fine in casual chat with the user but never appear in book prose, chapter titles, asides, or figure captions.
12. **Numerical indicators (counts, statistics, totals) are set in sans-serif (Inter), never in the display serif.** Carryover from the Refine design system; preserved here for consistency across Mansour's projects.

---

## Publishing model

**Free first, print second.** The book is released under CC BY-NC-ND 4.0 (text) and CC BY-NC-SA 4.0 (illustrations); code listings under MIT. The free digital edition (PDF + ePub) is the primary distribution. Print editions are offered through IngramSpark POD as a secondary channel for readers who want a physical copy.

**No advance, no publisher, no agent.** AYOUNI is Mansour's independent imprint. The book funds itself through optional pay-what-you-want PDFs and the modest print margin.

**Distribution channels (in priority order):**
1. ayouni.press — the book's home, hosting the HTML reader and free PDF/ePub downloads
2. IngramSpark — print-on-demand worldwide
3. (Future) ePub direct download
4. (Future) Audiobook — undecided; not pursuing actively

**Audience priority order:**
1. Programmers in regulated industries, especially francophone West African banking
2. Compliance officers, regulators, auditors in WAEMU / BCEAO and adjacent contexts
3. Software engineering practitioners broadly, especially those working at the new agent-driven throughput
4. Industry observers and theorists (last priority — write the book the practitioners need; the theorists can pick it up if they want to)

---

## Voice and register

**Documentary, not polemical.** The argument is in the events. Amina receives a letter. The team confronts it. A discipline emerges. The reader concludes.

**Calm, never breathless.** No "revolutionary," no "game-changing," no "paradigm shift." The book reports what worked. The reader decides what to do with it.

**Grounded.** Every abstract claim has a concrete instance in the Sonibank narrative. If a claim cannot be grounded, it is reconsidered.

**Plain.** Sentences are short by default. Long sentences earn their length. Jargon is defined the first time it appears (in an aside if needed) and used consistently thereafter.

**Honest about scope.** The book is about one bank, one regulator, one team, one discipline. Generalization happens carefully and is flagged. The book does not claim the discipline applies universally; it claims the discipline worked at Sonibank Niger and is worth examining.

---

## Characters and grounding

See `docs/characters-and-grounding.md` for the full sheet. Quick reference:

- **Amina Bello.** Mid-career, the bank's IT methodologist. The narrative's centre of gravity. She is the one who receives the Q3 letter on a Tuesday in September. She is competent, calm, careful, francophone (Nigerien Hausa background, university in Dakar, returned to Niamey to work). She is not an exceptional engineer; she is a working professional whose job became different around her, and who responded by changing how the work was done.
- **Sonibank Niger.** A small/medium commercial bank in Niamey. Real bank, real regulatory context. The book treats it with documentary respect — no caricature, no hagiography. Sonibank is not Apple. It is a careful organization in a regulated context that built something good.
- **BCEAO.** Banque Centrale des États de l'Afrique de l'Ouest. The Central Bank of West African States. Real institution. Headquartered in Dakar. Issues directives that ripple through every commercial bank in the eight WAEMU member states.
- **WAEMU.** West African Economic and Monetary Union. Eight member states (Benin, Burkina Faso, Côte d'Ivoire, Guinea-Bissau, Mali, Niger, Senegal, Togo) sharing the CFA franc.
- **The methodologist.** Mansour's stand-in within the narrative. Appears sparingly. Is never named in the book — referred to as "the methodologist" or by role. His role is to ask the right questions; the work belongs to the team.
- **The auditor.** Visits at month 18. The book's final perspective check. What does the auditor see? If the auditor's report is clean, the discipline held.

---

## Current state — what's drafted

**Chapter 1 — What broke** (Part One: The diagnosis)
- §1.1 The Q3 letter (~712 words) — DRAFTED
- §1.2 What was new (~284 words) — DRAFTED
- §1.3 The symmetry broke (~621 words) — DRAFTED
- §1.4 What this chapter does (~278 words) — DRAFTED
- Fig. 1.1: BCEAO directive letter on desk (SVG, full color)
- Fig. 1.2: Cascade diagram, 14 affected products radiating from `penalty_cap` (SVG, full color)
- Four asides: WAEMU, Cascade, The text diff, How to read

**Front matter:**
- Dedication
- Epigraph
- Copyright
- Contents (full 15-chapter TOC visible)

**End matter:**
- "End of preview" closing note

**Web reader:**
- `web/index.html` — single-file HTML book in 37signals Writebook-inspired format: overview page with chapter cards, chapter pages with sidebar TOC, hash-based routing, font size control, print stylesheet
- `web/cover.png` — current cover artwork (giraffe with patchwork coat)

> **THE TEACHING EDITION (2026-07-18) — the active program.** The author directed a full refactoring of the book:
> narration made **neutral from the commercial product** by teaching on the **open-source Softanza foundation**
> (Engine + Library; author statement: *"Refine is a commercial product based on an open source foundation: the
> Softanza Engine and Library"*), illustrated through an **`stz <command>` CLI idiom** (illustrative sessions,
> flagged once in front matter, faithful to `stzlib/.../design/SOFTANZA_INTELLIGENCE_ARCHITECTURE.md` — esp. §5.8
> refine module, §5.6 Uter ladder, §5.7 governance, §0.3 wise coding); Refine cited for its **visual IDE facets**
> only (SVG redraws, never raster). Stronger didactic mission (simplify the AI jungle; ROP as the gate through it);
> world-class simplifying style for everyone; all-SVG illustration program (CLI panels + IDE panels + diagrams);
> concise modern prose; **PDF edition to press standards** (giraffe cover — represents Niger — + new back cover).
> **Author decisions locked:** rebuild lean (13 chapters, 4 parts), teaching voice (second person), ~40k words,
> **replaces** the manifesto edition on the web (same manuscript feeds web + PDF). Master plan:
> `docs/teaching-edition-plan.md` (phases 0–6; execute one per ask).
>
> **PHASE 5 FLIPPED THE BUILD (2026-07-18): the Teaching Edition IS the book.** `python web/build.py` reads
> `manuscript/rop-book.md` → `web/index.html` (subtitle "A discipline for software in the agentic era";
> 20 pages: Start here · 4 parts · 13 chapters · coda · glossary; ~17.3k words — the author embraced the
> compact density; 27 SVG figures, all placed, per `docs/figure-register.md`; CLI panels generate from
> `web/figpanels.py`, diagrams live in `assets/illustrations/diagrams/`, two figures embed from `figures.py`
> via FIG_LEGACY). The manifesto edition is **superseded but retained**: this repo is NOT under git, so
> `manuscript/rop-manifesto.md` stays on disk as the record, rebuildable any time via
> `python web/build.py --manifesto` → `web/manifesto.html` (not a deployment artifact).
>
> **PHASE 6 SHIPPED THE PDF (2026-07-18) — THE PROGRAM IS COMPLETE.** `python web/print.py` composes the
> manuscript into 6×9in print HTML (full front-matter sequence, running heads, folios, TOC with real page
> numbers via paged.js) and drives Chrome over the DevTools protocol (waiting for pagination to finish —
> do NOT use --virtual-time-budget, it is unreliable under new headless) → **`web/book.pdf`, 106 pages**.
> The cover is the author's final flat giraffe artwork, used AS-IS (installed 2026-07-18 as web/cover.png +
> site/cover.png; the hand-held mockup archived in assets/covers/archive/). The author's tagline — *"Stop
> trying to govern the intelligence, and govern the change."* — appears on the BACK cover (orange italic in
> the blurb); the front cover carries no overlay by the author's instruction. Deployment artifacts:
> `web/index.html` + `web/cover.png` + `web/book.pdf`. Requires network at PDF-build time (fonts + paged.js
> CDN) and the `websocket-client` pip package.

> **Web-edition decision (2026-06-22).** At the author's explicit instruction, `web/index.html` now hosts the
> **full manifesto edition** — the complete book (18 chapters in five parts, since the July 2026 editorial restructure recorded in `refine/specs/ROP_MANIFESTO_EDITORIAL_PLAN_v0_1.md`) in the first-person *manifesto* voice (subtitle
> "A manifesto for software in the agentic era"), sourced from `manuscript/rop-manifesto.md` and **generated** by
> `web/build.py` (+ `web/figures.py`, `web/shell.template.html`). It carries a "Start here" reader's on-ramp, a
> concept-glossary appendix, per-chapter signposts, uniform "established / not established" chapter closes, Sonibank scenes in every chapter, figure callouts and code listings, five part-divider pages, and explanatory diagrams (incl. one interactive cascade).
> This deliberately supersedes the earlier documentary Chapter-1 *preview* on the web surface. The documentary
> "discipline" treatment (this CLAUDE.md's voice/register, the `manuscript/01-what-broke/` sections) remains the
> repo's separate prose project — do **not** revert the web reader to the preview, and do **not** rewrite the
> manifesto into documentary voice, without a fresh instruction. To refresh the web edition: edit the manifesto
> source and run `python web/build.py`. The two hard constraints still hold in the generated output (verified:
> 0 "substrate"; body prose monochrome with color only inside figures).

---

## What's next — priority order

1. **Chapter 2: The unit changed** — the text-diff problem in depth, what replaces it. Draft expected.
2. **Chapter 10: Sonibank Niger** — write the production case early. It grounds every later chapter; the discipline chapters (4–9) reference it.
3. **Chapter 11: Amina's refinement** — the narrative payoff. Should be drafted before Chapter 12 (auditor's visit) since they are continuous.
4. **Chapter 3: The codebase as a graph** — completes Part One.
5. **Chapters 4–6: The discipline** (Part Two).
6. **Chapters 7–9: The system** (Part Three).
7. **Chapter 12: What the auditor sees** — the case's closing chapter.
8. **Chapters 13–15: The implications** (Part Five).
9. **Prologue** — written last (Mansour's strong preference, as in his other work).
10. **Epilogue** — written last.

Writing order is not reading order. The book reads linearly; drafting can proceed in whichever sequence the material is ready.

---

## Repo layout

```
ayouni-rop/
├── CLAUDE.md                  ← this file, read first
├── README.md                  ← quick-start and orientation
├── BOOK.md                    ← master manuscript outline (canonical TOC)
├── LICENSE.md                 ← license terms in full
├── .gitignore
│
├── manuscript/                ← source-of-truth: book content in Markdown
│   ├── 00-front-matter/
│   ├── 01-what-broke/         ← Chapter 1 (drafted)
│   ├── 02-unit-changed/       ← (not yet created)
│   ├── ...
│   └── 99-end-matter/
│
├── web/                       ← the HTML reader
│   ├── index.html             ← single-file reader (current preview)
│   ├── cover.png              ← cover artwork (replaced by Mansour with new files as needed)
│   └── README.md              ← deployment notes
│
├── docs/                      ← design system, style guide, plans
│   ├── design-system.md
│   ├── writing-style-guide.md
│   ├── publishing-plan.md
│   ├── chapter-plan.md
│   └── characters-and-grounding.md
│
├── assets/                    ← reusable artwork
│   ├── illustrations/         ← figure SVGs extracted from the HTML
│   └── covers/                ← cover artwork variants and notes
│
└── sessions/                  ← per-session notes from Claude work
    └── 2026-06-07-initial-repo.md
```

---

## Standard recipes

### Adding a new chapter to the manuscript

1. Create `manuscript/NN-chapter-slug/` directory.
2. Create `_opener.md` with the chapter title, eyebrow (part), epigraph, and any opening matter.
3. Create section files numbered `01-section-slug.md`, `02-section-slug.md`, etc., one per top-level section.
4. Update `BOOK.md` to mark the chapter as DRAFTED with word counts.
5. (Later, at milestone) Sync `web/index.html` from the manuscript content.

### Updating the HTML reader from the manuscript

The web reader is currently maintained manually. When several chapters have been drafted and it's time to refresh `web/index.html`:

1. For each new section, add an `<article class="chapter-page" id="page-{slug}" data-slug="{slug}" data-title="{title}" data-prev="{prev-slug}" data-next="{next-slug}">...</article>` block in the chapter-main section.
2. Add a corresponding `<a class="sidebar-link" href="#{slug}">...</a>` in the sidebar nav.
3. Add a chapter card to the overview grid.
4. Fix up `data-prev` / `data-next` on the surrounding articles so navigation is continuous.

A small build script could automate this later. Not necessary yet.

### Updating the cover

1. Replace `web/cover.png` with the new artwork.
2. That's it. No HTML change needed.
3. Save the previous cover to `assets/covers/archive/` with a date prefix if it deserves keeping.

### Printing the preview to PDF

1. Open `web/index.html` in a browser.
2. Click the print icon (or `Ctrl/Cmd+P`).
3. Choose "Save as PDF" with default settings — the print CSS handles the rest (cover on its own page, chapters page-break-before, asides inline, toolbar/sidebar hidden, 0.7in margins, 11pt body).

---

## Honest boundaries

**What is known.** The book has its thesis, its grounding context, its main character, and a drafted opening chapter. The discipline being described is real (Refinement-Oriented Programming maps onto Mansour's actual methodology developed across years of work in regulated software). The Sonibank Niger production case is real. BCEAO and WAEMU are real. The five-part / fifteen-chapter structure is set.

**What is not yet known.**
- The exact narrative arc of Chapters 10–12 (Sonibank case). Outline exists; scenes and dialog do not.
- The precise level of technical depth in Chapters 4–9. Decisions about code listings, RFN grammar fragments, and ROM examples are not yet final.
- Whether the book has a foreword or preface, and by whom.
- Final cover. Current giraffe artwork is the working cover for the preview edition; final cover may iterate.
- Translation strategy. The book is in English; a French edition is plausible but not committed.

**What is deliberately out of scope.**
- The book is not a textbook on language design.
- The book is not a tools survey of agentic coding platforms.
- The book is not a polemic about AI in software development.
- The book does not predict the future of the industry. It reports what one small team did.

**What Mansour explicitly does NOT want.**
- No paid endorsements, blurbs from celebrities, or marketing puff.
- No association with any single vendor's tooling beyond what Sonibank actually used.
- No "first book on agentic governance!" positioning. The book stands on its own grounding.
- No translation or summary that loses the West African grounding. The book is by and for a Global South practitioner first.

---

## How to use this file in a new session

1. Open the repo in Claude Chat desktop as a project.
2. The session reads `CLAUDE.md` and inherits all locked decisions and constraints.
3. Skim `BOOK.md` to remember the manuscript outline.
4. If working on prose, read the relevant `manuscript/NN-chapter/` directory.
5. If working on design or layout, read `docs/design-system.md`.
6. If working on publishing or strategy, read `docs/publishing-plan.md`.
7. Add a session note to `sessions/YYYY-MM-DD-{topic}.md` describing what was done so the next session inherits the trail.
