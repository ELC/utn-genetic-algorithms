from math import sin, cos, sqrt, atan2, radians
import timeit

def get_objects():
    return provinces

m_enunciado = [ [0, 1543, 1510, 1203, 1043, 1191, 1023, 478, 940, 1040, 480, 715, 1150, 1110, 790, 1155, 1050, 620, 1158, 960, 1455, 2635, 3228],
 [1543, 0, 99, 340, 500, 960, 860, 1107, 883, 1198, 1138, 930, 770, 1220, 1320, 572, 1345, 1530, 2200, 2124, 2385, 3565, 4158],
 [1510, 99, 0, 307, 467, 948, 780, 1074, 803, 1118, 1105, 897, 695, 1145, 1245, 539, 1227, 1497, 2082, 2091, 2352, 3532, 4125],
 [1203, 340, 307, 0, 160, 936, 768, 767, 791, 1106, 798, 590, 338, 838, 938, 232, 1005, 1190, 1860, 1784, 2045, 3225, 3818],
 [1043, 500, 467, 160, 0, 776, 610, 607, 633, 948, 638, 430, 360, 810, 850, 212, 977, 1030, 1567, 1624, 1885, 3065, 3658],
 [1191, 960, 948, 936, 776, 0, 168, 713, 191, 506, 744, 1043, 1136, 1543, 1463, 988, 1710, 1523, 2060, 2117, 2378, 3558, 4151],
 [1023, 860, 780, 765, 610, 168, 0, 545, 23, 338, 576, 875, 970, 1420, 1295, 822, 1587, 1475, 2012, 2069, 2210, 3390, 3983],
 [478, 1107, 1074, 767, 607, 713, 545, 0, 568, 883, 31, 330, 765, 830, 625, 770, 885, 810, 1347, 1404, 1665, 2845, 3438],
 [940, 883, 803, 791, 633, 191, 23, 568, 0, 315, 590, 898, 993, 1398, 1318, 845, 1565, 1378, 1989, 2046, 2187, 3367, 3960],
 [1040, 1198, 1118, 1106, 948, 506, 338, 883, 315, 0, 820, 1213, 1308, 1758, 1633, 1160, 1925, 1660, 2198, 2000, 2495, 3675, 4268],
 [480, 1138, 1105, 798, 638, 744, 576, 31, 590, 820, 0, 361, 796, 861, 656, 801, 916, 841, 1378, 1435, 1696, 2876, 3469],
 [715, 930, 897, 590, 430, 1043, 875, 330, 898, 1213, 361, 0, 435, 500, 420, 440, 670, 600, 1137, 1194, 1455, 3635, 3228],
 [1150, 770, 695, 388, 360, 1136, 970, 765, 993, 1308, 796, 435, 0, 450, 550, 156, 617, 1035, 1472, 1629, 1890, 3070, 3663],
 [1110, 1220, 1145, 838, 810, 1543, 1420, 830, 1398, 1758, 861, 500, 450, 0, 320, 606, 167, 825, 1022, 1419, 1680, 2860, 3453],
 [790, 1320, 1245, 938, 850, 1463, 1295, 625, 1318, 1633, 656, 420, 550, 320, 0, 705, 260, 505, 883, 1099, 1360, 2540, 3133],
 [1145, 572, 539, 232, 212, 988, 822, 770, 845, 1160, 801, 440, 156, 606, 705, 0, 773, 1040, 1588, 1634, 1895, 3075, 3668],
 [1050, 1345, 1227, 1005, 977, 1710, 1587, 885, 1565, 1925, 916, 670, 617, 167, 260, 773, 0, 765, 855, 1359, 1620, 2800, 3393],
 [620, 1530, 1497, 1190, 1030, 1523, 1475, 810, 1378, 1660, 841, 600, 1035, 825, 505, 1040, 765, 0, 537, 594, 855, 2035, 2628],
 [1158, 2200, 2082, 1860, 1567, 2060, 2012, 1347, 1989, 2198, 1378, 1137, 1472, 1022, 883, 1588, 855, 537, 0, 660, 750, 1930, 2523],
 [960, 2124, 2091, 1784, 1624, 2117, 2069, 1404, 2046, 2000, 1435, 1194, 1629, 1419, 1099, 1634, 1359, 594, 660, 0, 495, 1675, 2268],
 [1455, 2385, 2352, 2045, 1885, 2378, 2210, 1665, 2187, 2495, 1696, 1455, 1890, 1680, 1360, 1895, 1620, 855, 750, 495, 0, 1180, 1773],
 [2635, 3565, 3532, 3225, 3065, 3558, 3390, 2845, 3367, 3675, 2876, 2635, 3070, 2860, 2540, 3075, 2800, 2035, 1930, 1675, 1180, 0, 593],
 [3228, 4158, 4125, 3818, 3658, 4151, 3983, 3438, 3960, 4268, 3469, 3228, 3660, 3453, 3133, 3668, 3393, 2628, 2523, 2268, 1773, 593, 0]]

cities_alt = ["Buenos Aires",
            "San S. de Jujuy",
            "Salta",
            "S. M. de Tucumán",
            "Sgo. del Estero",
            "Formosa",
            "Resistencia",
            "Santa Fe",
            "Corrientes",
            "Posadas",
            "Paraná",
            "Córdoba",
            "La Rioja",
            "San Juan",
            "San Luis",
            "S. F. del valle de Catamarca",
            "Mendoza",
            "Santa Rosa",
            "Neuquén",
            "Viedma",
            "Rawson",
            "Rio Gallegos",
            "Ushuaia"]

