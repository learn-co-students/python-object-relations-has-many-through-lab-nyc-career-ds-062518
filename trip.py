class Trip:

    _all = []

    def __init__(self, driver, passenger):
        self._driver = driver
        self._passenger = passenger
        Trip.all().append(self)
        # remember to keep track of all trip instances
    @property
    def driver(self):
        return self._driver
    @property
    def passenger(self):
        return self._passenger
    @classmethod
    def all(cls):
        return Trip._all
