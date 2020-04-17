from city import City
from gen import Gen
from fitness import fitness, List
import random

def generateRandomPath(cityList:List[City]):
    return random.sample(cityList, len(cityList))

def getRandomBetween(minVal, maxVal):
    return random.randint(minVal, maxVal)

def createChild(gen1:Gen, gen2:Gen):

    c = getRandomBetween(1, len(gen1.path))
    path1 = gen1.path
    path2 = gen1.path

    newPath = path1[0:c] + path2[c:]

    child = Gen(newPath, fitness(newPath))
    return child


def produceNewGeneration(population:List[Gen], eliteSize:int):

    newGeneration = []

    for i in range(eliteSize):
        newGeneration.append(population[i])

    randomPopulation = random.sample(population, len(population))

    remaining = len(randomPopulation) - eliteSize

    for i in range(remaining):
        child = createChild(randomPopulation[i], randomPopulation[len(randomPopulation) - 1 - i])
        newGeneration.append(child)

    return newGeneration

def mutateGen(path:List[City]):

    pos1 = getRandomBetween(0, len(path)-1)

    pos2 = getRandomBetween(0, len(path)-1)
    
    while pos1 == pos2:
        pos2 = getRandomBetween(0, len(path)-1)

    path[pos1], path[pos2] = path[pos2], path[pos1]

    return path    

def mutateGeneration(population:List[Gen], mutationProb:float):

    for i in range(len(population)):
        if getRandomBetween(0, 100) <= mutationProb*100:
            newPath = mutateGen(population[i].path)
            population[i] = Gen(newPath, fitness(newPath))

    return population


def geneticAlgorithm(cityList:List[City], nGenerations:int, mutationProb:float, initialPopulation:int, eliteSize:int):
    
    population = []

    for _ in range(initialPopulation):
        path = generateRandomPath(cityList)
        fit = fitness(path)
        population.append(Gen(path, fit))


    for i in range(nGenerations):
        population.sort()

        print("Generation " + str(i))

        newGeneration = produceNewGeneration(population, eliteSize)
        newGeneration = mutateGeneration(newGeneration, mutationProb)

        population = newGeneration

    population.sort()
    print("Final distance: " + str(population[0].fitness))
    bestRoute = population[0].path

    return bestRoute
