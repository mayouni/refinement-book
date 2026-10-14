# Publishing Plan — Refinement-Oriented Programming

How the book reaches readers. The strategy, the channels, the practicalities.

---

## Strategy in one paragraph

The book is published independently by Mansour Ayouni under his **AYOUNI** imprint. The free digital edition is the primary distribution; print is a secondary channel for readers who want a physical copy. No advance, no publisher, no agent. The book funds itself through optional pay-what-you-want PDFs and the modest print margin. The goal is reach and durability, not revenue.

---

## Editions

### Web edition (canonical, free)

**Where:** `ayouni.press/refinement-oriented-programming/`
**Format:** Single-file HTML with linked PNG cover. Plays in any modern browser, including phones.
**Source:** `web/index.html` and `web/cover.png` in this repo.
**Maintenance:** Updated at chapter milestones. The web edition is the live edition — what readers find when they land on the site at any moment is the current state of the book.

### PDF edition (free)

**Format:** A4 and 6×9 versions, both produced from the HTML reader's print stylesheet.
**Generation:** Open `web/index.html`, press print, "Save as PDF." That's it.
**Distribution:** Downloadable from `ayouni.press`. Pay-what-you-want via a Stripe / Lemonsqueezy / Buy Me a Coffee widget; $0 is a valid choice and unguilted.

### ePub edition (free, eventual)

**Format:** Standard ePub3 with embedded fonts.
**Generation:** Pandoc with a custom epub template (deferred until manuscript is complete).
**Distribution:** Downloadable from `ayouni.press`. Same pay-what-you-want model as PDF.

### Print edition (paid, modest margin)

**Channel:** IngramSpark print-on-demand.
**Trim:** 6 × 9 inches, perfect-bound paperback, possibly a hardcover variant later.
**Distribution:** Available worldwide through IngramSpark's wholesale network. Mansour orders no inventory; books are printed on demand.
**Cover:** Wraparound cover designed separately (front + spine + back); the giraffe artwork on the front, AYOUNI back-cover treatment with blurb, barcode, and ISBN.
**Price:** TBD. Target cover price covers IngramSpark printing cost + a modest margin (likely $18–22 USD trade paperback range).

---

## ISBN

Mansour to acquire a small ISBN block from Bowker (US) or the relevant national agency. Recommend purchasing 10 at once — cheaper per ISBN, and the AYOUNI imprint will use them for future titles (Ring book, Zin language, etc.).

ISBN gets registered with:
- Bowker / Books in Print
- IngramSpark distribution
- Library of Congress (optional, for catalog inclusion)
- Google Books, Amazon, et al. — handled via IngramSpark's distribution

---

## Marketing and reach

### Primary channels

1. **Direct readership** through `ayouni.press` and Mansour's network in the WAEMU programming and compliance communities.
2. **Word of mouth** in the regulated-software industry: banking, insurance, telecoms, government.
3. **Hacker News and Lobsters submissions** at the right moments — Chapter 1's argument is HN-shaped if framed well; subsequent chapters less so.
4. **Conference talks** in 2026 and 2027: AfricaTech, BCEAO programming community events, FOSDEM dev rooms, EU compliance/regtech conferences.
5. **Translations** — French edition is plausible (Mansour can produce it himself), opens distribution to all francophone Africa + France.

### Things not pursued

- **No celebrity endorsements or blurb-chasing.** The book stands on its grounding.
- **No SaaS partnership promotion.** No vendor pays for placement.
- **No Twitter/X marketing campaign.** Mansour's voice is preserved by not doing this.
- **No paid social media advertising.** Reach earned, not bought.
- **No early publishers' pitches.** AYOUNI is the publisher.

---

## Pricing

| Edition | Price |
|---|---|
| Web reader | Free |
| PDF download | Pay what you want, $0 valid |
| ePub download | Pay what you want, $0 valid |
| Print paperback | $18–22 USD (set to cover print cost + modest margin) |
| Print hardcover (eventual) | $30–35 USD |

No subscription. No DRM on any edition. The CC license precludes commercial redistribution but allows free sharing.

---

## Schedule

The schedule is illustrative; the actual schedule depends on the manuscript's pace, which is set by Mansour's other work.

| Milestone | Target | Status |
|---|---|---|
| Preview edition (Ch. 1 + front matter) | Q2 2026 | DONE |
| Chapter 2 + revised preview | Q3 2026 | not started |
| Chapter 10 (Sonibank case) drafted | Q3 2026 | not started |
| Chapter 11 drafted | Q4 2026 | not started |
| Half the manuscript drafted | Q1 2027 | aspirational |
| Full manuscript drafted | Q3 2027 | aspirational |
| First edition published | Q4 2027 or Q1 2028 | aspirational |

The aspirational dates are private. Public communications about the book do not commit to a publication date until the manuscript is at least 75% drafted.

---

## Future AYOUNI catalogue

Refinement-Oriented Programming is **Book One**. Likely successors:

1. **The Ring Programming Language** — a fresh, AYOUNI-owned book on Ring (replacing the Apress edition, which is now several years old and tied to a publisher Mansour does not own).
2. **The Zin Language** — a book-length account of the Zin organizational programming language.
3. **Patient Software** — a memoir-style book on three decades of building business software in Tunisia, Niger, France, and North America.
4. **StzEngine** — a deep dive into the Zig-backed runtime.

The AYOUNI design system established for Book One scales to all of these. The interior typography stays consistent. Covers vary in artwork but share the wordmark treatment.

---

## Honest boundaries

**What is known.** The publishing model and licensing are set. The technical path to production (HTML → PDF → IngramSpark) works. The web reader is live-ready. The book has a real publication target audience and real distribution channels.

**What is not yet known.**

- The actual market response. The book may find 100 readers or 10,000.
- The price point that works. $20 paperback is a hypothesis.
- Whether ePub is worth producing or whether PDF + web is enough.
- Whether the French edition happens. Likely yes; not committed.
- Whether AYOUNI eventually publishes books by other authors. Currently no; remains open.

**What is deliberately out of scope.**

- Selling the book to a traditional publisher. Decision locked: no.
- Audiobook production. Decision deferred.
- Translations into languages other than French. Open but not planned.
- Sequels or revised editions. Not until 5+ years after publication, if at all.
