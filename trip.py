class Trip:

    _all = []

    @classmethod
    def all(cls):
        return cls._all

    def __init__(self, driver, passenger):
        self._driver = driver
        self._passenger = passenger
        Trip.all().append(self)

    @property
    def driver(self):
        return self._driver
    @property
    def passenger(self):
        return self._passenger
    
