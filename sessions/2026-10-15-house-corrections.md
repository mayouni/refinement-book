# 2026-10-15 · The house's corrections to the live Teaching Edition

Done in the Softanza book session, on the author's words relayed by the AYOUNI Press house desk (his corrections 2 to 4 and the two false statements; the rewrite of the book is for a dedicated session).

- **Cover** (`web/cover.png`, mirrored at `site/cover.png`): a pure white page, the giraffe unchanged (taken from the archived flat cover, `assets/covers/archive/2026-07-flat-cover-giraffe.png`, its off-white mapped to white), title 78px bold in three lines, subtitle 38px regular and not italic, the AYOUNI logo from `assets/covers/ayouni-logo.png`. Drawn at 2194 x 2868 by `web/make_cover.py` (run it to redraw).
- **The logo** is the house's SVG (`assets/covers/ayouni-logo.svg`, traced from the author's file by the house desk), inlined once in the reader as a symbol (`web/logo-sprite.html`, injected into `web/shell.template.html`), in the header and the hero; the header logo links to https://mayouni.github.io/ayouni/ with the accessible name "AYOUNI Press: home". The PDF's title page and back cover carry its raster.
- **Type**: default reading size 24px (index 3 of the control), body ink #17140f, no label under 14px, card previews 18px. The 18 to 30px range is unchanged.
- **The PDF's two false statements**: the copyright page now reads "The free digital edition is at https://mayouni.github.io/ayouni/books/refinement/en/. Paper copies in quantity are supplied to organisations on request: https://mayouni.github.io/ayouni/offer/." and the back cover's "ayouni.press" is "mayouni.github.io/ayouni" (also in `manuscript/00-front-matter/copyright.md`). The back cover's "author of Beginning Ring Programming (Apress)" is removed (the author's "decide on my behalf", taken by the house desk: Ring is named only in the Softanza book's Appendix H); the bio reads "Mansour Ayouni is the founder of Softanza Labs. He works between Tunis, Niamey, and Paris."
- The standing invitation keeps "If this book is useful to your organisation".

The CLAUDE.md of this book still says, in places, "Default body font size 22px" and "ayouni.press" as the domain: both are superseded by the above and by the house decisions (HOUSE-10 to HOUSE-15); the dedicated rewrite session reconciles the file.

## Later the same day (logo, cover, zoom)

- The logo is the house's corrected SVG (a red dot): `assets/covers/ayouni-logo.svg` and `.png`, the sprite in `web/logo-sprite.html` and in `web/shell.template.html`. One logo per reader page, the header link home; the hero's copy is removed. In the PDF it is on the title page and the back cover and, with the cover, on the cover.
- The cover is the archived flat cover on white with the corrected logo in the old wordmark's place and the type as first designed (`web/make_cover.py`, 2194 x 2868). The larger-type redesign of the morning is not wanted.
- A zoom icon at the cover's lower right opens the cover in a lightbox at full size (`web/build.py`).
