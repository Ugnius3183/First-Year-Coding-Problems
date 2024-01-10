#!/usr/bin/env python3
 
import sys
 
total = 0
used = {}
a = sys.stdin.read().rstrip().split()
for line in a:
    s = line.rstrip().lower()
    for c in s:
        if c.isalnum() is False:
            s = s.replace(c, "")
    if len(s) > 0 and s not in used:
        total = total + 1
        used[s] = True
print(total)