# remeber to import the Trip class here
from trip import Trip
from query import Query

class Driver:

    def __init__(self, name, driving_style):
        self._name = name
        self._driving_style = driving_style

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def driving_style(self):
        return self._driving_style

    @driving_style.setter
    def driving_style(self, driving_style):
        self._driving_style = driving_style

    def trips(self):
        return [drive for drive in Trip.all() if drive.driver == self]
#        Query.trips(self, "driver")

    def passengers(self):
        return [drive.passenger for drive in Trip.all() if drive.driver == self]

    def trip_count(self):
        return len(self.trips())
