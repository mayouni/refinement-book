# Chapter Plan — Refinement-Oriented Programming

The fifteen-chapter outline with intent, key beats, and writing priority.

> `CLAUDE.md` is the source of truth for what's currently drafted. This file is the source of truth for what each chapter is *about*.

---

## Prologue — The Q3 letter (p. 11)

**Status:** Not yet drafted.

**Length target:** 1,800–2,200 words.

**Intent.** A short narrative bridge that introduces Amina, the bank, and the world of WAEMU regulated software *before* Chapter 1 develops the diagnosis. Where Chapter 1 is structural ("here is what broke"), the Prologue is atmospheric ("here is the place where it broke"). The reader learns who Amina is, where she lives, what the bank's offices feel like, what an ordinary day there looked like before the discipline was needed.

**Key beats.**
- Niamey morning, the office, the team
- Amina's role — IT methodologist, not pure programmer, not pure compliance officer
- A small flashback: a directive received a year ago, handled the old way
- The handoff into Chapter 1: "Then a Tuesday in September arrived."

---

## Part One · The diagnosis

### Chapter 1 — What broke (p. 17) — DRAFTED

**Status:** DRAFTED (~1,900 words). Four sections, two figures, four asides.

**Length target:** Met.

**Intent.** Establish the symmetry break: writing speed multiplied, review speed didn't, the old artefact (text diff) ceased to scale. Frame the book's argument and preview its structure.

---

### Chapter 2 — The unit changed (p. 39)

**Status:** Not yet drafted.

**Length target:** 4,500–5,500 words.

**Intent.** The text diff in depth. Why it served a previous decade and not this one. What its weaknesses look like when 80% of code is written by agents. What replaces it — the refinement, the cascade-as-artefact, the change-as-graph-mutation.

**Key beats.**
- A walk-through of a typical text-diff review at agent throughput
- The reviewer's experience: too much, too fast, with insufficient context
- What the reviewer actually needs: not the diff, but the cascade
- Introducing "the refinement" as the candidate replacement unit
- A short technical interlude on what makes the refinement different from a commit, a PR, a CL

**Figures expected.** A diff (textual) next to a refinement (graphical). Possibly two figures.

---

### Chapter 3 — The codebase as a graph (p. 59)

**Status:** Not yet drafted.

**Length target:** 4,500–5,500 words.

**Intent.** Reframe the codebase from a tree of files to a graph of refinements. Establish the conceptual model that the rest of the book operates inside.

**Key beats.**
- The historical tree-of-files model and what it was good for
- Where the tree model breaks down at agent throughput
- The graph model: nodes are constructs, edges are refinements
- The auditor's perspective on the graph model — why regulators find this familiar
- A first concrete example from Sonibank: the loan-product graph

**Figures expected.** Graph visualization of a small subset of the bank's code.

---

## Part Two · The discipline

### Chapter 4 — The compiler that revalidates (p. 83)

**Status:** Not yet drafted.

**Intent.** The mechanism. A refinement-aware "compiler" (not in the strict CS sense — closer to a static analyzer + cascade tracker) that re-checks the downstream cascade every time anything upstream changes. What it produces. What it costs. What it makes possible.

**Key beats.**
- The compile-then-review handoff under text diffs
- What re-validation means in a refinement model
- The economics: incremental, cached, parallelizable
- The team's experience of working with the revalidator
- What the revalidator catches and what it does not

---

### Chapter 5 — The cascade as a working surface (p. 105)

**Status:** Not yet drafted.

**Intent.** The cascade is not a side effect; it is the artefact the team works on. The interface, the discipline, the new normal.

**Key beats.**
- Working in cascades: a day in the life
- Visualizing the cascade as the team sees it on their monitors
- What "completing a change" looks like — not when the code compiles, but when the cascade closes
- How the cascade view differs from the IDE view, the diff view, and the spec view

**Figures expected.** Screenshot-style illustrations of the cascade UI from Refine (or a fictional equivalent).

---

### Chapter 6 — Authorities, attribution, audit (p. 127)

**Status:** Not yet drafted.

**Intent.** The governance dimension. Who decides. Who is recorded. What the auditor reads. This chapter is where the book speaks most directly to the regulated-industry reader.

**Key beats.**
- The four types of agents in the system: humans, machines (agents in narrow sense), policies, regulators
- Attribution: every refinement carries its author, its proposer, its reviewer
- Authorities: who is allowed to commit what, against which surface
- The audit trail: how the auditor reads the cascade history
- Sonibank's BCEAO audit, foreshadowed (Chapter 12 will pay this off)

---

## Part Three · The system

### Chapter 7 — A methodology, not just a tool (p. 149)

**Status:** Not yet drafted.

**Intent.** Refinement-Oriented Programming is a discipline first and a tool second. This chapter makes that distinction explicit and shows what the team did with paper, conversation, and process *before* any tool was built.

