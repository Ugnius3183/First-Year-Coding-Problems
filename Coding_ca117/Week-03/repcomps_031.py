#!/usr/bin/env python3

import sys

for line in sys.stdin:
    numbers = []
    for i in range(1, int(line) + 1):
        if i % 3 != 0:
            numbers.append(i)
        else:
            numbers.append("X")
    print("Multiples of 3 replaced:", numbers)
