#!/usr/bin/env python3
"""
figpanels.py — the CLI-panel generator for the Teaching Edition.

Every terminal figure in the book is generated from a spec here, so all panels
share one geometry, one palette, and one typography (docs/teaching-edition-plan.md §7).
Panels render the illustrative `stz` sessions — the open Softanza foundation's
machinery in idealized command form (flagged once in the book's front matter).

Usage:
    python web/figpanels.py            # writes every panel to assets/illustrations/cli/
    from figpanels import render        # returns the SVG string for inlining (figures.py)

Palette (matches the reader's code-listing style; no yellow anywhere):
    bg #211c15 · border #35302a · titlebar #2a241c · text #e8e1d1 · dim #8d8471
    prompt/keyword orange #f0914f · ok green #9fc98f · fail red #e0796a · num teal #82c0ae
"""
import html, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUTDIR = ROOT / "assets" / "illustrations" / "cli"

# ---------------------------------------------------------------- geometry
FONT = "Consolas, Menlo, 'DejaVu Sans Mono', monospace"
FS = 14.5          # font size
LH = 24            # line height
PAD_X = 26
PAD_TOP = 18       # below the title bar
PAD_BOT = 22
BAR_H = 38         # title bar height
CHAR_W = FS * 0.602  # monospace advance approximation (warn-only check)

COLORS = {
    "prompt": "#f0914f",   # the ❯ prompt
    "cmd":    "#e8e1d1",   # the typed command
    "flag":   "#82c0ae",   # option flags / values in a command
    "out":    "#cfc7b5",   # ordinary output
    "field":  "#f0914f",   # structural field labels in output
    "ok":     "#9fc98f",   # passing / landed
    "fail":   "#e0796a",   # refusing / failed
    "dim":    "#8d8471",   # comments, hints, de-emphasis
    "num":    "#82c0ae",   # numbers / ids
}

# ---------------------------------------------------------------- line helpers
def cmd(text, note=None):
    """A typed command line: orange prompt + light command (+ dim trailing note)."""
    segs = [("prompt", "❯ "), ("cmd", text)]
    if note:
        segs.append(("dim", "   " + note))
    return segs

def out(text, kind="out"):
    """One output line in a single color kind."""
    return [(kind, text)]

def seg(*pairs):
    """A line of explicit (kind, text) segments, for mixed-color output."""
    return list(pairs)

def blank():
    return []

