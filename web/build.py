#!/usr/bin/env python3
"""
build.py — generate web/index.html from manuscript/rop-manifesto.md

Ports the full 20-chapter manifesto into the Writebook-style single-file reader,
preserving the reader's shell (head/styles + routing script) verbatim and
converting the Markdown to the reader's article structure. Injects a curated set
of explanatory diagrams (including one interactive cascade) into specific chapters.

Run:  python web/build.py   (from repo root or anywhere)
Output: web/index.html (single self-contained file — the only deployment artifact)
"""
import re, html, pathlib, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent

# The Teaching Edition (docs/teaching-edition-plan.md) is THE book as of Phase 5
# (2026-07-18): the default build reads manuscript/rop-book.md into web/index.html.
# --manifesto rebuilds the superseded manifesto edition from its retained
# manuscript (the repo is not under git, so the file itself is the record) to a
# separate artifact, web/manifesto.html.
MANIFESTO = "--manifesto" in sys.argv
SRC = ROOT / "manuscript" / ("rop-manifesto.md" if MANIFESTO else "rop-book.md")
SHELL = ROOT / "web" / "shell.template.html"  # pristine shell (head/styles + routing script); a build INPUT
OUT = ROOT / "web" / ("manifesto.html" if MANIFESTO else "index.html")
SUBTITLE = ("A manifesto for software in the agentic era" if MANIFESTO
            else "A discipline for software in the agentic era")

md = SRC.read_text(encoding="utf-8")
orig = SHELL.read_text(encoding="utf-8")

# --------------------------------------------------------------------------
# 1. Extract the verbatim shell pieces from the existing reader
# --------------------------------------------------------------------------
OV_MARK = "<!-- ============ OVERVIEW VIEW ============ -->"
head_header = orig[: orig.index(OV_MARK)]               # <head>+<style>+<body>+header+backdrop
script_tail = orig[orig.index("<script>"):]            # routing script + </body></html>

# --------------------------------------------------------------------------
# 2. Inline + block Markdown conversion
# --------------------------------------------------------------------------
def inline(text):
    text = html.escape(text, quote=False)
    text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)",
                  r'<a href="\2" target="_blank" rel="noopener">\1</a>', text)
    # stash code spans first so their contents (e.g. policy/*) can't pair with
    # emphasis markers elsewhere in the line
    codes = []
    def _stash(m):
        codes.append(m.group(1)); return f"\x00C{len(codes)-1}\x00"
    text = re.sub(r"`([^`]+)`", _stash, text)
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)   # bold (non-greedy: allows inner *italic*)
    text = re.sub(r"\*(.+?)\*", r"<em>\1</em>", text)               # italic
    text = re.sub(r"\x00C(\d+)\x00", lambda m: "<code>" + codes[int(m.group(1))] + "</code>", text)
    return text

def plain(text):
    text = re.sub(r"`([^`]+)`", r"\1", text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"\1", text)
    text = re.sub(r"\*([^*]+)\*", r"\1", text)
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    return text

# syntax highlighting for code listings (RFN, pipelines, verdicts, diffs) —
# token-based so each fragment is escaped individually
CODE_TOKEN_RE = re.compile(r"""
   (?P<diffadd>^\+[^\n]*)
 | (?P<diffdel>^-[^\n]*)
 | (?P<comment>(?:\#|//)[^\n]*)
 | (?P<string>"[^"\n]*")
 | (?P<field>^[ \t]*[A-Z][A-Za-z_ ]*:(?=\s))
 | (?P<kw>^[ \t]*(?:refinement|pipeline|target|from|to|policy|author|reason|gates|
        review_by|must_pass|must_match|description|on_fail|revert_all|stage|verify)\b)
 | (?P<ok>\b(?:passed|validated|applied|PASSED)\b)
 | (?P<bad>\b(?:failed|FAILED|refused)\b)
 | (?P<number>(?<![\w-])\d+(?:/\d+|\.\d+)?%?(?![\w-]))
""", re.M | re.X)

def highlight_code(src):
    out, pos = [], 0
    for m in CODE_TOKEN_RE.finditer(src):
        out.append(html.escape(src[pos:m.start()], quote=False))
        out.append(f'<span class="c-{m.lastgroup}">'
                   f'{html.escape(m.group(0), quote=False)}</span>')
        pos = m.end()
    out.append(html.escape(src[pos:], quote=False))
    return "".join(out)

