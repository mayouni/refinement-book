# Covers

The cover artwork for *Refinement-Oriented Programming* and notes on its evolution.

## Current cover

**File:** `web/cover.png` (lives in `web/` so it sits next to the HTML reader for serving; mirrored at
`site/cover.png`). **Final flat artwork installed 2026-07-18** — the clean illustration, no mockup framing;
used as-is on the print edition's cover page (`web/print.py`). The earlier hand-held mockup photo is archived
at `archive/2026-06-handheld-mockup.png`.
**Subject:** A giraffe in patchwork coat, illustrated.
**Wordmark:** AYOUNI in Archivo Black, green-to-red gradient, with a dot above the I.
**Title typography:** Refinement-Oriented Programming in serif (EB Garamond), italic subtitle in slightly muted ink.
**Author byline:** MANSOUR AYOUNI at bottom-left in sans-serif.
**Location and year:** TUNIS · NIAMEY · PARIS · 2026 at bottom-right.
**Stroke:** A thin frame is part of the image itself (no CSS border in the reader).

The giraffe was chosen for grounded reasons: the giraffe is a Sahel animal (the Sahara-Sahel band running through Niger, Mali, and the eastern WAEMU member states) and the patchwork-coat treatment echoes the book's argument that a codebase is a graph of refinements — each patch its own area, each connected to its neighbors.

## Earlier cover concepts (not used)

These were sketched during the cover exploration but not adopted. They are not in this repo; this is a note for context.

- **The fennec fox.** First concept. A small Saharan fox with large ears, common in the desert regions of southern Algeria and northern Niger. Replaced because the fennec read as cute rather than serious — the wrong register for a book about regulated banking software.
- **The lilac-breasted roller.** Second concept. A colorful bird across much of sub-Saharan Africa, dramatic in flight. Implemented as inline SVG in earlier book versions (v1–v5). Replaced because the colorful bird competed visually with the wordmark; the giraffe gives the cover a single strong subject.

## Replacing the cover

To swap in a new cover:

1. Save the new image as `web/cover.png`.
2. No HTML change needed — the reader picks it up automatically.
3. Move the previous cover here to `assets/covers/archive/{date}-{slug}.png` if it deserves keeping.

## Format requirements

- **Dimensions:** between 4:5 (1280×1600) and 2:3 (800×1200). The reader scales responsively.
- **Format:** PNG with embedded sRGB profile. JPEG is acceptable but less crisp at small sizes.
- **File size:** target under 500 KB. Larger is fine but readers on slow connections will notice.
- **Border / stroke:** baked into the image, not added by CSS.

## Artist credit

Cover artist credit goes on the copyright page (`manuscript/00-front-matter/copyright.md`). Update the placeholder text when commissioning final artwork. If the artist permits, link to their portfolio in the same place.
