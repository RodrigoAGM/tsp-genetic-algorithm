import numpy as np

#This is the class that represents a city with a name and (x,y) coordinates.

class City:
    def __init__(self, name:str, x:float, y:float):
        self.name = name
        self.x = x
        self.y = y
    
    def calculateDistance(self, endCity):
        '''
        Method used to calculate the euclidean distance between this and another city
        '''

        xDistance = abs(self.x - endCity.x)
        yDistance = abs(self.y - endCity.y)

        distance = np.sqrt((xDistance ** 2) + (yDistance ** 2))

        return distance
    
    def __repr__(self):
        return self.name + " (" + str(self.x) + "," + str(self.y) + ")"