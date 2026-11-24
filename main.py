"""One word from your ex.

Exactly one word, the word the ex would use to describe the entrant,
written bare to /output/entry.txt with no extra text around it.
"""

import os

WORD = "Whatever"

OUT_DIR = "/output"
OUT_FILE = os.path.join(OUT_DIR, "entry.txt")


def main():
    # The gate allows 1 to 24 characters and rejects whitespace-only text.
    if not (1 <= len(WORD) <= 24) or not WORD.strip():
        raise SystemExit("word fails the gate")
    os.makedirs(OUT_DIR, exist_ok=True)
    with open(OUT_FILE, "w", encoding="utf-8") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
