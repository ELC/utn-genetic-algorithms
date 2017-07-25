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
    def get_generations(cls, module):
        cls.load_settings(module)
        return cls.generations

    @classmethod
    def get_cross_over_prob(cls, module):
        cls.load_settings(module)
        return cls.cross_over_prob

    @classmethod
    def get_mutation_prob(cls, module):
        cls.load_settings(module)
        return cls.mutation_prob

    @classmethod
    def get_population_size(cls, module):
        cls.load_settings(module)
        return cls.population_size

    @classmethod
    def get_chromosome_bits(cls, module):
        cls.load_settings(module)
        return cls.chromosome_bits

    @classmethod
    def get_elitism(cls, module):
        cls.load_settings(module)
        return cls.elitism

    @classmethod
    def set_generations(cls, module, value):
        cls.load_settings(module)
        cls.generations = value
        cls.__set_settings(module)

    @classmethod
    def set_cross_over_prob(cls, module, value):
        cls.load_settings(module)
        cls.cross_over_prob = value
        cls.__set_settings(module)

    @classmethod
    def set_mutation_prob(cls, module, value):
        cls.load_settings(module)
        cls.mutation_prob = value
        cls.__set_settings(module)

    @classmethod
    def set_population_size(cls, module, value):
        cls.load_settings(module)
        cls.population_size = value
        cls.__set_settings(module)

    @classmethod
    def set_chromosome_bits(cls, module, value):
        cls.load_settings(module)
        cls.chromosome_bits = value
        cls.__set_settings(module)

    @classmethod
    def set_elitism(cls, module, value):
        cls.load_settings(module)
        cls.elitism = value
        cls.__set_settings(module)

    @classmethod
    def load_settings(cls, module):
        """Load Configuration File."""
        settings = cls.load_all_settings(module)
        cls.generations = settings["generations"]
        cls.cross_over_prob = settings["cross_over_prob"]
        cls.mutation_prob = settings["mutation_prob"]
        cls.population_size = settings["population_size"]
        cls.chromosome_bits = settings["chromosome_bits"]
        cls.elitism = settings["elitism"]

    @classmethod
    def load_all_settings(cls, module):
        """Load Configuration File."""
        settings = filemanager.load_settings(module)
        return settings

    @classmethod
    def __set_settings(cls, module):
        """Write Configuration File."""
        settings = {
            "generations":cls.generations,
            "cross_over_prob":cls.cross_over_prob,
            "mutation_prob":cls.mutation_prob,
            "population_size":cls.population_size,
            "chromosome_bits":cls.chromosome_bits,
            "elitism":cls.elitism
        }
        filemanager.set_settings(module, settings)

    @classmethod
    def reset_configuration(cls, module):
        """Write Configuration File."""
        settings = {
            "generations":10,
            "cross_over_prob":0.9,
            "mutation_prob":0.001,
            "population_size":20,
            "chromosome_bits":5,
            "elitism":False
        }
        filemanager.set_settings(module, settings)
    
    @classmethod
    def get_settings_id(cls, module):
        settings = filemanager.load_settings(module)
        return hashlib.sha1(str(sorted(settings.values())).encode('utf-8')).hexdigest()

if __name__ != "__main__":
    import hashlib
    import base.data.filemanager as filemanager
