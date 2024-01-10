#!/usr/bin/env python3

class Score(object):

    def __init__(self, goals=0, points=0):
        self.goals = goals
        self.points = points
        self.total = self.points + (self.goals * 3)

    def __eq__(self, other):
        return ((self.total) == (other.total))

    def __lt__(self, other):
        return ((self.total) < (other.total))

    def __le__(self, other):
        return ((self.total) <= (other.total))

    def __add__(self, other):
        return (Score((self.total) + (other.total)))

    def __iadd__(self, other):
        z = self + other

    def __str__(self):
        return '{} goal(s) and {} point(s)'.format(self.goals, self.points)

s1 = Score()
s2 = Score(3, 12)
s3 = Score(4, 9)
s4 = Score(1, 1)

s5 = s3 + s4
print(s5)
assert(isinstance(s5, Score))
assert(s5 is not s3)
assert(s5 is not s4)

before = s2
s2 += s4
print(s2)
assert(isinstance(s2, Score))
assert(s2 is before)
assert(s2 is not s4)
