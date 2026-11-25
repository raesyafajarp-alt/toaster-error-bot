#!/usr/bin/env python3
"""The Funniest Toaster Error Message.

Writes one line, the error message a kitchen toaster shows its owner,
to /output/entry.txt. Deterministic: the same line on every run.
"""

import os

ENTRY = "ERROR: I BURNED IT ON PURPOSE. YOU KEEP PRESSING THE SAME BUTTON."

OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
