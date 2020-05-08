from server.city import City
from typing import List
import math
import random

class SimulatedAnnealing(object):

    def __init__(self, cityList: List[City], temperature: float = None, coldIndex: float = None,
                 stoppingIteration: int = None, stoppingTemperature: float = None):
        '''
        In this method we initialise all the atributes that we will need
        for the algorithm
        '''
        self.cityList = cityList
        self.N = len(cityList)
        self.temperature = 1000 if not temperature else temperature
        self.coldIndex = 0.995 if not coldIndex else (1-coldIndex)
        self.stoppingTemperature = 1e-8 if not stoppingTemperature else stoppingTemperature
        self.stoppingIteration = 100000 if not stoppingIteration else stoppingIteration

        self.iteration = 0
        self.progress = []

        self.currentRoute = None
        self.currentEnergy = float("Inf")
        self.bestRoute = None
        self.bestEnergy = float("Inf")

    def generateRandomRoute(self):
        '''
        This method will generate and return a random route
        that will connect all the cities in the list. This will
        be a path of indexes.
        '''
        #First we generate a list with all the indexes from citylist
        listnum = [i for i in range(0, self.N)]
        #Then we return the same array but with the elements in random positions
        return random.sample(listnum, self.N)

    def calculateEnergy(self, index1: int, index2: int):
        '''
        This method will compute the euclidean distance between 
        two cities using the cities indexes.
        '''
        #First we get the cities using the indexes
        city1, city2 = self.cityList[index1], self.cityList[index2]
        #Then we return the euclidean distance between these two cities
        return math.sqrt((city1.x - city2.x) ** 2 + (city1.y - city2.y) ** 2)

    def calculateRouteEnergy(self, route: List[int]):
        '''
        This method will compute the euclidean distance of all
        the cities in the route.  
        '''
        totalEnergy = 0

        #We iterate in every city in the citylist
        for i in range(0, self.N - 1):

            #We determine the endIndex, if we are in the last city in the
            #array, we need to connect it with the first city to close the route
            endIndex = 0 if i == (self.N - 1) else i + 1
            #We add the energy beetween two neighbour cities
            totalEnergy += self.calculateEnergy(route[i], route[endIndex])

        return totalEnergy

    def acceptanceFunction(self, newRoute):
        '''
        This method will determine if the new route could replace
        the actual route and, if possible, the best route. This will use
        the total route energy as decision criteria
        '''
        #First we get the total route energy of the new route
        newEnergy = self.calculateRouteEnergy(newRoute)

        #We compare the energy of the new route with the current route
        if newEnergy < self.currentEnergy:

            #if the energy of the new route is smaller, we change the current
            #route data with the new route data
            self.currentEnergy, self.currentRoute = newEnergy, newRoute

            #Then we check if this new route is also better than the actual best
            #route using the energy.
            if newEnergy < self.bestEnergy:
                
                #if the energy of the new route is smaller, we change the best 
                #route data with the new route data
                self.bestEnergy, self.bestRoute = newEnergy, newRoute

        else:

            #if not, we generate a random number and compare it with the
            #acceptance math function
            if random.random() < math.exp(-abs(newEnergy - self.currentEnergy) / self.temperature):

                #if the result of the acceptance math function is greater, we change the
                #current route data with the new route data
                self.currentEnergy, self.currentRoute = newEnergy, newRoute

    def executeAlgorithm(self):
        '''
        This method will execute the simulated annealing algorithm
        and return the best route with its energy
        '''
        #First we generate a random route to use as starting point for
        #the algorithm
        initRoute = self.generateRandomRoute()
        self.currentRoute, self.currentEnergy = initRoute, self.calculateRouteEnergy(initRoute)

        #We add the current energy to the progress list two draw a graphic at the end
        self.progress.append(self.currentEnergy)

        #We iterate until we reach the stopping iteration number or the
        #lowest temperature possible.
        while self.iteration < self.stoppingIteration and self.temperature >= self.stoppingTemperature:

            #Copy the current route as the new route two edit
            newRoute = list(self.currentRoute)

            #Generate to random indexes to mutate the route
            randomIndex1 = random.randint(2, self.N - 1)
            randomIndex2 = random.randint(0, self.N - randomIndex1)

            #we replace the route from the index1 to the index two with the same values but reversed
            newRoute[randomIndex1:(randomIndex2+randomIndex1)] = newRoute[randomIndex1:(randomIndex2+randomIndex1)][::-1]

            #apply the acceptance function to the new route
            self.acceptanceFunction(newRoute)

            #then we reduce the temperature with the coldIndex
            self.temperature *= self.coldIndex

            #increment the iteration
            self.iteration += 1

            #add the current energy to the progress list two draw a graphic at the end
            self.progress.append(self.currentEnergy)

        #Print results
        print("The best route found was: " + str(self.bestRoute))
        print("The best energy value is: " + str(self.bestEnergy))

        #Return best route and energy
        return self.bestRoute, self.bestEnergy
