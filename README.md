# Refinement-Oriented Programming — AYOUNI Book One

The working repository for **Refinement-Oriented Programming**, the first book from the AYOUNI imprint.
By Mansour Ayouni. Tunis · Niamey · Paris · 2026.

> Read [`CLAUDE.md`](CLAUDE.md) first if you are starting a new Claude Chat session on this project.

---

## What's in here

| Path | Purpose |
|---|---|
| [`CLAUDE.md`](CLAUDE.md) | Durable working memory: locked decisions, hard constraints, current state. Read first. |
| [`BOOK.md`](BOOK.md) | Master manuscript outline (canonical TOC). |
| [`LICENSE.md`](LICENSE.md) | License terms in full. |
| [`manuscript/`](manuscript/) | Book content as Markdown source. One file per section. |
| [`web/`](web/) | Single-file HTML reader (`index.html`) + cover image. Deployable as-is to ayouni.press. |
| [`docs/`](docs/) | Design system, writing style guide, publishing plan, chapter plan, characters sheet. |
| [`assets/`](assets/) | Reusable illustration SVGs and cover artwork variants. |
| [`sessions/`](sessions/) | Per-session notes from Claude Chat work. |

---

## Quick start

### Read the current preview locally

```
open web/index.html
```

The book loads with the giraffe cover, the overview grid of nine chapter cards, and Chapter 1 fully readable across four sections. Navigate by clicking cards or using the keyboard (← / → between chapters, Esc back to overview).

### Deploy to ayouni.press

```
# upload these two files to the web root for the book:
web/index.html  →  ayouni.press/refinement-oriented-programming/index.html
web/cover.png   →  ayouni.press/refinement-oriented-programming/cover.png
```

No build step. The HTML is self-contained except for Google Fonts (loaded via CDN) and the local `cover.png`.

### Print the preview as a PDF

1. Open `web/index.html` in a browser.
2. Click the print icon in the top-right toolbar (or `Ctrl/Cmd+P`).
3. Save as PDF with default settings.

The print stylesheet handles the conversion: toolbar and sidebar hidden, all chapter pages flow with page breaks, asides become inline blocks, 0.7in margins, 11pt body. The output PDF is your free download for ayouni.press and your IngramSpark print master.

---

## License

- **Text:** Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 (`CC BY-NC-ND 4.0`)
- **Illustrations:** Creative Commons Attribution-NonCommercial-ShareAlike 4.0 (`CC BY-NC-SA 4.0`)
- **Code listings, RFN grammar, ROM reference:** MIT License

Full terms in [`LICENSE.md`](LICENSE.md).

---

## Working on the book in a new Claude Chat session

1. Open this repo in Claude Chat desktop as a project.
2. The session reads `CLAUDE.md` and inherits all decisions and constraints.
3. Skim `BOOK.md` to remember the manuscript outline.
4. Edit prose in `manuscript/`. Edit design in `docs/design-system.md`. Edit publishing in `docs/publishing-plan.md`.
5. Update `web/index.html` at milestones (e.g., after a new chapter is drafted).
6. Drop a short note in `sessions/YYYY-MM-DD-{topic}.md` describing what was done.
