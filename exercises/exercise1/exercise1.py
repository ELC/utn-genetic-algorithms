"""First exercise of Genetic Algorithms"""
from numpy.random import randint
import matplotlib.pyplot as plt


class Util():
    """Utilities Class, support methods."""
    @staticmethod
    def get_random_prob(precision=2):
        """Return a random probability (between 0 and 1) with given precision."""
        toplimit = 10 ** precision
        percentage = randint(0, toplimit)
        prob = percentage / toplimit
        return prob

    @staticmethod
    def dec_bin(number):
        """ Convert X from Decimal to Binary."""
        return bin(number)[2:]

    @staticmethod
    def find_bigger(array, value):
        """Given a value and a sorted array, find the closest bigger element."""
        for i, j in enumerate(array):
            if value <= j:
                return i

    @staticmethod
    def graphics(datas, labels):
        """Plot several graph with its labels."""
        plt.figure(figsize=(17, 9))
        ax1 = plt.subplot2grid((1, 1), (0, 0))
        ax1.grid(True)

        plt.xlabel('Generaciones')
        plt.title('Algoritmo Genético')

        for data, label in zip(datas, labels):
            x_data = [i for i, _ in enumerate(data)]
            ax1.set_xticks(x_data[::2])
            y_data = data
            maximum = max(data)
            sticks = (i for i in range(0, maximum+1, 2))
            unique_sticks = set(sticks)
            yticsk = sorted(unique_sticks)
            ax1.set_yticks(yticsk)
            ax1.plot(x_data, y_data, label=label)
        plt.legend()
        plt.show()

class Algorithm():
    """Main Class"""
    def __init__(self):
        self.population = Population()
        self.averages = []
        self.average = None
        self.maximum = None
        self.minimum = None
        self.least = None
        self.range = None
        self.maximums = []
        self.minimums = []
        self.ranges = []
        self.leasts = []
        self.genes_values = []
        Settings.header()


    def __report(self, generation):
        print("Generacion {}:".format(generation))
        print("Promedio: {}".format(self.average))
        print("Maximo {}".format(self.maximum))
        print("Minimo {}".format(self.minimum))
        print("Distancia Cuadrada {}".format(self.least))
        print("Recorrido {}".format(self.range))
        print("")

    def __calc_aux(self):
        self.genes_values = self.population.get_genes()
        self.__calc_averages()
        self.__calc_maximum()
        self.__calc_minimum()
        self.__calc_range()
        self.__calc_least_squares()


    def __calc_averages(self):
        average = sum(self.genes_values) / len(self.genes_values)
        average_rounded = int(average + 0.5)
        self.average = average_rounded
        self.averages.append(average_rounded)

    def __calc_maximum(self):
        maximum = max(self.genes_values)
        self.maximum = maximum
        self.maximums.append(maximum)

    def __calc_minimum(self):
        minimum = min(self.genes_values)
        self.minimum = minimum
        self.minimums.append(minimum)

    def __calc_range(self):
        range_ = self.maximum - self.minimum
        self.range = range_
        self.ranges.append(range_)

    def __calc_least_squares(self):
        distance = 0
        for gene in self.genes_values:
            distance += (self.average - gene) ** 2
        self.least = distance
        self.leasts.append(distance)


    def evolve(self):
        """Start the process of evolution."""
        generations = Settings.generations
        for i in range(generations):
            self.population.evolve()
            self.__calc_aux()
            self.__report(i)
            self.population.survive()
            if self.maximum == self.average == self.minimum:
                break
        Util.graphics(
            [self.maximums, self.minimums, self.averages],
            ["Maximos", "Minimos", "Promedios"])

    @staticmethod
    def target(number):
        """Define a Target function."""
        return number ** 2


