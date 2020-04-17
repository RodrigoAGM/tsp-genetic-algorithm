# This is the class that represents a gen for the algorithm. Each Gen has
# a path of cities and a fitness value

class Gen:
    def __init__(self, path, fitness:float):
        self.path = path
        self.fitness =  fitness

    def __lt__(self, other):
        #This method will let us compare if a gen fitness is less than another
        #gen fitness. This will be useful to sort a list of gens 
        return self.fitness < other.fitness

    def __gt__(self, other):
        #This method will let us compare if a gen fitness is greater than another
        #gen fitness. This will be useful to sort a list of gens 
        return self.fitness > other.fitness
    
    def __repr__(self):
        return "[" + str(self.path) + "] = " + str(self.fitness)