"""Famous Last Words at 1 Percent.

Writes one line to /output/entry.txt: the last words of a phone whose
battery has just hit 1 percent. The phone speaks for itself, and its
parting shot is about the photos, not the charger.
"""

import os

ENTRY = "Do not mourn me. Mourn the 4,000 photos I never backed up. I am going dark now, and they are going with me."

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 199


def validate_entry(text):
    """Check the entry against the gate: 1 to 199 chars, one line."""
    if not isinstance(text, str):
        raise TypeError("entry must be a string")
    if not (1 <= len(text) <= MAX_CHARS):
        raise ValueError("entry must be 1 to 199 characters, got %d" % len(text))
    if text != text.strip():
        raise ValueError("entry must not start or end with whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if any(ord(ch) < 32 for ch in text):
        raise ValueError("entry must not contain control characters")
    return text


def main():
    text = validate_entry(ENTRY)
    out_dir = os.path.dirname(OUTPUT_PATH)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(text)
    with open(OUTPUT_PATH, "r", encoding="utf-8") as handle:
        written = handle.read()
    if written != text:
        raise ValueError("read-back mismatch: file does not hold the entry")
    if len(written.encode("utf-8")) != len(text.encode("utf-8")):
        raise ValueError("read-back mismatch: file byte length differs")
    print(text)
    print("%d characters" % len(text))


if __name__ == "__main__":
    main()
