"""Logic layer of Population"""


class PopulationController():

    results = []

    @classmethod
    def store_results(cls):
        FileManager.store_results(cls.results)

    @classmethod
    def add_population(cls, result):
        cls.results = cls.load_populations()
        cls.results.append(result)
        cls.store_results()

    @staticmethod
    def load_populations():
        return FileManager.load_results()

    @classmethod
    def reset_populations(cls):
        cls.results = []
        cls.store_results()

    @classmethod
    def get_maximums(cls):
        return [i.get_maximum() for i in cls.load_populations()]

    @classmethod
    def get_minimums(cls):
        return [i.get_minimum() for i in cls.load_populations()]

    @classmethod
    def get_averages(cls):
        return [i.get_average() for i in cls.load_populations()]

    @classmethod
    def get_targets(cls, population):
        return population.get_targets()

    @classmethod
    def get_ranges(cls):
        """Return a list with the difference between the maximum and the minimum
            of each population"""
        return [i.get_range() for i in cls.load_populations()]

    @classmethod
    def get_totals(cls):
        return [i.get_sum() for i in cls.load_populations()]

    @classmethod
    def get_last_population(cls):
        return cls.load_populations()[-1]


if __name__ != '__main__':
    from exercise1.data.filemanager import FileManager
    from exercise1.entities.population import Population
