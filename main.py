"""Make the AI Judge Laugh: Developer Excuses.

Writes one funny single-line developer excuse to
$MAKEFUN_OUTPUT_DIR/entry.txt. Deterministic, stdlib-only, no
network, no randomness, no clock.
"""

import os

ENTRY = "The framework auto-updated at 3 a.m. and deprecated the one function production actually used."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
