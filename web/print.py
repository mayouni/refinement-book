#!/usr/bin/env python3
"""
print.py — the press edition (Teaching Edition Phase 6).

Composes manuscript/rop-book.md into a 6x9in print-ready HTML (front-matter
sequence, running heads, folios, real TOC page numbers via paged.js) and drives
headless Chrome to web/book.pdf — cover and back cover included.

Run:  python web/print.py            (writes web/print.html, then web/book.pdf)
      python web/print.py --html     (compose only, skip the PDF step)

Requires network at build time (Google Fonts + the paged.js polyfill CDN).
"""
import pathlib, subprocess, sys, html

sys.argv = [a for a in sys.argv if a != "--manifesto"]   # safety: always the book
import build   # side effect: (re)builds web/index.html; supplies build.pages

ROOT = build.ROOT
OUT_HTML = ROOT / "web" / "print.html"
OUT_PDF = ROOT / "web" / "book.pdf"
CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

# --------------------------------------------------------------------------
# Print CSS — 6x9in trim, EB Garamond body, folios + running heads (paged.js)
# --------------------------------------------------------------------------
CSS = """
@page {
  size: 6in 9in;
  margin: 0.72in 0.66in 0.72in;
  @bottom-center { content: counter(page); font-family: 'Inter',sans-serif; font-size: 8.5pt; color: #1a1612; }
  @top-center { content: string(chaptitle); font-family: 'Inter',sans-serif; font-size: 7.5pt;
                letter-spacing: 1.2px; text-transform: uppercase; color: #6b6358; }
}
@page front { @bottom-center { content: none; } @top-center { content: none; } }
@page :blank { @bottom-center { content: none; } @top-center { content: none; } }
@page coverpage { size: 6in 9in; margin: 0; @bottom-center { content: none; } @top-center { content: none; } }

* { box-sizing: border-box; margin: 0; padding: 0; }
html { font-size: 10.8pt; }
body { font-family: 'EB Garamond', Georgia, serif; color: #1a1612; line-height: 1.52; }

/* ---------- the open book: the last page ---------- */
.pg-ask { page: front; break-before: page; break-after: page; padding-top: 2.2in; font-family: 'Inter', sans-serif; font-size: 10pt; line-height: 1.6; color: #3a3326; }
.pg-ask p { margin-bottom: 0.1in; text-indent: 0; }
.pg-ask .ask-line { font-family: 'EB Garamond', Georgia, serif; font-style: italic; font-size: 13pt; color: #1a1612; }
/* ---------- cover + back ---------- */
.pg-cover, .pg-back { page: coverpage; break-after: page; }
.pg-cover { height: 9in; background: #f7f6f2; display: flex; align-items: center; justify-content: center; }
.pg-cover img { max-width: 100%; max-height: 100%; }
.pg-back { height: 9in; background: #f5f0e2; padding: 0.85in 0.75in 0.7in; display: flex; flex-direction: column; }
.pg-back .bb-blurb { font-size: 10.5pt; line-height: 1.55; }
.pg-back .bb-blurb p { margin-bottom: 0.14in; text-indent: 0; }
.pg-back .bb-points { margin: 0.22in 0; font-family: 'Inter',sans-serif; font-size: 9pt; line-height: 1.6; }
.pg-back .bb-points div { margin-bottom: 0.08in; }
.pg-back .bb-points span { color: #E96A1A; margin-right: 0.08in; }
.pg-back .bb-tag { color: #E96A1A; font-size: 11.5pt; margin-top: 0.06in; }
.pg-back .bb-author { font-size: 9.5pt; font-style: italic; color: #3a3326; margin-top: 0.1in; }
.pg-back .bb-foot { margin-top: auto; display: flex; align-items: flex-end; justify-content: space-between; }
.pg-back .bb-imprint { font-family: 'Archivo Black', sans-serif; font-size: 15pt; letter-spacing: -0.01em; }
.pg-back .bb-imprint .dot { position: relative; }
.pg-back .bb-imprint .dot::before { content:''; position:absolute; width:0.16em; height:0.16em; border-radius:50%;
  background:#1a1612; top:-0.30em; left:50%; transform:translateX(-50%); }
.pg-back .bb-meta { font-family: 'Inter',sans-serif; font-size: 7.5pt; color: #6b6358; text-align: right; line-height: 1.7; }
.pg-back .bb-isbn { border: 1px solid #9a9078; padding: 0.06in 0.12in; display: inline-block; margin-top: 0.06in; }

/* ---------- front matter ---------- */
.fm { page: front; break-before: right; }
.fm-halftitle { padding-top: 2.6in; text-align: center; }
.fm-halftitle .t { font-family: 'Inter',sans-serif; font-weight: 800; font-size: 17pt; letter-spacing: -0.3px; }
.fm-title { padding-top: 2.1in; text-align: center; }
.fm-title .t { font-family: 'Inter',sans-serif; font-weight: 800; font-size: 25pt; line-height: 1.12; letter-spacing: -0.6px; }
.fm-title .s { font-style: italic; font-size: 12.5pt; color: #3a3326; margin-top: 0.22in; }
.fm-title .a { font-family: 'Inter',sans-serif; font-size: 12pt; font-weight: 600; margin-top: 0.55in; }
.fm-title .imprint { font-family: 'Archivo Black',sans-serif; font-size: 13pt; margin-top: 1.15in; }
.fm-title .imprint .dot { position: relative; }
.fm-title .imprint .dot::before { content:''; position:absolute; width:0.16em; height:0.16em; border-radius:50%;
  background:#1a1612; top:-0.30em; left:50%; transform:translateX(-50%); }
.fm-title .cities { font-family: 'Inter',sans-serif; font-size: 8pt; letter-spacing: 2px; color:#6b6358; margin-top: 0.12in; }
.fm-copyright { break-before: left; padding-top: 5.2in; font-size: 8.5pt; line-height: 1.6; color: #3a3326; }
.fm-copyright p { margin-bottom: 0.09in; text-indent: 0; }
.fm-dedication { padding-top: 2.8in; text-align: center; font-style: italic; font-size: 11pt; }
.fm-dedication .sig { font-style: normal; font-size: 9pt; color: #6b6358; margin-top: 0.3in; font-family:'Inter',sans-serif; }
.fm-epigraph { padding-top: 2.8in; padding-left: 0.5in; padding-right: 0.5in; }
.fm-epigraph blockquote { font-style: italic; font-size: 12pt; line-height: 1.6; border: none; }
.fm-epigraph .attr { font-size: 9.5pt; color: #6b6358; margin-top: 0.22in; }
.fm-toc h2 { font-family: 'Inter',sans-serif; font-size: 15pt; font-weight: 800; margin-bottom: 0.35in; }
.toc-line { display: flex; align-items: baseline; font-size: 10pt; margin-bottom: 0.075in; }
.toc-line.toc-part { font-family: 'Inter',sans-serif; font-weight: 700; font-size: 9pt;
  letter-spacing: 1.2px; text-transform: uppercase; margin: 0.18in 0 0.1in; }
.toc-line.toc-back { margin-top: 0.18in; }
.toc-line a { text-decoration: none; color: inherit; display: flex; width: 100%; align-items: baseline; }
.toc-line .tt { flex: 0 1 auto; }
.toc-line .ld { flex: 1 1 auto; border-bottom: 1px dotted #9a9078; margin: 0 0.06in 0.03in; min-height: 1px; }
.toc-line a::after { content: target-counter(attr(href url), page); font-family: 'Inter',sans-serif; font-size: 8.5pt; }
.toc-line.toc-part a::after { content: none; }
.toc-line.toc-part .ld { border: none; }

/* ---------- body pages ---------- */
.pp { break-before: right; }
.pp.pp-part { page: front; }
.pp-part .eyebrow { margin-top: 2.2in; }
.eyebrow { font-family: 'Inter',sans-serif; font-size: 8.5pt; font-weight: 700; letter-spacing: 2.5px;
  text-transform: uppercase; color: #6b6358; margin-bottom: 0.16in; }
h1.ch-title { font-family: 'Inter',sans-serif; font-weight: 800; font-size: 19pt; line-height: 1.15;
  letter-spacing: -0.4px; margin-bottom: 0.14in; string-set: chaptitle content(text); break-after: avoid; }
.pp-part h1.ch-title { font-size: 22pt; }
.ch-rule { border-bottom: 2.5px solid #1a1612; width: 0.55in; margin-bottom: 0.28in; }
.ch-lede { font-style: italic; font-size: 11pt; color: #3a3326; line-height: 1.5;
  margin-bottom: 0.26in; padding-bottom: 0.14in; border-bottom: 0.7px solid #cfc8b4; }
p { margin-bottom: 0.115in; text-align: justify; hyphens: auto; orphans: 3; widows: 3; }
p em { font-style: italic; } p strong { font-weight: 700; }
h3.subsection-h { font-family: 'Inter',sans-serif; font-size: 9.5pt; font-weight: 700; letter-spacing: 1.6px;
  text-transform: uppercase; margin: 0.28in 0 0.14in; break-after: avoid; }
h4.subsubsection-h { font-family:'Inter',sans-serif; font-size: 8.5pt; font-weight:700; letter-spacing:1px;
  text-transform: uppercase; color:#3a3326; margin: 0.2in 0 0.1in; break-after: avoid; }
ul, ol { margin: 0.12in 0 0.14in 0.28in; }
li { margin-bottom: 0.06in; line-height: 1.5; }
blockquote { margin: 0.16in 0; padding-left: 0.18in; border-left: 2px solid #1a1612;
  font-style: italic; color: #3a3326; }
code { font-family: Consolas, Menlo, monospace; font-size: 0.86em; background: #f5f0e2; padding: 0 0.03in; }
pre { background: #211c15; border-radius: 6px; padding: 0.14in 0.16in; margin: 0.18in 0;
  font-size: 7.5pt; line-height: 1.55; break-inside: avoid; }
pre code { background: none; color: #e8e1d1; padding: 0; font-size: 1em; white-space: pre-wrap; }
figure { margin: 0.22in 0; text-align: center; break-inside: avoid; }
figure svg { max-width: 100%; height: auto; max-height: 4.7in; }
figcaption { font-size: 8.8pt; font-style: italic; color: #3a3326; margin-top: 0.1in;
  line-height: 1.45; text-align: center; }
figcaption strong { font-style: normal; }
.fig-hint, .ci-replay { display: none; }                    /* web-only chrome */
#casc-int .ci-node, #casc-int .ci-edge { opacity: 1 !important; }  /* full cascade in print */
#casc-count { display: none; }
table { width: 100%; border-collapse: collapse; font-family:'Inter',sans-serif; font-size: 8pt; margin: 0.16in 0; }
th, td { border: 0.7px solid #cfc8b4; padding: 0.05in 0.07in; text-align: left; vertical-align: top; }
a { color: inherit; text-decoration: none; }
"""

