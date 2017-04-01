import json

initial = input("Enter number of initial population: ")
actual = input("Enter actual population per cycle: ")
word_size = input("Enter size of word to be guessed: ")
mutation_factor = input("Enter mutation factor (in decimal): ")
max_generations = input("Enter max generations: ")

with open('params.dat', 'w') as outfile:
    json.dump({"initial": initial,
        "actual":actual,
        "word_size": word_size,
        "mutation_factor": mutation_factor,
        "max_generations": max_generations}, outfile)

    print("Wrote to file")
