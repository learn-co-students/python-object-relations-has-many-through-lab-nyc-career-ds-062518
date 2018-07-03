class Trip:

   _all = []

   def __init__(self, driver, passenger):
       self._driver = driver
       self._passenger = passenger
       Trip._all.append(self)
       # remember to keep track of all trip instances

   @property
   def driver(self):
       return self._driver

   @driver.setter
   def driver(self, driver):
       self._driver = driver

   @property
   def passenger(self):
       return self._passenger

   @passenger.setter
   def passenger(self, passenger):
       self._passenger = passenger

   @classmethod
   def all(cls):
       return cls._all