# figure directive: a paragraph of the form {{fig:slug|Caption text}} becomes an
# inlined SVG figure. cli-* slugs render from figpanels.py; other slugs load
# assets/illustrations/diagrams/<slug>.svg (the checked-in source of truth).
FIG_LEGACY = {  # complete <figure> blocks reused from figures.py (caption/script included)
    "cascade-interactive": "ch5-the-cascade-as-a-working-surface",
    "ide-cascade-facet": "ch8-five-surfaces-one-engine",
}

def figure_html(slug, caption):
    if slug in FIG_LEGACY:
        import figures
        return figures.FIGURES[FIG_LEGACY[slug]]
    if slug.startswith("cli-"):
        import figpanels
        svg = figpanels.render(slug)
    else:
        svg = (ROOT / "assets" / "illustrations" / "diagrams" / f"{slug}.svg").read_text(encoding="utf-8")
    cap = f"<figcaption><strong>Fig.</strong> {inline(caption)}</figcaption>" if caption else ""
    return f'<figure class="book-fig" id="fig-{slug}">{svg}{cap}</figure>'

def render_table(tbl):
    rows = [r.strip().strip("|").split("|") for r in tbl]
    header = [c.strip() for c in rows[0]]
    body = rows[2:]
    th = "".join(f"<th>{inline(c)}</th>" for c in header)
    trs = ""
    for r in body:
        trs += "<tr>" + "".join(f"<td>{inline(c.strip())}</td>" for c in r) + "</tr>"
    return f'<table class="book-table"><thead><tr>{th}</tr></thead><tbody>{trs}</tbody></table>'

def convert_body(body_lines, meta):
    out = []
    n = len(body_lines)
    i = 0
    while i < n and body_lines[i].strip() == "":
        i += 1
    # lede: first single-line italic just under the heading (the chapter signpost)
    if i < n:
        l = body_lines[i].strip()
        if l.startswith("*") and l.endswith("*") and not l.startswith("**") and len(l) > 2:
            out.append(f'<p class="ch-lede">{inline(l[1:-1].strip())}</p>')
            i += 1
    if meta.get("sub") and not any('ch-lede' in o for o in out):
        out.append(f'<p class="ch-lede">{inline(meta["sub"])}</p>')

    para = []
    def flush():
        if para:
            out.append("<p>" + inline(" ".join(x.strip() for x in para)) + "</p>")
            para.clear()

    while i < n:
        line = body_lines[i]
        s = line.strip()
        if s == "":
            flush(); i += 1; continue
        if s == "---":
            flush(); out.append('<div class="divider">· · ·</div>'); i += 1; continue
        # table
        if s.startswith("|") and i + 1 < n and re.match(r"^\|[\s:|-]+\|?$", body_lines[i+1].strip()):
            flush(); tbl = [line]; j = i + 1
            while j < n and body_lines[j].strip().startswith("|"):
                tbl.append(body_lines[j]); j += 1
            out.append(render_table(tbl)); i = j; continue
        # headings
        if s.startswith("### "):
            flush(); out.append(f'<h4 class="subsubsection-h">{inline(s[4:].strip())}</h4>'); i += 1; continue
        if s.startswith("## "):
            flush(); out.append(f'<h3 class="subsection-h">{inline(s[3:].strip())}</h3>'); i += 1; continue
        # blockquote
        if s.startswith(">"):
            flush(); bq = []
            while i < n and body_lines[i].strip().startswith(">"):
                bq.append(body_lines[i].strip().lstrip(">").strip()); i += 1
            # preserve line breaks (verdict-style field lists stay one-per-line)
            out.append("<blockquote>" + "<br>".join(inline(x) for x in bq) + "</blockquote>"); continue
        # figure directive
        mfig = re.match(r"^\{\{fig:([a-z0-9-]+)(?:\|(.*))?\}\}$", s)
        if mfig:
            flush(); out.append(figure_html(mfig.group(1), mfig.group(2))); i += 1; continue
        # code fence
        if s.startswith("```"):
            flush(); i += 1; code = []
            while i < n and not body_lines[i].strip().startswith("```"):
                code.append(body_lines[i]); i += 1
            i += 1
            out.append("<pre><code>" + highlight_code("\n".join(code)) + "</code></pre>"); continue
        # unordered list
        if re.match(r"^[-*]\s+", s):
            flush(); items = []
            while i < n and re.match(r"^[-*]\s+", body_lines[i].strip()):
                items.append(re.sub(r"^[-*]\s+", "", body_lines[i].strip())); i += 1
            out.append("<ul>" + "".join(f"<li>{inline(x)}</li>" for x in items) + "</ul>"); continue
        # ordered list
        if re.match(r"^\d+\.\s+", s):
            flush(); items = []
            while i < n and re.match(r"^\d+\.\s+", body_lines[i].strip()):
                items.append(re.sub(r"^\d+\.\s+", "", body_lines[i].strip())); i += 1
            out.append("<ol>" + "".join(f"<li>{inline(x)}</li>" for x in items) + "</ol>"); continue
        para.append(s); i += 1
    flush()
    return "\n".join(out)

