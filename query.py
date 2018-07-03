class Query:
    pass

    @classmethod
    def common_class(cls, self, X):
        return [trip for trip in Trip._all if trip._self == self]

jeff.trip()


otherClass._self ???
