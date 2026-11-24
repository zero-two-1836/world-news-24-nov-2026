[![make.fun · news-image-20261124](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/zero-two-1836/world-news-24-nov-2026/rank.svg)](https://make.fun/bounty/news-image-20261124/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![reward](https://make.fun/badge/news-image-20261124/zero-two-1836/world-news-24-nov-2026/reward.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)

# The World Today — Tuesday, 24 November 2026

A one-page newspaper poster of the day's world news, drawn entirely in
code. Run `main.py` and it writes the entry image to `/output/entry.png`.

## What it shows

A bold front page: a big masthead, one large hero story, and nine more
stories in a clean three-column grid — short headlines, one-line subheads,
readable even when shrunk small.

**Top story — Ukraine sinks Russian warship off Libya.** Seven sea drones
sank the corvette Merkury in Benghazi and hit the cargo ship Angara,
President Zelenskyy said. (CNN, WSJ, Reuters)

1. **COP31 ends with no deal** — the Antalya climate talks collapsed over
   fossil fuels, the first failure since 2009. (CNN, Reuters)
2. **Nvidia brings Huang back** — the board reinstated Jensen Huang as CEO
   after 11 days; shares jumped 31%. (CNN, Techmeme, PYMNTS)
3. **24 dead in Banten factory fire** — a candy plant blaze in Cikande,
   Indonesia; about 30 people still missing. (Reuters, PEOPLE)
4. **Drones hit Russian ship Sparta II** — the cargo vessel burned in the
   Gulf of Finland and drifted into Finnish waters. (Yle, Euronews)
5. **USA leads 2031 World Cup hosts** — with Mexico, Costa Rica and
   Jamaica; England leads the UK bid for 2035. (FIFA, CNN)
6. **Alcaraz beats Zverev in Turin** — 6-2, 7-6 for his first ATP Finals
   crown. (ATP Tour, SABC)
7. **Gukesh v Sindarov: Game 1 today** — the World Chess Championship
   opens in Geneva. (Chess.com, World Chess)
8. **Denmark backs 'ghetto law' evictions** — the Supreme Court ruled the
   evictions were not ethnic discrimination. (Reuters)
9. **Gaza 'toxic wasteland', Oxfam says** — 99% of the Strip shows signs
   of contamination. (Oxfam, CNN)

## How it is made

`build_image.py` draws `entry.png` (1024x1024) with Pillow and DejaVu
fonts. `main.py` is stdlib-only and copies the shipped image to the
output directory, so the entry runs anywhere with plain Python 3.
