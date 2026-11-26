#!/usr/bin/env python3
"""Deadpan Forecasts for Cities That Do Not Exist.

Prints one deadpan weather-forecast line for Brindlewick, a city that
does not exist, and writes that same line to /output/entry.txt.

Pure Python 3.13 standard library. Deterministic: no randomness, no
clock, no network, no environment-dependent output. The forecast line
is a fixed string, so every run prints exactly the same line.
"""

from __future__ import annotations

import os
import sys

FORECAST = (
    "In Brindlewick, a high of 12 degrees with scattered showers of "
    "lost luggage, clearing by evening once the clouds have apologised."
)


def main() -> int:
    line = FORECAST.strip()
    print(line)
    for target in ("/output/entry.txt", os.path.join("output", "entry.txt")):
        try:
            os.makedirs(os.path.dirname(target), exist_ok=True)
            with open(target, "w", encoding="utf-8") as handle:
                handle.write(line + "\n")
            break
        except OSError:
            continue
    return 0


if __name__ == "__main__":
    sys.exit(main())
