"""Target Function"""

import base.util.util as util
from exercise3.main import get_objects, get_cities
from exercise3.main import calc_distance_beetween_cities

def target(gene_string):
    """Define a Target function."""
    cities = get_cities_from_array(gene_string)
    
    total_distance = get_distance_from_cities(cities)

    return 1 / total_distance

def get_distance_from_cities(cities):
    total_distance = 0
    for i in range(len(cities)-1):
        total_distance += calc_distance_beetween_cities(cities[i], cities[i+1])
    total_distance += calc_distance_beetween_cities(cities[-1], cities[0])
    return total_distance

def get_cities_from_array(array):
    cities = get_cities()
    return [cities[index] for index in array]
