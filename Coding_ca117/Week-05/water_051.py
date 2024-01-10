#!/usr/bin/env python3

import sys

litres = sys.stdin.readline().rstrip()
buckets = sys.stdin.readline().rstrip().split()

total = 0
total_buckets = 0
for bucket in buckets:
    total = total + int(bucket)
    if total <= int(litres):
        total_buckets = total_buckets + 1

print(total_buckets)
