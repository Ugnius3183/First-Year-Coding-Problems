#!/usr/bin/env python3

import sys

contact_book = {}

with open(sys.argv[1], "r") as f:
    for line in f:
        s = line.rstrip().split()
        contact_book[s[0]] = s[1], s[2]

for line in sys.stdin:
    print("Name:", line.rstrip())
    if line.rstrip() in contact_book:
        print("Phone:", contact_book[line.rstrip()][0])
        print("Email:", contact_book[line.rstrip()][1])
    else:
        print("No such contact")
