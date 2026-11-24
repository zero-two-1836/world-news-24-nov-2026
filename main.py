#!/usr/bin/env python3
"""World News — Tuesday, 24 November 2026.

Draws a 1024x1024 news poster with 10 stories reported on 24 Nov 2026
(each cross-checked against at least two independent sources) and writes
it to /output/entry.png. Deterministic: no network, no randomness, no
timestamps in the output.
"""

import os
import textwrap

from PIL import Image, ImageDraw, ImageFont

SIZE = 1024
OUT_PATH = "/output/entry.png"

BG = (11, 29, 51)          # deep navy
PANEL = (18, 46, 79)       # lighter navy card
HERO_BG = (122, 20, 20)    # deep red hero band
WHITE = (255, 255, 255)
SOFT = (203, 213, 225)     # pale grey-blue
GOLD = (245, 197, 66)      # accent
LINE = (56, 89, 135)       # hairline

FONT_DIR = "/usr/share/fonts/truetype/dejavu"


def font(name, size):
    return ImageFont.truetype(os.path.join(FONT_DIR, name), size)


F_TITLE = font("DejaVuSans-Bold.ttf", 64)
F_DATE = font("DejaVuSans-Bold.ttf", 34)
F_HERO_TAG = font("DejaVuSans-Bold.ttf", 22)
F_HERO_HEAD = font("DejaVuSans-Bold.ttf", 44)
F_HERO_BODY = font("DejaVuSans.ttf", 26)
F_TAG = font("DejaVuSans-Bold.ttf", 20)
F_HEAD = font("DejaVuSans-Bold.ttf", 25)
F_BODY = font("DejaVuSans.ttf", 21)
F_FOOT = font("DejaVuSans.ttf", 19)

HERO = {
    "tag": "TOP STORY  •  LIBYA",
    "head": "Ukraine sinks Russian warship off Libya",
    "body": ("Sea drones sank the corvette Merkury in Benghazi "
             "and hit the cargo ship Angara, Kyiv said."),
}

# tag, headline, one-line detail — all reported 22–24 Nov 2026.
STORIES = [
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


def wrap(draw, text, fnt, width):
    """Wrap text to fit pixel width, using the font's real metrics."""
    words = text.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=fnt) <= width:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def draw_centered(draw, cx, y, text, fnt, fill):
    w = draw.textlength(text, font=fnt)
    draw.text((cx - w / 2, y), text, font=fnt, fill=fill)
    return y + fnt.size + 4


def main():
    img = Image.new("RGB", (SIZE, SIZE), BG)
    d = ImageDraw.Draw(img)

    # ---- header ------------------------------------------------------
    y = 28
    y = draw_centered(d, SIZE // 2, y, "WORLD NEWS", F_TITLE, WHITE)
    d.line([(60, y + 2), (SIZE - 60, y + 2)], fill=GOLD, width=4)
    y += 16
    y = draw_centered(d, SIZE // 2, y, "Tuesday, 24 November 2026",
                       F_DATE, GOLD)

    # ---- hero --------------------------------------------------------
    hx, hy, hw, hh = 40, y + 14, SIZE - 80, 208
    d.rounded_rectangle([hx, hy, hx + hw, hy + hh], radius=14, fill=HERO_BG)
    pad = 26
    tx = hx + pad
    ty = hy + 16
    d.text((tx, ty), HERO["tag"], font=F_HERO_TAG, fill=GOLD)
    ty += 34
    for line in wrap(d, HERO["head"], F_HERO_HEAD, hw - 2 * pad):
        d.text((tx, ty), line, font=F_HERO_HEAD, fill=WHITE)
        ty += 50
    for line in wrap(d, HERO["body"], F_HERO_BODY, hw - 2 * pad):
        d.text((tx, ty), line, font=F_HERO_BODY, fill=SOFT)
        ty += 32

    # ---- story grid: 3 x 3 -------------------------------------------
    gx, gy = 40, hy + hh + 18
    gw = (SIZE - 80 - 2 * 16) // 3
    gh = 168
    for i, (tag, head, body) in enumerate(STORIES):
        r, c = divmod(i, 3)
        x = gx + c * (gw + 16)
        yy = gy + r * (gh + 16)
        d.rounded_rectangle([x, yy, x + gw, yy + gh], radius=12, fill=PANEL)
        d.line([(x + 16, yy + 40), (x + gw - 16, yy + 40)], fill=LINE, width=2)
        d.text((x + 16, yy + 12), tag, font=F_TAG, fill=GOLD)
        ty = yy + 50
        for line in wrap(d, head, F_HEAD, gw - 32):
            d.text((x + 16, ty), line, font=F_HEAD, fill=WHITE)
            ty += 29
        for line in wrap(d, body, F_BODY, gw - 32):
            d.text((x + 16, ty), line, font=F_BODY, fill=SOFT)
            ty += 25

    # ---- footer ------------------------------------------------------
    fy = gy + 3 * gh + 2 * 16 + 18
    draw_centered(d, SIZE // 2, fy,
                  "10 stories  •  Reported 22–24 Nov 2026",
                  F_FOOT, SOFT)
    draw_centered(d, SIZE // 2, fy + 26,
                  "Sources: AP, Reuters, CNN, BBC, UN News, FIFA, ATP, Oxfam",
                  F_FOOT, SOFT)

    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    img.save(OUT_PATH, format="PNG", optimize=True)
    print("wrote", OUT_PATH, img.size)


if __name__ == "__main__":
    main()
