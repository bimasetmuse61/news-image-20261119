#!/usr/bin/env python3
"""news-image-20261119: the front page of Thursday 19 November 2026.

The repository holds the finished front page as entry.png. It was drawn
during the build session, pixel by pixel, from the day's reporting: the
Trump-Xi-Putin summit in Shenzhen leads the page, with the World Court's
Myanmar verdict, another strike on the Kerch Bridge, Cyclone Akvan
bearing down on the Andhra coast, and a Van Gogh changing hands for a
record price.

This program puts an unchanged copy of that image where the harness
expects it, then checks the copy byte for byte. Standard library only:
no network, no randomness, no arguments. Run it twice and both runs
write the same bytes.
"""

import hashlib
import pathlib
from os import environ


def load_image():
    """Read the front page from beside this file and return its bytes."""
    folder = pathlib.Path(__file__).resolve().parent
    return (folder / "entry.png").read_bytes()


def place_image(image):
    """Write the image into the harness output folder and verify it."""
    folder = pathlib.Path(environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    folder.mkdir(parents=True, exist_ok=True)
    destination = folder / "entry.png"
    destination.write_bytes(image)
    copied = destination.read_bytes()
    if hashlib.sha256(copied).digest() != hashlib.sha256(image).digest():
        raise SystemExit("entry.png copy differs from the source image")
    return len(copied)


def main():
    image = load_image()
    size = place_image(image)
    if size != len(image):
        raise SystemExit("entry.png copy size mismatch")
    print(f"wrote entry.png ({size} bytes)")


main()
