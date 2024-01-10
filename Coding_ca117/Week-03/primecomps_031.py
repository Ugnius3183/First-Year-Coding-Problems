#!/usr/bin/env python3

import sys

for line in sys.stdin:
    primes = []
    not_primes = []
    for num in range(1, int(line) + 1):
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    not_primes.append(num)
                    break
            else:
                primes.append(num)
        else:
            not_primes.append(num)
    print("Primes:", primes)
