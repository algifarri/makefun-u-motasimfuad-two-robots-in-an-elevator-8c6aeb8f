#!/usr/bin/env python3
"""Two Robots in an Elevator entry for make.fun.

Writes one funny line to /output/entry.txt. The joke is a robot
keeping score of an awkward elevator silence: it treats avoiding
eye contact as a sensor reading worth a new record, then begs the
other robot not to ruin it by speaking. The machine logic -- sensors,
records, a plea framed as a system request -- carries the awkwardness.
One line, no trailing newline, so the judge reads exactly the line.
Deterministic, standard library only.
"""

import os

LINE = "According to my sensors, we have avoided eye contact for 43 seconds. New record. Please do not ruin it."


def main():
    # The gate allows 1-200 characters; the line is 103 characters, and
    # it is written exactly, with no trailing newline. The "43 seconds"
    # is a sensor reading, not a guess: the robot counted the silence.
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
