#!/usr/bin/env python3

entry = input()
while entry != "end":
    title = entry.split()
    module = " ".join(title[5:])
    print(module)
    entry = input()
