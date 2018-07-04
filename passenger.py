from trip import Trip

class Passenger:

    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name
    @property
    def age(self):
        return self._age

    def trips(self):
        return [trip for trip in Trip.all() if trip.passenger == self]

    def drivers(self):
        return [trip.driver for trip in self.trips()]

    def trip_count(self):
        return len(self.trips())
