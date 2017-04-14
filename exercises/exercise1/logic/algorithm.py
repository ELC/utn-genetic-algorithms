"""Algorithm Class"""

class Algorithm():
    """Main Class"""
    def __init__(self):
        self.populations = []
        self.actual_generation = Population()
        self.populations.append(self.actual_generation)
        self.__evolve()

    def __evolve(self):
        """Start the process of evolution."""
        generations = Settings.get_generations()
        for i in range(generations):
            self.actual_generation.set_generation(i)
            self.actual_generation.evolve()
            self.actual_generation = self.actual_generation.survive()
            self.populations.append(self.actual_generation)
            convergence = self.actual_generation.range
            if convergence == 0:
                break
        self.__store_results()

    def __store_results(self):
        Settings.store_results(self.populations)

if __name__ != '__main__':
    from exercise1.entities.population import Population
    from exercise1.logic.settings import Settings
