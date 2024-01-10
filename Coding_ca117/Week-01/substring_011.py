#!/usr/bin/env python3

import sys

for line in sys.stdin:
    s = line.split()
    print(s[0].lower() in s[1].lower())
