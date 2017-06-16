"""Data layer of Population"""

def add_population(module, result):
    """Add a population to the file"""
    results = filemanager.load_results(module)
    results.append(result)
    filemanager.store_results(module, results)

def store_population(module, results):
    """Store a collection of populations in the file"""
    filemanager.store_results(module, results)

def load_populations(module):
    """Return a list of all the populations from the results file"""
    results = filemanager.load_results(module)
    return results

def get_maximums(module):
    """Return a list with the maximums of each population"""
    populations = load_populations(module)
    return [i.get_maximum() for i in populations]

def get_minimums(module):
    """Return a list with the minimums of each population"""
    populations = load_populations(module)
    return [i.get_minimum() for i in populations]

def get_averages(module):
    """Return a list with the averages of each population"""
    populations = load_populations(module)
    return [i.get_average() for i in populations]

def get_ranges(module):
    """Return a list with the difference between the maximum and the minimum
        of each population"""
    populations = load_populations(module)
    return [i.get_range() for i in populations]

def get_totals(module):
    """Return a list with the sum of all the targets values of each
        population"""
    populations = load_populations(module)
    return [i.get_sum() for i in populations]

def get_last_population(module):
    populations = load_populations(module)
    return populations[-1]

if __name__ != '__main__':
    import base.data.filemanager as filemanager