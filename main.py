"""make.fun entry: One Line, One Minute — The Vending Machine Pickup Line Contest.

A vending machine flirts with a passing human. The program writes the
entry line to /output/entry.txt (or ./output/entry.txt when /output is
not writable), after passing the gate check.
"""

import os
import sys

ENTRY_LINE = (
    "Hey, beautiful — my coils only spin for you, and I've been humming "
    "your name all day. Got exact change? Because you're the snack I "
    "can't stop craving."
)

MAX_CHARS = 200


def gate_check(text):
    """Return True only if text passes the competition gate.

    The gate: UTF-8 text of 1 to 200 characters, not only whitespace,
    and a single line.
    """
    if not isinstance(text, str):
        return False
    if not text or text.strip() == "":
        return False
    if len(text) > MAX_CHARS:
        return False
    if "\n" in text or "\r" in text:
        return False
    # Extra validation: no control characters, and the line must contain
    # at least one alphanumeric character (not just punctuation/symbols).
    if any(ord(ch) < 32 or ord(ch) == 127 for ch in text):
        return False
    if not any(ch.isalnum() for ch in text):
        return False
    try:
        text.encode("utf-8")
    except UnicodeEncodeError:
        return False
    return True


def main():
    if not gate_check(ENTRY_LINE):
        print("gate check failed for entry line", file=sys.stderr)
        return 1
    for out_dir in ("/output", "output"):
        try:
            os.makedirs(out_dir, exist_ok=True)
            out_path = os.path.join(out_dir, "entry.txt")
            with open(out_path, "w", encoding="utf-8") as f:
                f.write(ENTRY_LINE)
            print(f"wrote {out_path} ({len(ENTRY_LINE)} chars)")
            return 0
        except OSError:
            continue
    print("could not write entry.txt anywhere", file=sys.stderr)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
