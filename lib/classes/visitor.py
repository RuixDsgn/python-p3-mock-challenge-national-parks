class Visitor:

    all = []

    def __init__(self, name):
        self.name = name
        Visitor.all.append(self)
           
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if hasattr(self, "name"):
            raise Exception("Attribute 'name' should not be changed after the Visitor is created.")
        elif (type(name) == str) and (1 <= len(name) <= 15):
            self._name = name
        else:
            raise Exception()

    def trips(self):
        from classes.trip import Trip
        return [trip for trip in Trip.all if self == trip.visitor]
    
    def national_parks(self):
        parks = [trip.national_park for trip in self.trips()]
        return [*set(parks)]