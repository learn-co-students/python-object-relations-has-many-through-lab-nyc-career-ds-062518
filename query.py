from trip import Trip

class Query:


    def trips(self, type):
        return [drive for drive in Trip.all() if drive.type == self]

    def other(self, type):
        pass

    def trip_count(self):
        return len(self.trips())

    def songs(self):
        return [music for music in Song.all() if  music.type == self]

    def genres(self):
        pass
