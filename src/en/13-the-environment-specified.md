---
id: the-environment-specified
part: 5
number: 13
title: The environment, specified
stage:
  built: "Refine's command at its first milestone: version, status and init run, and the six queued verbs answer that they are not built yet, with a reason and a next step; under it, the library's gate this book has run"
  designed: "Refine, the governed-change environment over code, interface and data: over a hundred specifications, an interactive prototype of its screens, twelve transactional primitives of change, the live modes of the interface and the data world, and the live mode of code named and drawn as a mockup; the remaining milestones of its command"
  absent: "Refine as a running product: the verbs validate, plan, apply, revert, show and export; the runtime of the code live mode; a public repository"
status: draft
research: research/ch13.md
guards: [gate_deepening_narrated]
---

In this chapter I turn to the product built on the foundation this book has run: Refine, the environment in which a team lives with refinements day to day. I tell it as stage and direction, with a date, because that is where it stands: specified at length, shown as screens, and started as a command. I say what runs, what is specified, and how the two meet.

## The field

The field's environments for changing software are mature and many: editors, review tools, pipelines, design tools, database migration tools, each excellent in its craft. This is general knowledge. Each holds one world and one kind of change, and the change between worlds is carried by people and meetings.

## The principle

**The discipline belongs to the foundation; the environment is a product built on it, and it never becomes the subject of the gate.**

Every verdict in this book came from the library, which is open. Refine is where those verdicts would be lived with: proposed from a screen, read as a cascade, reviewed, landed and taken back, across code, interface and data. If Refine did not exist, every block in this book would run as it did.

## What runs today

Refine's command is the first piece of the product that runs. Its plan names a ledger of milestones, each ending in a working verb with passing tests, and the command reports which are real. At its first milestone, three verbs run: `version`, `status` and `init`, which creates a project. Six are queued, in order: `validate`, `plan`, `apply`, `revert`, `show` and `export`. Asked for a queued verb, the command does not fail silently: it says the verb is not built yet, why, what to run instead, and where to read the plan. I ran it on 15 October 2026; asked for `validate`, its first line was: "`validate` is not built yet."

The command reports its state from the same ledger its roadmap describes.

What a verdict card on Refine's screen would show is the kind of answer this book has run. Refine's own `validate` is specified as a pipeline of four stages, without the library's governance and trust checks; here is the library's judgement:

```haro
v = new stzRefinableCode('cap = <R:PARAM name="penalty_cap" value="0.18" min="0.10" max="0.20">')
v {
	? Refine("penalty_cap").To("0.61")[:why]
	#--> constraint: 0.61 above max 0.20
	? Refine("penalty_cap").To("0.16")[:why]
	#--> admitted: 'penalty_cap' 0.18 -> 0.16 [:trusted] (structural + constraint + derivation + governance + trust passed)
}
```

A refusal with its check and its reason, and an admission with its values and its origin. A screen can draw these answers well. It does not need to make them.

## What is specified

Refine is specified in over a hundred documents, a hundred and thirteen in its folder when I counted them for this chapter. They describe a governed-change environment over three domains: code, interface and data. One machinery is shared across them: the refinement as the unit, the cascade as what is read before a change, the gate as the one writer, and a chain of record.

Three parts of the specification answer limits this book found in the library.

**Change as transformations.** The specification of Refine's graph model reduces every refinement to twelve primitive operations on a graph. They are creating, deleting and updating nodes; creating, deleting and retargeting edges; setting a refinement's value, adding an option and removing one; and inserting, removing and reordering the stages of a pipeline. A transformation is a sequence of them, applied transactionally: all commit, or none. That is the frame, specified, for the equality of chapter 11, two points that must move together; the specification handles a coordinated change through proposals produced by its derivation rules and judged on the state after them (its section 5).

**The interface and the data world.** The interface and the data domains each have their own specification, with their own primitives. A change to a screen's wording or a report's column is then a refinement like a change to a cap. That is the direction chapter 11 named, as Refine specifies it.

**Live refinement.** In the interface and the data world, a person points at the running product, a sentence on a screen, a column in a report, and refines it from there, through the same gate, with the cascade shown before the change lands. The live modes of the interface and the data world are specified and shown as working mockups; the live mode of code is named in the specifications, drawn as a mockup, and queued.

## What is shown

The prototype is one file, an interactive rendering of Refine's screens: the refinement editor, the cascade drawn across the three domains, the ribbon that moves between them, the verdict, the timeline. It runs in a browser, and it is a prototype: its screens are drawn from the specifications, not from the library's answers. The Teaching Edition of this book redrew several of them as figures. They show the direction well, and I mark them for what they are: illustrations of a product being built, not screenshots of one in use.

## What I refused

**I refused to make Refine the subject of the gate.** The gate is the library's, and every refusal in this book came from it. A reader who never uses Refine has the whole discipline in their hands.

**I refused to describe the screens as if they ran.** The prototype draws them, and the command reports three verbs that run. This chapter says both, with the date.

## The court

`gate_deepening_narrated`, in the library's `base/test/refine/`, asserts the gate whose answers a verdict card would draw. Refine's roadmap records six of six tests passing for its first milestone; this book did not run them.

## Where the field leads

The field leads Refine everywhere a product is used today. Its editors, review tools and migration tools are built, in use, and supported. Refine is specified, prototyped and started. What Refine's specifications add is one machinery across the three worlds, with the gate as its one writer; that is the direction, and the library under it is what runs.

## The limit

What is built: Refine's command at its first milestone, three verbs that run and six that answer that they are queued; and under it, the library's gate, run throughout this book.

What is designed: the environment, in over a hundred specifications; the screens, as an interactive prototype; the twelve transactional primitives; the live modes of the interface and the data world, as specifications and mockups, and the live mode of code, named and drawn; the remaining milestones of the command.

What is absent: Refine as a running product, its six queued verbs, the runtime of the live mode of code, and a public repository. The platform's site says the same in one word: the implementation's stage is "specification".

## In your hands

Take the equality of chapter 11, the letter that must state exactly the cap, and write it as Refine's specification would: one transformation, a sequence of primitives that all commit or none.

```haro exercise
# refinement.set_value  penalty_cap  0.18 -> 0.16
# refinement.set_value  letter_rate  18   -> 16
# the rule letter_rate = 100 * penalty_cap, checked once, after both
```

Then say what the gate would have to check, and when: after each primitive, or after the sequence. The specification's sections 5 and 6 frame an answer, and Refine's repository is not public yet; the library does not have one. Write yours.

The book's chapters end here. A coda returns to Softibank, for the next letter.