# --------------------------------------------------------------------------
# Front + back matter content
# --------------------------------------------------------------------------
COVER = '<div class="pg-cover"><img src="cover.png" alt="Refinement-Oriented Programming — cover"></div>'

HALF_TITLE = '<div class="fm fm-halftitle"><div class="t">Refinement-Oriented Programming</div></div>'

TITLE_PAGE = """<div class="fm fm-title">
<div class="t">Refinement-Oriented<br>Programming</div>
<div class="s">A discipline for software in the agentic era</div>
<div class="a">Mansour Ayouni</div>
<div class="imprint"><img alt="AYOUNI" src="../assets/covers/ayouni-logo.png" style="height:0.34in;width:auto"></div>
<div class="cities">TUNIS · NIAMEY · PARIS · 2026</div>
</div>"""

COPYRIGHT = """<div class="fm fm-copyright">
<p>© 2026 Mansour Ayouni</p>
<p>Published by AYOUNI, the independent imprint of Mansour Ayouni / Softanza Labs. Tunis · Niamey · Paris.</p>
<p>The text of this book is released under Creative Commons Attribution-NonCommercial-NoDerivatives 4.0
International (CC BY-NC-ND 4.0). Illustrations are released under CC BY-NC-SA 4.0 unless otherwise noted.
Terminal sessions and code fragments are released under the MIT License.</p>
<p>The free digital edition is at https://mayouni.github.io/ayouni/books/refinement/en/. Paper copies in quantity are supplied to organisations on request: https://mayouni.github.io/ayouni/offer/.</p>
<p>First edition: 2026 — the Teaching Edition. Typeset in EB Garamond, Inter, and Archivo Black.
Cover illustration: a giraffe in patchwork coat, for Niger. [Artist credit to be added.]</p>
<p>ISBN: pending.</p>
</div>"""

