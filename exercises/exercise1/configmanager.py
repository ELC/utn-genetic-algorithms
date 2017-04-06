import pickle
import json

class Manager():

    @staticmethod
    def load_settings():
        """Load Configuration File."""
        with open('config', 'rb') as handle:
            settings = pickle.loads(handle.read())
        return settings

    @classmethod
    def set_settings(cls, settings):
        cls.set_settings_pickle(settings)
        cls.set_settings_json(settings)

    @classmethod
    def set_settings_pickle(cls, settings):
        """Write Configuration File."""
        with open('config', 'wb') as handle:
            pickle.dump(settings, handle)

    @classmethod
    def set_settings_json(cls, settings):
        with open("config.json", "wb") as handle:
            json.dump(settings, handle)

    @classmethod
    def store_results(cls, results):
        """Write Configuration File."""
        with open('results', 'wb') as handle:
            pickle.dump(results, handle)

    @classmethod
    def load_results(cls):
        """Write Configuration File."""
        with open('results', 'rb') as handle:
            results = pickle.loads(handle.read())
        return results
