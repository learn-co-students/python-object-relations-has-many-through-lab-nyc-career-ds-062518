class Song:

    _all = []

    def __init__(self, name, artist, genre):
        self._name = name
        self._artist = artist
        self._genre = genre
        Song._all.append(self)

    @property
    def name(self):
        return self._name

    @property
    def genre(self):
        return self._genre

    @property
    def artist(self):
        return self._artist

    @classmethod
    def all(cls):
        return cls._all
