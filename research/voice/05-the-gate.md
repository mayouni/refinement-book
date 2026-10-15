# Voice reading: 05-the-gate.md

Reader: a fresh voice reader (brief `writing-framework/briefs/voice-reader.md`), 2026-10-15. Nothing in the chapter was changed.

1. **Shape (C9).** Opening: first person, three sentences, a real roadmap: "I make each one refuse in turn, on one governed configuration, in the order the code runs them." One vague item: "what the gate's answers are made of" (opening) names no section. Section closes: "Five refusals" closes on a dead end (the derivation paragraph); "The verdict that lands" closes on reasoning; "The four of the design" closes on "This book reports the five." (a verdict, good); "Deterministic" closes on "it spends it where it is needed, on the declarations." (good). Chapter close: a bridge, "the cascade, which a reviewer reads instead of the diff". Good.

2. **Run, then read (C1).** Strong: the five refusals run in one block, then each is read. Explanation before the thing: the setup paragraph of "Five refusals" (actor, delegated authority, risk tier two, floor of trust, rule across points) explains six things before the block shows them; the comments inside the block already carry most of it. Abstract paragraph: "The field", "What the field rarely has is one gate that knows the place being changed: its bounds, who may change it, from which origin, and what must stay true around it." Worst: "Deterministic", "the checks compare a value with bounds, a name with a list, an authority with a tier, a posture with a floor" (no run of the same proposal twice).

3. **The defect (C2).** Real: which rule the refusal names when two break, "I leave the choice open." But the page gives the answer before the run: "The refusal names one rule, not two." (In your hands), after asking the reader to predict. Wrong before right: the five refusals before the admission, good. Correct code rejected for taste: "I refused a gate that asks an AI model" with the reason ("could differ after lunch"). Good.

4. **Where it stops (C3).** Limit present, stage words used. Loss beside win: "a change can pass all five checks and still be a poor idea" (Deterministic). Undersell: none of "weak"/"falls short". Self-advertising in place of a limit: "That is also the gate's honest edge." (Deterministic). Reach: "a refusal costs seconds" (What I refused): a number no run shows. "an auditor can replay it, given the declarations" (Deterministic) is narrowed by the next sentence about `Save`, good. "which is a line" (The limit) is opaque: a line of code? a one-line fix? It sounds like a promise of size.

5. **The particulars (C4).** Fatou, compliance officer (record: `docs/characters-and-grounding.md`); Amina; "the bank's risk committee" (invented, hedged with "might set, say"); `pricing-agent`, `credit-ops` (code). "Softanza's chapter 10 says it in one line: I wrote the design with four stages, and the code has five checks." (The four of the design) quotes the author's other book in the first person; it should read as a quotation or be paraphrased. No `[AUTHOR` markers. "My design of the gate had four stages" is the author's own record, fine.

6. **Metaphors (C5).** "gate" (ruling, stable). "knob" carried from chapter 4 ("May this actor turn this knob?"), stable. "floor" used for two things: the trust floor (`TrustFloor`) and the `policy_floor` point; in one paragraph ("a floor below which the cap may not fall... A floor of trust is set on the cap") the two floors sit side by side and blur. "half-lands" (What I refused): load-bearing, short. "after lunch": a flourish that carries the point.

7. **Address (C6).** I: 10 (witness: "I report what runs", "I leave the choice open"), my: 1; we: 0; you: 4 ("which you just watched", the exercise). Prose questions: about 7, the five check questions plus "And a proposal that clears all five?" and "May this actor turn this knob?", all answered on the page. Exclamation: 1, "And the cap is still `0.18`!" after a run. Good. "ask yourself" (In your hands): fine.

8. **Rhythm and noise (C7, §4).** Long then short: "Five proposals, five refusals, each naming its check first."; "I report what runs." Colons: 30; prose dashes: 0. Intensifiers: none. Hedges: "one the bank's risk committee might set, say" (Five refusals) and "the cap never below fourteen per cent, say" (In your hands): "say" twice, the first stacked with "might". Absolutes: "Nothing in the gate draws at random" (backed). Tic: "All of this is general knowledge." (The field), the third chapter in a row; "honest" (Deterministic).

9. **Counted sets (C8).** "Five checks" matches the block and the five bold readings, named exactly (structural, constraint, governance, trust, derivation). "four stages" of the design matches its list. "two answers" in In your hands: matches. The admitted message's order (structural + constraint + derivation + governance + trust) is read as the printed order, exact.

10. **The stake (C10).** "Whatever else in a bank's software is probabilistic, the moment of admission is not, and an auditor can replay it" (Deterministic): rises to the auditor and the bank, backed by the block and narrowed by the `Save` sentence. Good. "That knowledge exists, in the heads of people like Fatou... The gate of this chapter is where it is written down." (The field): a stake about people, backed by the chapter.

11. **Most him.**
- "Admitted, with the value before and after and the origin... It is not the order the code ran them, which you just watched... I report what runs." (The verdict that lands)
- "The refusal is not about the value at all: nobody said what changing the floor would risk, so nobody may change it." (Five refusals)
- "A verdict that could differ after lunch cannot be replayed for an auditor." (What I refused)

**Least him:** "Here is the cap and, beside it, a floor below which the cap may not fall, one the bank's risk committee might set, say; both are declared as points." (Five refusals). Reason: a run-on with a stacked hedge ("might... say") and a semicolon splice where the author would state it and run it.

12. **The one change.** Move the six-part setup of "Five refusals" into the block's comments and open the section with "Run it." and the block, so the reader meets the governed configuration as code first.
