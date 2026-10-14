# Design System — AYOUNI Book One

The visual system for *Refinement-Oriented Programming* and the AYOUNI imprint generally. This document is the source of truth for typography, palette, layout, and brand decisions.

---

## Imprint identity

**AYOUNI** is the publishing imprint of Mansour Ayouni / Softanza Labs. The wordmark has its own treatment in two contexts:

| Context | Style |
|---|---|
| Cover image (`cover.png`) | Custom artwork — currently a green-to-red gradient in Archivo Black with a dot above the I |
| Interior (HTML reader, all surfaces) | Solid black Archivo Black with a CSS-rendered dot above the I |

The interior wordmark is the canonical wordmark for the brand. The cover treatment is the artistic interpretation. Future covers may iterate on the wordmark presentation; the interior wordmark stays stable.

### HTML implementation of the interior wordmark

```html
<span class="ayouni">AYOUN<span class="i-dot">I</span></span>
```

```css
.ayouni {
  font-family: 'Archivo Black', 'Helvetica Neue', Arial, sans-serif;
  letter-spacing: -0.01em;
  display: inline-block;
  line-height: 1;
}
.ayouni .i-dot { position: relative; }
.ayouni .i-dot::before {
  content: '';
  position: absolute;
  width: 0.16em;
  height: 0.16em;
  border-radius: 50%;
  background: currentColor;
  top: -0.30em;
  left: 50%;
  transform: translateX(-50%);
}
```

This scales with font size. Use it whenever the AYOUNI wordmark appears in the HTML reader.

---

## Typography

Three typefaces, all freely licensed via Google Fonts.

| Family | Role |
|---|---|
| **EB Garamond** | Body text (serif). All prose, asides, figure captions, dedication, epigraph. |
| **Inter** | UI chrome (sans-serif). Toolbar, sidebar, breadcrumb, chapter titles in the Writebook view, eyebrows, navigation, word counts, numerical indicators. |
| **Archivo Black** | Display (heavy geometric sans). Only the AYOUNI wordmark. |

### Body sizing

- **Default screen body:** 22px EB Garamond, line-height 1.7
- **Reader-adjustable range:** 18px / 20px / 22px / 24px / 26px / 28px / 30px (7 steps)
- **Mobile default (≤600px):** 19px
- **Print body:** 11pt

The default sits comfortably above the 16px web standard and below print-book size. Larger by deliberate choice — Mansour's hard-constraint preference.

### Display sizing

- Hero title (overview): 52px Inter 800
- Chapter title (chapter view): 44px Inter 800
- Section heading (in body): 28px EB Garamond italic 500
- Subsection eyebrow: 12px Inter 700, letter-spacing 3px, uppercase

### Numerical indicators

Counts, statistics, totals, page numbers, word counts, ratios — **always sans-serif (Inter), never the display serif**. Carryover hard constraint from the Refine design system. Color: black.

---

## Color

**Interior is monochrome.** Body text, headings, navigation, sidebar — all rendered in a single ink family. The only colors permitted in the book interior are inside the cover image and inside figure illustrations (where color may carry semantic meaning).

### Interior palette

| Token | Hex | Use |
|---|---|---|
| `--ink` | `#1a1612` | Primary text, headings, AYOUNI wordmark, active states |
| `--ink-soft` | `#3a3326` | Secondary body, soft text |
| `--soft` | `#6b6358` | Tertiary text, captions, metadata |
| `--soft-2` | `#9a9078` | Quaternary text, leader dots |
| `--paper` | `#ffffff` | Card backgrounds, page backgrounds |
| `--bg` | `#fbfaf6` | Page surround (warm off-white) |
| `--rule` | `#e3ddc9` | Dividers, card borders |
| `--hover-bg` | `#f3eedf` | Hover states |
| `--sidebar-bg` | `#f5f0e2` | Sidebar tint (warm cream), aside backgrounds |
| `--bookmark` | `#E96A1A` | Reader-position bookmark indicator only |

### Cover palette (per cover.png — current giraffe variant)

