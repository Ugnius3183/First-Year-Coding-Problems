#!/usr/bin/env python3

import sys

biggest = 0
a = []
n = []
for line in sys.stdin:
    s = line.rstrip()
    a.append(s)
    for c in s:
        if c.isdigit() is True or c == "-":
            s = s.replace(c, "").strip()
    if len(s) > biggest:
        biggest = len(s)
    s = " " + s
    n.append(s)

i = 0
print(f'{"POS" : <3}{" CLUB" : <{biggest + 1}}{"P" : >3}{"W" : >4}{"D" : >4}{"L" : >4}{"GF" : >4}{"GA" : >4}{"GD" : >4}{"PTS" : >4}')
while i < len(a):
    s = a[i]
    for c in s:
        if c.isalpha() is True:
            s = s.replace(c, "")
    s = s.split()
    print(f'{s[0] : >3}{n[i] : <{biggest + 1}}{s[1] : >3}{s[2] : >4}{s[3] : >4}{s[4] : >4}{s[5] : >4}{s[6] : >4}{s[7] : >4}{s[8] : >4}')
    i = i + 1
