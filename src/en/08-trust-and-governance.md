---
id: trust-and-governance
part: 2
number: 8
title: Trust and governance
stage:
  built: "four postures of origin ranked from trusted to an AI model's; a floor of trust per point; governance by permission, authority and declared risk, decided before any change; a lineage of decisions with actor, authority and risk at the time, a time and the action, queried by actor"
  designed: "the refinement carrying its author and verification as a typed transformation of the code graph (the architecture document)"
  absent: "an origin proven rather than declared: the posture is what the proposal says it is; an unknown origin refused or ranked lowest (requested, RL-04)"
status: draft
research: research/ch08.md
guards: [refine_deepening_narrated, gate_deepening_narrated]
---

In this chapter I run the two checks of the gate that ask who and from where. Trust asks from which origin a proposal comes and whether that origin clears the point's floor. Governance asks whether this actor may turn this knob, at the risk declared for it. I run both, I read the record governance keeps, and I say what an origin is today: a declaration, not a proof.

## The field

The field governs who may change code with permissions: who may push to a branch, who must approve a path, which service account may deploy. It governs AI agents with a different set of tools: what an AI agent is allowed to call, a sandbox around what it runs, a person who confirms before it acts. All of this is general knowledge.

Two questions are often mixed in it. Who is acting? And where did the change come from? A person may paste a change an AI model wrote; an AI agent may act under a person's account. Permissions answer the first question. The second is rarely asked of the change itself.

## The principle

**Ask who may turn the knob, and ask where the turn came from, as two separate questions, before anything changes.**

The library's own comment says it in three words: origin is not identity. Governance judges the actor. Trust judges the origin.

## The floor of trust

Every proposal carries a posture: where it came from. The library ranks four, from most trusted to least: `trusted`, `external`, `sandboxed` and `llm`, a proposal composed by an AI model. A proposal is `trusted` unless it says otherwise. A point may set a floor.

Run it. The cap gets a floor of `external`:

```haro
p = new stzRefinableCode('cap = <R:PARAM name="penalty_cap" value="0.18" min="0.10" max="0.20">')
p {
	TrustFloor("penalty_cap", :external)
	? Refine("penalty_cap").As(:sandboxed).To("0.16")[:why]
	#--> trust: posture :sandboxed below the required floor for 'penalty_cap'
	? Refine("penalty_cap").As(:llm).To("0.16")[:why]
	#--> trust: posture :llm below the required floor for 'penalty_cap'
	? Refine("penalty_cap").As(:external).To("0.16")[:admitted]
	#--> 1
	? PostureOf(1)
	#--> external
}
```

A proposal from a sandboxed run is refused, and one composed by an AI model is refused. A proposal from an external tool clears the floor, and the step records it: `external`.

This is the check that lets a bank say: a proposal declared as composed by an AI model may change the display text of a statement, and may not change the penalty cap, without saying anything about any person. The floor is on the knob, not on the people.

## An origin it does not know

Now a posture the library was never told about:

```haro
? p.Refine("penalty_cap").As(:auditor).To("0.15")[:why]
#--> admitted: 'penalty_cap' 0.16 -> 0.15 [:auditor] (structural + constraint + derivation + governance + trust passed)
```

Admitted! (The message lists the five checks as fixed text; here only the floor of trust had anything to judge.) `:auditor` is not one of the four, and an origin the library does not know is ranked as trusted, the top. The library's comment says why: an explicit posture opts in. I read it the other way for a bank. A floor exists to refuse what it does not recognise, and an unknown origin that clears the highest floor is the gap of this chapter. It is a one-line change; the book has written the request (RL-04), and the library's session has not yet received it.

## Governance

