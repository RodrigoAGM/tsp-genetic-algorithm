from city import City
from typing import List
import math

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

    


