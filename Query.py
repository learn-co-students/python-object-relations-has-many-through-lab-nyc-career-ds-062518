from trip import Trip

class Query:

    def trips(self):
        return [trip for trip in Trip._all if trip._passenger  == self]
