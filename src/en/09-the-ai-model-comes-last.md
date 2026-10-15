---
id: the-ai-model-comes-last
part: 3
number: 9
title: The AI model comes last
stage:
  built: "a programmatic agent, a plain loop over the declared points, whose proposals face the gate; a draft from an AI model read as a typed proposal and judged like any other; a floor of trust that refuses a proposal declared as the AI model's"
  designed: "the thinking machine's cascade across faculties, set out in the Softanza book's chapter 9 (listed in chapter 17); the AI model's draft held to the grammar of a declared language before it is read"
  absent: "an AI model called by this book's runs: the draft below is written as text, the way an AI model's answer arrives"
status: draft
research: research/ch09.md
guards: [refine_deepening_narrated]
---

In this chapter I open Part III and the question everyone asks first: what happens when an AI agent changes a bank's code? I answer it the way the Softanza book does, in order. The work that can be done by rules is done by rules. An AI model is called last, for what only it can do. And what it says is a proposal, judged like any other.

## The field

The field's agent is, by its own common definition, an AI model in a loop: given a goal, it calls tools, keeps some memory, and repeats until it is done. This is general knowledge, and it is a real and useful design. Its mind is one faculty, the AI model, and the safety of what it does is sought mostly in the AI model and around it: instructions, filters, a sandbox, a person who confirms.

My Softanza book takes that loop apart in its chapter 9 and runs the agent in its chapters 17 to 20. I keep the one result this book needs: the mind of an agent is a component, and you may choose it per task.

## The principle

**The mind is programmatic by default; an AI model is one faculty among others, the last one called, and what it says is a proposal that the gate admits or refuses.**

The sentence is the Softanza book's chapter 17, with its words for the model and the court given as this book's; this chapter runs it at a bank.

## The rules first

When the cap moved from eighteen per cent to sixteen, most of the work was not intelligent. Every product with a penalty cap needed the same new value. That is a rule, and a rule can be written as a plain loop over the declared points. Run it on three of Softibank's products:

```haro
cBook = 'auto_loan   = <R:PARAM name="cap_auto" value="0.18" min="0.10" max="0.20">' + nl +
        'school_fees = <R:PARAM name="cap_school" value="0.18" min="0.10" max="0.20">' + nl +
        'harvest     = <R:PARAM name="cap_harvest" value="0.18" min="0.10" max="0.20">'
o = new stzRefinableCode(cBook)
for aP in o.RefinementPoints()
	? o.Refine(aP[1]).To("0.16")[:why]
next
#--> admitted: 'cap_auto' 0.18 -> 0.16 [:trusted] (structural + constraint + derivation + governance + trust passed)
#--> admitted: 'cap_school' 0.18 -> 0.16 [:trusted] (structural + constraint + derivation + governance + trust passed)
#--> admitted: 'cap_harvest' 0.18 -> 0.16 [:trusted] (structural + constraint + derivation + governance + trust passed)
? o.NumberOfSteps()
#--> 3
```

Three proposals, three admissions, three steps. The loop is a programmatic agent in the plainest sense: it has a goal, it acts through the gate, and it reaches the same conclusion every time it runs, at no cost, offline. Nothing in it needs an AI model, and nothing in it should have one. A bank's penalty cap is work that must be exactly right, and exactly right is what rules do.

## The AI model, last

Where does an AI model belong, then? Where rules cannot go. A new circular arrives in French prose, and someone must read what it implies for the bank's products. That is language work, and it is what AI models are for.

What the AI model returns is text. Here is such a draft, written by hand for this run, the way an AI model's answer arrives, with a slip in it: sixty-one per cent where the circular says sixteen. No AI model is called in this book's runs; what matters is what happens to the text. The draft is read into a proposal, declared as the AI model's, against a point whose floor of trust is `external`:

