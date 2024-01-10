#!/usr/bin/env python3

import sys

rooms = sys.stdin.readline().split()
total = rooms.pop(0)
rooms.sort()

for i in range(0, int(total)):
    if int(rooms[i]) != i + 1:
        print(i + 1)
        break

if i + 1 == int(total) and i + 1 not in rooms:
    print("no room")
