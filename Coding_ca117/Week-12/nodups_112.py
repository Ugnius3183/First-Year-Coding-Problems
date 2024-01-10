#!/usr/bin/env python3

import sys

used = []
for line in sys.stdin:
    s = line.rstrip().split()
    for i in range(0, len(s)):
        word = s[i]
        for c in word:
            if not c.isalpha():
                word = word.replace(c, "")
        if word.lower() in used:
            s[i] = '.'
        else:
            used.append(word.lower())
    print(" ".join(s))
