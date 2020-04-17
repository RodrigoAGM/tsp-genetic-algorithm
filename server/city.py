import numpy as np

class City:
    def __init__(self, name:str, x:float, y:float):
        self.name = name
        self.x = x
        self.y = y
    
    def calculateDistance(self, endCity):

        xDistance = abs(self.x - endCity.x)
        yDistance = abs(self.y - endCity.y)

        distance = np.sqrt((xDistance ** 2) + (yDistance ** 2))

        return distance
    
    def __repr__(self):
        return self.name + " (" + str(self.x) + "," + str(self.y) + ")"