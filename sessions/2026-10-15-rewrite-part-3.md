# 2026-10-15 — the rewrite: Part III

```
by:        refinement-book · claude-opus-5-5 · 2026-10-15 13:20
subject:   Part III drafted, run and verified: chapters 9 The AI model comes last and 10 The safest write surface
why:       the author: "Yes, continue with Part III, chapters 9 and 10, the same way."

did:
  - drafted chapters 9 and 10 against the library at 93d7a39bd, citing the Softanza book's chapters 9, 17, 19, 20 and 24 and the platform's door for AI agents (decided 2 October 2026, not built)
  - ran a programmatic agent (a loop over the declared points), a hand-written draft standing for an AI model's answer, and a rehearsal on a copy of the refinable code
  - had them checked by a fresh verifier: 66 claims, 14 flagged, all fixed; recorded ROP-15 (two refusals as the book's choices)
  - the build ran 30 of 30 blocks kept across chapters 1 to 10; the lint is clean

state:     ch09 draft · 2/2 kept · 1 guard · not read
           ch10 draft · 2/2 kept · 3 guards · not read

waiting:
  - RL-01 to RL-06 -> stzlib [not routed]
  - RL-07: a guard asserting that a copy of a refinable code leaves the original untouched -> stzlib [not routed]

next:
  - you:  read chapters 1 to 10 when you choose
  - me:   Part IV, chapters 11 and 12 (Softibank, eighteen months: the refinement Amina made, what the auditor saw)

note:      no AI model is called in the book's runs; chapter 9 says so, and shows what happens to an AI model's text
```
