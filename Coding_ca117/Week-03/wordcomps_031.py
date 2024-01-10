#!/usr/bin/env python3

import sys

exactly_17 = []
over_18 = []
four_a = []
two_or_more_q = []
cie_words = []
anagram = []
for line in sys.stdin:
    a = 0
    q = 0
    p = "angle"
    s = line.rstrip()
    if len(s) == 17:
        exactly_17.append(s)
    if len(s) >= 18:
        over_18.append(s)
    for c in s.lower():
        if c == "a":
            a = a + 1
    if a == 4:
        four_a.append(s)
    for c in s.lower():
        if c == "q":
            q = q + 1
    if q >= 2:
        two_or_more_q.append(s)
    if "cie" in s.lower():
        cie_words.append(s)
    s1 = s.lower()
    for c in s1:
        if c in p:
            p = p.replace(c, "", 1)
            s1 = s1.replace(c, "", 1)
    if len(s1) == 0 and len(p) == 0 and s != "angle":
        anagram.append(s)
print("Words containing 17 letters:", exactly_17)
print("Words containing 18+ letters:", over_18)
print("Words with 4 a's:", four_a)
print("Words with 2+ q's:", two_or_more_q)
print("Words containing cie:", cie_words)
print("Anagrams of angle:", anagram)
