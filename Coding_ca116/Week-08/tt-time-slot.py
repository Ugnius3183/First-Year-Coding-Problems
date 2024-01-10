#!/usr/bin/env python3

line = input()

while line != "end":
    line = line.split()
    start_time = int(line[1])
    end_time = int(line[2])
    if end_time > 1:
        end_time = start_time + end_time - 1 + 1
    else:
        end_time = start_time
    start_time = str(start_time)
    end_time = str(end_time)
    start_time = start_time + ":00"
    end_time = end_time + ":50"
    line[1] = start_time
    line[2] = end_time
    line = " ".join(line)
    print(line)
    line = input()
