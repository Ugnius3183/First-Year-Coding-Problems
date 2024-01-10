#!/usr/bin/env python3

import sys

def capitalize(s):
    return s[0].upper() + s[1:len(s) - 1] + s[len(s) - 1].upper()


for line in sys.stdin:
    s = line.strip()
    if len(s) > 1:
        print(capitalize(s))
