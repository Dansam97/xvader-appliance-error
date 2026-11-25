#!/usr/bin/env python3
"""Entry for make.fun bounty u-xvader-the-funniest-honest-appliance-error-adec4450
(The Funniest Honest Appliance Error).

Writes one line to entry.txt in the output directory: an honest error
message a washing machine could plausibly show. The fault is real — an
unbalanced load makes a washer vibrate and "walk" across the floor — and
the line is written in the machine's own flat, put-upon voice.
"""

import os

ENTRY_TEXT = (
    "ERROR E9: Load unbalanced. I have walked half a metre across the floor "
    "again. If I reach the door, I am leaving."
)


MAX_CHARS = 200  # kit gate: entry.txt must be 1..200 characters, one line


def validated_text() -> str:
    """Return ENTRY_TEXT after checking it against the kit gate."""
    if "\n" in ENTRY_TEXT or "\r" in ENTRY_TEXT:
        raise ValueError("entry must be a single line")
    if not 1 <= len(ENTRY_TEXT) <= MAX_CHARS:
        raise ValueError(f"entry must be 1..{MAX_CHARS} characters")
    if not ENTRY_TEXT.strip():
        raise ValueError("entry must not be only whitespace")
    ENTRY_TEXT.encode("utf-8")  # raises if not UTF-8 encodable
    return ENTRY_TEXT


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # newline="\n" keeps the line ending identical on every platform/run.
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(validated_text() + "\n")


if __name__ == "__main__":
    main()
