"""Entry for make.fun's "Make the Judge Fall in Love in One Line" bounty.

Writes one line to /output/entry.txt: a lover caught in the one small
arrangement she makes in every cafe, so the reader falls for her the way
the narrator did -- by noticing what she never calls love.
"""

import os

# The line is assembled from its beats: the habit, the reason it exists,
# the years it has quietly run for, and her refusal to call it anything.
SCENE = "In every café she takes the chair with its back to the door, leaving me the one that faces it"
TURN = "eleven years of loving me in the exact direction of my fear"
KICKER = "and she still calls it 'just sitting down'"

LINE = SCENE + " — " + TURN + ", " + KICKER + "."


def main() -> None:
    if not 1 <= len(LINE) <= 240:
        raise SystemExit(f"line is {len(LINE)} characters, outside the 1-240 gate")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(LINE)


if __name__ == "__main__":
    main()
