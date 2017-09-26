from math import sin, cos, sqrt, atan2, radians
import itertools
import timeit
import random

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

def main(n=23,minimum=7166):
    start_time = timeit.default_timer()
    cities = sorted(i for i in provinces.keys())
    considered_cities = [city for city in get_cities(cities, n)]
    distances = list(i for i in (get_paired_cities(cities, provinces, minimum) for cities in considered_cities) if i > 0)
    
    for i, j in zip(considered_cities,distances):
        print(i, j)
    if len(distances) == 0:
        return tuple()
    
    minimum_distance = min(i for i in distances if i != 0)
    index = distances.index(minimum_distance)
    print("Posibilidades: ", factorial(23, n))
    print("Cantidad de rutas posibles: ", len(distances))
    print("Distancia minima: ", minimum_distance)
    print("Ciudades con distancia minima: ", considered_cities[index])
    total_time = timeit.default_timer() - start_time
    print("Total tiempo: ", "{0:.8f} segundos".format(total_time))
    return (tuple(considered_cities[index]), minimum_distance)
    

def factorial(start, x):
    f = 1
    base = start
    while start > base - x:
        f *= start
        start -=1
    return f

def get_cities(cities, per):
    base = [i for i in range(1,per)]
    i = 0
    while i < 30000:
        prox = base[:]
        random.shuffle(prox)
        prox.insert(0,0)
        yield [cities[i] for i in prox]
        i += 1
    return

def get_paired_cities(cities, provinces_, minimum):
    pair_distances = 0
    for i in range(len(cities)-1):
        pair_distance = calc_distance(*provinces_[cities[i]], *provinces_[cities[i+1]])
        pair_distances += pair_distance
        if pair_distances > minimum:
            pair_distances = 0
            break
    return pair_distances

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

start_time = timeit.default_timer()
routes = set()
for i in range(200):
    result = main()
    if len(result) != 0:
        routes.add(result)
        print("\n")


print("\n\n Rutas más cortas:")
for i,j in routes:
    print(i,j)

total_time = timeit.default_timer() - start_time
print("Total tiempo: ", "{0:.8f} segundos".format(total_time))