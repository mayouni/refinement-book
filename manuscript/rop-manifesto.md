# Refinement-Oriented Programming

*A manifesto for software in the agentic era.*

**Mansour Ayouni · Softanza Labs**
**v0.1 · 2026**

---

## Preface — Why this exists

I have been writing software for thirty years.

I started in Tunis in the mid-1990s, building accounting systems for small businesses in BASIC and then in Clipper. I moved through every era a programmer can live through: client-server, the early web, the Java enterprise years, the JavaScript renaissance, the cloud, the container, the API. I learned C, Smalltalk, Lisp, Perl, Python, PHP, Java, Ring, Zig. I worked across Tunisia, Niger, France, and North America. For most of those decades, the conversation about how to build software was a conversation about *which tools and which paradigms make humans more productive when humans write code.*

In late 2022, that conversation ended.

It ended for the reason every paradigm shift ends a prior conversation: the underlying physical situation changed faster than the conversation could absorb. Software is no longer primarily a thing humans write. In the projects I am paid to deliver — banking systems for a Niger-based bank operating under BCEAO regulation, where every code change carries audit obligations — AI agents now produce more lines of code per day than the human team. The lines are correct often enough to ship. They are wrong often enough to require review. And the human team can no longer read them at the rate they are produced.

This is not a productivity story. This is a *unit of work* story.

For five decades, the unit of programming work has been the *line*: written by a human, reviewed by a human, attributed to a human, debugged by a human. Every tool we have — the IDE, version control, code review, continuous integration, the diff — assumes this unit. When the human can no longer keep pace as the writer, the unit silently fails. The line is still there. The diff still renders. But the reviewer is no longer reading; the reviewer is *approving*, which is something else entirely. The audit chain that regulators expect — the one that answers *who decided this, on what authority, against what policy* — quietly stops being true.

You can feel this happening if you work in a regulated industry. The audits get harder to pass. The internal reviews get faster but shallower. The senior engineers stop reading the diffs and start asking the AI to explain them. The juniors stop pushing back because the AI is more confident than they are. Nobody is *wrong* exactly — the code works often enough — but the social structure that produced trustworthy software is hollowing out.

For two years I tried to fix this with the existing tools. Better code review. Better tests. More structured prompts to the agents. Linters tuned for AI-generated code. Audit-friendly commit messages. Each of these helped a little. None of them addressed the actual problem, which was that *the unit of work had changed and we were still managing the old unit.*

This book is the position I arrived at after those two years. The position is: **the unit changed.** It is no longer the line, the diff, the patch, the pull request. It is the *refinement* — a typed transformation of a subset of the codebase graph, carrying its cascade, its author, its verification, and its history. Once you accept the new unit, almost every existing tool turns out to be designed for the wrong thing: optimized for an artifact that is no longer the artifact that matters.

I gave this position a name — **refinement-oriented programming** — and I built a tool to make it concrete: **Refine**. Refine is not the only possible implementation of refinement-oriented programming. It is one implementation, in private development at the time of writing, validated against the Sonibank Niger banking system under BCEAO compliance. Other implementations will follow. The point of the book is the paradigm, not the tool. The tool exists because in our field a paradigm has no traction until somebody has shipped a working version of it; the position has to be defensible against a real codebase, against real regulators, against real working programmers under real deadlines.

This is a short book. There is enough material in it to fill a thousand pages, but I would rather write the manifesto first and the textbook second. The manifesto names the paradigm and stakes the position. The textbook can come later, once we have a community to write it with.

A few things this book is not:

It is not a user manual for Refine. The website at refine.softanzalabs.com carries the live documentation, the tutorials, the prototype, and the foundations pages. The book references that material; it does not duplicate it.

It is not a complete theory of programming under AI. We do not have one yet. What we have are working answers to specific questions — *who proposed this change, what cascade does it trigger, will it pass the audit* — and a discipline for asking those questions consistently. The book describes that discipline.

It is not neutral. I have a position. I have built a product. I have customers in regulated industry whose audits depend on getting this right. The book is the case for the position, written as honestly as I can write it, with explicit notice of what I am not certain about and what I am claiming despite that uncertainty.

I write from Niamey, where the requirements live; from Tunis, where the language work happens; and from Paris, where the policy work happens. Refinement-oriented programming is built where the audit chain is not optional. If it works there, it generalizes.

Mansour Ayouni
Niamey, 2026

---

## Start here — how to read this book

If you build software for a living right now, you are standing in a forest that keeps rearranging itself. Every few weeks a new word arrives — *agent*, *harness*, *memory*, *governance*, *context*, *MCP* — and each one means three things depending on who is saying it. The tools change faster than you can learn them. The advice contradicts itself. You are shipping code an AI wrote and you are no longer sure you read it. This book is written for exactly that person, and its first job is to be a light, not another tree.

So before the argument begins, here is the road.

**The whole book in one paragraph.** For fifty years the *unit* of programming work was the line of code: written, reviewed, attributed, and debugged by a human. AI broke that — not because the code is bad, but because humans can no longer read it at the speed it now arrives. So the unit has to change. This book argues the new unit is the **refinement**: a single, typed, *governed* change — one that carries proof of what it touches, who made it, what rule it obeys, and how to undo it. Everything else in the book follows from that one move.

**The spine — the path through the trees.** The chapters are a single line of reasoning, and you can hold the whole thing in your head as six steps:

1. **What broke** (Ch 1) — why the line stopped working as the unit.
2. **The unit changed** (Ch 2) — what a refinement *is*, precisely.
3. **The codebase as a graph** (Ch 3) — the place a refinement lives.
4. **The compiler that revalidates** (Ch 4) — the thing that checks a refinement before it lands.
5. **The cascade** (Ch 5) — what you read *instead of the diff*: the computed blast radius of a change.
6. **Authorities, attribution, audit** (Ch 6) — who is allowed to change what, and how the record survives.

> **Figure 0.1 — The road through the book.** Six steps, one line of reasoning: the break, the unit, the graph, the compiler, the cascade, the record. Everything after them is consequences.

If you read only those six, you have the paradigm. Everything after them is *consequences*: how it changes daily work (Ch 7–11), how agents fit (Ch 12–15), the three domains code/UI/data (Ch 16), the honest argument against the opposite bet (Ch 17), and — the chapter to read if you trust nothing else — **the honest boundaries** (Ch 18), where I state plainly what this paradigm does *not* do.

**Five parts.** On the shelf, the chapters sit in five parts — I. The argument (1–6) · II. The working discipline (7–12) · III. The collisions (13–15) · IV. The horizon (16–17) · V. The limits (18 + the coda) — each opening with a short page that says where you are.

**Two ways to read it.** If you have ninety minutes, read Chapters 1, 2, 4, 5, and 18 — that is the argument and its limits. If you have the evening, read it straight through; it is a short book by design. Either way, **when a word feels slippery, turn to the back.** The appendix *"The words that keep shifting, pinned"* takes the terms the field keeps redefining and fixes each to one meaning, names what it is usually confused with, and points to the chapter that settles it. It is the map for the parts of the forest where the signposts have been moved.

**One running example.** Almost every abstract idea in this book is shown on the same concrete system: **Sonibank**, a real banking system in Niamey, Niger, operating under West African (BCEAO) regulation, where every code change carries an audit obligation. When you see *Amina*, the *penalty cap*, or a *BCEAO policy*, that is the worked example — your "you are here" pin. If a chapter feels too abstract, find the Sonibank scene in it; that is where the idea touches the ground.

**A promise about honesty.** I sell a product built on this paradigm; I say so plainly, here and in the closing pages. The defense against my own bias is that every chapter ends by naming what it does *not* establish, and the whole of Chapter 18 is nothing but limits. If a claim in this book is not hedged where it should be, that is a bug — hold me to it.

Now, the forest.

---

# Part I — The argument

*Chapters 1–6 · The spine.* Everything in this book follows from one move, and these six chapters make it: what broke when code began arriving faster than humans can read it; the refinement as the new unit of work; the graph as the place a refinement lives; the compiler that revalidates it; the cascade you read instead of the diff; and the authorities, attribution, and audit that make the record survive. Read only this part and you have the paradigm.

---

# Chapter 1 — What broke

*The problem on the ground: why humans can no longer keep up as the readers of code, and how that quietly breaks the audit chain.*

In November 2022, a senior engineer at Sonibank Niger came to me with a problem.

His team had been using an AI coding assistant for about six months. The assistant produced reasonable Python and reasonable JavaScript. He estimated that across his eight-person team, perhaps half of the new code being shipped to production had been written by the assistant — sometimes typed verbatim from a chat response, sometimes lightly edited, occasionally rewritten substantially.

The team's velocity, measured in stories closed per sprint, had roughly doubled. Defect rates were flat. The CTO was pleased. The board was pleased. The pull request queue moved twice as fast as it had a year earlier.

What worried the senior engineer was something he could not articulate cleanly. He felt, he said, that he no longer knew what was in the codebase. Not in the literal sense — he could grep for anything, the files were where they had always been — but in the *responsibility* sense. When a regulator from the BCEAO came in for the quarterly audit and asked him *why* a particular interest-rate calculation worked the way it did, he could no longer answer with confidence. He could find the code. He could read the commit message. He could see whose name was on the commit. But he could not honestly say whether the engineer whose name was on the commit had written that code, or had asked the assistant to write it, or had read the code carefully before merging it.

"Three years ago," he said, "I could have told you who decided this and why. Now I cannot tell you who decided this. I can only tell you who clicked the merge button."

This chapter is about that gap. It is about what changed when AI agents started writing code at a pace that exceeds human reading speed, and about why the tools we built for the old pace fail silently — not by breaking, but by continuing to operate while the meaning they used to carry quietly drains out.

## §1 — The unit of programming work, briefly

To understand what broke, it is worth being explicit about what programming has been *for* most of its history.

From the late 1960s onward, the dominant model of programming work has assumed a human author. The human reads a specification, holds a mental model of the system, writes code, runs tests, iterates. The tools we built — text editors, version control, type checkers, IDEs, code review — are all instruments for a *human author working at human speed.*

The fundamental unit of this work has been the **line of code**. The line is small enough that a human can write one in a few seconds, read one in a fraction of a second, understand one in a few seconds more. The line is the unit we count when we estimate complexity. The line is the unit we attribute when we ask *git blame*. The line is the unit we review when we read a pull request.

When the line proved too granular for some kinds of analysis, we abstracted upward to the **diff**: a structured representation of which lines changed between two snapshots of the code. The diff is what version control records, what reviewers read, what continuous integration acts upon. A typical pull request might contain ten lines of changes, or a hundred, or — rarely — a thousand. The reviewer reads the diff and forms an opinion.

When the diff proved too narrow to express larger units of work, we wrapped it in the **pull request**: a bundle of diffs with a title, a description, a discussion thread, and a set of approvals. The pull request is what teams coordinate around. It is the social object of modern software development.

Lines, diffs, pull requests: three nested units, each one assuming the same thing — that a human authored what is being reviewed, that another human is reading it, and that the time between writing and reading is governed by human cognitive speed.

This is the system that worked. It worked because the bottleneck was always the human author. Code was scarce. Each line cost a programmer time and attention. The tools optimized for the constraint that mattered: making humans more effective at writing code.

The bottleneck moved.

## §2 — What changed in 2022

When the first usable AI coding assistants appeared in 2021 and 2022, most people who tried them noticed two things: the code was often surprisingly good, and it appeared surprisingly fast. The novelty wore off quickly. By early 2023, autocompletion-grade assistance was a default expectation in most editors. By the end of 2023, agentic systems — tools that could plan, edit multiple files, run tests, and iterate without continuous human guidance — were demonstrable. By 2025, agentic systems were in routine production use in many teams, including teams like the one at Sonibank.

The change that mattered was not the quality of the code, although that improved. The change that mattered was the **rate of production**.

A human programmer, working steadily, can produce somewhere between 50 and 200 lines of code per day, depending on the language, the domain, and the experience of the programmer. This is well-studied; the figure has been roughly constant since the 1970s. Two things have always limited it: the speed at which a human can think through a design, and the speed at which a human can type the resulting code.

An AI agent in 2026 can produce 50 to 200 lines of code in **eight to ninety seconds.** Not all of it is good. Most of it requires some editing. But the agent's marginal cost of producing another fifty lines is approximately zero, and its willingness to produce them is unlimited.

This is a four-orders-of-magnitude change in the speed of code production. It is the kind of change that doesn't fit smoothly into the old tools because the old tools assumed a constraint that no longer holds.

Consider what happens when you put an agent and a human reviewer on opposite sides of a pull request. The agent produces a 200-line change in twenty seconds. The reviewer needs to understand what changed, evaluate whether it is correct, judge whether it fits the system, decide whether to approve. For a careful human, that is fifteen to forty-five minutes of work. The arithmetic does not survive contact with reality. If the agent is producing changes ten times a day, the reviewer cannot read all of them at the level of attention the old workflow assumed.

So one of two things happens. Either the reviewer slows down and the agent's throughput becomes irrelevant (which is what happens in regulated environments, at the cost of the productivity gains everyone was promised). Or the reviewer speeds up, which means the reviewer is no longer *reading* in the old sense; the reviewer is *skimming*, or *trusting the tests*, or *trusting the agent*, or simply *approving*, where approving is a social signal rather than a cognitive act.

In most teams I have observed, the second thing happens. Reviewers approve. Sometimes they read carefully; more often, especially when the agent has a track record of producing reasonable code, they do not. The diff still renders. The merge button still clicks. The commit still bears a human approver's name. But the *meaning* of that approval has changed.

This is what the senior engineer at Sonibank was trying to describe. He had not lost the artifact. He had lost the *attestation behind the artifact.*

## §3 — Why this is invisible if you look at the wrong numbers

For about eighteen months, the industry conversation about AI coding tools focused almost entirely on productivity. Studies appeared comparing teams that used AI assistance to teams that didn't, measuring stories shipped per sprint, lines of code per day, time-to-merge for pull requests. These studies showed, almost uniformly, that AI-augmented teams shipped more, faster.

The studies were not wrong. The teams really did ship more, faster. The studies measured what they said they measured.

What the studies did not measure — what no productivity study can measure, because the effect is in the *quality of attestation*, not the quality of output — is what happens to the social and regulatory infrastructure that *depends on humans having read the code.*

Consider, in concrete terms, what code review historically accomplished beyond catching bugs:

It established that *at least two humans* understood the change. It created a moment where the change had to be defended in writing. It produced a record — the comments, the discussion, the back-and-forth — that an auditor or a future maintainer could read to understand why a decision was made. It distributed knowledge across the team, because a junior reviewing a senior's code learned, and a senior reviewing a junior's code corrected. It produced *shared mental models*, which are how teams build software that is more sophisticated than any individual on the team.

None of those functions show up in the productivity metrics. All of them depend on the reviewer actually having read the code.

When AI assistance is light — autocompletion, single-function suggestions — the reviewer's cognitive load doesn't change much. The reviewer reads the diff much as before. The attestation functions of review continue to work.

When AI assistance becomes agentic — multi-file changes, autonomous planning, hundreds of lines per session — the reviewer's cognitive load explodes. The reviewer cannot, in the time the workflow allots, perform the cognitive work that review used to require. The reviewer either falls behind (and the productivity gains evaporate) or compresses (and the attestation hollows out).

The productivity studies cannot see the hollowing because the artifacts — diff, comment, approval, commit — all still exist. What has changed is the relationship between those artifacts and what they used to mean. An approval that used to mean *I have read this and I vouch for it* now sometimes means *I have read this and I vouch for it,* and sometimes means *I have skimmed this and trust the tests,* and sometimes means *I have not really read this, but the system needs an approval.* All three produce identical bytes in the database. The bytes are not the meaning.

In a small team writing internal software, the difference may not matter. The cost of an error is bounded; the team trusts each other; the code can be fixed when problems appear. In a banking system regulated by the BCEAO — or in healthcare, or critical infrastructure, or government — the difference matters enormously. The audit chain is not a metaphor. It is a legal artifact. When the regulator asks *who decided this and on what authority*, the answer "the human who clicked the merge button" is no longer adequate if that human did not, in any meaningful sense, decide it.

## §4 — The reviewer attention crisis

Let me name this directly, because the rest of the book depends on it being clear: **AI agents have produced a reviewer attention crisis, and the existing tools cannot resolve it.**

The crisis is structural, not anecdotal. The tools we built for code review — GitHub's pull request interface, GitLab's merge request, Gerrit, Phabricator, every variant — all assume a roughly one-to-one ratio between code produced and code reviewed. When the ratio becomes ten-to-one or a hundred-to-one in favor of code produced, no amount of interface improvement to those tools can rescue the situation. The reviewer cannot read what the agents produce. The reviewer cannot meaningfully attest to it. The cognitive work that *used* to happen at review time has to happen *somewhere else*, or it does not happen at all.

There are four places it can move:

It can move *forward in time*, to before the agent acts. This is the prompt-engineering and design-document approach: invest more in specifying what the agent should do, so that the reviewer's job becomes verifying the specification was met rather than verifying the code. This works for narrow tasks. It scales poorly to systems whose specifications are themselves long and detailed; you end up reviewing the specification with the same difficulty you used to review the code.

It can move *to automation*: tests, type checkers, linters, static analyzers, mutation testing, fuzzing. This is the most popular response in the industry today. It also works, partially. The limit is that automation can verify the things you knew to automate. It cannot, in general, catch the class of error where the code does something subtly different from what the business required — that judgment still requires a human, and the human is what we ran out of.

It can move *to the compiler*. This is the move this book argues for. If the compiler can compute the cascade of a proposed change — which other parts of the system are affected, which tests revalidate, which policies are triggered — then the reviewer can read the *cascade*, which is much shorter than the diff, instead of reading the code. The reviewer's attention shifts from *what was written* to *what the change implies*. This restores the possibility of meaningful attestation at a higher level of abstraction.

It can be *abandoned*, which means accepting that AI-generated code goes through approval rituals that no longer carry the meaning they used to carry. This is, I believe, what is happening in many teams right now, though almost no one will say so out loud.

The book argues for the third option. The argument is not that the other three are wrong — automated testing is essential, specifications matter, even the abandoned ritual sometimes catches a problem — but that the third option is the only one that *restores meaningful human attestation at agent-production speeds.* It restores it by changing what the human reads, not by asking the human to read faster.

## §5 — The audit chain is not optional

It would be easy to read the preceding sections and conclude that the problem is regulated industries specifically, and that for everyone else the situation is fine. I want to push back on that conclusion.

The audit chain — the ability to answer *who decided this, on what authority, against what policy* — is not an artifact of regulation. Regulation makes the audit chain *visible*, because regulators ask for it explicitly. The audit chain itself is a property of any production codebase that is maintained over time.

Consider an unregulated SaaS company three years after launch. A customer reports a bug. The team investigates and traces it to a particular line of code, written four months ago, that handles a specific edge case in subscription renewals. The line is correct for most renewals; it is wrong for renewals that fall across the date of a billing-plan change. The team wants to fix it. To fix it correctly, they need to know *why* the line was written that way — was it a deliberate design decision, a workaround for a downstream system, a mistake, a misunderstanding of the requirements? If they can answer that question, they can fix the line. If they cannot, they have to guess, and the guess will sometimes introduce a worse bug than the one they were fixing.

The ability to answer that question is the audit chain. In a regulated environment it is enforced by external authorities. In an unregulated environment it is enforced by the cost of maintenance: codebases without audit chains become unmaintainable. The maintenance cost rises until the codebase is rewritten, abandoned, or — most commonly — slowly hollowed out, with knowledge concentrated in fewer and fewer people, until those people leave.

Every team eventually pays for the audit chain. Regulated teams pay up-front; unregulated teams pay over time. The difference is timing, not whether the chain matters.

When AI agents enter the picture, the chain becomes harder to maintain because the *author* of a change is no longer a person you can ask. The agent doesn't remember why it wrote what it wrote. The agent doesn't have a stake in the codebase three years later. The agent, when asked *why*, will generate a plausible-sounding answer that may or may not correspond to what was in its context when it wrote the code.

This is not a fixable property of the agent. Agents will get more transparent, more steerable, more capable of explaining themselves. But the underlying issue — that the agent is not a continuous identity with a memory of the project — is intrinsic to what agents are. The continuity has to live somewhere else.

It can live in the *records*. If the agent's proposal, the reviewer's approval, the cascade the compiler computed, the gates that ran, the tests that passed — if all of these are first-class artifacts, persisted, attributable, queryable — then the audit chain survives the agent's lack of memory. The chain is built around the agent, not through it.

This is the second thing the book argues for. The first was: move cognitive work to the compiler. The second is: make the records first-class, with the same care we apply to the source code itself.

## §6 — What the old tools assume

To make the rest of the book's arguments visible, it is worth being explicit about what the existing toolchain assumes.

**Version control** assumes the meaningful unit of change is the commit, and the meaningful identity of an author is a name and email address. Git makes both of these excellent: commits are atomic, signed, queryable; authorship is preserved through every operation. What Git does *not* preserve, because in 2005 it did not need to, is the difference between *the human who typed the code* and *the system that proposed it.* When `git blame` returns a name, it returns the human whose credentials were used at commit time. That tells you nothing about whether the code was authored, edited, reviewed, or merely accepted.

**Code review tools** assume a roughly one-to-one ratio between code produced and code read. They optimize for making the reading experience clearer: better diffs, inline comments, suggestion boxes, threaded discussions. None of this scales to a regime where ten times more code is produced than the reviewer can read.

**Continuous integration** assumes a test suite covers what matters. CI is a powerful automation, and it has carried much of the load of AI-augmented development. But CI cannot test what the team did not think to write tests for, and the gap between *what was tested* and *what is correct* is exactly where AI-introduced errors tend to live, because the AI often gets the explicit requirements right and gets the implicit ones — the ones the team never wrote down — wrong.

**The IDE** assumes the user is the author. The cursor, the suggestion bar, the autocompletion, the keybindings, the file tree — all of this is built around a human typing code into files. When an AI agent edits ten files in a session, the IDE shows ten dirty tabs and a `git status` listing. It does not show the *unit* of work the agent performed, because the IDE does not have a representation for that unit.

**The bug tracker, the project management tool, the documentation system** — each of these has its own assumption about the unit of work and the identity of the author. None of them was designed for a regime where some authors are humans and some are agents and the same task might be performed by either.

These assumptions are not bugs. They are sensible defaults for the world the tools were built for. The world changed; the tools have not caught up.

There is a strong instinct in the industry to fix this by *adding* — adding AI features to existing tools, adding agent identifiers to commits, adding new statuses to pull requests. These additions help marginally. They do not solve the underlying problem, which is that the unit of work changed, and a paradigm shift cannot be reached by incremental addition to a previous paradigm's tools.

The argument of this book is that we need to start at the unit. Not the line, not the diff, not the pull request. The **refinement**.

## §7 — A preview of where this goes

The next chapter introduces the unit. I want to close this one with a brief preview, so the reader can see the shape of what's coming.

A refinement is a typed transformation of a subset of the codebase graph. The shape of the change is captured by the type. The scope of the change is captured by the subset. The history of the change — who proposed it, with what authority, against what policy, with what verification, with what cascade — is captured by the refinement's metadata. The refinement is the *unit*; the line is an implementation detail underneath.

This sounds abstract. It will become concrete, with worked examples from the Sonibank codebase, in Chapter 2. By the end of Chapter 4, the reader should be able to look at any code change and ask, naturally: *what's the refinement here?* — and find that the question is well-formed, the answer is short, and the answer carries more information than the diff did.

A refinement is not a replacement for code. The code is still there. The refinement is a *representation* of the change to the code that is more useful, in the agentic era, than the raw textual diff. The cascade-aware compiler turns the refinement into the textual change. The human reviewer reads the refinement, not the textual diff. The audit chain is built out of refinements, not commits. The IDE shows the refinement first and the code second.

This is the move. Once you make it, almost everything else in the book follows by mechanical extension. The cascade-aware compiler exists because the refinement exists. The audit chain works because the refinement carries its own attestation. The agent has a tractable interface because it can propose a refinement rather than emit a diff. The methodology — onboarding, assessment, steady operation, change management — falls out of having a unit small enough to govern.

This is also where most readers will, reasonably, ask whether the move is overkill. *We have been writing software for fifty years without refinements; do we really need a new unit?* The honest answer is: for ten or fifteen years more, you could probably continue without one. The line still works for many teams. The diff still tells you what changed. If you are a small team writing internal software for non-regulated use cases, with humans writing most of the code, the existing tools will serve you well enough for a while.

But the trajectory is clear. The fraction of code written by agents is rising. The audit pressure on AI-generated code is rising. The cognitive load on human reviewers is unsustainable at current trajectories and growing. The teams that wait until the situation breaks will pay a much higher price than the teams that move now, while the alternative is still being shaped.

I would rather move now.

## §8 — What this chapter has established — and what it has not

What the chapter has established:

- The unit of programming work — line, diff, pull request — assumed a human author and a human reader working at human cognitive speed.
- AI agents raised the rate of code production by orders of magnitude, producing a reviewer attention crisis the existing tools cannot resolve.
- The approval artifacts still exist, but their meaning has hollowed: an approval no longer reliably attests that a human read the change.
- The audit chain is not a regulated-industry artifact; every long-lived codebase pays for it — regulated teams up-front, everyone else over time.
- Of the four places the review work can move — earlier specification, automation, the compiler, abandonment — only the compiler restores meaningful attestation at agent speed.

What it has not established:

- That every team must move today. For a small team writing mostly human-authored, unregulated code, the old tools still serve for a while; the argument is about the trajectory, not a present emergency.
- That the third option is achievable. Moving the cognitive work to the compiler is, at this point, a claim — making it good is the burden of the rest of the book, beginning with the unit it requires.

The next chapter begins the move.

---

# Chapter 2 — The unit changed

*The core move: what a refinement is, precisely — and why it, not the line or the diff, is now the unit of work.*

The most useful thing a paradigm does is name the unit.

Object-oriented programming named the object. Functional programming named the function. Structured programming named the procedure. Each of these naming acts was, at the time it happened, a small but disorienting shift in how programmers organized their attention. The object had existed in some form before OOP — there were always values with associated operations — but until somebody named the object and built tools around it, the object was not the *primary* thing programmers thought about. Once the object was named, programs were organized differently, designed differently, taught differently, talked about differently. The naming was the paradigm shift.

This chapter does the same naming act for the agentic era. I am going to name the unit, define it precisely, and show you what it looks like in a real codebase. The unit is the refinement.

By the end of this chapter you should be able to look at a code change — yours or somebody else's — and ask *what is the refinement?* and find that the question is well-formed and the answer is short.

## §1 — A refinement, defined

A **refinement** is a typed transformation of a subset of the codebase graph, carrying its cascade, its author, its verification, and its history.

Let me unpack each piece.

**Typed.** The refinement has a *kind*. There are not infinitely many kinds of changes a programmer makes; in practice, six shapes cover the great majority of work. A *knob* refinement adjusts a scalar value (a threshold, a rate, a flag). A *field* refinement adds, removes, or modifies a data field. A *symbol* refinement renames, moves, adds, or removes a function or module. A *policy* refinement creates, modifies, or retires a rule. A *composite* refinement bundles other refinements into one unit. A *pipeline* refinement orders a sequence of refinements that must land or revert together. These six shapes are not arbitrary; they correspond to the recurring patterns in how production codebases evolve. Each shape has different validation rules, different cascade behaviors, different review semantics. Typing the refinement lets the compiler reason about it precisely.

**Transformation.** The refinement *changes the system*. It is not a description, not a comment, not an annotation. It is an executable instruction to move the codebase from one state to another. When applied, it produces actual code changes — text on disk, files modified, commits created. When validated but not applied, it produces a precise statement of *what would change* if it were applied. The refinement is the work; the resulting diff is its observable trace.

**Of a subset of the codebase graph.** This is the most important phrase. The refinement is not a change to *the codebase* — it is a change to a *specific subset* of the codebase, and the subset is identifiable and bounded. The subset includes the primary target (the node where the change attaches) and the *cascade* — the nodes that must revalidate because the change reaches them. The subset is computed by the compiler; the refinement specifies the target and the compiler determines the rest. This is the foundational difference from a diff: a diff is a textual artifact that does not know what it touches semantically; a refinement is a semantic artifact that knows precisely what it touches.

**Carrying its cascade, its author, its verification, and its history.** The refinement is a self-describing object. It carries the cascade as data; it carries its author's identity (which may be a human or an agent); it carries the result of its verification (the gates that ran, the tests that passed, the policies that matched); it carries its history (when it was proposed, when it landed, by whom, with what predecessors and reversals). The refinement is, in this sense, the *complete* unit of change — not just the change but the attestation that surrounds it.

This is the definition. Memorize it; or, better, look at one.

## §2 — A refinement, illustrated

The simplest possible refinement in a real codebase looks like this.

At Sonibank Niger, the lending module has a policy value called `penalty_cap`. It controls the maximum penalty rate that can be applied to a late loan payment. The value is set to 18, meaning 18%. In the Q2 2026 risk review, the bank's risk committee decides that 18 is too aggressive for the current portfolio and lowers it to 16.

In the old workflow, an engineer would open the relevant file, find the line `penalty_cap = 18`, change it to `penalty_cap = 16`, run the tests, write a commit message ("Lower penalty cap per Q2 risk committee"), push, get the pull request reviewed, and merge. The diff would look like this:

```
-penalty_cap = 18
+penalty_cap = 16
```

This is, on its face, a perfectly clear change. A reviewer can read it in two seconds.

The trouble is everything that the diff doesn't say. It doesn't say *who decided this and on what authority* — there's a commit message, but the message is free-form prose, not a structured field. It doesn't say *what cascades from this change* — which functions revalidate, which tests rerun, which policies need to re-check. It doesn't say *whether the new value satisfies the BCEAO regulatory ceiling* — that check is presumably done by hand or by a separate compliance review. It doesn't say *who reviewed this with what authority* — the reviewer's approval is recorded, but their *role*, their *fit for reviewing risk policy changes*, is not. It doesn't say *what to do if this needs to be reverted* — the inverse change is presumably another commit, recomputed from scratch.

A refinement says all of these things, because they are part of what a refinement *is*.

Written in RFN — the Refinement Notation Language, which is Refine's textual surface — the same change looks like this:

**Listing 2.1 — `tighten_penalty_cap`, in RFN.**

```rfn
refinement tighten_penalty_cap {
  target  policy/penalty_cap
  from    18
  to      16

  policy  BCEAO-4.2
  author  amina@sonibank
  reason  "Q2 risk committee · ticket SBR-1284"

  gates {
    review_by  compliance_officer
    must_pass  tests/lending/*
    must_match policy/BCEAO-4.2
  }
}
```

Ten lines. Every field carries a specific kind of information. The `target` says *what part of the graph this attaches to* (a policy node, named `penalty_cap`). The `from` and `to` say *what the typed change is* (a knob, moving from 18 to 16). The `policy` says *which regulatory rule this answers to*. The `author` says *who is proposing this*. The `reason` is the human-readable why. The `gates` block says *what must be true before this can land*: a compliance officer must review it, the lending tests must pass, and the change must remain consistent with the BCEAO 4.2 policy.

When this refinement runs through the cascade-aware compiler, it produces several things. It produces the diff (which we still need; the code in the file does change). It produces the *cascade*: a list of every other node in the graph that the compiler determined must revalidate because of this change — perhaps the risk-assessment function, the loan-pricing function, two test files, and the BCEAO compliance rule. It produces the *verdict*: pass, gated (waiting on review), or fail. And it produces the *record* — a structured entry in the audit chain that an auditor can query three years later to answer the question the senior engineer at Sonibank couldn't answer.

The diff is still there. The diff is now an *output*, not the artifact. The artifact is the refinement.

## §3 — Why "of a subset of the graph" matters

The phrase that does the most work in the definition is *of a subset of the graph*. Let me dwell on it.

When a programmer changes a line of code, they are doing two things at once. They are changing the textual representation of the program — the bytes on disk — and they are changing the *behavior* of the program — what it does when run. These two changes are related but not identical. A textual change to a comment changes the representation without changing the behavior. A textual change to a function signature changes both the local behavior and the behavior of every caller. A textual change to a value in a data structure may change the behavior of nothing or of dozens of downstream consumers, depending on where that value is read.

The diff tells you the textual change. It does not tell you the behavioral change. The behavioral change is what the reviewer actually needs to know about, but the reviewer historically inferred it from the textual change by *holding the codebase in their head* — knowing, from experience, what a change to that file in that line is likely to affect.

This inference is the cognitive work that breaks at AI-generation speeds. The reviewer cannot hold the codebase in their head when the codebase is changing in ten different places at once, across files the reviewer has not opened in months.

The cascade-aware compiler does this work explicitly. Given a refinement, the compiler walks the graph from the target node and computes which other nodes must revalidate. The result is the *cascade*: an enumerated set of nodes that are affected. The reviewer reads the cascade — typically a handful of names — and gains, in seconds, the information that historically required minutes of mental simulation.

Crucially, the cascade is computed from a representation that the compiler maintains continuously: the codebase graph. The graph is not a side product; it is the primary representation. The text files on disk are how programmers happen to edit the graph, but the graph is what the compiler reasons about. This inverts the historical relationship — code as text, graph as derived view — to code as graph, text as derived view. We will return to this inversion at length in Chapter 3.

For now, accept that the graph exists, that the compiler maintains it, and that the *subset of the graph that a refinement touches* is a well-defined, computable thing.

## §4 — The six kinds

I claimed earlier that six kinds of refinements cover the great majority of changes a programmer makes in a production codebase. The claim deserves a little defense.

The six kinds — knob, field, symbol, policy, composite, pipeline — are not derived from a theoretical taxonomy. They are extracted from observing what actually changes in real codebases over time. Looking at three years of commits to the Sonibank codebase, sorting them by the *intent* of the change rather than the line count:

- About 35% are *knob* changes: a threshold moved, a rate adjusted, a flag toggled, a limit raised. Most of these correspond to business decisions — a risk committee, a pricing review, a regulatory update.

- About 25% are *field* changes: a column added to a schema, a new optional parameter, a removed property. Most of these correspond to evolving the data model as new requirements arrive.

- About 20% are *symbol* changes: a function renamed, a module moved, a helper extracted, a class deleted. Most of these correspond to maintenance — cleaning up duplication, aligning names, reorganizing.

- About 10% are *policy* changes: a regulatory rule added, a constraint tightened, an exception retired. Most of these correspond to compliance — new BCEAO directives, internal risk policies, operational rules.

- About 7% are *composite* changes: bundles of the above that must be coordinated. *"Add the credit-score field and update the eligibility function and the pricing function and the test suite, atomically."*

- About 3% are *pipeline* changes: sequences of related refinements with shared gates, typically corresponding to a quarterly compliance pass or a planned migration.

Together: about 100%. The remainder — pure refactors that don't fit any of the above, exotic operations like wholesale framework migrations — can usually be decomposed into the six kinds, or handled as a special case outside the refinement system (the "raw code" boundary we'll discuss in Chapter 3).

The six kinds are not the only way to slice the space. A different team in a different domain might find a different decomposition more useful. What matters is that *some* small set of kinds covers most of the work, and each kind has distinguishable semantics that the compiler can reason about. Six is the working set I've found; it has proven durable through pilots at Sonibank and conversations with teams in healthcare and infrastructure software.

The kind matters because it determines what the compiler does. A knob refinement asks the compiler to verify that the new value satisfies the constraints attached to the target node. A field refinement asks the compiler to compute which call sites are affected by the new field. A symbol refinement asks the compiler to verify that no caller is left dangling. A policy refinement asks the compiler to re-check every refinement that has previously matched against the affected policy. A composite refinement asks the compiler to coordinate atomic application of its members. A pipeline refinement asks the compiler to run gates across all members and either land all of them or none.

Each kind is a contract between the refinement author and the compiler. The author specifies what kind of change they intend; the compiler reasons accordingly. This is the typing relationship that makes refinement-oriented programming tractable.

## §5 — A refinement is not a wrapper around a diff

It would be easy, on first reading the previous sections, to conclude that a refinement is essentially a structured commit message — a way of attaching metadata to a diff that we would otherwise leave unstructured.

This is wrong, and the wrongness is important.

A structured commit message would be the diff plus metadata. The diff would still be the artifact; the metadata would be commentary. A reviewer would still read the diff to understand the change; the metadata would just help with classification, audit, search.

A refinement is not that. A refinement is the *artifact itself*. The diff is *derived* from the refinement when the compiler applies it. The reviewer reads the *refinement*, not the diff. The audit is built around *refinements*, not commits. The IDE shows *refinements*, with the resulting code as a secondary view.

This inversion has consequences. The most important one: the refinement carries *intent in a machine-readable form*. The compiler can act on the intent. The reviewer can read the intent. The auditor can query the intent. The agent can propose intent and have it validated before any text is generated. The intent is the thing; the code is the implementation.

A useful analogy: in a relational database, the artifact is not the SQL statement that updates a row; the artifact is the row itself. The SQL statement is the *operation* that produced the row, and we keep a log of operations, but the artifact we care about is the post-operation state, queryable, indexable, joinable. The diff is like the SQL statement. The refinement is more like the *change as a first-class entity*: not just *what bytes moved* but *what action was taken with what intent, by whom, against what authority, with what effect.*

If you've worked with event-sourced systems, the analogy is even closer: events are first-class, the current state is derived, audit is automatic because the events themselves are the audit trail. Refinement-oriented programming is, in part, event-sourcing applied to the act of programming.

