"""Reports"""

import base.logic.population_manager as population_manager
import pandas as pd
import time 
from openpyxl import load_workbook
from base.logic.settings_manager import Settings

pd.set_option('display.max_rows', 1500)
pd.set_option('display.max_columns', 700)
pd.set_option('display.width', 1500)
pd.set_option('precision', 12)

def full_report():
    """Show all the reports"""
    gens = generations_report()
    sol = solution_report()
    return gens, sol

def generations_report(module):
    """Show the generations report"""
    data = population_manager.load_populations(module)
    datas = _get_array_data(data)
    labels = ("1-Máx",
              "2-Mín",
              "3-Promedio",
              "5-Rango",
              "4-Total",
              "6-Cromosoma",
              "7-Estable")
    data_pd = {i:pd.Series(j) for i, j in zip(labels, datas)}
    data_frame = pd.DataFrame(data_pd)
    data_frame.index.names = ['G']
    
    filename = module + "/data/" + str(Settings.get_settings_id(module))[:5]
    settings = Settings.load_all_settings(module)
    settings = pd.DataFrame(list(settings.items()))

    write_csv(filename, data_frame, settings)
    write_excel(filename, data_frame, settings)
    return data_frame

def write_csv(name, df, settings):
    filename = name + '.csv'
    if is_empty(filename):
        settings.to_csv(filename, mode="a+",index=False)
        add_empty_line(filename)
    df.to_csv(filename, mode="a+")
    add_empty_line(filename)

def add_empty_line(filename):
    with open(filename,"a+") as handler:
        handler.write('\n')

def is_empty(filename):
    try:
        with open(filename) as my_file:
            pass
        return False
    except FileNotFoundError:
        return True

def write_excel(name, df, settings):
    sheet_name = str(time.strftime("%Y-%m-%d %H.%M.%S"))
    filename = name + '.xlsx'
    writer = pd.ExcelWriter(filename, engine='openpyxl')

    try:
        writer.book = load_workbook(filename)
        writer.sheets = dict(
            (ws.title, ws) for ws in writer.book.worksheets)
    except:
        pass

    settings.to_excel(writer, sheet_name=sheet_name, index=False, startcol=8)
    df.to_excel(writer, sheet_name=sheet_name, index=False)

    writer.save()
    writer.close()


def solution_report(module):
    """Show the final solution infered from the generations"""
    data = population_manager.load_populations(module)
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
    aux = ""
    stationary = []
    for population in data:
        if population.get_max_gene_string() != aux:
            aux = population.get_max_gene_string()
            last_value = int(population.get_generation())-1
        stationary.append(last_value)
    return stationary


