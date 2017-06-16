"""File Manager - Data Layer"""
import pickle
import json

def load_settings(module):
    """Load Configuration File from binary."""
    with open(module +'/data/config', 'rb') as handle:
        settings = pickle.loads(handle.read())
    return settings

def set_settings(module, settings):
    """Manages the writers of files"""
    _set_settings_pickle(module, settings)
    _set_settings_json(module, settings)

def _set_settings_pickle(module, settings):
    """Write Configuration File in binary format."""
    with open(module + '/data/config', 'wb') as handle:
        pickle.dump(settings, handle)

def _set_settings_json(module, settings):
    """Write Configuration File in Json format."""
    with open(module + '/data/config.json', 'w') as handle:
        json.dump(settings, handle)

#Results Section
def store_results(module, results):
    """Write Results File."""
    with open(module + '/data/results', 'wb') as handle:
        pickle.dump(results, handle)

def load_results(module):
    """Load Results File."""
    with open(module + '/data/results', 'rb') as handle:
        results = pickle.loads(handle.read())
    return results
