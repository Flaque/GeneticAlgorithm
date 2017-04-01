from population import Population
from files import readParamsFile

params = readParamsFile('params.dat')

def ga(size):
    pop = Population(size, params)
    pop.generate("honey")
    pop.sort()

    iterations = 0

    while not pop.haveConverged(0):
        iterations += 1
        pop.pairAndMate()
        pop.mutate()
        pop.sort()

    pop.display()
    print iterations

ga(50)
