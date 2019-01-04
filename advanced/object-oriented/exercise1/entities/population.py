"""Population Class"""


class Population():

    def __init__(self, chromosomes=None, generation=1):
        """Creates a new population"""
        self.amount = Settings.get_population_size()

        if chromosomes is None:
            chromosomes = [Chromosome() for i in range(self.amount)]

        self.generation = generation
        self.chromosomes = chromosomes
        self.childs = []
        self._fit_chromosomes()

    def _fit_chromosomes(self):
        """For each chromosome in the population, calculate its fitness"""
        target_total = self.get_sum()
        for chromosome in self.chromosomes:
            chromosome.fit(target_total)

    def get_generation(self):
        return self.generation

    def get_targets(self):
        return [chromosome.get_target() for chromosome in self.chromosomes]

    def get_maximum(self):
        return max(self.get_targets())

    def get_minimum(self):
        return min(self.get_targets())

    def get_sum(self):
        return sum(self.get_targets())

    def get_average(self):
        return self.get_sum() / self.amount

    def get_range(self):
        return self.get_maximum() - self.get_minimum()

    def evolve(self):
        self._choose_fathers()

        self._cross_over()

        self._mutate()

        if Settings.get_elitism():
            childs = self.get_fittest_chromosomes()
            self.childs.extend(childs)

    def _choose_fathers(self):
        """Return a list with the fathers, the fathers are chosen acording to
            their fitness value, it will choose as many fathers as the size
            of the population and if elitism, as many as the size minus 2"""
        self.fathers = []
        number = self.amount

        if Settings.get_elitism():
            number -= 2

        probabilities = self.get_fitness()

        for _ in range(number):
            chromosome = util.choose_roulette(self.chromosomes, probabilities)
            self.fathers.append(chromosome)

    def get_fitness(self):
        """Return a list with the fitness of each chromosome"""
        fitness = []
        for chromosome in self.chromosomes:
            chromosome_fitness = chromosome.get_fitness()
            fitness.append(chromosome_fitness)
        return fitness

    def _cross_over(self):
        """Given a list of fathers, when appropiate, cross over them two by two
            and add the resulting childs chromosomes"""
        couples = util.get_next_two(self.fathers)

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
        length = len(father1.genes)
        split_points = util.get_random_number(0, length)
        father1_gene_parts = self.split_chromosome(father1, split_points)
        father2_gene_parts = self.split_chromosome(father2, split_points)

        child1_gene_string = "".join(
            (father2_gene_parts[0], father1_gene_parts[1]))
        child2_gene_string = "".join(
            (father1_gene_parts[0], father2_gene_parts[1]))

        child1 = Chromosome(genes=child1_gene_string)
        child2 = Chromosome(genes=child2_gene_string)

        return child1, child2

    def split_chromosome(self, chromosome, split_point):
        """Given a chromosome and a split_point, return the gene string of the
            chromosome split at the split_point"""
        gene_string = chromosome.genes
        return [gene_string[:split_point], gene_string[split_point:]]

    def get_fittest_chromosomes(self):
        """Return the two chromosome with the highest fitness value"""
        fitness = self.get_fitness()
        fitness_sorted_list = sorted(fitness, reverse=True)
        max_fitness = fitness_sorted_list[:2]

        chromosomes = []
        for maximum in max_fitness:
            gene_string = self.find_gene_string_by_fitness(maximum)
            chromosome = Chromosome(genes=gene_string)
            chromosomes.append(chromosome)
        return chromosomes

    def find_gene_string_by_fitness(self, fitness):
        """Return the chromosome gene string with the given fitness"""
        for chromosome in self.chromosomes:
            if chromosome.get_fitness() == fitness:
                return chromosome.genes

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
        return Population(chromosomes=self.childs, generation=self.generation + 1)

    def get_max_gene_string(self):
        """Return the gene string corresponding to the fittest chromosome"""
        maximum_fitness = max(self.get_fitness())
        return self.find_gene_string_by_fitness(maximum_fitness)


if __name__ != "__main__":
    from exercise1.logic.settings_manager import Settings
    from exercise1.entities.chromosome import Chromosome
    import exercise1.util.util as util
