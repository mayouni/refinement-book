# Writing Style Guide — Refinement-Oriented Programming

The conventions for prose in this book. Calibrated to the voice and register locked in `CLAUDE.md`: documentary, calm, grounded, plain, honest about scope.

---

## Voice

**Documentary, not polemical.** Report what happened. Let the reader conclude.

**Calm, never breathless.** No revolutionary, no game-changing, no paradigm shift. No exclamation marks except in quoted direct speech.

**Grounded.** Every abstract claim has a concrete instance in the Sonibank narrative. Abstractions without grounding get reworked.

**Plain.** Short sentences by default. Long sentences earn their length. Jargon is defined on first use (in an aside if needed) and stays consistent thereafter.

**Honest about scope.** "At Sonibank Niger," "in the WAEMU context," "for this team." Avoid sweeping universals; flag generalizations explicitly.

---

## Mechanics

### Sentence length

The first sentence of any paragraph runs no longer than 25 words. A long sentence (40+ words) appears no more than twice per page. Long sentences are reserved for moments where the rhythm demands them — a list of consequences, a chain of reasoning, a passage of inevitability.

### Paragraph length

Most paragraphs run 2–5 sentences. Single-sentence paragraphs are a deliberate emphatic device, used sparingly (no more than two per page). Paragraphs of 6+ sentences are rare; if one appears, ask whether it should be two.

### Em dashes

Used freely. The em dash is the workhorse of this book's prose rhythm. Set with thin spaces or, in plain Markdown, with the dash flush against the surrounding words:

> *The bottleneck moved — from the writing of code to the review of code — and showed no sign of slowing.*

The HTML reader renders em dashes correctly via `—` directly in the Markdown source.

### Lists

Lists are reserved for content that is genuinely enumerable. Never use a list to avoid writing prose. If the items have varying weight or argue with each other, write prose.

### Numbers

- Spell out one through ten in prose ("six weeks," "fourteen loan products").
- Use digits for numbers above ten or when precision matters ("Directive 4.5," "20 percent," "16 percent").
- Percentages: digits + word ("16 percent," not "16%") in prose. The percent symbol appears in tables and figure labels only.
- Currency: the CFA franc is referred to as "the CFA franc" on first mention and "the franc" thereafter; avoid the `XOF` ISO code in prose.
- Years: digits ("2026"), no `'`-abbreviation.

### Foreign words and phrases

The book is in English but lives in francophone West Africa. Foreign words and phrases appear:

- In **italics** the first time used: *Banque Centrale des États de l'Afrique de l'Ouest*.
- In **roman** thereafter once the reader knows the term.
- French-language proper nouns retain accents: *Côte d'Ivoire, BCEAO, OHADA*.

### Em-dash speech

When quoting people, use clean double quotes with surrounding tags:

> "We need to know what else this touches," Amina said.

Avoid stage-directing the speaker ("she said firmly," "he muttered") unless the manner is the point.

---

## Conventions specific to this book

### Names

- **Amina Bello** — main character. Always "Amina" in narrative (her first name is what the team and the regulator's letters use). "Bello" only on initial introduction in each major chapter.
- **Sonibank Niger** — the bank. Always "Sonibank" after first mention. Never "Sonibank Limited," "Sonibank S.A.," or other formal variants — the book treats it informally as her institution.
- **BCEAO** — the regulator. Always BCEAO; full French expansion on first mention in each chapter, then the acronym.
- **The methodologist** — Mansour's stand-in. Never named in the book. Refer to him by role.
- **The agents** — collective term for AI coding agents on the team. Never "AI tools," "copilots," "LLMs," "AIs" — too generic. "The agents" is how the bank's team refers to them, and the book uses their idiom.

### Locations

- **Niamey** — the bank's city. The capital of Niger.
- **Dakar** — where BCEAO is headquartered (Senegal). Where Amina studied.
- **Ouagadougou, Bamako, Abidjan** — neighboring WAEMU capitals; mentioned only when relevant.
- The book does not lecture readers about West African geography. Place names appear with context but without exposition.

### Time

- Months and seasons in lowercase ("September," "the rainy season").
- Months in francophone context: ("le mois de septembre" in dialogue if a character is speaking French; otherwise English).
- The book's narrative present is loosely "the 2020s." Specific years (2024, 2025, 2026) appear when needed for technical context (e.g., "by 2026 the agents wrote eighty percent of new code"). Avoid pinning the narrative to a precise calendar year — Mansour wants the book to age well.

---

## Things to avoid

The following terms, phrases, and habits are unwelcome in this book.

| Avoid | Use instead |
|---|---|
| substrate | runtime, engine, graph model, system |
| revolutionary | (delete; show, don't claim) |
| game-changing | (delete; show, don't claim) |
| paradigm shift | (delete; show, don't claim) |
| best practice | what worked, what they did |
| AI | the agents (when in narrative); the language models (when technical) |
| developer | programmer |
| stakeholders | (be specific: officers, auditors, the team) |
| leverage (as verb) | use, draw on, rely on |
| utilize | use |
| in order to | to |

These are conventions, not rules. Break them when the prose demands it. But the default register is plain, grounded, and unmarketed.

---

## Figures and asides

### Figure captions

Format:

```
Fig. X.Y. Sentence-case caption ending in a period.
```

Captions are short — one or two sentences. The figure does the work; the caption labels it. No "see how" or "notice that" instructions.

### Asides

Asides are short defining or framing blocks. They appear inline in Markdown as blockquotes with bold-leading definition:

```markdown
> **WAEMU.** The West African Economic and Monetary Union. Eight member states...
```

Asides are for terms the reader benefits from having defined immediately, without breaking prose flow. They are not for digressions, tangents, or jokes. Keep them factual.

---

## Editorial conventions

- **Serial comma:** used. "Benin, Burkina Faso, and Niger."
- **Hyphens:** used in compound modifiers before a noun ("agent-driven throughput") but not after ("the throughput was agent driven").
- **Capitalization:** sentence case for headings, section titles, and chapter titles. Title case appears only in the book's title page and the cover.
- **Spelling:** British and American English are both acceptable but consistent within a chapter. Default to American spellings since most expected readers are international and American conventions are more widely recognized.
