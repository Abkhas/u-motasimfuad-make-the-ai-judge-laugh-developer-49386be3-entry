#!/usr/bin/env python3
"""Make the AI Judge Laugh: Developer Excuses.

Writes one funny single-line excuse (89 characters) to /output/entry.txt:
a developer's excuse for code breaking in production. The twist is the
review chain: the code was written, reviewed, and approved by the same
person, minutes apart, at 2am.
"""
import os

LINE = (
    "The bug was in the code I wrote at 2am, reviewed at 2:05am, "
    "and approved by me at 2:06am."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
