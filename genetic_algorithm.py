import random
import string
import operator

class Organism:
    def __init__(self, attributes):
        self.attributes = attributes
        self.fitness = self.fitness()
        self.mutation_chance = (self.fitness**3) / 216
    
    def fitness(self):
        fitness = 0
        if (self.attributes[0] == "H"):
            fitness += 1
        if (self.attributes[1] == "e"):
            fitness += 1
        if (self.attributes[2] == "l"):
            fitness += 1
        if (self.attributes[3] == "l"):
            fitness += 1
        if (self.attributes[4] == "0"):
            fitness += 1
        if (self.attributes[5] == " "):
            fitness += 1
        if (self.attributes[6] == "C"):
            fitness += 1
        if (self.attributes[7] == "S"):
            fitness += 1
        if (self.attributes[8] == " "):
            fitness += 1
        if (self.attributes[9] == "5"):
            fitness += 1
        if (self.attributes[10] == "0"):
            fitness += 1
        if (self.attributes[11] == "1"):
            fitness += 1
        if (self.attributes[12] == "!"):
            fitness += 1
    
        return fitness


# generate offspring
def reproduce(parent_1, parent_2, possible_characters):
    crossover_location = random.randint(1, 12)

    # Create a child
    child = Organism(parent_1[0 : crossover_location] + parent_2[crossover_location : 13])



    for i in range(13):
        if random.randrange(50) == 0:
            child.attributes = child.attributes[: i] + random.choice(possible_characters) + child.attributes[i + 1 :]

    return child


def main():
    # generate initial population
    population = []
    organism_attribute = ""
    possible_characters = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!\"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ "
    generation = 0
    
    for i in range(100):
        for j in range(13):
            organism_attribute += random.choice(possible_characters)
        
        population.append(Organism(organism_attribute))
        organism_attribute = ""
    

    while (population[0].fitness != 13):
        # Sort by fitness
        population.sort(key=operator.attrgetter('fitness'))
        population.reverse()

        print("Generation: " + str(generation) + " | Organism: " + population[0].attributes + " | Max fitness: " + str(population[0].fitness))
        
        # Kill least fit 1/2
        #print(str(generation) + " " + str(len(population)))
        for i in range(99, 49, -1):
            del population[i]
        
        # Breeding
        parent_1 = 0
        parent_2 = 1

        while (parent_2 != 49):
            child_1 = reproduce(population[parent_1].attributes, population[parent_2].attributes, possible_characters)
            child_2 = reproduce(population[parent_1].attributes, population[parent_2].attributes, possible_characters)
            population.append(child_1)
            population.append(child_2)
            parent_1 += 1
            parent_2 += 1
        
        generation += 1


if __name__ == "__main__":
    main()