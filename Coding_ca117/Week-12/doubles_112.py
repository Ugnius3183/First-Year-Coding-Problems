#!/usr/bin/env python3

import sys

dict = {}
for line in sys.stdin:
    dv = 0
    s = line.rstrip()
    for i in range(0, len(s)):
        if i != len(s) - 1 and s[i] in 'aeiou' and s[i + 1] == s[i]:
            dv = dv + 1
    dict[s] = dv

print(max(dict, key=dict.get))
