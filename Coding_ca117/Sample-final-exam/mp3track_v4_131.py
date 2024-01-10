#!/usr/bin/env python3

class MP3Track():

    def __init__(self, title, duration, artists=[]):
        self.title = title
        self.mins = duration // 60
        self.secs = duration % 60
        self.artists = artists

    def add_artist(self, artist):
        self.artists.append(artist)

    def __str__(self):
        return "Title: {}\nBy: {}\nDuration: {}:{:02d}".format(self.title, ", ".join(self.artists), self.mins, self.secs)
