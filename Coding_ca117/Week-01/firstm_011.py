#!/usr/bin/env python3

import sys

for line in sys.stdin:
    print(line.replace("m", "M", 1).rstrip())