# --------------------------------------------------------------------------
# 3. Parse the manifesto into ordered pages
# --------------------------------------------------------------------------
def slugify(s):
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")

def is_boundary(l):
    return bool(re.match(r"^# Chapter \d+ —", l) or re.match(r"^# Coda —", l)
                or re.match(r"^# Part [IVX]+ —", l)
                or re.match(r"^## Preface —", l) or re.match(r"^## Start here —", l)
                or re.match(r"^## About this book", l) or re.match(r"^## Appendix —", l))

lines = md.split("\n")
bounds = [i for i, l in enumerate(lines) if is_boundary(l)]

def meta_of(head):
    m = re.match(r"^# Chapter (\d+) — (.+)$", head)
    if m:
        num, title = int(m.group(1)), m.group(2).strip()
        return dict(eyebrow=f"Chapter {num}", title=title, slug=f"ch{num}-{slugify(title)}",
                    card_meta=f"Chapter {num}", num=num)
    m = re.match(r"^# Part ([IVX]+) — (.+)$", head)
    if m:
        rn, title = m.group(1), m.group(2).strip()
        return dict(eyebrow=f"Part {rn}", title=title, slug=f"part-{rn.lower()}",
                    card_meta=f"Part {rn}")
    m = re.match(r"^# Coda — (.+)$", head)
    if m:
        return dict(eyebrow="Coda", title=m.group(1).strip(), slug="coda", card_meta="Coda")
    m = re.match(r"^## Preface — (.+)$", head)
    if m:
        return dict(eyebrow="Front matter", title="Preface", sub=m.group(1).strip(),
                    slug="preface", card_meta="Front matter")
    m = re.match(r"^## Start here — (.+)$", head)
    if m:
        return dict(eyebrow="Front matter", title="Start here", sub=m.group(1).strip(),
                    slug="start-here", card_meta="How to read this book")
    if head.startswith("## About this book"):
        return dict(eyebrow="Back matter", title="About this book", slug="about", card_meta="Back matter")
    m = re.match(r"^## Appendix — (.+)$", head)
    if m:
        return dict(eyebrow="Appendix", title=m.group(1).strip(), slug="glossary",
                    card_meta="The shifting vocabulary, pinned")
    return dict(eyebrow="", title=head.strip("# ").strip(), slug=slugify(head), card_meta="")

pages = []
for k, start in enumerate(bounds):
    end = bounds[k + 1] if k + 1 < len(bounds) else len(lines)
    head = lines[start]
    m = meta_of(head)
    body = lines[start + 1:end]
    m["body_html"] = convert_body(body, m)
    # preview text: first 1-2 real (non-lede) paragraphs
    prev_txt = ""
    for ln in body:
        s = ln.strip()
        if not s or s.startswith(("#", ">", "-", "*", "|", "`")) or (s.startswith("*") and s.endswith("*")):
            continue
        prev_txt += (" " if prev_txt else "") + plain(s)
        if len(prev_txt) > 230:
            break
    if len(prev_txt) > 250:
        prev_txt = prev_txt[:250].rsplit(" ", 1)[0] + "…"
    m["preview"] = html.escape(prev_txt, quote=False)
    m["words"] = len(re.findall(r"\b\w+\b", plain("\n".join(body))))
    pages.append(m)

# wire prev/next
for idx, p in enumerate(pages):
    p["prev"] = pages[idx - 1]["slug"] if idx > 0 else ""
    p["next"] = pages[idx + 1]["slug"] if idx < len(pages) - 1 else ""

# --------------------------------------------------------------------------
# 4. Custom diagrams (color allowed inside figures; no yellow)
#    Injected after the 2nd </p> of the target chapter (after lede + 1st para).
# --------------------------------------------------------------------------
from figures import FIGURES   # slug -> figure HTML

def inject(article_html, fig):
    parts = article_html.split("</p>", 2)
    if len(parts) == 3:
        return parts[0] + "</p>" + parts[1] + "</p>" + fig + parts[2]
    return article_html + fig

