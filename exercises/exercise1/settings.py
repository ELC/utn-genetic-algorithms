"""Settings Class"""


class Settings():
    """Settings for the algorithm."""
    generations = None
    cross_over_prob = None
    mutation_prob = None
    population_size = None
    individual_bits = None
    report = None

    @classmethod
    def get_generations(cls):
        cls.load_settings()
        return cls.generations

    @classmethod
    def get_cross_over_prob(cls):
        cls.load_settings()
        return cls.cross_over_prob

    @classmethod
    def get_mutation_prob(cls):
        cls.load_settings()
        return cls.mutation_prob

    @classmethod
    def get_population_size(cls):
        cls.load_settings()
        return cls.population_size

    @classmethod
    def get_individual_bits(cls):
        cls.load_settings()
        return cls.individual_bits

    @classmethod
    def get_report(cls):
        cls.load_settings()
        return cls.report

    @classmethod
    def set_generations(cls, value):
        cls.load_settings()
        cls.generations = value
        cls.set_settings()

    @classmethod
    def set_cross_over_prob(cls, value):
        cls.load_settings()
        cls.cross_over_prob = value
        cls.set_settings()

    @classmethod
    def set_mutation_prob(cls, value):
        cls.load_settings()
        cls.mutation_prob = value
        cls.set_settings()

    @classmethod
    def set_population_size(cls, value):
        cls.load_settings()
        cls.population_size = value
        cls.set_settings()

    @classmethod
    def set_individual_bits(cls, value):
        cls.load_settings()
        cls.individual_bits = value
        cls.set_settings()

    @classmethod
    def set_report(cls, value):
        cls.load_settings()
        cls.report = value
        cls.set_settings()

    @classmethod
    def load_settings(cls):
        """Load Configuration File."""
        settings = cls.load_all_settings()
        cls.generations = settings["generations"]
        cls.cross_over_prob = settings["cross_over_prob"]
        cls.mutation_prob = settings["mutation_prob"]
        cls.population_size = settings["population_size"]
        cls.individual_bits = settings["individual_bits"]
        cls.report = settings["report"]

    @classmethod
    def load_all_settings(cls):
        """Load Configuration File."""
        settings = Manager.load_settings()
        return settings

    @classmethod
    def set_settings(cls):
        """Write Configuration File."""
        settings = {
            "generations":cls.generations,
            "cross_over_prob":cls.cross_over_prob,
            "mutation_prob":cls.mutation_prob,
            "population_size":cls.population_size,
            "individual_bits":cls.individual_bits,
            "report":cls.report
        }
        Manager.set_settings(settings)

    @staticmethod
    def target(number):
        """Define a Target function."""
        return number ** 2

    @classmethod
    def header(cls):
        """Show basic Configurations."""
        settings = cls.load_all_settings()
        population_size = settings["population_size"]
        cross_over_prob = settings["cross_over_prob"]
        mutation_prob = settings["mutation_prob"]
        generations = settings["generations"]
        report = settings["report"]
        print("##########################################")
        print("Población inicial: {}".format(population_size))
        print("Probabilidad de CrossOver: {}".format(cross_over_prob))
        print("Probabilidad de mutacion: {}".format(mutation_prob))
        print("Numero de generaciones maximas: {}".format(generations))
        print("Mostrar reporte: {}".format(report))
        print("##########################################")
        print()

if __name__ == "__main__":
    from algorithm import Algorithm
    from configmanager import Manager
    CONST = Algorithm()
    CONST.evolve()
else:
    from algorithm import Algorithm
    from configmanager import Manager
