#!/usr/bin/env python3

entry = input()
while entry != "end":
    entry = entry.split()
    if entry[0] == "3":
        print(" ".join(entry))
    entry = input()
