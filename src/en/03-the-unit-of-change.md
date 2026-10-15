---
id: the-unit-of-change
part: 1
number: 3
title: The unit of change
stage:
  built: "the refinement as a typed proposal to a declared point; three kinds of point judged against their declaration (a parameter, an algorithm, a library; the library kind run here and not yet guarded); every admitted proposal recorded as a step with its prior value"
  designed: "the point and the refinement as classes of their own (stzRefinementPoint, stzRefinement); points of eight kinds (parameter, block, algorithm, function, pipeline, variable type, library, custom)"
  absent: "a check for a point of another kind, a block of code for instance: it parses and passes without one"
status: draft
research: research/ch03.md
guards: [refinablecode_narrated]
---

In this chapter I say why the unit of change had to change, from the line to the diff to the refinement. I show the diff's blind spot by running it: a change of text that the gate never sees. Then I show what the refinement carries instead, and I name the three kinds of point the library judges today.

## The field

Every era of programming has had a unit of work: the thing you make, review and talk about. For decades the unit was the **line of code**. Version control raised it to the **diff**: the set of lines that changed, which can be stored, compared, shared and argued over. The diff is one of the good inventions of software, and this is general knowledge.

Chapter 2 named its limit. A diff records which characters moved. It says nothing of what a trusting person needs: whether the place was meant to change, how far it may change, who proposed it, and how to take it back.

## The principle

**A refinement is a change to code that was declared to be changeable, proposed in a typed form, judged by a gate, recorded as a step, and reversible.**

Five clauses, and each one does work. They are not chapter 2's five properties; they are what a change must be for it to carry them. *Declared* means the code says in advance where it may change. *Typed* means the change has a kind and a shape: set this parameter to this value, choose this algorithm, not "here are some new characters". *Judged* means it passes or fails before it lands, with a reason. *Recorded* means it becomes a step in a timeline. *Reversible* means the step keeps what it replaced.

The definition is the one my Softanza book gives, and the library carries all five clauses. Run it.

## The edit the gate never sees

Start with the old unit. Take the late-fee line of chapter 1 and change it as text, the way a patch changes it, with the same slip of the fingers:

```haro
cSrc = 'penalty = balance * <R:PARAM name="penalty_cap" value="0.18" min="0.10" max="0.20">'
cPatched = substr(cSrc, '"0.18"', '"0.61"')
o = new stzRefinableCode(cPatched)
? o.ValueOf("penalty_cap")
#--> 0.61
? o.NumberOfSteps()
#--> 0
```

The point now holds `0.61`, three times the ceiling it declares, and nothing refused it! The timeline is empty: as far as the library knows, nothing was ever changed. A text edit does not pass through the gate, the judge of chapter 1, because the gate judges proposals and a patch is not one.

That is the diff's blind spot, run. The bounds were in the code, written next to the value, and the edit walked past them. A reviewer might have caught it. The code could not, because the change did not arrive in a form the code could judge.

## The same change, typed

Now the new unit. The same slip, proposed to the point instead of written into the text:

```haro
o2 = new stzRefinableCode(cSrc)
r = o2.Refine("penalty_cap").To("0.61")
? r[:why]
#--> constraint: 0.61 above max 0.20
? o2.Refine("penalty_cap").To("0.16")[:admitted]
#--> 1
? @@( o2.History() )
#--> [ [ "penalty_cap", "0.18", "0.16", "trusted" ] ]
```

The slip is refused with its reason; the intended change is admitted; and the step is recorded with the value it replaced, `0.18`, the value it set, `0.16`, and its origin. The two changes looked the same as text. As proposals, one is a refusal and one is a step.

That is the whole difference between the units. The diff is what the code looks like after a change. The refinement is the change itself, in a form the code can judge, record and take back.

## Three kinds, judged

A point has a kind, and the kind says what a proposal to it must respect. The library judges three kinds against their declaration: a parameter against its bounds, and an algorithm or a library against its list of options.

