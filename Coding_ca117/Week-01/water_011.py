#!/usr/bin/env python3

import sys

n = int(input())
b = input().split()

total = 0
buckets = 0

i = 0
while i < len(b):
    total = total + int(b[i])
    if total <= n:
        buckets = buckets + 1
    i = i + 1

print(buckets)
