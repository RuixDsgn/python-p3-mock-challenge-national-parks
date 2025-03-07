from classes.national_park import NationalPark
from classes.visitor import Visitor
from classes.trip import Trip
import pytest

class TestVisitor:
    '''Visitor in visitor.py'''

    def test_has_name(self):
        '''Visitor is initialized with a name'''
        visitor = Visitor("John")
        assert (visitor.name == "John")

    def test_name_is_string(self):
        '''Visitor is initialized with a name of type str'''
        visitor = Visitor("Bob")
        assert (isinstance(visitor.name, str))
        
        with pytest.raises(Exception):
            Visitor(2)

    def test_name_setter(self):
        '''Cannot change the name of the visitor'''
        vis = Visitor("Poppy")
        with pytest.raises(Exception):
            vis.name = "Warren"

    def test_has_many_trips(self):
        '''Visitor has many Trips.'''
        p1 = NationalPark("Yosemmette")
        vis = Visitor("Bill")
        vis2 = Visitor('Steve')
        t_1 = Trip(vis, p1, "May 5th", "May 9th")
        t_2 = Trip(vis, p1, "May 20th","May 27th")
        t_3 = Trip(vis2, p1, "January 5th","January 20th")

        assert (len(vis.trips()) == 2)
        assert (t_1 in vis.trips())
        assert (t_2 in vis.trips())
        assert (not t_3 in vis.trips())

    def test_trips_of_type_trips(self):
        '''Visitor trips are of type '''
        vis = Visitor("Phil")
        p1 = NationalPark('Yellow Stone')
        t_1 = Trip(vis, p1, "May 5th", "May 9th")
        t_2 = Trip(vis, p1, "May 20th","May 27th")

        assert (isinstance(vis.trips()[0], Trip))
        assert (isinstance(vis.trips()[1], Trip))

    # def test_has_many_parks(self):
    #     '''Visitor has many parks.'''
    #     vis = Visitor("Flat White")

    #     p1 = NationalPark('Alaska Wilds')
    #     p2 = NationalPark('Bryce Canyon')
    #     t_1 = Trip(vis, p1, "","")
    #     t_2 = Trip(vis, p2, "","")

    #     assert (vis in p1.visitors())
    #     assert (vis in p2.visitors())

    def test_has_unique_parks(self):
        '''Visitor has unique list of all the parks they have visited.'''

        p1 = NationalPark("Yosemmette")
        p2 = NationalPark("Rocky Mountain")
        vis = Visitor('Steeve')
        t_1 = Trip(vis, p1, "May 5th", "May 9th")
        t_2 = Trip(vis, p1, "May 20th","May 27th")
        t_3 = Trip(vis, p2, "January 5th","January 20th")

        assert (len(set(vis.national_parks())) == len(vis.national_parks()))
        assert (len(vis.national_parks()) == 2)

    def test_customers_of_type_customer(self):
        '''Visitor nationalparks are of type NationalPark'''
        p1 = NationalPark("Yosemmette")
        p2 = NationalPark("Rocky Mountain")
        vis = Visitor('Steeeve')
        t_1 = Trip(vis, p1, "May 5th", "May 9th")
        t_3 = Trip(vis, p2, "January 5th","January 20th")

        assert (isinstance(vis.national_parks()[0], NationalPark))
        assert (isinstance(vis.national_parks()[1], NationalPark))

    