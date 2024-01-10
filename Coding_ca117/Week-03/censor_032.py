#!/usr/bin/env python3

import sys

censor = []
with open(sys.argv[1], "r") as f:
    for line in f:
        censor.append(line.rstrip())

for line in sys.stdin:
    a = line.rstrip().split()
    i = 0
    j = 0
    while i < len(a):
        while j < len(censor):
            print(censor[j])
            if censor[j] in a:
                print("yes")
            j = j + 1
        i = i + 1
