# Instructions :
# This challenge is about Biology that will put emphasis on your knowledge of classes, inheritance and
# polymorphism.

# Build a DNA object. DNA is composed of chromosomes which is itself composed of Genes.
# A Gene is a single value 0 or 1, it can mutate (flip).
# A Chromosome is a series of 10 Genes. It also can mutate, meaning a random number of genes can
# randomly flip (1/2 chance to flip).
# A DNA is a series of 10 chromosomes, and it can also mutate the same way Chromosomes can mutate.

# Implement these classes as you see fit.

# Create a new class called Organism that accepts a DNA object and an environment parameter that sets
# the probability for its DNA to mutate.

# Instantiate a number of Organism and let them mutate until one gets to a DNA which is only made of
# 1s. Then stop and record the number of generations (iterations) it took.
# Write your results in you personal biology research notebook and tell us your conclusion :).

import random


class Gene:
    def __init__(self):
        self.value = random.randint(0, 1)

    def mutate(self):
        """Flip the gene's value"""
        self.value = 1 - self.value


class Chromosome:
    def __init__(self):
        self.genes = [Gene() for _ in range(10)]

    @property
    def sum(self):
        # A property to dynamically calculate the sum of genes
        return sum(gene.value for gene in self.genes)

    def mutate(self):
        """A random number of genes can flip. The number of flips is random (0-10)"""
        num_flips = random.randint(0, 10)
        for _ in range(num_flips):
            gene_to_flip = random.choice(self.genes)
            gene_to_flip.mutate()


class DNA:
    def __init__(self):
        self.chromosomes = [Chromosome() for _ in range(10)]

    @property
    def sum(self):
        # A property to dynamically calculate the sum of genes
        return sum(chromosome.sum for chromosome in self.chromosomes)

    def mutate(self):
        """A random number of chromosomes can mutate."""
        num_flips = random.randint(0, 10)
        for _ in range(num_flips):
            chromosomes_to_flip = random.choice(self.chromosomes)
            chromosomes_to_flip.mutate()


class Organism:
    def __init__(self, dna, environment_prob):
        self.dna = dna
        self.environment_prob = environment_prob

    def mutate(self):
        if random.random() < self.environment_prob:
            self.dna.mutate()


def run_simulation(organisms):
    generations = 0
    target_sum = 100
    while True:
        generations += 1
        if generations % 1000 == 0:  # Print every 1000 generations
            print(f"Generation {generations}: Still simulating...")
        found_winner = False

        for organism in organisms:
            organism.mutate()
            if organism.dna.sum == target_sum:
                print(
                    f"Organism with environment probability {organism.environment_prob} reached all 1s!"
                )
                found_winner = True
                break

        if found_winner:
            break

    return generations


organism_1 = Organism(DNA(), 0.1)
organism_2 = Organism(DNA(), 0.2)
organism_3 = Organism(DNA(), 0.5)
organism_4 = Organism(DNA(), 0.7)
organism_5 = Organism(DNA(), 0.8)
organism_6 = Organism(DNA(), 1)

organism_list = [organism_1, organism_2, organism_3, organism_4, organism_5, organism_6]


generations_taken = run_simulation(organism_list)
print(
    f"It took {generations_taken} generations for an organism to reach the target DNA."
)
