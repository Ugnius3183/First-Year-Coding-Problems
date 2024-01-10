#!/usr/bin/env python3

import sys

try:
    highest = -1
    best = []
    with open(sys.argv[1], "r") as f:
        for line in f:
            try:
                s = line.rstrip().split()
                if int(s[0]) > highest:
                    highest = int(s[0])
                    best = s
                    length = len(best) - 1
            except ValueError:
                print(f"Invalid mark {s[0]} encountered. Skipping.")

    with open(sys.argv[1], "r") as f:
        for line in f:
            s = line.rstrip().split()
            if int(s[0]) == highest and s[1] != best[1] and s[2] != best[2]:
                s = " ".join(s)
                for c in s:
                    if c.isdigit() is True:
                        s = s.replace(c, "")
                best.append(s.strip())

    best = str(best).strip("[',]")
    for c in best:
        if c.isdigit() is True or c == "'" or c == "[" or c == "]":
            best = best.replace(c, "")
    print("Best student(s):", best.replace(",", "", length).strip())
    print("Best mark:", highest)

except FileNotFoundError:
    print(f"The file {sys.argv[1]} could not be opened.")
