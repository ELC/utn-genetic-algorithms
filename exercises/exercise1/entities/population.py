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
        self.targets = self._get_target()
        self.suma = self._calc_sum()
        self.maximum = self._calc_maximum()
        self.minimum = self._calc_minimum()
        self.average = self._calc_average()
        self.least = self._calc_least()
        self.range = self._calc_range()
        self.generation = "Final"

    def set_generation(self, value):
        """Set the generation it corresponds"""
        self.generation = value

    def __generate_individuals(self, size):
        return [Individual() for i in range(size)]

    def _calc_maximum(self):
        return max(self.targets)

    def _calc_minimum(self):
        return min(self.targets)

    def _calc_sum(self):
        return sum(self.targets)

    def _calc_average(self):
        return self.suma / self.amount

    def _calc_least(self):
        distance = 0
        for target in self.targets:
            distance_unrounded = (self.maximum - target) ** 2
            distance += int(distance_unrounded)
        return distance

    def _calc_range(self):
        return self.maximum - self.minimum

    def evolve(self):
        """Prepare the next generation."""
        self._fitness()

        self._choose_fathers()

        self._cross_over()

        self._mutate()

    def _mutate(self):
        mutation_prob = Settings.get_mutation_prob()
        for individual in self.childs:
            prob = util.get_random_prob(precision=5)
            if prob < mutation_prob:
                individual.mutate()

    def survive(self):
        """Replace the old generation with the new one."""
        next_generation = Population(individuals=self.childs)
        return next_generation

    def _fitness(self):
        target_total = self.suma
        for individual in self.individuals:
            individual.fit(target_total)

    def _choose_fathers(self):
        fitness_acumulated_values = self._acumulated_fitness()
        for _ in range(self.amount):
            prob = util.get_random_prob()
            index = util.find_bigger(fitness_acumulated_values, prob)
            individual = self.individuals[index]
            self.fathers.append(individual)

    def _acumulated_fitness(self):
        acum = []
        fitness_acum = 0
        for individual in self.individuals:
            fitness_acum += individual.get_fitness()
            acum.append(fitness_acum)

        if acum[-1] != 1:
            acum[-1] = 1

        return acum

    def _cross_over(self):
        couples = self._make_couples(self.fathers)
        cross_over_prob = Settings.cross_over_prob
        for (father1, father2) in couples:
            prob = util.get_random_prob()
            if prob < cross_over_prob:
                child1, child2 = self._cross_over_n_points(father1, father2)
            else:
                child1, child2 = father1, father2

            self.childs.append(child1)
            self.childs.append(child2)

    def _make_couples(self, fathers):
        amount = self.amount // 2
        couples = []
        for i in range(amount):
            couple = [fathers[i*2], fathers[i*2+1]]
            couples.append(couple)
        return couples

    def _cross_over_n_points(self, father1, father2, points=1):
        length = father1.get_size()
        split_points = self._get_split_points(points, length)
        father1_gene_parts = self._split_in_parts(father1, split_points)
        father2_gene_parts = self._split_in_parts(father2, split_points)
        child1, child2 = self._mix(father1_gene_parts, father2_gene_parts)
        return child1, child2

    def _get_split_points(self, points, length):
        split_points = []
        for _ in range(points):
            split_point = util.get_random_number(0, length)
            split_points.append(split_point)
        return split_points

    def _split_in_parts(self, father, split_points):
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

    def _mix(self, father1, father2):
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

    def get_total_target(self):
        """Return the total target value of all individuals."""
        target = self._get_target()
        return sum(target)

    def _get_target(self):
        """Return the target value of each individual."""
        targets = []
        for individual in self.individuals:
            individual_target = individual.target
            targets.append(individual_target)
        return targets

    def get_genes(self):
        """Return the genes string of each individual."""
        genes = []
        for individual in self.individuals:
            gene = individual.get_gene()
            genes.append(gene)
        return genes

if __name__ != "__main__":
    from exercise1.logic.settings import Settings
    from exercise1.entities.individual import Individual
    from exercise1.logic.target import target as target_function
    import exercise1.util.util as util
