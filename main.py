#!/usr/bin/env python3
"""Laugh Track: The Crypto Trading Joke Contest — make.fun entry.

Writes one original one-line joke about crypto/trading life
(140 characters, valid UTF-8) to /output/entry.txt.

The joke: a trader sets a stop-loss, keeps moving it down, then
deletes it and blames the market — the setup is a behaviour every
trader recognises, the turn lands at the end ("grief with extra
steps"). Pure Python standard library only; no third-party packages,
no network, no file reads outside this script.
"""

import os

JOKE = (
    "I set a stop-loss, moved it down twice, then deleted it and "
    "blamed the market \u2014 turns out my risk management is just "
    "grief with extra steps."
)


def main() -> None:
    # The sealed scorer gates on 1-200 chars of UTF-8 text, not only
    # whitespace. Fail loudly here rather than ship an entry the
    # gate would refuse.
    assert 1 <= len(JOKE) <= 200, "joke must be 1-200 characters"
    assert JOKE.strip(), "joke must not be only whitespace"
    assert "\n" not in JOKE, "joke must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
