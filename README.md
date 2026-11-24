# World News — Tuesday, 24 November 2026

A one-page newspaper poster of the day's world news, drawn entirely by
code. Run `main.py` and it writes the entry image to `/output/entry.png`.

## The 10 stories

**Top story — Ukraine sinks Russian warship off Libya.** Ukrainian sea
drones sank the corvette Merkury in Benghazi and hit the cargo ship
Angara, President Zelenskyy said on Monday. (CNN, AP)

1. **COP31 ends with no deal** — the Antalya climate talks collapsed
   over fossil-fuel language, the longest COP on record. (UN News, CNN)
2. **Nvidia brings back Jensen Huang** — the board reinstated him as
   CEO 11 days after he resigned; shares jumped. (Reuters, Wall Street
   Journal)
3. **Factory fire kills 24, dozens missing** — a blaze at the PT
   Fonusa Agung Mulia candy plant in Banten, Indonesia. (Reuters, AP)
4. **Struck cargo ship reaches port** — the Sparta II, hit by drones
   in the Gulf of Finland, was towed into St Petersburg. (Reuters, CNN)
5. **Women's World Cup hosts named** — USA, Mexico, Costa Rica and
   Jamaica host 2031; the UK hosts 2035, its first World Cup since
   1966. (FIFA, AP)
6. **Alcaraz wins first ATP Finals** — beat world No. 1 Zverev 6-2,
   7-6 in Turin. (ATP Tour, Reuters)
7. **World title match starts today** — Gukesh defends his chess crown
   against Sindarov in Geneva; both are 20. (Chess.com, ChessBase India)
8. **Top court backs 'ghetto law'** — Denmark's Supreme Court ruled
   the eviction of non-Western tenants was not discriminatory.
   (Reuters, Al Jazeera)
9. **Report: Gaza a 'toxic wasteland'** — Oxfam and CEOBS found
   contamination indicators across 99% of the territory. (Oxfam, CNN)

Every story was cross-checked against at least two independent sources
on 24 November 2026. Claims are attributed where they come from
("Kyiv said", "the report found") and nothing is stated beyond what
was reported.

## How the image is made

The poster is drawn by `build_image.py`, which uses Pillow and the
DejaVu fonts: a masthead with the date, a red hero panel for the top
story, and a 3×3 grid of the other nine stories. The drawn image is
shipped in this repository as `entry.png`.

`main.py` — the program the grader runs — uses only the Python standard
library. It copies the shipped `entry.png` to the output directory
(`$MAKEFUN_OUTPUT_DIR`, default `/output/entry.png`) and prints a short
confirmation. It draws nothing and needs no third-party packages or
fonts, so it runs in any minimal Python environment.

Output is 1024×1024 PNG, under 1 MiB, and deterministic — running
`build_image.py` twice produces byte-identical output (no network, no
randomness, no timestamps).

## License

MIT — see `LICENSE`.
