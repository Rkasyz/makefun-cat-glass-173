"""Entry for make.fun competition "Five Seconds to Explain the Glass".

The program writes a single sentence, in a house cat's own voice, to
$MAKEFUN_OUTPUT_DIR/entry.txt. The text is fixed, deterministic and
contains no randomness, timestamps or network access.
"""

import os

ENTRY_TEXT = (
    "The glass and I had a disagreement about its future, and after a "
    "thorough inspection from above I concluded it belonged on the "
    "floor, where it now lives rent-free."
)


def main() -> None:
    # The gate requires 1 to 200 characters of UTF-8 text; fail loudly
    # instead of writing an invalid entry.
    if not 1 <= len(ENTRY_TEXT) <= 200:
        raise ValueError(
            f"entry text is {len(ENTRY_TEXT)} characters, must be 1-200"
        )
    if not ENTRY_TEXT.strip():
        raise ValueError("entry text must not be only whitespace")

    raw_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    output_dir = raw_dir.strip() or "/output"
    os.makedirs(output_dir, exist_ok=True)
    entry_path = os.path.join(output_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY_TEXT)


if __name__ == "__main__":
    main()
