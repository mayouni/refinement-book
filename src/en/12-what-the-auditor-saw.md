---
id: what-the-auditor-saw
part: 4
number: 12
title: What the auditor saw
stage:
  built: "a governance saved to a file with its regime and its decisions, and loaded back; the decisions asked by action and by actor, each with the authority and risk at the time, a time and the action; the source saved with its current values"
  designed: "a refinement carrying its cascade, author, verification and history (the architecture document); an export scoped to an auditor's question"
  absent: "the timeline saved with the source; an approver distinct from the actor; the values before and after in a decision; the reason a person gave, in the record; two clocks; an auditor's reading of a finding the library produced, outside this story"
status: draft
research: research/ch12.md
guards: [gate_deepening_narrated, governance_lineage_narrated]
---

In this chapter the auditor comes to Softibank, eighteen months after the letter, and asks the question auditors ask. I answer it with what the library keeps after the program that made the change has ended: a governance saved to a file, with its decisions. I show what that record answers, and the parts of the question it does not answer yet. Then I step outside the story and say what the record of a real bank in Niamey holds.

## The visit

Eighteen months after the letter, on a Monday in March, the auditor came to Softibank. It was the scheduled kind of visit, with a checklist refined over many visits to many banks. He opened with the question he always opens with:

"The penalty-cap revision, the September before last. Show me who approved it, what it affected, and how you know your customer communications matched the new rate."

In many banks that question starts a small project: tickets pulled, emails found, a binder assembled. In the Teaching Edition of this book, Amina typed for a few seconds and turned the screen around. This chapter runs what she could turn around today.

## The field

The field's audit trail is assembled from many systems: the history of the repository, the tickets, the approvals in the review tool, the deployment logs. Each keeps its part, and an audit joins them, by hand or by a tool built for it. This is general knowledge. The record exists; it is scattered, and the joining is the work.

## The principle

**The record an auditor needs is written by the act of changing, not by a person afterwards, and it outlives the program that made the change.**

## The record that survives

Run it. Here is the change of chapter 11 once more, made on a governed code, and at the end the governance is saved to a file, the way it would be kept at the bank:

```haro
cDoc = 'cap    = <R:PARAM name="penalty_cap" value="0.18" min="0.10" max="0.20">' + nl +
       'ceil   = <R:PARAM name="regulatory_max" value="0.18" min="0.10" max="0.20">' + nl +
       'letter = Late payments carry a penalty of <R:PARAM name="letter_rate" value="18" min="10" max="20"> per cent.'
b = new stzRefinableCode(cDoc)
b {
	SetGovernedBy(new stzGovernance("softibank"))
	DeclareDerivation("letter-covers-cap",
		func oC { return (0 + oC.ValueOf("letter_rate")) >= 100 * (0 + oC.ValueOf("penalty_cap")) },
		"the letter may not state less than the cap in force")
	SetActor("compliance-officer")
	SetRiskFor("regulatory_max", 3).SetAllowRefine("regulatory_max").SetAuthorityLevel(:Autonomous)
	SetActor("pricing-agent")
	SetRiskFor("penalty_cap", 2).SetRiskFor("letter_rate", 1)
	SetAllowRefine("penalty_cap").SetAllowRefine("letter_rate").SetAuthorityLevel(:Delegated)
	Refine("penalty_cap").To("0.16")
	Refine("letter_rate").To("16")
	SetActor("compliance-officer")
	Refine("regulatory_max").To("0.16")
	cCode = Save("softibank_code")
	cFile = GovernanceQ().Save("softibank_audit")
}
? cCode
#--> softibank_code.zrfn
? cFile
#--> softibank_audit.zgov
```

Two files: the code with its current values, and the governance. Eighteen months later the program that made the change is long gone, and the files are not. Load it back:

```haro
g = new stzGovernance("audit")
g.LoadFrom(cFile)
? g.NumberOfDecisions()
#--> 3
aD = g.DecisionsAbout("refine-regulatory_max")[1]
? aD[:actor]
#--> compliance-officer
? aD[:authorityAtTime]
#--> autonomous
? aD[:riskAtTime]
#--> 3
? len(g.DecisionsOf("pricing-agent"))
#--> 2
```

Three decisions. The move of the regulation was decided by the compliance officer, holding autonomous authority, on an action of risk tier three. The pricing agent, an AI agent, made two decisions: the cap and the letter. Each decision also carries the time it was made, read from the clock, which I do not print because it changes at every run.

That is the first part of the auditor's question, answered from a file as *who acted*, with the authority each actor held at the moment it acted. Nobody wrote this record; it is what the gate leaves when it admits a change under governance.

