"""File Manager - Data Layer"""
import pickle
import json


class FileManager():
    @staticmethod
    def load_settings():
        """Load Configuration File from binary."""
        with open('exercise1/data/config.json', 'rb') as handle:
            settings = json.loads(handle.read())
        return settings

    @staticmethod
    def store_results(results):
        with open('exercise1/data/results', 'wb') as handle:
            pickle.dump(results, handle)

    @staticmethod
    def load_results():
        with open('exercise1/data/results', 'rb') as handle:
            results = pickle.loads(handle.read())
        return results