# ---------------------------------------------------------------- the panels
PANELS = {
    # Chapter 3 — the first session (the proof-of-concept panel for the program)
    "cli-first-session": {
        "title": "stz — your first refinement",
        "lines": [
            cmd("stz lift pricing.py"),
            seg(("out", "lifted "), ("num", "214"), ("out", " nodes into the graph "), ("dim", "· parser: python (its own ast)")),
            blank(),
            cmd("stz points"),
            seg(("field", "  vat_rate     "), ("out", "param   "), ("num", "0.18"), ("out", "   bounds "), ("num", "0.00..0.25")),
            seg(("field", "  rounding     "), ("out", "algo    "), ("out", "banker's   "), ("dim", "2 alternatives declared")),
            seg(("field", "  penalty_cap  "), ("out", "param   "), ("num", "18"), ("out", "     bounds "), ("num", "10..20")),
            blank(),
            cmd("stz refine vat_rate --to 0.20"),
            seg(("out", "proposal "), ("num", "rfn-0114"), ("out", " recorded "), ("dim", "· a typed proposal, not a diff")),
            blank(),
            cmd("stz cascade"),
            seg(("out", "3 nodes revalidate: "), ("field", "pricing.quote"), ("out", " · "), ("field", "invoice.total"), ("out", " · "), ("field", "tests/pricing")),
            blank(),
            cmd("stz apply"),
            seg(("ok", "  structural   pass"), ("dim", "   python re-validated the file")),
            seg(("ok", "  constraint   pass"), ("dim", "   0.20 within declared bounds")),
            seg(("ok", "  derivation   pass"), ("dim", "   cascade verdicts unchanged elsewhere")),
            seg(("ok", "  governance   pass"), ("dim", "   author authorized for this point")),
            seg(("ok", "landed."), ("out", " reversible "), ("dim", "· stz revert undoes it atomically")),
        ],
    },

    # Chapter 3 — asking before touching
    "cli-explain": {
        "title": "stz — ask before you touch",
        "lines": [
            cmd("stz explain vat_rate"),
            seg(("field", "  kind      "), ("out", "param")),
            seg(("field", "  value     "), ("num", "0.18")),
            seg(("field", "  bounds    "), ("num", "0.00..0.25"), ("dim", "    declared in pricing.py:41")),
            seg(("field", "  policy    "), ("out", "DGI-2024-7 "), ("dim", "“VAT stays within the legal band”")),
            seg(("field", "  history   "), ("num", "3"), ("out", " refinements "), ("dim", "· last: amina@sonibank, 2026-03-12")),
            seg(("field", "  cascade   "), ("num", "3"), ("out", " nodes would revalidate")),
        ],
    },

    # Chapter 4 — the lift on a whole module
    "cli-lift": {
        "title": "stz — the lift: code enters the graph",
        "lines": [
            cmd("stz lift lending/"),
            seg(("out", "  pricing.py     "), ("ok", "lifted"), ("out", " · "), ("num", "214"), ("out", " nodes    "), ("dim", "parser: python")),
            seg(("out", "  risk.py        "), ("ok", "lifted"), ("out", " · "), ("num", "178"), ("out", " nodes    "), ("dim", "parser: python")),
            seg(("out", "  policy.py      "), ("ok", "lifted"), ("out", " · "), ("num", "61"), ("out", " nodes     "), ("dim", "parser: python")),
            seg(("out", "  tests/         "), ("ok", "lifted"), ("out", " · "), ("num", "93"), ("out", " nodes     "), ("dim", "parser: python")),
            blank(),
            seg(("field", "graph"), ("out", "   "), ("num", "546"), ("out", " nodes · "), ("num", "1,312"), ("out", " edges · "), ("num", "9"), ("out", " refinement points declared")),
            seg(("field", "note"), ("out", "    2 annotations reference policies not yet in the graph")),
            seg(("dim", "         → stz points --missing to list them")),
        ],
    },

    # Chapter 5 — a landing verdict (the canon Sonibank change)
    "cli-verdict-pass": {
        "title": "stz — a verdict that lands",
        "lines": [
            cmd('stz refine penalty_cap --to 16 --reason "BCEAO circular 2026-Q3"'),
            seg(("out", "proposal "), ("num", "rfn-0207"), ("out", " recorded · author amina@sonibank")),
            blank(),
            cmd("stz apply"),
            seg(("ok", "  structural   pass"), ("dim", "    python re-validated 14 files")),
            seg(("ok", "  constraint   pass"), ("dim", "    16 within declared bounds 10..20")),
            seg(("ok", "  derivation   pass"), ("dim", "    17 nodes revalidated · verdicts hold")),
            seg(("ok", "  governance   pass"), ("dim", "    amina@sonibank may refine policy/*")),
            seg(("ok", "landed."), ("out", " reversible · audit entry sealed")),
        ],
    },

    # Chapter 5 — a refusal in the four-part grammar
    "cli-verdict-refuse": {
        "title": "stz — a refusal worth reading",
        "lines": [
            cmd("stz refine penalty_cap --to 22"),
            seg(("out", "proposal "), ("num", "rfn-0208"), ("out", " recorded · author kofi@sonibank")),
            blank(),
            cmd("stz apply"),
            seg(("ok", "  structural   pass")),
            seg(("fail", "  constraint   FAIL")),
            seg(("fail", "refused"), ("out", " — nothing changed.")),
            seg(("field", "  what happened  "), ("out", "22 exceeds the declared bound "), ("num", "10..20")),
            seg(("field", "  why            "), ("out", "policy BCEAO-4.2 caps late-payment penalties")),
            seg(("field", "  what to do     "), ("out", "propose within "), ("num", "10..20"), ("out", ", or refine the policy")),
            seg(("out", "                 itself "), ("dim", "(requires compliance authority)")),
            seg(("field", "  learn more     "), ("out", "stz why rfn-0208 · stz explain penalty_cap")),
        ],
    },

    # Chapter 6 — reading a cascade
    "cli-cascade": {
        "title": "stz — the blast radius, before anything lands",
        "lines": [
            cmd("stz cascade rfn-0207"),
            seg(("field", "  depth 1  "), ("num", "14"), ("out", " loan products reprice        "), ("dim", "gates: tests/pricing/*")),
            seg(("field", "  depth 2  "), ("out", "risk_assessment · statement_gen  "), ("dim", "gates: tests/risk/*")),
            seg(("field", "  depth 3  "), ("out", "q3_compliance_report             "), ("dim", "gate: policy/BCEAO-4.2")),
            seg(("field", "  stopped  "), ("out", "4 further nodes unchanged — "), ("ok", "early cutoff")),
            blank(),
            seg(("num", "17"), ("out", " nodes revalidate · nothing lands until "), ("cmd", "stz apply")),
        ],
    },

    # Chapter 7 — the audit chain answering
    "cli-history-why": {
        "title": "stz — the history that answers back",
        "lines": [
            cmd("stz history penalty_cap"),
            seg(("out", "  "), ("num", "rfn-0207"), ("out", "   18 → 16      amina@sonibank    2026-09-30   "), ("ok", "landed")),
            seg(("out", "  "), ("num", "rfn-0163"), ("out", "   20 → 18      amina@sonibank    2025-11-02   "), ("ok", "landed")),
            seg(("out", "  "), ("num", "rfn-0090"), ("out", "   set bounds   methodologist     2025-03-17   "), ("ok", "landed")),
            blank(),
            cmd("stz why rfn-0207"),
            seg(("field", "  proposed  "), ("out", "2026-09-30 14:02 by amina@sonibank")),
            seg(("field", "  reason    "), ("out", "“BCEAO circular 2026-Q3”")),
            seg(("field", "  checked   "), ("out", "4 stages passed · "), ("num", "17"), ("out", " nodes revalidated")),
            seg(("field", "  landed    "), ("out", "2026-09-30 14:06 · inverse stored "), ("dim", "(16 → 18)")),
            seg(("field", "  as of     "), ("out", "in force from 2026-10-01 · recorded 2026-09-30")),
        ],
    },

    # Chapter 9 — wise coding: the system asks
    "cli-wise-coding": {
        "title": "stz — wise coding: the system asks",
        "lines": [
            cmd('stz refine --assist "student savings product"'),
            seg(("field", "stz:"), ("out", " a savings product needs a rate profile. Which shape?")),
            seg(("out", "     "), ("num", "1"), ("out", " fixed rate    "), ("num", "2"), ("out", " tiered by balance    "), ("num", "3"), ("out", " indexed (BCEAO base)")),
            cmd("2"),
            seg(("field", "stz:"), ("out", " tiers need boundaries. Answer with values, a rule — or examples.")),
            cmd("examples: 0 → 2.5   100000 → 3.0   500000 → 3.5"),
            seg(("field", "stz:"), ("out", " induced "), ("num", "3"), ("out", " tiers from your examples")),
            seg(("ok", "     all within policy savings_rate_band ✓"), ("dim", "   nothing guessed, nothing landed")),
            seg(("out", "     proposal "), ("num", "rfn-0233"), ("out", " drafted · "), ("cmd", "stz cascade"), ("out", " to preview")),
        ],
    },
}

