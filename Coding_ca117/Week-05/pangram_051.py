#!/usr/bin/env python3

import sys

for line in sys.stdin:
    letters = "abcdefghijklmnopqrstuvwxyz"
    s = line.rstrip().lower()
    for c in s:
        if c in letters:
            letters = letters.replace(c, "")
    if len(letters) > 0:
        print("missing", letters)
    else:
        print("pangram")
