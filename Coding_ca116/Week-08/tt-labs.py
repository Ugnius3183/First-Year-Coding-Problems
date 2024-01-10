#!/usr/bin/env python3

line = input()
while line != "end":
    line = line.split()
    time = int(line[2])
    if time > 1:
        print(" ".join(line))
    line = input()
