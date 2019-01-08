# Metodo Greedy
import exercise3.logic.target as target
import timeit
from exercise3.main import coord_to_matrix, get_objects, calc_distance_beetween_cities

provinces = get_objects()

def greedy(matrix, cities, initial_city):
    total_distance = 0
    remaining_cities = {city:matrix[i] for i, city in enumerate(cities)}
    next_city = initial_city
    route = [next_city]
    while len(route) != len(cities):
        row = remaining_cities.pop(next_city)
        min_distance = min(i for i in row if i > 0 and cities[row.index(i)] not in route)
        index = row.index(min_distance)
        next_city = cities[index]
        total_distance += min_distance
        route.append(next_city)
    total_distance += calc_distance_beetween_cities(route[-1], initial_city)
    return (total_distance, route)

def execute(matrix, cities):
    start_time = timeit.default_timer()

    distancia = None
    for city in cities:
        distancia_alt, route_alt = greedy(matrix, cities, city)
        if distancia is None or distancia_alt < distancia:
            distancia = distancia_alt
            route = route_alt

    total_time = timeit.default_timer() - start_time

    return total_time, route[0], distancia, route