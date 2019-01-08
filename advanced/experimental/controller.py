"""Controller module"""

def execute():
    settings = FileManager.load_settings()

    number_of_generations = settings["generations"]
    population_size = settings["population_size"]
    chromosome_size = settings["chromosome_bits"]
    elitism = settings["elitism"]
    mutation_prob = settings["mutation_prob"] 
    cross_over_prob = settings["cross_over_prob"] 
    convergence = settings["convergence"]
    annealing = settings["annealing"]
    reverse_annealing = settings["reverse_annealing"]

    start_time = timeit.default_timer()
    _execute(number_of_generations, population_size, chromosome_size, elitism, mutation_prob, cross_over_prob, convergence, annealing, reverse_annealing)
    return timeit.default_timer() - start_time

def _execute(number_of_generations, population_size, chromosome_size, elitism, mutation_prob, cross_over_prob, convergence, annealing, reverse_annealing):
    
    FileManager.reset_results()

    population = Population.create_population(population_size, chromosome_size)
    
    for current_generation in range(number_of_generations):

        if annealing:
            mutation_prob = (1 - (current_generation / number_of_generations)**3) * mutation_prob

        if reverse_annealing:
            cross_over_prob = (current_generation / number_of_generations)**3 * cross_over_prob

        FileManager.add_to_results(population)
        
        population = Population.evolve(population, elitism, mutation_prob, cross_over_prob)

        targets = Population.get_targets(population)

        if max(targets) - min(targets) <= convergence:
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

    from experimental.util.report import Report
    import experimental.population as Population
    import experimental.filemanager as FileManager

    import pandas as pd
