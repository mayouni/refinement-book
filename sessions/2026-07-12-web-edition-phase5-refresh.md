# Session — 2026-07-12 · Web edition refreshed after the manifesto's editorial program (Phases 1–5)

One-shot port, closing the standing backlog. The manifesto in `refine/specs/ROP_MANIFESTO_v0_1.md` went through a
five-phase editorial program (reviewed and executed in the refine repo; plan at
`refine/specs/ROP_MANIFESTO_EDITORIAL_PLAN_v0_1.md`). This session brought the web edition current in one build.

## What changed upstream (summary)

- **Structure:** 20 flat chapters → **18 chapters in five parts** (former Ch 15–17 merged into Ch 15 *Agents, and the
  rest of us*; former 18/19/20 renumbered 16/17/18; five part pages with intros; all cross-references swept).
- **Apparatus:** uniform *"What this chapter has established — and what it has not"* closes on Ch 1–17; a Sonibank
  scene in every chapter; 12 figure callouts + 4 code listings (incl. the RFN pipeline the RFN section never showed);
  spec-pointer endings retired into a *"Further, in the reference corpus"* convention.
- **Content beats** accumulated since the last port: skills governance (Ch 12 §5), enterprise-AI-governance (Ch 6 §9),
  the OpenKB compose-or-govern item + glossary RAG pin (Ch 17 + appendix), the taste/context-advantage section
  (now Ch 4 §6), four-loci + governance-word beats (Ch 17), the OCTO team beat (Ch 10).

## What was done here

1. `web/build.py` patched: `# Part N —` headings are now page boundaries with their own meta (eyebrow "Part N",
   slug `part-n`) — the five part pages render as interstitials in the reader.
2. `manuscript/rop-manifesto.md` replaced with the current manifesto (64,497 words).
3. `python web/build.py` — **28 pages** (preface · start-here · 5 parts · 18 chapters · coda · about · glossary),
   509,736 bytes; run twice, byte-identical (idempotency holds); generator's own checks clean (0 "substrate",
   monochrome body / color only in figures).
4. All six SVG figures still inject correctly — their slug keys (`ch2…`–`ch8…`) were untouched by the renumbering,
   which only moved chapters 15+.
5. `CLAUDE.md` web-edition note updated (20-chapter claim → 18-in-five-parts; apparatus list extended).

## Queued (artwork)

The manuscript now carries 12 figure callouts; 6 map to existing SVGs, **6 are to-draw** (the road/spine, the audit
chain's pointers, one-supervisor-many-sessions, two-agent-kinds-one-gate, the cross-domain cascade, the three
pipelines). The mapping table lives in the refine repo's editorial plan §6.1. Next artwork session should add those
six to `web/figures.py` keyed by their chapter slugs.

## Addendum — reader typography pass (same day)

Author feedback on the reader layout: text stretched full-width, visible sidebar scrollbar, paragraph setting not
book-like, mobile readability. Root cause found: the CSS measured `.chapter-content` but the generated markup never
emits that wrapper (pages are `article.chapter-page` directly), so `--content-max` and all paragraph typography were
dead rules. Fixed in `web/shell.template.html` (so it survives rebuilds):

1. Measure applied to what exists: `.chapter-page.active { max-width: var(--content-max); margin: 0 auto; }` — 36em
   (~70 characters) centered at any viewport.
2. Typography retargeted `.chapter-content p` → `.chapter-page p`: justified with `hyphens: auto`, left-aligned on
   ≤600px. Initially set as print convention (1.5em first-line indent, zero gap); **author then asked for empty
   space between paragraphs**, so the final convention is spaced paragraphs — `margin: 0 0 1em`, no indent (the
   flush-left selector machinery removed as redundant). Author then also asked for the printed-book first-line
   indent back, so the final convention is **both**: `margin: 0 0 1em` + `text-indent: 1.5em` on every paragraph
   (uniform — no flush-left exceptions). Verified: 22px gap + 33px indent at the default 22px size, both scale
   with the font control.
3. Sidebar scrollbar hidden while staying scrollable (`scrollbar-width: none` + `::-webkit-scrollbar { display: none }`).
4. Mobile polish at ≤600px: tighter main padding, figure margins, epigraph size. (The <900px drawer sidebar already
   existed and is unchanged.)
5. Print media rule updated to release the measure on `.chapter-page.active` too.
6. **Sidebar TOC truncation fixed (author feedback):** `.sl-text` was `flex: 0 0 auto`, so long titles were clipped
   at the sidebar edge. Now `flex: 0 1 auto` + `min-width: 0` (titles wrap to a second line; `align-items: flex-end`
   keeps the dotted leader on the last line) and `--sidebar-w` widened 300px → 368px so only the four longest
   titles wrap. Verified: zero clipped titles, content column unchanged.