Trust judged the origin. Governance judges the actor, and it has three parts: a permission (may this actor refine this point at all), an authority level (how far this actor's judgement is trusted), and a risk tier declared for the action. An actor proceeds only when it holds the permission and its authority covers the risk.

```haro
gv = new stzRefinableCode('cap = <R:PARAM name="penalty_cap" value="0.18" min="0.10" max="0.20">')
gv {
	SetGovernedBy(new stzGovernance("credit-ops")).SetActor("pricing-agent")
	SetRiskFor("penalty_cap", 3).SetAllowRefine("penalty_cap").SetAuthorityLevel(:Delegated)
	? Refine("penalty_cap").To("0.16")[:why]
	#--> governance: refused: 'pricing-agent' holds 'delegated' authority (level 2) but 'refine-penalty_cap' is risk tier 3 (SHOULD does not cover it)
	? ValueOf("penalty_cap")
	#--> 0.18
	SetAuthorityLevel(:Autonomous)
	? Refine("penalty_cap").To("0.16")[:admitted]
	#--> 1
}
```

The pricing agent, an AI agent acting under the name `pricing-agent`, holds the permission and a delegated authority, level 2, and the cap's refinement is a risk of tier 3. Refused, before anything changed; the cap is still `0.18`. Raised to autonomous authority, level 3, the same proposal is admitted.

The four levels are advisory, delegated, autonomous and emergency override. A risk tier nobody declared refuses every actor, as chapter 5 ran: what nobody judged, nobody may change.

## The record governance keeps

The timeline of chapter 7 keeps the value and the origin. Governance keeps the decision:

```haro
gq = gv.GovernanceQ()
? gq.NumberOfDecisions()
#--> 1
aD = gq.DecisionsOf("pricing-agent")[1]
? aD[:actor]
#--> pricing-agent
? aD[:authorityAtTime]
#--> autonomous
? aD[:riskAtTime]
#--> 3
? aD[:action]
#--> refine-penalty_cap
```

One decision, and it is the one that landed: the refused proposal changed nothing and recorded nothing. It names the actor, the authority it held at that moment, `autonomous`, the risk of the action, and the action; it also keeps an id and a rationale that names the origin of the proposal. It also carries a time, read from the clock when it was decided, which I do not print because it changes at every run. The lineage can be asked by actor, as here, by action, or by a span of time.

The authority is recorded as it was, not as it is. If the pricing agent's authority is lowered tomorrow, this decision still says it was autonomous when it decided. That is what an auditor needs: what the actor was allowed to do at the time it did it.

## What I refused

**I refused to judge the intelligence.** Neither check asks whether an AI model is good. Trust asks where a proposal came from; governance asks whether the actor's authority covers the declared risk. Both hold whatever AI model comes next.

**I refused to mix the actor and the origin.** A trusted person pasting what an AI model wrote may declare the origin as `llm`, and the floor refuses it, though the person's authority would allow it. One check would have to choose between them; two checks answer both.

## The court

`refine_deepening_narrated`, in the library's `base/test/refine/`, asserts the postures recorded on steps and the floor that refuses a lower origin while admitting a trusted one. `gate_deepening_narrated` asserts the governed refusal before any change, the admission after escalation with at least one decision in its lineage, and the refusal of an action with no declared risk. No guard reads the fields of a decision; the record block above is their only run here.

## Where the field leads

The field leads in identity. Its permissions rest on accounts that are authenticated: a signed commit, a token, a single sign-on. The library's governance takes the actor's name as given, and the posture is what the proposal declares. Whoever runs the gate must make sure the name and the posture are true, and today that is the program around the library, not the library.

The field also leads in breadth for AI agents: sandboxes that limit what an AI agent can touch at all, whatever it proposes. The floor of trust is narrower and sharper: it governs one knob, by origin.

## The limit

What is built: the four postures and their ranks; the floor of trust per point; governance by permission, authority and declared risk, decided before any change; the lineage of decisions with the actor, the authority and risk at the time, a time and the action, asked by actor, action or time. All of it ran above, except the queries by action and by time.

What is designed: the refinement as a typed transformation of the code graph, carrying its author and its verification, in the architecture document.

What is absent: an origin the library does not know, refused or ranked lowest; the book has written the request (RL-04). And an origin proven rather than declared. A proposal says `As(:external)`, and the library believes it; proving where a proposal came from is the work of the program that receives it, and Part III is about that program.

## In your hands

Give the pricing agent permission on the cap and nothing on the grace period, and declare a risk for both. Then propose a change to each, and before you run it, write which part of governance refuses the second: the risk, the permission or the authority.

```haro exercise
h = new stzRefinableCode('cap   = <R:PARAM name="penalty_cap" value="0.18" min="0.10" max="0.20">' + nl +
                         'grace = <R:PARAM name="grace_days" value="5" min="0" max="15">')
h.SetGovernedBy(new stzGovernance("credit-ops-2")).SetActor("pricing-agent")
h.SetRiskFor("penalty_cap", 1).SetRiskFor("grace_days", 1)
h.SetAllowRefine("penalty_cap").SetAuthorityLevel(:Delegated)
? h.Refine("grace_days").To("7")[:why]
```

Then decide whether the refusal says enough for the AI agent to correct its proposal without asking a person. If it does not, write the sentence it should say. That sentence is a specification.

Part II ends here: the point, the gate, the cascade, the timeline, and the trust that decides who and from where. Part III opens the door to the author everyone is asking about: the AI agent, at the point.
