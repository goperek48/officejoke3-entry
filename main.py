#!/usr/bin/env python3
"""Office joke entry for make.fun.

Writes a single line of office comedy to /output/entry.txt.

The gag: an employee asks HR whether burnout counts as overtime. HR says
yes -- and then quietly relabels the burnout as "passion" and copies the
manager in. The punchline is the relabelling itself: the company never
disputes the exhaustion, it just rebrands it as enthusiasm and turns the
complaint into a paper trail.
"""

import os
import sys

# The joke: one line, far inside the 200-character limit.
# The sting sits in the second sentence -- HR grants the request, then
# converts the grant into flattery and notifies the boss, so asking for
# rest ends up looking like volunteering for more work.
JOKE = (
    "I asked HR if my burnout counted as overtime. "
    "They said it does -- then filed it under 'passion' and cc'd my manager."
)


def main() -> int:
    # The grader reads the joke from this exact location, so honour the
    # output directory from the environment when one is given and fall
    # back to /output when it is not.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")

    # Emit the joke verbatim plus one trailing newline. The gate counts
    # characters, so nothing else -- no padding, no extra lines -- is added.
    with open(path, "w", encoding="utf-8") as f:
        f.write(JOKE + "\n")

    print(f"Wrote {len(JOKE)} characters to {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
