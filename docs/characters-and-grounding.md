# Characters and Grounding — Refinement-Oriented Programming

The dramatis personae and the institutional context. Keep this consistent across chapters.

---

## Principal characters

### Amina Bello

The narrative's centre of gravity.

- **Role.** IT methodologist at Sonibank Niger. The role is part programmer, part analyst, part compliance liaison — common in small banks in francophone West Africa. She is the person the team brings questions to when the question is about *how to work*, not about a specific technical detail.
- **Background.** Hausa-Nigerien. Born in Maradi, grew up in Niamey. Lycée in Niamey. Computer science at the Université Cheikh Anta Diop in Dakar. First job at a small Senegalese fintech. Returned to Niamey in her late twenties.
- **Languages.** French (her professional language), Hausa, English (technical reading and conferences), some Wolof from her Dakar years.
- **Age in narrative.** Mid-thirties.
- **Demeanour.** Calm. Asks one question at a time. Does not raise her voice. Listens before responding. Writes carefully when she writes (the book occasionally quotes from her notebook).
- **Voice.** When she speaks in the book, her sentences are short, considered, and slightly formal — the cadence of someone who works in two languages and chooses each word in each.
- **Family.** Married, two children (ages 5 and 8 in the narrative present). Husband works in agricultural extension. The book mentions her family lightly; it is not a character book about her family.

She is **not** an exceptional engineer. She is a working professional whose job became different around her, and who responded by changing how the work was done. The book is not the story of a hero programmer. It is the story of a competent practitioner doing careful work in a context that demanded it.

### The methodologist

Mansour's stand-in within the narrative. **Never named** in the book. Referred to by role: "the methodologist," "the consultant," "the visiting specialist," or simply "him."

- **Role in narrative.** Asks questions. Sketches diagrams. Goes back to Tunis between visits. Returns with a refinement of the previous month's discussion. The work belongs to the team; the methodologist is a mirror they use.
- **Appearances.** Sparing. Maybe a half-dozen scenes across the book. Always with the team, not in isolation.
- **Why unnamed.** This is the book Mansour is writing about a discipline; he is not the protagonist. The naming convention makes the methodologist a function rather than a character, which is true to how Mansour wants to be read.

### The auditor

Visits at month 18. The book's final perspective check.

- **Role.** A BCEAO auditor — a senior banking-supervision officer who has done this for two decades.
- **Demeanour.** Polite, methodical, unimpressed by novelty. Asks for specific documents. Reads them carefully. Does not editorialize.
- **The audit scene.** Chapter 12. The auditor occupies a conference room for three days. The team brings what's asked for. The cascade history answers what used to take days of compilation.

---

## Secondary characters

### Issa, the senior programmer

The team's longest-tenured developer. Late forties. Has worked at Sonibank for fifteen years. Initially skeptical of the discipline. Becomes one of its strongest advocates by mid-book.

### Fatou, the compliance officer

The compliance department's representative on the IT side. Mid-forties. Holds a French banking-law qualification. Becomes the first non-programmer to write her own validators (Chapter 9 beat).

### The two interns

Both in their early twenties. Mentioned together. One stays at the end of the year, one returns to university. The interns are the canary — they are the readers of the future, and how easily they adopt the discipline says something.

### The CIO

Amina's boss. The person who said yes to the methodologist's first visit. Appears in three or four scenes. A steady, conservative banker with enough imagination to authorize an experiment.

---

## Institutional context

### Sonibank Niger

A real bank in Niamey. The book treats it with documentary respect — no caricature, no hagiography.

- **Size.** Small/medium commercial bank. The book does not commit to specific deposit or loan-book figures; it is treated as institutional rather than statistical.
- **Customer base.** Individuals, small businesses, mid-sized commercial customers, some agricultural lending. Not corporate-banking-heavy.
- **Product mix.** Fourteen loan products in the narrative present. Several deposit products. Standard West African retail banking.
- **IT footprint.** Ten programmers + two analysts + Amina + two interns. A few external consultants on retainer. Some COBOL fragments (the back office), Ring + Python (the front office and reporting layer), some Java (interbank messaging).
- **Compliance posture.** Conservative. Sonibank has not had an audit finding worth mentioning in five years.

### BCEAO

The **Banque Centrale des États de l'Afrique de l'Ouest**, the Central Bank of West African States. Headquartered in Dakar, Senegal.

- **What it does.** Sets monetary policy for WAEMU, supervises commercial banks across the eight member states, issues the CFA franc, conducts the regulatory audits the book references.
- **Typical year.** Three to four directives sent to commercial banks, ranging in scope from minor adjustments (a ratio, a threshold) to substantial (new prudential requirements). Each directive triggers a six-to-eight-week compliance cycle at every commercial bank in the zone.
- **Audit cycle.** Every three years per bank, with shorter follow-up visits in between when warranted.
- **In the book.** Treated with respect. The auditors are professionals doing a professional job. The book never positions BCEAO as antagonist.

### WAEMU

The **Union économique et monétaire ouest-africaine**, the West African Economic and Monetary Union. Eight member states: Benin, Burkina Faso, Côte d'Ivoire, Guinea-Bissau, Mali, Niger, Senegal, Togo.

The book uses WAEMU as the regulatory and economic frame. The CFA franc circulates across all eight states; commercial banks operate under harmonized regulation; the OHADA business-law framework adds another harmonization layer that complicates software design.

### OHADA

The **Organisation pour l'Harmonisation en Afrique du Droit des Affaires**, the Organization for the Harmonization of Business Law in Africa. A 17-state legal harmonization framework that overlaps but does not coincide with WAEMU.

OHADA matters to the book because software at Sonibank must comply with both WAEMU monetary regulations and OHADA business-law requirements. The two regimes do not always speak to each other cleanly. The book mentions OHADA when relevant, without lecturing.

---

## Places

- **Niamey.** The capital of Niger. The book's primary setting. The bank is in central Niamey. Amina lives in a residential neighborhood somewhat outside the center.
- **Dakar.** Senegal's capital. Where BCEAO is headquartered. Where Amina studied. Mentioned several times.
- **Tunis.** Where the methodologist comes from. Mentioned once or twice; the book does not visit Tunis.
- **Paris.** Mentioned only in passing. The methodologist sometimes works from there.
- **Ouagadougou, Bamako, Abidjan.** Other WAEMU capitals. Mentioned when context calls for them.

The book does not lecture readers about West African geography. Place names appear with context but without exposition.

---

## Things to keep consistent

- **Currency.** CFA franc throughout. Never "$." If amounts are referenced (rarely), they're in CFA francs.
- **Dates.** Months in lowercase. The narrative present is loosely "the 2020s," with specific years (2024, 2025, 2026) only when needed.
- **Language.** Characters speak French in scene; the book translates their dialog into English for the reader, with occasional French phrases retained for atmosphere (*"Bonjour, Madame Bello,"* the auditor said).
- **Honorifics.** The auditor addresses Amina as "Madame Bello." The team addresses her as "Amina." The CIO addresses her as "Amina." She addresses the methodologist as *"vous"* in French — the formal you — even after months of work together.
- **Religion and politics.** Mentioned only when relevant to story. The book does not have a political position on West African geopolitics; it is a book about a bank's software discipline.
