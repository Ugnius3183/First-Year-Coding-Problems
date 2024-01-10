#!/usr/bin/env python3

class MP3Track():

    def __init__(self, title, duration):
        self.title = title
        self.duration = duration

    def __str__(self):
        return "Title: {}\nDuration: {}".format(self.title, self.duration)

class MP3Collection():

    def __init__(self):
        self.tracklist = {}

    def add(self, t):
        self.tracklist[t.title] = t
        print(self.tracklist)

    def remove(self, track):
        if track in self.tracklist:
            del self.tracklist[track]

    def lookup(self, t):
        if t in self.tracklist:
            return self.tracklist[t]


def main():
    t1 = MP3Track('Fools Gold', 604)
    t2 = MP3Track('Shallow', 197)
    t3 = MP3Track('Telephone', 220)

    c = MP3Collection()

    c.add(t1)
    c.add(t2)
    c.add(t3)


    t = c.lookup('604')
    assert(isinstance(t, MP3Track))
    assert(t.title == 'Fools Gold')
    assert(t.duration == 604)

    c.remove('Fools Gold')
    t = c.lookup('Fools Gold')
    assert(t is None)

if __name__ == '__main__':
    main()
