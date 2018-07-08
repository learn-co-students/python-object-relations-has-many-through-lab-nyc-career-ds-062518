from trip import Trip

class Driver:

    def __init__(self, name, driving_style):
        self._name = name
        self._driving_style = driving_style

    def trips(self):
        return [trip for trip in Trip.all() if trip.driver == self]

    def passengers(self):
        return [trip.passenger for trip in Trip.all() if trip.driver == self]

    def trip_count(self):
        return len(self.trips())

    @property
    def name(self):
        return self._name

    # @name.getter
    # def name(self, name):
    #     self._name = name

    @property
    def driving_style(self):
        return self._driving_style

    # @driving_style.getter
    # def driving_style(self, driving_style):
    #     self._driving_style = driving_style