DEDICATION = """<div class="fm fm-dedication">
<p>For the compliance officers, programmers, and auditors of regulated banks across the WAEMU region,
who knew the discipline this book argues for before they had a name for it.</p>
<div class="sig">—MA · Niamey · 2026</div>
</div>"""

EPIGRAPH = """<div class="fm fm-epigraph">
<blockquote>An artisan refines until the work is finished. A regulator asks how the work was refined.
A programmer answers.</blockquote>
<div class="attr">— traditional adage, attribution lost</div>
</div>"""

THE_ASK = """<div class="pg-ask"><p class="ask-line">If this book is useful to your organisation, I work with organisations on its subjects: paper copies in quantity, workshops and training, talks, consulting and the building of solutions. Write to kalidianow@gmail.com.</p>
<p>How these books are offered: https://mayouni.github.io/ayouni/offer/</p>
<p>Free to read and share under CC BY-NC-ND 4.0; code under the library's licence.</p>
<p>https://mayouni.github.io/ayouni/licence/</p></div>"""

BACK_COVER = """<div class="pg-back">
<div class="bb-blurb">
<p><strong>Software is now written faster than anyone can trust it.</strong> An AI agent can draft in an
afternoon what a team once built in a quarter — and every organization shipping consequential software has
felt the ground move: the bottleneck is no longer writing changes. It is trusting them.</p>
<p>This book teaches the discipline that answers. Told through a small bank in Niamey facing a regulator's
deadline, it shows how every change — human or machine — becomes typed, checked before it lands, attributed,
and reversible. You will run a governed change end to end in Chapter&nbsp;3; by the last page, the jungle of
agents, memory, RAG, and governance has resolved into one legible map.</p>
<p class="bb-tag"><em>Stop trying to govern the intelligence, and govern the change.</em></p>
</div>
<div class="bb-points">
<div><span>&#9656;</span>The AI jungle, mapped — ten contested words, each given one honest job</div>
<div><span>&#9656;</span>A discipline you can start Monday with a notebook — the tooling makes it fast</div>
<div><span>&#9656;</span>For programmers, compliance officers, and everyone who signs for software</div>
</div>
<div class="bb-author">Mansour Ayouni is the
founder of Softanza Labs. He works between Tunis, Niamey, and Paris.</div>
<div class="bb-foot">
<div class="bb-imprint"><img alt="AYOUNI" src="../assets/covers/ayouni-logo.png" style="height:0.34in;width:auto"></div>
<div class="bb-meta">mayouni.github.io/ayouni<br>TUNIS · NIAMEY · PARIS · 2026<br><span class="bb-isbn">ISBN pending</span></div>
</div>
</div>"""