# ---------------------------------------------------------------- renderer
def _esc(s):
    return html.escape(s, quote=False)

def render(name):
    spec = PANELS[name]
    lines = spec["lines"]
    width = spec.get("width", 760)
    height = BAR_H + PAD_TOP + LH * len(lines) + PAD_BOT
    maxch = int((width - 2 * PAD_X) / CHAR_W)

    parts = []
    parts.append(
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" '
        f'width="{width}" height="{height}" role="img" aria-label="Terminal session: {_esc(spec["title"])}">')
    # panel + title bar (clipped to the rounded shape)
    parts.append(f'<defs><clipPath id="clip-{name}"><rect x="0" y="0" width="{width}" height="{height}" rx="12"/></clipPath></defs>')
    parts.append(f'<g clip-path="url(#clip-{name})">')
    parts.append(f'<rect x="0" y="0" width="{width}" height="{height}" fill="#211c15"/>')
    parts.append(f'<rect x="0" y="0" width="{width}" height="{BAR_H}" fill="#2a241c"/>')
    for i, c in enumerate(("#5a5248", "#6b6358", "#8d8471")):   # three neutral dots
        parts.append(f'<circle cx="{24 + i * 20}" cy="{BAR_H / 2}" r="5.5" fill="{c}"/>')
    parts.append(
        f'<text x="{width / 2}" y="{BAR_H / 2 + 4.5}" text-anchor="middle" font-family="{FONT}" '
        f'font-size="12.5" fill="#8d8471">{_esc(spec["title"])}</text>')
    # lines
    y = BAR_H + PAD_TOP + LH * 0.72
    for line in lines:
        n = sum(len(t) for _, t in line)
        if n > maxch:
            print(f"  [warn] {name}: line exceeds {maxch} chars ({n}): {(''.join(t for _, t in line))[:60]}...")
        if line:
            spans = "".join(
                f'<tspan fill="{COLORS[kind]}">{_esc(text)}</tspan>' for kind, text in line)
            parts.append(
                f'<text x="{PAD_X}" y="{y:.1f}" font-family="{FONT}" font-size="{FS}" '
                f'xml:space="preserve">{spans}</text>')
        y += LH
    parts.append('</g>')
    parts.append(f'<rect x="0.5" y="0.5" width="{width - 1}" height="{height - 1}" rx="12" '
                 f'fill="none" stroke="#35302a"/>')
    parts.append('</svg>')
    return "\n".join(parts)

def main():
    OUTDIR.mkdir(parents=True, exist_ok=True)
    for name in PANELS:
        svg = render(name)
        path = OUTDIR / f"{name}.svg"
        path.write_text(svg, encoding="utf-8", newline="\n")
        print(f"wrote {path}  ({len(svg)} bytes)")

if __name__ == "__main__":
    main()
