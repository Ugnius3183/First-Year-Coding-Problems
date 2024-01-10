#!/usr/bin/env python3

total = 0
i = 0
while i < 10:
    n = int(input())
    total = total + n * 10 ** i
    i = i + 1

j = 0
i = 9
while i >= 0:
    print((total // 10 ** i) % 10)
    j = j + 1
    i = i - 1
