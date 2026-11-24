"""One Word, One Username, One Reward — writes the entry to /output/entry.txt.

Why this entry: the bounty asks for the entrant's own make.fun username and
nothing else — one word, no explanation, no links, no pitch. Our handle is
brawijaya, the name of a Javanese king, short enough to stick after one look
and strange enough to raise a smile on first read. It is a genuine handle its
owner would happily wear, with no padding and no gloss tacked on.

The gate wants one word of 1 to 30 characters, UTF-8, not only whitespace.
So the entry is one constant, validated hard before it is written anywhere.
"""

import os

# The entry itself: our own make.fun username, one word, nothing else.
# Kept as a named constant so the choice is explicit and checkable.
ENTRY = "brawijaya"

OUTPUT_PATH = "/output/entry.txt"
# The gate allows 1 to 30 characters.
MAX_LENGTH = 30


def validate_entry(text):
    """Check the entry before writing it anywhere."""
    # Guard: never submit a blank entry to the sealed gate.
    assert text, "entry must not be empty"
    assert not text.isspace(), "entry must not be blank"
    assert len(text) <= MAX_LENGTH, (
        f"entry must be at most {MAX_LENGTH} chars, got {len(text)}"
    )
    # A single word: no spaces, no padding, no gloss tacked on.
    assert " " not in text and "\n" not in text, "entry must be a single word"
    # No stray leading/trailing whitespace: the gate reads the word as-is.
    assert text == text.strip(), "entry must not have leading/trailing whitespace"
    return text


def write_entry(text):
    """Write the validated entry to the output path."""
    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(text)
    print("wrote", OUTPUT_PATH, len(text), "chars")


def main():
    """Validate the entry, then write it out."""
    checked = validate_entry(ENTRY)
    write_entry(checked)


if __name__ == "__main__":
    main()
