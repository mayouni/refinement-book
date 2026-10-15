"""Retouch the Refinement-Oriented Programming cover (web/cover.png, mirrored at site/cover.png).

The author's rulings (2026-10-15): a pure white background, and text that reads at about 440 px wide. The giraffe is
kept exactly as drawn (it is taken from the archived flat cover, assets/covers/archive/2026-07-flat-cover-giraffe.png,
its off-white page colour mapped to white); the old title, subtitle, wordmark and byline are replaced by larger type on
the series template (as the Softanza cover), and the AYOUNI wordmark is the logo (assets/covers/ayouni-logo.png,
rasterised from ayouni-logo.svg). Drawn at twice the logical 1097 x 1434 (2194 x 2868). Run: python web/make_cover.py
"""
import shutil
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent
OLD = ROOT / "assets" / "covers" / "archive" / "2026-07-flat-cover-giraffe.png"
LOGO = ROOT / "assets" / "covers" / "ayouni-logo.png"
OUTS = [ROOT / "web" / "cover.png", ROOT / "site" / "cover.png"]
K = 2
W, H = 1097 * K, 1434 * K
INK = (23, 20, 15)
GREY = (74, 70, 64)
FONTS = Path("C:/Windows/Fonts")
OLD_PAPER = (247, 246, 242)


def font(name, size):
    return ImageFont.truetype(str(FONTS / name), round(size * K))


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


def giraffe():
    """The giraffe alone, on white: the old page colour scaled to white, the old text and frame cut away."""
    old = Image.open(OLD).convert("RGB")
    ow, oh = old.size
    white = Image.new("RGB", old.size, (255, 255, 255))
    px_old, px_new = old.load(), white.load()
    for y in range(24, 1345):
        for x in range(24, ow - 24):
            if y < 515 and x < 600:        # the old title block
                continue
            r, g, b = px_old[x, y]
            px_new[x, y] = tuple(min(255, round(v * 255 / p)) for v, p in zip((r, g, b), OLD_PAPER))
    return white.resize((ow * K, oh * K), Image.LANCZOS)


def make():
    cover = giraffe()
    d = ImageDraw.Draw(cover)

    logo = Image.open(LOGO).convert("RGBA")
    logo = logo.crop(logo.getbbox())
    logo = logo.resize((380 * K, round(logo.height * 380 * K / logo.width)), Image.LANCZOS)
    cover.paste(logo, (80 * K, 84 * K), logo)

    x = 80 * K
    y = 196 * K
    f_title = font("arialbd.ttf", 78)
    for line in ["Refinement-", "Oriented", "Programming"]:
        d.text((x, y), line, font=f_title, fill=INK)
        y += 88 * K
    y += 20 * K
    f_sub = font("arial.ttf", 38)
    for line in wrap(d, "A discipline for software in the agentic era", f_sub, 380):
        d.text((x, y), line, font=f_sub, fill=INK)
        y += 48 * K

    d.text((x, 1362 * K), "MANSOUR AYOUNI", font=font("arialbd.ttf", 32), fill=INK)
    right = "TUNIS · NIAMEY · PARIS · 2026"
    f = font("arialbd.ttf", 27)
    d.text((W - 80 * K - d.textlength(right, font=f), 1366 * K), right, font=f, fill=GREY)

    for out in OUTS:
        out.parent.mkdir(parents=True, exist_ok=True)
        cover.save(out)
        print("wrote", out, cover.size)


if __name__ == "__main__":
    make()
