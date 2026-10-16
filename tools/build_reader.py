#!/usr/bin/env python3
"""The rewrite's reader and PDF, built locally from src/en (ROP-11), without touching the live Teaching Edition.

The Teaching Edition's builders (web/build.py, web/print.py) read one Markdown file in a fixed shape and write into web/.
This script assembles that shape from the rewrite's pages, then runs the two builders with their inputs and outputs
redirected, so web/ is never written:

  reader/index.html   the web reader, one self-contained file, with reader/cover.png beside it
  print/print.html    the print composition (6 x 9 in), and print/book.pdf when Chrome and the network are there

What the rewrite adds to each page: its stage banner (HOUSE-18: Draft, In review or Published, read from the page's
front matter, with its meaning on hover; only the author moves a page beyond Draft), the stage lines of its front
matter (built, designed, absent), and under every block the verdict read from data/book-run.json, never composed.
The edition is a proof copy until every page is published; the cover page and the copyright page count pages by stage.
The front and back matter of the PDF are the rewrite's own: the Teaching Edition's back cover described a book that
is no longer this one.

    python tools/build_reader.py          # the reader only
    python tools/build_reader.py --pdf    # the reader, then the print HTML and the PDF
"""
import json, pathlib, re, shutil, sys, types

ROOT = pathlib.Path(__file__).resolve().parent.parent
WEB = ROOT / "web"
EN = ROOT / "src" / "en"
READER = ROOT / "reader"
PRINT = ROOT / "print"
CACHE = ROOT / ".cache"
sys.path.insert(0, str(ROOT / "tools"))
from book_common import sources, LIB_REF  # noqa: E402

PARTS = {1: "The discipline", 2: "The gate, run", 3: "The AI agent at the point",
         4: "Softibank, eighteen months", 5: "Refine, the product and the IDE"}
ROMAN = {1: "I", 2: "II", 3: "III", 4: "IV", 5: "V"}
FENCE = re.compile(r"(?ms)^```haro([^\n]*)\n(.*?)^```[ \t]*$")

# HOUSE-18; the labels and their meanings are the Softanza book's (6bb27a4), word for word
STAGES = ("draft", "review", "published")
LABEL = {"draft": "Draft", "review": "In review", "published": "Published"}
MEANING = {"draft": "Written, its code run and judged, read by fresh readers; awaiting the author's review",
           "review": "The author is reviewing this page; his remarks are being applied",
           "published": "Approved by the author: this is the book's text"}


def stage_of(meta):
    st = meta.get("status", "draft")
    return st if st in STAGES else "draft"


def banner(st):
    return f'<div class="status-banner st-{st}" title="{MEANING[st]}">{LABEL[st]}</div>'


def slugify(t):
    return re.sub(r"[^a-z0-9]+", "-", t.lower()).strip("-")


def page_stages():
    """The builder's slug of each source page -> its stage (the slug rule is web/build.py's)."""
    out = {}
    for _, meta, _b in sources("en"):
        if meta["id"] == "start-here":
            key = "start-here"
        elif meta["id"].startswith("coda"):
            key = "coda"
        elif meta["id"] == "glossary":
            key = "glossary"
        else:
            key = f"ch{meta['number']}-{slugify(meta['title'])}"
        out[key] = stage_of(meta)
    return out


def edition_line(stages):
    counts = {st: list(stages.values()).count(st) for st in STAGES}
    kind = "Published" if counts["published"] == len(stages) else "Proof copy"
    return kind + ": " + ", ".join(f"{counts[st]} {LABEL[st].lower()}" for st in STAGES)


def verdict_line(rec):
    v = rec.get("verdict")
    if v == "exercise":
        return "*An exercise: yours to run. Its answer is not printed.*"
    short = LIB_REF[:9]
    if v == "kept":
        return f"*Ran at `{short}`: the block printed what it promised.*"
    return f"*Ran at `{short}`: {v}.*"


