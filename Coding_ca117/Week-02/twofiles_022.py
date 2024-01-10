#!/usr/bin/env python3

import sys

numbers1 = []
with open(sys.argv[1], "r") as f:
    for line in f:
        numbers1.append(line.rstrip())

numbers2 = []
with open(sys.argv[2], "r") as f:
    for line in f:
        numbers2.append(line.rstrip())

i = 0
while i < len(numbers1):
    print(numbers1[i])
    print(numbers2[i])
    i = i + 1
