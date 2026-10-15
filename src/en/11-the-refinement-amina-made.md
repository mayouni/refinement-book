---
id: the-refinement-amina-made
part: 4
number: 11
title: The refinement Amina made
stage:
  built: "a rule of the regulator declared as a point and refined under compliance authority; the code and the customer's letter held in one refinable text, tied by a rule; two actors with different permissions and authorities on one governed code; an order of refinements the gate enforces, step by step"
  designed: "several points refined together as one change, ordered by their dependencies (the planner of the architecture document)"
  absent: "the language's own parser judging the changed source (the structural stage delegated); points of the interface and the data world in their own structures, a direction of the Teaching Edition not in the library's design documents"
status: draft
research: research/ch11.md
guards: [gate_deepening_narrated]
---

In this chapter Part IV returns to Softibank. I take the letter of chapter 1 to its end: the change Amina's team made, as the library can carry it today. The rule of the regulator becomes a point of its own, refined by the compliance officer; the customer's letter is governed with the code; and the gate decides the order in which the changes may land. Then I show the change the gate cannot make one step at a time.

## The field

The field treats the crafts a regulatory change touches as separate worlds. Code is reviewed in one place, the wording of a customer letter in another, a report's columns in a third, each with its own tool and its own approval. This is general knowledge, and it follows the organisation chart. The change does not.

Amina's notebook said so in chapter 1. The cap fed the pricing, and it was written in the statements and the text messages that told customers what a late payment costs. A change to the code that left the letter at eighteen per cent would be a correct program and a wrong promise.

## The principle

**Declare the rule itself as a point, put what must agree under one gate, and let the gate decide the order in which the changes may land.**

The Teaching Edition said the deepest change was not to any pricing function: it was to the rule. This chapter runs that sentence.

## The rule, as a point

Run it. Three points in one refinable text: the cap the code charges, the maximum the regulation allows, and the rate the customer's letter states. Two rules tie them: the cap may not exceed the regulatory maximum, and the letter may not state less than the cap in force. Two actors act on it: the compliance officer, who alone may move the regulatory maximum, a risk of tier three; and the pricing agent, an AI agent with delegated authority over the cap and the letter.

```haro
cDoc = 'cap    = <R:PARAM name="penalty_cap" value="0.18" min="0.10" max="0.20">' + nl +
       'ceil   = <R:PARAM name="regulatory_max" value="0.18" min="0.10" max="0.20">' + nl +
       'letter = Late payments carry a penalty of <R:PARAM name="letter_rate" value="18" min="10" max="20"> per cent.'
b = new stzRefinableCode(cDoc)
b {
	SetGovernedBy(new stzGovernance("softibank"))

	# what must stay true
	DeclareDerivation("cap-within-regulation",
		func oC { return (0 + oC.ValueOf("penalty_cap")) <= (0 + oC.ValueOf("regulatory_max")) },
		"the cap may not exceed the regulatory maximum")
	DeclareDerivation("letter-covers-cap",
		func oC { return (0 + oC.ValueOf("letter_rate")) >= 100 * (0 + oC.ValueOf("penalty_cap")) },
		"the letter may not state less than the cap in force")

	# who may move what
	SetActor("compliance-officer")
	SetRiskFor("regulatory_max", 3).SetAllowRefine("regulatory_max").SetAuthorityLevel(:Autonomous)
	SetActor("pricing-agent")
	SetRiskFor("penalty_cap", 2).SetRiskFor("letter_rate", 1)
	SetAllowRefine("penalty_cap").SetAllowRefine("letter_rate").SetAuthorityLevel(:Delegated)

	? NumberOfPoints()
	#--> 3
	? NumberOfDerivations()
	#--> 2
}
```

Three points, two rules, two actors. The letter is not code, and the library does not mind. A refinable text is any text with tags in it; the letter's rate is a point like the cap, with bounds of its own. That is what the Teaching Edition called one gate, many worlds, at the size the library has it today: one text, where code and wording sit together under one set of rules.

## The order the gate enforces

Now the change. The pricing agent starts with the letter, since the letter is what customers read:

```haro
b {
	? Refine("letter_rate").To("16")[:why]
	#--> derivation: rule 'letter-covers-cap' violated -- the letter may not state less than the cap in force
	? Refine("penalty_cap").To("0.16")[:why]
	#--> admitted: 'penalty_cap' 0.18 -> 0.16 [:trusted] (structural + constraint + derivation + governance + trust passed)
	? Refine("letter_rate").To("16")[:why]
	#--> admitted: 'letter_rate' 18 -> 16 [:trusted] (structural + constraint + derivation + governance + trust passed)
	? Refine("regulatory_max").To("0.16")[:why]
	#--> governance: refused: 'pricing-agent' lacks PERMISSION (can) for 'refine-regulatory_max'
	SetActor("compliance-officer")
	? Refine("regulatory_max").To("0.16")[:why]
	#--> admitted: 'regulatory_max' 0.18 -> 0.16 [:trusted] (structural + constraint + derivation + governance + trust passed)
}
```

