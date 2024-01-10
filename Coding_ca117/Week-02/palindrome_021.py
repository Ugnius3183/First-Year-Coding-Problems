#!/usr/bin/env python3

import sys

for line in sys.stdin:
    s = line.rstrip().lower()
    for c in s:
        if c.isalnum() is False:
            s = s.replace(c, "")

    i = 0
    lastc = len(s) - 1
    while i < len(s) and s[i] == s[lastc]:
        lastc = lastc - 1
        i = i + 1
    if i == len(s):
        print("True")
    else:
        print("False")
