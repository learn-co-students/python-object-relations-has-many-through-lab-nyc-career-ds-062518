from trip import Trip

class Query:
    @classmethod
    def trips(cls, name):
        return [item for item in Trip.all() if item.driver == name]
