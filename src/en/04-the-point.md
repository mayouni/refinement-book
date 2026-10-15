---
id: the-point
part: 2
number: 4
title: The point
stage:
  built: "the refinement point as a tag in the source, with a kind, a name, a value and bounds or options; the declared change surface listed on demand"
  designed: "points of eight kinds, among them a variable type, which carries a type and a validation; points anchored as typed nodes in the code graph"
  absent: "a form of the source with the tags replaced by their values, for a compiler to read; a refusal of two points with the same name; a value containing the character that closes a tag"
status: draft
research: research/ch04.md
guards: [refinablecode_narrated]
---

In this chapter I take the first piece of the discipline apart: the point, the place where code declares that it may change. I run the grammar of a tag, then what a point says and what it does not say yet. Part II begins here because every other piece, the gate, the cascade, the timeline and the trust, is a question asked of a point.

When Amina listed what the penalty cap touched, she was doing by hand what this chapter does in the code: naming the places where the letter would land.

## The field

The field keeps its knobs in many places. A configuration file holds settings outside the code; an environment variable changes a value per machine; a feature flag turns a path on or off without a release. All of this is general knowledge, and each answers a real need: change a behaviour without rewriting the program.

What they share is that the knob has a value and rarely a law. A configuration file will accept a penalty cap of sixty-one per cent if someone types it; the bounds, when they exist, live in a reviewer's memory or in a test somewhere else. The knob is declared. How far it may turn is not.

## The principle

**Declare, in the code itself, where it may change and how far.**

A refinement point puts the knob and its law on the same line. Whoever reads the line, a person or an AI agent, sees the value and the bounds together, and the gate of the next chapter reads them from the same place.

## The tag

Run it. A point is a tag in the source, opened by `<R:`, with its kind, its name, its value and, for a parameter, its bounds:

```haro
cFees = '# fees' + nl +
        'cap   = <R:PARAM name="penalty_cap" value="0.18" min="0.10" max="0.20">' + nl +
        'grace = <R:PARAM name="grace_days" value="5" min="0" max="15">' + nl +
        'x     = <R:PARAM value="1">'
o = new stzRefinableCode(cFees)
? o.NumberOfPoints()
#--> 2
? @@( o.RefinementPoints() )
#--> [ [ "penalty_cap", "param", "0.18" ], [ "grace_days", "param", "5" ] ]
```

Three tags, two points. The cap's bounds, ten to twenty per cent, are the bank's own; the regulator's ceiling is a point of its own, moved under compliance authority, in chapter 11. The third tag has no name, and a point without a name is not a point: nothing could refine it, because a proposal names the point it changes. The comment line and the rest of the code are left as they are. The library reads the tags and nothing else.

The grammar is short. The kind after `R:` says what the point is; `name` says how to call it; `value` is its current value; `min` and `max` bound a parameter; `options`, separated by `|`, list what an algorithm or a library may become. Chapter 3 ran the three kinds the gate judges.

## A name is exact

A proposal calls a point by its name, and the name is exact:

```haro
? o.ValueOf("penalty_cap")
#--> 0.18
? o.Refine("Penalty_Cap").To("0.16")[:why]
#--> structural: no refinement point 'Penalty_Cap'
```

The same letters in other capitals are another name, and the gate refuses the proposal at its first check, structural, before it looks at the value. That is strict, and I want it strict. A name is how a proposal says which knob it means; a proposal that spells it loosely has not said it, and should not land on a guess.

## What a kind says, and what it does not

A parameter's kind says that it has bounds. It does not say what sort of number it is. The grace period is counted in days:

```haro
? o.Refine("grace_days").To("7")[:admitted]
#--> 1
? o.Refine("grace_days").To("7.5")[:why]
#--> admitted: 'grace_days' 7 -> 7.5 [:trusted] (structural + constraint + derivation + governance + trust passed)
```

Seven days, admitted. Seven and a half days, admitted too! The value is inside the bounds, and a parameter checks its bounds. Nothing in the point says that a day is a whole number, so nothing refuses half of one.

The gate holds a point to what the point declares, and this point declared a range, not a type. The library's design names, among eight kinds of point, a variable type, which carries a type and a validation; it is designed, and today the parameter is the kind that carries a number.

## What I refused

**I refused points the code finds by itself.** The definition says *declared*, and I hold the word to its meaning. A point is declared by a person who knows that this value may change and how far. A program has many constants; most of them are not knobs, and a tool that turned every constant into a point would hand an AI agent a much larger surface than anyone meant to open. The declared change surface is small on purpose.

**I refused a knob without a place in the code.** The penalty cap's tag sits on the line that uses it. A setting kept in a file of its own, read at start-up, has its value far from its use; the point keeps both on one line, so that the cascade of chapter 6 can say which line a change reaches.

## The court

`refinablecode_narrated`, in the library's `base/test/refine/`, asserts two points declared from their tags, the parameter with its kind, and a point that does not exist answering as absent. The exact names, the tag without a name and the half day ran above, in this chapter's blocks; no guard asserts them yet.

## Where the field leads

The field leads in reach. A configuration file can be changed without touching the code, by an operator who never sees it, and the program reads the new value at its next start. A refinement point lives in the source: changing it is a change to the code, through the gate, and the program built from that code carries the new value once the tagged source is rendered for a compiler, which the limit names as absent. That is the point of the discipline, and it is also its cost: a knob an operator turns at night is outside this gate.

The field also leads in types. A configuration schema can say that a value is a whole number, a date or one of a list; the library's parameter says a range, and its variable type is designed.

## The limit

What is built: the tag, with its kind, name, value and bounds or options; the declared change surface listed on demand; names matched exactly. All of it ran above.

What is designed: points of eight kinds (parameter, block, algorithm, function, pipeline, variable type, library and custom), named in the library's architecture document, and points anchored as typed nodes in the code graph rather than read as tags from text.

What is absent, and next:

- The class renders the source with its tags in place. A form with each tag replaced by its value, for a compiler to read, is not in the class at this commit; the tagged source is the document the gate governs.
- Two tags with the same name are both listed, and a proposal changes the first one only. Nothing refuses the second declaration.
- A value that contains `>`, the character that closes a tag, is read as empty, and a later proposal is written in front of the old text, so the tag is spoiled. A block of code such as `amount > 100` cannot be the value of a point today.

## In your hands

The duplicate is the defect I leave you. Run it:

```haro exercise
cDup = 'a = <R:PARAM name="cap" value="1" min="0" max="5">' + nl +
       'b = <R:PARAM name="cap" value="2" min="0" max="5">'
d = new stzRefinableCode(cDup)
? d.NumberOfPoints()
? d.Refine("cap").To("4")[:why]
? d.Rendered()
```

Read which line changed. Then decide what the library should do with the second tag: refuse to parse the source, rename the point, or change both lines. Each answer has a cost for a bank whose code was written by many people over many years, and I have not chosen one.

A point declares where a change may land. The next chapter is the judge that stands at that place: the gate, its five checks, in the order the code runs them.