Five proposals, and the rules wrote the order; the gate enforced it. The letter could not go first: for a moment the bank would have charged eighteen per cent while telling customers sixteen, and the rule refused that moment. The cap went first, then the letter. The pricing agent could not move the regulation, because it holds no permission for it; the compliance officer could, last, when nothing in the code still exceeded the new maximum. The Teaching Edition told the rule moving first and the code following it; with these rules, the library lets the rule move only once the code is already under it.

Read the rules again, and see what they encode. The letter may state more than the cap for the length of one step, which is the safe direction: a customer is charged less than the letter says. It may never state less. Nobody had to remember that order. It was declared once, and every proposal met it.

## The change it cannot make one step at a time

Suppose the bank had declared the letter's rule as an equality, the letter states exactly the cap:

```haro
c = new stzRefinableCode(cDoc)
c.DeclareDerivation("letter-matches-cap",
	func oC { return (0 + oC.ValueOf("letter_rate")) = 100 * (0 + oC.ValueOf("penalty_cap")) },
	"the letter must state the cap in force")
? c.Refine("penalty_cap").To("0.16")[:why]
#--> derivation: rule 'letter-matches-cap' violated -- the letter must state the cap in force
? c.Refine("letter_rate").To("16")[:why]
#--> derivation: rule 'letter-matches-cap' violated -- the letter must state the cap in force
```

Neither can move first, so neither moves at all! The rule is right, and the gate keeps it at every step, and a change that needs two points to move together has no step in which the rule holds. The library judges one point at a time. A change of several points as one, ordered by what depends on what, is what the architecture document calls the planner; it is designed.

## Many languages

Softibank's code is not one language, and neither is a bank's anywhere. The Teaching Edition promised that each language would be the authority on its own structure: its own parser would read a file and judge the changed one. The library's refinable code reads tags in any text, so the gate above works on any text with tags in it. The tags stay in the text, so a tagged file is not valid source in its own language until it is rendered without them, which chapter 4 named as absent. What it does not do is ask that language whether the changed file still parses; chapter 5 named that as absent. My Softanza book tells, in its chapters 11 to 16, how the platform declares and closes languages, and which run at this commit.

## What I refused

**I refused separate gates for code and for wording.** The letter and the cap are judged by one gate, under one rule that ties them, because the customer meets them together.

**I refused to let the regulation be a constant.** The regulatory maximum is a point with its own risk and its own actor. When the next letter comes, the rule moves under compliance authority, and the gate checks every rule declared on it.

## The court

`gate_deepening_narrated`, in the library's `base/test/refine/`, asserts the rule across points that refuses and rolls back, governance by authority against a risk, and the refusal of an undeclared risk. No guard asserts a refusal for a missing permission, two actors on one governed code, the order the rules impose, or the equality that cannot be moved; the blocks above are their run.

## Where the field leads

The field leads in each world. Design systems hold tokens and wording with their own tools; data teams hold schemas and checks with theirs; each is mature, and none of this is the library's. The library's refinable code puts them under one gate only when they are written as one tagged text, as the letter was here. Points of the interface and of the data world, held in their own structures and judged by the same gate, are the Teaching Edition's direction; the library's design documents do not hold them yet.

## The limit

What is built: a regulator's rule as a point under compliance authority; code and letter in one refinable text tied by a rule; two actors with different permissions on one governed code; the order of changes the rules impose, enforced step by step. All of it ran above.

What is designed: several points refined as one change, ordered by their dependencies; the equality showed what its absence costs today.

What is absent: the language's own parser as the structural check; and points of the interface and the data world in their own structures, the Teaching Edition's direction.

## In your hands

The equality is the defect I leave you. The bank wants the letter to state exactly the cap in force, and the gate cannot move them one at a time. Find a way through with what is built: a different rule, a different order, a third point. Then say what each way costs.

```haro exercise
c2 = new stzRefinableCode(cDoc)
c2.DeclareDerivation("letter-matches-cap",
	func oC { return (0 + oC.ValueOf("letter_rate")) = 100 * (0 + oC.ValueOf("penalty_cap")) },
	"the letter must state the cap in force")
# your way through, here
? c2.ValueOf("penalty_cap")
? c2.ValueOf("letter_rate")
```

One way starts a new object without the rule, and an auditor will ask about that moment. Another writes a looser rule, as the bank did above. I do not know a way that keeps the equality with what is built today; if you find one, it is the specification of the planner.

The change is made, in the order the rules allowed. Eighteen months later, someone from outside asks the bank to prove it.
