# Illustrations

Standalone SVG figures used in the book. These are extracted from `web/index.html` and kept here as reusable assets — they can be edited independently, reused in other formats (PDF, ePub, print), or commissioned for replacement.

## Catalog

| File | Used in | Description |
|---|---|---|
| `fig-1-1-bceao-letter.svg` | §1.1 The Q3 letter | The BCEAO directive letter resting on a desk, with an inkwell and pen. Warm sepia palette with a red wax seal. |
| `fig-1-2-cascade.svg` | §1.2 What was new | The cascade diagram: a red central node (`penalty_cap` changing from 0.20 to 0.16) with green nodes radiating outward (14 directly affected loan products) and lighter-green dots beyond (downstream modules). |

## Editing

The SVGs are hand-authored, kept compact (under 4 KB each), and use no external resources. Open in any vector editor — Inkscape, Illustrator, Figma — or edit XML directly.

## Synchronization

If a figure is edited here:

1. Update the standalone `.svg` file.
2. Inline the updated SVG into `web/index.html` (replacing the existing `<svg>` block inside the appropriate `<figure>`).
3. Update `assets/illustrations/README.md` if the description changes.

The standalone files and the inline-in-HTML figures must stay in sync. There is no automated build step yet; this is a manual discipline.

## License

These illustrations are released under **CC BY-NC-SA 4.0** (see `LICENSE.md` at repo root). If you adapt them, share alike.

## Future figures

Chapter 2 onward will need additional figures. Likely candidates:

- A text diff next to a refinement (Chapter 2)
- The codebase-as-graph visualization (Chapter 3)
- The revalidator's flow (Chapter 4)
- The cascade UI surface (Chapter 5)
- The four-agent attribution model (Chapter 6)
- The five-surfaces / one-engine architecture (Chapter 8)
- The agentic-stack map (Chapter 14)

Add SVGs to this folder as they are produced. Number them `fig-N-M-slug.svg` matching the chapter and figure within chapter.
