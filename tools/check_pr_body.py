#!/usr/bin/env python3
"""Check that a pull request description used the template.

GitHub fills the template in only when a pull request is opened through the web
interface. `gh pr create --body` and `--fill` skip it, and the result is a
one-line description that answers none of the questions the template asks. The
template cannot enforce itself, so this does.

It checks for the presence of the required headings, not for particular
answers. A person can still tick a box without thinking; nothing can stop that.
What this stops is the template never appearing at all.

Reads the body on stdin. Exit 0 if every required heading is present.

    python3 tools/check_pr_body.py < body.txt
"""

import re
import sys

REQUIRED = [
    "# What this changes",
    "## Would any production be classified differently?",
    "## What the checks cannot see",
    "## Allowlist entries added",
]


def main():
    body = sys.stdin.read()

    if not body.strip():
        print("FAIL: the pull request description is empty.")
        print()
        print("Open the pull request through the GitHub web interface so the")
        print("template fills in, or paste the template from")
        print(".github/pull_request_template.md and answer it.")
        return 1

    normalised = "\n".join(line.rstrip() for line in body.splitlines())
    missing = [h for h in REQUIRED if h not in normalised]

    if missing:
        print("FAIL: the pull request description is missing %d required "
              "section(s):" % len(missing))
        for h in missing:
            print("  %s" % h)
        print()
        print("This usually means the pull request was created from the command")
        print("line with a --body or --fill flag, which skips the template.")
        print("Edit the description, paste in .github/pull_request_template.md,")
        print("and answer it.")
        return 1

    # The one substantive check: "What this changes" must say something.
    section = re.split(r"(?m)^## ", normalised, maxsplit=1)[0]
    prose = re.sub(r"(?s)<!--.*?-->", "", section)
    prose = prose.replace("# What this changes", "").strip()
    if len(prose) < 40:
        print("FAIL: 'What this changes' is empty or too short to be useful.")
        print()
        print("Two or three sentences: what is different afterwards, and why.")
        return 1

    print("PASS: the pull request description follows the template.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