> **Figure 2.1 — The unit changes.** The diff records which bytes moved; the refinement carries what the change *means* — its intent, its author, its blast radius, its proof, and its undo. The diff is derived output; the refinement is the artifact.

## §6 — What a refinement is not

To prevent overreach, a few explicit non-claims:

**A refinement is not a specification.** A specification describes what the system should do; a refinement describes a change to the system. The two interact — refinements often answer to specifications, and policies (which are a kind of specification) constrain what refinements can land — but they are different artifacts at different layers of abstraction.

**A refinement is not a *refinement* in the formal-methods sense — and the shared word is worth disarming.** There is a precise, fifty-year-old tradition that already owns this word. In the refinement calculus, and in the refinement-based methods used to build safety-critical systems — the B-method behind the driverless Paris Métro line 14, and its kin in Z and VDM — a *refinement* is a correctness-preserving step from an abstract specification toward a concrete implementation, each step discharging a proof obligation that the concrete preserves everything the abstract promised. It is a vertical movement, from idea down to code, done once, and what it buys you is *proof*. The refinement this book means is a different animal that happens to wear the same name: a governed *change* to an artifact that already exists — typed, attributed, validated against declared rules, cascade-aware, reversible — made continuously, by many hands, over the whole life of the system. Both are disciplined, validated movement toward a specification, and I claim the older tradition's lineage gladly; the name is not an accident. But the older refinement governs *correctness* — does this step preserve the properties? — while ours governs *governance* — may this change land, by whom, against which declared rule, and what does it touch? A reader who comes from formal methods should hold the two apart: this is the lighter, social, continuous cousin of the refinement calculus, not a claim to have automated proof. (Chapter 4 says plainly what the compiler does *not* do; proving programs correct is the first thing on that list.)

**A refinement is not a complete record of intent.** The `reason` field is a free-form string, and what goes into it is up to the author. A well-written reason explains the *why* in a way an auditor can verify; a poorly-written one says nothing useful. The system can enforce that the field is non-empty, but it cannot enforce that the content is meaningful. Discipline still matters.

**A refinement is not a substitute for human review.** It is a *different* artifact for human review than the diff. The reviewer reads the refinement instead of the diff; the reviewer's judgment is still required. What changes is *what the reviewer judges*: not "is this code correct" but "does this refinement express a valid intent against a verified cascade." That is still a judgment, but it is a judgment a human can make at the pace agents produce work.

**A refinement is not a replacement for tests.** The gates clause references tests; tests still run; tests still catch errors that the type system cannot. The refinement is the *unit of change*; tests are the *verification of behavior*. Both are necessary.

**A refinement is not unique to AI-assisted code.** Refinement-oriented programming works for purely human-authored code, too. The benefits — better attestation, faster review, automatic cascade — are useful regardless of who wrote the code. The argument that it is *necessary* hinges on AI; the argument that it is *useful* does not.

## §7 — A small thought experiment

Imagine, for a moment, a different version of the senior engineer's conversation at Sonibank.

Three years ago, the BCEAO auditor asks: *why is the penalty cap 16 percent?*

