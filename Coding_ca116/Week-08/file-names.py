#!/usr/bin/env python3

import sys

n = sys.stdin.readlines()

i = 0
while i < len(n):
    m = n[i].split("/")
    m = m[len(m) - 1].rstrip()
    print(m)
    i = i + 1
