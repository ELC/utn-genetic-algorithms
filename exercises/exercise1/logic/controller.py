"""Controller module"""

def execute():
    """Start the process of evolution."""
    population_manager.reset_populations()
    generations = Settings.get_generations()
    next_generation = Population()
    for _ in range(generations-1):
        population_manager.add_population(next_generation)
        actual_generation = next_generation
        actual_generation.evolve()
        next_generation = actual_generation.get_next_generation()
        convergence = next_generation.get_range()
        if convergence == 0:
            break
    population_manager.add_population(next_generation)

def show_settings():
    """Show basic Configurations."""
    settings = Settings.load_all_settings()
    return pd.Series(settings)

def get_generation_report():
    return report.generations_report()

def get_solution_report():
    return report.solution_report()

def get_cross_over_prob():
    return Settings.get_cross_over_prob()

def set_cross_over_prob(raw_value):
    value = float(raw_value)
    Settings.set_cross_over_prob(value)

def get_chromosome_bits():
    """Set the chromosome bits"""
    return Settings.get_chromosome_bits()

def set_chromosome_bits(value):
    int_value = int(value)
    Settings.set_chromosome_bits(int_value)

def get_generations():
    """Set the maximum amount of generations"""
    return Settings.get_generations()

def set_generations(value):
    int_value = int(value)
    Settings.set_generations(int_value)

def get_mutation_prob():
    """Set the mutation probability"""
    return Settings.get_mutation_prob()

def set_mutation_prob(value):
    float_value = float(value)
    Settings.set_mutation_prob(float_value)

def get_population_size():
    """Set the initial population size"""
    return Settings.get_population_size()

def set_population_size(value):
    int_value = int(value)
    Settings.set_population_size(int_value)

def get_elitism():
    """Set the elitism status"""
    return Settings.get_elitism()

def set_elitism(value):
    boolean_value = value == "1"
    Settings.set_elitism(boolean_value)

if __name__ != '__main__':
    import pandas as pd
    import exercise1.logic.report as report
    import exercise1.logic.population_manager as population_manager
    from exercise1.entities.population import Population
    from exercise1.logic.settings_manager import Settings
