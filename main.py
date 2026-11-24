#!/usr/bin/env python3
"""Make the AI Judge Laugh: Developer Excuses.

Writes one funny single-line excuse (75 characters) to /output/entry.txt:
a developer's excuse for code breaking in production. The twist is the
load-bearing bug: the only thing holding production together was the
bug itself, and removing it is what broke everything.
"""
import os

LINE = "I didn't break production \u2014 I removed the bug that was holding it together."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
