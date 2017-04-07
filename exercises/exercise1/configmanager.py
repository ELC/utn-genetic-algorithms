"""File Manager - Data Layer"""
import pickle
import json

class Manager():
    """File Manager"""

    #Configuration Section
    @staticmethod
    def load_settings():
        """Load Configuration File from binary."""
        with open('config', 'rb') as handle:
            settings = pickle.loads(handle.read())
        return settings

    @classmethod
    def set_settings(cls, settings):
        """Manages the writers of files"""
        cls.set_settings_pickle(settings)
        cls.set_settings_json(settings)

    @classmethod
    def set_settings_pickle(cls, settings):
        """Write Configuration File in binary format."""
        with open('config', 'wb') as handle:
            pickle.dump(settings, handle)

    @classmethod
    def set_settings_json(cls, settings):
        """Write Configuration File in Json format."""
        with open("config.json", "w") as handle:
            json.dump(settings, handle)


    #Results Section
    @classmethod
    def store_results(cls, results):
        """Write Results File."""
        with open('results', 'wb') as handle:
            pickle.dump(results, handle)

    @classmethod
    def load_results(cls):
        """Load Results File."""
        with open('results', 'rb') as handle:
            results = pickle.loads(handle.read())
        return results
