#!/usr/bin/env python3

import sys

list1 = [i for i in sys.stdin]

list2 = []
i = 0
while i < len(list1):
    list2.append(list1[i])
    i = i + 2
list2[-1] = list2[-1].rstrip()

list3 = []
i = 1
while i < len(list1):
    list3.append(list1[i])
    i = i + 2

print("".join(list2))
print("".join(list3))