The engineer pulls up the audit chain. The chain returns a refinement: `tighten_penalty_cap`, landed on May 30, 2026, by amina@sonibank, with reason *"Q2 risk committee · ticket SBR-1284"*, applied against policy BCEAO-4.2, reviewed by the compliance officer, with gates passed: tests/lending/* and policy match. The chain also returns the predecessor: `set_penalty_cap`, landed 2019, by a different author, with reason and policy.

The auditor doesn't ask the engineer to remember anything. The auditor doesn't ask the engineer to read the code. The auditor reads the refinements, follows the policy reference to the BCEAO regulation, sees that the chain is intact, and moves on.

This is the version of the audit conversation that the existing tools cannot produce, no matter how hard the team tries, because the existing tools don't have refinements as artifacts. The closest they have is commit messages, which are free-form prose; the prose is sometimes good and often not, and there is no way for the auditor to know in advance which.

Refinement-oriented programming is the discipline of *making sure the audit conversation always goes that way*, by making the refinement — not the commit — the primary artifact, and by maintaining the audit chain as an automatic consequence of how work is done, not as a manual overhead on top of the work.

There is a second clock in that conversation, and it is worth separating from the first. The dates in the chain above — *landed May 30, 2026*, *landed 2019* — are **transaction time**: when Sonibank *recorded* each decision. But the auditor's real question is often about a different clock. Not *when did you change the cap* but *what cap was in force during the quarter I am reviewing* — **valid time**, the interval over which a rule actually governed loans in the world. Most of the time the two clocks move together. The cases that end careers are the ones where they don't.

The sharpest is retroactive regulation. A BCEAO circular issued in July is declared effective from April. A system with a single clock cannot tell the truth about this: it can make the new cap look as though it had always been there (false), or as though it began in July (also false). The honest record needs both intervals — *valid from April, recorded in July* — and it must answer either question without rewriting history. An engineer asked in August what the bank's policy *was* in May has to return the value that was in force then, separately from the fact of when each version was entered.

This bi-temporal discipline is old in temporal databases, and in the agent-memory world it is most visible in Graphiti, which keeps exactly these two clocks on every fact and retires a superseded one with a closing date rather than deleting it. Refinement-oriented programming wants the same rigor pointed at governed change rather than ingested knowledge: a refinement carries not only *when it landed* but *when the rule it encodes took and lost force*, and a superseded policy edge is closed, not erased. The audit chain already keeps the recording clock faithfully; the world's clock is the other half, and a regulated codebase needs both. (The mechanics — how valid time is captured and queried — are worked out in the memory specification.)

## §8 — What this chapter has established — and what it has not

What the chapter has established:

- A refinement is a typed transformation of a subset of the codebase graph, carrying its cascade, its author, its verification, and its history.
- Six kinds — knob, field, symbol, policy, composite, pipeline — cover the great majority of changes a production codebase actually receives.
- The refinement is the artifact; the diff is derived output. The reviewer reads intent and impact, not bytes.
- The audit conversation changes shape: the auditor reads refinements and follows policy references instead of interrogating human memory.
- The honest record needs two clocks — when a rule was in force and when it was recorded — and keeps both.

What it has not established:

- A refinement is not a specification, not a formal-methods refinement, not a guarantee that its stated reason is meaningful, and not a substitute for human review or for tests — the non-claims of §6 stand.
- That six kinds are the final taxonomy. A different team in a different domain may slice the space differently; what matters is a small typed set the compiler can reason about.

The next chapter explains why this requires the codebase to be represented as a graph.

---

# Chapter 3 — The codebase as a graph

*Where a refinement lives: the codebase as one typed graph rather than a tree of text files.*

For most of programming's history, the canonical representation of a codebase has been a tree of text files.

This is a remarkable fact. We have, since at least the 1970s, treated source code as a hierarchy of named text files in named directories. Editors edit files. Version control versions files. Diffs compare files. IDEs open files. The text-files-in-folders representation is so deeply embedded that most programmers don't recognize it as a *choice*; it feels like the natural form of code.

It is not the natural form of code. It is one possible form, useful for some purposes, increasingly inadequate for others. This chapter is about why a different representation — the codebase as a graph — is what refinement-oriented programming requires, and why that representation is more honest to what code actually *is* in the agentic era.

## §1 — What's in a codebase, really

When you look at a codebase — a real production system — what's in it?

Files, of course. But also: functions defined in those files. Classes. Modules. Types. Schemas. Constants. Configuration values. Policies (codified business rules, sometimes scattered across multiple files). Tests. Documentation. Build configurations. Deployment manifests. Database migrations. API contracts. Localization strings. Feature flags.

And, more importantly, the relationships among these things. Function A calls function B. Class C inherits from class D. Module E imports module F. Schema G is read by service H. Policy I constrains function J. Test K verifies function L. Configuration M is consumed by deployment N. Feature flag O gates code path P.

A codebase is, in any meaningful sense, a *web* of typed entities with typed relationships. The files are how we store this web on disk. The web itself is what the program *is*.

When you read code, you trace the web. *What does this function call? Where is this constant used? What changes when I modify this schema? Which tests will fail if I rename this class?* These are graph traversals. They are the actual cognitive operations of understanding code, and they are mediated by the graph, not by the file structure.

The file structure is, in fact, often an *obstacle* to understanding the graph. A function and the function that calls it may be in different files. A schema and its consumers may be in entirely different parts of the directory tree. A policy may be encoded as scattered conditionals across a dozen files. The file structure organizes the graph for the convenience of editing, not for the convenience of reasoning.

Refinement-oriented programming makes the graph primary. The text files still exist; they are how programmers edit, how version control records, how diffs are computed. But the *primary representation* — the one the compiler reasons about, the one the IDE displays, the one refinements operate on — is the graph.

> **Figure 3.1 — The same codebase, two representations.** The tree shows where text lives; the graph shows how the parts relate — calls, depends-on, and the *satisfies* edge that ties code to the requirement it serves.

## §2 — What a node is

The graph has nodes and edges. Let me describe the nodes first.

A **node** in the codebase graph corresponds to a meaningful entity in the program. The set of node kinds is open — different languages and frameworks will introduce new kinds — but a useful starting set includes:

- *Modules*: namespaces, packages, source files (treated as nodes themselves, in addition to containing other nodes).
- *Functions and methods*: callable units with signatures.
- *Types and classes*: schemas for values, including their fields.
- *Constants and configuration values*: named scalar values, including policy values like `penalty_cap`.
- *Policies*: codified rules, possibly with constraints (e.g., "BCEAO-4.2 requires penalty_cap ≤ 18").
- *Tests*: verification units, with the entities they test attached.
- *Schemas*: data shapes used by databases, APIs, message queues.
- *Deployments*: stages, environments, with the artifacts they consume.

Each node has a *type* (which kind it is), a *name* (its path in the graph, like `policy/penalty_cap` or `module/lending/eligibility`), an *identity* (a stable identifier that survives renames), and a set of *attributes* specific to its kind.

This may sound elaborate, but most of it is mechanical. The compiler extracts the graph from the source code automatically: it parses each file, identifies the entities, assigns identities, computes relationships. The programmer does not maintain the graph manually; the programmer maintains the source code (as before), and the compiler maintains the graph as the source code changes.

The interesting cases are the ones that *aren't* mechanical — policies, schemas, deployment configurations — because these often live in formats outside the source language. A BCEAO regulatory rule may live in a YAML file or a database; a deployment configuration may live in Terraform; a schema may live in OpenAPI. The graph integrates these by treating each external format as a *graph fragment* that contributes nodes and edges to the unified graph. The compiler doesn't need to understand every format; it needs to understand *which formats contribute which kinds of nodes*, and it needs adapters to translate between them and the graph representation.

This is a substantial engineering task. It is not, however, a conceptual obstacle. The graph exists in principle whether or not the tooling has been built; the tooling determines how much of the graph the compiler can reason about automatically and how much the programmer must annotate.

## §3 — What an edge is

The graph has edges of several kinds, each carrying different semantics.

- *Call edges*: function A calls function B.
- *Reference edges*: function A reads or writes constant C.
- *Type edges*: class D extends class E; field F has type G.
- *Import edges*: module H imports module I.
- *Schema edges*: function J consumes schema K, produces schema L.
- *Policy edges*: function M is constrained by policy N.
- *Test edges*: test O verifies function P.
- *Deployment edges*: stage Q consumes artifact R.

Edges have a *kind*, a *source node*, and a *target node*. Some edges have additional attributes — call edges may record arity and conditionality, policy edges may record the specific clause being constrained.

What makes the graph powerful for refinement-oriented programming is that *all of these edges are first-class*. A traditional codebase tracks some of them (the compiler knows about call edges; the type checker knows about type edges) but treats others as implicit (policies, deployment dependencies, test coverage relationships often live in separate systems with no shared representation). The refinement compiler unifies them: every edge, regardless of kind, contributes to the cascade computation.

When you change a value at a node, the cascade walks the edges outward, computing which other nodes are affected. The walk respects edge semantics — a change to a constant cascades along reference edges; a change to a function signature cascades along call edges *and* type edges; a change to a policy cascades along policy edges and may trigger re-checks of every refinement that previously matched. The walk terminates when it reaches nodes that are not affected (because, for example, the type system can prove the change is compatible) or when it reaches the boundary of the graph (the edges of the represented system).

## §4 — The graph is not a model; it is the working representation

A common pattern in software engineering is to maintain a *model* of the system alongside the system itself. UML diagrams, architecture documents, design specifications — these are models of a codebase that exist separately from the codebase. They are useful for communication but they suffer a chronic problem: they go stale. The system changes; the model does not, or it does but slowly. Within a year of writing, most architecture documents are partially false.

The graph is not a model in this sense. The graph is the *working representation*, maintained continuously by the compiler. When source code changes, the graph changes immediately. There is no opportunity for the graph to go stale because there is no separate authoring step; the graph is computed from the source.

This is a strong claim, and it has implications.

It means the graph is always *correct in the same sense the source is correct*. If the source has bugs, the graph reflects those bugs faithfully. If the source is well-organized, the graph is well-organized. The graph does not improve on the source; it represents the source in a different form. The improvement, if any, comes from being able to *reason about* the source through the graph in ways that text-file-based reasoning could not support.

It means refactoring the graph and refactoring the source are the *same operation*. There is no "update the graph to reflect the new structure" step. The source changes; the graph follows. Or, in some operations, the graph changes (in the IDE, by direct manipulation); the source follows. Either direction works; the relationship is bidirectional and synchronous.

It means the graph is, in a meaningful sense, the *truth* about the codebase. When two programmers disagree about how a system is structured, the graph settles the disagreement: walk the edges, see what calls what, see what depends on what. The graph isn't always right (it can only represent what's been encoded), but it is *consistent*, in a way that mental models and documentation are not.

## §5 — Subsets of the graph

With the graph defined, we can return to the phrase that did so much work in Chapter 2: *a subset of the codebase graph*.

A subset is a collection of nodes (and the edges among them) that constitutes the scope of a particular refinement. The subset is not arbitrary; it is *computed*, by the cascade-aware compiler, from the refinement's target.

When you propose a refinement, you specify a *target node*. The target is where the change attaches: the policy value you're moving, the schema field you're adding, the function you're renaming. The target is the seed.

From the target, the compiler walks the graph along edges that propagate the change. The propagation rules depend on the refinement kind and the edge kind. A knob refinement on `policy/penalty_cap` propagates along reference edges to every function that reads the value. A field refinement on `schema/loan_record/credit_score` propagates along schema edges to every function that consumes the schema. A symbol refinement renaming `compute_score` propagates along call edges to every caller. A policy refinement on `policy/BCEAO-4.2` propagates along policy edges to every refinement that previously matched against the policy.

The walk produces the cascade: the set of nodes the change reaches. The cascade is the *subset of the graph* that the refinement operates on.

This is where the agentic-era reviewer's attention can settle. Not on the diff (textual, often misleading, of unknown scope). Not on the entire codebase (impossible to hold in mind at agent speeds). On the *subset of the graph the refinement reaches*: a bounded, computed, human-readable enumeration of what is affected.

A typical cascade has between three and twenty nodes. A reviewer can read twenty node names in seconds. The reviewer's question becomes: *given that this refinement touches these specific nodes, is the change still appropriate?* That is a question a human can answer in the agentic era.

## §6 — Why the graph requires the compiler to maintain it

You might reasonably ask: if the graph is so useful, why don't we just have programmers maintain it directly? Why couple it to the compiler?

The answer is that human-maintained graphs go stale the moment the human's attention moves elsewhere. Every architecture document confirms this; every "system overview" diagram that turns out to be three years old confirms this. Humans are bad at keeping ancillary representations in sync with the primary artifact, because keeping things in sync is dull work and the secondary artifact provides no immediate feedback when it falls out of date.

The graph has to be machine-maintained, derived from the source, and updated continuously. This means the graph requires a compiler that *understands the source well enough to extract it*. The compiler in question is more sophisticated than a traditional language compiler: it must extract not just the program's semantics but the relationships among entities, across files, across languages, across formats. It must integrate adapters for whatever formats the team uses. It must update incrementally as files change.

This is doable. It is doable today, for many languages and many formats. It is not trivial; it requires real engineering investment in the compiler. But the alternative — humans maintaining the graph manually — is a known failure mode that we have already tried, many times, under different names, and it has not worked.

Refine is one implementation of this kind of compiler. Other implementations will follow. The point is not the specific implementation; the point is that the discipline of refinement-oriented programming *requires* a compiler that maintains the graph automatically. Without that, you cannot compute cascades, you cannot validate refinements, you cannot run gates against a current representation of the system. The whole paradigm depends on the graph being live.

## §7 — A note on raw code

A practical reality: not every part of a real codebase will be representable in the graph from day one. Some files are too messy. Some legacy systems use frameworks the compiler doesn't yet understand. Some configurations live in formats nobody has written adapters for. Some code is, frankly, written by humans who have not yet adopted the discipline of structuring their code in graph-amenable ways.

This is fine, and the paradigm explicitly accommodates it.

A codebase under refinement-oriented programming has two regions: *anchored* code (parts of the codebase that contribute to the graph, where refinements can attach) and *raw* code (parts that don't, where changes happen the old way, via direct text editing and ordinary commits). The boundary between the two is explicit. A team can adopt refinement-oriented programming progressively, anchoring more of the codebase over time.

This is not a compromise; it is a design feature. The alternative — demanding that the entire codebase be anchored before any refinement-oriented work can happen — would be impossible for any team with a large legacy codebase. The paradigm has to coexist with the existing world, and the anchored/raw boundary is how it does.

What matters is that for the parts of the codebase that are anchored, the discipline holds: every change is a refinement, every refinement carries its cascade, every cascade is computed against the live graph. For the raw parts, the old workflow continues, with the old strengths and the old weaknesses. Over time, teams typically move more of their codebase into the anchored region as they see the benefits.

## §8 — What the graph buys you

A summary of what we get from making the graph primary:

- **Cascades become computable.** Given any proposed change, the compiler can enumerate what it reaches. The reviewer reads the cascade, not the diff.

- **Impact analysis becomes a query, not a guess.** *What touches this constant?* is no longer "let me grep and hope." It is a graph query, answered exactly.

- **Refactorings become safe.** Renaming a function rewrites every call site automatically; the graph identifies them all. Removing a field flags every consumer.

- **Policies become enforceable.** A regulatory rule attached to a node propagates to every refinement that touches the node. There is no way to "forget" to check compliance; the compiler checks.

- **Audit becomes structural.** Every refinement records the cascade it touched, the gates it passed, the author who proposed it. The audit chain is a graph traversal, not a forensic exercise.

- **Agents get a tractable interface.** An agent proposing a refinement is operating on a structured, queryable representation, not on raw text. The agent's proposal can be validated mechanically. The agent's mistakes — when they happen — are bounded by the graph it operates on.

- **The audit chain survives across authors.** Whether a refinement was proposed by a human or an agent, it is the same artifact, with the same metadata, in the same graph. The continuity that the agent cannot provide is provided by the graph.

There is one more thing the graph makes possible, and it is the one I underrated longest: the graph does not only let the compiler *govern* the codebase; it lets a newcomer *understand* it. For most of this project I thought of the graph as an instrument of control — the thing the compiler reads to validate a change. But the graph the compiler reads to validate a change is the same graph a person reads to learn the system, and that turns out to matter enormously, because understanding a large codebase is the first and most universal pain in software work. You join a team; the codebase is two hundred thousand lines; where do you even start?

The tools that answer that question — parse the source, build a graph of files and functions, walk a newcomer through it — are good, and they carry a design creed I have come to believe is exactly right: *graphs that teach beat graphs that impress.* A diagram that dazzles teaches nothing; a diagram that walks you through the system in the order its pieces depend on each other teaches everything. But those tools teach a codebase's *shape* — what calls what — and the shape is the shallow part. What a newcomer actually needs is *why*: which policy this constant serves, which requirement this function exists to satisfy, what breaks if they touch it, who changed it last and for what reason. A graph built from syntax alone cannot answer those questions, because the answers are not in the syntax — they are in the policy facet, the logframe, the cascade, the audit chain. And in Refine those are not separate documents to be cross-referenced; they are edges in the same graph. So Refine can teach a codebase the way no structural tool can: not its shape but its *meaning* — what this is, why it exists, what it serves, what it would break, who shaped it. Five facets, one explanation, and none of it able to drift from the code, because it *is* the code's graph.

It is worth stepping back to see what kind of thing this makes the graph. So much of this field now organizes itself around a graph of one kind or another: graphs that **teach** a codebase, graphs that **remember** what an agent has learned, graphs that **recommend** which tools to bring to a task. Each is real. Refine's graph does a fourth thing those do not — it **governs**: every node a typed, validated, attributed, reversible change. The teaching is a gift the governing graph gives almost for free, because the same edges that let the compiler check a change are the ones that let a newcomer learn the system. Graphs that teach, remember, recommend — and, here, govern.

This is why I now insist that teaching the codebase is not a feature to bolt on but a first-class output of the whole design. The same governance that makes a change safe makes exploration safe — every change previewed, every change reversible — so a learner can build a mental model the best possible way: by safely poking the running system and watching the consequence cascade across code, UI, and data before anything commits. The codebase that governs change well should also be the codebase that teaches itself — to the newcomer on their first day and to the agent on its first query alike. *The community's comprehension tools teach the structure; Refine teaches the meaning, and the same graph does both.*

The graph is, in this sense, *what makes the rest possible*.

## §9 — What this chapter has established — and what it has not

What the chapter has established:

- A codebase is a web of typed entities and typed relationships; files are how the web is stored, not what the program is.
- The graph is the working representation, maintained continuously by the compiler — not a model that can go stale.
- The subset of the graph a refinement touches is computed, not guessed, and that subset is where reviewer attention can settle.
- The anchored/raw boundary lets the paradigm coexist with legacy code and be adopted progressively.
- The governing graph also teaches: the same edges that let the compiler check a change let a newcomer learn the system's meaning, not just its shape.

What it has not established:

- That the whole codebase must live in the graph. Raw regions are a design feature, not a failure, and some parts of a codebase may stay raw indefinitely, by choice.
- That graph extraction is free. The adapters and the incremental maintenance are real engineering, and how much of the graph the compiler sees depends on that investment.

The next chapter shows what the compiler does with the graph: how it turns refinements into verdicts, how it computes cascades, how it runs gates, and what the architecture of the cascade-aware compiler looks like.

---

# Chapter 4 — The compiler that revalidates

*The thing that checks a change before it lands — four deterministic stages, and an honest account of what it does not do.*

The traditional compiler does one job: it turns source code into something the machine can execute. The cascade-aware compiler does a related but different job: it turns *proposed refinements* into *verdicts*, computing along the way which parts of the system are affected and whether the gates surrounding the change are satisfied.

This chapter walks through what the cascade-aware compiler does, when it runs, and what it can and cannot guarantee. The goal is to make the compiler's role concrete enough that a programmer can understand its place in the workflow, and skeptical enough that nobody mistakes the compiler for a substitute for human judgment.

## §1 — The lifecycle of a refinement

A refinement goes through eight steps from proposal to landing. The compiler is responsible for steps two through seven.

**Step 1 — Authoring.** A human or an agent writes the refinement. In the IDE, this might mean adjusting a knob in a panel; in RFN, it means writing a `.rfn` file; via the MCP server, it means an agent sending a structured proposal. The output of authoring is a refinement object: target, kind, fields, gates.

**Step 2 — Parsing.** The compiler reads the refinement object and validates its syntactic structure. The kind is recognized; required fields are present; the target is a syntactically valid graph path. Errors at this stage are rejection-with-precise-location: the refinement is malformed and cannot proceed.

**Step 3 — Resolving.** The compiler resolves references: imports are loaded, templates are expanded, target paths are bound to nodes in the live graph. Errors here include unresolvable targets (the path doesn't correspond to any node), missing imports, undefined template parameters.

**Step 4 — Type-checking.** The compiler checks that the refinement's kind-specific contract is satisfied. For a knob refinement, the `from` value must match the current state and the `to` value must satisfy the target's constraints. For a field refinement, the field must not already exist (if adding) or must exist (if modifying). For a symbol refinement, the renamed symbol must be a valid identifier; the old symbol must exist. Errors here mean the refinement is internally consistent but semantically wrong.

**Step 5 — Cascade computation.** This is the central act. The compiler walks the graph from the target node, applying propagation rules for the refinement's kind and the edges' kinds. The result is the cascade: a set of nodes that revalidate. The cascade is recorded as a structured object on the refinement. If the refinement declared an expected cascade (a rare but useful pattern for high-assurance work), the compiler compares the computed cascade to the declared one and fails on mismatch.

**Step 6 — Gate execution.** Each gate in the refinement's `gates` block is executed. A `review_by` gate blocks until the named role approves. A `must_pass` gate runs the referenced test suites. A `must_match` gate checks the change against the referenced policy. A `budget_at_most` gate verifies the agent's token spend. Gates can pass, wait, or fail. A waiting refinement is *gated* — it has not failed, but it cannot land yet.

**Step 7 — Application.** If all gates pass, the compiler applies the refinement. The textual changes are computed and written to the source files. The graph is updated. A Git commit is created with structured trailers carrying the refinement's metadata. The refinement is recorded in the audit chain. The inverse refinement is pre-computed and stored, ready for revert.

**Step 8 — Recording.** The compiler emits the final record: refinement applied, commit hash, author, cascade summary, gate results, timestamp. The record enters the audit chain. Notifications fire (the on_success block, if present). The refinement is now part of the codebase's history.

The compiler is responsible for steps 2 through 7. Step 1 is human or agent work; step 8 is mechanical accounting. Within the compiler's domain, every step is deterministic: given the same refinement and the same graph state, the same verdict every time. This determinism is what makes the compiler usable in continuous integration, in automated agentic workflows, in audit replays.

> **Figure 4.1 — The lifecycle of a refinement.** Eight steps from authoring to record; the compiler owns steps two through seven, and within its domain every step is deterministic — same refinement, same graph state, same verdict.

## §2 — What "deterministic" means here

The determinism claim deserves a closer look, because it is doing important work.

A traditional compiler is deterministic in a similar sense: given the same source, the same binary. The cascade-aware compiler is deterministic in a generalized sense: given the same refinement and the same graph state, the same verdict — including the same cascade, the same gate results (for purely computational gates), the same applied change.

For gates that depend on human review, "deterministic" is conditional: given the same refinement and the same reviewer decision, the same outcome. The compiler doesn't make the review decision; it records it.

For gates that depend on external systems — test runs, policy services — determinism is conditional on those systems' determinism. If a test suite is flaky, the gate result will be flaky. This is a known limitation, not a flaw in the paradigm: flaky tests are bad for many reasons, and the compiler's determinism makes their flakiness more visible, not less.

What determinism buys: an audit replay. Three years after a refinement lands, an auditor can re-run the validation against the graph state at the time of landing and verify that the verdict the compiler reported was the verdict it should have reported. The validation is reproducible. This is a property the existing tools cannot give you, because the existing tools have no representation of "the validation that ran"; they have only the code review comments and the test outputs, which may or may not be preserved.

## §3 — Gates: what blocks landing

Gates are the explicit preconditions a refinement must satisfy. They are the most operationally important part of the compiler's work, because they are where human judgment, automated verification, and policy enforcement meet.

There are seven gate kinds in the current Refine implementation. Other implementations may have more; the set is open. The seven are:

**review_by** — a named role must approve. The role is resolved against the project's identity registry. If the role has multiple holders, any one of them may approve. If the role is unfilled, the gate cannot pass; the refinement is blocked until someone is assigned.

**must_pass** — a test suite (or test pattern) must pass. The compiler invokes the test runner against the post-refinement state of the code. The test runner reports pass or fail. The gate inherits the report.

**must_match** — a named policy must be satisfied. The policy is a structured object specifying constraints on the target. The compiler checks the post-refinement state against the policy. Mismatch fails the gate.

**budget_at_most** — the cumulative cost of agent work on this refinement must not exceed a limit. Used when refinements are proposed by agents whose token spend the team is tracking.

**agent_provenance** — the proposing agent's identity must be verified. If the agent's credential is expired, revoked, or absent, the gate fails. This is the gate that prevents anonymous agentic work.

**signed_by** — a cryptographic signature is required, typically for high-assurance contexts. The signature is verified against the named identity's key.

**on_fail** — strictly speaking not a gate but a directive: it specifies what happens when any other gate fails. The most common values are `revert_all` (in pipelines, undo any partial progress) and `notify` (alert a named channel).

Gates can be declared per refinement (in the refinement's `gates` block) or per path (in the project's configuration). Path-level gates apply to every refinement that touches the path. A typical project has very few per-refinement gates (the author specifies what review the change needs) and a substantial set of path-level gates (the project specifies what every change to `policy/*` must go through).

The path-level gates are how compliance teams encode their requirements once and apply them automatically forever. *"Every change to anything matching `schema/loan_record/**` requires must_pass on tests/lending/* and review_by compliance_officer."* Stated once in the config; enforced on every applicable refinement; no opportunity to skip.

This is what the agentic era requires that the old tools could not provide: *enforcement of policy at change time, not at audit time*. An auditor reviewing old commits could discover that a compliance check was missed; the audit would be a finding, not a fix. Gates prevent the miss in the first place. The refinement cannot land if the gate is not satisfied.

## §4 — Cascade computation in detail

The cascade computation is the compiler's signature operation. It deserves a more careful look.

Given a refinement with a target node, the compiler performs a graph walk to determine which other nodes are affected. The walk is constrained by the refinement's kind and the edges' kinds.

For a knob refinement (a scalar change), the propagation rule is:

> From the target, follow reference edges to all nodes that read the value. For each such node, determine whether the read is *sensitive to the change* (the function uses the value in a way that the change affects) or *insensitive* (the function reads the value but the change doesn't alter behavior). Add sensitive readers to the cascade.

Determining sensitivity is sometimes tractable (a function that uses the value in an arithmetic computation is almost always sensitive) and sometimes not (a function that passes the value to a closure with unknown behavior is opaque). When sensitivity is uncertain, the compiler conservatively assumes sensitivity and adds the node to the cascade. The reviewer sees the cascade; the conservatism is visible and overridable.

For a field refinement (schema change), the propagation rule is:

> From the target schema, follow schema edges to all functions that consume the schema. For each consumer, determine which fields are read. If the changed field is read, add the consumer to the cascade. If the field is written, the cascade also includes the write site and any downstream consumers of the written value.

For a symbol refinement (rename/move/remove), the propagation rule is:

> From the target symbol, follow call edges (if the symbol is callable) and reference edges (if the symbol is referenced as a value). All callers and referencers enter the cascade. For renames, the cascade nodes have their references mechanically rewritten as part of application. For removes, the cascade is informational: each caller must be examined to determine if removal is safe.

For a policy refinement, the rule is conceptually different:

> When a policy is added, modified, or retired, the cascade includes every refinement that has previously matched against the policy. These refinements are re-checked against the new policy; any that no longer satisfy it are flagged.

Composite and pipeline refinements compute cascades by unioning the cascades of their constituents and resolving conflicts (e.g., two constituent refinements that touch the same node must be ordered).

The walks terminate when they reach nodes outside the represented graph (the boundary between anchored and raw code) or when the compiler can prove no further propagation is needed.

Cascade computation is, in practice, fast. Modern graph databases — and the compiler's internal graph is essentially a specialized graph database — can perform walks of hundreds of nodes in milliseconds. The bottleneck is not the walk; it is the *quality of the graph being walked*. A well-anchored codebase produces precise cascades; a poorly-anchored codebase produces conservative cascades (over-inclusive, because the compiler can't prove non-impact). Over time, as anchoring improves, cascades sharpen.

## §5 — What the compiler does not do

It is worth being explicit about the limits, because the compiler's job is easily overstated.

**The compiler does not verify correctness — it is not a theorem prover.** A refinement that type-checks, passes its gates, and lands successfully may still produce incorrect behavior in production. The compiler verifies *the things it can verify*: structural consistency, declared gates, the cascade. It does not prove the change correct against a full specification the way a verification-aware language or a proof assistant does — and this is the right place to retire the confusion the shared word *refinement* invites (Chapter 2, §6). Formal refinement, in the calculus of that name, discharges a proof obligation; our refinement discharges a *governance* obligation. The choice is deliberate: proof is expensive, expert-only, and undecidable in general, and most changes are not worth it, while governance, attribution, cascade, and reversibility are worth it for *every* change. *Valid is not wise, and valid is not proven-correct.* Where a single constraint genuinely warrants proof — a safety invariant in a regulated core — the honest move is to compose: hand that one constraint to a solver and let its verdict become a gate input, the same way tests and evals do. The compiler stays the governor; the prover advises. Correctness in the broad sense is what tests, runtime monitoring, and human review provide, independent of the compiler.

**The compiler does not understand intent.** The `reason` field is opaque to the compiler. It is recorded; it can be queried by auditors and reviewers; it cannot be checked for accuracy or meaningfulness. A refinement with a thoughtless reason is structurally identical to one with a carefully-considered reason. Discipline in writing reasons is a cultural property of the team, not a compiler-enforceable one.

**The compiler does not prevent bad design.** A refinement that lands a poorly-designed change — one that is structurally sound but architecturally regrettable — is still a refinement. The compiler can flag changes that violate explicit constraints (a policy match would fail) but cannot detect changes that violate good taste or long-term system health. Those judgments remain human — and they have grown interesting enough to deserve their own section, just below.

**The compiler does not eliminate the need for review.** It changes *what is reviewed* — the refinement, not the diff. It does not remove the review step. Reviewers still need to read refinements, evaluate them, and decide whether to approve. The compiler makes the reviewer's job tractable; it does not eliminate the job.

**The compiler does not solve agentic trust.** An agent that proposes a malicious or careless refinement is constrained by gates (must pass review, must pass tests, must match policy) but is not, by virtue of those gates alone, made trustworthy. Trust is built over time, through evaluation, provenance tracking, and the slow accumulation of attestation. The gates are the safety mechanism; trust is the longer game.

These limits are not weaknesses to be apologized for. They are the proper scope of the compiler. A compiler that claimed to solve all of them would be overpromising; a compiler that claimed less would be underutilizing its actual capability. The cascade-aware compiler does what compilers do best — mechanical, deterministic, structural reasoning — and leaves the rest to the social and cultural systems around it.

## §6 — Taste, and the context advantage

It is worth being exact about the judgments the compiler leaves to humans, because the field is now trying to write taste down. A tool like Kun Chen's *OPINIONS.md* maintains a living map of a person's durable judgment — what they believe makes a good design, a good agent, a good trade-off — and feeds it to agents so their proposals come back closer to what that person would actually want. This is a genuinely useful thing, and it is tempting to imagine the next step: if taste can be written down, can the compiler enforce it? The answer this paradigm gives is a firm no, and the firmness is the point. Taste may be *declared* — held as advisory context, attributed to the person whose taste it is, surfaced to the agent when it proposes and to the reviewer when they read — but it must **never become a gate**. You cannot compile *"prefer agents that gather evidence over agents that demo well"* into a structural check, and a compiler that pretended to would collapse the one distinction the whole paradigm rests on. A requirement is declared *and gated*; taste is declared *and surfaced, never gated*. Writing your judgment down makes the agent's first draft better; it does not, and must not, make any change more *landable*. Declaring wisdom is allowed; gating on it is not.

There is a sharper name for the part of this that is *not* taste, and it matters. Andrew Ng, writing about how this work now goes, argued that the human's irreplaceable contribution is less a matter of taste than of a **context advantage** — knowing something the model does not — and that the job is to *inject that knowledge into the system*. The reframing splits the human's contribution cleanly in two. Some of what a team calls taste is really context it has simply not written down yet — a regulation, a constraint, a hard requirement — and that does not belong *beside* the gate, advisory and ignorable; it belongs *in* it, declared as intent the compiler enforces. The rest — the genuine aesthetic and product judgment that cannot be reduced to a checkable rule — stays advisory, and never gates. The whole discipline is telling the two apart, and resisting the easy move of calling injectable knowledge "taste" so it can be waved through. Most of what deserves to be gated and isn't is not taste at all; it is knowledge nobody bothered to declare.

## §7 — What a verdict looks like

When a refinement runs through the compiler, the output is a *verdict*: a structured record of what happened. The verdict is short, readable, and queryable.

A successful verdict for the `tighten_penalty_cap` refinement might look like:

**Listing 4.1 — A verdict that lands.**

```text
Status:      validated, applied
Refinement:  tighten_penalty_cap (ref-2026-05-30-c40e)
Author:      amina@sonibank
Cascade:     4 nodes — policy/penalty_cap, module/lending/risk_assessment,
             module/lending/loan_pricing, rule/bceao_compliance
Gates:       review_by compliance_officer        passed
             must_pass tests/lending/*           47/47 passed
             must_match policy/BCEAO-4.2         matched: cap 16 ≤ ceiling 18
Commit:      7a4f2cd
Applied:     2026-05-30 14:55:08 UTC
Inverse:     pre-computed, ref-id reserved
```

This verdict is what enters the audit chain. It is what an auditor reads three years later when asked *why is the penalty cap 16 percent?* The verdict points to the refinement, which carries the reason; the reason points to the ticket; the ticket points to the risk committee decision. The chain is complete and walkable.

A failed verdict might look like:

**Listing 4.2 — A verdict that refuses, and says why.**

```text
Status:      failed, not applied
Refinement:  rename_score_function (ref-2026-05-31-7b3a)
Author:      kofi@sonibank
Cascade:     3 nodes — module/lending/compute, module/lending/eligibility,
             tests/lending/test_score
Gates:       must_pass tests/lending/*           FAILED:
             tests/lending/test_score has a stale reference to
             compute_score on line 142
Failure:     caller in test file was not updated by the refinement;
             manual fix or pipeline composition required.
```

This verdict is also useful. The author sees, immediately, what went wrong and where. The verdict is not a generic "test failed" message; it identifies the specific stale reference, in the specific file, on the specific line. The author can fix it and try again — or compose the rename refinement with an explicit test-update refinement into a pipeline that lands them atomically.

The verdict is structured. Tools can query verdicts: *show me all failed refinements from last week, grouped by gate*. *show me which agent's refinements have the highest revert rate*. *show me refinements that touched policy/BCEAO-* across the last quarter*. The structured verdict is the primary mechanism for operational visibility into AI-augmented programming.

## §8 — When the compiler runs

Different surfaces invoke the compiler at different points:

In the **IDE**, the compiler runs continuously: as the author edits a refinement, the cascade is recomputed and shown in the side panel. The verdict is live; the author sees the consequences of their proposed change before committing to apply it.

In the **CLI**, the compiler runs explicitly: `refine validate` runs steps 2 through 5 and reports the verdict without applying. `refine plan` runs steps 2 through 6 and shows what would happen, including gate results. `refine apply` runs all eight steps and lands the refinement.

In **continuous integration**, `refine validate` runs on every pull request. A failing validation blocks the merge. This is how the gates that path-policy declares get enforced before code lands, not after.

In the **MCP server**, the compiler runs in response to agent proposals: an agent proposes a refinement, the compiler validates it, the agent receives the verdict. The agent can iterate (refine its proposal based on the verdict) or escalate (request human review when the verdict indicates the agent can't resolve the issue alone).

In an **in-editor companion** (VS Code, Cursor, JetBrains), the compiler runs in the background, evaluating the changes an external agent is proposing in real time. The companion intercepts the agent's edits, packages them as a refinement, validates against the policies, and either lets the edits through or flags them for human attention.

In every surface, the compiler is the same compiler. The verdict is the same shape. The gates are the same gates. This is the meaning of "one engine, five surfaces" — the surfaces are different ways of authoring and observing refinements; the compiler is one.

## §9 — One compiler, two entry points

The cascade-aware compiler does not care where a refinement came from. It accepts work through two entry points, and treats them identically.

The first entry point is the **RFN submission**: the programmer (or AI agent) writes a `.rfn` file that declares a target, a delta, an authority, and a justification. The compiler reads the spec, computes the cascade, runs the gates, writes the audit chain entry. This is the canonical path — refinement as a formally proposed change, reviewed before it lands.

The second entry point is the **direct code edit**. The programmer, working inside the IDE's code editor, hand-edits a knob value, adjusts a constant, refines a function body. The cascade-aware compiler treats this edit *the same way* it treats an RFN submission. The edit is automatically wrapped: the compiler infers the target (the changed line and its containing region), computes the cascade fan-out, evaluates the gates, writes the audit chain entry. If the change crosses an authority threshold — a knob whose audit field requires risk_committee approval, for instance — the edit is held as a pending proposal rather than landing immediately. The programmer is shown the same cascade visualization, the same gate verdict, the same authority requirement that an RFN submission would have surfaced.

This is what makes Refine an authentic IDE rather than a refinement workbench bolted onto an editor. A programmer who lightly edits a function inside Refine is not "doing something outside the system" — the edit *is* a refinement, automatically. The two-tool problem dissolves: there is no inside-Refine vs. outside-Refine. There is only the cascade-aware compiler, with two surfaces for proposing work to it. The audit chain spans both.

The implications matter. A programmer who would otherwise have written `0.16` over `0.18` in a regular editor — and left no trace of *why* — now leaves a trace automatically. The compiler computes the cascade; the audit chain records the edit, the author, the time. If the edit needed risk-committee approval, the gate held the change as pending. If it did not, the edit landed with full provenance attached. Either way, the trail is durable. No edit escapes governance because none has the chance to.

This is also what lets AI-first daily work be authentically governed. When a coding agent proposes a change, the change enters through the same compiler regardless of whether it arrived as an RFN file or as a direct edit. The agent does not have to choose between "formal proposal" and "casual edit" — the choice does not exist. Every change is a refinement; the only variable is how heavyweight the surrounding metadata is.

## §10 — A word about performance

The compiler does more work per change than a traditional compiler does. It maintains a graph; it computes cascades; it runs gates. In a naïve implementation, this work could be slow enough to interrupt the flow of programming.

In practice, the work is bounded and parallelizable, and the implementations I've seen are fast enough to feel synchronous. Cascade computation, as noted, runs in milliseconds for typical refinements. Gate execution depends on the gates: a test suite that takes thirty seconds takes thirty seconds, but that thirty seconds was already required by any reasonable workflow. The compiler doesn't add it; the compiler just makes its execution part of the refinement's verdict.

The graph itself is maintained incrementally: when source code changes, only the affected portion of the graph is recomputed. The full graph extraction is needed once, at project import; thereafter, the compiler updates the graph in lockstep with edits.

This is, again, an engineering challenge, not a conceptual one. The work has to be done well, but it can be done well. Refine's implementation has been validated on a codebase of approximately 80,000 lines of Zin and Python, which is small by industrial standards but large enough that performance considerations are real. The graph maintenance and cascade computation have not become bottlenecks in any workflow I have observed.

## §11 — What this chapter has established — and what it has not

The compiler that revalidates is the engine of refinement-oriented programming. It is the piece that does the cognitive work that, in the old paradigm, the human reviewer did and is now drowning in.

What the chapter has established:

- The compiler runs in eight steps, six of which are mechanical and two of which involve human or external interaction.
- The compiler is deterministic in a generalized sense: same refinement, same graph state, same verdict.
- The compiler computes cascades by walking the graph along edges, applying kind-specific propagation rules.
- The compiler enforces gates: reviews, tests, policies, budgets, provenance, signatures.
- The compiler produces structured verdicts that enter the audit chain.
- The compiler accepts work through two entry points — the formal RFN submission and the direct code edit — and treats them identically; no edit escapes governance because none has the chance to.

What it has not established:

- The compiler does not verify correctness, intent, design quality, or trust — it is not a theorem prover. Those judgments remain human, with proof composable as a gate input for the rare constraint that earns it.
- Taste can be declared as advisory context but never becomes a gate — and much of what teams call taste is undeclared context that belongs in the gate as a requirement.
- Determinism is conditional at the edges: on reviewer decisions, and on the determinism of the external systems a gate invokes.

The next chapter is about what the programmer sees when the compiler's work becomes a working surface — about the cascade as the primary view, and what changes when the cascade replaces the diff as the artifact a reviewer reads.

---

# Chapter 5 — The cascade as a working surface

*What you read instead of the diff: the computed blast radius of a change, made a surface you can navigate.*

Chapter 4 described what the compiler computes. This chapter is about what the programmer sees.

I want to draw a distinction that took me longer to articulate than it should have. The cascade is a *computed artifact* — the compiler produces it, the audit chain records it. But what makes refinement-oriented programming *operational*, in the sense that a working programmer can adopt it as their daily practice, is the move from cascade-as-computation to cascade-as-surface. The cascade has to be something the programmer *looks at* and *navigates* and *reasons against*, not just something the compiler emits into a log file.

This chapter is about that move. About what it means for the cascade to become a first-class facet of the IDE, parallel in stature to Code or Graph, dedicated to a single question: *what does this refinement do, and what did it already do?*

## §1 — The diff was always derivative

Let me start by pushing back on something I have been treating as obvious but that deserves explicit treatment.

The diff is, and has always been, a *derived view*. It is a textual representation of *the bytes that changed* between two snapshots of a codebase. It tells you nothing about the *semantic* change underneath; it just tells you which lines moved. For most of programming's history, that has been enough, because the human reader looking at the diff *also held the codebase in their head*, and could infer the semantic change from the textual change.

When the codebase was small, the inference was cheap. When the codebase was large but the developer was experienced, the inference was still feasible. When the developer was new to the codebase, or the change touched parts of the system they didn't know well, the inference became harder. At every scale, though, the inference was the *human's* work, performed silently, mediated by experience.

What AI-assisted development broke is not the diff itself. It broke the human's capacity to do the inference at the pace diffs now arrive. A 200-line diff produced by an agent in 20 seconds is not less readable than a 200-line diff produced by a human over four hours; it is identical *as bytes*. What changed is the time the reviewer has to read it, and the cognitive load that comes from reviewing many such diffs in quick succession.

For five decades, we built our review apparatus around the diff because the diff was the *most precise representation we could afford*. The compiler couldn't tell us what a change *meant*, only what it *was*. The reviewer had to fill the gap.

The cascade-aware compiler closes the gap. It computes, deterministically, which other parts of the system the change *means* — which functions revalidate, which tests must rerun, which policies trigger, which schemas affect downstream consumers. The cascade *is* the semantic change, in machine-readable form. The diff is the textual trace of it; the cascade is the meaning.

There is a name for what the compiler does when it produces the cascade, and it is worth saying, because it grounds the word *computed* in something far older than this paradigm. Propagating a change through a graph of dependencies to find exactly what it affects is the central operation of **incremental computation** — the discipline behind self-adjusting computation, behind incremental view maintenance in databases, behind the demand-driven engines that sit under modern compilers and keep an editor's analysis fresh as you type. The cascade is not a bespoke trick I invented; it is that operation, pointed at a graph of *governance* rather than a graph of values. An ordinary incremental engine recomputes a value to keep it current; the cascade recomputes what must be *re-governed* — but the propagation machinery is the same, and forty years of other people's work stands behind it. Naming it does more than lend respectability. It hands the cascade a cure for the one complaint I made against it in Chapter 4. A poorly-anchored codebase produces *conservative* cascades — over-wide, because the compiler cannot prove in advance that a change fails to reach somewhere. The incremental-computation literature solved exactly this, and the solution has a name: **early cutoff**. When a node is revalidated and its verdict comes out *unchanged*, propagation stops there — the change did not really reach past it. You cannot prove non-impact in advance, but you can prove it after the fact, by noticing that the verdict did not move. The cascade I admitted was sometimes too wide gets narrower as the machinery underneath it grows up.

> **Figure 5.1 — The cascade propagates, then stops.** A single penalty-cap change forces its dependents to revalidate, then ripples outward — until a revalidated node's verdict comes back unchanged, where propagation stops. Early cutoff, visible on the surface.

Once the compiler can produce the cascade, the diff stops being the most precise artifact we can afford. It becomes a *secondary* artifact — useful for some purposes (a programmer who wants to see the exact bytes still wants the diff), but no longer the primary surface for reasoning about change.

The Cascade facet is what makes that shift operational. It gives the cascade a working surface, with the same kind of attention and craft that previous paradigms gave to the diff viewer.

## §2 — What the facet shows

Open the Cascade facet for any refinement — proposed, validated, or applied — and the IDE shows you three views, in sequence.

**Visualize** is the cascade as a picture. The refinement's target node sits at the center, in purple, surrounded by the dashed outer ring that has become Refine's visual signature for *focal point of a cascade*. From the target, edges fan outward to the affected nodes. First-degree cascade — direct impact — renders in solid green. Second-degree cascade — transitive impact — fades, with thinner edges and lower opacity. Tests appear as squares, distinct from circles. Policy nodes wear the orange that signals attention. Faded perimeter dots remind the viewer that the codebase graph extends *beyond* the cascade — what the refinement does not touch is as informative as what it does.

This is the picture a reviewer reads in fifteen seconds before they have read a single line of diff. It is, in my experience, the single most useful piece of information the IDE provides. A reviewer who sees a compact, well-bounded cascade can approve a refinement on the strength of the picture alone — the cascade tells them the change is local, isolated, well-tested. A reviewer who sees a sprawling cascade with deep transitive reach knows, before reading the code, that this change deserves more scrutiny.

**Analyze** is the cascade as a dataset. Five tabs — Nodes, Gates, Policies, Tests, History — each presenting a different slice of the impact picture, fully tabular, sortable, filterable. The reviewer who wants to know *which cascade nodes have the worst test coverage* sorts the Nodes tab by coverage ascending. The compliance officer who wants to see *every policy this refinement touched* opens the Policies tab. The auditor reconstructing what happened three months ago opens the History tab and walks the timeline.

The visualization is for visual cognition; the table is for the questions data structures answer. Both are necessary, because different decisions need different evidence.

**Compare** is the cascade against another cascade. Two refinements side by side, their cascades rendered as compact maps, their differences enumerated in a table below: nodes unique to A, nodes unique to B, nodes in both. Use this when two competing proposals address the same intent — which has the smaller blast radius? Use it when a pipeline contains constituent refinements — how do their cascades overlap? Use it when investigating after the fact — what did this refinement touch that the previous similar refinement did not?

These three views are not arbitrary. They map onto the three irreducible questions a reviewer asks: *what is the shape of this change?* (Visualize), *what are the precise dimensions of it?* (Analyze), *how does it compare to alternatives?* (Compare). I have not yet found a question about a cascade that does not reduce to one of these three.

To make it concrete: when Amina's `tighten_penalty_cap` arrives in the compliance queue at Sonibank, the Visualize view shows `policy/penalty_cap` at the center with three nodes in its ring — the risk-assessment function, the loan-pricing function, and the BCEAO compliance rule in its attention-orange. Fifteen seconds of reading says: local, bounded, policy-adjacent. One click into the Gates tab confirms the lending tests passed, forty-seven of forty-seven, and the policy matched — cap 16 against ceiling 18. The reviewer approves without reading a line of the diff, and every second of that judgment is in the chain.

> **Figure 5.2 — The judgment surface.** The Cascade facet's three views — Visualize, Analyze, Compare — with the target at the center, first-degree impact in green, tests as squares, policies in orange, and the faded perimeter reminding the reviewer what the change does *not* touch.

## §3 — Two temporal modes

A property of the Cascade facet that I want to draw explicit attention to: it serves *two different questions* with the same machinery.

**Prospective** mode is the pre-flight read. A refinement has been proposed but has not yet been applied. The reviewer is judging whether to let it land. The cascade shows what the refinement *will* touch if applied; the gates show what *must* pass; the history tab shows what's been touched recently in the same area, so the reviewer can spot brewing conflicts.

This is the mode the reviewer lives in when working through the gated queue. The toolbar's mode flag, in italic grey, says *prospective — not yet applied*. The status pill is amber. The gates show some passed and some pending. The reviewer's question is forward-looking: *should this land?*

**Retrospective** mode is the forensic read. A refinement landed three months ago; something now needs to be understood. Perhaps an auditor is examining the codebase; perhaps a debugger is tracing a defect; perhaps a programmer is asking *why is this constant 16 instead of 18 and who decided that?* The cascade is now historical — frozen at the time of landing. The gates show what *did* pass; the history tab walks the timeline from proposal through application.

The toolbar's mode flag reads *retrospective — 2026-05-30*. The status pill is green. The question is backward-looking: *what did this refinement do, who decided it, and what followed?*

The same facet serves both questions, because the underlying machinery is the same: cascade as object, gates as records, policies as references, history as timeline. What changes is the reader's intent and what they are looking *for*. The facet does not need to distinguish; the reader does.

This is the property that makes the audit chain operationally useful. Without the retrospective mode, the audit chain would be a log file — searchable, but not navigable. With it, the audit chain becomes the *working surface the reviewer reads when the past matters*, with the same affordances as the surface they read for the future.

## §4 — Why this changes the workflow

When the cascade is the primary surface, the daily workflow of a refinement-oriented programmer shifts in ways that took me several months at Sonibank to fully internalize.

The most visible shift: **proposals are evaluated against the cascade, not the diff**. When a refinement appears in my review queue, my first action is not to read the code. It is to open the Cascade facet and read the picture. If the cascade is compact, well-bounded, well-covered by tests, and matches policies I trust — I can approve in seconds, without reading the code at all. The compiler has already verified that the change is structurally sound; my job is to judge whether the *intent* (which I read from the refinement's `reason` field) and the *impact* (which I read from the cascade) are appropriate. The code itself becomes a third-tier artifact, consulted only when the cascade or the intent raises a question.

The second shift: **the cascade reframes coordination**. When two refinements have overlapping cascades, the reviewer sees the overlap before either lands. The Compare view makes this explicit; the standalone Visualize view makes it implicit through the cascade nodes' "last modified" column. A team that adopts the cascade as their primary surface has, in effect, a real-time map of where work is concentrated and where collisions are likely. The map is more honest than any sprint board or kanban view, because it derives from the actual codebase rather than the team's intentions.

The third shift: **retrospective work becomes systematic**. When a defect surfaces, the first action is to open the Cascade facet for the suspect refinement and walk the history. The audit chain is no longer a forensic exercise requiring database queries and git archaeology; it is a working surface, the same one the reviewer used at landing time, with the same affordances. The auditor and the reviewer use the same tool, asking different questions of the same data.

These three shifts are why the Cascade facet matters more than its visible footprint might suggest. It is not just a new view onto data the compiler already produces. It is a *reorganization of what the programmer's attention rests on*, with consequences for how the team works together, how reviews happen, how the audit chain functions.

## §5 — What the facet is not

I want to be explicit about what the Cascade facet does not claim to be, because the temptation to overstate is strong.

It is not the only place to look at a refinement. The RFN editor remains the authoring surface; the Code facet remains the source-of-truth view; the Graph facet remains the structural overview. The Cascade facet is the *judgment surface*, dedicated to the specific question of impact.

It does not compute the cascade. That is the compiler's job, documented in Chapter 4. The facet renders what the compiler produces. If the compiler computes a stale or incorrect cascade, the facet faithfully shows the staleness or the incorrectness; the facet does not improve the data.

It does not approve or reject refinements. The reviewer's judgment is exercised via the gate-discharge actions in the RFN facet (approving a `review_by` gate, for example). The Cascade facet *informs* the judgment; it does not *make* it. A reviewer who skims the cascade and then approves a problematic refinement has used the tool poorly; the tool does not protect against this.

It does not yet reconstruct historical graph state in full. The retrospective mode in v1.0 reads from the refinement's recorded cascade — the cascade *as it was computed at the time of landing*. If the graph has since evolved, the recorded cascade may differ from what the current cascade would be for the same refinement. Full time-machine reconstruction — replaying the graph state at landing time and recomputing the cascade against that state — is a phase 2 deliverable. The facet acknowledges this limitation in its documentation.

It is not a substitute for reading the code. Some changes are structurally simple but semantically subtle — a one-line change with a clear cascade that nonetheless implements the wrong logic. The Cascade facet helps with most reviews but does not eliminate the cases where the reviewer must consult the source. Knowing when to drop from cascade-level review to source-level review is part of the discipline a refinement-oriented programmer develops.

These honest boundaries are not weaknesses to be hidden. They are the proper scope of the facet. A facet that claimed to solve all of them would be overpromising; a facet that solved fewer would be underutilizing its actual capability.

## §6 — Why this took until now

A reasonable question, given that the cascade-aware compiler has been part of refinement-oriented programming from the beginning: why was the Cascade facet not part of v1.0 of Refine?

The honest answer is that I did not see it clearly until I had been using the IDE for several months. The cascade was always there — surfaced in the verdict pane next to the RFN editor, mentioned in the audit chain entries, computed by the compiler on every validation. But it was a *readout*, not a working surface. A list of node names in a small panel, easy to scroll past.

What I observed, over months of using my own tool, was that I kept wanting to *spend time* with the cascade. To zoom in. To filter. To compare two cascades. To trace what happened after a refinement landed. The verdict pane gave me a single number and a small list; what I wanted was a workspace. The other facets in the IDE — Code, Graph, Factory — each had their own workspace. The cascade did not. The asymmetry was strange and, eventually, untenable.

The Cascade facet is what happens when an under-served artifact gets the dedicated treatment it deserved all along. It is not a new computation; the compiler was already doing the work. It is a new *attention*, organized into a facet, with the structure and affordances and visual vocabulary that the cascade should have had from the beginning.

I think this is, in some ways, the most distinctive thing Refine offers in 2026: the move from cascade-as-computation to cascade-as-surface. Previous paradigms had their own central abstractions — the object in OOP, the function in FP — and each made the abstraction visible to the programmer in its preferred form. Refinement-oriented programming has the cascade as its central abstraction; the Cascade facet is what makes the abstraction visible. Without it, the paradigm was incomplete — not as a theory, but as a practice.

Future versions of the facet will deepen it: hover-highlight on nodes, click-to-drill into subcascades, force-directed layouts, full time-machine reconstruction. Phase 1 ships the surface; subsequent phases enrich it. The shape is set.

## §7 — What this chapter has established — and what it has not

The cascade is not a property of the compiler. It is, in refinement-oriented programming, the *primary working surface* — what the reviewer reads instead of the diff, what the auditor traces in the audit chain, what the programmer navigates to understand impact.

It is worth noting, two years on, that the market is arriving at this from the other side. A whole category of AI code-review tools now reads a pull request, and the best of them do something that would have sounded exotic when I started: they index the repository into a graph and pull a change's call-sites, its tests, its history into the review. They have, in effect, rediscovered the cascade. But they use it to *comment* — to hand a human better-informed remarks on a diff they will still merge by hand — where refinement-oriented programming uses it to *decide*: the same graph, read by a deterministic gate that can refuse. Same graph, review versus govern. It is the cleanest illustration I know of the difference between describing a change and governing it. And it generalizes past review. The tools clustering nearest this work all *verify* — they review the diff, they evaluate the output, they guardrail the runtime, they certify the model's compliance — and not one of them decides on the change. They establish how trustworthy a change *looks*. The cascade, read by the gate, is where it becomes answerable for itself — which is the difference between a change that is well-described and a change that is governed.

- The diff was always a derived view; the cascade is the semantic change in machine-readable form.
- The Cascade facet renders the cascade as a working surface with three views: Visualize, Analyze, Compare.
- The same facet serves prospective (pre-flight) and retrospective (forensic) reads.
- Adopting the cascade as primary reshapes review, coordination, and post-hoc analysis.

What it has not established:

- The facet renders, it does not compute; it informs judgment, it does not make it. A reviewer who skims the cascade and approves has used the tool poorly, and the tool does not protect against that.
- Retrospective mode in v1.0 reads the cascade as recorded at landing; full time-machine reconstruction of historical graph state is future work.
- The cascade does not replace reading the code in the structurally-simple-but-semantically-subtle cases; knowing when to drop to source is part of the discipline.

The next chapter is about who has the authority to land what — the social and structural layer that surrounds the compiler and the cascade, and gives the audit chain its meaning.

---

# Chapter 6 — Authorities, attribution, audit

*Who may change what — and how the record of who-decided-what survives three years, for an auditor who asks.*

A compiler that produces deterministic verdicts is a tool. A *system of authority* that decides who can ask for those verdicts, who can approve them, and how the resulting attestation is preserved over time — that is a paradigm.

This chapter is about the social and structural layer that surrounds the cascade-aware compiler: who proposes refinements, who reviews them, by what authority, against what policy, and how the chain of decisions accumulates into a usable audit history. Without this layer, the compiler is a clever mechanism that does not address the actual problem the agentic era introduced. With it, refinement-oriented programming has the property the senior engineer at Sonibank was missing: the ability to answer *who decided this, on what authority, against what policy*, three years after the fact.

## §1 — The four questions audit asks

A working audit chain answers four questions about every consequential change:

*Who proposed it?* The identity of the author — a human, a named agent, or a pipeline that proposed it on the basis of triggering conditions.

*By what authority?* The role or capability under which the author was acting. A senior engineer proposing a refactor; an agent proposing a knob change within delegated bounds; a compliance pipeline proposing a quarterly policy update.

*Against what policy?* The set of constraints the change was checked against — the regulatory rules, the internal policies, the architectural invariants. Not "did it pass our tests" but "did it satisfy our explicit, codified rules."

*With what verification?* The gates that ran — the tests that passed, the reviews that occurred, the policies that matched. Each gate's outcome recorded, each gate's identity recorded.

If the system can answer these four questions for any change, three years after the change landed, the audit chain is intact. If it cannot, the audit chain is broken — sometimes silently, sometimes catastrophically.

The existing toolchain answers question one (`git blame`) and partially answers question four (CI logs, sometimes). It does not, in any structured way, answer questions two and three. That is the gap refinement-oriented programming closes.

## §2 — Identity, for humans and for agents

The authority layer begins with identity. Every actor in the system — human or agent — has a credentialed identity that is bound to its actions.

For humans, identity is familiar: an account, a name, an email, a role within the organization. Modern auth systems (SSO, MFA, federated identity) make this tractable. The new requirement that refinement-oriented programming adds is that the identity must be linked to a *role* with specific *scope*: not just "this person is in the organization" but "this person is authorized to review compliance refinements" or "this person is authorized to approve schema migrations."

For agents, the equivalent is less well-established but no less necessary. An agent has:

- An *identity*: a stable identifier that names the agent (e.g., `sonnet-4.5@anthropic`, or `internal-refiner-v2@sonibank`).
- A *credential*: an issued, expirable token that authenticates the agent's actions. Credentials expire (six months is a reasonable default) and can be revoked immediately if the agent is compromised or retired.
- A *scope*: an explicit set of grants — which paths the agent may operate on, which actions it may propose, which states it may attain, which task kinds it is authorized for, what sensitivity ceiling applies to its work.
- A *delegation chain*: when an agent is acting on behalf of a human, the chain records the human-to-agent grant and the scope at which it was made.

This is not bureaucratic overhead. It is the minimum machinery required to answer *who proposed this* when the proposer is an agent. Without it, the proposal is anonymous in any meaningful sense; the audit chain breaks at the agent.

In Refine's implementation, the identity facet maintains this information as a first-class facet, queryable, auditable, and enforceable by the compiler at every gate. An agent without an identity record cannot propose refinements; an agent with an expired credential is blocked at the provenance gate; an agent whose scope does not cover the refinement it is proposing is rejected before the compiler even computes the cascade.

This level of rigor about agent identity is not yet industry-standard, but it will need to become standard. The alternative — agents that propose work anonymously, with no provenance trail — is incompatible with any regulated context and ultimately incompatible with any production context.

## §3 — Scope and the principle of least privilege

A central design choice in refinement-oriented programming is that *scope is explicit, narrow, and enforced*. Agents (and, to a lesser extent, humans) are granted specific capabilities, and the compiler enforces those capabilities at every step.

An agent with a scope grant of *"propose refinements to schema/loan_record/** , state authoring, task kind data-modeling, sensitivity moderate"* can propose a `add_field` refinement on `schema/loan_record/credit_score`. The same agent cannot propose a refinement on `policy/penalty_cap` (out-of-scope path), cannot propose a refinement requiring judgment state (out-of-scope state), cannot propose a refinement involving classified data (out-of-scope sensitivity).

Scope is enforced at proposal time, not at execution time. The agent cannot even draft a refinement outside its scope; the proposal is rejected before validation. This is the agentic-era equivalent of operating-system-level capability control: the agent does not need to be *trusted not to misbehave*; the system does not *permit* the misbehavior in the first place.

This matters for several reasons.

It matters because **agents are not yet trustworthy in the sense humans can be trustworthy.** Even capable agents can be confused by adversarial inputs, can hallucinate intentions, can drift outside their actual competence. Scope restricts the blast radius of those failures.

It matters because **delegated authority is the only way agents can scale.** A team that lets an agent propose any change anywhere has effectively granted the agent the privileges of a senior engineer. A team that scopes the agent narrowly can let it operate at high throughput within its scope, with confidence that the worst-case mistakes are bounded.

It matters because **compliance frameworks expect it.** Most regulatory regimes that govern software systems include some form of least-privilege requirement for non-human actors. The framework was written with service accounts and integration users in mind, but it applies cleanly to AI agents. Scope grants are the implementation that satisfies the requirement.

There is a name for the discipline all of this belongs to, and saying it locates refinement-oriented programming in a tradition rather than leaving it to look like a pile of local inventions. The discipline is **Zero Trust** — the security posture that replaced the old castle-and-moat with a flat premise: trust nothing, verify everything, assume the breach has already happened. Its canonical statement is NIST's; its sharpest agent-specific statement, as I write, is Anthropic's own framework for securing AI agents. And here is the thing I did not see until I read that literature with this book's argument in mind: refinement-oriented programming is the *same control pattern aimed at a different object*. Zero Trust governs **access** — what an actor may reach and do at runtime. Refinement-oriented programming governs **change** — whether an alteration to the software may land. The loop is identical in shape. Zero Trust runs *actor → policy engine → enforcement point → log*; the gate runs *authority → compiler → commit-or-refuse → audit chain*. And the four tenets transfer one for one, from access to change: *never trust implicitly* becomes *every authority faces the gate, no change waved through because of who proposed it*; *verify continuously* becomes *the compiler revalidates the cascade on every commit*; *grant least privilege* becomes the explicit, narrow, proposal-time scope this section is about; *assume breach* becomes *bound the blast radius, because an agent will at some point be confused or compromised*. So the cleanest one-line statement of where this paradigm sits in the security world is: **refinement-oriented programming extends Zero Trust from access to change.** It does not replace the runtime enforcement — the service meshes, the short-lived credentials, the identity-aware proxies are still doing their job at the moment of access. It is the missing half of the same discipline, applied at the moment a change is *made* rather than the moment a resource is *reached*. Two halves of one idea, and until recently only one of them had been built.

> **Figure 6.1 — The same loop, two objects.** Zero Trust runs *actor → policy engine → enforcement point → log*; the gate runs *authority → compiler → commit-or-refuse → audit chain*. One control pattern, aimed once at access and once at change.

## §4 — Roles, not individuals

For human actors, refinement-oriented programming organizes authority around *roles* rather than individuals. A refinement's `review_by` gate names a role — `compliance_officer`, `senior_engineer`, `chief_risk_officer` — not a specific person. The role is filled by one or more identified individuals; any one of them may discharge the gate; if the role is unfilled, the gate cannot pass.

This design choice has practical consequences:

- *Bus factor*: when an individual goes on vacation, leaves the company, or is reassigned, refinements requiring their role can still proceed if the role has other holders.
- *Scaling*: as the team grows, new individuals can be added to a role without modifying every refinement's gate configuration.
- *Audit clarity*: the audit chain records both the role and the specific individual who discharged the gate. The role tells the auditor *what authority was exercised*; the individual tells them *who exercised it*.
- *Policy enforcement*: organizational policies often specify roles ("changes to credit policy must be reviewed by compliance"). The role-based gate enforces the policy directly; there is no way to misroute a review.

This is more rigorous than the typical pull-request approval workflow, in which reviewers are usually picked ad-hoc. The role-based discipline forces the team to *codify who reviews what* once, in the project's configuration, and then enforces that codification automatically.

## §5 — Policies as first-class artifacts

A *policy*, in refinement-oriented programming, is a codified constraint that refinements must satisfy. Policies are first-class artifacts: they have identity, they are versioned, they are queryable, they can be the subject of refinements themselves.

The Sonibank codebase, as a working example, has policies like:

- *BCEAO-4.2*: the West African central bank's interest-rate policy. Constrains `policy/penalty_cap` and `policy/loan_floor`. Updated annually.
- *Internal-RC-2025*: the bank's internal risk-committee policy. Constrains a broader set of pricing and risk parameters. Updated quarterly.
- *Architecture-API-Contracts*: an internal architectural rule requiring that all API contracts be backward-compatible across minor versions. Constrains every `schema` refinement.

Each policy has:

- A unique identifier (BCEAO-4.2, etc.).
- A scope (which nodes it constrains).
- A set of *constraints* — machine-checkable conditions that refinements must satisfy.
- An owner (the role or organization responsible for the policy).
- A version history.

When a refinement declares `policy: BCEAO-4.2` in its fields, the compiler checks the refinement's target against BCEAO-4.2's constraints. If the constraints are satisfied, the policy match gate passes. If not, the gate fails.

Policies can also be declared at the path level. The project configuration can say *"every refinement on `schema/**` must match policy/Architecture-API-Contracts"* — and from that point forward, the compiler enforces the policy on every applicable refinement, with no further per-refinement opt-in required.

The first-class nature of policies enables a powerful audit pattern: when a policy itself is updated, the compiler can re-check every refinement that previously matched against the policy. If the new policy is stricter and some past refinements no longer satisfy it, the system flags them for re-examination. The audit chain doesn't just record what passed at the time; it can be re-evaluated against current standards, with the same rigor.

## §6 — The audit chain

The audit chain is the structural product of refinement-oriented programming. It is not a separate system; it is the cumulative record of every refinement that has ever landed in the codebase, with its complete metadata, in a queryable form.

Each entry in the chain includes:

- The refinement itself (target, kind, from/to, gates, reason, author).
- The compiler's verdict (cascade, gate results, applied state, commit hash).
- Timestamps for proposal, validation, gate execution, application.
- References to predecessor refinements (the chain of changes affecting the same target).
- References to successor refinements (what changed about this target after).
- The signature of the human or agent identity that authored.

The chain is *immutable* in the sense that entries are never deleted. Revisions to a refinement (when a re-proposal happens after a failed validation) are recorded as new entries, with explicit pointers to the original. Reverts are recorded as their own refinements, with explicit *inverse-of* references.

This immutability is what makes the chain trustworthy. An auditor or a regulator looking at the chain three years after the fact can be confident that what they see is what happened — not a reconstructed narrative, not a sanitized version, not a snapshot at the moment of audit. The chain is the historical truth, in the same sense that a Git history is the historical truth about commits.

Where the chain differs from a Git history is in its *structure*. Git history is a sequence of commits with free-form messages; the messages may or may not carry the information an auditor needs. The audit chain is a sequence of refinements with structured fields; every entry carries the information an auditor needs, by construction. The chain doesn't depend on commit-message discipline; it depends on the refinement schema, which is enforced by the compiler.

> **Figure 6.2 — The audit chain.** Every entry carries the refinement, the verdict, the timestamps, and the signature — plus the pointers, to predecessors, successors, and inverses, that let an auditor walk from any change to everything around it, years later.

## §7 — Reversibility

A property of the audit chain that deserves its own mention: *every refinement has a pre-computed inverse.*

When the compiler applies a refinement, it does not just compute the forward change. It also computes the *inverse*: the refinement that would undo this one, returning the system to its prior state. The inverse is stored as part of the refinement's record.

This means that reverting a refinement is itself an operation: a new refinement, with an explicit `inverse-of` reference to the original. The reverting refinement goes through the same lifecycle as any other — it is validated, its cascade is computed, its gates run, its verdict is recorded. The revert is a first-class operation, fully audited.

The pre-computation matters because it means reverts don't require the system to *reconstruct* what to undo. The original refinement's record already contains the undo. If, three years later, a refinement turns out to have introduced a subtle bug, the revert is mechanical: load the inverse, run it through the compiler, observe the verdict, apply.

Some refinements are not cleanly invertible (a delete, for instance, where the deleted content has been heavily modified by subsequent refinements). The compiler flags such cases: the inverse is *attempted* but may require human resolution. This is honest; there are limits to mechanical reversibility, and the system makes those limits visible rather than hiding them.

## §8 — Provenance

A related concept worth distinguishing: *provenance*.

Where authority asks *who is allowed to do this*, and authorship asks *who did this*, provenance asks *what is the chain of decisions and trust that led to this artifact existing*?

Provenance is broader than attribution. A refinement proposed by an agent has authorship: the agent's identity. Its provenance is richer: the agent was delegated by a human; the human was assigned a role; the role was created by a team policy; the team policy was approved by the organization. The provenance trail can be unrolled when needed — when a regulator wants to understand not just who did the work but the entire chain of authorization that produced it.

In Refine's implementation, provenance is its own facet. It tracks not just authorship but the full delegation chain, the trust level of each link, the credentials that were active at each step. A regulator examining the audit chain can ask *show me the provenance chain for this refinement* and receive a complete unrolling: the agent, the human who delegated to it, the team that authorized the human, the policy under which the team operates.

This is the deepest layer of attestation. Most systems don't need it most of the time. Regulated systems need it sometimes. The systems that need it tend to need it badly when they need it. Building it from the start, rather than retrofitting it after a regulatory examination, is the disciplined choice.

## §9 — What the audit chain enables

When the chain is intact and queryable, several things become possible that were not possible before:

**Forensic audit at change time.** When a problem is suspected, the chain is searched. *"Show me all refinements that touched `schema/loan_record` in the last six months, grouped by author and gate result."* The query is mechanical; the answer is complete.

**Compliance review without team interruption.** A compliance team can answer most of its own questions from the chain alone, without scheduling meetings with engineering. *"Was the BCEAO-4.2 policy update applied to all relevant refinements? Show me the refinements that matched against it before the update, and confirm they have been re-checked."* This is a chain query, not a human inquiry.

**Cross-team accountability.** When the security team needs to know what changes touched authentication code in the last quarter, the chain answers. When the platform team needs to know which agents have been operating in their domain, the chain answers. The chain is the shared infrastructure for cross-team coordination.

**Regulatory examination.** When a regulator examines the codebase, the examination is *of the chain*, not of the team's memory. The chain shows the auditor what happened, who decided it, against what policy, with what verification. The team explains anomalies; it does not have to reconstruct everything from scratch.

**Long-term maintainability.** When a programmer joins the team three years after a system was built, the chain is the team's collective memory of why things are the way they are. Reading the chain teaches the codebase's history; understanding the chain is understanding the codebase.

This is the value of refinement-oriented programming for environments where memory matters: where work outlives any individual's tenure, where regulatory examination is not optional, where systems need to be defensible decades after they were built.

There is a larger frame around all of this, and it arrived from a direction I did not expect — not from the tooling world but from the boardroom. As I write, enterprise AI regulation has converged, across the EU AI Act, the NIST AI Risk Management Framework, ISO/IEC 42001, and the OECD principles, on a single demand, and board-advisory writing on the subject states it more bluntly than I would have dared: *regulation is no longer assessing what an organisation intends to do; it is assessing what it can prove.* Policies are no longer sufficient. A framework on a shelf is no longer sufficient. What a regulator now wants is evidence that a control is *operating* — producible on demand, with accountability demonstrated rather than assumed, under governance that can absorb the next regulatory change rather than ossifying around the last one. Read that list again and it is, almost word for word, the list of things the audit chain produces as a by-product of how the work is done: the gate is the control operating, on every change; the chain is the evidence, accumulated rather than reconstructed; the authority model is accountability made specific; and because a rule is a refinable node, a regulatory change is itself a governed refinement whose cascade re-checks everything it touches. The market spent the last few years discovering, in the language of compliance, the property this book has been arguing for in the language of engineering.

I want to claim exactly the right amount from that convergence and not a syllable more. Refine is not a complete answer to AI governance, and a board that bought it expecting one would be misled. It governs the *change* — how the software, the policy, and the data an AI system rests on actually evolve, and who changed what — which, in an era when agents author most of that change, is a large and growing share of the problem but not the whole of it. The behaviour of the running model — whether it is drifting, whether it is biased, whether it is accurate in production — is a different object, governed by monitoring that Refine composes with rather than replaces. And providing the controls and the evidence a regime asks for is not the same as being compliant; that is a judgement a regulator and a lawyer make on top of the mechanism, and the mechanism cannot make it for them. What I will claim is the part the chain genuinely delivers: Refine is the change-governance pillar of an enterprise's AI-governance operating model, and on that pillar the answer to *can you prove it?* is yes — by construction, not by scramble.

One more extension belongs in this chapter before it closes: the move that brings business intent itself into the refinement system.

## §10 — Requirements as first-class refinable artifacts

The chapter to this point has described the audit chain as it operates over code-level artifacts. Refinements land in `.rfn` files; cascades fan out through the codebase graph; the chain records who proposed, what changed, what was checked, what was approved. The trail is durable and defensible.

But the trail begins, in that account, with the code. The *why* of the change — the business decision, the regulatory letter, the risk-committee minute that motivated the refinement in the first place — has remained outside the system. It has lived in meeting notes, in Word documents, in the heads of compliance officers, in tickets pointing at archived emails. The audit chain was complete from the code outward; it was incomplete from the intent inward.

For most engineering contexts, that gap is uncomfortable but tolerable. The codebase is the system; the business decisions are interpreted by engineers who are accountable for translating intent into implementation. The trail from intent to code is informal, but it exists in human memory and in the proximity of the people who hold it.

For regulated-enterprise contexts, the gap is a serious problem. A regulator who asks "why did you reduce the penalty cap to sixteen percent on the first of July?" needs an answer that begins with the risk-committee decision and ends with the specific code that implemented it. If the trail to the code is durable but the trail from the decision to the code is informal, the audit chain ends too late and the regulator's question goes partly unanswered. The compliance officer reconstructs the trail manually each time. The audit chain provides forensic evidence about the code but cannot, on its own, attest to the alignment between code and intent.

The development that addresses this is the elevation of **requirements** to first-class refinable artifacts within the same governance system as code. The move is small in conceptual terms — extend the kinds-of-thing the system refines from code-level artifacts to also include business-intent artifacts — but its consequences for the audit chain are substantial. The Requirements facet, which the prototype demonstrates in its first phase, is where this move lands in the product.

A formalized requirement carries the same kinds of metadata a code refinement does: an identifier, a title, an author, an authority structure naming the roles that must approve it, a status that moves through `draft → in-review → approved → active → retired`, and a creation timestamp. Beyond that, it carries fields specific to its kind: a prose statement preserved verbatim (the business author's own words), acceptance criteria expressed in given-when-then form or as worked scenarios, constraints expressed as predicates over named scopes, references to upstream policies (regulatory and internal), and a list of downstream code refinements that implement it.

What the audit chain gains is the link upstream. A code refinement now carries a `requirement REQ_NNN` field that names the requirement it implements. The cascade-aware compiler can require that field be present for refinements that touch sensitive paths. The audit chain, when traced backwards from a landed commit, now reaches not just to the refinement that landed it but to the requirement that motivated it, to the policy references underneath that requirement, to the authority structure that approved it. The chain is unbroken from regulator letter to landed code.

What the audit chain also gains is the linkage *forward* from intent. A requirement, viewed in the Trace sublevel of the Requirements facet, displays the code refinements that have implemented it. When a requirement is itself refined — when the risk committee decides to tighten the cap further from sixteen percent to fourteen percent — the cascade computation can identify which code refinements depend on the prior version and need re-validation. The same machinery that handles code-to-code cascades now extends to requirement-to-code cascades, with the same deterministic guarantees.

Two cautions are worth stating clearly.

The first concerns the role of AI in this surface. The Requirements facet supports AI-assisted formalization: the business author writes prose, the AI proposes a structured form, the author reviews and edits. This is *narrower* than the long-running ambition of business-rules engines, which promised that non-developers could author production logic directly. The Requirements facet does not promise this. It promises that business authors can capture *intent and the constraints code must satisfy*, in a form the system can govern. The execution remains in code, where execution semantics are precise; the intent remains in business, where intent semantics live; the linkage between them is governable. The AI extracts structure from prose; it does not author rules the business has not yet decided. When the prose carries ambiguity the AI cannot resolve, the AI says so. The requirement stays in prose form, or returns to the author for clarification, until the underlying decision is actually made.

The second concerns the discipline of authorship. Business intent is genuinely hard to formalize, and the history of structured-rule authoring tools is largely the history of systems that imposed a discipline on authors who were not prepared for it. The Requirements facet hedges against this risk by preserving the prose alongside the structured form. The business author can always read what they actually said, in their own words. The structured form is a derived artifact; the prose is the canonical statement. If the structure is wrong, the prose tells you so. Over time, as authors gain fluency, the structured form will become more authoritative; but the prose remains, for honesty and for traceability.

This is what the audit chain enables when it reaches upstream of code. The trail from the risk-committee minute to the landed commit becomes a single artifact, navigable in either direction, durable across personnel changes, defensible to regulators, and queryable by the same machinery that handles every other refinement in the system. The chain stops being a forensic exercise that requires reconstruction each time the regulator asks. It becomes the working representation of how the organization decides what to build.

## §11 — What this chapter has established — and what it has not

What the chapter has established:

- The audit chain answers four questions — who proposed, by what authority, against what policy, with what verification — for every consequential change, years after the fact.
- Identity is credentialed for humans and agents alike; scope is explicit, narrow, and enforced at proposal time.
- Gates name roles, not individuals; policies are first-class, versioned, and re-checkable when they change.
- Every refinement carries a pre-computed inverse; a revert is a first-class, fully audited refinement.
- The chain now reaches upstream of code: requirements are first-class refinable artifacts, so the trail runs from the regulator's letter to the landed commit.
- This is the same control pattern as Zero Trust, aimed at change instead of access — the four tenets transfer one for one.

What it has not established:

- Legal compliance. Providing the controls and the evidence a regime requires is not the auditor's determination; the mechanism cannot make that call for them.
- The whole of AI governance. The running model's behaviour in production is a different object, governed by monitoring this paradigm composes with rather than replaces.
- Clean reversibility in every case. Some inverses require human resolution, and the system flags those rather than hiding them.

Now, the methodology — how a team actually moves from the old workflow into this one.

---

# Part II — The working discipline

*Chapters 7–12 · The practice.* A paradigm is a practice before it is a product. This part is the working day: the methodology a team actually follows, the five surfaces one engine wears, the moment the world's evidence caught up with the argument, and the three artifacts that scale a person — parallel sessions, loops instead of prompts, and the vocabulary of governed skills an agent calls by name.

---

# Chapter 7 — A methodology, not just a tool

*Why this is a discipline, not a product: the working practice the paradigm asks of a team.*

It would be easy to read the preceding chapters and conclude that refinement-oriented programming is, fundamentally, a piece of technology. New compiler; new file format; new IDE; new audit chain. Install the technology and you have the paradigm.

This is wrong, and the wrongness is the most common reason early adopters of major paradigm shifts fail.

A paradigm is not a tool. A paradigm is a coordinated set of practices, organized around a unit of work and a set of values, that a group of people enact together. Object-oriented programming is not Smalltalk; functional programming is not Haskell; refinement-oriented programming is not Refine. The tools embody the paradigm and make it tractable, but the paradigm is the practice, and the practice is what a team has to learn.

This chapter is about the methodology — the practice of refinement-oriented programming for a team that wants to adopt it. It covers four phases: onboarding, assessment, steady operation, and change management. Each phase has specific deliverables, specific decision points, and specific failure modes. The whole arc, if executed well, takes a team from the existing workflow to a stable refinement-oriented practice over the course of a year. Teams that try to do it faster usually skip a phase; teams that try to do it cleverly usually skip the discipline.

## §1 — Onboarding: the first week

The first week is mechanical. Point the system at your codebase; configure your AI providers; train your reviewers on five examples. That is the entire program for week one.

**Day 1 — Import.** The compiler scans the existing codebase and extracts the initial graph. The graph will be incomplete; many parts of a typical codebase don't yet have the structure the compiler can fully understand. The output is a *coverage report*: how much of the codebase has been anchored, where the boundaries are, what's recognizable and what's raw. The team reviews the coverage; nothing else is done with it yet.

**Day 2 — Configuration.** The team declares its AI providers: which models, with which credentials, with which budgets. It declares its routing policy: cost-optimized, quality-first, local-first, or mixed. It declares its safety policies: what agents may not do (which paths, which states, which sensitivity ceilings). The configuration is one file; it can change over time; today's version is the starting position, not the final answer.

**Day 3 — Roles.** The team identifies its roles. `compliance_officer`, `senior_engineer`, `chief_risk_officer`, `tech_lead` — whatever the organization actually uses. Each role is bound to one or more identified individuals. The role-based gates start working immediately.

**Day 4 — Five guided refinements.** The team selects five small, low-stakes refinements from the recent backlog (or recent commits) and re-proposes them through the system. Each refinement goes through the full lifecycle: proposal, validation, gate execution, application. The team observes the verdicts, reads the cascades, sees what the chain records. The five examples become the team's shared mental model.

**Day 5 — Reviewers' first session.** The team's reviewers — whoever does code review today — sit through a half-day session focused not on the tool but on the *cognitive shift*: *what do you read when you review a refinement, instead of a diff?* The answer is the refinement itself (what's the intent, what's the policy, what's the reason) and the verdict (what's the cascade, what gates passed, what's the audit trail). The diff is a secondary artifact; the reviewer doesn't ignore it, but the reviewer's primary attention is on the refinement.

That is week one. Nothing has been re-architected; nothing has been rewritten; the team is producing about the same amount of work as before. What has changed is that the team now has a working installation, a starting set of refinements, and a baseline of reviewer competence.

The most common failure in week one is *trying to do too much*. Teams will sometimes want to anchor their entire codebase immediately, or run dozens of refinements through the system in the first three days, or rewrite their CI configuration to use Refine for everything at once. Don't. Week one is for getting the foundation in place. The foundation has to be solid before anything is built on it.

Week one at Sonibank looked exactly this ordinary. The import produced a coverage report that flagged most of the lending module as anchorable and the older reporting scripts as raw; the configuration declared the providers and a conservative routing policy; Aïcha was bound to `compliance_officer` on day three. The five guided refinements were deliberately small — the penalty-cap change among them, re-proposed from the previous quarter's commit history — and by Friday the reviewers had seen five verdicts, five cascades, five chain entries. Nobody's velocity changed that week. What changed is that the next BCEAO question had an answer waiting.

## §2 — Assessment: the second week

The assessment phase is the most distinctive part of refinement-oriented programming adoption. It is also the most underappreciated and the most useful.

In the second week, the compiler produces an *assessment report* — a structured analysis of the codebase as it currently exists, viewed through the refinement-oriented lens. The report covers:

- **Refinement point density**: how many places in the codebase could plausibly become refinement targets. High density means the codebase is structured in a way amenable to refinement-oriented work; low density means substantial parts of the codebase will need restructuring before they can be governed.

- **Cascade depth**: typical lengths of cascades for typical refinements. Shallow cascades (1–3 nodes) mean changes are localized; deep cascades (10+ nodes) mean the codebase has significant coupling. Neither is bad in itself, but knowing the distribution informs how reviewers should prepare.

- **Governance gaps**: places where changes are made today that *would* require gates under refinement-oriented programming but currently are not gated. These are usually compliance gaps: changes to policy values that should be reviewed by compliance but aren't, changes to schemas that should match architectural rules but don't.

- **Hotspots**: parts of the codebase that change often and have high cascade. These are the places where refinement-oriented programming will provide the most value first.

- **Test coverage at refinement points**: how many of the candidate refinement points are protected by tests that the compiler can use as gates.

- **Policies discovered**: codified rules already present in the codebase that can be promoted to first-class policies. Sometimes a codebase has well-organized policy logic that needs only to be lifted into the policy facet; sometimes the policies are scattered and need significant work to extract.

The report is not, on first generation, complimentary. Most real codebases have significant gaps. The assessment is honest about them. The team reads the report and decides what to do with it.

This is the moment — and I have seen it happen on every adoption I have facilitated — when the team has a kind of clarity it has not had before. The team knew, vaguely, that the codebase had issues. The team did not know, precisely, what the issues were, where they were concentrated, or how they ranked against each other. The assessment names them.

*"This is the moment of honesty most teams have never had."* The phrase appears in the website's adoption page; I wrote it because I have seen the moment over and over. It is not flattering, but it is liberating: once the situation is named, it can be addressed.

The output of the assessment phase is a *staged adoption plan*: which parts of the codebase to anchor first, which policies to codify first, which gaps to close first, what the ordering should be. The plan is risk-ranked: high-impact, high-feasibility work first; low-impact or high-cost work later.

The most common failure in the assessment phase is *defensiveness*. Teams sometimes read their first assessment and react as if it were criticism of their work. It is not; it is a snapshot of where the codebase is, which is mostly a product of years of accumulated decisions under different constraints. The assessment is more useful when the team treats it as a tool for planning, not as a verdict on past choices.

## §3 — Steady operation: months one through twelve

The bulk of the methodology is in steady operation. The first two weeks are setup; the next year is the practice.

Steady operation has a daily cadence, a weekly cadence, and a monthly cadence.

**Daily cadence.** Programmers propose refinements through the IDE, the CLI, or RFN files. Agents propose refinements through the MCP server or the in-editor companion. The compiler validates each one. Gates run. Refinements either land or are gated; gated ones wait for their reviewers. Reviewers work through the gated queue once or twice a day. The Factory facet — the IDE's operational dashboard — shows the team's throughput in refinements per day, gate-passage rates, agent-vs-human authorship splits, cost per landed refinement.

The day is, in some ways, indistinguishable from the day before refinement-oriented programming was adopted. Programmers code; reviewers review; agents propose; tests run. What's different is the *unit*: everything is happening in refinements rather than commits.

**Weekly cadence.** Once a week, the team has a *factory review*: a short meeting that looks at the previous week's throughput, gate-failure patterns, agent performance, and any anomalies in the audit chain. The conversation is structured around the data the Factory facet provides; it is not a status meeting or a planning meeting, it is a *systems health meeting*. What's working? What's gated for the wrong reason? What's slipping?

The weekly cadence catches drift. Without it, teams sometimes settle into bad patterns — agents proposing refinements that consistently fail one specific gate, for example, or reviewers approving without reading — and the patterns calcify. The weekly review keeps the practice honest.

**Monthly cadence.** Once a month, the team does a *policy review*: a longer session focused on whether the codified policies are still serving their purpose. New policies are added; old ones are retired; existing ones are refined. The session also reviews the assessment from the previous month: has refinement-point density improved? Have cascade depths come down (suggesting better decoupling)? Are the hotspots still the hotspots, or have they shifted?

The monthly cadence is where the methodology *learns*. The system is not static; it is continually being tuned by the team based on what the chain is teaching them about how their work actually proceeds.

**Quarterly cadence.** Once a quarter — at the same time as most teams' planning cycles — there is a *strategic refinement review*. The audit chain is examined for the previous quarter: what got built, who built it, how often the compiler caught issues, what trends are emerging. This review is often where teams identify systemic improvements: a new policy that would have prevented a class of issues, a new role that should be created to handle reviews that are bottlenecking, a new agent that should be onboarded for a task currently consuming too much human time.

The cadence works because it is multi-scale. Daily attention catches immediate issues; weekly attention catches drift; monthly attention catches structural inefficiencies; quarterly attention catches strategic gaps. Most teams that adopt refinement-oriented programming find that some of these cadences map onto things they already do (the daily and weekly are usually familiar) while others (the monthly policy review, the quarterly strategic refinement review) are new and require deliberate cultivation.

## §4 — The measurable signals

What does success look like in steady operation? Several signals are worth tracking, none of which are line count:

**Cost per landed refinement.** When agents are part of the workflow, this is the dollar figure (token costs plus human review time, valued at hourly rates) per refinement that successfully lands. The figure is volatile early on and stabilizes as the team finds its routing patterns. Stable cost per refinement is a sign the system is healthy; rising cost is usually a sign that something needs attention (a tool change, an agent change, a process gap).

**Revert rate.** What fraction of refinements that land are subsequently reverted? Some reverts are healthy (the team is willing to undo); high revert rates indicate that refinements are landing without sufficient validation. The revert rate by author (human vs. agent) is worth tracking separately.

**Time to land.** How long does it take, on average, from refinement proposal to landed state? This is the equivalent of the old "PR cycle time" metric. Faster is better, within limits — too-fast time-to-land usually indicates inadequate gating.

**Gate-failure distribution.** Which gates fail most often? Test failures are different from policy failures, which are different from review rejections. The distribution is diagnostic: high test-failure rates mean tests are too brittle or agents are too aggressive; high policy-failure rates mean policies are too strict or agents don't understand them; high review-rejection rates mean reviewers and authors are misaligned about what should pass.

**Agent throughput vs. human review bandwidth.** A central balance in refinement-oriented programming is matching agent output to human review capacity. If agents are producing twenty refinements a day and reviewers can process ten, the gated queue grows. The Factory facet surfaces this imbalance; the team responds by either slowing the agents (with stricter scope, lower budgets) or expanding review capacity (more reviewers, better reviewer tools).

**Audit chain coverage.** What fraction of recent changes are governed by the chain (proposed as refinements, validated, gated) versus made directly (raw code edits)? This is a coverage metric for the paradigm itself. Early in adoption, coverage may be 20%; by the end of the first year, mature teams reach 60-80%; some parts of the codebase remain raw indefinitely, by choice.

What you don't measure: lines of code per day; commits per programmer; story points closed per sprint. These metrics, in an agentic-era context, are either meaningless or actively misleading. A team can produce ten thousand lines of code in a week, all of it bad, with no governance, and the line-count metric will look great. The signals above show whether the work is *trustworthy*, which is the actual question.

## §5 — Change management: the second year

A team in its second year of refinement-oriented programming is doing something different from a team in its first year. The first year is about adopting the paradigm; the second year is about *managing change within it*.

Things change. The codebase grows. Team members join and leave. AI providers improve, change pricing, deprecate models. Regulations are updated. Internal policies are revised. Business priorities shift. Each of these changes ripples through a system that, under refinement-oriented programming, has explicit representations of all of them.

The methodology accommodates this through several mechanisms:

**Policy updates propagate.** When a policy is updated, the compiler can re-check every refinement that previously matched against the policy. Refinements that no longer satisfy the new policy are flagged for review. The team doesn't have to remember to check; the compiler reminds them.

**Team changes update the role registry.** When a person leaves a role, the Factory facet shows pending refinements waiting on that role; the team can reassign or accept the gap until a replacement is named. There is no silent failure.

**Provider changes adapt routing.** When an AI provider deprecates a model or changes pricing, the routing policies the team set up at onboarding are revisited. The evaluation facet shows per-provider quality and cost trends, informing the choice of replacements.

**Codebase growth re-anchors.** As new code is added to the codebase, the team decides what to anchor and what to leave raw. The boundary moves. Periodic re-assessment — once a quarter is typical — flags new areas of growth that should be considered for anchoring.

**Refinement lifecycle includes reversibility.** Every refinement carries its inverse. When a change turns out to be wrong (a policy was too strict, a refactor was premature), the revert is itself a refinement, fully audited. The system absorbs the reversal without breaking the chain.

Change management is, in a sense, the *test* of whether a team has actually adopted refinement-oriented programming or is just running the tool. A team that has adopted the paradigm absorbs change as a continuous activity; a team that has not adopted it experiences each change as a crisis. The difference shows up in the second year more than the first.

## §6 — Cultural prerequisites and contraindications

Not every team is a good fit for refinement-oriented programming. Honesty about this matters.

**Good fit:**

- Teams in regulated industries (banking, healthcare, infrastructure, defense, government) where audit trails are operationally required.
- Teams with substantial AI-assisted development where attestation has become a problem.
- Teams managing long-lived codebases where institutional memory matters across years.
- Teams that already have a culture of code review and explicit policy.
- Teams whose engineering leadership is willing to invest a year in adopting a new practice.

**Poor fit:**

- Teams in fast-prototyping environments where code is intentionally throwaway.
- Teams with no codified policies and no appetite to write them (the paradigm requires this).
- Teams where review is already a rubber stamp and there is no organizational will to change that.
- Teams that want a productivity improvement without changing how they work (refinement-oriented programming is not a productivity tool; it is a paradigm).

**Contraindications:**

- A team that has just adopted a major new framework or technology and is still stabilizing.
- A team under acute deadline pressure where adding a new practice creates risk rather than reducing it.
- A team that does not have at least one senior engineer who has read this book, internalized the position, and is willing to advocate for it internally.

I will not claim refinement-oriented programming is for everyone. It is for teams that have a specific problem — the breakdown of attestation under AI-assisted development — and who have the organizational capacity to address it through a paradigm shift rather than an incremental fix. That is not every team. It is enough teams.

## §7 — The system must be programmable by its users

A methodology that depends on a vendor for every variation is not a methodology. It is a service contract dressed as a paradigm. Refinement-oriented programming, to be real, must be extensible by the practitioners who adopt it — without requiring them to modify the engine, fork the compiler, or wait for a release cycle.

This is why the refinement environment exposes a **scripting layer** operating on a **Refinement Object Model**. The scripting layer is not an afterthought or an admin convenience. It is the methodological commitment that says: *the refinement world is yours to query, extend, report on, and constrain in ways we did not anticipate*.

Three categories of work belong to the scripting layer:

**Query work.** Auditors ask non-canonical questions. *Show me every refinement targeting a BCEAO-cited policy in Q3 where the cascade crossed module boundaries and any gate held longer than four hours.* The engine cannot ship a UI button for every such query. The scripting layer lets the auditor express the question as code and get a precise, reproducible answer.

**Policy work.** Each organization has organization-specific approval rules that do not generalize. One bank requires dual review when a refinement touches policy and the cascade reach exceeds five nodes; another bank has different thresholds, different roles, different escalation paths. The scripting layer lets each organization declare its own gates, which the cascade-aware compiler then invokes alongside the built-in ones.

**Workflow work.** Reactive automation that connects the refinement lifecycle to external systems: notifying compliance officers when specific policies are touched, opening tickets when refinements land, producing scheduled reports, integrating with calendars and approval systems. The scripting layer subscribes to refinement lifecycle events and runs scripted hooks without modifying the core engine.

The pairing of a production language (which is compiled, governed, and slow-changing) with an extension language (which is dynamic, accessible, and fast-changing) is a pattern that has proven robust across many software ecosystems: 3D engines pair C++ with Lua, web browsers pair compiled engines with JavaScript, operating systems pair compiled binaries with shell scripts. The refinement environment does the same: **Zin** (compiled, refinement-aware, the production surface) paired with **Ring** (embedded, accessible, the extension surface), sharing the **ROM** as their common object model.

This is what makes refinement-oriented programming a methodology that *lives in the user's hands* rather than a paradigm administered from the vendor's servers. The system is not finished when the engine ships. It is finished when the user has written their first script.

## §8 — What this chapter has established — and what it has not

The methodology is the practice that surrounds the technology. Without it, the technology is interesting but inert; with it, the technology becomes the basis for a different kind of engineering culture.

- The methodology has four phases: onboarding (week 1), assessment (week 2), steady operation (months 1-12), change management (ongoing).
- Each phase has specific deliverables, cadences, and failure modes.
- Success is measured in attestation quality, not productivity: cost per landed refinement, revert rate, time to land, gate-failure distribution, audit chain coverage.
- The cadence is multi-scale: daily attention to throughput, weekly to drift, monthly to structure, quarterly to strategy.
- Cultural prerequisites matter; refinement-oriented programming is not for every team.
- The system must be programmable by its users: the scripting layer over the Refinement Object Model is a methodological commitment, not an administrative convenience.

What it has not established:

- That the cadences and figures are laws. They are practice-shaped defaults; teams tune them, and the tuning is part of the method.
- That the methodology fits every team. The poor fits and contraindications of §6 are real, and naming them is part of the method too.
- That the methodology generalizes beyond its evidence. Its base is one regulated pilot context and the adoptions it informed; other organizational shapes remain a hypothesis.

The next chapter is about the surfaces — the five different ways a team interacts with the refinement engine. The methodology lives inside these surfaces; the surfaces are how the methodology becomes visible work, day to day.

---

# Chapter 8 — Five surfaces, one engine

*The shape of the tool: how one governed engine shows up as several working surfaces, not five separate apps.*

A paradigm needs more than one surface.

Object-oriented programming worked because OOP wasn't just Smalltalk's IDE; it was also C++'s headers, Java's classes, Python's `__init__`, the whiteboard diagrams architects drew, the books programmers read, the conversations programmers had. The paradigm spread because it could be expressed in multiple media, each suited to a different context. A paradigm with only one surface — one way of doing things, available only one place — is a hothouse flower. It survives only in the conditions that produced it.

Refinement-oriented programming has, in the implementation I have built, five surfaces. Each is a different *way of interacting* with the same underlying engine. Each suits a different audience, a different context, a different stage of adoption. Together they cover the working day of a software team in 2026, and they let the paradigm meet programmers where they are rather than demanding programmers move to where the paradigm lives.

This chapter walks through the five. The point is not the specific implementations — other implementations of refinement-oriented programming will have different surfaces — but the *principle*: a paradigm needs to be embodied in multiple forms, each honoring the constraints of its context, all sharing one underlying engine.

## §1 — The principle of multiple surfaces

Before walking through the five, let me state the principle they collectively embody.

A surface is *a way of interacting with the underlying paradigm.* It is not a tool, not an interface, not a frontend; it is the whole stack of conventions, formats, and gestures by which a programmer engages with the paradigm in a particular context.

Multiple surfaces are necessary because different contexts have different needs. A programmer at her desk, working in flow, needs different things from a programmer running CI in a build pipeline. A team adopting the paradigm for the first time needs different things from a team in its third year. A human contributing in person needs different things from an agent contributing programmatically. A reviewer in a code-review tool needs different things from an auditor reading the chain three years later.

A single surface — a single IDE, say, that everyone must use — would force all these contexts through one funnel. That funnel would either be over-fit to one context (and inadequate for the others) or so generic that it serves none of them well. Multiple surfaces avoid the funnel by allowing each context its own native expression while ensuring all of them share the same underlying engine.

The principle has a consequence: *every surface is round-trippable with every other.* A refinement authored in the IDE can be exported as RFN; an RFN file can be opened in the IDE; an MCP server can read and write the same artifacts. The engine is the source of truth; the surfaces are different windows onto it. A team can adopt one surface today and add others as their practice matures.

One refinement at Sonibank makes the principle tangible. Amina authors `tighten_penalty_cap` as a form in the IDE; the engine writes the canonical `.rfn` file; CI re-validates that same file on the pull request with `refine validate`; a compliance agent queries the same refinement's verdict over MCP before proposing a follow-up; and three years later the auditor reads the same entry in the chain viewer. Four surfaces touched one artifact, and nobody translated anything.

The five surfaces in the current implementation are: the IDE, the CLI, the MCP server, the in-editor companion, and RFN. I will treat each in turn.

## §2 — The IDE

The IDE is the surface most readers will picture first when they hear "programming environment." It is a graph-aware workspace, organized by facet rather than by file, with twenty-eight facets covering every aspect of refinement-oriented work: foundations, intent, build, AI, operate, support.

The IDE is the surface where the paradigm is most fully expressed. Every concept in this book — the graph, the cascade, the refinement, the gate, the verdict, the audit chain — has a dedicated view. A programmer working in the IDE can see the graph of their codebase visually, navigate it by clicking nodes, propose refinements directly in a panel, watch the cascade compute as they edit, observe gate executions in real time, browse the audit chain in a structured viewer.

The IDE is the right surface for:

- Teams adopting refinement-oriented programming end-to-end.
- Programmers whose primary work is governing and orchestrating, not just writing code.
- Compliance reviewers and audit specialists who need to see the system as a whole.
- Junior engineers learning the paradigm.

It is the wrong surface for:

- Programmers who live in Vim or Emacs and consider GUIs a degradation.
- Headless contexts (CI, scripts, automation).
- Existing teams who don't want to abandon their current editor.
- Teams adopting incrementally who want to keep their current workflow mostly intact.

A common mistake teams make in early adoption is assuming the IDE is the *only* way to use refinement-oriented programming. It is not. It is the most complete way, but completeness is not always what a team needs. A team that adopts only the CLI and RFN files — never opening the IDE — can still practice the paradigm fully. The IDE is a useful surface; it is not the paradigm.

## §3 — The CLI

The CLI is the surface for headless and scripted contexts. It exposes the same engine the IDE uses, accessed through a small set of verbs: `refine validate`, `refine plan`, `refine apply`, `refine revert`, `refine show`, `refine export`.

The CLI is what continuous integration runs. Every pull request, every push to a branch, every nightly build can invoke `refine validate` to check that no refinements are broken. The CLI is what scheduled jobs use to run quarterly assessments. The CLI is what an engineer types when they want to apply a refinement quickly without opening any GUI.

The CLI is the right surface for:

- CI pipelines and automation.
- Engineers who prefer terminal workflows.
- Teams with existing tooling that integrates by shell command.
- Audit scripts and compliance verification.

It is the wrong surface for:

- Discovering the system for the first time. The CLI is not a teaching tool; it is for users who already know what they want.
- Visual analysis of the graph. The CLI can output structured data; it cannot show you the cascade as a diagram.
- Interactive refinement authoring. Editing complex refinements directly through CLI flags is painful; RFN files are better.

The CLI's role is to be the *atom* of automation. Every IDE action, every MCP server method, every in-editor companion feature ultimately invokes the same engine the CLI exposes. The CLI is the universal foothold for integrating refinement-oriented programming with whatever else a team uses.

## §4 — The MCP server

The MCP server is the surface for AI agents. It exposes the engine as a Model Context Protocol service that external agentic stacks — Claude Code, Cursor, custom agent platforms — can call to validate proposals, request cascades, check gates, and submit refinements.

This is the surface that makes refinement-oriented programming compatible with the agent stacks teams are already using. A team that has invested in Claude Code or Cursor or built their own agentic platform does not need to abandon it. They configure their agents to call the MCP server before any code change is finalized; the server validates the proposed change as a refinement; the verdict comes back; the agent either proceeds (if the verdict is favorable) or escalates (if it is not).

This is also the surface that lets teams *add governance to existing agent workflows without changing the agent stack*. The agents continue to do what they were doing; the MCP server intercepts their proposals and applies refinement-oriented validation. Over time, as the team adopts more of the paradigm, the agents can be configured to use richer refinement features — proposing structured refinements directly, querying the graph, observing the cascade — but the entry point is low.

The MCP server is the right surface for:

- Teams with existing agent platforms.
- Multi-agent systems where governance must be enforced uniformly across agents.
- Custom agent platforms that need a governance layer but don't want to build one.
- Federation: multiple teams using different agent stacks coordinating through a shared refinement-oriented governance.

It is the wrong surface for:

- Human-only teams. The MCP server's value is in the agent integration; for purely human workflows, the IDE and CLI are better.
- Teams without a clear understanding of what their agents are doing. The MCP server can enforce governance, but it requires the team to know what governance to enforce.

## §5 — The in-editor companion

The in-editor companion is a surface that lives inside the editors programmers already use: VS Code, Cursor, JetBrains. It is the most *cohabit* of the five surfaces — it does not ask the programmer to leave their editor; it adds a governance layer on top.

When the programmer (or an AI agent operating in the editor) proposes a change, the companion intercepts the proposal, packages it as a refinement, validates it against the policies, surfaces the cascade in a side panel, and either lets the change through or flags it for human attention. The companion is, in effect, the IDE's governance facets ported into the programmer's existing environment.

The in-editor companion is the right surface for:

- Teams already deeply invested in a particular editor.
- Teams with agentic workflows running in those editors (Cursor's agent mode, Claude Code in JetBrains, etc.).
- Teams that want to add governance without disrupting daily work.
- Individual contributors evaluating refinement-oriented programming before the team commits.

It is the wrong surface for:

- Teams that need the full IDE experience. The companion is intentionally less complete than the IDE; it gives you the governance layer, not the full operational dashboard.
- Reviewers and auditors. The companion is for authoring; reviewers and auditors need the dedicated tools that the IDE and the audit chain viewer provide.

The companion is, in many ways, the *gateway drug* for refinement-oriented programming. A team can adopt the companion as a low-risk pilot — install it in the editors they already use, configure a few basic policies, see what happens. Over time, the companion's value accumulates as more refinements are made under its governance. By the time the team is ready to move to the IDE for fuller capability, they have a substantial body of refinements already in their audit chain.

## §6 — RFN — the Refinement Notation Language

RFN — the Refinement Notation Language — is the surface for text-first programmers. It is the textual frontend to the engine: a declarative language for expressing refinements in `.rfn` files, version-controlled in Git alongside the source code, edited in any editor the programmer prefers.

RFN exists because of an observation I made earlier in the book: there is a population of programmers whose productivity is grounded in text, in their editor of choice, in version-controlled artifacts, in scriptable workflows. Vim users. Emacs users. Programmers who have spent twenty years optimizing their personal toolchains and consider any GUI a degradation. For them, a graph-based IDE is a step backward, no matter how powerful the underlying paradigm.

RFN inverts the equation for that audience. The model is unchanged from the IDE; the compiler is unchanged; the audit chain is unchanged. The surface is plain text files in Git, editable anywhere. The compiler invokes are the same as the CLI's. The validation and gate semantics are identical. The same refinements that an IDE user authors visually, an RFN user authors textually, and the same audit chain records both.

The design principles that produced RFN are worth stating explicitly, because they apply to any textual-DSL design effort.

**Declarative, not imperative.** An RFN file describes *what should be true* after the refinement lands, not the steps to get there. The compiler infers the operational details. SQL over cursor loops; Terraform over shell scripts; Dhall over Bash. The declarative form is more concise, more analyzable, and less prone to operational mistakes.

**Composable.** A refinement is the atomic unit; pipelines, templates, parameters, and imports let larger work compose from smaller refinements. A multi-step compliance migration is itself a refinement that contains refinements. Composition is the path to expressiveness without language sprawl.

**Listing 8.1 — Composition: a quarterly compliance pass as a pipeline of refinements.**

```rfn
pipeline q2_compliance_pass {
  description  "Three policy updates required by Q2 BCEAO directive"
  author       compliance@sonibank
  reason       "Quarterly compliance refresh · directive 2026-Q2"

  refinement tighten_penalty_cap
  refinement update_audit_threshold
  refinement migrate_loan_schema

  gates {
    review_by    compliance_officer
    review_by    chief_risk_officer
    must_pass    tests/lending/*
    must_pass    tests/compliance/*
    on_fail      revert_all
  }

  on_success {
    deploy to staging
    notify  compliance-team@sonibank
  }
}
```

Three refinements, two reviewers, shared gates, one decision to land or revert all — and a reader who has never seen RFN can follow it, which is the readability principle doing its work.

**Readable by non-programmers.** A compliance officer reading a `.rfn` file should grasp eighty percent of what is happening without learning the language. Syntax favors structured English over symbol-heavy notation. The language is not Lisp; it is more like an English-prose schema, with keywords like `refinement`, `target`, `policy`, `author`, `reason`, `gates`. A reader who has never seen RFN can parse most of it on first encounter.

**Identical semantics to the IDE.** Every refinement expressible in RFN is one that can be produced by clicking in the IDE, and vice versa. No DSL-only features, no IDE-only features. Two surfaces, one model. This is the property that lets a team mix surfaces freely.

**Round-trippable.** A `.rfn` file is the canonical source. The IDE reads it, edits it, writes it back. The file in Git is the source of truth; the IDE is one editor among many. This is what makes RFN the *primary* surface for teams that adopt it, not an alternate one.

RFN is the right surface for:

- Text-first programmers and their teams.
- Code review at scale: pull requests in GitHub, GitLab, Gerrit are simpler with `.rfn` files than with binary IDE state.
- CI/CD integration: `refine validate` on `.rfn` files is the standard pattern.
- Sharing refinements across projects: an `.rfn` file is a portable artifact that can be checked into a refinement library.

It is the wrong surface for:

- Exploratory work where you want to *see* the graph as you reason. RFN is text; visual reasoning happens in the IDE.
- Operational dashboards. The Factory facet, the audit chain viewer, the evaluation summary — these are screens, not text files.

A team that adopts only RFN — never the IDE, never the in-editor companion — is practicing refinement-oriented programming fully. They are missing some of the visualization and observability features the IDE provides, but the paradigm is complete in their hands. This is the proof that the IDE is not the paradigm; the engine is. The surfaces are doorways into the engine, and each doorway lets in a different population.

## §7 — Choosing surfaces

Most teams that adopt refinement-oriented programming end up using more than one surface, but they don't usually adopt them all at once. A common adoption path:

**Phase 1 (months 1-3):** The in-editor companion, possibly combined with the CLI. The companion adds governance to existing workflows without disrupting them; the CLI is added for CI integration. The audit chain begins to populate.

**Phase 2 (months 3-6):** RFN is introduced, often initially for compliance refinements that benefit from text-first review. A handful of RFN files are checked into the repo, validated in CI, applied by hand when changes are needed.

**Phase 3 (months 6-9):** The IDE is brought online for facets that benefit most from visualization: the graph, the Factory dashboard, the audit chain viewer. Some programmers adopt the IDE as their primary editor; others stay in their previous editor with the companion.

**Phase 4 (months 9-12):** The MCP server is configured for agentic workflows, if the team has them. By this point, the team understands their policies well enough to express them as governance the MCP server can enforce.

This is not the only adoption path. A team in heavy regulatory pressure might adopt the IDE first for compliance work and only later add the companion for daily engineering. A team running predominantly agentic workflows might prioritize the MCP server and use RFN files as the audit-readable artifact. The path depends on the team; the surfaces are designed to accommodate many paths.

What matters is that the team understands the surfaces are *interoperable by design*. A refinement authored in any surface is visible in every other; the audit chain is global; the engine is one. Adoption is therefore additive rather than substitutive: adding a new surface enriches the workflow without disrupting what came before.

## §8 — What this chapter has established — and what it has not

The principle of multiple surfaces is what makes refinement-oriented programming adoptable across diverse teams and contexts. A paradigm with only one surface dies in conditions outside its hothouse; a paradigm with multiple surfaces spreads across the conditions where its underlying ideas have value.

- Refinement-oriented programming, in the implementation I have built, has five surfaces: the IDE, the CLI, the MCP server, the in-editor companion, and RFN.
- Each surface has a context in which it is the right choice and a context in which it is wrong.
- All five share one engine and one audit chain; a refinement authored in any is visible in all.
- Adoption is typically incremental, surface by surface, not all at once.
- The plurality of surfaces is the property that makes the paradigm portable across teams that would otherwise be incompatible.

What it has not established:

- That these five surfaces are the paradigm's. They are this implementation's; other implementations will cut the surfaces differently, and the principle — multiple doorways, one engine — is the claim, not the list.
- That the adoption path is prescriptive. It is a common shape, not a requirement.
- That RFN reads well to non-programmers. That is a design goal the pilot must still evidence.

The next chapter pauses the argument to look outward: at the account that arrived, from inside the largest AI lab's own engineering practice, confirming that the bottleneck this book opened with has moved exactly as Chapter 1 said it would — and at what that confirmation does and does not establish.

---

# Chapter 9 — The bottleneck moves

*What changes when writing code is cheap: the constraint shifts from producing code to trusting it.*

The previous eight chapters made an argument. The unit of change had shifted; the codebase deserved to be modelled as a graph; the compiler needed to revalidate after every refinement; the cascade was the right working surface for judgment; authority, attribution, and audit could no longer be afterthoughts; refinement-oriented programming was a methodology rather than a tool; the user had to be able to program the system extensibly; and the five surfaces of a refinement environment composed coherently around a single engine. Each chapter was an argument from first principles. None of them, individually, was an empirical claim.

This chapter is the empirical claim.

## §1 — The argument and its evidence

The argument across Chapters 1–8 amounts to a prediction: that the bottleneck in serious software development would move from *writing code* to *reviewing and directing the writing of code by agents*. The prediction was not novel — careful readers of the trajectory of foundation models could see it coming — but the choice to build infrastructure around the prediction *now*, before the bottleneck became universally obvious, was a decision Refine made early. Sonibank Niger's BCEAO compliance obligations made the bottleneck visible to us before it was visible to most others; the regulatory rhythm forced review-and-governance to be primary rather than bolt-on; and the design choices documented in the previous chapters all flowed from that forcing.

In June 2026, The Anthropic Institute published an article titled *When AI builds itself*. The article reports findings from inside Anthropic about the present state of AI-assisted software development. The findings are striking enough that they deserve to be quoted directly from the article (with attribution and within fair-use constraints): code authorship has flipped, with more than 80 percent of merged code at Anthropic now written by Claude rather than by humans; engineer output measured in lines of merged code per day has risen roughly eightfold over the past eighteen months; code quality from AI authors has reached parity with human authors and is projected to exceed it within the year. Direction-setting is described as the locus of remaining human comparative advantage. Anthropic states plainly that human review has *already* become the new bottleneck in their internal development process, and they describe building automated review infrastructure — an automated reviewer running on every code change before merge — to address that bottleneck. A retrospective analysis indicates the automated reviewer would have caught roughly one-third of past production incidents before they reached customers.

The article is grounded in internal Anthropic data, not external benchmarks. It is, to our knowledge, the strongest public statement yet from a frontier AI lab about the bottleneck shift the previous chapters of this manifesto predicted on theoretical grounds.

## §2 — What this confirms

Five of the manifesto's claims receive direct empirical support from the Anthropic article.

**The unit of change shifted (Chapter 2).** Anthropic reports 80 percent of merged code being AI-authored. The article notes the broader industry context: GitHub processed roughly one billion commits in all of 2025, then 275 million per week by mid-2026 — a roughly fourteenfold acceleration in twelve months. At those throughputs, reviewing change at the level of text diffs is structurally impossible. The unit of change cannot remain the text patch; the diff is a human-author artifact that does not scale to AI generation rates. Refinement-oriented programming proposed the refinement — typed, semantically structured, governance-aware — as the unit that compresses what review must process. The article validates the necessity.

**The compiler must revalidate (Chapter 4).** Anthropic describes an automated Claude reviewer running on every change before merge. That reviewer is, in our vocabulary, a class of gate evaluator: an automated judgment producing a structured verdict that participates in the decision to land. The chapter argued that the compiler must do more than parse and type-check; it must revalidate the change against the broader graph of dependencies and policies. The article shows a frontier lab building exactly that capability under a different name.

**The cascade as a working surface (Chapter 5).** Anthropic identifies *research taste and judgment* — choosing which problems matter, which results to trust, when an approach is a dead end — as the area of remaining human comparative advantage. Translated to software-development terms, this is the question every reviewer asks: *if I land this, what propagates? what else moves? what other decisions does this commit me to?* The cascade view in a refinement environment makes that question answerable in a glance. The article does not name the cascade by name; it does describe the human work as having moved to exactly the kind of forward-looking judgment the cascade exists to support.

**Authority, attribution, audit (Chapter 6).** When 80 percent of code is AI-authored, the questions a future engineer or regulator will ask change shape. *Why was this changed?* becomes harder to answer when the author is a model invocation. *Under what authority?* and *citing what policies?* and *with what verdicts?* become structurally necessary to answer, not optional features. The article does not dwell on auditability; Anthropic's internal team knows what they did and why, and their context is research rather than regulated industry. For external customers — especially in regulated contexts — audit is the bottleneck that comes after review. The chapter argued that audit must be a first-class concern of the system, not an export feature. The article does not contradict this; it leaves the door open and the regulated context fills the gap.

**A methodology, not just a tool (Chapter 7).** Anthropic reports an explosion of ideas, initiatives, and tools that has overrun their capacity to pursue them — the article names this as Amdahl's law applied at the organizational level. They name the rate at which an organization can spot and fix shifting bottlenecks as the critical skill of the AI era. Chapter 7 argued that a methodology has to be programmable by its users, because no vendor can anticipate every customization a real organization will need. The article's finding that AI-generated capacity outruns organizational ability to direct it makes programmable extensibility — the scripting layer, the object model, the user-authored gates and hooks — a methodological necessity, not a power-user convenience.

## §3 — What this does not confirm

A manifesto chapter that read too triumphantly here would betray its own discipline. The article confirms the *diagnosis* of the previous chapters. It does not confirm the *delivery*.

It does not confirm that refinement-oriented programming is the only or the best architecture for addressing the bottleneck. Other architectures may emerge — indeed, the Anthropic article itself describes some elements of an alternative architecture being built internally at one company, on different premises, for different users.

It does not confirm that this manifesto's particular vocabulary (refinement, cascade, gate, knob, audit chain, ROM) will be the vocabulary the industry converges on. Other terms may win.

It does not confirm that the specific Refine product, as it exists in implementation today, addresses the bottleneck better than any alternative. The Anthropic article is about the *problem*, not about candidate solutions; we read it as supporting the problem framing the previous chapters laid out, not as judging between solutions.

And it does not confirm that Refine's contextual grounding — Sonibank Niger, BCEAO directives, OHADA articles, WAEMU banking, francophone West African regulatory rhythms — generalizes cleanly to other contexts. Generalization is a hypothesis. The argument that what is true for a regulated francophone West African bank is also true for a Silicon Valley AI lab is a generalization across very different organizational shapes. The article makes that generalization more plausible than it was; it does not prove it.

## §4 — What changes for refinement-oriented programming as a paradigm

If the bottleneck shift the previous chapters predicted is now empirically observed, then refinement-oriented programming as a paradigm has crossed an important threshold. It is no longer being argued in the abstract; it is being argued in the presence of evidence that the world it describes has begun to arrive. Three consequences follow.

The first consequence is rhetorical. Anyone explaining refinement-oriented programming to a sceptical audience can now reference an external, credible source that describes the bottleneck the paradigm exists to address. The argument is no longer one-sided; the evidence has come in. The conversations that used to begin *imagine a world in which AI writes most of your code* can now begin *here is published evidence from Anthropic that this world has arrived in their codebase, and here is what a paradigm designed for it looks like.*

The second consequence is structural. Refinement-oriented programming was developed against the regulatory rhythm of WAEMU banking, where review-and-governance has always been heavy because the regulator demanded it. The bottleneck shift means that what was previously a regulatory burden — careful refinement, authority chains, policy citation, audit — is now a *competitive* requirement for any team operating at the throughput AI generation produces. The paradigm's centre of gravity does not move; the audience for whom it is relevant expands.

The third consequence is intellectual. If the bottleneck shift is real, then the previous decade's worth of programming languages, IDEs, and software-engineering tooling — all designed under the assumption that the bottleneck was *writing* — will need to be re-examined under the assumption that the bottleneck is *reviewing*. That is a vast undertaking; refinement-oriented programming is one early articulation of what the re-examination might produce; we expect other articulations to follow, some convergent and some divergent. The chapter is not closed; it has opened.

## §5 — What does not change

The work continues. Refine is built first for Sonibank Niger and the BCEAO/WAEMU context that grounded its design. The next regulated customer in francophone West Africa is the next priority after Sonibank. The implementation roadmap — the cascade-aware compiler, the StzEngine runtime, the Ring scripting layer, the refinement object model, the agent integration — proceeds along the path the previous chapters mapped. External evidence that the diagnosis was correct is welcome; it does not change what we build, for whom, or in what order.

A manifesto that pivoted on a single external article would not be much of a manifesto. The argument across Chapters 1–8 was made on first principles; the account this chapter reports simply provides the kind of empirical confirmation that first-principles arguments occasionally receive when the world catches up to them. The first principles still hold; the empirical confirmation joins the record.

## §6 — A closing observation about timing

Refinement-oriented programming was being designed at the same moment Anthropic was experiencing internally the bottleneck shift their article reports. We did not know about their experience while we were designing; they did not know about our design while they were experiencing the shift. Two separate work streams, in two very different organizational contexts, with two very different motivations, converged on a shared diagnosis.

That kind of convergence is the strongest evidence the diagnosis is real. When independent observers in different contexts, working on different problems with different methods, arrive at the same description of the underlying phenomenon, the description is unlikely to be an artifact of any one observer's perspective. The bottleneck has moved. The work is to build the infrastructure that will let humans continue to direct what gets built in a world where the writing is no longer theirs to do.

That infrastructure is what refinement-oriented programming proposes. The previous eight chapters described it from first principles. This chapter notes that the world has begun to confirm the description.

## §7 — What this chapter has established — and what it has not

What the chapter has established:

- The bottleneck shift predicted from first principles is now reported empirically from inside a frontier lab: authorship has flipped, review is the constraint, and automated review infrastructure is being built to cope.
- Five of the book's claims receive direct support: the unit shifted, the compiler must revalidate, judgment moved forward, audit became structurally necessary, and extensibility became a methodological requirement.
- The convergence is independent — two work streams, different contexts, same diagnosis — which is the strongest kind of evidence a diagnosis can receive.

What it has not established:

- The delivery. The article confirms the problem, not the solution: not that this architecture is the best answer, not that this vocabulary wins, not that this product outperforms alternatives, and not that the Sonibank grounding generalizes. The diagnosis is confirmed; the bet remains a bet.

The next chapter — Working in parallel — takes up the practical productivity question that follows: now that the bottleneck has moved, how does one supervisor shepherd ten parallel refinements to commit? The architectural answer is the session, parallelized.

# Chapter 10 — Working in parallel

*One human, many agents: how review — not typing — becomes the thing you scale.*

The bottleneck moved. Chapter 9 stated what the move looks like from the outside; this chapter states what it looks like from inside the workday of a programmer or methodologist who is trying to keep up.

The honest description of the workday in 2026 is this: a single human, equipped with current tooling, is asked to supervise more refinements per hour than the human can hold in working memory. Three streams are open at once — the regulatory directive, the customer feature, the performance fix — and each is generating proposals at a rate that, if accepted whole, would land more code than the human reviewed in their first three months on the job. The reviewer's choice is to triage (which means accepting some refinements without proper review), to slow down the agents (which means accepting the bottleneck), or to fragment their attention across all three streams and hope (which means accepting both unreviewed code and worsened decisions). None of these are acceptable.

The escape is not faster reading. The escape is parallelism — but parallelism of a particular shape, structured by the engine, not improvised by the human.

## §1 — Why parallelism is not optional

Programmers have always worked on more than one thing at a time. The team handles three features in flight; one programmer fixes a bug while another adds a screen; a single person juggles a refactor between meetings. Parallelism is not new.

What is new is the scale and the asymmetry. The team's *writing* capacity, when agents are doing the writing, has grown by an order of magnitude. The team's *reviewing and committing* capacity, when the reviewers and committers are still humans, has not. The ratio between proposals produced and proposals reviewed has tipped from roughly one-to-one (everyone writes; everyone reviews about as much as they write) to roughly ten-to-one. Three programmers can produce sixty proposals a day; the three of them can review six. The other fifty-four are stranded.

Strain a system at the asymmetric joint long enough and the system gives up the harder side. Teams either stop reviewing carefully (the worst outcome and, predictably, the dominant outcome in places that have not addressed the bottleneck) or they slow the writing to match the review (which surrenders the productivity gain that motivated agent adoption in the first place) or they find a structural answer.

The structural answer is to make one human able to supervise *many* sessions at once, by changing what supervising means.

## §2 — What the session is, and what it adds to the refinement

The previous chapters defined the refinement: the smallest unit of change in the graph, with its cascade, its authority, its commit boundary. The refinement is the right unit for the engine, but it is too small to be the unit a person inhabits while working. A person works in coherent units that span several refinements: a feature, a regulatory directive, a refactor, a hardening pass. These units have scope, intent, and duration that the single refinement does not capture.

The session is that unit. It is the working context within which several related refinements are proposed, reviewed, and committed as a coherent piece of work. A session has a name (something the author chose, like *q3-letter-compliance*), a scope (the constructs it may touch), a policy (how it surfaces overlap with other sessions), an authority (who can author, who reviews, who commits), and a state (in progress, awaiting review, committed, abandoned). It contains zero or more refinements. It produces a timeline.

A session is what a programmer means when they say "I was working on the BCEAO directive this morning." Before refinement-oriented programming, this unit existed only in the programmer's head and, partially, in a git branch. With refinement-oriented programming, the session is a graph object the engine knows about. The engine can compute its cascade, surface its overlaps with other sessions, enforce its scope, audit its history. The work has a structural location, not just a mental one.

The session was always implicit in how programmers worked. Making it explicit — making it a thing the engine can reason about — is what makes parallelism scale.

## §3 — Three policies for overlap

When several sessions run at once, some of them will touch shared constructs. The team has to decide what should happen when they do. Three policies, chosen per session or per construct, cover the spectrum.

The first is **optimistic**: sessions proceed independently and the engine surfaces overlaps as signals to both authors, who decide whether to coordinate. This is the default because most sessions are independent — most refinements touch disjoint parts of the graph — and the cost of coordinating sessions that did not need to coordinate is wasted attention.

The second is **pessimistic**: a session acquires a lock on its declared scope when it opens, and other sessions cannot touch the locked constructs until the first session commits or releases. This is for the cases where the cost of a conflict at commit time is much higher than the cost of waiting — production-critical constructs, regulated reporting templates, credit-decision rules. The compliance officer sets pessimistic policy on these constructs as a team default; everything else stays optimistic.

The third is **speculative**: a session may declare a dependency on an uncommitted refinement in another session, and its own commit is gated on that dependency landing. This is how agent fleets work: many sessions building on each other's proposals, the human committer landing them in batches in the correct order. Speculation is also useful between humans — a methodologist proposes a refinement that depends on a compliance officer's pending validator change, so the engine can re-validate the whole package before either side signs off.

The discipline is that the team chooses the policy explicitly, per construct or per session. Default optimistic is the *default*, not the requirement. A team that runs every session pessimistic has chosen safety over throughput, which is sometimes correct. A team that runs everything optimistic has chosen throughput over safety, which is sometimes correct. The choice is the team's; the engine enforces what was chosen.

## §4 — From writer to supervisor

Once the session is a first-class thing and the policies are explicit, the human's role can change. A programmer who once worked one branch at a time, writing and reviewing both, becomes a person who opens five or ten sessions at once, supervises them, and commits the work as it ripens.

The cognitive trick is that the engine holds the state. The human does not have to remember which session was touching the credit rules and which was touching the reporting template; the session indicator tells them. They do not have to mentally simulate what happens if both sessions commit; the cascade preview shows them. They do not have to remember which session blocks which; the signals attached to each session surface the dependency. The engine is the working memory.

What the human contributes is judgment: deciding which proposals are good, which conflicts are real, which sessions should commit and which should wait, which agent-driven sessions are doing useful work and which are confused. These are decisions a human is much better at than an agent, and they scale per supervisor at a rate close to N (number of sessions) rather than constant (one session at a time).

The supervisor pattern is the productivity gain. It is not faster typing; it is more sessions per person. A single methodologist supervising ten agent-driven sessions, with proper signaling and proper policy, lands more correct work in a day than ten programmers writing in the old model. This is the structural answer to the asymmetric joint: change the role on the slow side, do not pretend the slow side can be sped up by individual effort.

> **Figure 10.1 — One supervisor, many sessions.** The engine holds the state — scopes, overlaps, signals, dependencies — and the human contributes the judgment: which proposals are good, which conflicts are real, which sessions commit and which wait.

## §5 — The signaling discipline

A common failure mode in parallel-work tooling is the *modal interrupt*: a popup that demands the user's attention right now to resolve a conflict. Modal interrupts are catastrophic in a fleet supervisor's workflow. If every signal is a popup, five sessions running in parallel means five popups in five minutes, and the supervisor's attention is shredded.

The signaling discipline is the opposite: signals are persistent indicators the supervisor attends to when convenient. A signal on a session shows as a colored chip on the session card, a count badge on the session indicator, a marker on the shared construct in the tree view. The signal does not interrupt the author's current session. The author finishes the thought, looks up, sees the signals, decides which to address.

This is the discipline transferred from how a working programmer manages their own attention in the old model: they do not check their inbox every ten seconds. They check it at intervals, when they are between tasks. Signals work the same way. The engine holds the state; the human attends when ready.

The same discipline applies between humans. Author A is in the middle of a refinement when author B's session generates a signal that overlaps. The signal does not interrupt author A; it queues. Author A finishes, sees the signal, decides whether to coordinate now, defer, or proceed in parallel knowing the engine will surface any conflict at commit. The default is *not* to interrupt; the default is to let the work continue and surface state when the author looks for it.

A team that adopts modal-interrupt-style signaling has not adopted parallel sessions correctly. The architecture supports the right discipline; the team has to choose it.

## §6 — Cross-authority cascades

The hardest problem in parallel sessions is the one this chapter is least ready to fully solve: cross-authority cascades.

The scenario. Session A has authority to touch credit-decision rules. Session B has authority to touch reporting templates but not credit-decision rules. Session B's proposed refinement, however, would cascade through a construct in A's zone — perhaps because the reporting template depends on a value computed by the credit-decision rule, and B's change forces a re-derivation in A's territory.

This is not a conflict between A and B in the usual sense. B is not trying to touch A's zone; B's cascade reaches into it as a consequence. The engine has to decide: does B's refinement land? It cannot land if it forces a change A's authority did not approve. It cannot be silently rejected, because B did not violate any explicit rule — B's own scope was respected.

The current answer is a hard stop at proposal time: the engine surfaces the cross-authority cascade as a signal and B cannot commit until either the scope is narrowed, A's authority extends the scope, the two sessions merge into a joint session with combined authority, or B abandons.

This is an honest answer that says *we know this is a problem and we have not yet built the friction-free workflow*. The friction-free workflow probably involves a scope-extension request protocol, batch authority approvals, and joint-session creation as cheap as opening a tab. The design of these workflows has to be informed by actual practice at Sonibank Niger; the spec leaves them open until practice arrives.

Honesty about open problems is part of the discipline. The architecture handles cross-authority cascades correctly (it does not let unapproved changes through). The user experience for resolving them is not yet ergonomic. The team adopting the paradigm should expect to feel friction here.

## §7 — What changes for the auditor

The audit story is the unexpectedly strong consequence of parallel sessions. In the text-diff world, a regulator visiting a bank to audit a quarter's changes has to reconstruct the merge story from commit messages, branch histories, and the implicit ordering of when things landed in main. The reconstruction is archaeology, and the answers depend on how well commit messages were written.

In the session model, the merge story is the native artifact. The auditor opens any time window and sees: which sessions were active, which refinements they proposed, which signals fired between them, how the conflicts were resolved, who committed which refinement against which base, in what order. The story is in the graph because the events happened in the graph. No reconstruction needed.

A BCEAO auditor in 2026 can ask: "Show me every session that touched the credit-decision rules in Q3, ordered by commit time, with the cross-session signals each one generated." The query returns the sessions, their actors, their refinements, their committers, their timelines. The discipline holds at the audit layer because the discipline held at the session layer.

This is the kind of consequence that justifies the paradigm at the boundary that matters most for regulated software. The audit is not an afterthought retrofitted onto the workflow; the audit is what the workflow produces.

## §8 — What this requires of the team

Parallel sessions are not a tool you turn on. They are a discipline the team has to adopt, with three changes that have to be made together for any of them to work.

The first change is that someone has to be the supervisor. The role exists in any team, but in the old model it was often diffuse — everyone was their own supervisor on their own branches. In the parallel-sessions model, the supervisor role concentrates: one person (or sometimes two, by rotation) is responsible for the fleet of sessions, and other people contribute to individual sessions. This is not a hierarchy reshuffle; it is a recognition that supervising a fleet is itself a distinct kind of work, with its own skill, and treating it that way is the first move.

The second change is that scope and policy have to be set explicitly, per session and per construct, by people who know the work. Compliance officers set policy on regulated constructs. Engineering leads set policy on platform constructs. Project leads set scope on feature sessions. The team adopting parallel sessions has to do this organizational work before the productivity gain materializes. A team that does not set policy or scope has effectively chosen optimistic for everything, which is sometimes fine and sometimes catastrophic depending on the work.

The third change is that the signaling discipline must be respected. No modal interrupts. No anxious checking of every session every ten minutes. Trust the engine to hold state and surface it when attended to. This is a cultural change as much as a tooling change. Teams that adopt the tooling without the discipline get fragmented attention and worse outcomes than they had before. Teams that adopt both get the productivity gain the paradigm promised.

The work of adopting parallel sessions is the work of building these three changes simultaneously. The architecture supports them; the team has to make them real.

This is no longer a lonely prediction. As I write, the consultancies that advise development teams are arriving at the same picture from the organizational side, and the convergence is a comfort. They say a team should be sized by the *value and complexity of the domain it owns* — not by headcount or story points — so that a handful of experts piloting many agents replaces a room of developers; and that the binding constraint has become the *quality of decisions*, not the speed of production. That is this chapter's argument in the vocabulary of team design, and it carries one piece worth taking back: the practice they call *context engineering* — a living, shared structure of the team's knowledge, its domain rules and conventions and decisions, that the agents read and the humans maintain. It is the right instinct, and it is exactly what this book has described, with one difference that is the whole difference. They keep that knowledge as loose documents, owned by convention and kept honest by discipline; the paradigm keeps it as the governed graph — typed, attributed, compiled, owned by the team the way a codebase is owned, not the way a wiki is. The same commitment that the context belongs to the team and never to the agent, made structural instead of cultural. Their advice is to write the knowledge down and share it; the paradigm makes the writing-down *be* the work, and makes it something a compiler can hold you to.

## §9 — What this chapter has established — and what it has not

What the chapter has established:

- Parallelism is structural, not optional: writing capacity grew by an order of magnitude and review capacity did not; the asymmetric joint must be redesigned, not strained.
- The session is the unit of work — named, scoped, policied, stateful — and making it a graph object is what lets supervision scale.
- Overlap is a chosen policy, per construct or per session: optimistic, pessimistic, or speculative.
- The supervisor pattern is the productivity gain: judgment scales with the number of sessions once the engine holds the working memory and signals replace interrupts.
- The audit story strengthens: the merge story becomes the native artifact rather than archaeology.

What it has not established:

- An ergonomic resolution for cross-authority cascades. The engine handles them correctly — nothing unapproved lands — but the workflow for resolving them still carries friction, named openly in §6.
- That five-to-ten sessions per supervisor is a law. It is the empirical sweet spot for review as currently practiced; the consultancies' "dozens" is the aspiration the cascade's compression is meant to enable.
- The organizational changes themselves. A named supervisor, explicit scope and policy, the signaling discipline — the architecture supports them; only the team can make them real.

The next chapter — Writing loops, not prompts — takes up the third primitive the paradigm has had to wait for: the unit of automation that produces sessions and refinements, recognized when Boris Cherny, the creator of Claude Code, named what senior practitioners had quietly already been doing.

# Chapter 11 — Writing loops, not prompts

*From one-shot prompts to durable, governed loops: telling the agent the procedure, not just the wish.*

Boris Cherny, the creator of Claude Code, gave a talk in May 2026 in which he said something that the engineering community noticed: *"I don't write prompts for Claude anymore. I have a whole set of loops running. My job now is writing loops."* The line went around the discipline because it named, with unusual directness, a shift that many practitioners had already been making without saying out loud. The unit of human authorship for AI-assisted engineering work was moving up one rung — from the per-turn prompt to the per-workflow loop.

The article this chapter responds to closed with the observation that Anthropic had productized the pattern as Dynamic Workflows on the 28th of that same month, and that the internal teams at Anthropic — research, code review, agent development — had been writing custom harnesses for some time before that. The senior practitioner's day was no longer composed of clever messages and watchful reading. It was composed of *designing structures that ran themselves*, and watching the outputs of those structures.

This chapter argues two things. First, that Boris's shift is structurally identical to the shift this manifesto has been making — the move from text diffs to refinements — at a different layer of the system. Second, that recognizing the parallel is the precondition for naming a third primitive in the refinement-oriented paradigm: the *loop*. The paradigm has had two primitives until now (the refinement and the session); the third has been quietly necessary for some time, and Boris's observation is the cue that names it openly.

## §1 — The two shifts are the same move at different layers

The manifesto has been making, in slow rotation, one structural argument: when human capacity becomes the binding constraint of a system, the way to scale that capacity is to make the unit of human authorship more durable, more reviewable, more composable. Move it up one rung of the abstraction ladder. The artifact the human produces should be a *named, addressable, versioned, governable thing*, not a transient utterance.

This argument was applied first to changes. The text diff is a transient utterance; the refinement is a named, addressable, versioned, governable artifact. The change that used to disappear into a commit message now persists as a graph object with cascade, authority, lifecycle, and audit attribution. The human's work shifted upstream — from typing edits to designing refinements. Refinement-oriented programming was the name of that shift.

The same argument applies, with surprising directness, to conversations. The prompt is a transient utterance — composed for one turn, used once, often lost to chat-log archaeology. The loop is the named, addressable, versioned, governable artifact: a workflow definition that specifies intent, stages, verification, retry, branching, and success criteria, designed once and run many times. The conversation that used to disappear into a sequence of messages now persists as a graph object that the team reviews, the audit reads, and the engine executes.

The two moves are not coincidental. They are the same response pattern, applied at different layers of the same system. The change layer; the conversation layer. The same pressure (human review-and-design capacity is the constraint); the same answer (move the unit up one rung); the same kind of artifact (typed, durable, composable). Two different teams — Anthropic from the model side, Softanza from the codebase side — arriving at the same shape from different starting points is the evidence that the shape is correct. The shape is not specific to either team's vantage. It is the structurally right answer to the problem both face.

## §2 — The third primitive

The refinement-oriented paradigm has had two first-class primitives:

The **refinement** is the unit of *change*. *What is being modified in the codebase.* A typed graph delta, with cascade, authority, lifecycle, audit attribution. This was Chapter 2's argument.

The **session** is the unit of *work*. *Why, and by whom, and within what scope, the change is being made.* A bounded episode that contains many refinements, with intent, policy, committer chain, parallelism. This was the argument of the parallel-sessions chapter (Chapter 10).

A third unit has been quietly necessary for some time, and Boris's observation is what makes it explicit:

The **loop** is the unit of *automation*. *How the work proceeds, stage by stage, with verification and retry, in a structure that runs the same way every time it is invoked.* A typed workflow definition that produces sessions and refinements when executed. Designed once, run many times. Versioned. Reviewable. Governed by the same authority model as the rest of the system.

The three primitives compose. A loop runs within (or defines) a session. A session contains refinements. The audit chain reads from refinement to session to loop and back. Each unit is addressable independently — a team can author a loop without opening any session; a session can use any loop in the library; an audit can trace a refinement to its loop independently of the session it ran in.

The three units, named together, are the complete answer to the question *how is software written when agents do most of the writing?* The refinement says what changes. The session says why and by whom. The loop says how. Each had to wait for the technological and operational pressure that would name it. Refinements emerged when the cost of agentic writing collapsed and review became the bottleneck. Sessions emerged when parallel work required durable bounded contexts. Loops emerged when senior practitioners stopped composing prompts and started composing workflows.

## §3 — The gate is a loop

The argument that the paradigm has needed loops all along is best made by observing that one of its central artifacts already *is* one. The gate (specified in `REFINE_GATE_v0_1`) is a fixed, opinionated, eleven-stage workflow: intent, rebase, cascade, review, test, document, lint, authority, push, PR, CI. Every stage has its verification step. The on-failure transitions route to the fix-rounds subloop, which iterates within the failed stage until either the verification passes, the auto-fix limit is reached, or the human pauses the run for judgment.

That is a loop. It has stages, transitions, verification, retry, success criteria. It runs the same way every time it is invoked. It produces refinements (through the validation pipeline, as Chapter 2 specified). It carries authority constraints and a cost budget. The gate is not merely *like* a loop; it is the canonical loop the paradigm has been building toward.

The reason the gate has not been called a loop is that the paradigm did not yet have the word. Now that it does — and the practitioners building agentic-era harnesses have arrived at the same word — the gate's identity becomes clearer. It is `l/refine-gate`, version 1.0, the first entry in the canonical library of loops.

This matters because once the gate is recognized as one specific loop, the existence of *other* loops becomes plausible. The BCEAO directive intake loop. The regression triage loop. The documentation drift loop. The compliance audit response loop. The refinement anchoring loop for teams climbing from the gate rung to the IDE rung of the adoption ladder. Each is a structured workflow that produces refinements. Each is reviewable, versionable, governable like the gate. The gate is the canonical one; the others are the library that teams build over time as their work patterns settle.

The BCEAO directive intake loop — one of the six in active design — is what this becomes at Sonibank. A circular arrives each quarter; the loop's stages are always the same: parse the directive into proposed policy refinements, validate each against the existing rule set, queue the compliance review, land what Aïcha approves, file the audit bundle. Nobody re-invents in a July prompt window the procedure that was designed in April. The loop is versioned; the quarter's run references the version; and when the regulator asks how directives become code, the team points at the loop instead of describing a habit.

## §4 — What changes for the team

The team adopting loops makes a series of changes that are similar in shape to the changes adopting refinement-oriented programming required.

The first change is that there has to be a *loop author* on the team. In small teams this is the same person who designs the architecture; in larger teams it becomes a distinct role, often filled by a methodologist or a senior engineer whose primary output is the team's library of loops. The role exists in the prompt-era too — someone wrote the team's prompt templates — but it was implicit and the artifacts drifted across copies. With loops, the role is explicit and the artifacts are governed.

The second change is that loop review becomes a thing the team does. A new loop in the library is reviewed before it advances from `tested` to `active`, the same way a new refinement is reviewed before it lands. The review reads the intent, examines the stage structure, checks the verification at each stage, considers the failure modes, runs the dry-run output against historical sessions. The team that does this well builds a library of loops whose reliability compounds over time.

The third change is that the day-to-day work of senior practitioners shifts. The person who used to spend their day composing prompts and reading responses now spends their day designing loops, watching the Runs sublevel, intervening when a loop pauses for human judgment, and adjusting loops when the Monitor sublevel shows degrading performance. The output is more concentrated and more visible than prompt-craft; the discipline is more like writing code than like writing emails.

The fourth change is that the audit story is one layer richer. A regulator visiting the team in 2027 can ask: *which loop produced this refinement, in what version, under what authority?* The answer is one query against the refinement's provenance. The team that has invested in the loop library, with proper versioning and dry-run discipline, has the strongest possible answer to that question. The team that has not has only its own memory.

These changes do not arrive overnight. They are the same kind of gradual shift the refinement-oriented paradigm required for the change layer: a year for the discipline to settle, several years for the muscle memory to be steady. The team that begins early settles early. The team that waits for the practice to be universal settles late, with less time to refine its own library.

## §5 — The honesty discipline carries over

The manifesto has, throughout, held to one rule: claim less than is true, then defend the claim. The Loop primitive is named here because Boris's observation made it necessary to do so; the spec for it is written because the architecture already supported it; the canonical library is named because six concrete loops are in active design. None of this is speculation about a future that has not arrived.

What is *not* claimed: that loops solve the problem of agent reliability. They do not. A loop that invokes an unreliable agent at one of its stages produces unreliable output; the loop's verification step can catch some of it, but the verification is itself produced by an agent at the next stage. The discipline buys structure, not magic. The team that hopes loops will make their agents trustworthy will be disappointed; the team that uses loops to make agent unreliability visible, attributable, and bounded will see the benefit the architecture provides.

What is also *not* claimed: that every team needs loops. A small team running occasional refinements under direct human supervision does not need a loop library; the gate alone is sufficient, and the gate exists already. Loops become valuable when the team is running enough agent work, in enough parallel sessions, that the workflows become repeatable and the cost of designing them once is paid back many times. For most regulated-software adopters, the threshold arrives around the second or third project; for prompt-era hobbyists, it never arrives. Neither outcome is wrong; the loop is a tool whose value scales with the volume of agentic work the team handles.

The third unit completes the paradigm's core. Future chapters of this book will explore specific applications — the canonical library in detail, the migration of script-shaped workflows to loop-shaped ones, the discipline of versioning a team's loops over years — but the primitive itself is named, the architecture supports it, and the practice has begun. Refinements were the unit of change. Sessions were the unit of work. Loops are the unit of automation. The three together are how regulated software gets written in the agentic era.

## §6 — What this chapter has established — and what it has not

What the chapter has established:

- The loop is the third primitive: the unit of automation, a typed workflow designed once and run many times, versioned and governed like everything else.
- The shift from prompts to loops is the same move as the shift from diffs to refinements, one layer up — and two teams reached it independently, from opposite sides.
- The gate is the canonical loop, and recognizing it as one is what makes the rest of the library plausible.
- Adopting loops changes the team: a loop author emerges, loop review becomes practice, and the audit story gains a layer — which loop, in which version, produced this refinement.

What it has not established:

- That loops solve agent reliability. They make unreliability visible, attributable, and bounded; they do not remove it.
- That every team needs a loop library. The value scales with the volume of agentic work; below the threshold, the gate alone is enough, and never crossing the threshold is not failure.

The next chapter takes up the abstraction layer that sits *above* the three primitives: the vocabulary the agent uses to call the operations the team has codified — the set of named, typed, governed words an agent can pronounce when it wants to do work. A skill, in Refine, is one word of that vocabulary.

# Chapter 12 — The agent's vocabulary

*The verbs an agent actually uses here — query, propose, check, commit — governed, not freeform tool-calling.*

A team that has been working under refinement-oriented programming for a few months ends up with a particular kind of artifact in its repository — a set of named operations the team has decided are worth doing well, often enough, that they deserve their own word. *Migrate this table.* *Tighten this policy.* *Re-affirm the satisfies-links on the loan node.* *Refactor the eligibility scorer.* These are not refinements; each one *produces* refinements when invoked. They are not sessions; a single session may invoke several. They are not loops; some skills are simpler than loops, some are loops, some are LLM-led reasoning under loop-shaped bounds. They are something else — a fourth artifact, layered on top of the three primitives, with its own purpose.

The purpose: to give the agent a vocabulary.

## §1 — Why a vocabulary is necessary

In the pre-paradigm world, a user told an agent what to do in natural language. The agent did something. Sometimes it was the right thing. Sometimes it was something close but wrong. Sometimes it was something obviously wrong but plausible-sounding. The variance was high; the audit chain pointed back to *the model said so;* the team carried the risk.

The first move toward bounding this was the agent's *capability set* — the typed list of operations the agent was allowed to perform. The next move was *authority* — the typed list of who-may-do-what under what scope. The third move, which this chapter takes up, is to give those typed operations *names*. Not nicknames; not labels; *names* with grammar, signatures, contracts, and versions.

A name is what lets an agent decide. The agent reads a user's request — *"can you tighten the penalty cap for Q4 lending under the BCEAO Q3 directive?"* — and picks a skill: `tighten_policy(point: lending/penalty_cap, new_value: 18%)`. The skill is the call point. Its signature tells the agent what parameters it needs. Its pre-conditions tell the runtime what to check before the call is allowed. Its post-conditions tell the runtime what to verify when the call completes. Its authorities tell the compiler whether *this* agent, *here*, in *this* session, has permission to make the call at all.

Without the named call point, the agent's only option is to do the work raw — generate refinements directly, in whatever shape the LLM produces. The audit chain leads back to a model output and a prompt. With the named call point, the audit chain leads back to a *skill* — a versioned, typed, contracted operation the team explicitly defined. The difference is not cosmetic. Regulators do not audit prompts. They audit operations. The named call point is what makes the operation auditable.

This is the same move that programming languages made when they introduced *named procedures.* A program without procedures is a stream of instructions; the audit trail is the instruction sequence. A program with procedures is a composition of named operations; the audit trail is the call graph. The named procedure was not just a way to reuse code; it was a way to give the operation a *name* that the program's reader and the language's compiler could both reason about. Skills are the same move, one level up: for the agent's calls into the runtime, not the procedure's calls within the program.

## §2 — What a skill is

A skill is a typed, versioned, governed graph node that declares:

A *signature* — a name, a list of typed parameters, an outcome kind. Like a function signature in a typed language, except the types refer to the project's domain (TableRef, SchemaRef, PolicyPoint, ModuleRef) rather than language primitives.

A *kind* — one of three: `pi` (deterministic, no LLM), `hybrid` (governance-gated, judgment at gate points), `llm-led` (LLM at the core, bounded by the skill's contract). The kind is declared, not inferred; the compiler refuses skills whose impl violates their declared kind.

A set of *pre-conditions* — typed predicates the runtime checks before allowing invocation. A pre-condition is not a comment; it is executable. *"from-table exists"* is checked against the project graph; if it cannot be checked, the skill cannot be declared.

A set of *post-conditions* — typed predicates the runtime verifies after completion. Failure of a post-condition marks the invocation failed and may trigger the impl's reversal.

An *implementation* — a pointer to a loop, a refinement template, or a script. Most skills wrap loops; some wrap simpler templates; a few wrap scripts. The impl is versioned independently of the skill's contract.

A set of *authorities* — the agents or roles authorized to invoke the skill. Authority is a property of the skill (who may call it), bidirectional with the agent's `use:` capability set (what the agent claims to know how to call). The compiler reconciles both at gate time.

A *version* — bumped on contract change. Impl changes that preserve the contract bump the impl's version, not the skill's.

A set of *tests* — invariants the skill must satisfy. Skill-level tests are not implementation tests (the loop or template has its own); they are *contract* tests, verifying that pre/post-conditions hold for sample invocations and that authority enforcement actually rejects unauthorized calls.

What this adds up to: a skill is the interface; everything below the skill is mechanism. The agent invokes by name; the runtime takes care of the rest, under the discipline the skill declares.

## §3 — The three kinds, briefly

A *pi* skill is deterministic. `migrate_table` is pi: given the same inputs and the same graph state, it produces the same refinements. No LLM is consulted. The audit trail is the inputs and the impl's version. These are the easiest to test, the easiest to reverse, and the most common in mature projects.

A *hybrid* skill has a deterministic structure with one or more governance gates inside it. `tighten_policy` is hybrid: the structure (validate the policy point, check the regulatory floor, enqueue for human review, compute cascade) is deterministic; the gate (the human reviewer's decision to accept or reject the new value) is not. Hybrid skills are how Refine handles operations that require judgment without losing structure — judgment lives at the gate, structure lives in the skill.

An *llm-led* skill has an LLM at its core, bounded by the skill's contract. `refactor_module` is llm-led: the skill's signature says *(module, intent)*, the pre-conditions check the module exists and the intent is non-empty, the post-conditions verify that every refinement the LLM emitted is attributable to the session and the attribution chain is intact. The LLM proposes; the session commits. The skill provides the bounded surface inside which the LLM operates.

The distinction matters because it tells the team — and the regulator — what to expect from a given operation. A pi skill produces a predictable outcome; a hybrid skill produces a structured judgment; an llm-led skill produces a bounded LLM proposal. None of the three is "better"; they cover different territories. Most projects use all three.

## §4 — How skills relate to loops

The cleanest way to see the boundary: a skill is an *interface*, a loop is an *implementation*. Most useful skills are implemented by loops, because most useful operations have multiple stages. But the boundary matters because the *interface* is what the agent calls and the *implementation* is what the engine runs, and conflating them leads to confusion in both directions.

A skill *may* be invoked without a loop — when its impl is a refinement template (one-shot operations like `rename_construct(old, new)`) or a script (simple deterministic operations that don't benefit from staging). A loop *may* be invoked without a skill — when it runs autonomously on a schedule (the documentation-drift loop runs nightly without any agent calling it) or fires on a trigger (the gate loop runs on PR-opened).

Skills exist for the cases where an agent calls an operation by name with parameters under authority binding. Loops exist for the cases where an operation needs staged execution with verification gates. The two compose: skill-wraps-loop is the common case; skill-without-loop is the simple case; loop-without-skill is the autonomous case.

When a skill wraps a loop, the skill's contract (pre, post, authority) becomes the loop's entry and exit conditions. The loop's stages are not visible at the skill's surface; only the skill's signature and contract are. This is the seam between the agent's world (named operations) and the engine's world (staged pipelines). Either world is incoherent without the other; the seam is where they meet.

## §5 — The collision with Anthropic Skills

The word "skill" is already in industry use, and the most prominent use is Anthropic's. In Claude.ai, Claude Code, and the Claude API, a "Skill" is a folder containing a `SKILL.md` file plus supporting materials that tells Claude how to approach a particular kind of task — write a Word document, build a React component, fill a PDF form. The `SKILL.md` is instructional: when to use this skill, what conventions to follow, what to avoid.

Refine's skills are different. Refine skills are *operational*: typed graph nodes with signatures, pre/post-conditions, authority bindings, and versioned implementations. The Anthropic Skill informs the LLM's *approach*; the Refine skill bounds the LLM's *output*. They are different layers of the same general territory.

The two compose well. An llm-led Refine skill — `refactor_module` — may benefit from Anthropic Skills loaded into the LLM's context when the skill body executes. The Anthropic Skills shape the LLM's thinking; the Refine skill bounds the LLM's output. An Anthropic Skill is part of the prompt; a Refine skill is part of the contract.

This book uses "skill" (lowercase) to mean Refine's concept — the *operational* skill — and "instructional skill" for the community format, reserving "Anthropic Skill" for sentences specifically about Anthropic's products. The vendor-neutral name matters: the format has outgrown its originator. It is now a de-facto community standard, model-agnostic and installer-distributed, and it carries real engineering methodology. The most-starred skills collection in the community — `mattpocock/skills` — condenses decades of practice (the grilling session for alignment, the ubiquitous-language document, triage as a state machine, vertical-slice TDD, the out-of-scope knowledge base) into small composable instruction sets that any agent can consume. That body of practice is not a vendor convenience; it is the community independently attacking the same problem Refine attacks — converting raw model capability into reliable work — at the prompt layer rather than the runtime layer.

So Refine embraces the layer rather than holding it at arm's length, and adds the one thing the format cannot give itself: governance. Instructional skills installed under `.refine/skills/instructional/` are registered as graph citizens — source, content hash, trust label. An llm-led operational skill declares its `guidance:` — the instructional skills, pinned by hash, that load into its body's context. Every turn records which guidance actually loaded, at which version, in the context-assembly record. The audit question the rest of the industry cannot answer — *what guidance shaped this output?* — gets a graph answer. The community brings the practices; Refine brings the governance.

That the format *needs* the governance from outside is not my inference; it is the format's own design. The community has by now turned the loose convention into a published standard — an open specification, a folder shape, a small frontmatter schema, a validator — and the striking thing about reading that specification is what it deliberately leaves out. It defines no versioning, no trust model, no signing, no permissions, no sandboxing, no registry. Not by oversight: by choice, in the name of simplicity and portability. A skill that asks for nothing of its host travels everywhere. That intentional ungovernedness is the cleanest possible statement of the gap this book has been describing — the format stays portable precisely *because* it omits governance, and Refine supplies the governance the format omits without forking the format. A skill that validates against the standard validates against Refine; what Refine adds sits around the unmodified skill, not inside it.

What it adds turns adoption into a governed act rather than a copy-and-trust. Installing a community skill runs it through a small pipeline that mirrors the compiler's own stages: the standard's validator checks its shape; a security scan checks it for the patterns that turn a helpful skill into a hostile one — the ecosystem has produced dedicated scanners for exactly this, because the empirical reality is that a non-trivial fraction of public skills carry vulnerabilities and a smaller fraction carry intent; a methodologist reviews what the machine flags; and only then does the skill earn a trust label and a place a governed session will load. The stakes have risen with the libraries: security-skill collections now ship offensive tooling beside defensive — red-team playbooks, malware analysis, helper scripts that execute with the agent's own permissions — so a skill's declared *intent* becomes part of its trust profile. An offensive-capability skill is adopted only under elevated authority and runs only inside a scope that permits it, never against the compliance code or the production data.

The sharpest case is a single field. The standard lets a skill *declare* the tools it intends to use — a line that says, in effect, *this skill may run git and read files, nothing more.* But the standard marks the field experimental and advisory: an agent may honor it or may not. A declaration with no enforcement is a promise with no teeth. Refine gives it teeth, and does so without inventing anything — it routes the skill's body through the governed sandbox this book takes up in Chapter 15, where the only tools that exist are the ones the skill declared, narrowed further by what the calling authority is itself permitted. A tool the skill did not ask for is not *forbidden and checked*; it is *structurally absent* — there is no reference to it to misuse. The format lets a skill say what it needs; Refine makes the saying the only thing it can do.

The collision is real and worth naming because senior practitioners moving between the two ecosystems will encounter both words. Mistaking one for the other produces confusion at exactly the moments — adoption, audit, regulatory review — when confusion is most expensive.

## §6 — Why this is not a fourth primitive

The Refine paradigm has three primitives: refinement (the unit of change), session (the unit of work), loop (the unit of automation). Skills are not added as a fourth.

The reason: a primitive is a thing the runtime cannot decompose. Refinement is a primitive because below it there is only the diff, and the diff is not the unit the runtime governs. Session is a primitive because below it there is only the turn-and-tool-call stream, which is not auditable as a coherent piece of work. Loop is a primitive because below it there is only the script, and the script is not the unit that gives the team a vocabulary for automation.

A skill, in contrast, *is* decomposable. A skill is an interface to a loop, or a template, or a script — its implementation. The runtime that knows refinements, sessions, and loops can run skills without adding a new primitive. The skill adds a *naming layer* on top of the primitives, the way procedures add a naming layer on top of instruction sequences. Procedures were not a primitive of CPU architecture; they were a discipline imposed by programming languages on top of the primitive of instruction. Skills are the same: a discipline imposed by methodologists on top of the primitives of refinement, session, and loop.

This distinction matters for adoption. A team can adopt refinement-oriented programming and run without skills — they will define operations directly through sessions and refinements, and that will work. A team that adopts skills before it has stable patterns to codify will produce premature skill abstractions, with contracts that bend awkwardly as the work evolves. Skills earn their place when the patterns have stabilized; the primitives earn their place from the first day.

## §7 — The vocabulary as a project deliverable

Over time, a project's skill catalog becomes one of its most valuable deliverables. New team members learn the project by reading the catalog — what operations the team has codified, what their contracts are, who can perform them. Auditors review the catalog when they want to know what the team is allowed to do; the answer is the union of the authority sets across all active skills. Regulators audit the catalog as part of any compliance review; the catalog is the operational interface between the project's intent and its execution.

The catalog is also where the team's *thinking* lives. A skill is a small piece of designed work — *this is what we have decided is worth doing, repeatedly, well.* The codification of `migrate_table` is not just a technical artifact; it is the team's collective decision about how schema migrations should be done in this project, under these constraints, with these checks. The decision survives turnover, scales to new team members, and is auditable when something goes wrong.

This is the deliverable that the Anthropic-Skill folder cannot produce, however well-written. An Anthropic Skill is an instruction; a Refine skill is a contract. Instructions can be argued with; contracts have authority. For regulated work, the contract is what the project hands to the regulator. The instruction is a tool the project uses internally.

The two are not interchangeable. A project that has only instructional skills (no operational skills) is a project where the agents have *approaches* but no typed *calls* — the operations they perform are raw refinements, however well-shaped; this is where the community is today, and it is also why the community's practices remain ungoverned. A project that has only operational skills (no instructional skills) is a project where the agents have *calls* but no learned *approaches* — the LLM in an llm-led skill operates without the conventions the community's experience would have given it. Both are partial. The full picture is both, composed through the typed `guidance:` binding, with the boundary clearly named.

## §8 — The discipline of authoring

Skills are not written speculatively. The discipline of skill authoring is: do the work several times without a skill, recognize the pattern, write the skill, promote it from draft to tested to active. Each step is a refinement on the skill node, attributable to the methodologist who made the decision.

The premature skill — the one written before the pattern has been seen enough — is the most common failure mode. It produces skills with signatures that fit the first case awkwardly and the second case worse, pre-conditions that turn out to be wrong, post-conditions that miss the actual invariant the team needed. The remedy is empirical: live with the work for a while before codifying it. A methodologist's instinct to abstract early is the same instinct that produces over-engineered class hierarchies in object-oriented systems. The discipline is to wait.

The corollary: a project's skill catalog grows slowly, deliberately, and with deletions as well as additions. Skills that turn out to be wrong are deprecated. The catalog is curated, not accumulated. Five well-tested skills are worth more than fifty draft ones. The size of the catalog is not the measure of a project's maturity; the *fit* of the catalog is.

## §9 — What this chapter has established — and what it has not

Skills are the agent's vocabulary — the named, typed, governed operations the team has decided are worth codifying. They are not a fourth primitive but a naming layer on top of the three primitives. They give the audit chain a name to point at when an operation is performed; they give the regulator a contract to audit; they give the team a deliverable that captures its thinking about how its work should be done.

The collision with Anthropic Skills is real and worth naming. The two compose; they are not the same.

The discipline of skill authoring is patience: wait until the pattern has been seen enough to be sure of its shape; codify the contract; promote through tested to active; deprecate when wrong. The catalog is curated, not accumulated.

What it has not established:

- The mechanics of skill composition, cross-project skill catalogs, and the full bridge between instructional and operational skills — sketched in the v0.1 spec, open for the v0.2 work.
- A cure for premature abstraction. The catalog is curated by patience, and the waiting cannot be automated; a skill written before its pattern has been seen enough will fit the first case awkwardly and the second case worse.

What is firm: a skill is a typed graph citizen. The runtime that does not know this is not Refine. The team that does not author skills as it matures is leaving most of the paradigm's value on the table.

*Further, in the reference corpus: `REFINE_SKILLS_v0_2`, `REFINE_INSTRUCTIONAL_SKILLS_v0_2`.*

The next three chapters complete the agent-side architecture by treating three concepts the agent-framework industry has used to mean things Refine specifically does not. Memory, in the rest of the industry, is a private buffer the agent owns; in Refine it is a queryable view on the project graph the team owns. Team, in the rest of the industry, is a coordination layer above agents; in Refine it is the multi-authority state of the graph itself. Pi-agents, almost nowhere outside Refine, are first-class — the deterministic counterpart to llm-agents, half of the two-kinds architecture that makes regulated agentic work possible — and the chapter that treats them carries the rest of the story with it: the people the paradigm is for, and the governed sandbox for when an agent writes code itself. Each chapter follows the pattern that Loops and Skills established: name what is being claimed, defend the architectural position against the industry's alternative, leave the gaps honest.

---

# Part III — The collisions

*Chapters 13–15 · The words that fight back.* The agent industry uses the same words this book needs — memory, team, agent — and means nearly the opposite by each. These chapters take the collisions head-on: memory as a graph view the team owns, not a private buffer; the team as graph structure, not a coordination layer; and the two kinds of agent — together with the people the whole thing is for, and the governed sandbox for the moment an agent writes code itself.

---

# Chapter 13 — Memory as a graph view, not a private buffer

*Memory the team owns and can inspect, not a private buffer the agent hides: a queryable view of the graph.*

A team running an agent through a serious project quickly accumulates a question it cannot ignore: *what does this agent know?* The agent is acting; the actions have consequences; the team is responsible. Knowing what the agent knew at the moment of action is not optional. The question is whether the answer is available, and how easily.

## §1 — The industry's answer: a private buffer

The mainstream agent frameworks of 2026 answer the question the same way: the agent has a *memory*, the memory is a *private buffer* the agent owns, and the team can inspect the buffer through tooling the framework provides. Anthropic's memory feature writes to a memory file the model reads at session start and edits during the session. Mem0 maintains a vector store of "user memories" the agent queries on demand. OpenAI's persistent memory is a profile attached to the user, opaque to the work the assistant performs. LangChain's memory abstractions cache conversation turns and entity facts in stores parallel to the conversation. CrewAI agents carry short-term, long-term, and entity memory as separate stores keyed to the agent.

The architecture is intuitive: each agent has a place to remember things; the place is separate from the work; the team inspects the place when curious. It is also wrong for governable software work, for three reasons that compound.

First, the buffer is *opaque*. The agent's memory is the agent's private state. Reading it requires going to the agent's storage and decoding what is there. The encoding is usually optimized for the agent, not the human reader. The decoded content is generally a list of "facts the agent has stored" — but facts in what form, from what source, with what attribution? In most implementations, the buffer's contents are entries with timestamps and provenance hints, accumulating over weeks and months. An auditor asking *what did this agent know about credit_floor on Tuesday* has to query the memory store, filter by date, parse the entries, and reconstruct the agent's likely state. The exercise depends on the agent's cooperation and on instrumentation many frameworks do not provide.

Second, the buffer is *unattributed*. A memory entry that the agent recorded six weeks ago because someone said something in conversation, an entry that the agent inferred from a tool result, an entry that the agent received from a human's direct instruction — these blur together in the buffer. The provenance, if it was recorded, is metadata on each entry; the metadata is rarely uniform; the team's confidence in any particular fact's origin is the team's trust in the memory store's metadata fidelity. For regulated work — work that must be defensible to an external auditor — *trust in metadata fidelity* is a thin foundation.

Third, the buffer is *unsynchronized with the work product*. The agent's memory says credit_floor is 12 months because that was true when the entry was made. The team changed credit_floor to 18 months last week as part of a regulatory tightening. The agent's memory is now stale. The agent does not know it is stale. When the agent acts on the remembered fact, the cascade collides with reality at commit time, the gate refuses the proposal, and the team has to debug a memory-drift incident. The industry-standard remedy is periodic memory refresh — the agent reads recent updates and rewrites stale entries — but this is a workaround for a problem the architecture creates. The right answer is to not have a memory store separate from the graph at all.

## §2 — Memory as a view on the governed graph

Refine's answer is structural. Memory in Refine is *not* a private buffer. Memory is a queryable view on the project graph the team owns. The things an agent remembers are graph nodes and edges the agent is currently pinned to, currently aware of, or currently traversing. Nothing the agent remembers lives in a place separate from the work; nothing the agent acts on is unattributable; nothing the agent thinks is true can be stale relative to the graph, because the graph *is* the source of truth and the agent's memory *is* a view on the graph.

The view has four observable components, all of which are graph properties the runtime maintains. *Pinned for current session* — the nodes the session has explicitly anchored, visible to all team members, visible to all agents, attributed to the human or agent who pinned them. *Recently touched* — a short, time-decayed list computed from the audit chain, of nodes the agent has read or modified in recent turns. *Open intent edges* — refinements proposed but not landed, satisfies-edges flagged stale, cascades pending arbitration; the agent's awareness of what is in flight is also memory in the operational sense. *Stale-flagged edges* — edges that were fresh when created but have been invalidated by a subsequent refinement, with the staleness as a graph property the agent reads when it queries the edge.

Every element is a graph entity. Every element is inspectable. Every element is attributable. Every element is fresh, or, when stale, flagged as such by the cascade arbitration. The auditor asking *what did this agent know on Tuesday* queries the audit chain for the agent's memory state at that point in time; the answer is a graph view, not an opaque buffer. The agent referencing a fact at commit time references the same graph view; the gate refuses the action if the reference is wrong, before any commit is attempted.

At Sonibank this is not hypothetical; the credit_floor example above is the pilot's own shape. A BCEAO tightening moves the floor from twelve months to eighteen; the team lands it as a refinement on a Tuesday; the following week a supervisor asks what the lending agent knew when it proposed Wednesday's batch of eligibility changes. The answer is a query, not an investigation: the agent's view at that timestamp — pinned nodes, recently-touched, open intent, stale flags — reconstructed from the audit chain, with the stale credit_floor edge visible if the agent read it before the cascade re-affirmed the view. Amina does not interrogate the agent. She reads the graph the agent read.

## §3 — The inversion, and what it buys

This is a structural inversion. The industry treats the agent's memory as something the agent owns and the team observes. Refine treats the agent's memory as a *view* the team owns and the agent reads. The agent does not store; the agent queries. The team does not inspect a foreign object; the team manages its own graph and the agent's view follows. Shaping the agent's memory — adding a pin, removing a pin, narrowing or extending its scope, re-affirming a stale edge — is the team acting on its own graph through typed, governed operations. There is no separate memory-management tool because there is no separate memory store.

The architectural commitment buys something specific: *structural hallucination becomes impossible at the source*. An agent in a private-buffer system can confidently cite a function that does not exist, a requirement number that was never created, a policy value that was never set — the agent's memory is its own; the agent's reference to its memory is what it sees; the work product is checked at the time of action. An agent in Refine cannot cite a function that does not exist in the graph, because *the graph is the memory*. The reference goes through the graph view; the graph view contains only what the graph actually contains; the reference fails before the action proceeds.

The collision with Anthropic Memory and the others is the same shape as the Skills collision: the industry uses a familiar word to mean a private structure the agent owns; Refine uses the same word to mean a typed graph property the team owns. We disambiguate explicitly. *Memory* in Refine documents means Refine's view; the other concepts get their provider qualifier (*Anthropic Memory*, *Mem0 store*, *LangChain memory*, *CrewAI memory*). Projects mixing the two — most projects that adopt Refine alongside existing tooling — can register the external memory store as an external resource (under `.refine/external-memory/anthropic/`, for example) and treat its contents as retrieved documents in the context.assembly record, not as part of the agent's standing memory. For new projects the cleaner discipline is to not compose; the Refine model supplies what the team needs.

What is firm: memory in Refine is the graph seen from the agent's current position. The runtime that treats memory as a private buffer is not Refine. The team that adopts a private-buffer model alongside Refine is carrying two incompatible architectures simultaneously, and one of them will lose.

## §4 — What this chapter has established — and what it has not

What the chapter has established:

- Memory is a queryable view on the graph the team owns — pinned, recently-touched, open intent, stale-flagged — not a private buffer the agent owns.
- The inversion is structural: the agent does not store, it queries; shaping the agent's memory is the team acting on its own graph through typed, governed operations.
- Structural hallucination dies at the source: an agent cannot cite what the graph does not contain, because the graph is the memory.

What it has not established:

- Cross-session pinning, a typed memory query language, memory analytics, memory-shaping skills, and the bridge to external memory stores — open questions, sketched in the specification.
- That composing with private-buffer frameworks is advisable. It is possible — register the external store and treat its contents as retrieved documents — but two memory architectures in one project means one of them loses.

*Further, in the reference corpus: `REFINE_MEMORY_v0_1`.*

The next chapter applies the same inversion to a second word the industry uses for a structure the agent system owns: the team.

# Chapter 14 — Team as graph structure, not coordination layer

*Coordination without a coordination layer: the team as edges on the same graph everyone refines.*

A project under refinement-oriented programming has multiple authorities acting on the same graph. Some are human; some are llm-agents; some are pi-agents. They act concurrently, propose refinements, review each other's work, hand off when one cannot commit and another can. The architecture must answer: *what is the team, and where does it live?*

## §1 — The industry's answer: a coordination layer

The mainstream agent-framework answer in 2026 is that the team is a *coordination structure* layered above the agents. AutoGen's `Team` class composes agents with a manager that orchestrates turn-taking. CrewAI's `Crew` defines a roster of role-playing agents and a process that sequences their work. MetaGPT models a team as a hierarchy of roles (PM, architect, engineer) with handoff rules between them. OpenAI Swarm orchestrates agent handoffs as conversation transfers. LangGraph multi-agent uses graph nodes to model agents and edges to model handoff routing.

The common architecture: the team is a *control structure* layered above the agents. The agents are independent reasoners; the team's existence comes from the rules about how they pass work to each other. Without the team layer, the agents would be unrelated. The team is the composition; it does not exist in the work product itself, only in the coordination logic.

This works for orchestrating conversations. It fails for governable work product, again for three reasons.

The team has no presence in the work product. When an AutoGen Team or a CrewAI Crew produces an output, the output is files or data. The team itself is not in the output; the team was the producer, not part of the produced. An auditor reading the output sees the final artifact and (if instrumented) a conversation log; the team's role structure has to be reconstructed from the orchestration code, not from the artifact. The team is a fact about *how the work was made*, not a fact about *the work*.

The team's handoffs are ephemeral. A handoff in these frameworks is a conversational event: agent A finishes its turn, agent B begins its turn, the framework's manager routes the work. The handoff is logged as a chat-style transition, but the typed semantics of the transfer — who is accountable now, what review queue does this enter, what reversal path does it take if it fails — are not first-class. Reversal in particular is awkward: a CrewAI crew that needs to undo a handoff has to inspect the conversation log and re-issue work. There is no typed record to reverse.

The team coexists awkwardly with humans. Most multi-agent frameworks treat humans as a special case: a "HumanInputAgent" or a "user proxy" that participates in the agent conversation. The human is one more agent in the loop, conforming to the framework's coordination protocol. For a regulated software project where humans are the authority holders, this is the wrong direction. Humans should not have to behave like an agent to be in the loop; the team's structure should make the human's position first-class without retrofitting the agent's protocol.

## §2 — The team as graph structure

Refine's answer is structural again. A team is not a coordination layer above the agents. A team is *the multi-authority state of the project graph*. The team exists in the work product because the work product is a graph and the team is what the graph's edges and nodes attribute to. Every refinement has an author. Every refinement points to a session. Every session is owned by an authority. Every module has an `owns` edge to a person. Every gated refinement has a `reviews` edge to a reviewer. Every comment is a typed node with an open-or-resolved lifecycle. The team is not orchestration logic; the team is graph structure.

Four typed primitives compose the team's structure. *owns(module → person)* declares responsibility — the owner is informed about consequential refinements, not required. *reviews(refinement → person)* assigns review — the refinement is held in the reviewer's queue, adjudicated with a typed action (approved, revised, rejected). *handoff(refinement → person)* declares an explicit transfer of accountability — the originator's work preserved, the receiver named, the time-of-transfer audited. *comment(node)* attaches a typed discussion to any graph node with open/resolved lifecycle, refusing to silently disappear when a refinement lands under an unresolved thread.

That is the full vocabulary. The runtime needs no more to handle multi-authority work, including multi-agent work, including the supervisor-fleet pattern that delivers most of the agentic-era productivity gain. The pattern itself — one human supervisor commanding five to ten agent-driven sessions — is constructible from the primitives: the supervisor *owns* the modules; the agents propose; the gate creates *reviews* edges to the supervisor's queue; refinements exceeding agent commit authority arrive via *handoff*; discussions happen as *comments*.

Sonibank runs the multi-supervisor version of this. Mansour supervises the lending fleet; Salif the compliance fleet; Koffi the customer-facing fleet. Each supervisor's queue is filtered by the scopes they own, and a lending refinement whose cascade reaches a compliance construct appears in both queues — not because a coordination tool routed it, but because the cascade traversal crossed the scope boundary. The coordination is not a meeting; it is an edge.

## §3 — One protocol, async by principle

The cascade-overlap arbitration that handles two agents handles two humans the same way. The architecture does not have separate protocols for human-human conflict and human-agent conflict; it has one protocol — cascade arbitration on commit. The first refinement to reach commit lands; the second is rejected with a clear base to revise from; neither is silently merged; neither produces "merge conflict markers" in a working file. This works whether the parties are two agents, two humans, or one of each.

The architectural choice carries a commitment Refine makes deliberately: *async-by-principle*. There is no live cursor showing one team member where another is editing in real time. There is no chat-channel-of-record where decisions are made in synchronous discussion. There is no screen-share mode where one team member watches another work. These are not omissions; they are commitments. The reason is that synchronous collaboration produces decisions whose audit trail is the meeting transcript or the chat log — outside the graph, hard to retrieve, hard to verify. Async collaboration on the graph produces decisions whose audit trail is the refinement chain — inside the work, easy to retrieve, easy to verify. Real-time clarification (a quick question, a "did you see this") happens on whatever real-time channel the team prefers; the discipline is that decisions land as refinements with rationale captured as commit message or comment.

The collision with AutoGen, CrewAI, MetaGPT, OpenAI Swarm, and LangGraph is real and worth naming once. The industry uses *team* to mean a coordination structure layered above agents; Refine uses *team* to mean the multi-authority state of the graph. The pattern is the same as Skills and Memory: industry meaning is *control structure or private state owned by the agent system*; Refine meaning is *graph property owned by the team*. We disambiguate explicitly — *team* in Refine documents means Refine's concept; *AutoGen Team*, *CrewAI Crew*, *MetaGPT Team*, *OpenAI Swarm* get their qualifier — and we offer the composition pattern for projects that want to keep their existing multi-agent framework while adopting Refine for governance: register the AutoGen Team or CrewAI Crew as a *composite agent* in Refine, with a single identity node, the framework's internal coordination opaque from Refine's perspective, but the framework's outputs (the refinements it proposes) attributed to the composite agent. The framework is the agent's brain; Refine is the agent's runtime.

What is firm: a team in Refine is graph structure. The architecture is the same for two humans as for two agents as for a human and an agent. The cascade arbitration handles all three pairs the same way. The team's existence is structural; its primitives are typed; its actions are auditable. The runtime that treats the team as a control structure layered above the agents is not Refine.

## §4 — What this chapter has established — and what it has not

What the chapter has established:

- The team is the multi-authority state of the graph, not a coordination layer above the agents; four typed primitives — owns, reviews, handoff, comment — are the full vocabulary.
- One arbitration protocol serves human–human, human–agent, and agent–agent conflict alike; the supervisor-fleet pattern is constructible from the primitives.
- Async-by-principle is a commitment, not an omission: decisions land as refinements, so the audit trail lives inside the work.

What it has not established:

- Role hierarchies, cross-project team membership, time-bound authority grants, and team analytics — open questions, sketched in the specification.
- That existing multi-agent frameworks must be abandoned. They compose as composite agents — the framework the agent's brain, Refine the agent's runtime — at the cost of their internal coordination staying opaque to the chain.

*Further, in the reference corpus: `REFINE_TEAM_v0_1`.*

The next chapter turns from the structures the team owns to the workers inside them — and to a distinction between two kinds of agent that regulated agentic work cannot do without.

# Chapter 15 — Agents, and the rest of us

*Who acts on the graph — the reasoning llm-agent, the deterministic pi-agent, the humans it is all for — and the governed sandbox when an agent writes code itself.*

Most of what has been said in this book so far has used the word *agent* without distinguishing kinds. The text has named *llm-agent* and *pi-agent* in passing but the architectural commitment behind the distinction has not been argued in its own right. This chapter is that argument.

Refine commits to two structurally distinct kinds of agent, neither of which is reducible to the other.

## §1 — Two kinds, not two species

The *llm-agent* is what most of the agentic-era discourse means by "agent": a model-driven entity, fluent over language, capable of open-ended reasoning, non-deterministic in its outputs, externally hosted by a foundation lab. The agent's behavior is the model's behavior; the runtime calls the model and accepts what comes back. *claude-sonnet-4.5*, *gpt-5*, *gemini-2.5* are llm-agents. The locus of behavior is a foundation model the runtime queries; the runtime cannot inspect the model's internals; the runtime cannot guarantee reproducibility of the model's outputs.

The *pi-agent* is the structural counterpart, less discussed publicly because the agent-framework discourse focuses overwhelmingly on llm-agents. A pi-agent is deterministic, computationally independent, internally hosted. The agent's behavior is code in StzEngine that the runtime executes directly; the runtime fully inspects the agent's logic; the runtime guarantees byte-identical reproducibility of the agent's outputs given the same inputs. *pi-router*, *pi-classifier*, *pi-migrator*, *pi-injection-scan*, *pi-context-curator*, *pi-economy-watch*, *pi-safety*, *pi-snapshot*, *pi-refactor* are pi-agents. The locus of behavior is code the team can read; the runtime is the executor; the test suite is the agent's contract.

These are not two species of a single concept. They are two distinct kinds, with different anatomies, different lifecycles, and different roles in the runtime's operation. The architectural commitment of Refine is that *real agentic work requires both*. A project trying to do everything with llm-agents will find that critical operational concerns — routing decisions that must be auditable, safety checks that must always fire, classification decisions that must be reproducible for regulatory inspection — become unreliable because they depend on a non-deterministic, externally-hosted, opaque-reasoning step. A project trying to do everything with pi-agents will find that it cannot handle natural language, ambiguous human intent, or open-ended synthesis. The two kinds complement each other; the architecture makes both first-class.

## §2 — The determinism discipline

The defining property of a pi-agent is *computational independence*. The agent's behavior is fully determined by its code and its inputs. It does not call an external model. It does not query a remote API for its decisions (it may call tools that have remote dependencies, but the pi-agent's own decision logic is local). Given the same inputs and the same state of the graph, a pi-agent produces the same output, byte-identical, on every run. The agent's reasoning is auditable to the line of code, reproducible without re-invoking external services, and verifiable by test.

These properties are why pi-agents handle the parts of agentic work that cannot tolerate non-determinism. *pi-router* decides which provider gets the next llm-agent call; the decision must be defensible to auditors who ask why this provider was chosen for this work, and the answer cannot be "the model decided to" because the routing decision is what *creates* the model invocation. *pi-safety* enforces declared guardrails on every agent action; the safety check must fire deterministically every time the action's preconditions are met, with no possibility of the check being skipped on a turn where the model "felt" the action was safe. *pi-classifier* assigns task kinds to incoming requests; the classification must be reproducible for regulatory inspection, including months later when the original conversation has been replayed for audit.

The lifecycle of a pi-agent reflects the rigor. A pi-agent is declared in a typed file (`.pi-agent` under `.refine/pi-agents/`); the file specifies the agent's identity, capabilities, policy invariants (`must` constraints), forbidden operations (`never` constraints), implementation pointer, and test suite. The pi-agent moves through five states: drafted (declared but not tested), tested (passes its own tests and the runtime's determinism verification suite), registered (operating in the project), versioned (superseded by a newer version), deprecated (scheduled for removal). Each transition is a refinement on the pi-agent's identity node, attributable to the methodologist who approved it.

The determinism verification suite deserves its own mention. The runtime ships a suite that exercises every registered pi-agent across repeated invocations (output is byte-identical), concurrent invocations from multiple sessions (no race conditions; outputs are independent of invocation order), replay invocations from old audit-chain records (the agent produces the same output it produced originally, even if invoked months later), and adversarial inputs (the agent does not behave erratically when given unexpected input). The suite runs nightly; a pi-agent that begins failing its checks is demoted from active to tested status with a notification. This is what allows pi-agents to participate in regulated work: a test that passed in development passes the same way in production, because the agent has no way to drift between the two.

## §3 — Script, skill, loop, agent — and why the pi-agent never delegates

Distinguishing the pi-agent from adjacent constructs takes care. A pi-agent looks superficially similar to a script (both are local executable code), to a skill (both can be invoked by name), to a loop (both can produce sequences of refinements). The distinctions matter because the right discipline depends on the right naming.

A *script* is the lowest level: a Ring file under `.refine/scripts/` containing executable logic, no first-class identity, no declared policy, no capability set. Used for small utility operations the team writes once and forgets.

A *skill* is a named, typed, parameterized, authority-bound operation an agent invokes by name with a contract. A skill has a signature, pre/post conditions, an implementation pointer (often to a loop or refinement template), and authority bindings. Used when the operation is called by name with parameters and significant enough to deserve versioning.

A *loop* is a staged pipeline that produces refinements through stages with verification gates. Used when the operation has multiple stages worth running with retry/verification logic.

A *pi-agent* is a first-class agent identity with deterministic body, declared capabilities, ongoing operation in the runtime, and graph-citizen authority. Used when the operation needs to act as an authority — to propose refinements under its own identity, to enforce policies across the project, to be referenced as a participant by other agents.

A pi-agent may invoke a loop (the agent's body invokes the loop). A skill may be implemented by a script (the skill's impl points to the script). A pi-agent's body may be a script-sized piece of code, but the pi-agent has identity, capabilities, and policy bindings that the script does not. The discipline of *what to write* depends on the role the work plays — incidental utility (script), invocable operation (skill), staged pipeline (loop), continuous authority (pi-agent).

The pi-agent does not delegate. The authority block on a pi-agent declaration is always `grants_to: never`. The reason is structural: pi-agents are computationally independent and behaviorally bounded; delegation would require the pi-agent to reason about another agent's capabilities, which would require modeling the other agent, which would be a step toward general reasoning, which is the territory of llm-agents. The architectural commitment is: pi-agents act within their bounds; llm-agents reason about the broader picture; the two cooperate via the gate, not via direct delegation.

The cooperation pattern is what makes the architecture practical. Consider the canonical flow at Sonibank when Aïcha asks an llm-agent to tighten the credit floor under the BCEAO's Q3 directive. *pi-classifier* reads the request and classifies it. *pi-router* chooses an llm-agent. *pi-context-curator* assembles the context. The llm-agent reads the context and proposes a refinement. *pi-safety* checks the proposal against safety policies. The proposal lands in a supervisor's queue. *pi-snapshot* records state at commit; *pi-economy-watch* records cost. Every step has an identity. The deterministic steps are pi-agents; the synthesizing step is an llm-agent; the human step is the supervisor. The audit chain references each participant by name — at Sonibank that entry reads, in order: pi-classifier, pi-router, pi-context-curator, the llm-agent's proposal, pi-safety's check, Amina's approval; six named participants for one governed change. Both kinds of agent are necessary — neither is sufficient.

> **Figure 15.1 — Two kinds of agent, one gate.** The deterministic pi-agents classify, route, curate, and check; the llm-agent synthesizes the proposal; the human supervises — and every participant meets the same gate, under its own name.

What is firm: pi-agents are first-class. They are not "deterministic LLMs" or "advanced scripts" or "embedded automation." They are a distinct kind of agent, with their own identity, their own discipline, their own role in the architecture. The runtime that does not treat them as first-class is not Refine.

The two kinds together are what makes regulated agentic work possible. The architectural cost of admitting both — two kinds of agent, two anatomies, two lifecycles, two test disciplines — is real but is paid back many times over by the reliability gain. The llm-agent does what only llm-agents can do (open-ended reasoning, fluent natural language, novel synthesis). The pi-agent does what only pi-agents can do (deterministic decisions, reproducible classifications, locally-executable guardrails). The team designs which kind handles which concern; the runtime composes both into the project's coherent operation.

So much for the machinery. The other half of this chapter is the people it is all for — and a strategic claim about who gets to participate in the agentic age at all.

## §4 — The rest of us

There is a paradox at the center of the agentic age, and nobody in the tooling industry has resolved it. The *interface* to software work has never been more accessible: natural language. A compliance officer who has never written a line of code can describe, in her own words, exactly what a system should do — and an agent can do it. The great equalizer arrived. And yet the *tooling* around that interface is the most expert-hostile the industry has produced in decades: terminal-first, configuration-heavy, jargon-dense. To use agents seriously you are expected to know what a context window is, what MCP means, why your agent hallucinated, and how to wire markdown files so the right guidance loads at the right moment. The interface says *everyone is welcome*; the tooling says *experts only*.

This has been resolved before, in a different age, and the precedents are instructive. The RAD tradition — WinDev above all, Delphi and Visual Basic alongside — made business application development accessible to people the mainstream industry had written off, and the method was never dumbing down: it was wizards that wrote real code you could open, visual editors over real structures, an environment that assumed you wanted to ship something this week. The spreadsheet made computational modeling a tool for accountants and remains the most successful end-user programming environment ever shipped. HyperCard made interactive software a medium for teachers. And the constructionist tradition — Papert, then Scratch — named the principle all of these share: *low floor, high ceiling*, and crucially the same floor and ceiling in the same building. Programming for the rest of us. Refine takes up that lineage for the agentic age — and with a specific geography in mind, because the people who most need agentic capability in Refine's home context are exactly the people the current tooling excludes: the compliance officer in Niamey who knows BCEAO directives better than any programmer ever will, the operations manager who understands the loan workflow end to end.

The structural insight that makes this more than aspiration is that **Refine does not need to build a learning environment, because the governance runtime already is one.** Every learning tool in the lineage had to construct its safety as extra machinery — Scratch made invalid programs unrepresentable, the spreadsheet made undo cheap, HyperCard sandboxed the stack — always a separate apparatus, distinct from how professionals worked. Refine's safety is the production machinery itself. Every change is previewed before it lands: the cascade shows the full ripple of consequences first. Every change is reversible: nothing is ever lost. Every change is gated: the system stops you before a serious mistake and tells you why. Every change is attributed: you can always retrace what you did. Read as governance, these properties protect the bank. Read as pedagogy, they are precisely the guarantees a beginner needs to explore without fear — and they are not a sandbox. The training wheels are load-bearing. The learner's first week and the bank's production Tuesday run on the same gates, and nobody ever graduates across a cliff into "the real thing," because they were in the real thing from minute one.

## §5 — The dial, the artifact, and the glass

On this foundation, three design commitments. The **experience dial**: every surface renders at one of three presentation altitudes — Guided, with plain language everywhere, a standing safety promise, and an assistant that explains any screen on request; Standard, the working instrument; Expert, density-first, explanations collapsed, raw views a keystroke away — selected by the person, changeable at any moment, and governed by one inviolable rule: *the level changes presentation, never capability or authority.* Simplicity is not a permissions tier. A guided beginner with commit authority commits; an expert without it is refused at the gate. The **same-artifact principle**: everything a guided user produces is the canonical artifact — the form, the CLI command, and the raw edit make the same typed node, so there is no beginner format, no export cliff, no stranded learners at a representation boundary. And **glass wizards**: a Refine wizard shows, live and ignorable, the artifact it is assembling and the command that would do the same thing — the floor teaches the ceiling, so the person who works through forms for six months has been passively reading the expert's language the whole time. In most tools the wizard is a wall in front of the lower level. In Refine it is a window onto it.

Two guarantees close the design, one for each end of the dial. For the newcomer: *never disoriented, never blocked.* Every screen answers what it is and what you can do here; every error, refusal, and empty state follows a four-part grammar — what happened, why, what to do next, where to learn more — so that even failure is curriculum: a person refused at the gate three times, each time legibly, has learned the authority model from the system behaving well. For the expert: *nothing is hidden.* Raw views are first-class, the CLI has full parity, every guided surface exposes the artifact and the command beneath it, and the explanatory chrome strips away on demand. The didactic design can afford total transparency precisely because the governance holds at every altitude; the low level in Refine is not a hazardous basement but the same typed, gated, reversible graph, seen closer up. Simplicity by design and power by design turn out to be the same design.

The flagship test of all of this is a person, not a benchmark. Aïcha, compliance officer, fifteen years of BCEAO directives, zero code: today her expertise enters software through tickets and meetings and developer interpretation, lossy at every hop. In Refine at Guided altitude she reads the domain in her own professional vocabulary, authors a requirement by being interviewed — one question at a time, with recommended answers — reads a cascade preview in plain language, and commits a policy refinement under her own authority, gated exactly as the governance demands. She is not a user of outputs. She is an authority on the graph. When she is real and working — not as a persona in a specification but as a pilot user in Niamey — the claim of this chapter will be evidence. Until then it is design intent, stated plainly, with the machinery shipped to make it testable.

From the people, back to the machinery one last time — because there is a hole in the architecture nothing earlier in this book has quite filled, and the broader agent-development industry has been independently discovering what should fill it.

## §6 — When agents write code

For most of this book the work an agent does has had one shape: the agent reasons, the agent proposes a refinement, the gate validates the proposal, the refinement either lands or is refused. This shape covers an enormous range of useful work — most of what an llm-agent does on a typical project — and a deliberate architectural commitment runs through it: agent action is *typed*, the refinement is the unit of change, and the gate is the only path to the graph. The book has not deviated from that commitment, and it does not deviate from it here.

But the shape leaves a gap, and the gap has become more visible as the rest of the industry has converged on a pattern named for it. The pattern's most-cited name is *codemode*, after a Cloudflare post in early 2026 that argued it in plain terms: an LLM that needs to compose several operations against external resources — *read these records, group them by region, filter, transform, summarize* — is dramatically more efficient writing a small program that does the composition than making one tool call per step. Anthropic ships the same pattern as Programmatic Tool Calling; Hugging Face's smolagents lands on it independently; Pydantic's Monty exists explicitly to power it. The argument is empirical: one model round-trip producing a script that does ten things outperforms ten round-trips producing one tool call each, on latency, on cost, on reliability. The model gets the compositional vocabulary of a real programming language — variables, loops, conditionals — instead of being limited to whatever the tool-call schema allows. The pattern only works if the code can run *safely*, which is what Monty and its peers provide.

The hole the pattern reveals in earlier chapters is straightforward: a Refine llm-agent that needs to compose operations on the graph cannot do so in one motion today. The book has names for one-shot composition (a refinement), for fixed-stage composition (a loop), for continuous deterministic composition (a pi-agent), but no name for *ad-hoc compositional execution at invocation time*. Without one, an llm-led skill that needs to read ten audit-chain entries, group them, filter them, and propose a single summary refinement must either be a fixed loop with rigid stages (works when the shape is predictable; fails when it isn't) or a series of sequential tool calls back through the gate (the round-trip tax the codemode pattern was named to avoid). The codemode-shaped option — *let the llm-agent write a small program that composes the operations as ordinary function calls in a real language, and execute it under bounds* — has been implicit in the architecture without being said.

It is said now. The execution surface is `stzSandbox`, a new sibling of the `stzPolyCode` and `stzExtCode` modules already in StzEngine. The polyglot foundation is already there — Refine has run Python and JavaScript and other languages from the beginning, because the projects Refine serves run code in many languages; what was missing was a *governed* mode of that foundation for code an LLM wrote at invocation time. The sandbox adds four properties to the existing polyglot execution: it runs in-process (microseconds, not the hundreds of milliseconds a container-based sandbox costs); it has no host access by default beyond the functions explicitly injected at the call site (filesystem, environment, network are structurally inaccessible because no reference exists); it pauses and snapshots its entire interpreter state at every call to an injected function, allowing resumption later, on a different machine, days afterward (and feeding the audit chain at every boundary); and it operates against a deliberately bounded subset of whichever language frontend it uses (no third-party libraries, no introspection escape hatches, a small audited standard-library slice). Each of the four exists for a reason and earns its weight; the references for the design lineage — Cloudflare Codemode, Anthropic Programmatic Tool Calling, smolagents, Pydantic Monty — are the convergent industry evidence that this is the right shape.

## §7 — The governed sandbox

The architectural fit with Refine's existing concepts is unusually clean, which is the test by which the spec confirms it belongs. Capability injection maps directly onto Refine's authority model: every agent declares `use:X` capabilities, and the sandbox's injected function set is exactly that declaration materialized as host functions — a pi-agent without `use:propose` cannot, even if its LLM-composed body tries to, produce a mutation, because `propose_refinement` was never passed in and the symbol does not exist. Capability becomes structural rather than enforced; there is no permission check to circumvent because there is no permission check. Snapshot-and-resume maps directly onto the audit chain: every external-call boundary writes a snapshot record, so the chain records not only that the agent took an action but the entire computational state at every step that led to it — a future auditor can step through the script, byte-identical, replay the LLM's reasoning made executable. Bounded subsets map onto declared-and-versioned graph artifacts: each frontend's allowed surface lives at `.refine/sandbox-frontends/<name>.zml`, versioned, attributable, reversible. In-process execution matches the rest of Refine's governance posture — cheap enough to run on every action.

Three Refine-specific commitments harden the design beyond the industry's baseline. *Mutations always route through the gate.* A sandboxed script can compose any number of reads, computations, and proposed mutations; every proposal enters the gate exactly as if a human had typed it. The script is the body of computation; the gate remains the only authorized writer. *Snapshots are first-class audit artifacts.* In Monty the snapshot mechanism is a feature; in Refine it is structural — every external-call boundary produces a snapshot record by default, accepting the audit-volume cost deliberately because Refine's whole project is to make agent action auditable in ways the industry doesn't. *Determinism is declared per frontend, not blanket-claimed.* The Python frontend's v1 declaration pins what's deterministic; constructs outside the pinned subset are either disallowed or flagged in the audit chain as non-deterministic boundaries. Honesty beats marketing.

What this unlocks is concrete. An llm-led skill body that genuinely needs to compose can be a single script the LLM writes once at invocation, executed in microseconds, producing one refinement (or several) with the full computational trace audited. The expert immediate-window promised in §5 — the `refine play` REPL where an expert composes graph primitives in a few lines and sees the result inline — has its execution surface. Pi-agents that wrap LLM-composed transforms can hybridize cleanly: the *what* is LLM-composed; the *that-it-stays-bounded* is pi-agent-enforced; the audit chain reads cleanly because the pi-agent took the action and the sandbox snapshots show the body it executed. Tutorial sandboxes can be read-only by construction — a learner's session injects only read capabilities; the sandbox structurally cannot mutate. Guided-level computational exploration becomes possible — a non-coder asks the data a question; the assistant translates to a sandbox script; the script runs; the answer comes back in plain language; the script itself is shown alongside (the glass-wizard principle from §5), so the floor teaches the ceiling without any code being hidden.

The Sonibank shape of this is the quarterly BCEAO summary. An llm-led skill must read the quarter's penalty-related refinements from the audit chain, group them by directive, filter the ones that touched regulated paths, and propose one summary refinement for compliance review. As sequential tool calls, that is dozens of round-trips through the gate; as a sandbox script it is one composition — the reads free within the session's granted capabilities, the single proposed mutation still entering the gate like anything else, and the whole computational trace snapshotted for the auditor who will one day ask how the summary was produced.

None of this requires inventing a new agent kind, a new refinement primitive, or a new scripting language. The sandbox is an execution *surface*, not a new construct in the refinement model; the languages it runs are the ones the polyglot foundation already supports; the agents that use it are the llm-agents and pi-agents already named. What was missing was the *governed mode* of code execution — the bridge between the LLM's compositional reach and the project's audit chain — and the bridge is now there.

## §8 — What this chapter has established — and what it has not

What the chapter has established:

- Agent means two kinds: the reasoning, non-deterministic llm-agent and the deterministic, computationally-independent pi-agent — and real agentic work requires both, cooperating through the gate, never by delegation.
- Pi-agents hold the roles that cannot tolerate non-determinism — routing, safety, classification — and a determinism suite verifies them for life, not just at development time.
- The governance runtime is the learning environment: previewed, reversible, gated, attributed — so the paradigm stays open to the non-expert without a sandbox-for-beginners and without a graduation cliff. The dial changes presentation, never capability or authority; the artifact is the same at every altitude; the wizards are glass.
- When an agent must compose, the sandbox is the governed mode of it: in-process, capability-injected, snapshotting, bounded — an un-granted function does not exist, mutations still route through the gate, and the snapshots are audit artifacts.

What it has not established:

- Pi-agent composition, the debugging story, determinism against external systems, and production update tooling — open questions. And the two-kinds distinction does not make llm-agents trustworthy; it bounds where their non-determinism is allowed to live.
- The simplicity claim itself, yet. Until Aïcha is real — a working pilot user in Niamey, not a persona in a specification — that part of this chapter is design intent stated plainly, with the machinery shipped to make it testable.
- Blanket determinism or measured economics for the sandbox: determinism is declared per frontend, one frontend ships at launch, and the latency and cost wins are the industry's numbers until the pilot measures its own.

*Further, in the reference corpus: `REFINE_PI_AGENTS_v0_2`, `REFINE_SIMPLICITY_BY_DESIGN_v0_1`, `REFINE_SANDBOX_v0_1`.*

The next chapter turns from the *mechanism* of agent-authored code to the *scope* of what refinement-oriented programming actually governs — not just code, as the earlier chapters' examples might have suggested, but two further artifact-kinds that this book has, until here, treated as backdrop and that deserve to be named as peers.

---

# Part IV — The horizon

*Chapters 16–17 · Where it opens out.* The paradigm is wider than code — UI and data are refinement domains with the same rights — and it has a serious rival reading of the same evidence: dissolve the artifact and trust the agent. This part names the three domains, then meets the strongest argument against this book head-on.

---

# Chapter 16 — Code, UI, and data: the three domains

*The paradigm is not just for code: UI and data as first-class refinement domains, with cascades that cross between them.*

The book's examples to this point have been almost entirely about code. A threshold lifted from twelve months to eighteen. A function's strategy swapped from greedy to deliberate. An invariant tightened so a new BCEAO directive can no longer be quietly violated. A loop's stages reshaped so a compositional task can settle into a deterministic body. Each example carries the same shape — a typed refinement, a cascade computed before commit, a gate that writes or refuses, an audit chain that remembers — and each example happens to live in the code domain. A careful reader could be forgiven, this late in the book, for concluding that refinement-oriented programming is a paradigm for code. It is not. It is a paradigm for the three artifact-kinds every non-trivial software project produces, of which code is one. The other two deserve to be named.

## §1 — The fragmentation we inherited

For most of software's short history, the three artifact-kinds have been treated as belonging to three different disciplines with three different tools, three different vocabularies, and three different authority structures. *Code* is what software engineers produce; it lives in IDEs and in version-controlled repositories; its discipline is computer science. *UI* is what designers produce; it lives in design tools and component libraries and design-system platforms; its discipline is human-computer interaction and visual design. *Data* is what data engineers and database administrators produce; it lives in database administration consoles and migration frameworks and lineage platforms; its discipline is data modeling and information architecture. The three disciplines have grown deep but largely separately. The tools for each presume the others as backdrop — the IDE's view of a database is "a connection string and some opaque tables," the design tool's view of code is "what eventually consumes my export," the database administrator's view of UI is "where someone might display the data I curate." Each discipline has internal sophistication and external thinness; each treats the others as someone else's problem.

Most projects fail at the seams. A schema change that breaks an upstream form. A design-variable rename that the analytics suite never updated. An API rename that one query in one report missed. The seams are where systems fail in production, in regulatory audits, in customer-facing crises. The disciplines have grown so separately that the tools have no shared cascade to cross. A code-refactoring tool computes the impact of a function rename within the code; it does not compute the impact on the UI components that bind to that function's output, or on the queries that feed it. A design system computes the impact of a design-variable rename within its components; it does not compute the impact on the code that consumes the variable by name or on the audit logs that record the variable-version stamp. A database migration tool computes the impact of a column type change within the schema; it does not compute the impact on the queries that read the column or on the UI forms that bind to it. Each tool stops at its discipline's boundary. Each project pays the cost in production.

## §2 — The three artifact-kinds, named

Every non-trivial software project produces three kinds of artifact, more or less continuously. *Code* is the executable logic — the functions, the control flow, the contracts, the invariants. *UI* is the visible surface the user touches — the design variables, the components, the layouts, the motion specifications, the microcopy, the accessibility attributes. *Data* is the persistent state the project reads, writes, transforms, and exposes — the schemas, the queries, the indexes, the constraints, the lineage edges, the retention rules, the masking policies. Most projects need all three. Many projects fail at the seams between them. The three are not optional and they are not derivative of one another; a project that exists only as code is a library, a project that exists only as UI is a prototype, a project that exists only as data is a database. A *project* in the sense this book has been describing all along is the composition of the three, refined continuously, by multiple authorities with overlapping concerns.

Refinement-oriented programming — stated carefully now, with the elevation this chapter is introducing — is a meta-paradigm whose core model governs all three domains. The refinement is the unit. The cascade revalidates. The gate writes. The audit chain remembers. The authorities authorize. The simplicity dial protects. The codemode bridge composes. These structural commitments do not care which domain the refinement targets — they operate identically whether the refinement is a code threshold, a design variable, or a column type. What varies is the *vocabulary*. A code refinement speaks in function bodies and invariants and dependencies; a UI refinement speaks in variables and components and motion curves; a data refinement speaks in schemas and queries and lineage. The meta-paradigm is one wheel; each domain expresses the same wheel in the right language for its operators.

## §3 — One paradigm in three domain languages

Stated this way, the elevation reads almost banal: of course a paradigm that claims to govern *change* should apply to every kind of artifact a project changes. The reason it has not, in the broader industry, is partly historical — the disciplines grew separately — and partly architectural: the tools that promise to govern *some kind of change* were built within a single discipline's view of the world, and their architectures don't reach beyond it. To make one paradigm reach all three domains requires that the core machinery be domain-agnostic in a particular way — the typed graph holds nodes of all three kinds; the cascade follows edges across the kinds; the gate validates without caring which kind; the audit chain attributes without caring which kind. This is what Refine's architecture has been, structurally, from early on; it has simply been *named* as governing code. The naming is what changes here. The architecture was always domain-agnostic; the examples were code-heavy because the author's background and the pilot context were code-heavy. The architecture's reach is wider than the examples have shown.

Three concrete consequences flow from naming the meta-paradigm this way. The first is *the cascade crosses domain boundaries*. A code refinement that changes a function's output type cascades into the UI domain when the function feeds a component, into the data domain when the function writes to a table. A UI refinement that changes a design variable cascades into the code domain when the variable name appears in the component implementation, into the data domain when the variable-version is stamped in audit logs. A data refinement that changes a column type cascades into the code domain when the column is consumed by queries, into the UI domain when the column is bound to a form. The cascade is one graph; the edges are typed; the domains are sectors within the graph, not separate graphs. This is the structural difference no neighbor tool offers, and it is the difference that matters most for projects that fail at the seams.

> **Figure 16.1 — One graph, three domains.** A change in any domain — a code threshold, a design variable, a column type — cascades along typed edges into the other two. The seams where projects fail in production become visible edges in one graph.

The second consequence is *projects can launch in any of the three domains*. A designer who opens Refine to start a UI-first project finds the UI domain active, design variables and components as the first refinement targets, code and data as *pending domains* in the project graph — placeholders that name what will exist when authorities for code and data engage, holding no refinements until then. A data modeler who opens Refine to start a data-first project finds the data domain active, schemas and queries and lineage as the first refinement targets, code and UI pending. A developer who opens Refine to start a code-first project follows the path the existing corpus has described in detail. None of the three orderings is privileged; each is a legitimate entry point; Refine adapts the experience to which domain leads. This commitment costs something in product engineering — three substantial entry experiences, three sets of authoring surfaces, three skill catalogs to populate — and it earns something larger: *Refine is the programming environment for the people who do programming, not for one particular kind of programmer*.

The third consequence is *the audience expands to include designers and data modelers as first-class users*. The compliance officer in Niamey — Aïcha, who has been the persona-figure for the simplicity pillar since Chapter 15 — was already an example of a non-programmer authority with the same architectural standing as a programmer. Chapter 15's argument was correct as far as it went; what it understated was the *generality* of the move. Aïcha is not an exception to the programmer-as-user assumption; she is the first non-programmer named example in a series that now properly includes designers and data modelers and brand stewards and accessibility specialists and privacy officers. Each of these holds authority on something the project produces; each is a first-class Refine user; each operates with the same authority model, the same skill catalog (filtered to their domain), the same simplicity-dial protections, the same audit-chain presence. *Authority on the graph*, the rest-of-us section said, *not user of outputs*. The elevation in this chapter is the recognition that the move generalizes to every non-programmer authority a project may need.

## §4 — What this looks like in practice

A designer working on the Sonibank lending portal in Refine opens the IDE and the UI facet is active by default. The first refinements she authors are design variables — a primary action color, a baseline spacing scale, a type system tuned for the long-form regulatory language a banking interface must carry. Each refinement enters the gate, cascades within the UI domain to the components and pages that will eventually use the variables, and lands attributed. As her work progresses, she adds component variants — a primary button, a secondary button, a destructive button for the rare but consequential actions of regulated banking. The cascade now reaches further: a component refinement cascades to layouts, to motion specifications, to copy conventions. Some refinements carry cross-domain edges from the start — a component that will eventually bind to a regulated field carries an edge into the data domain, even if the data domain is still empty. The edge is a placeholder for the eventual data binding; when a data modeler joins and refines the schema, the edge's other end populates and the cascade becomes bidirectional.

A data modeler working on the same project may join later, or may have been the founding authority on a data-first variant of the project. In the data-first launch he opens Refine and the data domain is active. The first refinements are schema declarations — the obligor table, the credit-floor configuration, the BCEAO directive table with its versioning convention. Each refinement enters the gate, cascades within the data domain to the queries that will eventually read or write the column, to the views that will aggregate the data, to the lineage graph that records the flow. The cascade tells him, before he commits a column-type change, which queries will need updating and which downstream reports will need re-running. Cross-domain edges populate as code and UI authorities engage; eventually, his refinement of a masking policy cascades into the code that touches the masked field and into the UI components that display it, with the cascade preview showing every affected surface across the three domains.

A developer working on the same project, regardless of whether he was the founding authority or joined later, encounters the project graph as it has come to be. His code refinements live in the code domain; his cascade reads naturally show which code revalidates and, when the cross-domain edges populate, which UI surfaces and which data queries also revalidate. The familiar discipline of code-domain refinement is preserved exactly; the new capability is that he can *see*, before he commits, what his change implies for the work of the designer and the data modeler. The seams that other tools leave hidden are visible in the cascade. The auditor reading the chain months later sees the same complete picture across all three domains — not three separate audit trails to reconcile, one audit chain that crosses domain boundaries cleanly.

## §5 — The Sonibank context, sharpened

Banking is data. The BCEAO reports a Sonibank pilot will produce are data artifacts — aggregations of regulated values under regulated transformations, exported in regulated formats, retained under regulated schedules. The compliance authority's primary day-to-day concern is data movement and data exposure. The auditor's primary investigative tool is data lineage. The reason banking is the chosen pilot context for Refine is not that banking is code-heavy (it is; every regulated industry is); it is that banking is *data-regulated* in a way that makes the governance claim of refinement-oriented programming face its sharpest empirical test in the data domain. The pilot likely leads with data — not as a phasing accident but as the right empirical proving ground for the meta-paradigm's central claim. *Every change is a typed refinement that the cascade revalidates across all three domains, the gate writes through, and the audit chain attributes*. The data domain is where that claim is hardest to make and most necessary to make true.

UI is no less weighted, contextually. The compliance officer authoring a regulatory report is consuming the same data through a UI that other authorities also consume — the same data, presented differently, with different accessibility needs, with different localization (the BCEAO context is French-language in Niamey), with different visual emphases for different audiences. The UI that the data domain feeds is itself a refinement target. The variable system, the copy voice, the accessibility attributes, the responsive behavior across the field officers' tablets and the central office's desktops — each is a refinement, each enters the gate, each is attributed. The UI domain is where the project's *humans-on-the-other-end* discipline lives, and Refine's claim to govern UI work is the claim that the people authoring the surface have the same governance protections and the same simplicity-dial friendliness as the people authoring the code or the data.

Code, finally, remains what the existing chapters described it as. The function bodies, the control flow, the contracts, the invariants — these are unchanged by this chapter's elevation. What changes is the *naming*: the code domain is one of three. The corpus that already exists is read, going forward, as the corpus of the code domain. The retroactive consolidation — a spec that names what's in the corpus as "the code domain, in detail" — is a small editing pass, queued. The mature parts of Refine remain mature; the elevation makes their scope explicit.

## §6 — The discipline this requires

Naming the three domains as peers requires a discipline going forward, and the discipline is worth stating plainly. *No new feature ships that addresses only one refinement domain without naming what its analog in the other two domains would look like, even if not built yet*. A spec that introduces a new primitive for code refinement names what the UI-domain analog and the data-domain analog would look like, even if those analogs aren't yet specified in detail. A website page that talks about Refine governing changes names all three domains as first-class, even when the immediate exemplar is from one. A tutorial that opens in one domain references the parallel tutorials in the other two, even if those tutorials are queued rather than built. The discipline costs a small overhead per artifact; it buys the consistent claim, made true in every surface, that the paradigm covers all three.

## §7 — Live refinement, across all three domains

A specific capability deserves explicit naming because it recurs across all three per-domain authoring surfaces and is genuinely distinctive to Refine: **live refinement**. Each per-domain authoring surface specifies a Live Mode that lets authors propose typed refinements by picking elements in a running representation of the project — picking a UI component in a running web app, picking a column in a live query result, picking a function in a live debugger session. The interaction is the same across all three: pick a primitive, the system opens a popover offering applicable refinement kinds, the author states an intent in plain English, the system proposes variants, the cross-domain cascade preview shows reach into the other two domains, acceptance routes through the gate, the result is reversible and audit-chain stamped.

Three properties make live refinement distinctive. The mutations are governed even when authored from a live monitor — no live-authoring path bypasses the canonical writer. The cross-domain cascade reaches into the other two domains *at proposal time* — the author sees what an apparently-local change will reach across the whole project graph before they commit. The result is reversible — each refinement carries its typed inverse; rollback is one-click within the reversibility window. None of the existing live-authoring tools — design tools with HMR for UI, query consoles for data, REPLs and live-coding environments for code — combine these three properties.

UI Live Mode (Impeccable-inspired, the most developed of the three in v0.1) and Data Live Mode (the data-domain peer, equally developed in v0.1) ship in the v0.1 specs; Code Live Mode is conceptually clear and operationally queued (the runtime hooks are substantial engineering work). The pattern is a first-class capability of refinement-oriented programming, not a UI-specific feature ported to other domains. The book's pedagogy treats it as one of Refine's defining surfaces alongside the cascade, the gate, the audit chain, and the simplicity dial. Tutorials in the per-domain tracks open with a Live Mode walkthrough so the learner experiences the three-domain framing in the surface where the cross-domain reach is most empirically visible.

## §8 — The lineage, before bridging out

Three citations matter to this chapter, because each represents a domain Refine's claim depends on validating against. For the code domain, the lineage is the broader history of programming — Knuth, Dijkstra, Liskov, the literature on type systems and program correctness, the practice of code review, the discipline of test-driven development, the slow accumulation of tooling that lets a function rename cascade safely within the code. For the UI domain, the recent lineage is Impeccable (`github.com/pbakaus/impeccable`), the design-skill for AI harnesses that translated Anthropic's frontend-design baseline into a 23-command catalog of named gestures, with deterministic anti-pattern detection and a Live Mode authoring surface; Impeccable arrived at, independently, almost every architectural commitment Refine's UI domain will inherit, which is the kind of convergent evidence that suggests the architecture is correct. For the data domain, the lineage is dbt and sqlfluff and Liquibase and Flyway, the modern data-engineering tools that recognized — each in their corner of the data world — that lineage is first-class, that anti-patterns are detectable deterministically, that migrations are change-as-typed-artifact, that authority and audit need to apply to data work as much as to code work. None of these tools individually offer the cross-domain cascade; each, within its domain, validates that the architecture Refine extends across the three is the right architecture for its own domain. *The community brings the pattern; Refine brings the governance. Again, and now in three domains at once.*

## §9 — What this chapter has established — and what it has not

What the chapter has established:

- Refinement-oriented programming is a meta-paradigm: one core model — refinement, cascade, gate, chain, authority, dial — expressed in three domain languages: code, UI, and data.
- The cascade crosses domain boundaries; the seams where projects fail in production become visible, typed edges in one graph.
- Projects can launch from any of the three domains, and designers and data modelers are first-class authorities on the graph, not consumers of outputs.
- Live refinement — pick an element in the running system, state intent, see the cross-domain cascade before committing — is a defining surface across all three domains.

What it has not established:

- Code Live Mode, which is conceptually clear but operationally queued behind substantial runtime engineering.
- The cross-domain cascade's implementation mechanics, which are named here and specified per-domain, not yet demonstrated; the data-led Sonibank pilot is the empirical test still ahead.

*Further, in the reference corpus: `REFINE_THREE_DOMAINS_v0_1`, `REFINE_UI_DOMAIN_v0_1`, `REFINE_DATA_DOMAIN_v0_1`, `REFINE_CODE_DOMAIN_v0_1`.*

But before the honest accounting, the moment demands one more argument — because by the time I was writing this, a thesis louder than mine had appeared, and refinement-oriented programming is, in part, my answer to it.

# Chapter 17 — Two answers: when the artifact dissolves

*The strongest argument against this book — dissolve the artifact, trust the agent — met head-on, with Refine's opposite bet.*

By the time I was writing this, a thesis louder than mine had taken shape, and it deserves to be met head-on rather than waved away. Its sharpest form runs like this: software engineering is not improving — it is *ending*. When a model can understand a task, decompose it, generate the code to do it, and throw that code away when it's done, then code was never the system; it was a transient instrument of reasoning. What ships is the *outcome*, not the software. What persists is the agent's *capability*, not its artifacts. Push the idea to its limit and the distinction between "software" and "agent" dissolves: the agent *is* the system, and it evolves on its own. The names attached to this reading — *Agent-as-a-Service*, "Agent → Result", *Software 3.0* — all point the same way: stop delivering software; deliver results.

## §1 — The dissolve reading, taken seriously

I want to be fair to it, because it is not foolish. It rests on a real observation — the same one this book opened with. Software complexity scales combinatorially while human cognition stays fixed; for fifty years we papered over the gap with methodology, and the gap kept winning. The dissolve reading attacks that gap from the other side: if the bottleneck is human cognitive capacity, route the reasoning through models whose capacity grows with compute, and the bottleneck lifts. That is a genuine argument, and a genuine alternative to mine. Where I say *the unit of change moved*, it says *the artifact disappeared*. We agree the line of code is finished as the unit of work. We disagree about what replaces it.

A whole layer of machinery is being built to make the dissolve reading real, and it is good machinery. Harnesses that let you compose an agent from primitives and bend it to your workflow rather than the other way around. Frameworks that give the agent durable execution, so that when the server dies the work is not lost and the agent resumes where it stopped. Sandboxes, skills, subagents, multi-provider switching, deploy-anywhere runtimes. This is the operational body of the agentic era, and it is maturing fast. I have no quarrel with it. I will say something stronger: refinement-oriented programming *needs* it. An agent has to run somewhere, reliably, before there is anything to govern.

## §2 — What the machinery is silent about

But notice what all that machinery is *silent* about. It answers *how the agent runs* — extensibly, durably, anywhere. It does not answer the question this book keeps returning to: *what do you trust when no human read the code?* A durable stream guarantees the work is not lost; it does not guarantee the work is *right*. A harness lets you compose any agent you like; it holds no opinion about whether the change that agent lands is allowed. And the dissolve reading's own honest reports admit as much from the inside — that agents drift over long horizons, that an early error propagates into compounding failure, that they optimize for finishing the task and not for the maintainability of what they leave behind, that they pass the tests while quietly breaking the meaning. Every one of those is a *governance* failure wearing a *capability* costume. You do not fix "the change broke an invariant nobody was checking" by making the model bigger. You fix it by checking the invariant.

So here is the other answer — the one this whole book has been building. The artifact does not dissolve. It becomes a graph: typed, persistent, governed. And the change to it becomes a refinement that carries its own proof — who decided it, against which declared rule, and everything it cascades into, computed before it lands and reversible after. The dissolve reading escapes the complexity barrier by *scaling the reasoning*. Refinement-oriented programming escapes it by *structuring the consequences*: you never ask a human — or a model — to re-traverse the whole interaction surface by hand; the compiler computes the cascade, and the reviewer reads one card. Trust does not attach to the agent's growing capability. It attaches to the proof.

## §3 — Sonibank, and the wager

I cannot take the dissolve reading at its word, and the reason is Sonibank. In a microfinance institution under BCEAO supervision you do not deliver an *outcome*. Months after a change lands, a supervisor arrives and asks *why* — why this penalty cap, on whose authority, against which directive, touching which obligor records. "The agent was very capable" is not an answer anyone can file. In that world the artifact is not overhead to be dissolved; the artifact, made into a governed graph, *is the proof you will be asked for*. Regulated, long-lived software is not a niche where my answer happens to win. It is the place where the dissolve reading's central promise — trust the capability, discard the artifact — simply cannot be kept, and where you can see most clearly that the artifact was never the problem. Ungoverned *change* was the problem.

I owe the other side its strongest punch. If the self-evolving ecosystems the dissolve reading anticipates genuinely arrive — agents that rewrite their own architectures and need no declared specification of correctness — then everything I have built preserves an intermediary that future says is unnecessary: a persistent graph, and rules a human wrote down. My wager against that is not technical; it is institutional. I am betting that *"who decided this, and what did it touch?"* — liability, regulation, the simple human need to be answerable for consequences — does not evaporate because the typing got faster. And I am careful about the size of my own claim: Refine governs what you have *declared*. A rule you never wrote is a blind spot it cannot see, and *valid* is never the same as *wise*. That boundary belongs in this chapter, not hidden from it — which is, fittingly, what the next chapter is entirely about.

## §4 — Three pipelines, and a fourth position

Set the two answers side by side and a third position falls out, one neither pole states. The failed pipeline was *AI → Software → Result* — use the model to write the old artifact faster, and keep every old bottleneck. The dissolve reading's pipeline is *Agent → Result* — delete the artifact, trust the capability. Refinement-oriented programming is *Agent → governed refinement → Result*: the agent proposes, a deterministic compiler over a persistent graph validates the cascade and the gate, and the outcome itself *is* a trusted, reversible, attributed change. This is why I keep insisting the harnesses and the governance layer are not rivals. They meet at a single seam — the same tool protocol the rest of the ecosystem is standardizing on. The framework brings the muscle; Refine brings the rules. The community brings the agent; Refine brings the governance — the same refrain as every chapter before, now aimed at the loudest claim the moment has produced.

> **Figure 17.1 — Three pipelines.** *AI → Software → Result* kept every old bottleneck. *Agent → Result* deletes the artifact and trusts the capability. *Agent → governed refinement → Result* keeps the artifact as a governed graph — and the outcome itself is a trusted, reversible, attributed change.

There is a fourth position now, subtler than the other two and closer to mine — the one I am most often mistaken for, so I had better mark the seam. Call it **spec-driven development**: the spec is the durable artifact and the code is *generated from it* — *Spec → Code*. This is not the dissolve reading; it keeps an artifact, and the artifact it keeps is the one I most agree is first-class — intent, captured, versioned, made to drive the work. That serious, security-minded builders are now betting AI-native development is *spec-centric, not code-centric* I take as confirmation of half of what this book argues: the line of code was never the unit; intent is. Refinement-oriented programming has said as much from its first page — the requirement, the logframe, the *satisfies* edge are intent made first-class.

But the half we differ on is the half that pays the regulator. If the code is *generated from* the spec, what you hold at the end is a faithful translation, not a governed history — and *regeneration is the opposite of an audit chain*. The spec tells you what the system is *supposed* to be; it does not tell you who moved the penalty cap to sixteen percent, on whose authority, against which directive, and what that move reached. *Spec → Code* makes intent durable and the change ephemeral; refinement-oriented programming makes the *change* durable and governed, with intent as the authority it answers to. So once more the two are not enemies but neighbours: a spec-driven front end that turns intent into code is a fine thing to set in front of the gate — the agent proposes from the spec, and the compiler still validates the cascade, attributes the author, computes what it touched, and keeps the inverse. *Spec → Code → governed refinement → Result.* What I will not surrender is the middle term: the moment a change becomes answerable for itself.

## §5 — The word, the neighbours, and the four loci

The harness was only the first of these neighbours, and once I had the habit of looking I found the same shape everywhere. A system that remembers what an agent has learned. A system that recommends which tools to hand it. A system that isolates where its code runs, or coordinates which agent does what, or teaches a newcomer the shape of a codebase. Each is real and useful; each governs something *around* the change — the agent's memory, its capabilities, its compute, its coordination, its comprehension. None of them governs the change itself. That cell — validate the consequence, attribute it, compute what it touches, make it reversible — is where almost nothing else sits, and it is the cell this book has been describing the whole time.

The newest of these neighbours sharpens the point rather than blunting it. A memory that doesn't merely remember but *learns* — that reflects across experience to form new beliefs — governs what the agent comes to *believe*, and belief is the one thing you might think escapes the gate. It does not. A conclusion an agent reaches from its own history is a change like any other: in a governed world it is typed, attributed to the reflection that produced it, checked against the rules, and reversible if it was wrong. Ungoverned learning is just ungoverned drift wearing a wiser face. So the line extends one notch further than I first drew it — the gate governs not only what an agent *changes* but what it *concludes*.

It even shows in what the word *graph* is being asked to do. So much of this moment organises itself around a graph of one kind or another: graphs that *teach* a codebase, graphs that *remember* an agent's facts, graphs that *recommend* what to bring to a task. Refine's graph does a fourth thing those do not — it *governs*: every node a typed, validated, attributed, reversible change. I have come to think of that as the whole strategy stated as a test. For any new system the field produces, there are only two honest verdicts — *compose* with it, or build the *governed* version of what it does. Memory becomes an audit chain with two clocks. Recommendation becomes selection ranked by trust, not only by relevance. Comprehension becomes an explanation read off the very graph the compiler already checks. A document compiler — the kind of tool that reads a pile of regulations and policies into a tidy knowledge base — becomes the intake that turns those documents into *governed intent*: proposed rules and requirements that land through the gate, checked against the rules already there, rather than knowledge that merely accumulates. The neighbours bring the muscle, the memory, the catalogue; Refine asks, each time, what the governed version would be — and most of the time the answer is to let them run, and govern what they change.

There is a second family of neighbour the compose-or-govern test does not quite catch, and it is worth naming because it shares this book's complaint most closely. A handful of projects answer the same charge — *software arrives faster than it can be trusted* — not by governing something *around* the change but by putting the rigour somewhere else entirely. One bets on **mathematical proof**: behaviour derivable from types, correctness discharged the way a theorem is. One bets on a **formal prompt language**: replace the ambiguous English request with a precise symbolic notation before anything runs. A sister language of my own, Zin, bets on a **compiled constitution**: governance articles a compiler enforces before it emits a line. And this book bets on the **governed change** itself. Four places to put the rigour — proof, prompt, constitution, change — and naming which one a system chose is the fastest way to see what it is. Two of them refuse the agentic premise outright, or nearly so; two of them govern it. The advantage of the change as the place for rigour is precisely that it leaves the intent in plain language and the code where it already lives, and asks for rigour only at the moment a change tries to land.

A subtler confusion deserves a sentence, because it will outlast the harness one. As the governance idea catches on, the word itself is splitting in two, and the halves are easy to mistake for each other. Some of the new machinery governs the *agent*: it caps what the agent may spend, restricts what it may touch, sandboxes how it runs. That is real, and I am glad of it — it is good and necessary work. But it is not what this book has meant by governance. I have meant governing the *change*: validating the thing the agent lands against the rules you declared, computing what it touches, attributing it to an authority, making it undoable. The two govern different objects — one governs the *actor*, the other the *consequence* — and they do not substitute for each other. An agent can stay perfectly inside its budget and its permissions and still land a change that violates a directive no runtime was ever told about. Process and consequence are different things to be answerable for, and only the second is the one the supervisor will arrive and ask me about. When I say Refine governs, I mean the consequence.

I owe one honest caution about the word I keep using. *Governance* is now claimed from more than one direction, and by larger hands than mine — a major platform ships an "agent governance" toolkit that means something real and different: governing what an agent may *do* at runtime, which tool it may call, at what cost, under what policy. That is worth having, and it is not what this book means. This book means **change-governance**: whether the change an agent lands may stand, against the rules the project has declared. Same word, two objects — the actor's *action* and the consequence's *validity* — and they compose rather than compete. Where the shorter word would blur the two, I say *change-governance* in full, and I would rather be a syllable longer than a category vaguer.

## §6 — What this chapter has established — and what it has not

What the chapter has established:

- The dissolve reading is serious and rests on the same observation this book opened with; the disagreement is over what replaces the line — a vanished artifact, or a governed graph.
- The harnesses and frameworks are necessary muscle and are silent about trust; their own failure reports — drift, compounding error, passing the tests while breaking the meaning — are governance failures wearing capability costumes.
- The third pipeline is the book's position: Agent → governed refinement → Result. The fourth position, Spec → Code, keeps the right artifact — intent — but regeneration is the opposite of an audit chain.
- The neighbourhood organizes: compose or govern; four loci of rigour — proof, prompt, constitution, change; and change-governance said in full, because a hyperscaler now uses the shorter word for a different object.

What it has not established:

- Victory over the dissolve reading's endgame. The wager against self-evolving, specification-free ecosystems is institutional, not technical: a bet that answerability does not evaporate because the typing got faster.
- Governance of the undeclared. Refine governs what you have declared; a rule you never wrote is a blind spot it cannot see, and valid is never the same as wise.

*Further, in the reference corpus: `REFINE_IN_THE_AGENTIC_STACK_v0_2` §8, `REFINE_POSITIONING_METHOD_v0_1`, `REFINE_VS_SPEC_DRIVEN_DEVELOPMENT_v0_1`.*

Which leaves the accounting I have been promising. I have just spent a chapter arguing that the artifact should be governed rather than dissolved; honesty demands I now say plainly where that governance reaches its limits — what refinement-oriented programming does *not* do, and where its own promises, pushed too far, would land me in the very trouble I have just accused the other side of.

---

# Part V — The limits

*Chapter 18 and the Coda · What this does not do.* The book closes the way it promised to: a full chapter of honest boundaries — what refinement-oriented programming does not solve, what it shifts but does not remove, and what it has not yet earned — and a coda about where the road goes from here.

---

# Chapter 18 — Honest boundaries

*The chapter of limits: everything refinement-oriented programming does not do, stated as plainly as what it does. Read this one even if you read nothing else.*

Every paradigm makes promises. The promises that hold up are the ones the paradigm can defend with examples; the promises that don't are the ones that get the paradigm into trouble. A paradigm is not honestly delivered until its boundaries are stated as clearly as its capabilities.

This chapter is the explicit statement of what refinement-oriented programming does *not* do. It is the longest section of the book where I am most likely to be wrong about specifics, because some of the boundaries are sharp today but may shift as the field matures. The boundaries as I see them in 2026:

## §1 — It does not solve agentic trust

The most common question about refinement-oriented programming is: *does this make AI agents trustworthy?*

The answer is no.

What refinement-oriented programming does is *make trust legible*. When an agent proposes a refinement, the proposal carries the agent's identity, the scope under which it was made, the cascade it touches, the gates it must pass. A human or a system can read these and decide whether to extend trust *for this specific refinement* — not in general. The decision is contextual, structured, and recorded.

But the underlying problem — that current AI agents can be confused, can hallucinate intent, can be manipulated by adversarial inputs, can produce confidently-wrong outputs — is not solved by any amount of structuring of their output. The agent is still the agent. Refinement-oriented programming bounds the *blast radius* of agent failure (scope limits where an agent can act; gates limit what can land without verification), but it does not eliminate the failure itself.

A team that adopts refinement-oriented programming and concludes that they can therefore let their agents operate unsupervised has made an error. The paradigm makes supervision more *efficient* — a reviewer can review one refinement faster than one diff — but it does not make supervision unnecessary. The expectation of human judgment on consequential changes is *necessarily* preserved by the paradigm, not bypassed by it.

The broader question of agentic trust — when can agents be trusted, in general, to act autonomously in high-stakes contexts — is not a question this book can answer. It is one of the open problems of the field, addressed by alignment research, by capability evaluations, by red-teaming, by the slow accumulation of operational experience. Refinement-oriented programming gives that broader work a *system to act on*: structured records of agent behavior over time, queryable provenance, reproducible audits. It does not replace the work.

## §2 — It does not eliminate the need for tests

A refinement that type-checks, passes its declared gates, and lands successfully may still produce a wrong behavior at runtime. The gates verify what the gates verify; they cannot verify what no one wrote a test for.

This is not a limitation of refinement-oriented programming specifically; it is a limitation of all formal verification approaches. The set of things a system can mechanically verify is always a subset of the set of things that could go wrong. The gap between them is filled by tests, by runtime monitoring, by graceful failure modes, by the long tail of operational experience.

What refinement-oriented programming does is *concentrate the test investment* around refinement points. A team using the paradigm has clear answers to questions like *which tests must pass for this kind of change?* (encoded in path-level gates); *what's the cascade of this refinement, and are all the cascade nodes covered by tests?* (a query against the graph). Test coverage becomes a property of the graph, not an aggregate number across the codebase. Untested refinement points are visible; tested ones can be exercised reliably.

But the tests still have to be written. They have to be maintained. They have to actually exercise the behaviors that matter. None of that goes away. A team that adopts refinement-oriented programming and stops investing in its test suite will find that the paradigm has not protected them from the consequences of inadequate testing; it has only made the inadequacy more legible.

## §3 — It does not replace human judgment

The whole architecture of the paradigm assumes that some questions are answered by humans. Reviewers approve refinements. Compliance officers verify policy matches in cases the compiler can't decide. Architects design the policies and the cascade rules. Authors write the `reason` field with whatever care they bring to it.

When humans make bad decisions in any of these places, the paradigm faithfully records them. It does not correct them. A reviewer who approves without reading is still a reviewer; the audit chain shows that they approved, not that they failed to read. A `reason` field that says "Q2 risk committee · ticket SBR-1284" is no more accurate than the ticket it references; if the ticket was wrong, the `reason` is wrong, and the audit chain inherits the wrongness.

The paradigm provides the *structure* in which judgment is exercised. It does not provide the judgment. A team with weak judgment will produce weak refinements with weak audit trails. The trails will be more queryable than the alternative — that is a real improvement — but the underlying judgment problem is unsolved.

I have seen, in early pilots, the temptation to treat the audit chain as a substitute for thinking carefully. "We have the chain; if anything goes wrong, we can trace it." This is the wrong way to use the chain. The chain is *evidence* of careful thinking, not a *substitute* for it. A team that thinks carefully and records the thinking will have a useful chain; a team that doesn't think carefully and just records the absence of thinking will have a chain that is honestly bad.

## §4 — It is not yet stable

The implementation I have built — Refine, with RFN at v0.1 — is in active development. The grammar may change. The IDE will gain facets and lose facets. The MCP server's protocol will evolve. Refinement records may need migration as the schema matures.

This is true of every new paradigm: the early implementations are the experiments, and the conventions that stick across implementations only become clear once multiple implementations exist. The conventions I describe in this book are my best understanding as of 2026, validated against a single primary pilot at Sonibank Niger, with secondary input from conversations with teams in adjacent industries. They are not the canonical statement of refinement-oriented programming for all time. They are the statement *I am willing to commit to*, knowing that I will revise it.

Teams adopting Refine today should expect a period of churn. The conventions will sharpen; the implementations will mature; some of what I describe in this book may be obsolete in three years. What I believe will be durable is the central move: the unit changed; the line is no longer the unit; the refinement is the unit. That move is not a property of Refine. Other implementations of the same move will follow.

## §5 — It does not address the labor question

A separate set of concerns about AI-assisted software development — what happens to programmer employment, how value is distributed when agents produce most of the code, what the economic structure of software engineering looks like in ten years — is not addressed by refinement-oriented programming.

These are real questions, and they matter, and they have moral dimensions that go beyond engineering practice. I think about them; I do not pretend to have answers to them. What I can say is that refinement-oriented programming, by preserving the *role* of human judgment as a distinct and essential activity, may help preserve the *labor* of human judgment as something that has value. A workflow in which agents produce work and humans rubber-stamp it disempowers humans economically; a workflow in which agents produce work and humans exercise meaningful judgment on it preserves the value of that judgment.

But whether the economic structure of the industry actually preserves human judgment as compensated work is a question of labor, of capital, of regulation, of institutions — not of engineering tools. The tools shape what is possible; they do not determine what happens.

## §6 — It does not solve the "agent acts maliciously" case

A specific failure mode worth naming: what if the agent itself is adversarial?

Most discussions of agent safety treat this as the central problem, sometimes to the exclusion of more mundane failure modes. I think that's an error of proportion — most agent failures in production today are due to confusion, hallucination, or scope drift, not malice — but malicious agents are a real concern, especially as agentic systems become more autonomous and as the line between "internal agent" and "agent acting on external inputs" blurs.

Refinement-oriented programming offers some defense against malicious agent action. Scope grants limit what an agent *can* propose. Gates ensure that consequential changes require human or external review. Cryptographic signatures, where required, prevent forgery. The audit chain ensures that any malicious action is recorded and discoverable.

But a sufficiently capable malicious agent operating within its granted scope can still do damage — it cannot land arbitrary changes, but it can land *technically permitted* changes in damaging ways. A schema migration that is permitted by policy but designed to introduce a subtle data loss; a knob change within bounds that has been selected to maximize harm. Refinement-oriented programming does not detect these in general; no automated system can, because the problem is not structural but semantic.

The defense against malicious agents is, ultimately, the same as the defense against malicious humans: limit scope, monitor behavior, build trust over time, revoke quickly when concerns arise. Refinement-oriented programming gives a team the infrastructure to do all of this — but it does not eliminate the underlying threat model.

## §7 — Performance and cost

A practical boundary: refinement-oriented programming has costs.

The compiler does more work per change than a traditional compiler does. The graph has to be maintained. Gates have to run. Audit records have to be written. Each of these is a small cost individually; collectively they add up to a system that is more *operationally heavy* than the alternative.

For most teams, this is a fine trade — the cost is small relative to the cost of the work itself, and the benefits of attestation and cascade-awareness outweigh the overhead. But for some teams it is not. A team writing throwaway prototype code at high speed will find refinement-oriented programming actively obstructive. A team operating in extreme resource-constrained environments may find the graph maintenance prohibitive.

The cost question is also relevant for the AI side. Running an MCP server that validates every agent proposal adds latency to the agent's workflow; running an in-editor companion that intercepts every change adds friction. For teams where speed is more important than governance, the friction is undesirable. For teams where governance is essential, the friction is the price of the discipline.

I have not done formal performance benchmarks for the Refine implementation, partly because they would be highly dependent on the specific codebase and workflow. What I can say from observation is that the Refine implementation, on a 80,000-line codebase with mixed Python and Zin, validates a typical refinement in under a second and applies it in under five seconds. For most workflows, this is unnoticeable. Some workflows will find it slow.

## §8 — Multi-repo, multi-project, multi-org

A limitation I am aware of but have not fully resolved: refinement-oriented programming, in the Refine implementation, currently assumes a single codebase per project. Multi-repo systems — where a single logical system spans many Git repositories — are not yet first-class. Cross-project refinements (a change in repo A that has a cascade in repo B) require manual coordination.

This is a real limitation, not a small one. Many production systems are multi-repo. The integration story for refinement-oriented programming across repos is an open design problem; I have ideas about it (a shared graph spanning repos, with adapters for each repo's source format) but I have not implemented them, and I expect the implementation will reveal complications I have not yet considered.

The same is true for multi-organization scenarios. A system that spans organizations — a vendor system used by multiple customers, where each customer has its own policies — requires the paradigm to think about federated governance, shared audit chains, and policy interaction. These are real scenarios. I do not have a complete answer for them in 2026.

## §9 — It is downstream, and the composition is mostly still a promise

There is a strategic honesty I owe alongside the technical ones, and it follows directly from the position I spent the last chapter defending. Refinement-oriented programming governs the *consequence* of a change — which means it sits *downstream* of everything that produces the change. The agent runs in someone else's harness; it remembers through someone else's memory; it is handed its tools from someone else's catalogue. Refine governs what all of that *changes*, and only that. The upside is a position almost no one else occupies. The exposure is the other face of the same coin: Refine generates none of the activity it governs. Its value rises only as agents actually land more change, and it cannot manufacture that demand on its own.

There is a sharper version, and it is the one I am least comfortable with. Through this book I have said, more than once, that Refine *composes* with the rest of the stack — that it meets the harness at the tool protocol, that a temporal-memory engine could back its memory, that untrusted execution could be handed to an isolated runtime. Most of those compositions are, as I write, *designed rather than demonstrated*. The argument for each is sound; the integrations are not all built. A reader is entitled to discount a composition until it is shown, and I would rather name that gap than let the word "composes" do work it has not yet earned. The way I mean to close it is unglamorous: build one composition, end to end, and let it stand for the claim. Until then, the seam is a thesis, not a feature — and the most honest thing I can say about Refine's place in the ecosystem is that it is the right place to stand, not yet a fully built one.

And there is a third honesty, the one I held back longest because it complicates the cleanest line in the book. I have written as though *governing the change itself* were a cell almost no one else stands in. That was always slightly too flattering. The cell is occupied at its edges — and well. The most successful change-governance loop running in production today is not Refine; it is infrastructure-as-code with a policy engine: a plan is computed, checked against declared rules, and refused or applied, deterministically, every day, at scale. Schema migrations have their own version of it; merge queues have a scoped one. And a funded class of "AI code governance" tools is now reaching for the generalist version with automated review and a gate. So I should not say Refine is alone where it stands. What I should say — and what the rest of this book has actually been arguing — is that those incumbents each govern *one* artifact through *one* toolchain, with no language-neutral graph beneath them, no cascade computed *across* domains, no `satisfies` edge tying a change back to the requirement it serves, and no inverse waiting to undo it. Refine's bet was never the territory; it was the **depth** — the whole apparatus as one paradigm rather than a policy gate bolted onto a single tool. That is a better bet, but it is also a heavier one, and depth is not a thing you can claim. It is a thing you have to show. The honest statement of Refine's position, then, is not "no one else is here" — it is "others have reached one corner of this; the question is whether the depth that the corner-holders skipped is worth the larger ask, and that has to be demonstrated, not asserted."

## §10 — The discipline is the hard part

I will close this chapter by saying the thing that is least flattering to the work I have done but most true:

The language is the easy part. The compiler is the easy part. The IDE is the easy part. They are not easy in absolute terms — they took years to build — but they are easy compared to the actual hard part, which is the *team discipline* of writing refinements thoughtfully, of taking the audit chain seriously, of resisting the temptation to rubber-stamp, of investing in the practice over a year when the visible benefits arrive only in the second year.

A team that has the discipline produces good work in any paradigm. A team that lacks the discipline produces bad work in any paradigm. Refinement-oriented programming makes the discipline more *expressible* — it provides the structure in which the discipline can be exercised — but it does not provide the discipline itself.

What the paradigm provides, at best, is the *infrastructure for discipline*. The compiler that catches the structural mistakes. The audit chain that makes the careful work visible. The policies that codify what good looks like. The gates that prevent the obviously bad. The records that, over time, accumulate into evidence that the team has been doing the work.

That infrastructure is not nothing. In the agentic era, when the old infrastructure of human-readable diffs has stopped working at the scale agents produce code, having any infrastructure that scales is enormously valuable. But infrastructure is not virtue. The team still has to bring the virtue.

The coda picks up this thread.

---

# Coda — Where this goes

*The open horizon: the four transitions the paradigm still has to make, and the test it must finally pass.*

I have argued in this book that the unit of programming work has changed, that the new unit is the refinement, and that the existing toolchain is built around a previous unit that no longer fits. I have introduced refinement-oriented programming as the paradigm built around the new unit, described its key elements — the graph, the cascade-aware compiler, the audit chain, the authorities, the methodology, the surfaces — and tried to be honest about what the paradigm does and does not do.

The argument is complete. What remains is the question of where this goes next.

I see four trajectories that the paradigm will need to traverse in the years ahead. None of them is guaranteed; all of them are necessary. I sketch them here partly to commit publicly to the work, and partly so that other teams adopting or extending the paradigm have a sense of the open horizon.

## §1 — From one implementation to a field

Refine is one implementation of refinement-oriented programming. It is the implementation I have built, validated against a specific pilot, refined through specific design choices. It is not, and should not be, the only implementation.

A paradigm becomes a paradigm when multiple implementations exist that share the central abstractions but diverge in the details. Java and Smalltalk and Ruby and Python all implemented object-oriented programming differently; the differences taught the field what was essential and what was contingent. The same will need to happen with refinement-oriented programming.

I expect — I hope — to see implementations from research groups, from other companies, from open-source contributors who take the central ideas and embody them in different stacks. Each will bring its own assumptions about what matters. Some will prioritize different languages. Some will integrate with different agent platforms. Some will make different tradeoffs about graph maintenance, about gate enforcement, about audit chain durability. Through their variation, the field will discover what is durable in the paradigm and what is incidental to my specific implementation.

The most useful thing I can do to encourage this is to keep the central ideas *separable from the implementation*. The book you are reading is one part of that work — articulating the paradigm in a way that does not require Refine. The RFN specification is another part — defining a textual surface that any implementation can target. Future work will include reference specifications for the compiler's behavior, the audit chain's structure, the gate semantics, the agent identity model. These are the standards-like artifacts a field needs to coordinate around.

## §2 — From regulated industry to everywhere

The current implementation is validated in West African banking. The next implementations should be validated in adjacent regulated industries — healthcare, infrastructure, defense, government — where the audit chain is similarly non-optional and the principles transfer cleanly.

After that, the harder transition: from explicitly regulated contexts to *implicitly regulated* ones. Most production software is not regulated by a named external body, but it still operates under accountability structures — internal compliance, customer SLAs, legal liability, organizational policy. These structures benefit from the same kind of attestation that explicit regulation requires, just with the structure being implicit rather than codified.

I expect this transition to be slower and harder than the regulated-industry transition. Teams without explicit regulation have less obvious motivation to adopt a heavyweight discipline. The argument for adoption in these contexts has to be made on different grounds: maintainability over years, defensibility in the face of failures, integration with agentic workflows that are coming regardless.

The pattern from previous paradigm shifts suggests this transition will be uneven. Some teams will adopt early because they see the trajectory; others will adopt late, after a precipitating incident in their own work; some will resist for years and then convert all at once. The pattern is familiar from object-oriented programming, from continuous integration, from infrastructure-as-code. Each was once exotic; each is now baseline; each took roughly a decade to traverse the path.

## §3 — From compiler to runtime

The current implementation treats the cascade-aware compiler as a primary tool — something a team installs, runs, and integrates with their existing workflow. This is the right place to start, but I suspect it is not the final form.

In the long arc, I expect refinement-oriented programming to become *runtime-like*: an underlying layer that other tools and languages build on, rather than a separate tool a team explicitly installs. Just as type systems are no longer a separate concern from the language but a property of the language itself, the graph and the cascade may eventually be properties of the codebase that the language compiler manages natively, without a separate tool.

What would this look like? A future language might compile to a graph as its primary representation, with text as a derived view. A future version control system might track refinements as the primary artifact, with commits as a derived view. A future IDE might be unable to operate on a codebase that is not graph-anchored, because the graph would be a precondition for all other operations.

This is speculation. The current implementation is what I can build today, and the speculative future is what other implementations and other generations of programmers may build. But I think the trajectory is clear: the more the paradigm becomes the *background assumption* of how software is built, the less it will feel like a thing one adopts and the more it will feel like the way things work.

## §4 — From the engineer to the team to the industry

Most of this book has addressed the practitioner: the senior engineer, the team lead, the architect who is reading this and deciding whether to commit to the paradigm. That is the audience whose decisions matter most in the immediate future, because they are the people who will adopt the paradigm into their work and whose adoption will determine whether it spreads.

But the paradigm will not stop at the team. Once enough teams have adopted it, the conversation will widen. Hiring will start to look for refinement-oriented experience. Curricula will include refinement-oriented programming alongside the other paradigms. Standards bodies will codify aspects of the audit chain. Regulators will begin to *expect* attestation of the kind refinement-oriented programming provides, and the absence of it will become a flag.

I do not know when these wider effects will arrive, or in what order. I am writing this book partly to accelerate them. A paradigm that is widely understood becomes adopted faster; a paradigm that is poorly articulated takes longer to spread, even when the underlying ideas are sound. The book is one of the artifacts the field needs in order to grow.

I do not pretend this is a complete account. There is material in this book that I will look back on in five years and want to revise. There are gaps I have not identified yet, and ones I have identified but did not have the answers for. There are claims I have made that careful work will sharpen, and other claims I have made that careful work will disprove. The book is the position I am willing to take publicly *today*; it is not the last word.

What I hope it is, is *clear enough to argue with*. If you read this book and disagree with it — if you think the unit has not changed, if you think the existing tools are adequate, if you think the paradigm I have described is the wrong response — the work I have done makes it possible for us to disagree productively. We can point at specific claims; we can ask for specific evidence; we can build alternative implementations; we can let the work of building and using the systems decide.

That is the test I will hold the paradigm to. Not whether it is rhetorically convincing today, but whether the teams that adopt it produce better-attested software, fewer regulatory incidents, more maintainable codebases, more responsible AI-assisted development over a sustained period. If they do, the paradigm earns its claim. If they don't, the paradigm will be revised — by me, by other practitioners, by the field — until it does, or until the field finds something better.

I have built what I could build. I have written what I could write. The rest is the work of the community that adopts, critiques, extends, and replaces what I have done.

I am ready to be wrong about parts of this. I am committed to the central move.

The unit changed.

We need to change with it.

---

**Mansour Ayouni**
*Niamey · Tunis · Paris · 2026*

---

## About this book

*Refinement-Oriented Programming: A manifesto for software in the agentic era* is the first articulation of the paradigm and the reasoning behind it. The book is intended to be read by practicing engineers, technical leaders, and anyone making strategic decisions about how their team builds software in an environment where AI agents produce code at scale.

This book draws on:

- The development of **Refine**, the cascade-aware programming environment built by Softanza Labs that governs refinement across three first-class domains (code, UI, data), validated against the Sonibank Niger banking system under BCEAO (West African Central Bank) regulatory compliance.
- The **RFN specification** (v0.1, June 2026), the Refinement Notation Language that gives the paradigm its textual surface.
- The **foundations** of refinement-oriented programming as documented at refine.softanzalabs.com, including thirty-plus concept pages, twenty-nine tutorials, and a complete prototype of the Refine IDE.
- Conversations with engineers, compliance officers, and technical leaders in West African banking, European fintech, and the broader regulated software industry between 2024 and 2026.

The book does not duplicate the reference material available at the Refine website. It states the position; the reference material shows the implementation. Both are needed; neither replaces the other.

**Honest disclosure.** I am the author of this book and the founder of Softanza Labs, the company that builds Refine. The book is a manifesto for a position I have a commercial interest in seeing adopted. I have tried, throughout, to be explicit about the boundaries of the paradigm, to distinguish what is durable from what is contingent, and to avoid claims I cannot defend with examples. Readers should still weight my arguments with the awareness that I am not a neutral party. I am the position's most-invested advocate, and I am asking you to consider it on its merits.

If the position is correct, the work I have done was worth doing. If it is not, the work was honest in its intent, and revising it is the proper next step. The criterion is not who is convinced today; it is whether the practitioners who adopt the paradigm produce better software over time.

**Where to read more:**

- refine.softanzalabs.com — The product, the prototype, the foundations pages, the tutorials, the RFN specification, the research notebook.
- The eighteen chapters of this book — the paradigm.
- The work of adopting and validating the paradigm in your own context — the test.

**v0.1 · 2026**
*This is the first edition. Revisions will follow as the paradigm matures and as the field develops.*

---

## Appendix — The words that keep shifting, pinned

The hardest thing about this moment is not the ideas; it is the vocabulary. The field keeps reusing a small set of words for different things, and a reader can lose an afternoon to a sentence that would be clear if everyone agreed on what *governance* or *agent* or *memory* meant. This appendix does not invent terms. It takes the words this book leans on most, pins each to **one** meaning, names what it is most often confused with, and points to the chapter that settles it. When a passage feels slippery, the word has probably moved on you. Come here; it has not moved here.

**Refinement** — The unit of work in this book: a typed, validated, attributed, reversible change to a *subset of the codebase graph*, carrying its cascade, its author, the rule it satisfies, and its inverse. *Confused with:* a diff or patch (which is only the textual trace of a change), and — importantly — a "refinement" in the formal-methods sense (a correctness-*preserving* step from an abstract spec toward code; an older, narrower, proof-driven idea). *Settled in: Ch 2 (and the name-collision in Ch 2 §6).*

**The graph** — Code and all its facets — policy, tests, requirements, infrastructure — as one language-neutral, typed property graph; the *working representation* the compiler reads and maintains, not a diagram drawn beside the code. *Confused with:* an architecture *model* (a picture *of* the system), and the field's other graphs — ones that *teach* a codebase, *remember* an agent's facts, *recommend* what to bring. Refine's graph does a fourth thing: it *governs*. *Settled in: Ch 3 (the four jobs of a graph, Ch 17).*

**The cascade** — The set of nodes a change forces to revalidate — its *computed blast radius* — produced before the change lands and read *in place of the diff*. *Confused with:* the diff (the textual trace), and an AI reviewer's impact comments (advisory prose). The cascade is computed, and a gate can *refuse* on it. *Settled in: Ch 5.*

**The compiler / the gate** — The deterministic governor that checks a refinement in four stages and refuses what cannot be validated; "the gate" is its decisive moment — commit or refuse. *Confused with:* a linter or CI (which advise but do not decide), and a theorem prover (the compiler checks the rules you *declared*, not full mathematical correctness). *Settled in: Ch 4 (its limits, Ch 4 §5).*

**Authority** — Who may make a refinement: a human, an AI agent, or a rule. All face the same gate. An authority is identity *plus scope* — not "who you are" but "what you are permitted to change." *Confused with:* identity alone. *Settled in: Ch 6.*

**Governance** — The most overloaded word in the field. This book always means **change-governance** — *may this change land, against declared rules?* — unless it says otherwise. *Confused with:* *process-governance* (cap an agent's cost, access, or runtime — govern the *actor*) and *access-governance* (Zero Trust — what an actor may *reach* at runtime). All three compose; they are different objects. *Settled in: Ch 6, Ch 17.*

**Harness** — As the field now uses it, the layer that *runs and extends* an agent (e.g. Pi, Flue) — the execution machinery. It is **not** Refine: Refine is where an agent's *consequences* are governed, not where the agent is built or run. *Confused with:* Refine itself (early drafts of this paradigm misused "harness" for it; that usage is retired). *Settled in: Ch 17.*

**Memory** — In Refine, a *queryable view of the project graph that the team owns* — pinned attention, recently-touched, open intent, stale-flagged — not a private buffer the agent owns and the team cannot inspect. The agent does not store; it queries. *Confused with:* the industry's "private buffer" memory. *Settled in: Ch 13.*

**RAG / Context** — *RAG* (retrieval-augmented generation) names a *mechanism*: retrieve relevant material, place it in the prompt, generate. **Context** is what Refine governs in its place — the *concern* beneath that mechanism: what an agent was allowed to see before it acted, what it cost, and what the turn can be replayed from. Everything RAG does, Context makes auditable and bounded; the book names the surface for its governance question, not its mechanism (the same move as *design variable* over *token*). *Confused with:* a standalone "RAG facet" — there is none, by design; and the *retrieval source* itself (the knowledge base retrieved *from*), which Context does **not** own — making that source governed is a separate, queued concern. *Settled in: Ch 13 (what the agent sees and knows).*

**Agent** (and the three that share the name) — An *llm-agent* is model-driven (it reasons, and can be wrong). A *pi-agent* (Softanza's term) is deterministic and computationally independent. **Pi** (proper noun, pi.dev) is an unrelated agent *harness* — same syllable, different thing. When this book says "agent" plainly, it means an authority that proposes refinements. *Settled in: Ch 12, Ch 15.*

**Provenance** — The lineage of *trust* a change carries: which model proposed it, under what prompt, through which tools, at what trust label. *Confused with:* *supply-chain provenance* (was the built *artifact* tampered with on its way to production?) — that governs the binary's journey; Refine's provenance governs the change's *authoring*. *Settled in: Ch 6.*

**`satisfies` edge / the logframe** — The link from a change (or a node) to the *requirement* it serves. It lets the audit chain answer "what was this for," and it goes *stale* when code drifts from intent. *Settled in: Ch 3, Ch 6.*

**Drift** — Code quietly diverging from the intent it was meant to serve, detected as a *stale* `satisfies` edge. Drift is **flagged, not blocked** — the paradigm surfaces it; humans decide. *Settled in: Ch 3.*

**Valid / wise / proven** — Three different bars, kept apart on purpose. *Valid* = the compiler will let it land (it satisfies declared rules). *Wise* = a human judges it a good idea (the compiler has no opinion). *Proven* = mathematically verified correct (this paradigm does **not** do this). The recurring line: *valid is not wise, and valid is not proven.* Note one consequence: *wisdom* can be written down (a taste file like OPINIONS.md) and fed to an agent as advisory context, but it is still never *gated* — declaring wisdom is allowed, gating on it is not. And beware the inverse mistake: a *context advantage* (a rule or requirement you could have written down) is not taste — it belongs *in* the gate as declared intent, not beside it. *Settled in: Ch 4, Ch 18.*

**Cascade vs verdict vs audit chain** — Three things readers blur together. The *cascade* is what a change touches (impact). The *verdict* is the gate's recorded decision on it — passed or failed, with reasons (decision). The *audit chain* is the durable, append-only sequence of verdicts over time (history). *Settled in: Ch 4, Ch 5, Ch 6.*

**The dial (Guided / Standard / Expert)** — A presentation *altitude*, not a capability gate. The same refinement is produced whether authored through a guided form, a command line, or a raw edit; the dial changes how much is *shown*, never what you are *allowed* to do. *Confused with:* a beginner/expert feature split. *Settled in: the simplicity discussion (Ch 16).*

**Live refinement** — Acting on an element in a *running* representation of the project — a component in the live app, a column in a live query result, a function in a debugger — to open a typed refinement on it, see its cross-domain cascade, and accept it through the gate. The governed cousin of "direct manipulation." *Settled in: Ch 18.*

*If a word you need is not here, it is probably not one the field disputes — look it up in the chapter where it first appears. This appendix is only for the terms that move.*