def assemble():
    run = json.loads((ROOT / "data" / "book-run.json").read_text(encoding="utf-8"))
    out, part_seen = [], set()
    for path, meta, body in sources("en"):
        n, title = meta["number"], meta["title"]
        recs = run["chapters"].get(f"en/{path.stem}", {}).get("blocks", [])
        k = [0]

        def mark(m):
            rec = recs[k[0]] if k[0] < len(recs) else {}
            k[0] += 1
            return m.group(0) + "\n\n" + verdict_line(rec)
        body = FENCE.sub(mark, body)
        stage = meta.get("stage") or {}
        stage_md = ""
        if stage:
            lines = []
            for key in ("built", "designed", "absent"):
                if stage.get(key):
                    lines.append(f"- **{key.capitalize()}.** {stage[key]}")
            stage_md = "\n".join(lines) + "\n\n"
        part = meta.get("part")
        if part and part not in part_seen:
            part_seen.add(part)
            chs = [m2 for _, m2, _ in sources("en") if m2.get("part") == part]
            names = ", ".join(f"{m2['number']} {m2['title']}" for m2 in chs)
            out.append(f"# Part {ROMAN[part]} — {PARTS[part]}\n\nChapters {names}.\n")
        if meta["id"] == "start-here":
            out.append(f"## Start here — How to read this book\n\n{body}\n")
        elif meta["id"].startswith("coda"):
            out.append(f"# Coda — The next letter\n\n{stage_md}{body}\n")
        elif meta["id"] == "glossary":
            out.append(f"## Appendix — The words, pinned\n\n{body}\n")
        else:
            out.append(f"# Chapter {n} — {title}\n\n{stage_md}{body}\n")
    CACHE.mkdir(exist_ok=True)
    md = CACHE / "rewrite-book.md"
    md.write_text("\n".join(out), encoding="utf-8")
    return md


def load_builder(md):
    """web/build.py, run with its source and output redirected; returns it as the module `build`."""
    READER.mkdir(exist_ok=True)
    src = (WEB / "build.py").read_text(encoding="utf-8")
    src = src.replace('SRC = ROOT / "manuscript" / ("rop-manifesto.md" if MANIFESTO else "rop-book.md")', f"SRC = pathlib.Path(r'{md}')")
    src = src.replace('OUT = ROOT / "web" / ("manifesto.html" if MANIFESTO else "index.html")', f"OUT = pathlib.Path(r'{READER / 'index.html'}')")
    assert f"r'{md}'" in src and "reader" in src, "web/build.py changed shape; update the redirection"
    mod = types.ModuleType("build")
    mod.__file__ = str(WEB / "build.py")
    sys.path.insert(0, str(WEB))
    sys.argv = [a for a in sys.argv if a != "--manifesto"]
    exec(compile(src, str(WEB / "build.py"), "exec"), mod.__dict__)
    sys.modules["build"] = mod
    return mod


STAGE_CSS = (".status-banner{display:inline-block;font-family:var(--sans);font-size:14px;font-weight:700;letter-spacing:2px;"
             "text-transform:uppercase;padding:5px 10px;border-radius:4px;margin:0 0 1.2em;border:1px solid var(--rule-strong);"
             "color:var(--ink);cursor:help;}"
             ".hero-info .edition-line{font-family:var(--sans);font-size:14px;color:var(--ink);margin:0 0 1em;}"
             ".chapter-page pre{overflow-x:hidden;}.chapter-page pre code{white-space:pre-wrap;overflow-wrap:anywhere;}")
ARTICLE_HEAD = re.compile(r'<article class="chapter-page" id="page-([^"]+)"[^>]*>\n<div class="ch-eyebrow">.*?</div>\n'
                          r'<h1 class="ch-title">.*?</h1>\n<div class="ch-rule"></div>', re.S)


def finish_reader():
    p = READER / "index.html"
    s = p.read_text(encoding="utf-8")
    s = s.replace("</style>", STAGE_CSS + "\n</style>", 1)
    stages = page_stages()

    def put(m):
        st = stages.get(m.group(1))
        return m.group(0) + ("\n" + banner(st) if st else "")
    s = ARTICLE_HEAD.sub(put, s)
    s = s.replace('<p class="hero-author">Mansour Ayouni</p>',
                  f'<p class="hero-author">Mansour Ayouni</p>\n<p class="edition-line">{edition_line(stages)}</p>', 1)
    p.write_text(s, encoding="utf-8")
    shutil.copy2(WEB / "cover.png", READER / "cover.png")
    n = s.count('class="status-banner')
    print(f"reader: {p}  ({len(s)} bytes, {n} stage banners for {len(stages)} pages; {edition_line(stages)})")
    assert n == len(stages), "a page has no stage banner"
    assert "not yet read by the author" not in s


