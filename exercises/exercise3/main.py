from math import sin, cos, sqrt, atan2, radians

def get_objects():
    return provinces

provinces = {
    #"rosario":(-32.95, -60.65),
    #"bs_as":(-34.599722, -58.381944),
    "cordoba":(-31.416667, -64.183333),
    "la_plata":(-34.933333, -57.95),
    "san_fernando":(-28.468611, -65.779167),
    "resistencia":(-27.451389, -58.986667),
    "rawson":(-43.3, -65.1),
    "corrientes":(-27.483333, -58.816667),
    "parana":(-31.744444, -60.5175),
    "formosa":(-26.184722, -58.175833),
    "san_salvador":(-24.185556, -65.299444),
    "santa_rosa":(-36.620278, -64.290556),
    "la_rioja":(-29.413056, -66.855833),
    "mendoza":(-32.883333, -68.833333),
    "posadas":(-27.366667, -55.896944),
    "neuquen":(-38.95735, -68.045533),
    "viedma":(-40.8, -63),
    "salta":(-24.788333, -65.410556),
    "san_juan":(-31.5375, -68.536389),
    "san_luis":(-33.277222, -66.3525),
    "rio_gallegos":(-51.633333, -69.233333),
    "santa_fe":(-31.633333, -60.7),
    "santiago_del_estero":(-27.784444, -64.266944),
    "ushuaia":(-54.807222, -68.304444),
    "san_miguel":(-26.816667, -65.216667),
}

def calc_distance_beetween_cities(city1, city2):
    return calc_distance(*provinces[city1], *provinces[city2])

def calc_distance(_lat1, _lon1, _lat2, _lon2):
    """ Use of Haversine Algorithm"""
    
    R = 6373.0
    lat1 = radians(_lat1)
    lon1 = radians(_lon1)
    lat2 = radians(_lat2)
    lon2 = radians(_lon2)
    
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    
    return int(R * c)

def coord_to_matrix(coords):
    matrix = []

    for city_coords in coords:
        row = []
        for city_coords_ in coords:
            distance = calc_distance(*city_coords, *city_coords_)
            row.append(distance)
        matrix.append(row)

    return matrix

def get_cities():
    return sorted(i for i in provinces.keys())

def get_matrix():
    coords = [provinces[i] for i in get_cities()]
    matrix = coord_to_matrix(coords)
    return matrix

def main():
    Settings.set_chromosome_bits("exercise3", len(get_objects()))

    cities = get_cities()
    matrix = get_matrix()

    print("\nGreedy: ")
    time, best_city, ruta, route = greedy.execute(matrix, cities)
    show(time, best_city, ruta, route)

    print("\nAlgoritmos geneticos: ")
    time, best_city, ruta, route, number_generations = api.execute()
    show(time, best_city, ruta, route)
    max_gen = Settings.get_generations("exercise3")
    if number_generations == max_gen:
        print("Finalizó por llegar a la cantidad máxima de generaciones - {} generaciones".format(max_gen))
    else:
        print("Convergió antes de llegar al máximo de generaciones - Generación: {} - Máxima: {}".format(number_generations, max_gen))

    # print("\nExhaustiva: ")
    # time, best_city, ruta, route = exhaustiva.execute()
    # show(time, best_city, ruta, route)

def show(time, best_city, ruta, route):
    print("Ciudad Inicial: {}".format(best_city))
    print("Distancia Total: {}".format(ruta))
    print("Ruta: {}".format(", ".join(route)))
    print("Tiempo de ejecucion: {0:.6f}".format(time))

if __name__ == '__main__':
    import exercise3.api as api
    import exercise3.greedy as greedy
    #import exercise3.exhaustiva as exhaustiva
    from base.logic.settings_manager import Settings
    
    main()
