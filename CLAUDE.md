# CLAUDE.md — Refinement-Oriented Programming (the rewrite)

**Read this first.** This folder holds *Refinement-Oriented Programming*, the second of the AYOUNI books (house decision HOUSE-13), being
rewritten radically on the Softanza book's foundation. The author's rulings for the rewrite are in `DECISIONS.md` (ROP-01 onward) and
override anything below that disagrees. The house's rules (`../../CLAUDE.md`) bind this folder too.

```
Refinement-Oriented Programming
A discipline for software in the agentic era
Stop trying to govern the intelligence, and govern the change.
```

**Author:** Mansour Ayouni · **Imprint:** AYOUNI · **Series:** second of the AYOUNI books; *Softanza — The Governed Software Platform of the AI
Age* (`../softanza-book/`) is the first and this book's technical foundation.

## Two editions in one folder, until the handover

| | The live Teaching Edition | The rewrite |
|---|---|---|
| Source | `manuscript/rop-book.md` | `src/en/NN-slug.md`, one page per chapter (ROP-11) |
| Build | `web/build.py`, `web/print.py` | `tools/book_run.py` (runs every block); the reader build comes before the handover |
| Who edits | the house desk and the Softanza book session, for the house's corrections | this book's session |
| Online | yes, at `/books/refinement/en/` and `book.pdf` | no, until the author has read it and handed it over (HOUSE-13(c), ROP-08) |

Do not edit `manuscript/`, `web/`, `assets/covers/` or `site/` from the rewrite without the house desk's word. The old plans in `BOOK.md`,
`docs/chapter-plan.md`, `docs/publishing-plan.md`, `docs/writing-style-guide.md` and `docs/teaching-edition-plan.md` are superseded by
`DECISIONS.md` and kept as the record.

## The story

Softibank (ROP-01), a fictional commercial bank in Niamey, receives a letter from the BCEAO: Directive 4.5 lowers the penalty cap on consumer
credit lines from twenty per cent to sixteen, with six weeks to comply across fourteen loan products. Amina Bello, its IT methodologist, is the
centre of the story; the methodologist (the author's stand-in) is never named; the auditor visits at month eighteen. The bank, its people and
the directive are invented and the book says so once (ROP-05); BCEAO, WAEMU, Niamey and the CFA franc are real. The particulars of the story
are those of `manuscript/01-what-broke/` and `docs/characters-and-grounding.md`, renamed; nothing is added to them without the author.
The story is told in the third person; "I" in the book is always the author speaking as himself, never a character.

## The outline (ROP-10)

I The discipline: 1 The letter, 2 What broke, 3 The unit of change. II The gate, run: 4 The point, 5 The gate, 6 The cascade, 7 The timeline,
8 Trust and governance. III The AI agent at the point: 9 The AI model comes last, 10 The safest write surface. IV Softibank, eighteen months:
11 The refinement Amina made, 12 What the auditor saw. V Refine, the product and the IDE: 13 The environment, specified. Coda, The next letter.
Glossary, aligned with Softanza's appendix D. About 2,000 words a chapter.

## The shape of a chapter

Front matter: `id`, `part`, `number`, `title`, `stage` (`built`, `designed`, `absent`, carried from code, never from documents), `status: draft`
(only the author sets `read`), `research`, `guards`. Then, in order: an opening in the first person that says what the chapter does (a few
sentences); the story's scene where the chapter has one; `## The field`; `## The principle`; sections that run a block, show its exact answer and
read it (titled freely); `## What I refused`; `## The court`; `## Where the field leads`; `## The limit`; `## In your hands` (a real defect or
open question, with a `haro exercise` fence); a closing bridge to the next chapter, never a summary. Headings are reused exactly.

## The evidence and the run

- The library is pinned at **93d7a39bd** (ROP-07), the Softanza book's pin, and run from a snapshot, never from `D:\GitHub\stzlib`'s working
  tree. `tools/book_common.py` reads the Softanza book's snapshot when present (it is not copied) and exports its own into `.cache/` otherwise.
- Every block is a ```` ```haro ```` fence whose `#-->` lines are its promise; `python tools/book_run.py` runs each chapter in one process and
  writes the verdicts to `data/book-run.json`. A chapter whose blocks do not all keep their promise is not done.
- Research per chapter in `research/chNN.md`, every block probed in `base/test/_probe_ropNN` inside the snapshot and the folder removed.
- Never run `zig`; one `ring` process at a time, in the foreground; never background a heavy command.

## The voice (the AYOUNI Writing Framework, `../../writing-framework/FRAMEWORK.md`, v0.2)

First person, "you" at the keyboard, the tool as "it" (ROP-02); run it, then read it; a question is a beat answered on the page; an exclamation only
after a run or a reveal, one or two per thousand words; long sentence then short verdict; the colon, not the dash; one metaphor at a time; no
particular the record or the author did not give. Cite the Softanza book's chapters for what they already establish; do not re-derive them.
The lint: `python ../../writing-framework/tools/style_lint.py src/en --strict`. Then a fresh verifier (`briefs/fresh-verifier.md`), the voice
reader (`briefs/voice-reader.md`) and the fixer (`briefs/fixer.md`).

## Rules that bind

- The house's and the author's standing rules: never undersell the work (stage and direction, never "weak" or "falls short"); the language is Haro,
  and the former host language is named nowhere in this book; "crafter" is the person, never "maker" outside "decision-maker"; "AI model" and
  "AI agent" where the bare word is ambiguous; no "substrate", no "developer" for programmer; no emoji; text size follows semantic level.
- Kept from the Teaching Edition's hard constraints: reference documents are Markdown only; no yellow anywhere in the design; body text is
  monochrome; every spec ends with what is known, what is not yet known and what is out of scope; never invent metrics, prices, dates or
  endorsements.
- Refine is told as stage and direction, with a date: specified in over a hundred documents, an interactive mockup of its screens, a command whose
  `version`, `status` and `init` run and six verbs are queued. It is never the subject of the gate (ROP-03).
- Commit by explicit paths, never `git add -A`; never push (the house desk pushes, and a push publishes); never set `status: read`.
- Every substantive report to the author is a memo in the format of `../../writing-framework/templates/memo.md` (HOUSE-MEMO-01).

## Working state

- 2026-10-15: phase 0 (the read) done; the author's rulings ROP-01 to ROP-11 recorded, ROP-02 onward on his delegation; the run tools copied
  from the Softanza book (`tools/`); chapter 1, *The letter*, drafted (`src/en/01-the-letter.md`, five blocks kept at 93d7a39bd).
- Session notes: `sessions/YYYY-MM-DD-topic.md`.