COPYRIGHT = """<div class="fm fm-copyright">
<p>© 2026 Mansour Ayouni</p>
<p>Published by AYOUNI, the independent imprint of Mansour Ayouni / Softanza Labs. Tunis · Niamey · Paris.</p>
<p>The text of this book is released under Creative Commons Attribution-NonCommercial-NoDerivatives 4.0
International (CC BY-NC-ND 4.0). Code follows the licence of the library it runs against. Illustrations and the cover follow the book's LICENSE.md.</p>
<p>This edition rewrites the Teaching Edition of 2026 on the Softanza foundation. Every block was run against the Softanza library at commit {lib}.</p>
<p><strong>{edition}.</strong> The edition is a proof copy until the author has published every page. This is a local build, not a published edition.</p>
<p>Typeset in EB Garamond and Inter. ISBN pending.</p>
</div>"""

BACK_COVER = """<div class="pg-back">
<div class="bb-blurb">
<p><strong>Software is now written faster than anyone can trust it.</strong> When an AI agent can draft in an
afternoon what a team once wrote in a quarter, the slow part of the work is no longer writing a change. It is trusting it.</p>
<p>This book is a discipline for that moment, told through a bank in Niamey that receives a regulator's letter. A change
becomes a refinement: declared where the code may change, proposed in a typed form, judged by a gate of five checks,
recorded as a step, and reversible. Every block in the book runs against an open library, and every chapter says what
is built, what is designed and what is still absent.</p>
<p class="bb-tag"><em>Stop trying to govern the intelligence, and govern the change.</em></p>
</div>
<div class="bb-points">
<div><span>&#9656;</span>The gate, run: five checks, each refusal with its reason</div>
<div><span>&#9656;</span>The AI model last: what an AI agent may touch, and who sets its origin</div>
<div><span>&#9656;</span>For programmers, analysts, and everyone who signs for software</div>
</div>
<div class="bb-author">Mansour Ayouni is the founder of Softanza Labs. He works between Tunis, Niamey, and Paris.</div>
<div class="bb-foot">
<div class="bb-imprint"><img alt="AYOUNI" src="../assets/covers/ayouni-logo.png" style="height:0.34in;width:auto"></div>
<div class="bb-meta">mayouni.github.io/ayouni<br>TUNIS · NIAMEY · PARIS · 2026<br><span class="bb-isbn">ISBN pending</span></div>
</div>
</div>"""

PRINT_BANNER = ('font-family:Inter,sans-serif;font-size:8pt;font-weight:700;letter-spacing:1.5pt;text-transform:uppercase;'
                'border:0.5pt solid #6b6358;padding:2pt 6pt;display:inline-block;margin:0 0 10pt;')


def build_print(mod):
    stages = page_stages()
    for pg in mod.pages:
        st = stages.get(pg["slug"])
        if st:
            pg["body_html"] = (f'<p class="status-banner st-{st}" title="{MEANING[st]}" style="{PRINT_BANNER}">{LABEL[st]}</p>\n'
                               + pg["body_html"])
    PRINT.mkdir(exist_ok=True)
    src = (WEB / "print.py").read_text(encoding="utf-8")
    src = src.replace('OUT_HTML = ROOT / "web" / "print.html"', f"OUT_HTML = pathlib.Path(r'{PRINT / 'print.html'}')")
    src = src.replace('OUT_PDF = ROOT / "web" / "book.pdf"', f"OUT_PDF = pathlib.Path(r'{PRINT / 'book.pdf'}')")
    assert "print.html'" in src and "book.pdf'" in src, "web/print.py changed shape; update the redirection"
    # the rewrite's own front and back matter, replaced after print.py defines its own
    src = src.replace("# --------------------------------------------------------------------------\n# TOC + body from the parsed pages",
                      "COPYRIGHT = _COPYRIGHT\nBACK_COVER = _BACK_COVER\n"
                      "# --------------------------------------------------------------------------\n# TOC + body from the parsed pages", 1)
    assert "_COPYRIGHT" in src
    ns = {"__file__": str(WEB / "print.py"), "__name__": "__main__",
          "_COPYRIGHT": COPYRIGHT.format(lib=LIB_REF[:9], edition=edition_line(stages)), "_BACK_COVER": BACK_COVER}
    shutil.copy2(WEB / "cover.png", PRINT / "cover.png")   # before the render: the composition loads it
    exec(compile(src, str(WEB / "print.py"), "exec"), ns)


def main():
    md = assemble()
    mod = load_builder(md)
    finish_reader()
    if "--pdf" in sys.argv:
        build_print(mod)


if __name__ == "__main__":
    main()
