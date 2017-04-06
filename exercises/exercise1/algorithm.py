"""Algorithm Class"""


class Algorithm():
    """Main Class"""
    def __init__(self):
        self.populations = []
        self.actual_generation = Population()
        self.populations.append(self.actual_generation)
        self.maximums = []
        self.minimums = []
        self.averages = []
        self.ranges = []
        self.leasts = []
        Settings.header()


    def __report(self):
        for i, pop in enumerate(self.populations):
            print("Generacion {}:".format(i))
            print("Promedio: {}".format(pop.average))
            print("Maximo {}".format(pop.maximum))
            print("Minimo {}".format(pop.minimum))
            print("Distancia Cuadrada {}".format(pop.least))
            print("Recorrido {}".format(pop.range))
            print("")

    def evolve(self):
        """Start the process of evolution."""
        generations = Settings.get_generations()
        for _ in range(generations):
            self.actual_generation.evolve()
            self.actual_generation = self.actual_generation.survive()
            self.populations.append(self.actual_generation)
            variety = self.actual_generation.range
            if variety == 0:
                break
        Manager.store_results(self.populations)

if __name__ != '__main__':
    from population import Population
    from settings import Settings
    from util import Util
    from configmanager import Manager
