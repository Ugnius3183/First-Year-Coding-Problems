#!/usr/bin/env python3

def swap_keys_values(d):
    d = {v: k for k, v in d.items()}
    return d
