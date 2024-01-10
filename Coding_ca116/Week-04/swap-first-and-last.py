#!/usr/bin/env python3

s = input()

first = s[0]
last = s[len(s) - 1]
mid = s[1:len(s) - 1]

print(last + mid + first)
