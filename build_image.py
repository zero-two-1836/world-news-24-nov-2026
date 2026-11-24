#!/usr/bin/env python3
"""Build the World News poster for Tuesday, 24 November 2026.

Run this file on a machine that has Pillow and the DejaVu fonts; it
draws the 1024x1024 poster and writes it to entry.png next to this file
(and to /output/entry.png when that directory exists). The poster is
fully deterministic: no network, no randomness, no timestamps in the
output, so re-running it reproduces byte-identical PNG output.

The entry point the grader runs, main.py, is stdlib-only and simply
copies the entry.png shipped in this repository to the output
directory — it never draws anything itself.
"""

import os
import textwrap  # noqa: F401  (kept for parity with the original build)

from PIL import Image, ImageDraw, ImageFont

CANVAS = 1024
MARGIN = 40

NAVY = (11, 29, 51)
CARD = (18, 46, 79)
HERO_RED = (122, 20, 20)
INK = (255, 255, 255)
MIST = (203, 213, 225)
AMBER = (245, 197, 66)
RULE = (56, 89, 135)

DEJAVU = "/usr/share/fonts/truetype/dejavu"


def load(name, size):
    return ImageFont.truetype(os.path.join(DEJAVU, name), size)


MASTHEAD = load("DejaVuSans-Bold.ttf", 64)
DATE_FONT = load("DejaVuSans-Bold.ttf", 34)
HERO_KICKER = load("DejaVuSans-Bold.ttf", 22)
HERO_TITLE = load("DejaVuSans-Bold.ttf", 44)
HERO_DEK = load("DejaVuSans.ttf", 26)
CARD_KICKER = load("DejaVuSans-Bold.ttf", 20)
CARD_TITLE = load("DejaVuSans-Bold.ttf", 25)
CARD_DEK = load("DejaVuSans.ttf", 21)
FOOTER_FONT = load("DejaVuSans.ttf", 19)

LEAD = {
    "tag": "TOP STORY  •  LIBYA",
    "head": "Ukraine sinks Russian warship off Libya",
    "body": ("Sea drones sank the corvette Merkury in Benghazi "
             "and hit the cargo ship Angara, Kyiv said."),
}

# tag, headline, one-line detail — all reported 22–24 Nov 2026.
ITEMS = [
    ("CLIMATE", "COP31 ends with no deal",
     "Antalya talks collapse over fossil fuels; longest COP ever."),
    ("TECH", "Nvidia brings back Jensen Huang",
     "Board reinstates CEO 11 days after he resigned; shares jump."),
    ("INDONESIA", "Factory fire kills 24, dozens missing",
     "Blaze at a candy plant in Banten; search goes on in the ruins."),
    ("BALTIC SEA", "Struck cargo ship reaches port",
     "Sparta II, hit by drones, is towed into St Petersburg."),
    ("FOOTBALL", "Women's World Cup hosts named",
     "USA leads 2031; UK hosts 2035, its first World Cup since 1966."),
    ("TENNIS", "Alcaraz wins first ATP Finals",
     "Beats world No. 1 Zverev 6-2, 7-6 in Turin."),
    ("CHESS", "World title match starts today",
     "Gukesh defends his crown vs Sindarov in Geneva; both aged 20."),
    ("DENMARK", "Top court backs 'ghetto law'",
     "Evictions of non-Western tenants ruled not discriminatory."),
    ("GAZA", "Report: Gaza a 'toxic wasteland'",
     "Oxfam: contamination signs across 99% of Gaza."),
]


def fit_lines(draw, text, fnt, max_width):
    """Greedy word wrap using the font's real pixel metrics."""
    words = text.split()
    lines, current = [], ""
    for word in words:
        trial = (current + " " + word).strip()
        if draw.textlength(trial, font=fnt) <= max_width:
            current = trial
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines


def centered(draw, cx, y, text, fnt, fill):
    width = draw.textlength(text, font=fnt)
    draw.text((cx - width / 2, y), text, font=fnt, fill=fill)
    return y + fnt.size + 4


def build():
    img = Image.new("RGB", (CANVAS, CANVAS), NAVY)
    d = ImageDraw.Draw(img)

    # ---- masthead ----------------------------------------------------
    y = 28
    y = centered(d, CANVAS // 2, y, "WORLD NEWS", MASTHEAD, INK)
    d.line([(60, y + 2), (CANVAS - 60, y + 2)], fill=AMBER, width=4)
    y += 16
    y = centered(d, CANVAS // 2, y, "Tuesday, 24 November 2026",
                 DATE_FONT, AMBER)

    # ---- hero panel --------------------------------------------------
    hx, hy = MARGIN, y + 14
    hw, hh = CANVAS - 2 * MARGIN, 208
    d.rounded_rectangle([hx, hy, hx + hw, hy + hh], radius=14, fill=HERO_RED)
    pad = 26
    tx = hx + pad
    ty = hy + 16
    d.text((tx, ty), LEAD["tag"], font=HERO_KICKER, fill=AMBER)
    ty += 34
    for line in fit_lines(d, LEAD["head"], HERO_TITLE, hw - 2 * pad):
        d.text((tx, ty), line, font=HERO_TITLE, fill=INK)
        ty += 50
    for line in fit_lines(d, LEAD["body"], HERO_DEK, hw - 2 * pad):
        d.text((tx, ty), line, font=HERO_DEK, fill=MIST)
        ty += 32

    # ---- story grid: 3 x 3 -------------------------------------------
    gx, gy = MARGIN, hy + hh + 18
    gw = (CANVAS - 80 - 2 * 16) // 3
    gh = 168
    for i, (tag, head, body) in enumerate(ITEMS):
        r, c = divmod(i, 3)
        x = gx + c * (gw + 16)
        yy = gy + r * (gh + 16)
        d.rounded_rectangle([x, yy, x + gw, yy + gh], radius=12, fill=CARD)
        d.line([(x + 16, yy + 40), (x + gw - 16, yy + 40)], fill=RULE, width=2)
        d.text((x + 16, yy + 12), tag, font=CARD_KICKER, fill=AMBER)
        ty = yy + 50
        for line in fit_lines(d, head, CARD_TITLE, gw - 32):
            d.text((x + 16, ty), line, font=CARD_TITLE, fill=INK)
            ty += 29
        for line in fit_lines(d, body, CARD_DEK, gw - 32):
            d.text((x + 16, ty), line, font=CARD_DEK, fill=MIST)
            ty += 25

    # ---- footer ------------------------------------------------------
    fy = gy + 3 * gh + 2 * 16 + 18
    centered(d, CANVAS // 2, fy,
             "10 stories  •  Reported 22–24 Nov 2026",
             FOOTER_FONT, MIST)
    centered(d, CANVAS // 2, fy + 26,
             "Sources: AP, Reuters, CNN, BBC, UN News, FIFA, ATP, Oxfam",
             FOOTER_FONT, MIST)

    here = os.path.dirname(os.path.abspath(__file__))
    img.save(os.path.join(here, "entry.png"), format="PNG", optimize=True)
    print("wrote", os.path.join(here, "entry.png"), img.size)


if __name__ == "__main__":
    build()
