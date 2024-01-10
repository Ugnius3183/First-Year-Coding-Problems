#!/usr/bin/env python3

import sys

def sum_factors(n):
    total = 0
    for i in range(1, (n // 2) + 1):
        if n % i == 0:
            total = total + i
    return total


def is_perfect(n):
    if n == sum_factors(n):
        return True
    else:
        return False


for line in sys.stdin:
    print(is_perfect(int(line.rstrip())))
