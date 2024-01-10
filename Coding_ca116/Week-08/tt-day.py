#!/usr/bin/env python3

line = input()
tt = []

while line != "end":
    tt.append(line)
    line = input()

day = input()
i = 0
while i < len(tt):
    line = tt[i]
    line = line.split()
    if line[0] == day:
        print(" ".join(line))
    i = i + 1
