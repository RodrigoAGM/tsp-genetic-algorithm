from server.city import City
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
        self.stoppingIteration = 100000 if not stoppingIteration else stoppingIteration

        self.iteration = 0
        self.currentRoute = None
        self.currentEnergy = float("Inf")
        self.bestRoute = None
        self.bestEnergy = float("Inf")


    def generateRandomRoute(self):

        listnum = [i for i in range(0, self.N)]
        return random.sample(listnum, self.N)

    def calculateEnergy(self, index1:int, index2:int):

        city1, city2 = self.cityList[index1], self.cityList[index2]
        return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)
    
    def calculateRouteEnergy(self, route:List[int]):

        totalEnergy = 0

        for i in range(0, self.N - 1):

            endIndex = 0 if i == (self.N - 1) else i + 1
            totalEnergy += self.calculateEnergy(route[i], route[endIndex])

        return totalEnergy


    def acceptanceFunction(self, newRoute):
    
        newEnergy = self.calculateRouteEnergy(newRoute)

        if newEnergy < self.currentEnergy:

            self.currentEnergy, self.currentRoute = newEnergy, newRoute

            if newEnergy < self.bestEnergy:

                self.bestEnergy, self.bestRoute = newEnergy, newRoute

        else:

            if random.random() < math.exp(-abs(newEnergy - self.currentEnergy) / self.temperature):

                self.currentEnergy, self.currentRoute = newEnergy, newRoute


    def executeAlgorithm(self):

        initRoute = self.generateRandomRoute()
        self.currentRoute, self.currentEnergy = initRoute, self.calculateRouteEnergy(initRoute)

        progress = []
        progress.append(self.currentEnergy)

        while self.iteration < self.stoppingIteration and self.temperature >= self.stoppingTemperature:

            newRoute = list(self.currentRoute)

            randomIndex1 = random.randint(2, self.N - 1)
            randomIndex2 = random.randint(0, self.N - randomIndex1)

            newRoute[randomIndex1:(randomIndex2+randomIndex1)] = newRoute[randomIndex1:(randomIndex2+randomIndex1)][::-1]

            self.acceptanceFunction(newRoute)
            self.temperature *= self.coldIndex
            self.iteration +=1

            
        print("The best route found was: " + str(self.bestRoute))
        print("The best energy value is: " + str(self.bestEnergy))

        return self.bestRoute, self.bestEnergy