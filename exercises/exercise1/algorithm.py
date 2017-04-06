"""Algorithm Class"""
from population import Population
from settings import Settings
from util import Util

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

if __name__ == '__main__':
    CONST = Algorithm()
    CONST.evolve()
