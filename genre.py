# remeber to import the Song class here
from song import Song

class Genre:

    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    def songs(self):
        return [music for music in Song.all() if  music.genre == self]

    def artists(self):
        return [music.artist for music in Song.all() if  music.genre == self]
