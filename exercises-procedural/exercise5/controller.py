"""Controller module"""

def execute():
    settings = FileManager.load_settings()

    number_of_generations = settings["generations"]
    population_size = settings["population_size"]
    objects = settings["objects"]
    chromosome_size = len(objects)
    elitism = settings["elitism"]
    mutation_prob = settings["mutation_prob"] 
    cross_over_prob = settings["cross_over_prob"] 
    total_vol = settings["total_vol"]

    start_time = timeit.default_timer()
    _execute(number_of_generations, population_size, chromosome_size, elitism, mutation_prob, cross_over_prob, objects, total_vol)
    return timeit.default_timer() - start_time

def _execute(number_of_generations, population_size, chromosome_size, elitism, mutation_prob, cross_over_prob, objects, total):
    
    FileManager.reset_results()

    population = Population.create_population(population_size, chromosome_size, objects, total)
    
    for _ in range(number_of_generations - 1):

        FileManager.add_to_results(population)
        
        population = Population.evolve(population, elitism, mutation_prob, cross_over_prob, objects, total)

        targets = Population.get_targets(population, objects, total)

        if max(targets) - min(targets) == 0:
            break

    FileManager.add_to_results(population)


def show_settings():
    return pd.Series(FileManager.load_settings())


if __name__ != '__main__':

    import timeit

    from exercise5.util.report import Report
    import exercise5.population as Population
    import exercise5.filemanager as FileManager

    import pandas as pd
