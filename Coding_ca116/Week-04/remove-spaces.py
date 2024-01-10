#!/usr/bin/env python3

s = input()
m = ""

i = 0
while i < len(s):
    if s[i] != " ":
        m = m + s[i]
    i = i + 1

print(m)
