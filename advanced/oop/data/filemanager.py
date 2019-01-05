"""File Manager - Data Layer"""
import pickle
import json


class FileManager():
    @staticmethod
    def load_settings():
        """Load Configuration File from binary."""
        with open('oop/data/config.json', 'rb') as handle:
            settings = json.loads(handle.read())
        return settings

    @staticmethod
    def store_results(results):
        with open('oop/data/results', 'wb') as handle:
            pickle.dump(results, handle)

    @staticmethod
    def load_results():
        with open('oop/data/results', 'rb') as handle:
            results = pickle.loads(handle.read())
        return results

    @classmethod
    def get_generations(cls):
        return cls.load_settings()["generations"]

    @classmethod
    def get_cross_over_prob(cls):
        return cls.load_settings()["cross_over_prob"]

    @classmethod
    def get_mutation_prob(cls):
        return cls.load_settings()['mutation_prob']

    @classmethod
    def get_population_size(cls):
        return cls.load_settings()['population_size']

    @classmethod
    def get_chromosome_bits(cls):
        return cls.load_settings()['chromosome_bits']

    @classmethod
    def get_elitism(cls):
        return cls.load_settings()['elitism']

    @classmethod
    def get_settings_id(cls):
        settings = cls.load_settings()
        return hash(tuple(sorted(settings.values())))
