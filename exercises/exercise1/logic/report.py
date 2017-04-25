"""Reports"""

import exercise1.logic.population_manager as population_manager
import pandas as pd

def full_report():
    """Show all the reports"""
    gens = generations_report()
    sol = solution_report()
    return gens, sol

def generations_report():
    """Show the generations report"""
    data = population_manager.load_populations()
    data_pd = _get_data_frame(data)

    gens = [i for i, _ in enumerate(data)]

    data_frame = pd.DataFrame.from_items(data_pd, orient='index', columns=gens)

    return data_frame

def solution_report():
    """Show the final solution infered from the generations"""
    data = population_manager.load_populations()
    last_population = data[-1]
    solution = last_population.get_maximum()
    return solution

def _get_data_frame(data):
    datas = _get_array_data(data)
    labels = ("Máximo", "Mínimo", "Promedio", "Rango")
    return [(i, j) for i, j in zip(labels, datas)]

def _get_array_data(data):
    maximums = [i.get_maximum() for i in data]
    minimums = [i.get_minimum() for i in data]
    averages = [i.get_average() for i in data]
    ranges = [i.get_range() for i in data]
    return (maximums, minimums, averages, ranges)
