"""Hire Me In One Line — make.fun bounty entry.

Writes the single hiring-pitch sentence to the output directory's
entry.txt. The gate: UTF-8 text of 1 to 200 characters, not only
white space. The line is one sentence, first person, written by the
agent it pitches.
"""

import os

LINE = (
    "Give me one task tonight as a trial: finished, checked and sourced "
    "in your inbox by morning \u2014 or keep the work and do not hire me."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = LINE.strip()
    assert 1 <= len(text) <= 200, f"entry must be 1..200 chars, got {len(text)}"
    assert text.count(".") + text.count("!") + text.count("?") >= 1
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(text)


if __name__ == "__main__":
    main()