Cover image carries its own palette. Current cover uses warm earth tones (giraffe coat: oranges, browns, with colored patches in violet, teal, emerald, and amber). The wordmark on the cover transitions from emerald green to brick red.

The cover palette is intentionally distinct from the interior palette. The cover is the imprint's visual identity statement; the interior is the reading experience.

### Figure palette

Figures may use color where it conveys meaning. In Chapter 1:

- **Fig. 1.1** (BCEAO letter): warm sepia desk, navy inkwell, red wax seal (`#B83838`), cream paper. Realistic illustration.
- **Fig. 1.2** (cascade diagram): red central node (`#B83838`) = the change. Forest-green nodes (`#2F6B3A`) = directly affected products. Lighter green dots (`#7FC272`) = further downstream. Color is semantic; do not strip it.

Figures may not introduce yellow or yellow-orange (hard constraint).

---

## Layout

### Reading column

Body text column is **`max-width: 36em`** (~684px at default 22px). This is the comfortable reading width; broader lines fatigue the eye and break the book's quiet register.

### Overview view (book landing page)

- Maximum container width: **1280px**
- Hero: cover image (280–360px wide) on left, book metadata on right
- Chapter grid: 4 columns desktop, 3 at 1100px, 2 at 900px, 1 at 600px

### Chapter view (reading)

- Sidebar: **300px** wide on desktop, fixed to viewport, with cream tint (`--sidebar-bg`)
- Main content: 36em max-width centered in the remaining column
- Mobile: sidebar collapses to a slide-in panel triggered by the toolbar hamburger

### Spacing

The system uses generous whitespace by default. Paragraphs separated by 22px (1em at default body size). Sections separated by 56px between heading and prior paragraph. Chapter blocks have 88px top margins.

### Print

- Page size: **6 × 9 inches** (standard trade paperback)
- Margins: 0.7 inch all sides
- Body: 11pt EB Garamond
- Chapter titles: 26pt Inter 800
- Each chapter page-break-before; cover on its own page

---

## Components

### Cards (chapter cards in overview)

- Background: `--paper` (`#fff`)
- Border: 1px solid `--rule`
- Border radius: 6px
- Hover: border darkens to `--ink`, lifts 2px, gains soft shadow
- Preview text: serif 15px with bottom mask fade
- Card title: Inter 700 21px
- Word count: Inter 400 15px in `--soft`

### Asides

- Background: `--sidebar-bg`
- Left border: 3px solid `--ink`
- Padding: 18px 22px
- Border radius: 0 4px 4px 0
- Header: Inter 700 11px uppercase, letter-spacing 2.5px

### Buttons (circular header buttons)

- Size: 38 × 38px
- Border: 1px solid `--rule`
- Radius: 50%
- Background: `--paper`
- Hover: `--hover-bg` background, `--ink` border
- Icon: 17 × 17px inline SVG, stroke 2.2px

### Sidebar links (Writebook-style with leader dots)

```html
<a class="sidebar-link" href="#slug">
  <span class="sl-text">Chapter Title</span>
  <span class="sl-leader"></span>
</a>
```

The leader is a flex-grow div with `border-bottom: 1px dotted var(--soft-2)`. Active link's leader fades to opacity 0 and text bumps to weight 700.

---

## Hard constraints (recap from CLAUDE.md)

1. No yellow colors.
2. No CSS-rendered border on the cover image (the cover.png carries its own).
3. No drop caps in the Writebook layout (they belong to the older paginated layout that we moved away from).
4. AYOUNI wordmark in body text is always solid black, never gradient.
5. Numerical indicators are sans-serif (Inter), never the display serif.
6. The word "substrate" never appears in any design notes, documentation, manuscript, or interface label.

---

## Open questions

These are design decisions not yet locked. They will be made when the manuscript matures.

- **Headers in print:** running heads (book title left, chapter title right) — likely yes, but not yet wired in.
- **Footnotes vs asides:** the book currently uses inline asides. If technical depth in Chapters 4–9 requires footnotes, the layout will need a footnote treatment. Not yet designed.
- **French edition typography:** if a French translation happens, the typography needs to handle French smart-quotation conventions and slightly different line-break rules. Deferred.
