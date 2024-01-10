#!/usr/bin/env python3

dec = int(input())
hex = ""

i = 0
while dec > 16 ** i:
    i = i + 1

i = i - 1
while i != -1:
    n = dec // 16 ** i
    hex = hex + str(n)
    dec = dec % 16 ** i
    i = i - 1

print(hex)
