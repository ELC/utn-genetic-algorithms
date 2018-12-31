"""Settings Manager, sets, gets and resets the configuration"""

from exercise1.data.filemanager import FileManager


class Settings():
    """Settings for the algorithm."""
    generations = None
    cross_over_prob = None
    mutation_prob = None
    population_size = None
    chromosome_bits = None
    elitism = None
    filemanager = FileManager()

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
        return cls.filemanager.load_settings()

    @classmethod
    def get_settings_id(cls):
        settings = cls.filemanager.load_settings()
        return hash(tuple(sorted(settings.values())))
