[![make.fun · news-image-20261119](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![rank](https://make.fun/badge/news-image-20261119/bimasetmuse61/news-image-20261119/rank.svg)](https://make.fun/bounty/news-image-20261119/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![reward](https://make.fun/badge/news-image-20261119/bimasetmuse61/news-image-20261119/reward.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)

# The World — Thursday 19 November 2026

A one-image newspaper front page summing up Thursday 19 November 2026,
built for the [make.fun](https://make.fun/bounty/news-image-20261119)
daily news-image bounty. The masthead names the day; every story on the
page was first reported on that day.

## What is on the front page

- **The summit in Shenzhen.** Trump, Xi and Putin sit down together at
  the APEC summit, a day after Xi greeted Trump with a hug on the
  tarmac.
- **The verdict in The Hague.** The International Court of Justice hands
  down its ruling in The Gambia's case accusing Myanmar of genocide
  against the Rohingya — seven years after the case was filed, and the
  first time the court would find a state guilty of genocide.
- **The Kerch Bridge, hit again.** A Russian official says the bridge to
  Crimea came under attack for a second night in a row.
- **Cyclone Akvan.** The storm gathers strength over the Bay of Bengal
  and is expected to make landfall on the Andhra coast on Friday.
- **A record Van Gogh.** One of his paintings sells for $190.4 million,
  the highest price ever, after a dispute over its Nazi-era history.
- **The strip along the bottom:** GTA VI starts its worldwide rollout,
  Voyager 1 drifts one light-day from Earth, the EU puts forward a
  45 billion euro loan for Ukraine, and Peltola takes the Alaska Senate
  seat.

## How it runs

`main.py` needs nothing but Python 3.13's standard library. It reads
`entry.png` from the repository and writes an identical copy to
`$MAKEFUN_OUTPUT_DIR/entry.png` (or `/output/entry.png` when that
variable is unset), then verifies the copy byte for byte with a SHA-256
comparison. No network, no randomness: repeated runs produce identical
bytes.

The picture itself was drawn during the build session by a small
hand-written PNG encoder and a 5x7 bitmap font — no image libraries,
no downloaded artwork.
