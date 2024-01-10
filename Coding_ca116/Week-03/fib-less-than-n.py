#!/usr/bin/env python3

n = int(input())
prev = 0
curr = 1
if prev < n:
    if n >= 1:
        print(prev)
if curr < n:
    if n >= 2:
        print(curr)

i = 2
while i < n:
    if curr + prev < n:
        print(curr + prev)
    tmp = curr
    curr = prev + curr
    prev = tmp
    i = i + 1
