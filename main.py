#!/usr/bin/env python3
"""Make the AI Judge Laugh — make.fun entry.

Writes one office-life joke (single line, under 200 characters)
to /output/entry.txt. Python standard library only; deterministic.
"""

import os

# Final pick: HR answers a raise request with a mindfulness app — the
# punchline lands on the last two words, and every word earns its place.
# Shorter and sharper than the printer draft (86 chars vs 119).
JOKE = (
    "I asked HR for a raise and got a mindfulness app instead — "
    "so now I'm calmly underpaid."
)


def main() -> None:
    text = JOKE.strip()
    assert 1 <= len(text) <= 200, f"entry must be 1-200 chars, got {len(text)}"
    assert text == text.strip() and "\n" not in text, "entry must be one line"
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)
    print(f"Wrote {len(text)} chars to {os.path.join(out_dir, 'entry.txt')}")


if __name__ == "__main__":
    main()
