#!/usr/bin/env python3

import sys

for line in sys.stdin:
    multiples_of_3 = []
    multiples_of_3_squared = []
    doubles_of_4 = []
    multiples_of_3_or_4 = []
    multiples_of_3_and_4 = []
    for i in range(1, int(line) + 1):
        if i % 3 == 0:
            multiples_of_3.append(i)
        if i % 3 == 0:
            multiples_of_3_squared.append(i ** 2)
        if i % 4 == 0:
            doubles_of_4.append(i * 2)
        if i % 3 == 0 or i % 4 == 0:
            multiples_of_3_or_4.append(i)
        if i % 3 == 0 and i % 4 == 0:
            multiples_of_3_and_4.append(i)
    print("Multiples of 3:", multiples_of_3)
    print("Multiples of 3 squared:", multiples_of_3_squared)
    print("Multiples of 4 doubled:", doubles_of_4)
    print("Multiples of 3 or 4:", multiples_of_3_or_4)
    print("Multiples of 3 and 4:", multiples_of_3_and_4)
