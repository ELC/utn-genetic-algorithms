"""Data layer of Population"""

def add_population(result):
    """Add a population to the file"""
    results = filemanager.load_results()
    results.append(result)
    filemanager.store_results(results)

def store_population(results):
    """Store a collection of populations in the file"""
    filemanager.store_results(results)

def load_populations():
    """Return a list of all the populations from the results file"""
    results = filemanager.load_results()
    return results

def reset_populations():
    """Delete all the populations in the results file and reset the generations
        counter"""
    results = []
    filemanager.store_results(results)

def get_maximums():
    """Return a list with the maximums of each population"""
    populations = load_populations()
    return [i.get_maximum() for i in populations]

def get_minimums():
    """Return a list with the minimums of each population"""
    populations = load_populations()
    return [i.get_minimum() for i in populations]

def get_averages():
    """Return a list with the averages of each population"""
    populations = load_populations()
    return [i.get_average() for i in populations]

def get_ranges():
    """Return a list with the difference between the maximum and the minimum
        of each population"""
    populations = load_populations()
    return [i.get_range() for i in populations]

def get_totals():
    """Return a list with the sum of all the targets values of each
        population"""
    populations = load_populations()
    return [i.get_sum() for i in populations]

if __name__ != '__main__':
    import exercise1.data.filemanager as filemanager
