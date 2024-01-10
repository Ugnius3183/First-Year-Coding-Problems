#!/usr/bin/env python3

import sys

for s in sys.stdin:
    s = s.rstrip()
    digits = False
    upper = False
    lower = False
    special = False
    for c in s:
        if digits is False:
            digits = c.isdigit()
        if upper is False:
            upper = c.isupper()
        if lower is False:
            lower = c.islower()
        if c.isalnum() is False:
            special = True
        characters = int(digits) + int(upper) + int(lower) + int(special)
    print(characters)
