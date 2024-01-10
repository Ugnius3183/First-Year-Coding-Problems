#!/usr/bin/env python3

class Stack():

    def __init__(self):
        self.s = []

    def push(self, e):
        self.s.append(e)

    def top(self):
        return self.s[-1]

    def is_empty(self):
        return len(self.s) == 0

    def pop(self):
        return self.s.pop()

    def matcher(self):
        for c in self.s:
            if c in "({[":
                if c == "(":
                    

    def __len__(self):
        return len(self.s)
