---
id: the-letter
part: 1
number: 1
title: The letter
stage:
  built: "the refinement point declared in the source; the proposal judged by a gate of five checks (two of them run here); the refusal that leaves the source whole; the step taken back; the cascade of a point (its line) and of a class (the code graph)"
  designed: "the two cascades joined into one, reaching beyond a line; Refine, the environment in which a team lives with refinements day to day (Part V)"
  absent: "a saved history: the file the library writes keeps the source, not the timeline"
status: draft
research: research/ch01.md
guards: [refinablecode_narrated, refine_deepening_narrated, gate_deepening_narrated]
---

In this chapter I tell the letter that starts the story of this book, and I say what it asks of the software of a bank. Then I run the one thing the rest of the book is built on: a change proposed to a place in the code that was declared to be changeable, and judged before it lands. I close on what that one run does not yet do.

The bank in this story is invented. Softibank, its people and the letter it receives are fiction, written to carry a discipline that is not. The central bank, the monetary union, the city and the currency, the CFA franc, are real, and I treat them as such.

## The letter

The letter arrived at Softibank, a commercial bank in Niamey, on a Tuesday in September: paper, stamped, from the *Banque Centrale des États de l'Afrique de l'Ouest* in Dakar. The BCEAO is the central bank of the eight countries of the West African Economic and Monetary Union, and when it issues a circular, every commercial bank in the union adjusts.

This one was routine, as regulation goes. Under a revised directive, the cap on late-payment penalties would drop from eighteen per cent to sixteen. Compliance within ninety days.

Amina is the bank's IT methodologist: part programmer, part analyst, the person the team asks when the question is about how to work. She read it twice, then opened a notebook and listed what the number touched.

The penalty cap was not one line in one file. It fed the pricing of fourteen loan products. It appeared in the risk-assessment module, in the quarterly compliance report, in the statement generator that printed customer letters, in the text-message templates that warned late payers, and in tests that asserted, in effect, that the world is eighteen per cent. Some of these she knew. The others she would discover, she wrote, "when they break."

The work of writing the change was not what worried her. Her team wrote faster than it ever had; AI agents helped at every turn, and code reached the modules faster than any one person could read it line by line. What worried her was a question that speed made harder, not easier.

When a change is written, what else moves?

## The field

The field's answer to that question is the review. A change to code arrives as a diff, a patch of text, and a person reads it before it is merged. Tests run, a second person approves, and the history of the repository keeps the patch. In infrastructure the field goes further: a tool computes what would change, shows the plan, and applies it only when you say so. All of this is general knowledge, and it is good practice.

The review rests on one assumption: that a person wrote the change and a person can read it, at the pace the changes come. My Softanza book, on the platform this book stands on, opens on the place where that assumption gives way: change arrives faster than trust (*Softanza*, chapter 1). I do not re-tell that chapter here. I tell what it means at a bank with ninety days and fourteen products.

A diff tells you which lines changed. It does not tell you that the line was meant to change, how far it may change, who proposed it, or how to take it back. A reviewer supplies all four from memory and judgement. At the pace of a person, that works. At the pace of a team helped by AI agents, memory and judgement are the bottleneck, and the letter has a date on it.

## The principle

I put one sentence on the back cover of this book, and the rest of the book runs it: **stop trying to govern the intelligence, and govern the change.**

It does not matter here whether the penalty cap is changed by Amina, by Issa, the senior programmer, or by an AI agent proposing a patch. The intelligence that wrote the change will be different next year. The change is what reaches the customer's contract. So the thing to govern is the change: where it may happen, within what bounds, from which origin, and how it is taken back.

That is what I call a refinement. A refinement is a change to code that was declared to be changeable, proposed in a typed form, judged by a gate, recorded as a step, and reversible. The definition is the one my Softanza book gives in its chapter 10, and this book is that chapter told at full length, with a bank in it.

## The cap, declared

Run it. The penalty cap becomes a refinement point: a named knob written into the source as a tag, with its kind, its current value and its bounds. Here its bounds run from ten per cent to twenty, and its value is the old cap, eighteen:

```haro
cSrc = 'penalty = balance * <R:PARAM name="penalty_cap" value="0.18" min="0.10" max="0.20">'
o = new stzRefinableCode(cSrc)
? o.NumberOfPoints()
#--> 1
? o.ValueOf("penalty_cap")
#--> 0.18
```

One point, and its value is `0.18`. The line is still a line of code; the tag says that this part of it may change, and how far.

Now the directive. A change is not an edit of the text: it is a proposal that names the point and the new value.

```haro
r = o.Refine("penalty_cap").To("0.16")
? r[:admitted]
#--> 1
? r[:why]
#--> admitted: 'penalty_cap' 0.18 -> 0.16 [:trusted] (structural + constraint + derivation + governance + trust passed)
? o.NumberOfSteps()
#--> 1
```

Admitted, and the answer says why. It names the value before and after, the origin of the proposal, `[:trusted]`, and the five checks of the gate, in the order the message prints them. On this point only the first two had anything to judge, the structure of the proposal and the bounds of the point: no governance, floor of trust or rule across points was declared yet, and chapter 5 runs the five in the order the code runs them. One step is recorded. The admission prints as `1`.

