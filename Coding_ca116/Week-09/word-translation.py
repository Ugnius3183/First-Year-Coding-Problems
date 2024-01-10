#!/usr/bin/env python3

import sys

d = {}

with open("translation.txt") as translation:
    num_in = translation.readline()
    while 0 < len(num_in):
        num_in = num_in.rstrip()
        num_in = num_in.split()
        d[num_in[0]] = num_in[1]
        num_in = translation.readline()

inp = sys.stdin.readlines()
i = 0
while i < len(inp):
    number = inp[i].rstrip()
    if number in d:
        print(d[number])
    i = i + 1
