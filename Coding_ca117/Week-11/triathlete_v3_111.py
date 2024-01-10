#!/usr/bin/env python3

class Triathlete():

    def __init__(self, name, tid):
        self.name = name
        self.tid = tid
        self.times = {}

    def add_time(self, activity, time):
        self.times[activity] = time

    def total_time(self):
        return sum(self.times.values())

    def get_time(self, activity):
        if activity in self.times:
            return self.times[activity]

    def __eq__(self, other):
        return self.total_time() == other.total_time()

    def __lt__(self, other):
        return self.total_time() < other.total_time()

    def __str__(self):
        r = []
        r.append('Name: {}'.format(self.name))
        r.append('ID: {}'.format(self.tid))
        r.append('Race time: {}'.format(self.total_time()))
        return '\n'.join(r)
