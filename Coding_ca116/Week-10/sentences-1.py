#!/usr/bin/env python3

import sys

s = sys.stdin.readlines()

n = " ".join(s).split()

i = 0
j = 0
while i < len(n):
    if ". " in n[i] or "!" in n[i] or "? " in n[i]:
        print(" ".join(n[j:i + 1]))
        j = i + 1
    i = i + 1
