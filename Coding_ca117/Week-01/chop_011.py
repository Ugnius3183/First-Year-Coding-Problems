#!/usr/bin/env python3

import sys

def chop(s):
    return s[1:len(s) - 1]


for line in sys.stdin:
    s = line.strip()
    if len(s) > 2:
        print(chop(s))
