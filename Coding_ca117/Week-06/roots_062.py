#!/usr/bin/env python3

import sys

def find_roots(a, b, c):
    r1 = (-b + (((b ** 2) - 4 * a * c) ** 0.5)) / 2 * a
    r2 = (-b - (((b ** 2) - 4 * a * c) ** 0.5)) / 2 * a
    if len(str(r1)):
        return f"r1 = {r1}, r2 = {r2}"

for line in sys.stdin:
    s = line.rstrip().split()
    print(find_roots(int(s[0]), int(s[1]), int(s[2])))
