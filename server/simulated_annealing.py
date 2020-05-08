from city import City
from typing import List
import math
import random

class SimulatedAnnealing(object):

    def __init__(self, cityList:List[City], temperature:float = None, coldIndex:float = None, 
                                stoppingIteration:int = None, stoppingTemperature:float = None):
        self.cityList = cityList
        self.N = len(cityList)
        self.temperature = 1000 if not temperature else temperature
        self.coldIndex = 0.995 if not coldIndex else (1-coldIndex)
        self.stoppingTemperature = 1e-8 if not stoppingTemperature else stoppingTemperature
        self.stoppingIterations = 100000 if not stoppingIterations else stoppingIterations

        self.currentRoute = None
        self.currentEnergy = float("Inf")
        self.bestRoute = None
        self.bestEnergy = float("Inf")


    def generateRandomPath(self):

        listnum = [i for i in range(0, self.N)]
        return random.sample(listnum, self.N)

    def calculateEnergy(self, index1:int, index2:int):

        city1, city2 = self.cityList[index1], self.cityList[index2]
        return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)
    
    def calculatePathEnergy(self, path:List[int]):

        totalEnergy = 0

        for i in range(0, self.N - 1):

            endIndex = 0 if i == (self.N - 1) else i + 1
            totalEnergy += self.dist(path[i], path[endIndex])

        return totalEnergy


