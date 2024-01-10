#!/usr/bin/env python3

import sys

def tagger(item):
    return item[1]


vowel_count = {"a": 0,
               "e": 0,
               "i": 0,
               "o": 0,
               "u": 0}

for line in sys.stdin:
    s = line.rstrip().split()
    for word in s:
        for c in word:
            if c.lower() in vowel_count:
                vowel_count[c.lower()] = vowel_count[c.lower()] + 1

biggest = 0
for line in vowel_count:
    if len(str(vowel_count[line])) > biggest:
        biggest = len(str(vowel_count[line]))

for k, v in sorted(vowel_count.items(), key=tagger, reverse=True):
    print(f"{k} : {v : >{biggest}}")
