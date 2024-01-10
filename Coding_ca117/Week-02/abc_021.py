#!/usr/bin/env python3

import sys

for line in sys.stdin:
    n = line.rstrip().split()
    s = input().rstrip()
    a = []
    a.append(s[0])
    a.append(s[1])
    a.append(s[2])
    if int(n[0]) < int(n[1]) and int(n[0]) < int(n[2]):
        A = int(n[0])
    elif int(n[1]) < int(n[0]) and int(n[1]) < int(n[2]):
        A = int(n[1])
    elif int(n[2]) < int(n[0]) and int(n[2]) < int(n[1]):
        A = int(n[2])
    if int(n[0]) != A and int(n[0]) > int(n[1]) and int(n[0]) > int(n[2]):
        C = int(n[0])
    elif int(n[1]) != A and int(n[1]) > int(n[0]) and int(n[1]) > int(n[2]):
        C = int(n[1])
    elif int(n[2]) != A and int(n[2]) > int(n[0]) and int(n[2]) > int(n[1]):
        C = int(n[2])
    if int(n[0]) != A and int(n[0]) != C:
        B = int(n[0])
    elif int(n[1]) != A and int(n[1]) != C:
        B = int(n[1])
    elif int(n[2]) != A and int(n[2]) != C:
        B = int(n[2])
    if a[0] == "A":
        a[0] = A
    elif a[0] == "B":
        a[0] = B
    elif a[0] == "C":
        a[0] = C
    if a[1] == "A":
        a[1] = A
    elif a[1] == "B":
        a[1] = B
    elif a[1] == "C":
        a[1] = C
    if a[2] == "A":
        a[2] = A
    elif a[2] == "B":
        a[2] = B
    elif a[2] == "C":
        a[2] = C
    print(a[0], a[1], a[2])