The next blocks are written as scenes: the object is named once, `o { ... }`, and each line inside the braces speaks to it. The first two blocks named the object on every line, the classic form, and a proposal is one sentence, the chain `Refine(...).To(...)`. This book uses the scene where three or more things are said to one object, and the chain where the thought is one sentence.

## The slip

Ninety days is enough time to write the change, and people type fast. Suppose the proposal arrives with two digits swapped:

```haro
o {
	r2 = Refine("penalty_cap").To("0.61")
	? r2[:admitted]
	#--> 0
	? r2[:why]
	#--> constraint: 0.61 above max 0.20
	? ValueOf("penalty_cap")
	#--> 0.16
	? NumberOfSteps()
	#--> 1
}
```

Refused! The refusal names its check first, `constraint`, then says what was wrong: `0.61 above max 0.20`. The value is still `0.16`, and the timeline did not grow by a step. Nobody had to read a diff to see that sixty-one per cent is not a penalty cap a bank may charge. The point said so.

And what does the code look like now? Ask it:

```haro
? o.Rendered()
#--> penalty = balance * <R:PARAM name="penalty_cap" value="0.16" min="0.10" max="0.20">
```

The tag carries the new value, and the bounds are still there for the next proposal. The point is a knob that stays in the code, not a one-time substitution.

## The step taken back

A change made early may have to wait for the day the new cap applies, and a change made wrongly has to be undone. Can the step be taken back?

```haro
o {
	Revert()
	? ValueOf("penalty_cap")
	#--> 0.18
	? NumberOfSteps()
	#--> 0
	? Refine("penalty_cap").As(:llm).To("0.16")[:admitted]
	#--> 1
	? PostureOf(1)
	#--> llm
}
```

Reverted: the value is `0.18` again and the timeline is empty. Then the same change is proposed by an AI model, which the proposal says with `As(:llm)`. It is admitted, and the step records its origin, which the library calls its posture: `llm`.

Read that last answer twice. Nothing in this point refuses a proposal from an AI model, because nothing was declared that would: the point has bounds and no floor of trust. The origin is recorded, not judged. Whether it should be judged is a declaration you make on the point, and chapter 8 makes it.

## What I refused

**I refused to make the review the gate.** The review stays: a person still reads what matters. But the first judgement of a change is made by the code itself, against what the code declared about the place being changed, before a person spends attention on it. The person reads a change that already cleared the declared bounds, with a reason attached to every refusal.

**I refused the diff as the unit of change.** The diff is kept as an artefact; it is not the thing a team governs. The unit is the refinement: a point, a value, an origin, a verdict and a step. Chapter 3 says why the unit had to change.

## The court

What proves this chapter is not my run alone. The library carries three guards for the refinement, in `base/test/refine/`: `refinablecode_narrated`, `refine_deepening_narrated` and `gate_deepening_narrated`. Between them they assert the point declared, the proposal admitted, the refusal that leaves the source whole, the timeline with its checkpoints, the trust floor and the governed refusal. The chapters of Part II run what they prove.

## Where the field leads

The field leads in breadth. A review can look at any change to any file in any language, declared or not; a refinement point covers only the places someone declared. A change to an undeclared place is outside this gate, and the review still has to catch it.

The field also leads in habit. Programmers know the diff and the pull request; a refinement point is a new thing to write and a new answer to read. That is the cost of the discipline, and this book pays it chapter by chapter.

## The limit

What is built: the refinement point, declared in the source; the proposal; the gate with its five checks; the refusal that leaves the source whole; the step taken back. All of it ran above, against the library at the commit this book is pinned to, the gate on its first two checks; the guards prove the other three, and Part II runs them.

What is designed: the cascade that would tell Amina what a point reaches beyond its line. Today two cascades are built: a point's cascade is its line and the other points on it, and a class's cascade comes from the code graph. The two are not yet one, and chapter 6 runs them. Refine, the environment in which a team lives with refinements day to day, is specified and shown as screens; Part V tells it as stage and direction.

What is absent: a saved history. The library saves the source with its current values; the timeline you just reverted lives in the running object, and carrying it into the file is the next step.

## In your hands

Take a setting of a program of yours that has a ceiling: a rate, a limit, a timeout. Declare it as a point with that ceiling as its `max`. Before you run anything, write down two things: the value one step over the ceiling, and the exact first word of the refusal you expect.

```haro exercise
cMine = 'limit = <R:PARAM name="my_limit" value="10" min="0" max="10">'
m = new stzRefinableCode(cMine)
? m.Refine("my_limit").To("11")[:why]
```

Run it. Then declare the point again with `min="15" max="20"`, keeping its value at 10, below the new `min`, and propose 12. I will not tell you what the second run says. When you have read it, you will know whether the gate checks the value that is there, or only the value proposed.

The letter asked for one change. The next chapter asks why one change became hard, and what broke when writing stopped being the slow part of the work.