# --------------------------------------------------------------------------
# 5. Assemble overview cards, sidebar links, articles
# --------------------------------------------------------------------------
cards, sidelinks, articles = [], [], []
for p in pages:
    cards.append(
        f'<a class="chapter-card" href="#{p["slug"]}">\n'
        f'<div class="card-preview"><p>{p["preview"]}</p></div>\n'
        f'<div class="card-meta"><h3 class="card-title">{html.escape(p["title"], quote=False)}</h3>'
        f'<p class="card-words">{p["card_meta"]} · {p["words"]} words</p></div>\n</a>')
    # part pages carry their "Part N : " prefix in every label surface
    # (sidebar, breadcrumb, prev/next, search) while the page itself keeps
    # the eyebrow + bare title
    disp_title = (f'{p["card_meta"]} — {p["title"]}'
                  if p["slug"].startswith("part-") else p["title"])
    sl_label = (f'{p["num"]} · {html.escape(p["title"], quote=False)}'
                if p.get("num") else html.escape(disp_title, quote=False))
    # data-t mirrors the label so CSS can reserve the bold width (no reflow on hover/active)
    sl_attr = sl_label.replace('"', '&quot;')
    sidelinks.append(
        f'<a class="sidebar-link" href="#{p["slug"]}">'
        f'<span class="sl-text" data-t="{sl_attr}">{sl_label}</span>'
        f'<span class="sl-leader"></span></a>')
    body = p["body_html"]
    if p["slug"] in FIGURES:
        body = inject(body, FIGURES[p["slug"]])
    # the open book (house OPEN-BOOK.md, HOUSE-11): the ask and the colophon line once, after the last chapter
    the_ask = ('<section class="the-invite"><p class="invite-line">If this book is useful to your organisation, I work with organisations on its subjects: paper copies in quantity, workshops and training, talks, consulting and the building of solutions. Write to <a href="mailto:kalidianow@gmail.com">kalidianow@gmail.com</a>.</p>'
               '<p class="invite-more"><a href="https://mayouni.github.io/ayouni/offer/">How these books are offered</a></p>'
               '<p class="colophon-line">Free to read and share under <a href="https://mayouni.github.io/ayouni/licence/">CC BY-NC-ND 4.0</a>; code under the library&#39;s licence.</p></section>') if p["slug"] == "coda" else ""
    articles.append(
        f'<article class="chapter-page" id="page-{p["slug"]}" data-slug="{p["slug"]}" '
        f'data-title="{html.escape(disp_title, quote=False)}" data-prev="{p["prev"]}" data-next="{p["next"]}">\n'
        f'<div class="ch-eyebrow">{p["eyebrow"]}</div>\n'
        f'<h1 class="ch-title">{html.escape(p["title"], quote=False)}</h1>\n'
        f'<div class="ch-rule"></div>\n{body}\n{the_ask}</article>')

