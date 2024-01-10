#!/usr/bin/env python3

import sys

numbers = {"0": "zero",
           "1": "one",
           "2": "two",
           "3": "three",
           "4": "four",
           "5": "five",
           "6": "six",
           "7": "seven",
           "8": "eight",
           "9": "nine",
           "10": "ten"}

translation = {}
with open(sys.argv[1], "r") as f:
    for line in f:
        translation[line.rstrip().split()[0]] = line.rstrip().split()[1]

for line in sys.stdin:
    print(" ".join([translation[numbers[number]] for number in line.rstrip().split()]))
