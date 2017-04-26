import exercise1.logic.population_manager as population_manager
from exercise1.util.graphic import graphics

def graphic_mma():
    maximums = population_manager.get_maximums()
    averages = population_manager.get_averages()
    minimums = population_manager.get_minimums()
    labels = ["Máximo", "Promedio", "Minimo"]
    graphics((maximums, averages, minimums), labels)

def graphic_r():
    ranges = [population_manager.get_ranges()]
    labels = ["Rangos"]
    graphics(ranges, labels)

def graphic_t():
    totals = [population_manager.get_totals()]
    labels = ["Totales"]
    graphics(totals, labels)
