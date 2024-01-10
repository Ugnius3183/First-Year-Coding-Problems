#!/usr/bin/env python3

class Score(object):

    def __init__(self, goals=0, points=0):
        self.goals = goals
        self.points = points
        self.total = self.points + (self.goals * 3)

    #def score_to_points(self):
    #    self.total = self.points + (self.goals * 3)

    def __eq__(self, other):
        return ((self.total) == (other.total))

    def __lt__(self, other):
        return ((self.total) < (other.total))

    def __le__(self, other):
        return ((self.total) <= (other.total))

    def __str__(self):
        return '{} goal(s) and {} point(s)'.format(self.goals, self.points)
