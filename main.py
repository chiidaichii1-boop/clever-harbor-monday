"""One Star for Monday — make.fun entry.

Writes a one-star review of Monday, as if Monday were a restaurant,
to /output/entry.txt. Pure standard library.
"""

import os

ENTRY = "One star. The server lost my weekend, served a lukewarm Monday, and still expected a tip."
# Verified: 89 characters (gate 1-180), 16 words (gate at most 25).


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)

    text = ENTRY.strip()
    words = text.split()
    assert 1 <= len(text) <= 180, f"entry must be 1-180 chars, got {len(text)}"
    assert len(words) <= 25, f"entry must be at most 25 words, got {len(words)}"
    assert text.strip(), "entry must not be only whitespace"
    assert "\n" not in text, "entry must be a single line"

    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
