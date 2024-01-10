#!/usr/bin/env python3

import sys

d = {}
animals = sys.stdin.readlines()

i = 0
while i < len(animals):
    d["snap"] = animals[i]
    i = i + 1

print(d)
