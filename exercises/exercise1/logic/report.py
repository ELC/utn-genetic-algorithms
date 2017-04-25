"""Reports"""

import exercise1.logic.population_manager as population_manager
import pandas as pd

pd.set_option('display.height', 1000)
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
pd.set_option('precision',20)

def full_report():
    """Show all the reports"""
    gens = generations_report()
    sol = solution_report()
    return gens, sol

def generations_report():
    """Show the generations report"""
    data = population_manager.load_populations()

    datas = _get_array_data(data)
    labels = ("1-Máximo", "2-Mínimo", "3-Promedio", "5-Rango", "4-Total", "6-Cromosoma")
    data_pd = {i:pd.Series(j) for i, j in zip(labels, datas)}
    data_frame = pd.DataFrame(data_pd)

    return data_frame

def solution_report():
    """Show the final solution infered from the generations"""
    data = population_manager.load_populations()
    last_population = data[-1]
    solution = last_population.get_maximum()
    return solution


def _get_array_data(data):
    maximums = [population.get_maximum() for population in data]
    minimums = [population.get_minimum() for population in data]
    averages = [population.get_average() for population in data]
    ranges = [population.get_range() for population in data]
    total = [population.get_sum() for population in data]
    chromosome = [population.get_max_gene_string() for population in data]
    return (maximums, minimums, averages, ranges, total, chromosome)
