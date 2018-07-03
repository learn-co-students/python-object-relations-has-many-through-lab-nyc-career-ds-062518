# import Trip class here
from trip import Trip
#from query import Query

class Passenger:

    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        self._name = name

    @property
    def age(self):
        return self._age
    @age.setter
    def age(self, age):
        self._age = age

    def trips(self):
        return [trip for trip in Trip._all if trip._passenger == self]

    def drivers(self):
        return [trip.driver for trip in self.trips()]

    def trip_count(self):
        return len(self.trips())
