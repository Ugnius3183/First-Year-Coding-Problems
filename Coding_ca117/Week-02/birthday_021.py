#!/usr/bin/env python3

import sys
import calendar

for line in sys.stdin:
    s = line.rstrip().split()
    if calendar.weekday(int(s[2]), int(s[1]), int(s[0])) == 0:
        print("You were born on a Monday and Monday's child is fair of face.")
    elif calendar.weekday(int(s[2]), int(s[1]), int(s[0])) == 1:
        print("You were born on a Tuesday and Tuesday's child is full of grace.")
    elif calendar.weekday(int(s[2]), int(s[1]), int(s[0])) == 2:
        print("You were born on a Wednesday and Wednesday's child is full of woe.")
    elif calendar.weekday(int(s[2]), int(s[1]), int(s[0])) == 3:
        print("You were born on a Thursday and Thursday's child has far to go.")
    elif calendar.weekday(int(s[2]), int(s[1]), int(s[0])) == 4:
        print("You were born on a Friday and Friday's child is loving and giving.")
    elif calendar.weekday(int(s[2]), int(s[1]), int(s[0])) == 5:
        print("You were born on a Saturday and Saturday's child works hard for a living.")
    else:
        print("You were born on a Sunday and Sunday's child is fair and wise and good in every way.")
