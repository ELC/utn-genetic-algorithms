"""Reports"""

import exercise1.logic.population_manager as population_manager
import pandas as pd
import time 
from openpyxl import load_workbook
from exercise1.logic.settings_manager import Settings

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
    # data_frame = data_frame.reindex(data_frame.index.rename("Generacion"))
    write_csv(data_frame)
    write_excel(data_frame)
    return data_frame

def write_csv(df):
    name = str(Settings.get_settings_id())[:5]
    filename = name + '.csv'
    if is_empty(filename):
        settings = Settings.load_all_settings()
        pd.DataFrame(list(settings.items())).to_csv(filename, mode="a+",index=False)
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

def write_excel(df):
    sheet_name = str(time.strftime("%Y-%m-%d %H.%M.%S"))
    filename = 'resultados.xlsx'
    writer = pd.ExcelWriter(filename, engine='openpyxl')

    try:
        writer.book = load_workbook(filename)
        writer.sheets = dict(
            (ws.title, ws) for ws in writer.book.worksheets)
    except:
        pass

    settings = Settings.load_all_settings()
    pd.DataFrame(list(settings.items())).to_excel(writer, sheet_name=sheet_name, index=False, startcol=8)
    df.to_excel(writer, sheet_name=sheet_name, index=False)

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
    aux = ""
    stationary = []
    for population in data:
        if population.get_max_gene_string() != aux:
            aux = population.get_max_gene_string()
            last_value = int(population.get_generation())-1
        stationary.append(last_value)
    return stationary


