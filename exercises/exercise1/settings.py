"""Settings Class"""

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
