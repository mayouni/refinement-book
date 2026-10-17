"""Draw the back covers of Refinement-Oriented Programming on the front cover's grid (ROP-18, ROP-19).

The author asked, on 2026-10-17, for a back cover on both AYOUNI books, turnable in the reader and set with the front in
the PDF, "professional grade"; then ruled on the Softanza back: "The cover does not cite Softanza anywhere and does not say
what is it and for whome!!!". So each back carries, on top, the title and the subtitle; then the book's opening argument and
two labelled blocks, "What it is" and "Who it is for"; then the thesis; then the imprint band (the AYOUNI logo, the series,
the free reader and its QR code, decoded at build) and the foot (the shelf, the edition, the licence). Every sentence of the
description is the edition's own, word for word, never new prose.

Two editions, two backs (the desk's ruling under HOUSE-09 and HOUSE-18: stage words are the author's to set):
  web/cover-back.png              the live Teaching Edition: its own sentences; "TEACHING EDITION" in the corner
  assets/covers/back-rewrite.png  the rewrite: its own sentences (src/en); "PROOF COPY" until every page is published

White, drawn at twice the logical 1097 x 1434 (2194 x 2868), the front's size. Run: python web/make_back.py
"""
import sys
from pathlib import Path

import segno
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent
LOGO = ROOT / "assets" / "covers" / "ayouni-logo.png"
K = 2
W, H = 1097 * K, 1434 * K
PAPER, INK, GREY, RULE, RED = (255, 255, 255), (20, 20, 20), (110, 110, 106), (200, 198, 192), (212, 21, 25)
FONTS = Path("C:/Windows/Fonts")

TITLE = "Refinement-Oriented Programming"
SUBTITLE = "A discipline for software in the agentic era"
THESIS = "Stop trying to govern the intelligence, and govern the change."
SERIES = "Second of the AYOUNI books"
FREE = "Free to read, in every form"
URL = "https://mayouni.github.io/ayouni/books/refinement/en/"
SHELF = "Software engineering \u00b7 AI governance"

# Each item is a paragraph; '## ' starts a label; **...** is bold. Sources are given beside each sentence.
EDITIONS = {
    "teaching": {
        "out": ROOT / "web" / "cover-back.png",
        "corner": "TEACHING EDITION \u00b7 CC BY-NC-ND 4.0",
        "blurb": [
            # the Teaching Edition's back cover (web/print.py, BACK_COVER), its first paragraph
            "**Software is now written faster than anyone can trust it.** An AI agent can draft in an afternoon what a team "
            "once built in a quarter \u2014 and every organization shipping consequential software has felt the ground move: the "
            "bottleneck is no longer writing changes. It is trusting them.",
            "## What it is",
            # the same back cover, its second paragraph, first two sentences
            "This book teaches the discipline that answers. Told through a small bank in Niamey facing a regulator's deadline, "
            "it shows how every change \u2014 human or machine \u2014 becomes typed, checked before it lands, attributed, and reversible.",
            "## Who it is for",
            # manuscript/rop-book.md, Start here, third paragraph
            "You do not need to be a programmer to read this book. If you are a programmer, you will find the terminal sessions "
            "and the mechanics precise enough to act on. Both readers get the same book; they just linger on different pages.",
        ],
    },
    "rewrite": {
        "out": ROOT / "assets" / "covers" / "back-rewrite.png",
        "corner": "PROOF COPY \u00b7 CC BY-NC-ND 4.0",
        "blurb": [
            # src/en/02-what-broke.md, The afternoon; src/en/00-start-here.md, first sentence
            "If the change can be written in an afternoon by something that is not accountable for it, who makes sure it is "
            "right? **This book is about one discipline: governing the change to software, now that writing the change is no "
            "longer the slow part of the work.**",
            "## What it is",
            # src/en/00-start-here.md, first paragraph; src/en/01-the-letter.md, The principle
            "I call it refinement-oriented programming, and I tell it through a bank that receives a letter. A refinement is a "
            "change to code that was declared to be changeable, proposed in a typed form, judged by a gate, recorded as a step, "
            "and reversible.",
            "## Who it is for",
            # src/en/00-start-here.md, Who it is for
            "It is written first for the crafter at the keyboard, who will run every block. A decision-maker, a bank's head of IT "
            "or of compliance, can read the same pages through the story of Softibank and each chapter's lines on what is built, "
            "designed and absent.",
        ],
    },
}


def font(name, size):
    return ImageFont.truetype(str(FONTS / name), size * K)


def typeset(text):
    return text.replace("'", "\u2019")


def wrap(draw, text, fnt, maxw):
    lines, cur = [], ""
    for word in text.split():
        t = (cur + " " + word).strip()
        if draw.textlength(t, font=fnt) <= maxw * K or not cur:
            cur = t
        else:
            lines.append(cur)
            cur = word
    return lines + [cur]


def rich_lines(draw, text, regular, bold, maxw):
    words = []
    for i, part in enumerate(text.split("**")):
        words += [(w, bold if i % 2 else regular) for w in part.split(" ") if w]
    lines, cur, width = [], [], 0
    for w, f in words:
        ww = draw.textlength(w, font=f)
        sp = draw.textlength(" ", font=f) if cur else 0
        if cur and width + sp + ww > maxw * K:
            lines.append(cur)
            cur, width = [(w, f)], ww
        else:
            cur.append((w, f))
            width += sp + ww
    return lines + ([cur] if cur else [])


