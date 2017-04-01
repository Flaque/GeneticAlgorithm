from random import choice, shuffle
from string import ascii_lowercase

def random_gene(length):
    """ Generates a random lowercase string of length 12 """
    return ''.join(choice(ascii_lowercase) for i in range(length))

def random_letter():
    return choice(ascii_lowercase)

def randomlyPair(items):
    shuffle(items)
    left, right = items[:len(items)/2], items[len(items)/2:]
    return zip(left, right)

def getGenes(items):
    return [items[i][0] for i in range(len(items))]