# --------------------------------------------------------------------------
# 6. Extra CSS for the new block types + interactive cascade
# --------------------------------------------------------------------------
EXTRA_CSS = """
/* ---- manifesto edition additions ---- */
.ch-lede{font-style:italic;color:var(--soft);font-size:1.04em;line-height:1.55;margin:0 0 1.7em;padding-bottom:1.1em;border-bottom:1px solid var(--rule);}
h4.subsubsection-h{font-family:var(--sans);font-weight:700;font-size:0.76em;letter-spacing:0.05em;text-transform:uppercase;color:var(--ink-soft);margin:2em 0 0.5em;line-height:1.4;}
.chapter-page ul,.chapter-page ol{margin:1.1em 0 1.1em 1.3em;padding:0;}
.ayouni-home{display:inline-flex;align-items:center;}
.top-header .ayouni-home{height:38px;margin-right:6px;}
.top-header .ayouni-home svg{height:22px;width:auto;aspect-ratio:2095/518;}
.hero-imprint .ayouni-home svg{height:46px;width:auto;aspect-ratio:2095/518;}
@media (max-width: 900px){.top-header .ayouni-home svg{height:16px;}}
.card-preview{font-size:18px;line-height:1.55;color:var(--ink);max-height:340px;}
.hero-subtitle{font-size:24px;color:var(--ink);}
.hero-author{font-size:20px;}
.hero-meta,.hero-series,.hero-status,.hb-label,.search-clear-hl{font-size:14px;}
.spine-badge,.code-cell .cell-label,.stage,.aside-h,.src-k,.cnb-dir,.eyebrow,.ch-eyebrow,.card-words,.fig-label{font-size:14px;}
.cover-wrap{position:relative;display:inline-block;line-height:0;}
.cover-wrap .cover-img{cursor:zoom-in;}
.cover-zoom{position:absolute;right:14px;bottom:14px;width:46px;height:46px;border-radius:50%;border:1px solid var(--rule-strong);background:var(--paper);color:var(--ink);display:flex;align-items:center;justify-content:center;cursor:zoom-in;padding:0;box-shadow:0 2px 10px rgba(23,20,15,.25);}
.cover-zoom svg{width:22px;height:22px;}
.cover-zoom:hover{background:var(--ink);color:var(--paper);}
.cover-lightbox{position:fixed;top:0;right:0;bottom:0;left:0;z-index:1000;background:rgba(23,20,15,.88);display:flex;align-items:center;justify-content:center;padding:24px;cursor:zoom-out;}
.cover-lightbox[hidden]{display:none;}
.cover-lightbox img{max-width:calc(100vw - 48px);max-height:calc(100vh - 48px);width:auto;height:auto;background:var(--paper);box-shadow:0 8px 40px rgba(23,20,15,.45);}
.cover-close{position:absolute;top:14px;right:18px;width:46px;height:46px;border-radius:50%;border:1px solid var(--rule-strong);background:var(--paper);color:var(--ink);font-size:28px;line-height:1;cursor:pointer;padding:0;}
.the-invite{margin:3.2em 0 1em;padding:1.6em 0 0;border-top:1px solid var(--rule);}
.the-invite p{text-indent:0;text-align:left;hyphens:none;}
.the-invite .invite-line{font-style:italic;}
.the-invite a{border-bottom:1px solid var(--rule-strong);}
.the-invite .invite-more,.the-invite .colophon-line{font-family:var(--sans);font-size:14.5px;color:var(--soft);line-height:1.5;}
.chapter-page li{margin:0.4em 0;line-height:1.6;}
blockquote{margin:1.5em 0;padding:0.3em 0 0.3em 1.3em;border-left:3px solid var(--rule-strong);color:var(--ink-soft);font-style:italic;}
.book-table{width:100%;border-collapse:collapse;font-family:var(--sans);font-size:0.74em;line-height:1.45;margin:1.7em 0;}
.book-table th,.book-table td{border:1px solid var(--rule);padding:7px 10px;text-align:left;vertical-align:top;}
.book-table th{background:var(--sidebar-bg);font-weight:700;color:var(--ink);}
.book-table tr.is-refine td,.book-table td strong{color:var(--ink);}
pre{background:#211c15;border:1px solid #35302a;border-radius:10px;padding:1.1em 1.3em;overflow-x:auto;margin:1.5em 0;font-size:0.7em;line-height:1.65;}
.chapter-page pre code{font-family:ui-monospace,'Cascadia Code','SF Mono',Consolas,Menlo,monospace;font-size:1em;white-space:pre;color:#e8e1d1;background:none;padding:0;border-radius:0;}
pre .c-kw,pre .c-field{color:#f0914f;font-weight:600;}
pre .c-string{color:#a9c795;}
pre .c-number{color:#82c0ae;}
pre .c-comment{color:#8d8471;font-style:italic;}
pre .c-ok,pre .c-diffadd{color:#9fc98f;}
pre .c-bad,pre .c-diffdel{color:#e0796a;}
.chapter-page code{font-family:var(--sans);font-size:0.82em;background:var(--sidebar-bg);padding:0.05em 0.35em;border-radius:4px;}
figure figcaption .fig-hint{font-family:var(--sans);font-size:0.82em;color:var(--bookmark);font-style:normal;}
/* interactive cascade */
#casc-int .ci-node,#casc-int .ci-edge{transition:opacity .45s ease, fill .45s ease;}
#casc-int .ci-n1,#casc-int .ci-n2,#casc-int .ci-e1,#casc-int .ci-e2{opacity:0.13;}
#casc-int .ci-lit{opacity:1;}
#casc-int{cursor:pointer;}
.ci-replay{font-family:var(--sans);font-size:0.8em;color:var(--bookmark);cursor:pointer;border:none;background:none;padding:4px 0;}
.ci-replay:hover{text-decoration:underline;}
"""
if "manifesto edition additions" not in head_header:   # idempotent: inject CSS only once
    head_header = head_header.replace("</style>", EXTRA_CSS + "\n</style>", 1)

