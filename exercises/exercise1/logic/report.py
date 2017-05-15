"""Reports"""

import exercise1.logic.population_manager as population_manager
import pandas as pd
import time 
from openpyxl import load_workbook

pd.set_option('display.max_rows', 1500)
pd.set_option('display.max_columns', 700)
pd.set_option('display.width', 1500)
pd.set_option('precision', 12)

def full_report():
    """Show all the reports"""
    gens = generations_report()
    sol = solution_report()
    return gens, sol

def generations_report():
    """Show the generations report"""
    data = population_manager.load_populations()
    datas = _get_array_data(data)
    labels = ("1-Máximo",
              "2-Mínimo",
              "3-Promedio",
              "5-Rango",
              "4-Total",
              "6-Cromosoma",
              "7-Estable")
    data_pd = {i:pd.Series(j) for i, j in zip(labels, datas)}
    data_frame = pd.DataFrame(data_pd)
    write_excel(data_frame)
    return data_frame

def write_excel(df):
    sheet_name = str(time.strftime("%Y-%m-%d %H.%M.%S"))
    filename = 'resultados.xlsx'
    writer = pd.ExcelWriter(filename, engine='openpyxl')
    #df.to_excel(writer, index=False, sheet_name=sheet_name)

    # Get the xlsxwriter objects from the dataframe writer object.
    try:
        writer.book = load_workbook(filename)
        writer.sheets = dict(
            (ws.title, ws) for ws in writer.book.worksheets)
    except:
        pass

    df.to_excel(writer, sheet_name=sheet_name)

    writer.save()
    writer.close()


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
    stationary = _get_stationary(data)
    return (maximums, minimums, averages, ranges, total, chromosome, stationary)

def _get_stationary(data):
    aux = data[0].get_max_gene_string()
    stationary = []
    last_value = 0
    for population in data:
        stationary.append(last_value)
        if population.get_max_gene_string() != aux:
            aux = population.get_max_gene_string()
            last_value = population.get_generation()
    return stationary


