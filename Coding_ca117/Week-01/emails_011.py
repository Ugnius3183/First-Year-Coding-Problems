#!/usr/bin/env python3

import sys

for email in sys.stdin:
    s = email.replace("@mail.dcu.ie", "")
    for c in s:
        if c.isdigit() is True:
            s = s.replace(c, "")
    s = s.split(".")
    s[0] = s[0].capitalize()
    s[1] = s[1].capitalize()
    print(" ".join(s).rstrip())
