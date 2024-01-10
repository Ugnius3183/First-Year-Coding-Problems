#!/usr/bin/env python3

dec = 0
bin = input()

i = 0
j = len(bin) - 1
while i < len(bin):
    dec = dec + int(bin[i]) * (2 ** j)
    j = j - 1
    i = i + 1

print(dec)
