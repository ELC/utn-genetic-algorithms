"""Controller module"""

def execute():
    settings = FileManager.load_settings()

    number_of_generations = settings["generations"]
    population_size = settings["population_size"]
    chromosome_size = settings["chromosome_bits"]
    elitism = settings["elitism"]
    mutation_prob = settings["mutation_prob"] 
    cross_over_prob = settings["cross_over_prob"] 

    start_time = timeit.default_timer()
    _execute(number_of_generations, population_size, chromosome_size, elitism, mutation_prob, cross_over_prob)
    return timeit.default_timer() - start_time

def _execute(number_of_generations, population_size, chromosome_size, elitism, mutation_prob, cross_over_prob):
    
    FileManager.reset_results()

    population = Population.create_population(population_size, chromosome_size)
    
    for _ in range(number_of_generations - 1):

        FileManager.add_to_results(population)
        
        population = Population.evolve(population, elitism, mutation_prob, cross_over_prob)

        targets = Population.get_targets(population)

        if max(targets) - min(targets) == 0:
            break

    FileManager.add_to_results(population)


def show_settings():
    return pd.Series(FileManager.load_settings())


def get_generation_report(execution_time):
    return Report.generations_report(execution_time)


def get_solution_report():
    return Report.solution_report()


def get_decimal_value_report():
    population = FileManager.load_results()[-1]
    gene_string = Population.get_fittest_chromosome(population)
    return int(gene_string, 2)

if __name__ != '__main__':

    import timeit

    from exercise1.util.report import Report
    import exercise1.population as Population
    import exercise1.filemanager as FileManager

    import pandas as pd
