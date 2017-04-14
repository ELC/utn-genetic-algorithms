"""File Manager - Data Layer"""
import pickle
import json

def load_settings():
    """Load Configuration File from binary."""
    with open('config', 'rb') as handle:
        settings = pickle.loads(handle.read())
    return settings

def set_settings(settings):
    """Manages the writers of files"""
    _set_settings_pickle(settings)
    _set_settings_json(settings)

def _set_settings_pickle(settings):
    """Write Configuration File in binary format."""
    with open('config', 'wb') as handle:
        pickle.dump(settings, handle)

def _set_settings_json(settings):
    """Write Configuration File in Json format."""
    with open("config.json", "w") as handle:
        json.dump(settings, handle)

#Results Section
def store_results(results):
    """Write Results File."""
    with open('results', 'wb') as handle:
        pickle.dump(results, handle)

def load_results():
    """Load Results File."""
    with open('results', 'rb') as handle:
        results = pickle.loads(handle.read())
    return results
