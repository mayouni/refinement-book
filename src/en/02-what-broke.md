---
id: what-broke
part: 1
number: 2
title: What broke
stage:
  built: "the declared change surface, listed on demand; a proposal answered with its verdict; the reach of its point on its line; a step that keeps the origin the proposal declared and its way back"
  designed: "a change that keeps its reason with it after the moment it was judged; the reach of a change across the code graph, joined to the gate"
  absent: "a saved history: the record of what changed and from which origin lives in the running object and not in the file"
status: draft
research: research/ch02.md
guards: [refinablecode_narrated, refine_deepening_narrated]
---

In this chapter I say what broke in the way software is changed, and why the letter of chapter 1 is harder now than it would have been some years ago, though the change it asks for is easier to write. I name the instruments the field trusts and the world they assume. Then I run the list of what a change must carry for trust to survive the speed at which changes now arrive.

## The afternoon

By the time the letter reached Softibank, an AI agent could draft the whole change in an afternoon: all fourteen products, the compliance report, the statement templates, the text messages, the tests.

The draft would not be careless work. In my view, today's AI agents write code that is plausible, idiomatic and often correct, and they write it at a speed no team matches: many changes at once, at any hour, at a small cost. In a few years, writing code went from the most expensive step in making software to one of the cheapest. These are views drawn from the work I see, not measured results.

In my view, every earlier era of programming had the same slow step: writing. Languages, tools and methods were shaped around that scarcity. When it ended, a question arrived in every serious software team at once.

If the change can be written in an afternoon by something that is not accountable for it, who makes sure it is right?

## The field

The field's answer has four instruments, and each is good at its job. This is general knowledge.

The **diff** shows which lines changed. The **pull request** gathers a change, its author and a discussion around it. The **sign-off** puts a person's name under a release. **Version control** keeps every change ever made, in order, and can return to any of them.

Each assumes something about the world. The diff assumes a reader who can hold the change in mind. The pull request assumes an author who can be asked. The sign-off assumes changes rare enough to schedule people around them. Version control remembers every change and judges none of them; it was never meant to.

They were built for a world in which a person wrote every change at the pace of a person. That world had a quiet symmetry: code was written at human speed and reviewed at human speed, and the two kept pace. Nobody designed the symmetry. It came from the fact that both sides of the desk held people.

## The principle

**The field automated the writing of changes without automating the trusting of them, and its instruments of trust were built for changes written by hand.**

When writing speeds up and reading does not, review does not stop. It goes on in form: the requests are opened, the approvals are clicked. But a reviewer facing forty changes written by AI agents cannot give each the twenty minutes the old symmetry assumed, and in the teams I see, approval drifts away from understanding. The name is still under the change. It certifies less.

At a bank, that drift has a consequence. When the auditor of this story visits Softibank, at month eighteen, the question will not be whether a change was approved. It will be who approved it, what was checked, and what it reached. An approval that certified nothing answers none of the three.

So trust has to move. It cannot rest on a person reading everything; it has to rest on the change. For trust to survive the speed of the afternoon, a change must carry five things:

- it is **validated**: judged before it lands, against rules declared in advance;
- it is **scoped**: what it reaches is computed and shown, not discovered in production;
- it is **attributed**: it carries where it came from;
- it is **reversible**: it carries its way back;
- it is **explainable**: it can say, later, why it was allowed.

Read the list again and notice what it never mentions: the author. Whether the change came from Amina, from a script or from an AI agent, the five are properties of the change, checkable either way. Judging authors does not keep pace with an afternoon. Judging changes can.

## The surface, declared

Can a program say where it may be changed? Run it. Here is a small piece of Softibank's pricing, with four places declared as refinement points:

```haro
cSrc = 'late_fee = balance * <R:PARAM name="penalty_cap" value="0.18" min="0.10" max="0.20"> * <R:PARAM name="days_factor" value="1" min="1" max="3">' + nl +
       'rounding = <R:ALGO name="rounding" value="half_up" options="half_up|bankers">' + nl +
       'vat = <R:PARAM name="vat_rate" value="0.19" min="0" max="0.25">'
o = new stzRefinableCode(cSrc)
? o.NumberOfPoints()
#--> 4
? @@( o.RefinementPoints() )
#--> [ [ "penalty_cap", "param", "0.18" ], [ "days_factor", "param", "1" ], [ "rounding", "algo", "half_up" ], [ "vat_rate", "param", "0.19" ] ]
```

