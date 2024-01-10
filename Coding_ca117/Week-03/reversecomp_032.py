#!/usr/bin/env python3

import sys

def reverse_word(s):
    s = s.lower()
    reversed_word = []
    i = 1
    while i <= len(s):
        p = len(s) - i
        reversed_word.append(s[p])
        i = i + 1
    return "".join(reversed_word)

def binsearch(word, sorted_list):
    if len(word) < 5:
        return False
    else:
        low = 0
        high = len(sorted_list) - 1
        while low <= high:
            mid = (low + high) // 2
            if sorted_list[mid].lower() < word:
                low = mid + 1
            elif sorted_list[mid].lower() > word:
                high = mid - 1
            else:
                return True
        return False


words = [line.rstrip() for line in sys.stdin]
a = []
for word in words:
    if binsearch(reverse_word(word).lower(), words) is True:
        a.append(word)
    elif binsearch(reverse_word(word).capitalize(), words) is True:
        a.append(word)
print(a)