## What the record answers, and what it does not

Read the auditor's question in three parts, against what the file holds.

**Who approved it.** Answered as who acted: the actor of each decision, its authority at the time, the risk of the action, the time. The pricing agent's changes were admitted on its own delegated authority; an approver distinct from the actor is not in the record, and the Teaching Edition's screen had one.

**What it affected.** Answered in part. The decisions name their actions, `refine-penalty_cap`, `refine-letter_rate`, `refine-regulatory_max`, and the source saved with its current values, `softibank_code.zrfn`, shows where the points stand now. The values before and after are in the timeline of the running object, and chapter 7 said the timeline is not saved. The cascade of chapter 6 is asked of a point today; it is not kept with the decision.

**How you know the communications matched.** Answered by a rule, not by a record. The rule `letter-covers-cap` was declared, and the gate refused the one order of changes that would have broken it, as chapter 11 ran. But the file does not keep the rule, nor the refusal: the governance saves its regime and its decisions, and a rule across points belongs to the refinable code. An auditor has to take the rule from the code; the refusal is not kept yet.

So the screen Amina could turn around today answers the first part of the question as who acted and under what authority, the second in part, and the third by pointing at the code. The Teaching Edition drew a screen that answered all three, with an export scoped to the question and two clocks on every line. That screen is the direction. The architecture document describes a refinement that carries its cascade, its author, its verification and its history; the file above is the part of it that is built.

## The report

In the story, the auditor spent the afternoon on what auditors should spend it on: whether the declared rules were the right ones, and whether the authorities were given to the right people. The report filed three weeks later was clean.

That is fiction, and I mark it as such. The record of this book holds no auditor's reading of anything the library produced.

## Outside the story

My Softanza book tells, in its chapter 29, what was delivered to a commercial bank in Niamey, under the same regional regulator. It is an organisation-assessment product, installed on the bank's own network under licence, which judges an organisation chart under the regulator's rules. It uses the name Softibank for that bank too, and says the name is fictional. The letter, the people and the eighteen months of this book are not that bank's history; they are a story built to carry a discipline.

What the Softanza book's chapters 29 and 31 say is absent is worth repeating here. It is the honest edge of Part IV: no word from the bank's own people, and no auditor's reading of a finding the library produced. The evidence of this discipline is the code that ran in these chapters, at the commit this book is pinned to. The evidence of its use at a bank is still to come.

## What I refused

**I refused to write the audit trail by hand.** The decisions in the file were written by the gate, at the moment of each admission. A record a person writes afterwards is missing the week it is needed.

**I refused to show the screen the Teaching Edition drew as if it ran.** The file above is what runs. The rest of the screen is in the limit.

## The court

`gate_deepening_narrated`, in the library's `base/test/refine/`, asserts that a governed admission leaves at least one decision in the lineage. `governance_lineage_narrated`, in `base/test/governance/`, asserts the round trip. A governance saved and loaded back still judges, its decisions come back with their time, action and rationale, and a decision still reports the risk it was taken under after the rules have changed. That last one is the auditor's guarantee: the file records what was true, not what is.

## Where the field leads

The field leads in the audit itself. Tools built for compliance keep evidence from many systems, map it to controls and export it for an examiner, and banks use them. The library keeps one kind of evidence, the decision to admit a refinement, and keeps it well: with the authority at the time, written by the act. Joining it to the rest of a bank's evidence is a program the bank or a product writes.

## The limit

What is built: a governance saved with its regime and its decisions and loaded back; decisions asked by action and by actor, with authority and risk at the time, a time and the action; the source saved with its current values. All of it ran above.

What is designed: a refinement carrying its cascade, author, verification and history; an export scoped to an auditor's question.

What is absent: the timeline saved with the source; an approver distinct from the actor; the values before and after in a decision; the reason a person gave for a refinement (a decision recorded directly can carry one, and the guard above keeps it intact, but a refinement's decision carries a fixed rationale that names its origin); two clocks; and, outside the story, an auditor's reading of a finding the library produced.

## In your hands

Write the auditor's third answer. The question was how you know the communications matched; the file cannot say. Design the smallest record that could: what it would keep, when it would be written, and by whom.

```haro exercise
? read(cFile)
```

Read the saved file line by line first. Then write, under it, the lines your record would add: the rule, its text, the refusals it made and the values before and after. When you have written them, you have written a request for the library, and for the next letter.

Part IV ends with the auditor gone and the report filed. Part V turns to the product built on this foundation: Refine, the environment, as stage and direction.
