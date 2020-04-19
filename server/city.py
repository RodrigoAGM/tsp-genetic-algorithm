import numpy as np

# This is the class that represents a city with a name and (x,y) coordinates.


class City:
    """
    Represents a city to visit for the traveler salesman into the map

    Attributes
    ----------
    name: str
        The name of the city
    x: int
        The horizontal coordinate into the map for the city
    x: int
        The vertical coordinate into the map for the city
    """

    def __init__(self, name: str, x: float, y: float):
        self.name = name
        self.x = x
        self.y = y

    def calculateDistance(self, endCity):
        '''
        Method used to calculate the euclidean distance between this and another city
        Parameters
        ----------
        endCity : City
            The end city
        '''

        xDistance = abs(self.x - endCity.x)
        yDistance = abs(self.y - endCity.y)

        distance = np.sqrt((xDistance ** 2) + (yDistance ** 2))

        return distance

    def __repr__(self):
        # Mapper for the City object
        return self.name + " (" + str(self.x) + "," + str(self.y) + ")"
