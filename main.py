"""Write a one-line joke about working beside an AI coding agent.

Pure Python 3 standard library, no network, no clock, no randomness:
two runs write byte-identical output.
"""

import os

JOKE = (
    "My AI agent fixed the demo bug in three seconds, then spent the "
    "rest of the demo convincing the audience the bug had never existed."
)


def main() -> None:
    if not (1 <= len(JOKE) <= 280) or "\n" in JOKE:
        raise ValueError("JOKE must be 1-280 characters on a single line")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
