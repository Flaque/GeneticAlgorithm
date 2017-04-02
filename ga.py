from population import Population
from files import readParamsFile
from pprint import pprint


params = readParamsFile('params.dat')

def ga(size):
    pop = Population(size, params)
    pop.generate("honey")
    pop.sort()

    iterations = []

    while not pop.haveConverged(0):
        pop.pairAndMate()
        pop.mutate()
        pop.sort()
        iterations.append(pop.best())


    pprint(iterations)
    print len(iterations)

ga(50)
