"""Population Class"""

class Population():
    """Population Class."""
    def __init__(self, individuals=None):
        population_size = Settings.get_population_size()
        self.amount = population_size
        if individuals is None:
            individuals = self.__generate_individuals(self.amount)
        self.individuals = individuals
        self.childs = []
        self.fathers = []
        self.genes = self.get_genes()
        self.maximum = self.__calc_maximum()
        self.minimum = self.__calc_minimum()
        self.average = self.__calc_average()
        self.least = self.__calc_least()
        self.range = self.__calc_range()
        self.generation = "Final"

    def set_generation(self, value):
        """Set the generation it corresponds"""
        self.generation = value

    def __generate_individuals(self, size):
        return [Individual() for i in range(size)]

    def __calc_maximum(self):
        return max(self.genes)

    def __calc_minimum(self):
        return min(self.genes)

    def __calc_average(self):
        total = sum(self.genes)
        return total / self.amount

    def __calc_least(self):
        distance = 0
        for gene in self.genes:
            distance_unrounded = (self.average - gene) ** 2
            distance += int(distance_unrounded)
        return distance

    def __calc_range(self):
        return self.maximum - self.minimum

    def evolve(self):
        """Prepare the next generation."""
        self.__fitness()

        self.__choose_fathers()

        self.__cross_over()

        self.__mutate()

    def __mutate(self):
        mutation_prob = Settings.get_mutation_prob()
        for individual in self.childs:
            prob = Util.get_random_prob(precision=5)
            if prob < mutation_prob:
                individual.mutate()

    def survive(self):
        """Replace the old generation with the new one."""
        next_generation = Population(individuals=self.childs)
        return next_generation

    def __fitness(self):
        target_total = self.get_total_target()
        for individual in self.individuals:
            individual.fit(Settings.target, target_total)

    def __acumulated_fitness(self):
        acum = []
        fitness_acum = 0
        for individual in self.individuals:
            fitness_acum += individual.get_fitness()
            acum.append(fitness_acum)

        if acum[-1] != 1:
            acum[-1] = 1

        return acum

    def __choose_fathers(self):
        fitness_acumulated_values = self.__acumulated_fitness()
        for _ in range(self.amount):
            prob = Util.get_random_prob()
            index = Util.find_bigger(fitness_acumulated_values, prob)
            individual = self.individuals[index]
            self.fathers.append(individual)

    def __make_couples(self, fathers):
        amount = self.amount // 2
        couples = []
        for i in range(amount):
            couple = [fathers[i*2], fathers[i*2+1]]
            couples.append(couple)
        return couples

    def __cross_over(self):
        couples = self.__make_couples(self.fathers)
        cross_over_prob = Settings.cross_over_prob
        for (father1, father2) in couples:
            prob = Util.get_random_prob()
            if prob < cross_over_prob:
                child1, child2 = self.__cross_over_n_points(father1, father2)
            else:
                child1, child2 = father1, father2

            self.childs.append(child1)
            self.childs.append(child2)

    def __cross_over_n_points(self, father1, father2, points=1):
        length = father1.get_size()
        split_points = self.__get_split_points(points, length)
        father1_gene_parts = self.__split_in_parts(father1, split_points)
        father2_gene_parts = self.__split_in_parts(father2, split_points)
        child1, child2 = self.__mix(father1_gene_parts, father2_gene_parts)
        return child1, child2

    def __get_split_points(self, points, length):
        split_points = []
        for _ in range(points):
            split_point = Util.get_random_number(0, length)
            split_points.append(split_point)
        return split_points

    def __split_in_parts(self, father, split_points):
        start = 0
        parts = []

        lenght = father.get_size()
        if split_points[-1] != lenght:
            split_points.append(lenght)

        for i in split_points:
            end = i
            gene_string = father.get_gene_string()
            part = gene_string[start:end]
            parts.append(part)
            start = end

        return parts

    def __mix(self, father1, father2):
        child1_raw = []
        child2_raw = []
        joint = zip(father1, father2)
        for i, (father1, father2) in enumerate(joint):
            if i % 2 == 0:
                child1_raw.extend(father1)
                child2_raw.extend(father2)
            else:
                child1_raw.extend(father2)
                child2_raw.extend(father1)
        child1_gene_string = "".join(child1_raw)
        child2_gene_string = "".join(child2_raw)
        child1 = Individual(genes=child1_gene_string)
        child2 = Individual(genes=child2_gene_string)
        return child1, child2

    def get_fitness(self):
        """Return the fitness value of each individual."""
        fitness = []
        for individual in self.individuals:
            individual_fitness = individual.get_fitness()
            fitness.append(individual_fitness)
        return fitness

    def get_total_target(self):
        """Return the total target value of all individuals."""
        target = self.get_target()
        return sum(target)

    def get_target(self):
        """Return the target value of each individual."""
        target = []
        individuals_genes = self.get_genes()
        for individual_gene in individuals_genes:
            individual_target = Settings.target(individual_gene)
            target.append(individual_target)
        return target

    def get_genes(self):
        """Return the genes string of each individual."""
        genes = []
        for individual in self.individuals:
            gene = individual.get_gene()
            genes.append(gene)
        return genes

if __name__ == "__main__":
    pass
else:
    from numpy.random import randint
    from settings import Settings
    from individual import Individual
    from util import Util
    from algorithm import Algorithm
