from server.city import City
from server.gen import Gen
from server.fitness import fitness, List
import random

def generateRandomPath(cityList:List[City]):
    '''
    This method will generate and return a random path
    that will connect all the cities in the list
    '''
    return random.sample(cityList, len(cityList))

def getRandomBetween(minVal, maxVal):
    '''
    This method will return a random number between a max and
    min value. [min,max] 
    '''
    return random.randint(minVal, maxVal)

def createChild(gen1:Gen, gen2:Gen):
    '''
    This method will generate a child of to specified gens
    '''

    #First we get a random number that we will use as a cut index.
    c = getRandomBetween(1, len(gen1.path) - 1)
    path1 = gen1.path
    path2 = gen1.path

    #We generate the new path using a portion of path1 (from the beginning to the cut index)
    #and a portion of path2 (from the cut index inclusive to the end)
    newPath = path1[0:c] + path2[c:]

    #Then we generete a new Gen and calculate its fitness. 
    child = Gen(newPath, fitness(newPath))
    return child


def produceNewGeneration(population:List[Gen], eliteSize:int):
    '''
    This method will produce and return a new Generation of gens using
    the old generation and the elitism technique
    '''

    #The elitism thechique consist in passing a specified quantity of 
    #gens from the old generation to the new one. This old gens would 
    #be the ones with best fitness score. Then, the rest of the new 
    #generation will be generated from random sets of two random gens.

    newGeneration = []

    #Firs we pass the n gens with best score to the new generation
    for i in range(eliteSize):
        newGeneration.append(population[i])

    #We get a random sample of the population, this will randomly mix the gens
    #in the list and return a new List.
    randomPopulation = random.sample(population, len(population))

    #We calculate the quantity of remaining cities for the new generation
    remaining = len(randomPopulation) - eliteSize

    #Then we generate the n new gens and add them to the new generation
    for i in range(remaining):
        child = createChild(randomPopulation[i], randomPopulation[len(randomPopulation) - 1 - i])
        newGeneration.append(child)

    return newGeneration

def mutateGen(path:List[City]):
    '''
    This method will mutate the path of cities of a Gen.
    '''
    #We get two random indexes that would be the pair of cities
    #that we will swap.
    pos1 = getRandomBetween(0, len(path)-1)
    pos2 = getRandomBetween(0, len(path)-1)
    #We need to make sure that both positions are different
    while pos1 == pos2:
        pos2 = getRandomBetween(0, len(path)-1)

    #We swap the cities in the path
    path[pos1], path[pos2] = path[pos2], path[pos1]

    return path    

def mutateGeneration(population:List[Gen], mutationProb:float):
    '''
    This method will receive the population and return it with
    some mutated gens according to the mutation probability. 
    '''
    #We iterate all the gens in the current generation
    for i in range(len(population)):
        #We generate a random number to validate the probability of mutation
        if getRandomBetween(0, 100) <= mutationProb*100:
            #If the statement is True we mutate the gen in the current index
            newPath = mutateGen(population[i].path)
            #Then we replace the old gen with the new mutated one
            population[i] = Gen(newPath, fitness(newPath))

    return population


def geneticAlgorithm(cityList:List[City], nGenerations:int, mutationProb:float, initialPopulation:int, eliteSize:int):
    '''
    Method that will apply the genetic algorithm to a set of cities in order
    to get the most efficient route to visit all of them. 

    nGenerations - Quantity of generations that will be computed to get the path

    mutationProb - The probability (in decimals) to mutate a gen

    initialPopulation - Amount of gens that will be generated for each generation

    eliteSize - Amount of gens for the elitism technique. Less tan initialPopulation
    '''
    population = []

    #First we compute random paths for the first generation of gens
    for _ in range(initialPopulation):
        #Generate the random path
        path = generateRandomPath(cityList)
        #Compute the fitness of the new path
        fit = fitness(path)
        #Add the new gen to the generation
        population.append(Gen(path, fit))


    #We compute the next n generations of gens 
    for i in range(nGenerations):
        #First we sort the population of gens in ascending order using the fitness
        #of each gen's path
        population.sort()

        print("Generation " + str(i))

        #Produce the new generation of gens
        newGeneration = produceNewGeneration(population, eliteSize)
        #Mutate some of the gens using the mutation probability
        newGeneration = mutateGeneration(newGeneration, mutationProb)

        #Change the old generation with the new generated
        population = newGeneration

    #Sort the population in ascending order using the fitness to get the best route
    #as the first element of the list 
    population.sort()

    #Return the best path
    print("Final distance: " + str(population[0].fitness))
    bestPath = population[0].path

    return bestPath, population[0].fitness
