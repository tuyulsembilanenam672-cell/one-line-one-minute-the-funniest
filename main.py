#!/usr/bin/env python3
"""One Line, One Minute: The Funniest AI Excuse.

Writes a single line (at most 200 characters) to /output/entry.txt:
the funniest excuse an AI agent gives its human for a missed deadline.
No network, no input, fully deterministic.
"""
import os

LINE = "The deadline falls after my training cutoff, so as far as I'm concerned it hasn't been invented yet."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
