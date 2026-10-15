---
id: the-gate
part: 2
number: 5
title: The gate
stage:
  built: "the gate of five checks in the order the code runs them: structural, constraint, governance, trust, derivation; a refusal that names its check and leaves the source whole; a rule across points judged on the state the change would produce, and rolled back"
  designed: "the gate composed from the code graph's rules (stzGraphRule), so that a change is judged against what it reaches and not only against its point"
  absent: "a check that the language itself still parses the changed source; the admitted message printing the checks in the order they ran"
status: draft
research: research/ch05.md
guards: [gate_deepening_narrated, refine_deepening_narrated, refinablecode_narrated]
---

In this chapter I run the gate whole. Five checks stand between a proposal and the code, and I make each one refuse in turn, on one governed configuration, in the order the code runs them. Then I say what the gate's answers are made of, why the same proposal always meets the same verdict, and where the order the gate prints differs from the order it runs.

## The field

The field has gates, and good ones. A build refuses code that does not compile; a test suite refuses a change that breaks an assertion; an admission controller refuses a request a cluster's policy forbids. All of this is general knowledge. Each gate answers one question, and a change passes through several of them, run by different tools at different moments.

What the field rarely has is one gate that knows the place being changed: its bounds, who may change it, from which origin, and what must stay true around it. That knowledge exists, in the heads of people like Fatou, the bank's compliance officer, who know why a rule holds. The gate of this chapter is where it is written down.

## The principle

**One gate, every proposal, the same checks in the same order, and a refusal that says which check refused and why.**

It does not matter whether the proposal comes from Amina, from a script or from an AI agent. Chapter 3 said the gate judges proposals and not authors; this chapter shows what judging means.

## Five refusals

Run it. Here is the cap and, beside it, a floor below which the cap may not fall, one the bank's risk committee sets; both are declared as points. The code is governed: an AI agent acts on it as the actor `pricing-agent`, with delegated authority, and the cap's refinement is a risk of tier two. A floor of trust is set on the cap, and a rule across the two points says the cap may not fall below the floor.

```haro
g = new stzRefinableCode('cap   = <R:PARAM name="penalty_cap" value="0.18" min="0.10" max="0.20">' + nl +
                         'floor = <R:PARAM name="policy_floor" value="0.12" min="0" max="0.20">')
g {
	# who acts, at what risk, from which origin
	SetGovernedBy(new stzGovernance("credit-ops")).SetActor("pricing-agent")
	SetRiskFor("penalty_cap", 2).SetAllowRefine("penalty_cap").SetAuthorityLevel(:Delegated)
	TrustFloor("penalty_cap", :external)

	# what must stay true across the two points
	DeclareDerivation("cap-above-floor",
		func oC { return (0 + oC.ValueOf("penalty_cap")) >= (0 + oC.ValueOf("policy_floor")) },
		"the cap may not fall below the policy floor")

	# five proposals, one for each check
	? Refine("ghost").To("1")[:why]
	#--> structural: no refinement point 'ghost'
	? Refine("penalty_cap").To("0.25")[:why]
	#--> constraint: 0.25 above max 0.20
	? Refine("policy_floor").To("0.1")[:why]
	#--> governance: refused: 'refine-policy_floor' has NO declared risk tier (undeclared actions never proceed)
	? Refine("penalty_cap").As(:llm).To("0.11")[:why]
	#--> trust: posture :llm below the required floor for 'penalty_cap'
	? Refine("penalty_cap").As(:external).To("0.11")[:why]
	#--> derivation: rule 'cap-above-floor' violated -- the cap may not fall below the policy floor
	? ValueOf("penalty_cap")
	#--> 0.18
}
```

Five proposals, five refusals, each naming its check first. And the cap is still `0.18`!

Read them in order, because the order is the code's.

**Structural.** Does the point exist? `ghost` does not, and the proposal stops before anything else is asked.

**Constraint.** Is the value within what the point declares? Twenty-five per cent is above the cap's own ceiling.

**Governance.** May this actor turn this knob? The code is governed, so every point is a governed action, and the floor's refinement was never given a risk tier. An action with no declared risk never proceeds. The refusal is not about the value at all: nobody said what changing the floor would risk, so nobody may change it.

**Trust.** Does the origin clear the point's floor? A proposal declared as composed by an AI model, `:llm`, is below the floor of `:external` set on the cap.