# --------------------------------------------------------------------------
# TOC + body from the parsed pages
# --------------------------------------------------------------------------
toc, body = [], []
toc.append('<div class="fm fm-toc"><h2>Contents</h2>')
for p in build.pages:
    slug, title, eyebrow = p["slug"], p["title"], p["eyebrow"]
    if slug.startswith("part-"):
        toc.append(f'<div class="toc-line toc-part"><a href="#pp-{slug}"><span class="tt">'
                   f'{eyebrow} — {html.escape(title, quote=False)}</span><span class="ld"></span></a></div>')
    else:
        label = f'{p["num"]} · {html.escape(title, quote=False)}' if p.get("num") else html.escape(title, quote=False)
        extra = " toc-back" if slug in ("coda", "glossary") else ""
        toc.append(f'<div class="toc-line{extra}"><a href="#pp-{slug}"><span class="tt">{label}</span>'
                   f'<span class="ld"></span></a></div>')
toc.append('</div>')

for p in build.pages:
    kind = "pp-part" if p["slug"].startswith("part-") else "pp-chapter"
    body.append(
        f'<article class="pp {kind}" id="pp-{p["slug"]}">\n'
        f'<div class="eyebrow">{p["eyebrow"]}</div>\n'
        f'<h1 class="ch-title">{html.escape(p["title"], quote=False)}</h1>\n'
        f'<div class="ch-rule"></div>\n{p["body_html"]}\n</article>')

