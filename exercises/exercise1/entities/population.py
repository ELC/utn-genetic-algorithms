"""Population Class"""

class Population():
    """Population Class."""
    def __init__(self, chromosomes=None):
        self.amount = Settings.get_population_size()
        if chromosomes is None:
            chromosomes = [Chromosome() for i in range(self.amount)]
        self.chromosomes = chromosomes
        self.childs = []
        self.fathers = []
        self.generation = "Final"

    def set_generation(self, value):
        """Set the generation it corresponds"""
        self.generation = value

    def get_maximum(self):
        targets = self.get_targets()
        return max(targets)

    def get_minimum(self):
        targets = self.get_targets()
        return min(targets)

    def get_sum(self):
        targets = self.get_targets()
        return sum(targets)

    def get_average(self):
        suma = self.get_sum()
        return suma / self.amount

    def get_range(self):
        maximum = self.get_maximum()
        minimum = self.get_minimum()
        return maximum - minimum

    def evolve(self):
        """Prepare the next generation."""
        self._fit_population()

        self._choose_fathers()

        self._cross_over()

        elitism = Settings.get_elitism()
        if elitism:
            fittest_chromosome = self.get_fittest_chromosome()
            self.childs[0] = fittest_chromosome

        self._mutate()

    def _fit_population(self):
        target_total = self.get_sum()
        for chromosome in self.chromosomes:
            chromosome.fit(target_total)

    def _choose_fathers(self):
        number = self.amount
        probabilities = self.get_fitness()
        for _ in range(number):
            chromosome = util.choose_n_elements_from_narray(self.chromosomes, probabilities)
            self.fathers.append(chromosome)

    def get_fitness(self):
        """Return a list with the fitness of each chromosome"""
        fitness = []
        for chromosome in self.chromosomes:
            chromosome_fitness = chromosome.get_fitness()
            fitness.append(chromosome_fitness)
        return fitness

    def _cross_over(self):
        couples = util.get_next_two(self.fathers)
        cross_over_prob = Settings.cross_over_prob
        precision = util.get_precision(cross_over_prob)
        for (father1, father2) in couples:
            prob = util.get_random_prob(precision=precision)
            if prob < cross_over_prob:
                child1, child2 = self._cross_over_1_point(father1, father2)
            else:
                child1, child2 = father1, father2
            self.childs.append(child1)
            self.childs.append(child2)

    def _cross_over_1_point(self, father1, father2):
        length = father1.get_size()
        split_points = util.get_random_number(0, length)
        father1_gene_parts = self.split_chromosome(father1, split_points)
        father2_gene_parts = self.split_chromosome(father2, split_points)
        child1, child2 = self._mix(father1_gene_parts, father2_gene_parts)
        return child1, child2

    def split_chromosome(self, chromosome, split_point):
        """Return the gene string of a chromosome split at the split_point"""
        gene_string = chromosome.get_gene_string()
        return [gene_string[:split_point], gene_string[split_point:]]

    def _mix(self, father1, father2):
        child1_gene_string = "".join((father2[0], father1[1]))
        child2_gene_string = "".join((father1[0], father2[1]))
        child1 = Chromosome(genes=child1_gene_string)
        child2 = Chromosome(genes=child2_gene_string)
        return child1, child2

    def get_fittest_chromosome(self):
        """Return one chromosome with the highest fitness value"""
        max_fitness = self.get_max_fitness()
        for chromosome in self.chromosomes:
            if chromosome.get_fitness() == max_fitness:
                return chromosome

    def get_max_fitness(self):
        """Return the maximum value of fitness"""
        fitness = self.get_fitness()
        return max(fitness)

    def _mutate(self):
        mutation_prob = Settings.get_mutation_prob()
        precision = util.get_precision(mutation_prob)
        for chromosome in self.childs:
            prob = util.get_random_prob(precision=precision)
            if prob < mutation_prob:
                chromosome.mutate()

    def get_next_generation(self):
        """Replace the old generation with the new one."""
        next_generation = Population(chromosomes=self.childs)
        return next_generation

    def get_targets(self):
        """Return the target value of each chromosome."""
        targets = []
        for chromosome in self.chromosomes:
            chromosome_target = chromosome.get_target()
            targets.append(chromosome_target)
        return targets


if __name__ != "__main__":
    from exercise1.logic.settings_manager import Settings
    from exercise1.entities.chromosome import Chromosome
    import exercise1.util.util as util
