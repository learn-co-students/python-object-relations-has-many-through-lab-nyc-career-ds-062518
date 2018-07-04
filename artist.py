from song import Song

class Artist:

    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    def songs(self):
        return [song for song in Song.all() if song.artist == self]

    def genres(self):
        return [song.genre for song in self.songs()]
