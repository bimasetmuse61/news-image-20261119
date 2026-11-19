#!/usr/bin/env python3
"""news-image-20261119: sum up the world news of Thursday 19 November 2026.

The entry is the front-page image entry.png that sits next to this file
(it was drawn during the build session: lead story Trump-Xi-Putin
trilateral summit in Shenzhen, the ICJ verdict on Myanmar's Rohingya
genocide case, Ukraine striking the Kerch Bridge again, Cyclone Akvan
closing in, a Van Gogh selling for a record $190.4m, plus GTA VI's
global rollout, Voyager 1 reaching one light-day, the EU's 45bn euro
Ukraine loan and Peltola winning Alaska in the strip).

Running this program copies that image, unchanged, into the folder the
harness provides ($MAKEFUN_OUTPUT_DIR, or /output when unset). Standard
library only, no network, no randomness: every run writes identical bytes.
"""

import os
import shutil
from pathlib import Path


def main():
    here = Path(__file__).resolve().parent
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    src = here / "entry.png"
    dst = out_dir / "entry.png"
    shutil.copyfile(src, dst)
    # Guard the gate's byte-identical rule: the copy must match the source.
    if dst.stat().st_size != src.stat().st_size:
        raise SystemExit("entry.png copy size mismatch")


if __name__ == "__main__":
    main()
