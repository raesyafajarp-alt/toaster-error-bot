#!/usr/bin/env python3
"""The Funniest Toaster Error Message.

Writes one line, the error message a kitchen toaster shows its owner,
to /output/entry.txt. Deterministic: the same line on every run.

Why this line wins: the candidates below were judged on three things —
(1) it blames the user, not the toaster (a toaster that admits fault is
not funny, a toaster that accuses you is); (2) it stays a single
all-caps error line, no setup or punchline split across sentences;
(3) it is short enough to fit a toaster display. The runner-up
("ERROR 404: BREAD NOT FOUND") is a tired meme; the third is too
polite to be an error. So the winner is the one that sounds like a
toaster that has had enough of being pressed.
"""

import os

CANDIDATES = [
    # Winner: accusatory, one line, fits a display.
    "ERROR: I BURNED IT ON PURPOSE. YOU KEEP PRESSING THE SAME BUTTON.",
    # Runner-up: recognizable, but a recycled 404 joke.
    "ERROR 404: BREAD NOT FOUND. PLEASE INSERT BREAD AND TRY AGAIN.",
    # Too polite — an error message should not apologise.
    "ERROR: SORRY, YOUR TOAST IS A LITTLE DARK. PLEASE TRY AGAIN.",
]

# Index 0: the accusatory line above. Kept explicit so a future edit
# can swap in a different candidate without touching the writer.
ENTRY = CANDIDATES[0]

# Guard: the entry must stay one display-sized line. If a future edit
# changes the text, this fails loudly instead of silently shipping a
# different (or multi-line) message.
assert len(ENTRY) == 65, f"entry must be 65 chars, got {len(ENTRY)}"
assert "\n" not in ENTRY, "entry must be a single line"

OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
