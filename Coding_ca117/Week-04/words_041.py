#!/usr/bin/env python3

import sys
import string

word_count = {}
for line in sys.stdin:
    s = line.rstrip().split()
    for word in s:
        a = word.lower()
        for c in a:
            if c == "'":
                c = c
            elif c in string.punctuation:
                a = a.replace(c, "")
        if a not in word_count:
            word_count[a] = 1
        else:
            word_count[a] = word_count[a] + 1

for k, v in sorted(word_count.items()):
    print(f"{k} : {v}")
