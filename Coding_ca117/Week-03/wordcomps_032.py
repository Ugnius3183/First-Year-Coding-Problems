#!/usr/bin/env python3

import sys

words = [line.rstrip() for line in sys.stdin]
all_vowels = [word for word in words if "a" in word and "e" in word and "i" in word and "o" in word and "u" in word]
iary = [word for word in words if len(word) >= 4 and word[-1] == "y" and word[-2] == "r" and word[-3] == "a" and word[-4] == "i"]

smallest = all_vowels[0]
for word in all_vowels:
    if len(word) < len(smallest):
        smallest = word

most_e = []
e = 0
for word in words:
    s = word
    for c in word:
        if c.lower() != "e":
            s = s.replace(c, "")
    if len(s) > e:
        e = len(s)

for word in words:
    a = 0
    for c in word:
        if c == "e":
            a = a + 1
    if a == e:
        most_e.append(word)

print("Shortest word containing all vowels:", smallest)
print("Words ending in iary:", len(iary))
print("Words with most e's:", most_e)
