# Web Reader

The single-file HTML book at `index.html` plus the cover artwork at `cover.png`.

**Edition note.** `index.html` now hosts the **full manifesto edition** — the complete 20-chapter book in the
author's first-person voice (`A manifesto for software in the agentic era`), including the "Start here" reader's
on-ramp, the concept glossary appendix, per-chapter signposts, and a set of explanatory diagrams (one interactive
cascade). It is **generated** from the Markdown manuscript by `build.py`; it is no longer the hand-authored
documentary Chapter-1 preview.

## What's in here

| File | Purpose |
|---|---|
| `index.html` | The book (generated). Self-contained except for Google Fonts (CDN) and `cover.png`. The only deployment artifact. |
| `cover.png` | The cover artwork. Mansour replaces this file directly when iterating on the cover. *(Not committed in this checkout — `COVER_PLACEHOLDER.md` stands in; the reader shows alt text until a real `cover.png` is added.)* |
| `build.py` | Generator: converts `../manuscript/rop-manifesto.md` → `index.html` using the shell template. Run `python web/build.py`. Idempotent. |
| `figures.py` | The custom explanatory diagrams (SVG), including the interactive cascade, injected into specific chapters by `build.py`. |
| `shell.template.html` | The reader's pristine shell (head + styles + routing script) — a build **input**, not a deployment artifact. `build.py` wraps generated content in it. |

The **deployment artifact is still a single self-contained file** (`index.html` + `cover.png`). The `.py` files and
the template are build inputs; they are not uploaded. To regenerate after editing the manuscript: `python web/build.py`.

## How to deploy to ayouni.press

```
# upload both files to the book's web root:
web/index.html  →  ayouni.press/refinement-oriented-programming/index.html
web/cover.png   →  ayouni.press/refinement-oriented-programming/cover.png
```

Done. The book is live.

## How the reader works

The book is a small single-page application implemented in vanilla HTML/CSS/JS.

**Two views**, switched by URL hash:

- **Overview** (default, no hash): cover hero + chapter card grid. The landing experience.
- **Chapter view** (`#section-slug`): sidebar TOC + single-section reading area. Hash routing means each section has its own URL: `ayouni.press/refinement-oriented-programming/#q3-letter`.

**Navigation:**

- Click a chapter card → goes to that chapter
- Click the breadcrumb library icon or book title → returns to overview
- Click ← back arrow → returns to overview
- Click sidebar links → switch chapters
- Click Previous / Next at the chapter footer → step through chapters in order
- Keyboard: ← / → cycle chapters, Esc returns to overview, +/− adjust font size

**Font size:**

Reader-adjustable in 7 steps from 18px to 30px. Default is 22px. Selection persists to `localStorage` so each reader's preference is remembered.

**View mode:**

The overview's chapter grid toggles between grid (default, 4-column cards) and list (single-column rows with title and word count). Selection persists.

**Print:**

The print icon (or `Ctrl/Cmd+P`) triggers the print stylesheet. Toolbar and sidebar hide. All chapter pages flow with `page-break-before`. Asides become inline blocks. 0.7 inch margins, 11pt body. Browser's "Save as PDF" outputs the print PDF.

## Adapting the cover

To replace the cover:

1. Drop the new cover into this folder as `cover.png`.
2. No HTML change needed — the reader's `<img src="cover.png">` will pick it up.
3. If the new cover has its own border / stroke, no further work needed. The CSS does not add a border to the cover image (intentional — the cover.png carries its own visual identity).

Image aspect ratio: ideally between 4:5 (1280×1600) and 2:3 (800×1200). The reader scales it responsively within a max-width of 360px on desktop and 280px on mobile.

## What the reader is *not*

- Not a Vue / React / Svelte app. Vanilla JS.
- Not a static-site-generator output. Hand-authored.
- Not a Pandoc derivative. `build.py` is a small purpose-built Markdown→reader converter; the Markdown manuscript (`../manuscript/rop-manifesto.md`) is the source-of-truth for text content, and `index.html` is generated from it.

That build step now exists (`build.py`). It converts the manuscript Markdown into the reader's article structure, wraps it in the pristine `shell.template.html`, and injects the diagrams from `figures.py`. Re-run it whenever the manuscript changes.

## File size

`index.html` weighs roughly 450 KB (the full 20-chapter manifesto plus inline SVG diagrams). The Google Fonts CSS adds ~30 KB on first load, then cached. The book loads quickly on a modest broadband connection and is fully usable offline once visited. (The single-file weight is the deliberate trade for zero-build, zero-dependency deployment.)

## Browser support

Tested in modern Chromium, Firefox, and Safari (desktop and iOS). Uses standard CSS Grid, Flexbox, and ES2018 JS. No transpilation. No polyfills.
