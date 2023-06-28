class NationalPark:

    def __init__(self, name):
        self._name = name
        if (type(name) == str) and hasattr(self, "name"):
            self._name = name
        else:
            raise Exception("Attribute 'name' should not be changed after the NationalPark is created.")


    @property
    def name(self):
            return self._name
    
    @name.setter
    def name(self, name, value):
        if (type(name) == str) and hasattr(self, "name"):
            self._name = name
        else:
            raise Exception("Attribute 'name' should not be changed after the NationalPark is created.")

        
    def trips(self):
        from classes.trip import Trip
        return [trip for trip in Trip.all if self == trip.national_park]
    
    def visitors(self):
        visits = [trip.visitor for trip in self.trips()]
        return [*set(visits)]

    def total_visits(self):
        return len(self.trips())
    
    def best_visitor(self):
        from classes.visitor import Visitor
        counter = dict()
        for trip in self.trips():
            v_name = trip.visitor.name
            try:
                counter[v_name] += 1
            except KeyError:
                counter[v_name] = 1
        return [vis for vis in Visitor.all if vis.name == max(counter)][0]