"""Controller module"""
import timeit
total_time = 0

module = "exercise2"

def execute():
    """Start the process of evolution."""
    global total_time
    reset_populations()
    generations = Settings.get_generations(module)
    start_time = timeit.default_timer()
    next_generation = Population()
    for _ in range(generations-1):
        population_manager.add_population(module, next_generation)
        actual_generation = next_generation
        actual_generation.evolve()
        next_generation = actual_generation.get_next_generation()
        convergence = next_generation.get_range()
        if convergence == 0:
            break
    total_time = timeit.default_timer() - start_time
    population_manager.add_population(module, next_generation)

def show_settings():
    """Show basic Configurations."""
    settings = Settings.load_all_settings(module)
    return pd.Series(settings)

def get_generation_report():
    return report.generations_report(module)

def get_solution_report():
    return report.solution_report(module) 

def get_execution_time():
    global total_time
    return total_time

def get_decimal_value_report():
    population = population_manager.get_last_population(module)
    gene_string = population.get_max_gene_string()
    return ", ".join(str(i) for i in target.get_indexes(gene_string))

def get_cross_over_prob():
    return Settings.get_cross_over_prob(module)

def set_cross_over_prob(raw_value):
    value = float(raw_value)
    Settings.set_cross_over_prob(module, value)

def get_chromosome_bits():
    """Set the chromosome bits"""
    return Settings.get_chromosome_bits(module)

def set_chromosome_bits(value):
    int_value = int(value)
    Settings.set_chromosome_bits(module, int_value)

def get_generations():
    """Set the maximum amount of generations"""
    return Settings.get_generations(module)

def set_generations(value):
    int_value = int(value)
    Settings.set_generations(module, int_value)

def get_mutation_prob():
    """Set the mutation probability"""
    return Settings.get_mutation_prob(module)

def set_mutation_prob(value):
    float_value = float(value)
    Settings.set_mutation_prob(module, float_value)

def get_population_size():
    """Set the initial population size"""
    return Settings.get_population_size(module)

def set_population_size(value):
    int_value = int(value)
    Settings.set_population_size(module, int_value)

def get_elitism():
    """Set the elitism status"""
    return Settings.get_elitism(module)

def set_elitism(value):
    boolean_value = value == "1"
    Settings.set_elitism(module, boolean_value)

def reset_populations():
    """Delete all the populations in the results file and reset the generations
        counter"""
    results = []
    Population.reset_generations()
    filemanager.store_results(module, results)

if __name__ != '__main__':
    import pandas as pd
    import exercise2.logic.target as target
    import base.logic.report as report
    import base.data.filemanager as filemanager
    import base.logic.population_manager as population_manager
    from exercise2.entities.population import Population
    from base.logic.settings_manager import Settings
