"""Population Class"""

class Population():
    """Population Class."""
    generation = -1

    def __init__(self, chromosomes=None):
        """Creates a new population"""
        self.amount = Settings.get_population_size()
        if chromosomes is None:
            chromosomes = [Chromosome() for i in range(self.amount)]
        self.chromosomes = chromosomes
        self.childs = []
        self.generation = Population.next_generation()
        self._fit_chromosomes()

    @classmethod
    def next_generation(cls):
        """Increase by one the generation counter and return its value"""
        cls.generation += 1
        return cls.generation

    @classmethod
    def reset_generations(cls):
        """Reset the generation counter"""
        cls.generation = 0

    def _fit_chromosomes(self):
        """For each chromosome in the population, calculate its fitness"""
        target_total = self.get_sum()
        for chromosome in self.chromosomes:
            chromosome.fit(target_total)

    def get_generation(self):
        """Return the generation it corresponds"""
        return self.generation

    def get_targets(self):
        """Return a list with the target value of each chromosome."""
        targets = []
        for chromosome in self.chromosomes:
            chromosome_target = chromosome.get_target()
            targets.append(chromosome_target)
        return targets

    def get_maximum(self):
        """Return the maximum target value of the chromosomes"""
        targets = self.get_targets()
        return max(targets)

    def get_minimum(self):
        """Return the minimum target value of the chromosomes"""
        targets = self.get_targets()
        return min(targets)

    def get_sum(self):
        """Return the sum of all the target values of the chromosomes"""
        targets = self.get_targets()
        return sum(targets)

    def get_average(self):
        """Return the average of all the target values of the chromosomes"""
        suma = self.get_sum()
        return suma / self.amount

    def get_range(self):
        """Return the difference between the maximum and the minimum target
            values of the chromosomes"""
        maximum = self.get_maximum()
        minimum = self.get_minimum()
        return maximum - minimum

    def evolve(self):
        """Prepare the next generation."""

        fathers = self._choose_fathers()

        self._cross_over(fathers)

        self._mutate()

        if Settings.get_elitism():
            childs = self.get_fittest_chromosomes()
            self.childs.extend(childs)

    def _choose_fathers(self):
        """Return a list with the fathers, the fathers are chosen acording to
            their fitness value, it will choose as many fathers as the size
            of the population and if elitism, as many as the size minus 2"""
        fathers = []
        number = self.amount
        if Settings.get_elitism():
            number -= 2
        probabilities = self.get_fitness()
        for _ in range(number):
            chromosome = util.choose_n_elements_from_narray(self.chromosomes, probabilities)
            fathers.append(chromosome)
        return fathers

    def get_fitness(self):
        """Return a list with the fitness of each chromosome"""
        fitness = []
        for chromosome in self.chromosomes:
            chromosome_fitness = chromosome.get_fitness()
            fitness.append(chromosome_fitness)
        return fitness

    def _cross_over(self, fathers):
        """Given a list of fathers, when appropiate, cross over them two by two
            and add the resulting childs chromosomes"""
        couples = util.get_next_two(fathers)
        cross_over_prob = Settings.cross_over_prob
        precision = util.get_precision(cross_over_prob)
        for (father1, father2) in couples:
            prob = util.get_random_prob(precision=precision)
            if cross_over_prob > prob:
                childs = self._cross_over_1_point(father1, father2)
            else:
                childs = father1, father2
            self.childs.extend(childs)

    def _cross_over_1_point(self, father1, father2):
        """Perform a 1 point cross over between the given father chromosomes"""
        length = len(father1.get_gene_string())
        split_points = util.get_random_number(0, length)
        father1_gene_parts = self.split_chromosome(father1, split_points)
        father2_gene_parts = self.split_chromosome(father2, split_points)
        child1, child2 = self._mix(father1_gene_parts, father2_gene_parts)
        return child1, child2

    def split_chromosome(self, chromosome, split_point):
        """Given a chromosome and a split_point, return the gene string of the
            chromosome split at the split_point"""
        gene_string = chromosome.get_gene_string()
        return [gene_string[:split_point], gene_string[split_point:]]

    def _mix(self, father1, father2):
        """Given two genes strings split at 1 point, return them mixed"""
        child1_gene_string = "".join((father2[0], father1[1]))
        child2_gene_string = "".join((father1[0], father2[1]))
        child1 = Chromosome(genes=child1_gene_string)
        child2 = Chromosome(genes=child2_gene_string)
        return child1, child2

    def get_fittest_chromosomes(self):
        """Return the two chromosome with the highest fitness value"""
        max_fitness = self.get_max_fitness()
        chromosomes = []
        for maximum in max_fitness:
            gene_string = self.find_gene_string_by_fitness(maximum)
            chromosome = Chromosome(genes=gene_string)
            chromosomes.append(chromosome)
        return chromosomes

    def get_max_fitness(self):
        """Return a list with the 1st and 2nd maximum values of fitness"""
        fitness = self.get_fitness()
        fitness_sorted_list = sorted(fitness, reverse=True)
        return fitness_sorted_list[:2]

    def find_gene_string_by_fitness(self, fitness):
        """Return the chromosome gene string with the given fitness"""
        for chromosome in self.chromosomes:
            if chromosome.get_fitness() == fitness:
                return chromosome.get_gene_string()

    def _mutate(self):
        """Mutate each chromosome when appropiate"""
        mutation_prob = Settings.get_mutation_prob()
        precision = util.get_precision(mutation_prob)
        for chromosome in self.childs:
            prob = util.get_random_prob(precision=precision)
            if mutation_prob > prob:
                chromosome.mutate()

    def get_next_generation(self):
        """Return a new population with this one's childs as chromosomes"""
        next_generation = Population(chromosomes=self.childs)
        return next_generation

    def get_max_gene_string(self):
        """Return the gene string corresponding to the fittest chromosome"""
        max_fitness = max(self.get_fitness())
        for chromosome in self.chromosomes:
            if chromosome.get_fitness() == max_fitness:
                return chromosome.get_gene_string()

if __name__ != "__main__":
    from exercise1.logic.settings_manager import Settings
    from exercise1.entities.chromosome import Chromosome
    import exercise1.util.util as util
