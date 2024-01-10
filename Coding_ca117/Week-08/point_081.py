#!/usr/bin/env python3

class Point():

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def midpoint(self, other):
        Point(((self.x + other.x)) / 2, ((self.y + other.y) / 2))

    def __str__(self):
        return '({:.1f}, {:.1f}).'.format(self.x, self.y)

p1 = Point(2, 3)
p2 = Point(4, 6)

p3 = p1.midpoint(p2)

print(p1)
print(p2)
print(p3)

assert(isinstance(p3, Point))
