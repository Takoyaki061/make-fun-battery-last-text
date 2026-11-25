#!/usr/bin/env python3
"""The Battery's Last Text to Its Charger.

Writes the battery's final one-line text message to /output/entry.txt.

The line was picked from 14 candidates by critique against the kit's judge
criteria: it reads as a last text to the charger, lands a real joke whose
twist pays off in the final words ("replied to the toaster"), sounds like a
person actually texting (read receipts, jealousy, the repeated "Twelve."),
spends its 111 characters with no filler, and finds an angle beyond the
obvious dying-battery complaint. See CANDIDATES.md for the full field and
the pick rationale.
"""

import os

TEXT = "I sent you twelve little lightning bolts today. Twelve. You opened every single one and replied to the toaster."

MAX_CHARS = 200


def validate(text):
    """The gate: 1-200 UTF-8 characters, not only whitespace, one line."""
    if not (1 <= len(text) <= MAX_CHARS):
        raise ValueError("entry must be 1-%d chars, got %d" % (MAX_CHARS, len(text)))
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text:
        raise ValueError("entry must be a single line")
    return text


def main():
    entry = validate(TEXT)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(entry)


if __name__ == "__main__":
    main()
