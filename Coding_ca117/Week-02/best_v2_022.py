#!/usr/bin/env python3

import sys

try:
    highest = 0
    best = ""
    with open(sys.argv[1], "r") as f:
        for line in f:
            s = line.rstrip().split()
            if int(s[0]) > highest:
                highest = int(s[0])
                best = s

    print("Best student:", best[1], best[2])
    print("Best mark:", best[0])

except ValueError:
    print(f"Invalid mark {s[0]} encountered. Exiting.")

except FileNotFoundError:
    print(f"The file {sys.argv[1]} could not be opened.")