Four points, each with its name, its kind and its value. Three are parameters with bounds; one, `rounding`, is a choice between two named algorithms. This list is something the diff never had: the declared change surface of a program, printed on demand. You are not reading files to guess what is safe to touch. The program says what it was built to have changed.

## The five, carried

Now the afternoon. An AI agent proposes the new cap:

```haro
o {
	r = Refine("penalty_cap").As(:llm).To("0.16")
	? r[:admitted]
	#--> 1
	? r[:why]
	#--> admitted: 'penalty_cap' 0.18 -> 0.16 [:llm] (structural + constraint + derivation + governance + trust passed)
	? @@( Cascade("penalty_cap")[:alsoTouches] )
	#--> [ "days_factor" ]
	? @@( History() )
	#--> [ [ "penalty_cap", "0.18", "0.16", "llm" ] ]
	? CanRevert()
	#--> 1
}
```

Read the five answers against the list.

**Validated:** the proposal was judged before it landed, and admitted, `1`. Here only the structure of the proposal and the bounds of the point had rules to apply; the other three checks pass when nothing is declared for them, and Part II declares them. **Explainable:** the answer says why, at the moment of the judgement: the value before and after, and the checks of the gate. **Scoped:** the cascade of the point names what else sits on its line, `[ "days_factor" ]`, the other factor of the late fee. **Attributed:** the history holds one step, and the step keeps the origin the proposal declared, `llm`: the kind of source, not its name. **Reversible:** `CanRevert()` printed `1`; the step keeps the value it replaced.

Five properties, and none of them came from reading a diff. The change and its point answered for them because the unit of the change was not a patch of text. It was a proposal to a declared point.

## What I refused

**I refused "review harder".** Add reviewers, add checklists, slow the queue: organisations try it, and in my view it works against the speed that made the work cheap. It asks people to match an afternoon with attention, and attention does not scale.

**I refused to judge the author.** The list of five does not ask whether the AI agent is good. The next generation of AI models will differ from this one, and a discipline built on judging them would have to be rebuilt each time. A discipline built on judging changes holds.

## The court

`refinablecode_narrated` asserts the points declared, a point's kind and the line it sits on; `refine_deepening_narrated` asserts the timeline and the origin a step records. No guard yet asserts the other points on a line, the answer this chapter reads as scope. Both are in the library's `base/test/refine/`, at the commit this book is pinned to.

## Where the field leads

The field's instruments lead in reach. A diff covers every line of every file, declared or not, in any language; a pull request can discuss a change no point anticipated. A refinement point covers what someone declared, and nothing more. A team that adopts this discipline keeps its reviews for the rest, and spends the work of declaring its points where change is frequent and costly.

Version control leads in memory. It keeps every change forever, on disk, across machines. The timeline you just read lives in the running object; the next paragraph says so.

## The limit

What is built: the declared change surface, listed on demand; a proposal judged before it lands and answered with its verdict; the other points on its line; a step that keeps the origin the proposal declared and its way back. All of it ran above.

What is designed: a cascade that reaches beyond the line, across the code graph, joined to the gate (chapter 6). And the fifth property is carried only at the moment of judgement: the answer explains, but the step in the history keeps the point, the values and the origin, not the reason. A change that keeps its reason with it, for the auditor of chapter 12, is the direction.

What is absent: a saved history. The library writes the source with its current values; the timeline is not in the file, so it does not yet survive the end of the program that made it.

## In your hands

Take the four points above and propose a change to each of them, one at a time, from an origin you name. One thing to know first: an origin the library was never told about is ranked as trusted, so the name you choose is recorded and not judged. Before you run each one, write which of the five properties you expect the answer to show, and which you expect to be missing.

```haro exercise
? o.Refine("rounding").As(:analyst).To("bankers")[:why]
? @@( o.Cascade("rounding")[:alsoTouches] )
? @@( o.History() )
```

Then look at what the history keeps of the second change, and look for anything that still says why it was allowed: `Why()` answers only for the last proposal. You will find out what the timeline keeps and what it does not, and that gap is the one chapter 12's auditor would ask about. I leave it open: it is the place where this discipline has the most work still to do.

What broke is the old unit of change. The next chapter says what replaced it, and why the replacement had to be typed.
