#!/usr/bin/env python3

import sys

biggest = 0
a = []
for line in sys.stdin:
    s = line.rstrip()
    a.append(s)
    if len(s) > biggest:
        biggest = len(s)

i = 0
while i < len(a):
    print(f'{a[i] : ^{biggest}}')
    i = i + 1
