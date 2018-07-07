# remeber to import the Song class here
from song import Song

class Genre:

    def __init__(self, name):
        self._name = name
    @property
    def name(self):
        return self._name
    def songs(self):
        return [song for song in Song.all() if song.genre == self]

    def artists(self):
        return [song.artist for song in Song.all() if song.genre == self]
