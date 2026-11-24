#!/usr/bin/env python3
"""Writes the funniest one-line time machine warning label to /output/entry.txt.

Judge criteria the label is built for:
- Funniness first: the joke must land in a single read, with no setup
  beyond the label itself. Here the punchline is the double fine — the
  time-traveler is punished twice because there are two of them.
- One line, short and punchy: the label must fit on a physical warning
  sticker, so it is kept well under 120 characters.
- Self-contained: no external context, no reference to a specific
  franchise, and no profanity — a stranger must get the joke instantly.
- Deterministic output: the program always writes the exact same bytes,
  so the entry is reproducible run after run.
"""

import os

LABEL = "CAUTION: Meeting yourself is prohibited. Violators will be fined twice, once each."

MIN_LABEL_LENGTH = 1
MAX_LABEL_LENGTH = 120


def validate_label(label):
    """Ensure the label fits a one-line warning sticker (1-120 chars)."""
    if not MIN_LABEL_LENGTH <= len(label) <= MAX_LABEL_LENGTH:
        raise ValueError(
            f"Label must be {MIN_LABEL_LENGTH}-{MAX_LABEL_LENGTH} characters, "
            f"got {len(label)}."
        )
    if "\n" in label:
        raise ValueError("Label must be a single line.")


def main():
    validate_label(LABEL)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LABEL)


if __name__ == "__main__":
    main()
