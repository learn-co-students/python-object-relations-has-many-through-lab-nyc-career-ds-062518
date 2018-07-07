from trip import Trip  # remeber to import the Trip class here

class Driver:

    def __init__(self, name, driving_style):
        self._name = name
        self._driving_style = driving_style
    @property
    def name (self):
        return self._name
    @property
    def driving_style(self):
        return self._driving_style

    def trips(self):
        return [trip for trip in Trip.all() if trip.driver == self]

    def passengers(self):
        return [trip.passenger for trip in Trip.all() if trip.driver == self]

    def trip_count(self):
        number_of_trips = len(self.trips())
        return number_of_trips
