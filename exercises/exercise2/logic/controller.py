"""Controller module"""
import timeit
total_time = 0

def execute():
    """Start the process of evolution."""
    global total_time
    reset_populations()
    generations = Settings.get_generations("exercise2")
    start_time = timeit.default_timer()
    next_generation = Population()
    for _ in range(generations-1):
        population_manager.add_population("exercise2", next_generation)
        actual_generation = next_generation
        actual_generation.evolve()
        next_generation = actual_generation.get_next_generation()
        convergence = next_generation.get_range()
        if convergence == 0:
            break
    total_time = timeit.default_timer() - start_time
    population_manager.add_population("exercise2", next_generation)

def show_settings():
    """Show basic Configurations."""
    settings = Settings.load_all_settings("exercise2")
    return pd.Series(settings)

def get_generation_report():
    return report.generations_report("exercise2")

def get_solution_report():
    return report.solution_report("exercise2") 

def get_execution_time():
    global total_time
    return total_time

def get_decimal_value_report():
    population = population_manager.get_last_population("exercise2")
    gene_string = population.get_max_gene_string()
    return int(gene_string, 2)

def get_cross_over_prob():
    return Settings.get_cross_over_prob("exercise2")

def set_cross_over_prob(raw_value):
    value = float(raw_value)
    Settings.set_cross_over_prob("exercise2", value)

def get_chromosome_bits():
    """Set the chromosome bits"""
    return Settings.get_chromosome_bits("exercise2")

def set_chromosome_bits(value):
    int_value = int(value)
    Settings.set_chromosome_bits("exercise2", int_value)

def get_generations():
    """Set the maximum amount of generations"""
    return Settings.get_generations("exercise2")

def set_generations(value):
    int_value = int(value)
    Settings.set_generations("exercise2", int_value)

def get_mutation_prob():
    """Set the mutation probability"""
    return Settings.get_mutation_prob("exercise2")

def set_mutation_prob(value):
    float_value = float(value)
    Settings.set_mutation_prob("exercise2", float_value)

def get_population_size():
    """Set the initial population size"""
    return Settings.get_population_size("exercise2")

def set_population_size(value):
    int_value = int(value)
    Settings.set_population_size("exercise2", int_value)

def get_elitism():
    """Set the elitism status"""
    return Settings.get_elitism("exercise2")

def set_elitism(value):
    boolean_value = value == "1"
    Settings.set_elitism("exercise2", boolean_value)

def reset_populations():
    """Delete all the populations in the results file and reset the generations
        counter"""
    results = []
    Population.reset_generations()
    filemanager.store_results("exercise2", results)

if __name__ != '__main__':
    import pandas as pd

    import base.logic.report as report
    import base.data.filemanager as filemanager
    import base.logic.population_manager as population_manager
    from exercise2.entities.population import Population
    from base.logic.settings_manager import Settings
