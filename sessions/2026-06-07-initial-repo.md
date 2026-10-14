# Session note — 2026-06-07 — Initial repo setup

## What was built in this session

The book's web reader and supporting repo, starting from a blank slate and iterating across six HTML versions before settling on the structure to commit to source control.

### HTML reader iterations

| Version | Format | Outcome |
|---|---|---|
| v1 | Paginated 6×9 reader app with spread view and page-flipping | Too app-like; Mansour wanted plainer |
| v2 | Same family with spread/flip animation + zoom controls | Same direction, more polish — still too app-like |
| v3 | Plain HTML book in Crafting-Interpreters / Eloquent JavaScript / mdBook lineage | Right direction; needed more refinement on logo and color |
| v4 | Plain HTML with Archivo Black AYOUNI logo (dot above I), monochrome interior, cover stroke, 22px default body | Locked the typography and color rules |
| v5 | Adopted 37signals Writebook ergonomics: library breadcrumb, chapter-card overview, sidebar TOC with leader-dot lines | Locked the format and navigation |
| v6 | Cover swapped from inline SVG (lilac-breasted roller) to external `cover.png` (giraffe in patchwork coat); CSS-rendered cover stroke removed since the new PNG carries its own | Shipped as the current canonical web reader |

### Repo structure created

```
ayouni-rop/
├── CLAUDE.md                          # session-continuity anchor
├── README.md
├── BOOK.md                            # canonical TOC
├── LICENSE.md
├── .gitignore
├── manuscript/                        # Markdown source-of-truth
│   ├── 00-front-matter/   (dedication, epigraph, copyright, contents)
│   ├── 01-what-broke/     (chapter 1: _opener + 4 sections)
│   └── 99-end-matter/     (end-of-preview)
├── web/                               # the HTML reader (v6 snapshot)
│   ├── index.html
│   ├── cover.png                      # PLACEHOLDER: Mansour to drop in
│   └── README.md
├── docs/                              # design + writing + publishing docs
│   ├── design-system.md
│   ├── writing-style-guide.md
│   ├── publishing-plan.md
│   ├── chapter-plan.md
│   └── characters-and-grounding.md
├── assets/
│   ├── illustrations/
│   │   ├── fig-1-1-bceao-letter.svg
│   │   ├── fig-1-2-cascade.svg
│   │   └── README.md
│   └── covers/
│       └── README.md
└── sessions/
    └── 2026-06-07-initial-repo.md     # this file
```

## Decisions locked this session

These now live as hard constraints in `CLAUDE.md` and should not be relitigated:

1. The book is plain HTML in the 37signals Writebook format, not a reader app with page-flipping.
2. AYOUNI wordmark is Archivo Black with a CSS-rendered (or SVG-rendered) dot above the I; solid black in the interior, custom treatment on the cover.
3. The interior is monochrome — color only on cover and inside figures.
4. The cover image carries its own stroke; CSS never adds a border to the cover.
5. Default body size is 22px on screen (reader-adjustable 18–30 in 7 steps).
6. The HTML is single-file and self-contained, deployable by uploading two files.
7. Chapter cards in the overview match Writebook ergonomics: paragraph excerpt with fade-out, bold sans title, sans-serif word count, hover-darken border.
8. Sidebar TOC uses dotted leader lines extending from each chapter title to the column edge.
9. Hash routing: `#` for overview, `#section-slug` for chapter view.
10. Print stylesheet handles the conversion to PDF; no separate Pandoc step yet.

## What is in `web/cover.png`

Mansour to drop the giraffe cover artwork there. The HTML references it via `<img src="cover.png" alt="..." class="cover-img">` and the CSS scales it responsively. Until the file is present, the reader will show a broken image placeholder in the hero — drop the PNG in to fix.

## What's next

In rough priority order (also captured in `CLAUDE.md`):

1. Drop the actual `cover.png` into `web/` so the reader is complete.
2. Draft Chapter 2 (The unit changed) in `manuscript/02-unit-changed/`.
3. Draft Chapter 10 (Sonibank Niger) in `manuscript/10-sonibank-niger/` — high priority since it grounds Parts Two and Three.
4. Once Chapter 2 or Chapter 10 is drafted, sync `web/index.html` to include it (manually, until a build step exists).

## Working pattern going forward

The recommended pattern is:

- **Prose work** happens in `manuscript/`. Edit Markdown files. Commit prose changes there.
- **Design and layout work** happens in `web/index.html` and `docs/design-system.md`. Keep them in sync.
- **At milestones** (e.g., end of a chapter draft), sync the new content from `manuscript/` into `web/index.html` so the reader is current.
- **Each session** adds a short note in `sessions/YYYY-MM-DD-{topic}.md` so the next session inherits the trail.

The repo as it stands today is the working base for everything that follows.
