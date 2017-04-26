"""Settings Manager, sets, gets and resets the configuration"""

class Settings():
    """Settings for the algorithm."""
    generations = None
    cross_over_prob = None
    mutation_prob = None
    population_size = None
    chromosome_bits = None
    elitism = None

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
    def get_chromosome_bits(cls):
        cls.load_settings()
        return cls.chromosome_bits

    @classmethod
    def get_elitism(cls):
        cls.load_settings()
        return cls.elitism

    @classmethod
    def set_generations(cls, value):
        cls.load_settings()
        cls.generations = value
        cls.__set_settings()

    @classmethod
    def set_cross_over_prob(cls, value):
        cls.load_settings()
        cls.cross_over_prob = value
        cls.__set_settings()

    @classmethod
    def set_mutation_prob(cls, value):
        cls.load_settings()
        cls.mutation_prob = value
        cls.__set_settings()

    @classmethod
    def set_population_size(cls, value):
        cls.load_settings()
        cls.population_size = value
        cls.__set_settings()

    @classmethod
    def set_chromosome_bits(cls, value):
        cls.load_settings()
        cls.chromosome_bits = value
        cls.__set_settings()

    @classmethod
    def set_elitism(cls, value):
        cls.load_settings()
        cls.elitism = value
        cls.__set_settings()

    @classmethod
    def load_settings(cls):
        """Load Configuration File."""
        settings = cls.load_all_settings()
        cls.generations = settings["generations"]
        cls.cross_over_prob = settings["cross_over_prob"]
        cls.mutation_prob = settings["mutation_prob"]
        cls.population_size = settings["population_size"]
        cls.chromosome_bits = settings["chromosome_bits"]
        cls.elitism = settings["elitism"]

    @classmethod
    def load_all_settings(cls):
        """Load Configuration File."""
        settings = filemanager.load_settings()
        return settings

    @classmethod
    def __set_settings(cls):
        """Write Configuration File."""
        settings = {
            "generations":cls.generations,
            "cross_over_prob":cls.cross_over_prob,
            "mutation_prob":cls.mutation_prob,
            "population_size":cls.population_size,
            "chromosome_bits":cls.chromosome_bits,
            "elitism":cls.elitism
        }
        filemanager.set_settings(settings)

    @classmethod
    def reset_configuration(cls):
        """Write Configuration File."""
        settings = {
            "generations":10,
            "cross_over_prob":0.9,
            "mutation_prob":0.001,
            "population_size":20,
            "chromosome_bits":5,
            "elitism":False
        }
        filemanager.set_settings(settings)

if __name__ != "__main__":
    import exercise1.data.filemanager as filemanager