COVER_ZOOM_JS = "(function(){var z=document.querySelector('.cover-zoom'),lb=document.getElementById('coverLightbox'),im=document.querySelector('.hero-cover .cover-img');if(!z||!lb||!im)return;var big=lb.querySelector('img'),x=lb.querySelector('.cover-close');function open(){big.src=im.src;lb.hidden=false;document.body.style.overflow='hidden';x.focus();}function close(){lb.hidden=true;big.removeAttribute('src');document.body.style.overflow='';z.focus();}z.addEventListener('click',open);im.addEventListener('click',open);lb.addEventListener('click',function(e){if(e.target!==big)close();});document.addEventListener('keydown',function(e){if(e.key==='Escape'&&!lb.hidden)close();});})();"

# --------------------------------------------------------------------------
# 7. Overview + chapter views
# --------------------------------------------------------------------------
overview = f"""{OV_MARK}
<div class="view view-overview active" id="viewOverview">
<div class="overview-container">

<section class="book-hero">
<div class="hero-cover">
<div class="cover-wrap"><img src="cover.png" alt="Refinement-Oriented Programming — book cover" class="cover-img"><button type="button" class="cover-zoom" aria-label="View the cover large" title="View the cover large"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="10.5" cy="10.5" r="6.5"/><line x1="15.5" y1="15.5" x2="21" y2="21"/><line x1="10.5" y1="7.5" x2="10.5" y2="13.5"/><line x1="7.5" y1="10.5" x2="13.5" y2="10.5"/></svg></button></div>
</div>
<div class="cover-lightbox" id="coverLightbox" role="dialog" aria-modal="true" aria-label="View the cover large" hidden><button type="button" class="cover-close" aria-label="Close">&times;</button><img alt="Refinement-Oriented Programming — book cover"></div>
<script>{COVER_ZOOM_JS}</script>
<div class="hero-info">
<h1 class="hero-title">Refinement-Oriented Programming</h1>
<p class="hero-subtitle">{SUBTITLE}</p>
<p class="hero-author">Mansour Ayouni</p>
<p class="hero-meta">NIAMEY · TUNIS · PARIS · 2026</p>
<div class="view-mode-toggle" role="group" aria-label="View mode">
<button class="vm-list" id="vmList" aria-label="List view">
<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="8" y1="6" x2="21" y2="6"/><line x1="8" y1="12" x2="21" y2="12"/><line x1="8" y1="18" x2="21" y2="18"/><circle cx="4" cy="6" r="1.2"/><circle cx="4" cy="12" r="1.2"/><circle cx="4" cy="18" r="1.2"/></svg>
</button>
<button class="vm-grid active" id="vmGrid" aria-label="Grid view">
<svg viewBox="0 0 24 24" fill="currentColor"><rect x="3" y="3" width="8" height="8" rx="1"/><rect x="13" y="3" width="8" height="8" rx="1"/><rect x="3" y="13" width="8" height="8" rx="1"/><rect x="13" y="13" width="8" height="8" rx="1"/></svg>
</button>
</div>
</div>
</section>

<section class="chapter-grid" id="chapterGrid">

{chr(10).join(cards)}

</section>

</div><!-- /overview-container -->
</div><!-- /view-overview -->

<!-- ============ CHAPTER VIEW ============ -->
<div class="view view-chapter" id="viewChapter">
<div class="chapter-container">

<aside class="chapter-sidebar" id="chapterSidebar">
<h2 class="sidebar-book-title"><a href="#">Refinement-Oriented Programming</a></h2>
<nav class="sidebar-nav" id="sidebarNav">
{chr(10).join(sidelinks)}
</nav>
</aside>

<main class="chapter-main">

{chr(10).join(articles)}

<!-- CHAPTER NAV (next/previous) — populated by JS -->
<nav class="ch-nav" id="chapterNav" aria-label="Chapter navigation">
<a class="ch-nav-btn" id="cnPrev" href="#">
<span class="cnb-dir">← Previous</span>
<span class="cnb-title">—</span>
</a>
<a class="ch-nav-btn next" id="cnNext" href="#">
<span class="cnb-dir">Next →</span>
<span class="cnb-title">—</span>
</a>
</nav>

</main>

</div><!-- /chapter-container -->
</div><!-- /view-chapter -->

"""

out = head_header + overview + script_tail
OUT.write_text(out, encoding="utf-8")
print(f"wrote {OUT}  ({len(pages)} pages, {len(out)} bytes)")
if "substrate" in out.lower():
    print("!! WARNING: 'substrate' found in output")
else:
    print("substrate check: clean")
