from trip import Trip

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
        return [item for item in Trip.all() if item.passenger == self]

    def drivers(self):
        return [item.driver for item in Trip.all() if item.passenger == self]

    def trip_count(self):
        return len(self.trips())
