#!/usr/bin/env python3
"""Draw the 24 Nov 2026 world-news front page (1024x1024 PNG).

Fresh artwork, drawn entirely in code with Pillow. No external assets,
no timestamps, no randomness: two runs produce byte-identical output.
"""
import os
from PIL import Image, ImageDraw, ImageFont

W = H = 1024
FONT_DIR = "/usr/share/fonts/truetype/dejavu"

SERIF_B = os.path.join(FONT_DIR, "DejaVuSerif-Bold.ttf")
SANS = os.path.join(FONT_DIR, "DejaVuSans.ttf")
SANS_B = os.path.join(FONT_DIR, "DejaVuSans-Bold.ttf")

PAPER = (250, 247, 238)
INK = (18, 18, 18)
RED = (190, 16, 36)
GOLD = (232, 185, 60)
NAVY = (16, 42, 74)
SEA = (24, 68, 110)
GREY = (110, 108, 100)
LIGHT_GREY = (210, 206, 196)


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_w):
    """Greedy word wrap; returns a list of lines that fit max_w."""
    words = text.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
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
    return y + fnt.size


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    # ---- Masthead -------------------------------------------------------
    d.rectangle([0, 0, W, 118], fill=(12, 12, 12))
    draw_centered(d, W // 2, 14, "THE WORLD TODAY",
                  font(SERIF_B, 62), (255, 255, 255))
    draw_centered(d, W // 2, 84, "TUESDAY, 24 NOVEMBER 2026",
                  font(SANS_B, 27), GOLD)
    d.rectangle([0, 118, W, 122], fill=RED)

    # ---- Hero -----------------------------------------------------------
    d.text((32, 142), "TOP STORY  ·  LIBYA", font=font(SANS_B, 24), fill=RED)
    hero_lines = ["UKRAINE SINKS", "RUSSIAN WARSHIP", "OFF LIBYA"]
    y = 178
    for line in hero_lines:
        y = draw_centered(d, W // 2, y, line, font(SERIF_B, 58), INK) + 2
    sub = ("Seven sea drones sank the corvette Merkury in Benghazi "
           "and hit the cargo ship Angara, Zelenskyy said.")
    sub_lines = wrap(d, sub, font(SANS, 23), 880)
    y = 372
    for line in sub_lines:
        y = draw_centered(d, W // 2, y, line, font(SANS, 23), (52, 52, 52)) + 2

    # Sea strip: simple sinking-ship silhouette under the hero text.
    d.rectangle([0, 452, W, 500], fill=SEA)
    d.rectangle([0, 452, W, 456], fill=NAVY)
    # hull, tilted as if listing
    d.polygon([(380, 478), (640, 478), (610, 496), (410, 496)], fill=(10, 10, 10))
    d.rectangle([470, 452, 478, 478], fill=(10, 10, 10))
    d.rectangle([540, 458, 548, 478], fill=(10, 10, 10))
    # smoke puffs rising from the ship, kept inside the sea strip
    for cx, cy, r in [(500, 464, 10), (522, 456, 13), (548, 464, 9)]:
        d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(200, 200, 200))
    # drone dots in the sky of the strip
    for cx, cy in [(820, 468), (860, 462), (900, 470)]:
        d.ellipse([cx - 4, cy - 4, cx + 4, cy + 4], fill=GOLD)
    d.text((32, 462), "BENGHAZI  ·  SEVEN SEA DRONES",
           font=font(SANS_B, 18), fill=(255, 255, 255))
    d.rectangle([0, 500, W, 506], fill=RED)

    # ---- Nine stories: 3 x 3 grid --------------------------------------
    stories = [
        ("CLIMATE", "COP31 ends with no deal",
         "Antalya talks fail on fossil fuels \u2014 first collapse since 2009."),
        ("TECH", "Nvidia brings Huang back",
         "Shares jump 31% as the board reinstates its CEO after 11 days."),
        ("INDONESIA", "24 dead in Banten factory fire",
         "Candy plant blaze in Cikande; about 30 people still missing."),
        ("BALTIC SEA", "Drones hit Russian ship Sparta II",
         "Burning ship drifts into Finnish waters; towed out on Sunday."),
        ("FOOTBALL", "USA leads 2031 World Cup hosts",
         "Mexico, Costa Rica, Jamaica join 2031; England leads 2035."),
        ("TENNIS", "Alcaraz beats Zverev in Turin",
         "Wins 6-2, 7-6 for his first year-end crown."),
        ("CHESS", "Gukesh v Sindarov: Game 1 today",
         "Champion defends his title in Geneva; 14 games, $2.5m prize."),
        ("DENMARK", "Denmark backs \u2018ghetto law\u2019 evictions",
         "Top court says evictions were not ethnic discrimination."),
        ("GAZA", "Gaza \u2018toxic wasteland\u2019, Oxfam says",
         "99% of the Strip shows contamination signs, report finds."),
    ]
    margin, gap = 28, 20
    cell_w = (W - 2 * margin - 2 * gap) // 3
    cell_h = 148
    top = 528
    for i, (kicker, head, sub) in enumerate(stories):
        col, row = i % 3, i // 3
        x = margin + col * (cell_w + gap)
        yy = top + row * (cell_h + 8)
        d.text((x, yy), kicker, font=font(SANS_B, 17), fill=RED)
        head_lines = wrap(d, head, font(SERIF_B, 25), cell_w)
        hy = yy + 26
        for line in head_lines[:2]:
            d.text((x, hy), line, font=font(SERIF_B, 25), fill=INK)
            hy += 30
        sub_lines = wrap(d, sub, font(SANS, 18), cell_w)
        sy = hy + 4
        for line in sub_lines[:2]:
            d.text((x, sy), line, font=font(SANS, 18), fill=(64, 64, 64))
            sy += 22
        if row < 2:
            d.line([(x, yy + cell_h + 2), (x + cell_w, yy + cell_h + 2)],
                   fill=LIGHT_GREY, width=1)

    # ---- Footer ---------------------------------------------------------
    d.rectangle([0, 992, W, 994], fill=LIGHT_GREY)
    draw_centered(d, W // 2, 1000,
                  "Reported 22\u201324 Nov 2026  ·  Sources: CNN \u00b7 Reuters \u00b7 WSJ \u00b7 ATP \u00b7 FIFA \u00b7 Oxfam \u00b7 Yle",
                  font(SANS, 15), GREY)

    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
    img.save(out, "PNG")
    print("wrote", out)


if __name__ == "__main__":
    main()
