class Gen:
    def __init__(self, path, fitness:float):
        self.path = path
        self.fitness =  fitness

    def __lt__(self, other):
         return self.fitness < other.fitness

    def __gt__(self, other):
         return self.fitness > other.fitness
    
    def __repr__(self):
        return "[" + str(self.path) + "] = " + str(self.fitness)