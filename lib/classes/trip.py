
class Trip:

    all = []
    
    def __init__(self, visitor, national_park, start_date, end_date):
        self.visitor = visitor
        self.national_park = national_park
        self.start_date = start_date
        self.end_date = end_date
        Trip.all.append(self)
    
    @property
    def visitor(self):
        return self._visitor
    
    @visitor.setter
    def visitor(self, visitor):
        from classes.visitor import Visitor
        if isinstance(visitor, Visitor):
            self._visitor = visitor
        else:
            raise Exception()
    
    @property
    def national_park(self):
        return self._national_park
    
    @national_park.setter
    def national_park(self, national_park):
        from classes.national_park import NationalPark
        if isinstance(national_park, NationalPark):
            self._national_park = national_park
        else:
            raise Exception()


    @property
    def start_date(self):
        return self._start_date
    
    @start_date.setter
    def start_date(self, start_date):
        if (type(start_date) == str):
            self._start_date = start_date
    
    @property
    def end_date(self):
        return self._end_date
    
    @end_date.setter
    def end_date(self, end_date):
        if (type(end_date) == str):
            self._end_date = end_date