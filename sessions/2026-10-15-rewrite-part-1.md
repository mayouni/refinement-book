# 2026-10-15 — the rewrite begins: Part I

```
by:        refinement-book · claude-opus-5-5 · 2026-10-15 12:28
subject:   Part I of the rewrite drafted, run and verified: chapters 1 to 3
why:       the author: "Yes, I confirm the delegation and the decisions in your memo. Record them and start the rewrite."

did:
  - recorded ROP-02 to ROP-12 in DECISIONS.md, on his delegation; ROP-12 chose the Teaching Edition's letter (18 to 16 per cent, ninety days)
  - copied the run tools from the Softanza book (tools/book_common.py, book_judge.py, book_run.py), reading its snapshot of the library at 93d7a39bd
  - drafted chapters 1 The letter, 2 What broke, 3 The unit of change; the build ran 10 of 10 blocks kept at 93d7a39bd
  - had each chapter checked by a fresh verifier: 125 claims, 30 flagged, all fixed (research/verify/ch01.md, research/ch02.md §7, research/ch03.md §5)
  - rewrote the book's CLAUDE.md for the rewrite; the lint is clean (0 em dashes, 0 forbidden words)

state:     ch01 draft · 5/5 kept · 3 guards · no translation · not read
           ch02 draft · 2/2 kept · 2 guards · no translation · not read
           ch03 draft · 3/3 kept · 1 guard · no translation · not read

waiting:
  - RL-01: a guard for a LIB refinement point -> the library's session [not routed]
  - RL-02: a non-numeric value proposed to a bounded parameter refused with a reason, not error R41 -> the library's session [not routed]
  - RL-03: a guard asserting the other points on a line (alsoTouches) -> the library's session [not routed]

next:
  - you:  read chapters 1 to 3 when you choose; nothing waits on you
  - me:   Part II, chapters 4 to 8 (the point, the gate, the cascade, the timeline, trust and governance), the same way

note:      the gate's order in the code (structural, constraint, governance, trust, derivation) differs from the order its admitted message prints; chapter 5 says so
```
