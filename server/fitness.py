from city import City
from typing import List

def calculateTotalDistance(path:List[City]):
    '''
    This method will calculate the total sum of distances of a
    provided path of cities
    '''
    
    nCities = len(path)
    totalDistance = 0
    
    #We iterate all the cities
    for i in range(nCities):

        origin = path[i]
        end = None

        #The destination city will always be the next city in the array
        if i + 1 < nCities:
            end = path[i+1]
        #But, for the last element we take the first city as the destination
        else:
            end = path[0]
        
        #We calculate the distance between the origin and end cities
        totalDistance += origin.calculateDistance(end)
    
    return totalDistance

def fitness(path:List[City]):
    '''
    This method will return the fitness of a provided path
    '''
    return calculateTotalDistance(path)