#!/usr/bin/env python3

s = input()
m = ""

i = 1
while i <= len(s):
    m = m + s[len(s) - i]
    i = i + 1

print(m)
