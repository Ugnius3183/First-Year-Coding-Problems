#!/usr/bin/env python3

import sys

phone_book = {}
with open(sys.argv[1], "r") as f:
    for line in f:
        s = line.rstrip().split()
        phone_book[s[0]] = s[1]

for line in sys.stdin:
    print("Name:", line.rstrip())
    if line.rstrip() in phone_book:
        print("Phone:", phone_book[line.rstrip()])
    else:
        print("No such contact")