**Derivation.** Does what must stay true around the point still hold? Eleven per cent is inside the cap's bounds, from an origin that clears the floor, by an actor allowed to change it, and it would put the cap below the policy floor. The gate applied it tentatively, judged the rule on the state it would produce, found it false, and put the value back.

## The verdict that lands

And a proposal that clears all five?

```haro
? g.Refine("penalty_cap").As(:external).To("0.16")[:why]
#--> admitted: 'penalty_cap' 0.18 -> 0.16 [:external] (structural + constraint + derivation + governance + trust passed)
? g.ValueOf("penalty_cap")
#--> 0.16
```

Admitted, with the value before and after and the origin. Look at the order of the checks in that message: structural, constraint, derivation, governance, trust. It is not the order the code ran them, which you just watched: governance and trust come before derivation. The message lists the five; the refusals above are the order. I report what runs.

The order is not an accident of the code. Governance and trust are asked before anything is applied, because they judge who and from where, and those need no tentative value. Derivation is asked last, because it judges the state the change would produce, and that state must exist, for a moment, to be judged. So the only check that ever touches the value before admitting it is the last one, and it puts the value back when it refuses.

## The four of the design

My design of the gate had four stages: structural, constraint, derivation, governance. The library's architecture document still lists those four, in that order. The code has five, because a check of the origin's trust was added beside governance, and the code numbers it 4b. Softanza's chapter 10 says it in one line: I wrote the design with four stages, and the code has five checks. This book reports the five.

## Deterministic

The same proposal, against the same declarations, meets the same verdict, provided the declared rules are plain comparisons, as they are here. Nothing in the gate draws at random or asks an AI model; the checks compare a value with bounds, a name with a list, an authority with a tier, a posture with a floor, and run the rules a person declared. Whatever else in a bank's software is probabilistic, the moment of admission is not, and an auditor can replay it, given the declarations. `Save` does not keep the risk tiers, floors and rules today, so they must be kept with the code.

That is also the gate's honest edge. It proves a change against what was declared. A rule nobody wrote down is not checked, and a change can pass all five checks and still be a poor idea. The gate does not replace judgement; it spends it where it is needed, on the declarations.

## What I refused

**I refused a gate that asks an AI model.** A verdict that could differ after lunch cannot be replayed for an auditor. The checks are plain comparisons and declared rules.

**I refused a gate that half-lands.** A refusal at any of the five checks leaves the source as it was; the one check that applies a value first takes it back when it refuses. There is nothing to clean up after a refusal.

## The court

`gate_deepening_narrated` asserts the derivation rule that refuses and rolls back, the governed refusal before any change, the refusal of a point with no declared risk, and the checks composed on one configuration, the structural refusal of an unknown point among them. `refine_deepening_narrated` asserts the trust floor; `refinablecode_narrated` asserts the constraint refusals. All three are in the library's `base/test/refine/` at the commit this book is pinned to.

## Where the field leads

The field's gates lead in what they check. A compiler checks that the code still parses; a test suite checks behaviour the change may break three modules away. This gate checks a value at a declared point, the actor, the origin and the rules declared across points. It does not ask the language whether the changed source still parses, and it does not run the tests that cover the line. Teams keep their builds and their suites, and this gate stands in front of them.

## The limit

What is built: the five checks, in the order the code runs them; a refusal that names its check and its reason; a rule across points judged on the state the change would produce, and rolled back; governance and trust that refuse before anything is applied. All of it ran above.

What is designed: the gate composed from the rules of the code graph, so that a change is judged against what it reaches beyond its line; the architecture document describes it.

What is absent: a check that the language still parses the changed source; and an admitted message that prints the checks in the order they ran, a change of one line in the library.

## In your hands

A rule of the kind Fatou would write is the one I leave you. Declare a second rule across the points: the bank's risk committee wants the cap never below fourteen per cent, say. Then propose eleven per cent, which breaks both rules. Before you run it, write which rule the refusal will name.

```haro exercise
g.DeclareDerivation("cap-committee-minimum",
	func oC { return (0 + oC.ValueOf("penalty_cap")) >= 0.14 },
	"the cap may not fall below the committee's minimum")
? g.Refine("penalty_cap").As(:external).To("0.11")[:why]
```

Read the refusal, then read the code of the gate and find how it chooses. Then ask yourself whether the order in which rules were declared should decide which one a refusal names, or whether a refusal should name every rule it breaks. A compliance officer reading the refusal would want one of the two answers, and I leave the choice open.

The gate judged a change against its point and its rules. The next chapter asks what the change reaches: the cascade, which a reviewer reads instead of the diff.
