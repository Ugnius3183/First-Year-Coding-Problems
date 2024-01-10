#!/usr/bin/env python3

import sys

def change(strings):
    new_strings = []
    for i in range(0, len(strings[0])):
        a = []
        for word in strings:
            a.append(word[i])
        new_strings.append("".join(a))
    return new_strings


strings = [line.rstrip() for line in sys.stdin]
strings = "\n".join(change(sorted(change(strings), key=str.casefold)))
print(strings)
