"""Data layer of Population"""

def add_population(result):
    """Send the result to the file manager"""
    results = filemanager.load_results()
    results.append(result)
    filemanager.store_results(results)

def store_population(results):
    """Send the results to the file manager"""
    filemanager.store_results(results)

def load_populations():
    """Load the results from the file manager"""
    results = filemanager.load_results()
    return results

def reset_populations():
    """Load the results from the file manager"""
    results = []
    filemanager.store_results(results)

def get_maximums():
    populations = load_populations()
    return [i.get_maximum() for i in populations]

def get_minimums():
    populations = load_populations()
    return [i.get_minimum() for i in populations]

def get_averages():
    populations = load_populations()
    return [i.get_average() for i in populations]

def get_ranges():
    populations = load_populations()
    return [i.get_range() for i in populations]

def get_totals():
    populations = load_populations()
    return [i.get_sum() for i in populations]

if __name__ != '__main__':
    import exercise1.data.filemanager as filemanager
