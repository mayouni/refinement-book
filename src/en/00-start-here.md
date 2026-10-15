---
id: start-here
number: 0
title: Start here
status: draft
research: research/ch14.md
---

This book is about one discipline: governing the change to software, now that writing the change is no longer the slow part of the work. I call it refinement-oriented programming, and I tell it through a bank that receives a letter.

**The story.** A bank in Niamey, Softibank, receives a letter from its central bank, and the book follows the change it asks for, to an auditor's visit eighteen months later. Chapter 1 says what in the story is invented and what is real.

**The code is real.** Every block in this book runs against the open Softanza library, at the commit `93d7a39bd`, the same commit my Softanza book runs at. Each block is followed by the exact answer it printed, and the book's build runs every block again and refuses a page whose answer changed. A block marked as an exercise is yours to run; I do not print its answer. To run a block yourself, take the library's public repository at that commit and run the blocks of a chapter in order, in one program that loads the library first; the book's own runner, `tools/book_run.py`, does exactly that.

**The language is Haro.** The blocks are written in it. They take three forms: the classic form, which names the object on every line; the chain, for one sentence; and the scene, `obj { ... }`, where three or more things are said to one object.

**Every chapter says where it stops.** Its front matter names what is **built**: the code exists and a block ran, and the chapter's court says which guards assert it. It names what is **designed**: a document specifies it, and the code is the next step. And it names what is **absent**. Each chapter ends with a limit and with something left in your hands: a defect, an open question, a rule to write.

**The earlier edition.** This book was first published as a Teaching Edition in 2026. Where this edition departs from it, a page says so and names it.

**The book stands on another.** *Softanza — The Governed Software Platform of the AI Age* is the foundation, and this book cites its chapters rather than repeat them. Refine, the product built on that foundation, has a part of its own at the end, as stage and direction.

**The parts.** Part I, the discipline: the letter, what broke, the unit of change. Part II, the gate, run: the point, the gate, the cascade, the timeline, trust and governance. Part III, the AI agent at the point. Part IV, Softibank's eighteen months, to the auditor's visit. Part V, Refine. A coda, and a glossary.

Read it in order, with the library open beside you. Run each block before you read what I say about it.