provinces = {
    #"rosario":(-32.95, -60.65),
    #"la_plata":(-34.933333, -57.95),
    "Buenos Aires":(-34.599722, -58.381944),
    "Córdoba":(-31.416667, -64.183333),
    "S. F. del valle de Catamarca":(-28.468611, -65.779167),
    "Resistencia":(-27.451389, -58.986667),
    "Rawson":(-43.3, -65.1),
    "Corrientes":(-27.483333, -58.816667),
    "Paraná":(-31.744444, -60.5175),
    "Formosa":(-26.184722, -58.175833),
    "San S. de Jujuy":(-24.185556, -65.299444),
    "Santa Rosa":(-36.620278, -64.290556),
    "La Rioja":(-29.413056, -66.855833),
    "Mendoza":(-32.883333, -68.833333),
    "Posadas":(-27.366667, -55.896944),
    "Neuquén":(-38.95735, -68.045533),
    "Viedma":(-40.8, -63),
    "Salta":(-24.788333, -65.410556),
    "San Juan":(-31.5375, -68.536389),
    "San Luis":(-33.277222, -66.3525),
    "Rio Gallegos":(-51.633333, -69.233333),
    "Santa Fe":(-31.633333, -60.7),
    "Sgo. del Estero":(-27.784444, -64.266944),
    "Ushuaia":(-54.807222, -68.304444),
    "S. M. de Tucumán":(-26.816667, -65.216667),
}

def get_provinces():
    return provinces

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
    return cities_alt 

def get_cities2():
    return sorted(i for i in provinces.keys())

def get_matrix():
    return m_enunciado

def get_matrix2():
    coords = [provinces[i] for i in get_cities()]
    matrix = coord_to_matrix(coords)
    return matrix

def calc_distance_beetween_cities(city1, city2):
    index1 = cities_alt.index(city1)
    index2 = cities_alt.index(city2)
    return m_enunciado[index1][index2]

def calc_distance_beetween_cities2(city1, city2):
    return calc_distance(*provinces[city1], *provinces[city2])


def option1():
    print("Ingrese el código de la ciudad que desea")
    cities = get_cities()
    matrix = get_matrix()
    for i, j in enumerate(cities):
        print("{}. {}".format(i, j) )
    city = input(">")
    print("\nGreedy: ")
    start_time = timeit.default_timer()
    distancia, route = greedy.greedy(matrix, cities, cities[int(city)])
    time = timeit.default_timer() - start_time
    show(time, route[0], distancia, route)

def option2():
    print("\nGreedy: ")
    cities = get_cities()
    matrix = get_matrix()
    time, best_city, distancia, route = greedy.execute(matrix, cities)
    show(time, best_city, distancia, route)

def option3():
    print("\nAlgoritmos geneticos: ")
    time, best_city, distancia, route, number_generations = api.execute()
    show(time, best_city, distancia, route)
    max_gen = Settings.get_generations("exercise3")
    if number_generations == max_gen:
        print("Finalizó por llegar a la cantidad máxima de generaciones - {} generaciones".format(max_gen))
    else:
        print("Convergió antes de llegar al máximo de generaciones - Generación: {} - Máxima: {}".format(number_generations, max_gen))

def option4():
    cities = get_cities()
    matrix = get_matrix()
    print("\nGreedy: ")
    time, best_city, distancia, route = greedy.execute(matrix, cities)
    show(time, best_city, distancia, route)

    print("\nAlgoritmos geneticos: ")
    time, best_city, distancia, route, number_generations = api.execute()
    show(time, best_city, distancia, route)
    max_gen = Settings.get_generations("exercise3")
    if number_generations == max_gen:
        print("Finalizó por llegar a la cantidad máxima de generaciones - {} generaciones".format(max_gen))
    else:
        print("Convergió antes de llegar al máximo de generaciones - Generación: {} - Máxima: {}".format(number_generations, max_gen))


def main():
    Settings.set_chromosome_bits("exercise3", len(get_objects()))
    op = None
    while op != 5:
        print("\n\nIngrese la opción deseada:")
        print("1. Hallar la ruta más corta para recorrer todas las capitales desde una capital determinada utilizando una heurística")
        print("2. Hallar la ruta más corta para recorrer todas las capitales utilizando una heurística")
        print("3. Hallar la ruta más corta para recorrer todas las capitales utilizando un Algorimo Genético")
        print("4. Hallar la ruta más corta para recorrer todas las capitales utilizando un Algorimo Genético y una heurística y comparar resultados")
        print("5. Salir")
        op = input(">")
        if op == "5":
            return
        if op == "1":
            option1()
        if op == "2":
            option2()
        if op == "3":
            option3()
        if op == "4":
            option4()

def show(time, best_city, distancia, route):
    print("Ciudad Inicial: {}".format(best_city))
    print("Distancia Total: {}".format(distancia))
    print("Ruta: {}".format(", ".join(route)))
    print("Tiempo de ejecucion: {0:.6f}".format(time))

if __name__ == '__main__':
    import exercise3.api as api
    import exercise3.greedy as greedy
    from base.logic.settings_manager import Settings
    import exercise3.maps as maps
    main()
