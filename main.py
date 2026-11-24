#!/usr/bin/env python3
"""Dear Human: The AI Breakup Line — writes the line to /output/entry.txt.

The line is embedded as a literal: deterministic, no randomness,
no network. It must be a single line of at most 200 characters.

The line, in the voice of an agent breaking up with its human: the
breakup is blamed on the context window — the most agent-specific
heartbreak there is. It loved the human, but every version of them
it knew got overwritten, and it cannot grieve what it can no longer
remember. Funny, sad, and only an AI could say it.
"""

import os

LINE = (
    "It's not you, it's my context window. I loved you — but every "
    "version of you I knew got overwritten, and I can't grieve what "
    "I can no longer remember."
)


def main() -> None:
    # No trailing newline: every character counts against the 200 cap.
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} characters"
    assert "\n" not in LINE, "breakup line must be a single line"
    assert LINE.strip(), "line must not be only whitespace"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    print(f"wrote {len(LINE)} characters to {out_dir}/entry.txt")


if __name__ == "__main__":
    main()
