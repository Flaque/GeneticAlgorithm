import heapq
from util import random_gene, randomlyPair, getGenes, random_letter
from fitness import hamming_distance
from operator import itemgetter
from pprint import pprint
from random import random, randint

class Population:

    def __init__(self, size, params):
        self.size = size
        self.items = []
        self.params = params

    def __randomItem(self):
        word_size = self.params["word_size"]
        gene = random_gene(word_size)
        dist = hamming_distance(gene, self.goal)
        return (gene, dist)

    def __appendDistance(self, gene):
        return (gene, hamming_distance(gene, self.goal))

    def generate(self, goal):
        self.goal = goal
        self.items = [self.__randomItem() for i in range(self.size)]

    def sort(self):
        self.items = sorted(self.items, key=itemgetter(1))

    def haveConverged(self, limit):
        if self.items[0][1] <= limit:
            return True
        return False

    def selectBreeders(self):
        return self.items[:self.params["actual"]]

    def mate(self, pairs):
        babies = []
        for left, right in pairs:
            babies.append(left[:len(left)/2] + right[len(right)/2:])
        return babies

    def pairAndMate(self):
        breeders = self.selectBreeders()
        genes = getGenes(breeders)
        pairs = randomlyPair(genes)
        genes.extend(self.mate(pairs))
        self.items = [self.__appendDistance(gene) for gene in genes]

    def best(self):
        return self.items[0]

    def mutate(self):
        for index, (gene, dist) in enumerate(self.items):
            if random() >= self.params["mutation_factor"]:
                gene = list(gene)
                gene[randint(0, len(gene)-1)] = random_letter()
                self.items[index] = self.__appendDistance("".join(gene))

    def display(self):
        pprint(self.items)
