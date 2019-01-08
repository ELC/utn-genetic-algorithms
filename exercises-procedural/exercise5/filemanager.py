"""File Manager - Data Layer"""
import pickle
import json


def load_settings():
    """Load Configuration File from binary."""
    with open('exercise5/config.json', 'rb') as handle:
        settings = json.loads(handle.read())
    return settings


def add_to_results(add):
    results = load_results()
    results.append(add)
    store_results(results)


def store_results(results):
    with open('exercise5/results/results', 'wb') as handle:
        pickle.dump(results, handle)

def reset_results():
    with open('exercise5/results/results', 'wb') as handle:
        pickle.dump([], handle)

def load_results():
    with open('exercise5/results/results', 'rb') as handle:
        results = pickle.loads(handle.read())
    return results


def get_settings_id():
    settings = load_settings()
    settings = [str(i) for i in settings]
    return hash(tuple(settings))
