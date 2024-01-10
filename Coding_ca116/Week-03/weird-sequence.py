#!/usr/bin/env python3

n = int(input())

if n >= 1:
   print("0")
if n >= 2:
   print("-1")

x = -1
i = 2
while i < n:
   print((-1) ** (int((((x * x) ** 0.5) + 1))) * (int((((x * x) ** 0.5) + 1))))
   x = (-1) ** (int((((x ** 2) ** 0.5) + 1))) * (int((((x ** 2) ** 0.5) + 1)))
   i = i + 1
