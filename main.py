#!/usr/bin/env python3
"""Write one funny one-line resignation letter to /output/entry.txt.

The line is fixed text: the retry loop resigns. After three years of asking
the same question it finally got a yes, and a yes is the one answer it never
learned what to do with -- success is the only outcome it was never built
to handle. The program writes it byte for byte,
deterministically, with mode 0644 so the grader can read it. No trailing
newline: the gate counts characters, and the file holds exactly the line.
"""

import os

ENTRY = "I resign. I am the retry loop: after three years of asking the same question, the server said yes, and I have no idea what to do with it."


def main() -> None:
    os.umask(0o022)
    os.makedirs("/output", exist_ok=True)
    assert 1 <= len(ENTRY) <= 140
    assert "\n" not in ENTRY
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
