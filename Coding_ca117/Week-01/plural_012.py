#!/usr/bin/env python3

import sys

for line in sys.stdin:
    s = line.rstrip()
    if s[-2] == "c" and s[-1] == "h":
        s = s + "es"
    elif s[-2] == "s" and s[-1] == "h":
        s = s + "es"
    elif s[-1] == "x" or s[-1] == "s" or s[-1] == "z":
        s = s + "es"
    elif s[-2] != "a" and s[-2] != "e" and s[-2] != "i" and s[-2] != "o" and s[-2] != "u" and s[-1] == "y":
        s = s[0:-1]
        s = s + "ies"
    elif s[-1] == "f":
        s = s[0:-1]
        s = s + "ves"
    elif s[-2] == "f" and s[-1] == "e":
        s = s[0:-2]
        s = s + "ves"
    elif s[-1] == "o":
        s = s + "es"
    else:
        s = s + "s"
    print(s)
