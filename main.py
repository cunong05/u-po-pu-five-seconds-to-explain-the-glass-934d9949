#!/usr/bin/env python3
"""Five Seconds to Explain the Glass — make.fun bounty entry.

Writes the single sentence a house cat would say in its own defence
after knocking a glass off the table, to /output/entry.txt.
No dependencies, no network, fully deterministic.

The excuse: the glass was spying on the cat's naps and reporting to
the dog — so the cat gave it one fair trial and sentenced it to the
floor. Pure cat logic: self-interest, zero remorse, no apology,
no confession, and a fresh comic idea (espionage + courtroom).
"""

import os

ENTRY = (
    "The glass had been spying on my naps and reporting to the dog, "
    "so I gave it one fair trial and sentenced it to the floor."
)

OUT_DIR = "/output"
OUT_PATH = os.path.join(OUT_DIR, "entry.txt")


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 200, f"entry must be 1-200 chars, got {len(text)}"
    assert text.count(".") == 1 and text.endswith("."), "entry must be one sentence"
    os.makedirs(OUT_DIR, exist_ok=True)
    with open(OUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
