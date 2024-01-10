#!/usr/bin/env python3

import math
import sys

for line in sys.stdin:
    n = line.rstrip()
    print(f'{math.pi:.{int(n)}f}')
