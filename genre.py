from song import Song

class Genre:

   def __init__(self, name):
       self._name = name

   @property
   def name(self):
       return self._name

   @name.setter
   def name(self, name):
       self._name = name

   def songs(self):
       return [song for song in Song._all if song._genre == self]

   def artists(self):
       return [song._artist for song in Song._all if song._genre == self]
