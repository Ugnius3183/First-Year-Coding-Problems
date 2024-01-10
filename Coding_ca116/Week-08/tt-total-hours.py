#!/usr/bin/env python3

total_hours = 0

line = input()
while line != "end":
    line = line.split()
    time = line[2]
    time = int(time)
    total_hours = total_hours + time
    line = input()

print(total_hours)
