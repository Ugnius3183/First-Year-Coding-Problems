#!/usr/bin/env python3

import sys

translations = {
    "one": "eins",
    "two": "zwei",
    "three": "drei",
    "four": "vier",
    "five": "funf",
    "six": "sechs",
    "seven": "sieben",
    "eight": "acht",
    "nine": "neun",
    "ten": "zehn",
}

numbers = sys.stdin.readlines()

i = 0
while i < len(numbers):
    number = numbers[i].rstrip()
    if number in translations:
        print(translations[number])
    i = i + 1