```haro
cDraft = "cap_school = 0.61"
aParts = Q(cDraft).Split(" = ")
? @@( aParts )
#--> [ "cap_school", "0.61" ]
o2 = new stzRefinableCode(cBook)
o2 {
	TrustFloor("cap_school", :external)
	? Refine(aParts[1]).As(:llm).To(aParts[2])[:why]
	#--> constraint: 0.61 above max 0.20
	? Refine("cap_school").As(:llm).To("0.16")[:why]
	#--> trust: posture :llm below the required floor for 'cap_school'
	? Refine("cap_school").To("0.16")[:admitted]
	#--> 1
}
```

Read the three answers in order. (Governance passes here because none is declared, as chapter 2 said.) The slip is refused by the point's own bounds, before anyone asks where it came from. The corrected draft, still declared as the AI model's, is refused by the floor of trust: on this point, an AI model may suggest and may not land. The same value, proposed with the default trusted posture, as a person's proposal would be after reading the circular and agreeing with the draft, is admitted.

That is admission over generation. The AI model generated; the gate admitted or refused; and the person did what the gate cannot, which is to read the circular and decide that sixteen is what it says.

## What I refused

**I refused to make the AI model the mind.** The loop above did the work that had to be exactly right, and an AI model would have added cost and doubt to it. The Softanza book's chapter 17 states it as a law: programmatic by default.

**I refused to trust the AI model's text because it is fluent.** A draft is read into the same typed proposal as everything else, with its origin declared, and judged by the same five checks. Fluency is not a check.

## The court

`refine_deepening_narrated`, in the library's `base/test/refine/`, asserts that a point's floor refuses a proposal declared as composed by an AI model while a trusted one is admitted. The loop and the reading of the draft ran above; no guard asserts them.

## Where the field leads

The field leads in what an AI agent can do on its own. An AI agent in a loop can read a repository, write a change across many files, run the tests and open a request for review, all without a person. The discipline here hands it less: a set of declared points, a typed proposal, and a gate. Much of what such an AI agent does in the field is outside this gate, and stays a diff for review.

The field also leads in the AI model itself. The library's own language models, the domain language model of the Softanza book's chapter 19, are small and built for a closed vocabulary; reading a circular in French prose is work for the field's large AI models, which the bank brings and the library does not ship.

## The limit

What is built: the programmatic agent, a loop whose proposals face the gate; a draft read into a typed proposal with its origin declared; the floor of trust that refuses the AI model's proposal on a point that asks for more. All of it ran above.

What is designed: the thinking machine's cascade across faculties, set out in the Softanza book's chapter 9 and listed in its chapter 17; and the AI model's draft held to the grammar of a declared language before it is read, which the platform's door for AI agents names as a verb (chapter 10).

What is absent: an AI model called by this book's runs. The draft was written as text, and the reading of it was a split on `" = "`, which a real draft would break in many ways. The grammar compiler is built, in the Softanza book's chapter 19; holding a draft to it here, before the gate, is the direction, and chapter 10 says where the door for it stands. And the origin is what the proposal declares: chapter 8 said so, and it holds here.

## In your hands

Write three drafts the way an AI model might return them, each wrong in a different way: a point that does not exist, a value in the wrong form, and a line the split cannot read. Before you run them, write which check of the gate you expect to refuse each, or whether something refuses before the gate.

```haro exercise
for cD in [ "cap_mortgage = 0.16", "cap_school = sixteen", "set cap_school to 0.16" ]
	aP = Q(cD).Split(" = ")
	? @@( aP )
next
```

The third one is the defect I leave you. A draft the program cannot read never reaches the gate at all. What should happen to it: refused with a reason, sent back to the AI model, or shown to a person? Write the rule. It belongs before the gate, in the program that receives the draft; the next chapter names the door that would hold a draft to a grammar.

The AI model comes last, and its words are proposals. The next chapter is the surface those proposals are allowed to touch: the safest write surface a bank can hand an AI agent.
