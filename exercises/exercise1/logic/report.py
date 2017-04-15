"""Reports"""

from exercise1.logic.settings import Settings
import pandas as pd

def full_report():
    """Show all the reports"""
    gens = generations_report()
    sol = solution_report()
    return gens, sol

def generations_report():
    """Show the generations report"""
    data = Settings.load_results()
    data_pd = _get_data_frame(data)

    gens = [i for i, _ in enumerate(data)]

    data_frame = pd.DataFrame.from_items(data_pd, orient='index', columns=gens)

    return data_frame


def solution_report():
    """Show the final solution infered from the generations"""
    data = Settings.load_results()
    last_population = data[-1]
    solution = last_population.maximum
    return solution

def _get_data_frame(data):
    datas = _get_array_data(data)
    labels = ("Máximo", "Mínimo", "Promedio", "Mínimos cuadrados", "Rango")
    return [(i, j) for i, j in zip(labels, datas)]

def _get_array_data(data):
    maximums = [i.maximum for i in data]
    minimums = [i.minimum for i in data]
    averages = [i.average for i in data]
    leasts = [i.least for i in data]
    ranges = [i.range for i in data]
    return (maximums, minimums, averages, leasts, ranges)
