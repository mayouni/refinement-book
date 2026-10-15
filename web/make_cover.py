"""Retouch the Refinement-Oriented Programming cover (web/cover.png, mirrored at site/cover.png).

The author's rulings (2026-10-15): a pure white background; the AYOUNI logo as the corrected SVG (red dot); and the
cover's type as first designed (the larger-type redesign was not wanted). So the cover is the archived flat cover
(assets/covers/archive/2026-07-flat-cover-giraffe.png) with exactly two changes: its off-white page colour mapped to
white, and its baked-in wordmark replaced by the logo (assets/covers/ayouni-logo.png, rasterised from ayouni-logo.svg).
Drawn at twice the size (2194 x 2868). Run: python web/make_cover.py
"""
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
OLD = ROOT / "assets" / "covers" / "archive" / "2026-07-flat-cover-giraffe.png"
LOGO = ROOT / "assets" / "covers" / "ayouni-logo.png"
OUTS = [ROOT / "web" / "cover.png", ROOT / "site" / "cover.png"]
K = 2
OLD_PAPER = (247, 246, 242)
LOGO_BOX = (80, 73, 305, 129)          # where the old wordmark sat (x0, y0, x1, y1), measured on the archived cover


def make():
    im = Image.open(OLD).convert("RGB")
    px = im.load()
    x0, y0, x1, y1 = LOGO_BOX
    for y in range(y0 - 8, y1 + 10):                 # the old wordmark and its dot: painted out
        for x in range(x0 - 8, x1 + 10):
            px[x, y] = OLD_PAPER
    out = Image.new("RGB", im.size)
    po = out.load()
    for y in range(im.height):
        for x in range(im.width):
            po[x, y] = tuple(min(255, round(v * 255 / p)) for v, p in zip(px[x, y], OLD_PAPER))
    out = out.resize((im.width * K, im.height * K), Image.LANCZOS)
    logo = Image.open(LOGO).convert("RGBA")
    logo = logo.crop(logo.getbbox())
    w = (x1 - x0) * K
    logo = logo.resize((w, round(logo.height * w / logo.width)), Image.LANCZOS)
    out.paste(logo, (x0 * K, y0 * K), logo)
    for dest in OUTS:
        dest.parent.mkdir(parents=True, exist_ok=True)
        out.save(dest)
        print("wrote", dest, out.size)


if __name__ == "__main__":
    make()
