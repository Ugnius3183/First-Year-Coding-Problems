#!/usr/bin/env python3

dec = int(input())
bin = ""

i = 0
while dec > 2 ** i:
    i = i + 1

i = i - 1
while i != -1:
    if dec // 2 ** i == 1:
        bin = bin + "1"
    elif dec // 2 ** i == 0:
        bin = bin + "0"
    dec = dec % 2 ** i
    i = i - 1

print(bin)