DOC = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Refinement-Oriented Programming — print edition</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Archivo+Black&family=EB+Garamond:ital,wght@0,400;0,500;0,600;0,700;1,400;1,500;1,600&family=Inter:wght@400;600;700;800&display=swap" rel="stylesheet">
<style>{CSS}</style>
<script src="https://unpkg.com/pagedjs/dist/paged.polyfill.js"></script>
</head>
<body>
{COVER}
{HALF_TITLE}
{TITLE_PAGE}
{COPYRIGHT}
{DEDICATION}
{EPIGRAPH}
{chr(10).join(toc)}
{chr(10).join(body)}
{THE_ASK}
{BACK_COVER}
</body>
</html>"""

OUT_HTML.write_text(DOC, encoding="utf-8", newline="\n")
print(f"wrote {OUT_HTML}  ({len(DOC)} bytes)")
if "substrate" in DOC.lower():
    print("!! substrate check FAILED"); sys.exit(1)
print("substrate check: clean")

if "--html" not in sys.argv:
    # Drive Chrome over the DevTools protocol: load, WAIT until paged.js has
    # actually finished laying out the book, then print. (--virtual-time-budget
    # is unreliable under the new headless mode.)
    import json, time, base64, socket, urllib.request
    import websocket   # websocket-client

    def free_port():
        s = socket.socket(); s.bind(("127.0.0.1", 0)); port = s.getsockname()[1]; s.close(); return port

    port = free_port()
    proc = subprocess.Popen([CHROME, "--headless=new", "--disable-gpu",
                             f"--remote-debugging-port={port}", "--remote-allow-origins=*",
                             "--no-first-run", "--no-default-browser-check",
                             OUT_HTML.as_uri()],
                            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    try:
        ws_url = None
        for _ in range(50):
            try:
                tabs = json.load(urllib.request.urlopen(f"http://127.0.0.1:{port}/json"))
                page = next(t for t in tabs if t["type"] == "page")
                ws_url = page["webSocketDebuggerUrl"]; break
            except Exception:
                time.sleep(0.3)
        assert ws_url, "could not reach Chrome DevTools"
        ws = websocket.create_connection(ws_url, timeout=240)
        mid = [0]
        def cmd(method, **params):
            mid[0] += 1
            ws.send(json.dumps({"id": mid[0], "method": method, "params": params}))
            while True:
                msg = json.loads(ws.recv())
                if msg.get("id") == mid[0]:
                    return msg.get("result", {})
        cmd("Runtime.enable")
        # wait for paged.js to finish: page count stable and > 50
        last, stable = 0, 0
        for i in range(240):
            r = cmd("Runtime.evaluate",
                    expression="document.querySelectorAll('.pagedjs_page').length")
            n = r.get("result", {}).get("value", 0) or 0
            if n > 50 and n == last:
                stable += 1
                if stable >= 4:      # unchanged for ~4s -> done
                    break
            else:
                stable = 0
            last = n
            time.sleep(1)
        print(f"paged.js layout: {last} pages")
        assert last > 50, "pagination did not complete"
        time.sleep(2)                # settle fonts/last reflow
        res = cmd("Page.printToPDF", printBackground=True, preferCSSPageSize=True,
                  displayHeaderFooter=False)
        OUT_PDF.write_bytes(base64.b64decode(res["data"]))
        ws.close()
        print(f"wrote {OUT_PDF}  ({OUT_PDF.stat().st_size} bytes)")
    finally:
        proc.terminate()
