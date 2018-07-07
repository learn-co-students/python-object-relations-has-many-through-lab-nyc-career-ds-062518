class Song:

    _all = []

    def __init__(self, name, artist, genre):
        self._name = name
        self._artist = artist
        self._genre = genre
        Song.all().append(self)
        # remember to keep track of all trip instances
    @property
    def name (self):
        return self._name
    @property
    def artist(self):
        return self._artist
    @property
    def genre(self):
        return self._genre
    @classmethod
    def all(cls):
        return Song._all