def spaced(draw, xy, text, fnt, fill, track):
    x, y = xy
    for ch in text:
        draw.text((x, y), ch, font=fnt, fill=fill)
        x += draw.textlength(ch, font=fnt) + track * K
    return x


def spaced_width(draw, text, fnt, track):
    return sum(draw.textlength(ch, font=fnt) for ch in text) + track * K * (len(text) - 1)


def qr_image(url, size):
    q = segno.make(url, error="m", micro=False)
    m = list(q.matrix)
    cell = (size * K) // len(m)
    im = Image.new("RGB", (cell * len(m), cell * len(m)), PAPER)
    d = ImageDraw.Draw(im)
    for r, row in enumerate(m):
        for c, v in enumerate(row):
            if v:
                d.rectangle((c * cell, r * cell, (c + 1) * cell - 1, (r + 1) * cell - 1), fill=INK)
    return im


def logo_png(width):
    im = Image.open(LOGO).convert("RGBA")
    im = im.crop(im.getbbox())
    return im.resize((width * K, round(im.height * width * K / im.width)), Image.LANCZOS)


def make(name, ed):
    back = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(back)
    x, right, maxw = 80 * K, W - 80 * K, 937

    # the title and the subtitle, then the red rule of the series
    y = 84 * K
    tf = font("arial.ttf", 62)
    for line in wrap(d, TITLE, tf, maxw):
        d.text((x, y), line, font=tf, fill=INK)
        y += 74 * K
    sf = font("georgiai.ttf", 32)
    for line in wrap(d, SUBTITLE, sf, maxw):
        d.text((x, y + 4 * K), line, font=sf, fill=INK)
        y += 44 * K
    y += 26 * K
    d.rectangle((x, y, x + 64 * K, y + 5 * K), fill=RED)
    y += 40 * K

    # the description: the edition's own sentences, with its two labelled blocks
    reg, bld, lab = font("georgia.ttf", 25), font("georgiab.ttf", 25), font("arialbd.ttf", 16)
    for para in ed["blurb"]:
        if para.startswith("## "):
            y += 6 * K
            spaced(d, (x, y), para[3:].upper(), lab, RED, 1.6)
            y += 30 * K
            continue
        for line in rich_lines(d, typeset(para), reg, bld, maxw):
            cx = x
            for w, f in line:
                d.text((cx, y), w, font=f, fill=INK)
                cx += d.textlength(w + " ", font=f)
            y += 37 * K
        y += 16 * K

    # the thesis, on its own line above the imprint band
    tf = font("georgiai.ttf", 32)
    tl = wrap(d, typeset(THESIS), tf, maxw)
    THESIS_Y = 1126 - 44 * len(tl)                 # the thesis sits on the imprint band's hairline
    if y > (THESIS_Y - 20) * K:
        raise SystemExit(f"back cover ({name}): the description runs into the thesis ({y // K} > {THESIS_Y - 20})")
    for i, line in enumerate(tl):
        d.text((x, (THESIS_Y + 44 * i) * K), line, font=tf, fill=INK)

    # the imprint band: a hairline, the logo and the series; the free reader and its QR code
    d.rectangle((x, 1150 * K, right, 1150 * K + 1 * K), fill=RULE)
    logo = logo_png(196)
    back.paste(logo, (x, 1190 * K), logo)
    spaced(d, (x, 1190 * K + logo.height + 20 * K), SERIES.upper(), font("arialbd.ttf", 17), GREY, 2.2)
    qr = qr_image(URL, 148)
    back.paste(qr, (right - qr.width, 1180 * K))
    tx = right - qr.width - 30 * K
    f1, f2 = font("arial.ttf", 25), font("arial.ttf", 21)
    url = URL.split("://", 1)[1]
    host, path = url.split("/", 1)[0] + "/ayouni/", url.split("/ayouni/", 1)[1]
    for i, (s, f, c) in enumerate(((FREE, f1, INK), (host, f2, GREY), (path, f2, GREY))):
        d.text((tx - d.textlength(s, font=f), (1196 + (0 if i == 0 else 8 + 30 * i)) * K), s, font=f, fill=c)

    # the foot, on the front's baseline: the shelf, and the edition with the licence
    foot, track = font("arial.ttf", 19), 0.8
    end_shelf = spaced(d, (x, 1373 * K), SHELF.upper(), foot, GREY, track)
    start_ed = right - spaced_width(d, ed["corner"], foot, track)
    if start_ed - end_shelf < 40 * K:
        raise SystemExit(f"back cover ({name}): the foot's two lines touch")
    spaced(d, (start_ed, 1373 * K), ed["corner"], foot, GREY, track)

    ed["out"].parent.mkdir(parents=True, exist_ok=True)
    back.save(ed["out"])
    print(f"wrote {ed['out']} {back.size}, description ends at {y // K}")

    import cv2, numpy as np
    img = cv2.cvtColor(np.array(back.crop((right - qr.width - 40, 1180 * K - 40, right + 40, 1180 * K + qr.height + 40))), cv2.COLOR_RGB2BGR)
    data, _, _ = cv2.QRCodeDetector().detectAndDecode(img)
    if data != URL:
        raise SystemExit(f"back cover ({name}): the QR code reads {data!r}, not {URL!r}")


def main():
    for name, ed in EDITIONS.items():
        make(name, ed)
    print("QR codes decoded:", URL)


if __name__ == "__main__":
    sys.exit(main())
