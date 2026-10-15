---
id: the-timeline
part: 2
number: 7
title: The timeline
stage:
  built: "every admitted proposal recorded as a step with the value it replaced and its origin; revert by one step, to a step, to a named checkpoint and to zero; redo, cleared when the timeline forks; under governance, a decision recorded with its actor, authority, risk and time"
  designed: "the refinement as a typed transformation of the code graph, its inverse a graph event; the step carrying its cascade, author, verification and history"
  absent: "a saved timeline: the file holds the source; a time and an actor on the step itself; a revert judged by the gate and recorded under governance; the two clocks of a rule, in force and recorded"
status: draft
research: research/ch07.md
guards: [refine_deepening_narrated, refinablecode_narrated]
---

In this chapter I run what happens after a change lands: the timeline. I take a step back, rewind to a named checkpoint, go forward again, and fork the timeline so that the way forward closes. Then I say what the timeline keeps, what it does not keep yet, and where the record a bank needs lives today.

## The field

The field's way back is the revert commit: a new change that undoes an old one. Version control makes it easy to write, and, as the Teaching Edition of this book put it, undoing a landed change is often a small project of its own: the system moved on after the old change, other changes grew around it, and the revert is a new change written under pressure, reviewed as one.

A rollback of a deployment is faster, and it takes back everything that release carried, not one change.

## The principle

**A change keeps its own way back, recorded when it lands, and taking it back is one act.**

A refinement is typed: the cap went from `0.18` to `0.16`. Its inverse is known the moment it lands: from `0.16` back to `0.18`. The step keeps it.

## Steps, and a checkpoint

Run it. The cap goes through two changes, an interim value first, say; between them the bank files its compliance position, and the team marks that moment on the timeline:

```haro
t = new stzRefinableCode('cap = <R:PARAM name="penalty_cap" value="0.18" min="0.10" max="0.20">')
t {
	Refine("penalty_cap").To("0.17")
	Checkpoint("filed")
	Refine("penalty_cap").To("0.16")
	? NumberOfSteps()
	#--> 2
	? @@( History() )
	#--> [ [ "penalty_cap", "0.18", "0.17", "trusted" ], [ "penalty_cap", "0.17", "0.16", "trusted" ] ]
}
```

Two steps, each with the point, the value it replaced, the value it set and its origin. The checkpoint `filed` marks the timeline after the first.

## The way back

Now take a step back, then go forward again:

```haro
t {
	Revert()
	? ValueOf("penalty_cap")
	#--> 0.17
	? CanRedo()
	#--> 1
	Redo()
	? ValueOf("penalty_cap")
	#--> 0.16
	RevertToCheckpoint("filed")
	? ValueOf("penalty_cap")
	#--> 0.17
	? Why()
	#--> reverted 1 step(s) -> timeline at 1
}
```

One step back, `0.17`; forward again, `0.16`; back to what was filed, `0.17`, and the answer says how far it went: one step, to a timeline of one. No counter-edit was written. The way back was in the step.

## The fork

What happens to the way forward when, from a step back, a new change lands?

```haro
t {
	? CanRedo()
	#--> 1
	Refine("penalty_cap").To("0.15")
	? CanRedo()
	#--> 0
	? @@( History() )
	#--> [ [ "penalty_cap", "0.18", "0.17", "trusted" ], [ "penalty_cap", "0.17", "0.15", "trusted" ] ]
}
```

The step to `0.16` could be redone a moment ago. Then a new proposal was admitted from the checkpoint, and the redo is gone: the timeline forked, and the other branch closed. The history reads as what happened on the branch that stands. That is the ordinary rule of undo and redo, and the library keeps it.

And a checkpoint nobody marked?

```haro
try
	t.RevertToCheckpoint("approved")
catch
	? cCatchError
done
#--> No checkpoint 'approved'.
```

It refuses, by name.

## What the timeline keeps

Read the history once more: point, value before, value after, origin. Four things per step. What it does not keep is as plain: no time, no actor, no reason. The step does not say when it landed, who proposed it, or why it was admitted.

When the code is governed, as in chapter 5, there is a second record, and it keeps more. Each admitted refinement becomes a decision of the governance, with an id, a rationale that names the origin, the actor, the authority the actor held at that moment, the risk tier of the action, a time and the action itself. Chapter 8 runs it. So today the record a bank needs is in two places: the timeline of the code, which can go back, and the lineage of the governance, which says who and when.

## What I refused

**I refused the counter-edit as the way back.** A revert here is the stored inverse applied as one act, not a new change written to cancel an old one. Its value was judged when the step landed. The revert itself is not judged: it passes no gate and, under governance, records no decision; that is in the limit.

**I refused a single undo button.** A bank needs to go back to what was filed, not only one step; the checkpoint is a named moment, and `RevertTo(0)` returns to the source as it was declared.

## The court

`refine_deepening_narrated`, in the library's `base/test/refine/`, asserts the timeline: steps, revert to a step, checkpoints, redo and the fork that clears it. `refinablecode_narrated` asserts the single revert and the saved file.

## Where the field leads

The field leads in memory. Version control keeps every change on disk, on every clone, with its author, its time and its message; this is general knowledge. The timeline of this chapter lives in the running object: when the program that holds it ends, the timeline ends with it. The library saves the source with its current values, in a file with the suffix `.zrfn`, and the steps are not in it.

The Teaching Edition of this book told of two clocks on every record: when a rule was in force, and when the system recorded it. That is how an auditor's question "as of May: what was in force, and what did your system believe?" gets an answer. The library's refinement does not carry it, and neither does its architecture document; the governance lineage carries one time, the moment of the decision.

## The limit

What is built: the step with its prior value and its origin; revert by one, to a step, to a checkpoint and to zero; redo, and the fork that clears it; under governance, a decision with its actor, authority, risk and time. All of it ran above, runs in chapter 8, or is asserted by `refine_deepening_narrated` (the revert to a step and to zero).

What is designed: the refinement as a typed transformation of the code graph, carrying its cascade, its author, its verification and its history, with its inverse as a graph event; the architecture document describes it.

What is absent, and next: a saved timeline, so that the way back survives the program; a time and an actor on the step itself; a revert that passes the gate and is recorded as a decision under governance; and the two clocks of a rule.

## In your hands

The saved file is the defect I leave you. Save the refinable code, read the file back into a new object, and ask it for its history:

```haro exercise
cFile = t.Save("cap_timeline")
t2 = new stzRefinableCode(read(cFile))
? t2.ValueOf("penalty_cap")
? t2.NumberOfSteps()
? t2.CanRevert()
```

Before you run it, write what you expect each line to print. The value comes back. What else does? When you have the answer, write the fields a saved step would need for chapter 12's auditor, and mark those the step does not have today.

The timeline says what changed and how to go back. The next chapter is about who may change, and from where: trust and governance.