7. **Part titles prefixed (author request, dash form):** part pages now display "Part N — Title" in the sidebar, breadcrumb,
   prev/next buttons, and search labels (`disp_title` in build.py feeds `data-title` + the sidebar label; the search
   `pageLabel()` part branch now passes the title through untouched). The part page itself keeps eyebrow "Part N" +
   bare title — no doubling.
8. **Section headings + figure captions enlarged (author feedback):** `.subsection-h` (the §N headings) 12px →
   `0.8em` (17.6px at default, scales with the font control), letter-spacing 3px → 2px; `figcaption` 15px →
   `0.82em` (18px), color `--soft` → `--ink-soft`, line-height 1.55; `h4.subsubsection-h` 0.72em → 0.76em +
   ink-soft (build.py EXTRA_CSS). The § prefix was already present on all 146 headings (from the manuscript).
9. **Code listings restyled as real code (author feedback):** `pre` went from cream box + Inter to a dark warm
   editor panel (#211c15, light #e8e1d1 text, ui-monospace stack, 0.7em) with build-time syntax highlighting —
   `highlight_code()` in build.py tokenizes fenced blocks (keywords/fields orange #f0914f, strings sage,
   numbers teal, passed/validated green vs failed red, diff +/- green/red, comments gray italic). Inline prose
   `code` keeps the light pill (needed the more specific `.chapter-page pre code` selector to beat the pill rule).
10. **Hover/active reflow fixed (author feedback):** bolding a title on hover/active made near-fitting ones (Ch 5)
   wrap to a second line. Fix: `build.py` now emits `data-t` on `.sl-text` and CSS renders it as an invisible
   zero-height bold `::after` ghost, so every link is laid out at its bold width from the start; plus
   `--sidebar-w` 368px → 380px (Ch 5 bold needs 290px, the 368px column gave 288px). Verified: bolding any of
   the 28 links produces zero height shift.

Rebuilt twice — byte-identical (505,362 bytes, 28 pages); generator checks clean. Verified in browser at 1500px
(792px centered column, indents/justification correct, no sidebar scrollbar) and at 375px (drawer TOC, readable
left-aligned column).

## Addendum 2 — search feature (same day)

Author request: "Add a search feature in the book." Implemented entirely in `web/shell.template.html` (survives
rebuilds); pure client-side over the 28 `article.chapter-page` elements already in the DOM — no build-time index,
no new files, `build.py` untouched.

- **UI:** a command-palette-style overlay — magnifier `circle-btn` in the header (next to Print), opened also by
  `Ctrl/Cmd+K` or `/`, closed by `Esc` / the Esc chip / clicking the backdrop. Panel: 620px max, card style on the
  existing vars; accent is `--bookmark` orange only (no yellow; body prose stays monochrome — search is chrome).
- **Matching:** lazy-built index of text blocks (`p, li, blockquote, h2–h4, figcaption, pre`, nested-block deduped);
  case- and **diacritics-insensitive** (NFD strip — "aicha" finds *Aïcha*), multi-term AND, ranked by term frequency
  with a heading bonus; top 60 rendered with chapter label ("Chapter N · Title" derived from slug) and a
  `<mark>`-highlighted snippet (highlight mapped back through a normalization offset map so accented matches
  highlight correctly).
- **Navigation:** ↑↓ + Enter or click → hash-routes to the page, scrolls the matched block to center, and flashes it
  (1.8s orange fade, `--bookmark` tint). Esc is handled in capture phase so closing search never also bounces the
  reader back to the library (the reader's own Escape handler).
- **Persistent term highlighting (author request):** jumping to a result now marks every occurrence of the search
  terms in the target chapter (`mark.search-term-hl`, orange tint, diacritics-insensitive via the same offset-map
  walker over text nodes). A floating "Clear highlights ×" pill (bottom center) deactivates them; Esc does too;
  navigating to another chapter auto-clears; hidden in print. Clearing un-marks and `normalize()`s the text nodes
  and invalidates the lazy search index.
- **Results-list polish (author feedback, two rounds):** hits separated by hairline rules; selection vs hover made
  distinct — final scheme per the author: selected line = the full `--hover-bg` beige (#f3eedf), mouse-over = a
  lighter version of it (#f9f6ec); an intermediate orange-tint+bar scheme was rejected.
- Rebuilt twice — byte-identical (517,527 bytes); substrate check clean. Verified in browser: diacritics query,
  multi-word query ("penalty cap", 29 passages), click-through + flash on Ch 2, all shortcuts, mobile 375px
  (full-width panel) and desktop 1500px (centered 620px). Print CSS hides the overlay.
