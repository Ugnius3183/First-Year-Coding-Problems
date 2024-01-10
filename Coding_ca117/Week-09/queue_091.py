#!/usr/bin.env python3

class Queue():

    def __init__(self):
        self.q = []

    def enqueue(self, e):
        self.q.insert(0, e)

    def first(self):
        return self.q[-1]

    def is_empty(self):
        return len(self.q) == 0

    def dequeue(self):
        return self.q.pop()

    def __len__(self):
        return len(self.q)
