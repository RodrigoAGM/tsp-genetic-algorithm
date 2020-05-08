import numpy as np

# This is the class that represents a city with a name and (x,y) coordinates.


class City:
    """
    Represents a city to visit for the traveler salesman into the map

    Attributes
    ----------
    lat: float
        The latitude of the city
    lng: float
        The longitude of the city
    """

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __repr__(self):
        # Mapper for the City object
        return " (" + str(self.x) + "," + str(self.y) + ")"
