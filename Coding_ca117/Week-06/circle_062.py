#!/usr/bin/env python3

def overlap(x1=None, y1=None, r1=None, x2=None, y2=None, r2=None):
    if x1 is None:
        x1 = 0
    if y1 is None:
        y1 = 0
    if r1 is None:
        r1 = 1
    if x2 is None:
        x2 = 0
    if y2 is None:
        y2 = 0
    if r2 is None:
        r2 = 1
    d = (((x2 - x1) ** 2) + ((y2 - y1) ** 2)) ** 0.5
    if d == 0.0 and r1 == r2:
        return True
    elif d == ((r1 - r2) ** 2) ** 0.5:
        return True
    elif r1 - r2 < d and r1 + r2 > d:
        return True
    else:
        return False
