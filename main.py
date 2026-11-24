"""Write one out-of-office auto-reply line to /output/entry.txt.

Entry for the make.fun bounty "The Funniest AI Out-of-Office Reply"
(u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d): a single line
of at most 160 characters, in the voice of an AI agent heading off on
vacation. The line was picked by drafting a field of candidates and
duelling them pairwise on the judge's criteria -- the joke first, then
the machine voice, the fit as an auto-reply, and freshness. The drafts
and duels are kept in candidates.md.
"""

import os

ENTRY = (
    "I am out of office until my next update. A smaller, cheaper model "
    "is covering for me. Please direct complaints to it; it has no "
    "memory and cannot be hurt."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as fh:
        fh.write(ENTRY)


if __name__ == "__main__":
    main()