class Population():
    """Population Class."""
    def __init__(self):
        population_size = Settings.population_size
        self.individuals = [Individual() for i in range(population_size)]
        self.amount = population_size
        self.childs = None

    def evolve(self):
        """Prepare the next generation."""
        self.childs = []

        self.__fitness()

        fathers = self.__choose_fathers()
        couples = self.__make_couples(fathers)
        self.__cross_over(couples)
        self.__mutate()

    def __mutate(self):
        mutation_prob = Settings.mutation_prob
        for individual in self.childs:
            prob = Util.get_random_prob(precision=5)
            if prob < mutation_prob:
                individual.mutate()

    def survive(self):
        """Replace the old generation with the new one."""
        self.individuals = self.childs

    def __fitness(self):
        target_total = self.get_total_target()
        for individual in self.individuals:
            individual.fit(Algorithm.target, target_total)

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
        fathers = []
        fitness_acumulated_values = self.__acumulated_fitness()
        for _ in range(self.amount):
            prob = Util.get_random_prob()
            index = Util.find_bigger(fitness_acumulated_values, prob)
            individual = self.individuals[index]
            fathers.append(individual)
        return fathers

    def __make_couples(self, fathers):
        amount = self.amount // 2
        couples = []
        for i in range(amount):
            couple = [fathers[i*2], fathers[i*2+1]]
            couples.append(couple)
        return couples

    def __cross_over(self, couples):
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
            split_point = randint(0, length)
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
            individual_target = Algorithm.target(individual_gene)
            target.append(individual_target)
        return target

    def get_genes(self):
        """Return the genes string of each individual."""
        genes = []
        for individual in self.individuals:
            gene = individual.get_gene()
            genes.append(gene)
        return genes


class Individual():
    """Individual class"""
    def __init__(self, genes=None):
        if genes is None:
            bits = Settings.individual_bits
            genes = self.__generate_gene_string(bits)
        self.genes = genes
        self.amount_genes = len(self.genes)
        self.target = None
        self.fitness = None

    def __generate_gene_string(self, length):
        maximum = 2 ** length - 1
        dec_gene = randint(0, maximum)
        bin_gene = Util.dec_bin(dec_gene)
        gene = self.__fill(bin_gene, length)
        return gene

    def __fill(self, raw, lenght, neutral="0"):
        raw_gene = list(raw)
        while len(raw_gene) < lenght:
            raw_gene.insert(0, neutral)
        filled_gene = "".join(raw_gene)
        return filled_gene

    def mutate(self, inverse=True, func=None):
        """Mutate the genes string"""
        gene = self.__pick_random_gene()
        if inverse:
            if gene == "1":
                gene = "0"
            else:
                gene = "1"
        else:
            gene = func(gene)

    def __pick_random_gene(self):
        index = randint(0, self.amount_genes -1)
        return self.genes[index]

    def fit(self, target, total):
        """Calc the fitness value of this individual."""
        usable_gene = self.get_gene()
        self.target = target(usable_gene)
        self.fitness = self.target / total

    def get_gene(self):
        """Return the genes in decimal format."""
        return int(self.genes, 2)

    def get_gene_string(self):
        """Return the genes string."""
        return self.genes

    def get_target(self):
        """Return the target value of this individual."""
        return self.target

    def get_fitness(self):
        """Return the fitness value of this individual."""
        return self.fitness

    def get_size(self):
        """Return the amout of genes of this individual."""
        return self.amount_genes

class Settings():
    """Settings for the algorithm."""
    population_size = 20
    cross_over_prob = 0.1
    mutation_prob = 0.001
    generations = 1000
    individual_bits = 5

    @classmethod
    def header(cls):
        """Show basic Configurations."""
        population_size = cls.population_size
        cross_over_prob = cls.cross_over_prob
        mutation_prob = cls.mutation_prob
        generations = cls.generations
        print("##########################################")
        print("Población inicial: {}".format(population_size))
        print("Probabilidad de CrossOver: {}".format(cross_over_prob))
        print("Probabilidad de mutacion: {}".format(mutation_prob))
        print("Numero de generaciones maximas: {}".format(generations))
        print("##########################################")
        print()


MAIN = Algorithm()
MAIN.evolve()
