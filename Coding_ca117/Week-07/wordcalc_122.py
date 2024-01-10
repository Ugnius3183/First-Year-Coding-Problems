#!/usr/bin/env python3

import sys

def define(word, num):
    memory[word] = int(num)

def calculate(c):
    i = 0
    total = 0
    while i < len(c):
        if c[i] in memory:
            if c[i - 1] == "-":
                total = total - memory[c[i]]
            else:
                total = total + memory[c[i]]
        elif c[i] not in memory:
            print('{} unknown'.format(" ".join(c)))
            break
        i = i + 2
    if i == len(c) and total in memory.values():
        for k, v in memory.items():
            if v == total:
                print(f'{" ".join(c)} {k}')
    elif i == len(c) and total not in memory.values():
        print('{} unknown'.format(" ".join(c)))


memory = {}
for line in sys.stdin:
    c = line.rstrip().split()
    if c[0] == "clear":
        memory = {}
    elif c[0] == "def":
        define(c[1], c[2])
    elif c[0] == "calc":
        del(c[0])
        calculate(c)
