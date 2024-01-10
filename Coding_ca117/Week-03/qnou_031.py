#!/usr/bin/env python3

import sys

print(f"Words with q but no u: {[line.rstrip() for line in sys.stdin if 'q' in line.lower().replace('qu', '')]}")
