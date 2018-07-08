class Trip:

    _all = []
    _count = 0

    def __init__(self, driver, passenger):
        self._driver = driver
        self._passenger = passenger
        Trip._all.append(self)
        Trip._count += 1

    @property
    def driver(self):
        return self._driver

    @property
    def passenger(self):
        return self._passenger

    @classmethod
    def all(cls):
        return cls._all
