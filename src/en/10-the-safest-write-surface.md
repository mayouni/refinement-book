---
id: the-safest-write-surface
part: 3
number: 10
title: The safest write surface
stage:
  built: "the declared change surface as the AI agent's map; a proposal outside it refused by name; a rehearsal on a copy of the refinable code that leaves the original untouched; the floor of trust per point"
  designed: "the door for AI agents, one command with rehearse and commit among its verbs, ratified on 2 October 2026 and not built; the live mode of Refine, in which a person refines from the running product (Part V)"
  absent: "a rehearsal carried to the original as one act: today a person or a program proposes again on the original what the copy admitted"
status: draft
research: research/ch10.md
guards: [refinablecode_narrated, refine_deepening_narrated, gate_deepening_narrated]
---

In this chapter I say what a bank can hand an AI agent when it lets one change its code. Not the file system: the declared points. I run the points as the AI agent's map, a proposal that steps off the map, and a rehearsal on a copy before anything touches the original. Then I say where the door for AI agents stands: decided, and not built.

## The field

When people picture "giving an AI write access", they picture the file system: an AI agent alone with the repository, able to edit anything, the way a contractor with a master key is alone with a building. The field's answers to that picture are real: a sandbox, a branch, a review before merge, a list of tools the AI agent may call. This is general knowledge, and each answer narrows what the AI agent can reach.

What they share is that the surface stays the file system, narrowed. The AI agent still writes text, and a person still reads the diff.

## The principle

**Hand an AI agent typed knobs, not your files: the declared points are its map, a typed proposal is its only pen, and the gate reads everything it writes.**

The Softanza book says the same thing at the scale of the world, in its chapter 20: do not build safe agents; build a safe world, and let ordinary agents loose inside it. This chapter is that sentence at the scale of one bank's code.

## The map

Run it, on the three products of chapter 9. The AI agent's first question is the one chapter 2 asked: where may this code be changed? The answer is the list it reads:

```haro
cBook = 'auto_loan   = <R:PARAM name="cap_auto" value="0.18" min="0.10" max="0.20">' + nl +
        'school_fees = <R:PARAM name="cap_school" value="0.18" min="0.10" max="0.20">' + nl +
        'harvest     = <R:PARAM name="cap_harvest" value="0.18" min="0.10" max="0.20">'
o = new stzRefinableCode(cBook)
? @@( o.RefinementPoints() )
#--> [ [ "cap_auto", "param", "0.18" ], [ "cap_school", "param", "0.18" ], [ "cap_harvest", "param", "0.18" ] ]
? o.Refine("interest_rate").As(:llm).To("0.05")[:why]
#--> structural: no refinement point 'interest_rate'
```

Three points, each with its name, kind and value; the bounds are in the tags the AI agent reads with them. And a proposal to the interest rate, which nobody declared as a point, is refused at the first check, by name. The AI agent did not have to be told not to touch the interest rate. The surface did not include it.

That is what makes the surface safe, and it is worth saying in the words of chapter 2. A proposal on this surface is validated, scoped, attributed and reversible by construction: it names a declared point, it has bounds that are law, it carries its origin, and it is recorded as a step that can be taken back. A bank can let an AI agent propose on it at any hour, because nothing it proposes lands without the gate, provided the program around the code gives the AI agent `Refine` and nothing else; the timeline's `Redo`, for one, re-applies a step without the gate.

## The rehearsal

Before a change touches the code, the AI agent, or the person reviewing it, may want to see what the gate would say. The library's refinable code is a value: assigning it makes a copy. So a rehearsal is a copy that takes the proposals, while the original waits:

```haro
o2 = new stzRefinableCode(cBook)
oTwin = o2
oTwin {
	? Refine("cap_auto").To("0.16")[:admitted]
	#--> 1
	? Refine("interest_rate").To("0.05")[:why]
	#--> structural: no refinement point 'interest_rate'
	? NumberOfSteps()
	#--> 1
}
? o2.NumberOfSteps()
#--> 0
? o2.ValueOf("cap_auto")
#--> 0.18
```

The twin took one change and refused one. The original has no step, and its cap is still `0.18`! Rehearse on what touches nothing, then commit through a governed actor: the Softanza book's chapter 24 makes that its first principle for files, processes and deployments, and here it is for one refinable code.

The commit, today, is to propose again on the original what the twin admitted. The gate judges it again, which is as it should be: the original may have moved since the rehearsal.

## The door, decided

How does an AI agent outside the program reach this surface? Through a door, and the door is decided. On 2 October 2026 the platform ratified one command for AI agents, with verbs that answer from the library and never from an AI model: ask, explain and howto, check, promise and guard, rehearse and commit, do, and grammar. The rehearse verb gives the change as a plan without touching the disk; the commit verb passes it through the gates, by someone entitled to commit. The grammar verb would hold an AI model's sentence to a declared language before it runs, which is the answer to the defect chapter 9 left you.

The door is ratified and not built. Today an AI agent reaches the refinable code through a program a team writes around it, the way this chapter's blocks do.

## What I refused

**I refused the file system as the AI agent's surface.** The fear of an AI agent with write access is a fear of the file system, and the answer is a smaller surface, not more courage. The declared points are the surface; everything else is a diff, and a person reviews it.

**I refused a door that thinks.** The verbs of the door answer from the library and the engine; the AI agent brings its AI model, and the platform brings the judgement. A door that asked an AI model whether to let a change through would put the guessing back where the gate took it out.

## The court

`refinablecode_narrated` asserts the declared points; `gate_deepening_narrated` asserts the refusal of a point that does not exist; `refine_deepening_narrated` asserts the floor of trust. The rehearsal on a copy ran above; no guard asserts that a copy leaves the original untouched.

## Where the field leads

The field leads in what its AI agents can reach and do today, through doors that are built: protocols by which tools and AI agents connect to a system, command lines, editor integrations. This is general knowledge. The platform's door is decided and not built; its application tier already serves a declared project to AI tools, read-only and audited, and until the door is built, an AI agent reaches the refinable code through a program someone writes.

The field also leads in the rehearsal of whole changes, as the field holds it: a branch, a preview environment, a plan for infrastructure. The rehearsal here is of a refinable code, one object, and the Softanza book's chapter 24 tells the larger twins that are built, of files and of the process environment.

## The limit

What is built: the declared points as the AI agent's map; a proposal off the map refused by name; a rehearsal on a copy that leaves the original as it was; the floor of trust per point. All of it ran above.

What is designed: the door, one command whose verbs include rehearse and commit, ratified on 2 October 2026; and the live mode of Refine, the product, in which a person refines a point from the running product's screen, which Part V tells as stage and direction.

What is absent: a rehearsal carried to the original as one act. The twin knows what it admitted; carrying those steps to the original, re-judged, is the commit verb's work, and the verb is not built.

## In your hands

Write the commit by hand. Take the twin's history, and propose each of its steps again on the original, in order, keeping the answers:

```haro exercise
for aStep in oTwin.History()
	? o2.Refine(aStep[1]).As(aStep[4]).To(aStep[3])[:why]
next
? o2.NumberOfSteps()
```

Then change the original between the rehearsal and the commit, a cap moved by someone else, say, and run your commit again. Which steps does the gate still admit? Should a commit that finds the original moved go on, stop at the first refusal, or refuse the whole plan? The door's commit verb will have to choose, and I leave the choice with you first.

Part III ends here. Part IV returns to Softibank, for the eighteen months between the letter and the auditor.
