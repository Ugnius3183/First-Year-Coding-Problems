#!/usr/bin/env python3

n = int(input())
prev = 0
curr = 1

if n >= 1:
    print(prev)
if n >= 2:
    print(curr)

i = 2
while i < n:
    print(curr + prev)
    tmp = curr
    curr = prev + curr
    prev = tmp
    i = i + 1
