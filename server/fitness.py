from city import City
from typing import List

def calculateTotalDistance(path:List[City]):
    
    nCities = len(path)
    totalDistance = 0
    
    for i in range(nCities):

        origin = path[i]
        end = None

        if i + 1 < nCities:
            end = path[i+1]
        else:
            end = path[0]
        
        totalDistance += origin.calculateDistance(end)
    
    return totalDistance

def fitness(path:List[City]):
    return calculateTotalDistance(path)