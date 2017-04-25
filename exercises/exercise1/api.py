"""API"""

from exercise1.logic.settings_manager import Settings
from exercise1.logic.algorithm import Algorithm

def execute():
    """Execute the main algorithm"""
    Algorithm()

def export_results():
    """Get the results for the previous run"""
    results = Settings.load_results()
    return results

def export_settings():
    """Get the Settings"""
    settings = Settings.load_all_settings()
    return settings

def set_cross_over_prob(value):
    """Set the cross over probability"""
    Settings.set_cross_over_prob(value)

def set_individual_bits(value):
    """Set the individual bits probability"""
    Settings.set_individual_bits(value)

def set_generations(value):
    """Set the generations probability"""
    Settings.set_generations(value)

def set_mutation_prob(value):
    """Set the mutation probability"""
    Settings.set_mutation_prob(value)

def set_population_size(value):
    """Set the initial population size"""
    Settings.set_population_size(value)

def set_report(value):
    """Set the report status"""
    Settings.set_report(value)

