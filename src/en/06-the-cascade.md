---
id: the-cascade
part: 2
number: 6
title: The cascade
stage:
  built: "the cascade of a point: the line it sits on and the other points on that line, asked before a change; the cascade of a class from the code graph: its descendants and the classes that inherit a method"
  designed: "one cascade from a point through the code graph to everything that reads its value, joined to the gate as the review artifact"
  absent: "in the code, the reach of a point beyond its own line: a line that reads a variable the point sets is not in its cascade"
status: draft
research: research/ch06.md
guards: [refinablecode_narrated]
---

In this chapter I run the cascade: the answer to "what does this change reach?", asked before the change lands. I run the cascade of a point as the library has it, I show the line it does not reach yet, and I say what the cascade of a class adds and where the two are not yet one.

Amina's notebook from chapter 1 was a cascade written by hand: fourteen products, a risk module, a report, the statements, the text messages, the tests. She wrote it from memory, and she wrote that some of it she would discover "when they break".

## The field

The field's review shows the diff: the lines that changed, file by file. A reviewer reconstructs from it what the change means and what it reaches. Tools in common use add some of the reach: which files import a changed module, which tests cover a changed line, which owners must approve a path. All of this is general knowledge, and it helps.

The reconstruction is still the reviewer's. The diff shows what moved; the reach is inferred, by a person, at the pace of a person.

## The principle

**Before a change lands, ask what it reaches, and read that instead of the diff.**

The cascade is the reviewer's object. It names what a change to a point would touch, computed by the code, not reconstructed by the reader.

## The cascade of a point

Run it. Here is a piece of the late-fee code, three lines, three points, and a line that uses the fee:

```haro
cLate = 'late_fee = balance * <R:PARAM name="penalty_cap" value="0.18" min="0.10" max="0.20"> * <R:PARAM name="days_factor" value="1" min="1" max="3">' + nl +
        'vat      = <R:PARAM name="vat_rate" value="0.19" min="0" max="0.25">' + nl +
        'total    = principal + late_fee + vat'
o = new stzRefinableCode(cLate)
aC = o.Cascade("penalty_cap")
? aC[:exists]
#--> 1
? @@( aC[:lines] )
#--> [ 1 ]
? @@( aC[:alsoTouches] )
#--> [ "days_factor" ]
? @@( o.Cascade("vat_rate")[:alsoTouches] )
#--> [ ]
```

The cap sits on line 1, and a change to it also touches `days_factor`, the other factor of the same fee: a reviewer reading a change to the cap should look at the two together. The VAT rate sits on line 2 and touches no other point. The cascade answered before any change was proposed.

And for a point that is not there?

```haro
? @@( o.Cascade("ghost") )
#--> [ [ "point", "ghost" ], [ "exists", 0 ], [ "lines", [ ] ], [ "alsotouches", [ ] ] ]
```

It says so, `exists` at `0`, and reaches nothing.

## The line it does not reach

Now read line 3 again. `total` adds the late fee to the principal and the VAT. A change to the cap changes the late fee, and so the total. Is line 3 in the cascade of the cap?

```haro
? @@( o.Cascade("penalty_cap")[:lines] )
#--> [ 1 ]
```

No. The cascade of a point is its own line and the other points on it. It does not follow `late_fee` to the line that reads it. At Softibank, the fourteen products, the risk module and the statements are all lines like line 3: they read what the cap sets, somewhere else.

That is the line between what is built and what is designed, and I want it read plainly. The cascade of a point, today, tells a reviewer which knobs move together. The cascade that would tell Amina what the cap reaches across the bank's code is the one the library's architecture describes as reachability in the code graph, and it is not yet joined to the point.

## The cascade of a class

The code graph has a cascade of its own, and it is built. My Softanza book runs it in its chapter 10: given a class, the library scans the source into a graph and answers which classes descend from it, and which of them inherit a method rather than redefine it. Change the rate of a tariff class, and the graph names the three classes in the blast radius and the two that inherit the method. I do not run it again here; the page is there, with its blocks and their answers.

So two cascades are built. One belongs to the point and stops at its line; the other belongs to the class and follows the structure of the code. They are separate, and joining them is the direction: a point anchored as a node of the code graph, whose cascade is the graph's reachability from that node.

## What I refused

**This book does not call the line-local cascade the whole cascade.** The Teaching Edition of this book drew a cascade of seventeen nodes in three depths, with a wave that stopped where verdicts came back unchanged. That drawing showed the direction. The library at this commit computes what this chapter ran, and the book now shows that.

**I refused the diff as the review object, and kept it as evidence.** A reviewer reads the cascade first, because it names consequences; the diff stays available, because the cascade does not yet reach every line.

## The court

`refinablecode_narrated`, in the library's `base/test/refine/`, asserts the line a point sits on and that an unknown point does not exist. No guard yet asserts the other points on a line, the answer this chapter reads as the cascade's first use; the blocks above are its run. The cascade of a class has no guard here either: the code graph's guard scans a path of the library's working tree, and Softanza's chapter 10 says so.

## Where the field leads

The field leads in reach. Code-intelligence tools in common use follow calls, imports and references across a whole repository and many languages, and some draw the result beside the diff; this is general knowledge. The library's point cascade follows one line. What the discipline adds is the kind of answer: a cascade computed from what was declared, asked before the change, in the same object the gate judges. What the field adds today is distance.

## The limit

What is built: the cascade of a point, its line and the other points on it, asked before a change; the cascade of a class, from the code graph, run in Softanza's chapter 10.

What is designed: one cascade, from a point through the code graph to every line that reads what it sets, joined to the gate so that a change is judged against what it reaches.

What is absent, in the code: the reach of a point beyond its own line, as line 3 showed. The wave that stops early where a re-check comes back unchanged, drawn in the Teaching Edition, is not in the library and not in its architecture document: it is a direction this book keeps, not a design it can cite.

## In your hands

Make the cascade lie by omission. Write a source where a point's value is read on three other lines, and predict what `Cascade()` answers before you run it:

```haro exercise
cMine = 'rate = <R:PARAM name="base_rate" value="0.05" min="0" max="0.10">' + nl +
        'a = principal * rate' + nl +
        'b = a + fees' + nl +
        'report = b * 12'
m = new stzRefinableCode(cMine)
? @@( m.Cascade("base_rate") )
```

Then write, by hand, the cascade you wanted: the lines, in order. That list is the specification of the cascade the library does not compute yet. Keep it; chapter 12 returns to it.

A change is judged, and its reach is named. The next chapter is what happens after it lands: the timeline, and the way back.
