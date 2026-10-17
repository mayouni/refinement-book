"""Draw the back cover of Refinement-Oriented Programming (web/cover-back.png), on the front cover's grid (ROP-18).

The author asked, on 2026-10-17, for a back cover on both AYOUNI books, turnable in the reader and set with the front in
the PDF, "professional grade". The Softanza book drew its own first (COVER-05, its tools/make_cover.py); this one follows
the same grid and the same rules: white, drawn at twice the logical 1097 x 1434 (2194 x 2868), and a description made
only of sentences the book already says, never new prose:

  - the thesis, on top: the sentence of the back cover of every edition of this book (ROP-06);
  - the opening sentence of the PDF's back cover, the question of chapter 2, and the first sentence of the start page;
  - the definition of a refinement, chapter 1 and the Softanza book's chapter 10;
  - the imprint band: the AYOUNI logo, the series (HOUSE-13), the free reader and its QR code (checked by decoding it);
  - the foot: the shelf, the edition (a proof copy until every page is published, HOUSE-18) and the licence.

Run: python web/make_back.py
"""
import sys
from pathlib import Path

import segno
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent
LOGO = ROOT / "assets" / "covers" / "ayouni-logo.png"
OUT = ROOT / "web" / "cover-back.png"
K = 2
W, H = 1097 * K, 1434 * K
PAPER, INK, GREY, RULE, RED = (255, 255, 255), (20, 20, 20), (110, 110, 106), (200, 198, 192), (212, 21, 25)
FONTS = Path("C:/Windows/Fonts")

THESIS = "Stop trying to govern the intelligence, and govern the change."
BLURB = [
    "**Software is now written faster than anyone can trust it.** If the change can be written in an afternoon by "
    "something that is not accountable for it, who makes sure it is right?",
    "This book is about one discipline: governing the change to software, now that writing the change is no longer the "
    "slow part of the work.",
    "A refinement is a change to code that was declared to be changeable, proposed in a typed form, judged by a gate, "
    "recorded as a step, and reversible.",
]
SERIES = "Second of the AYOUNI books"
FREE = "Free to read, in every form"
URL = "https://mayouni.github.io/ayouni/books/refinement/en/"
SHELF = "Software engineering \u00b7 AI governance"
EDITION = "PROOF COPY \u00b7 CC BY-NC-ND 4.0"


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


def make():
    back = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(back)
    x, right, maxw = 80 * K, W - 80 * K, 937

    # the thesis on top, then the red rule of the series
    y = 104 * K
    head = font("georgiai.ttf", 50)
    for line in wrap(d, typeset(THESIS), head, maxw):
        d.text((x, y), line, font=head, fill=INK)
        y += 66 * K
    y += 30 * K
    d.rectangle((x, y, x + 64 * K, y + 5 * K), fill=RED)
    y += 52 * K

    # the description: the book's own sentences
    reg, bld = font("georgia.ttf", 30), font("georgiab.ttf", 30)
    for para in BLURB:
        for line in rich_lines(d, typeset(para), reg, bld, maxw):
            cx = x
            for w, f in line:
                d.text((cx, y), w, font=f, fill=INK)
                cx += d.textlength(w + " ", font=f)
            y += 46 * K
        y += 22 * K
    if y > 1100 * K:
        raise SystemExit(f"back cover: the description runs into the imprint band ({y // K} > 1100)")

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
    start_ed = right - spaced_width(d, EDITION, foot, track)
    if start_ed - end_shelf < 40 * K:
        raise SystemExit("back cover: the foot's two lines touch")
    spaced(d, (start_ed, 1373 * K), EDITION, foot, GREY, track)

    back.save(OUT)
    print("wrote", OUT, back.size, f"description ends at {y // K}")

    # the QR code must read back as the reader's address
    import cv2, numpy as np
    img = cv2.cvtColor(np.array(back.crop((right - qr.width - 40, 1180 * K - 40, right + 40, 1180 * K + qr.height + 40))), cv2.COLOR_RGB2BGR)
    data, _, _ = cv2.QRCodeDetector().detectAndDecode(img)
    if data != URL:
        raise SystemExit(f"back cover: the QR code reads {data!r}, not {URL!r}")
    print("QR code decoded:", data)


if __name__ == "__main__":
    sys.exit(make())
