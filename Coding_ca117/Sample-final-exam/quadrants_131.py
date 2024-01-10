#!/usr/bin/env python3

import sys

for line in sys.stdin:
    s = line.split()
    s[0] = int(s[0])
    s[1] = int(s[1])
    if s[0] > 0 and s[1] > 0:
        print("1")
    if s[0] > 0 and s[1] < 0:
        print("2")
    if s[0] < 0 and s[1] < 0:
        print("3")
    if s[0] < 0 and s[1] > 0:
        print("4")