**Key beats.**
- The first three months at Sonibank: paper and whiteboards
- The methodologist's role: ask questions, never write code
- What happened when the team thought they could buy the discipline as a tool (they couldn't)
- When tooling became appropriate, and why
- The lesson: tools follow discipline, not the reverse

---

### Chapter 8 — Five surfaces, one engine (p. 169)

**Status:** Not yet drafted.

**Intent.** The five working surfaces (design, code, scripting, refinement, governance) and the single graph-engine underneath. The architectural account, but kept practitioner-grounded.

**Key beats.**
- The surfaces, in order: what each does, who works on it
- Why they share an engine and not five
- What the engine knows that the surfaces don't
- A diagram of the whole system at Sonibank scale

**Figures expected.** A high-level architecture diagram.

---

### Chapter 9 — Programmable by its users (p. 187)

**Status:** Not yet drafted.

**Intent.** Extensibility. The discipline must be programmable by the people doing the work — compliance officers writing their own constraint checks, analysts writing their own report templates, programmers extending the language.

**Key beats.**
- The principle: the people who depend on the system must be able to change it
- How Sonibank's compliance officers wrote their own validators
- Examples of small extensions that mattered
- The escape hatch from declarative-first into general-purpose code, when needed
- The trust boundary between PI agents and LLM agents (architectural carryover from Zpj — explain it without leaning on Zin terminology readers don't have)

---

## Part Four · The case

### Chapter 10 — Sonibank Niger (p. 207)

**Status:** Not yet drafted. **High priority** — Mansour wants this written early because Parts Two and Three reference it.

**Length target:** 5,000–6,000 words.

**Intent.** The production case. The bank, its regulatory environment, its team, its codebase before the discipline. Document the starting conditions thoroughly enough that the reader trusts the later chapters.

**Key beats.**
- Sonibank as an institution: its size, its book, its customers
- The IT department: ten programmers, two analysts, Amina, two interns
- The codebase before: Ring + Python + COBOL fragments, 220k lines, four production services
- BCEAO's typical year: three to four directives, one audit cycle in three
- The OHADA harmonization layer that complicates everything
- Why a small WAEMU bank produced this discipline and not a Silicon Valley unicorn

---

### Chapter 11 — Amina's refinement (p. 227)

**Status:** Not yet drafted.

**Length target:** 5,500–6,500 words.

**Intent.** The narrative payoff. Eighteen months from the Q3 letter to the auditor's visit, told in scene-by-scene detail. This is the book's longest chapter.

**Key beats.**
- The first week after the letter
- The team's initial response — the failed first attempt
- The methodologist arrives. The team works on paper for three weeks
- The first successful refinement of the penalty cap
- The second directive, four months later, handled in four days instead of six weeks
- The compliance officer who learned to write her own validators
- The November audit. The June audit. The next year's directive.

---

### Chapter 12 — What the auditor sees (p. 249)

**Status:** Not yet drafted.

**Intent.** Month 18. The BCEAO auditor's visit. What the discipline produced is presented and inspected. If the audit is clean, the discipline held.

**Key beats.**
- The auditor's checklist, in their words
- What the auditor used to ask for, and how the bank used to provide it
- What the auditor asks for now, and how the cascade history answers it
- One specific challenge in the audit, traced through the refinement record
- The auditor's report. The book's quietest victory.

---

## Part Five · The implications

### Chapter 13 — The bottleneck moves (p. 269)

**Status:** Not yet drafted.

**Intent.** Generalize carefully. Why what worked at Sonibank maps onto a broader shift the industry is starting to see. Reference (without leaning on) the Anthropic Institute observations from 2026.

**Key beats.**
- The published evidence on the bottleneck shift
- Why review is harder to scale than writing
- What other industries (not just banking) face the same shift
- What the regulated-industry experience contributes
- A short, deliberate caveat: this is one bank's experience, not a universal law

---

### Chapter 14 — The agentic stack (p. 289)

**Status:** Not yet drafted.

**Intent.** A map of the new software industry. Where refinement-oriented practice fits. What other categories exist (writing acceleration, code generation, agentic IDE, governance tooling) and how they relate.

**Key beats.**
- The twelve layers of the agentic stack (carryover from Mansour's earlier industry-survey document)
- Where refinement-oriented practice sits (governance + review + audit)
- Why it complements rather than competes with writing-acceleration tools
- The map for compliance officers and regulators — what to look for in vendor pitches

**Figures expected.** The stack diagram, simplified for the book's reader.

---

### Chapter 15 — What this is not (p. 307)

**Status:** Not yet drafted.

**Length target:** 2,500–3,500 words (deliberately shorter).

**Intent.** Honest about scope and limits. What the book is not claiming. Where the discipline does not apply. What the practitioner who adopts it should expect to fail at.

**Key beats.**
- This is not a complete methodology for greenfield startups
- This is not a substitute for engineering judgment
- This is not a finished discipline — it's a starting point
- This is not for the team that cannot afford the upfront cost
- This is the closing chapter — quiet, sober, encouraging

---

## End matter

### Epilogue — The next letter (p. 317)

A short envoi. Amina at her desk, perhaps a year after the auditor's visit. A new letter from BCEAO arrives. What she does with it, in three pages.

### Appendices (p. 323)

- A. The RFN grammar (formal specification, MIT-licensed)
- B. The Refinement Object Model reference (MIT-licensed)
- C. Glossary
- D. Selected reading

---

## Writing order (priority for next sessions)

1. Chapter 2 — The unit changed (continues Part One's diagnosis; the natural next chapter)
2. Chapter 10 — Sonibank Niger (grounds the rest)
3. Chapter 11 — Amina's refinement (the narrative payoff)
4. Chapter 12 — What the auditor sees (closes the case)
5. Chapter 3 — The codebase as a graph (completes Part One)
6. Chapters 4–9 (Parts Two and Three, in any order — depends on what's most ready)
7. Chapter 13 — The bottleneck moves
8. Chapter 14 — The agentic stack
9. Chapter 15 — What this is not
10. Prologue
11. Epilogue
