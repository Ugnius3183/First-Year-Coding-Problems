#!/usr/bin/env python3

import sys

for line in sys.stdin:
    s = line.split()
    s1 = s[0].lower()
    s2 = s[1].lower()
    for c in s1:
        if c in s2:
            s2 = s2.replace(c, "", 1)
            s1 = s1.replace(c, "", 1)
    if len(s1) == 0 and len(s2) == 0:
        print("True")
    else:
        print("False")