```haro
cMix = 'rounding = <R:ALGO name="rounding" value="half_up" options="half_up|bankers">' + nl +
       'pdf = <R:LIB name="statements" value="engine_a" options="engine_a|engine_b">'
m = new stzRefinableCode(cMix)
? @@( m.RefinementPoints() )
#--> [ [ "rounding", "algo", "half_up" ], [ "statements", "lib", "engine_a" ] ]
? m.Refine("rounding").To("truncate")[:why]
#--> constraint: 'truncate' not in options half_up|bankers
? m.Refine("statements").To("engine_b")[:admitted]
#--> 1
```

The rounding rule may be `half_up` or `bankers`, and nothing else; a proposal of `truncate` is refused by name. The library that prints the customer statements may be swapped between the two declared engines, and the swap is admitted. In each case the point says what it may become, and the gate holds it to that.

A bank changes more than numbers. Swapping a rounding rule across a bank's products would be a change a regulator may ask about, and here it is a typed proposal like the cap.

## What I refused

**I refused to make the refinement a new kind of file.** The point lives in the code, as a tag next to the value it governs. A programmer reading the line sees the knob, its value and its bounds in one place, kept in the tag and not in a side file that can drift from the code. What a point needs beyond its bounds, its floor of trust and the rules across points, is declared in the program, and Part II declares it.

**I refused to forbid the text edit.** Files remain files, and an emergency remains an emergency. The block above shows what a text edit does: it changes the code without a step. The discipline does not pretend that cannot happen; it makes the governed path the one that carries a reason, a record and a way back, and leaves the other path visible as what it is.

## The court

`refinablecode_narrated`, in the library's `base/test/refine/`, asserts two points declared, the parameter with its kind, a proposal admitted, and the refusals of a value out of bounds and of an option not declared, the first leaving the source as it was. No guard yet covers a library point; the block above is its only run here.

## Where the field leads

The field leads in what a change may be. A diff can change anything: a function, a class, a whole file, a comment. A refinement changes the value of a declared point, and today the library judges three kinds of point. Changing the structure of the code itself, adding a function or a product, is not a refinement today; it is still a diff, reviewed as one. Points of a block or a function kind are designed, and the limit says where they stand.

## The limit

What is built: the refinement as a typed proposal to a declared point; a parameter judged against its bounds, an algorithm and a library against their options; every admitted proposal recorded as a step with the value it replaced. All of it ran above.

What is designed: the point and the refinement as classes of their own, named in the library's architecture document (`stzRefinementPoint`, `stzRefinement`), and points of eight kinds: parameter, block, algorithm, function, pipeline, variable type, library and custom.

What is absent: a check for a point of any other kind. A point tagged as a block of code, for instance, parses and is listed, and a proposal to it passes the constraint check without one, because the library checks three kinds. Checks for the other kinds are the next step. And the gate judges proposals, not the code as it stands: a text edit that set a value out of bounds, as above, is not flagged when the code is read again, and a later step records it as the value to return to. One more: a value that is not a number, proposed to a bounded parameter, stops the program with an error instead of a refusal with a reason. Both are the next steps of the gate, and I have asked the library for them.

## In your hands

Declare a point of a kind the library does not check, and propose something to it that you would refuse if you were the reviewer:

```haro exercise
cBlock = 'check = <R:BLOCK name="limit_rule" value="amount < 100">'
b = new stzRefinableCode(cBlock)
? b.KindOf("limit_rule")
? b.Refine("limit_rule").To("1 = 1")[:admitted]
```

Before you run it, write what you expect the gate to answer, and what you would want it to answer. The distance between the two is a check the library does not yet have. What would its rule be, for a block of code? I do not have the answer in the library today, and I leave the question with you.

The unit has changed. Part II takes it apart: the point, the gate, the cascade, the timeline, and the trust that decides who may turn which knob.
