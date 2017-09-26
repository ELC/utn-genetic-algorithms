# Smopy Imports
import smopy

# Basemap Imports
from mpl_toolkits.basemap import Basemap

import matplotlib.pyplot as plt

# Greedy Imports
from math import sin, cos, sqrt, atan2, radians
import itertools


northermost_lat = -21
southernmost_lat = -56
eastermost_long = -53
westermost_long = -75

provinces = {
    #"rosario":(-32.95, -60.65),
    "Buenos Aires":(-34.599722, -58.381944),
    "Córdoba":(-31.416667, -64.183333),
    #"la_plata":(-34.933333, -57.95),
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

GOOGLE = True

import urllib.request, json

def calc_distance(lat1, lon1, lat2, lon2, google=None):
    if google is None:
        return calc_distance_harversine(lat1, lon1, lat2, lon2)
    return get_distance_from_google_maps(lat1,lon1,lat2,lon2)

def get_distance_from_google_maps(lat1,lon1,lat2,lon2):
    url = "https://maps.googleapis.com/maps/api/distancematrix/"
    query_string = "json?origins={},{}&destinations={},{}".format(lat1,lon1,lat2,lon2)
    with urllib.request.urlopen(url+query_string) as url:
        data = json.loads(url.read().decode())
    distance_meters = data['rows'][0]['elements'][0]['distance']['value']
    return distance_meters / 1000

def calc_distance_harversine(_lat1, _lon1, _lat2, _lon2):
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


def plot_capital_cities(my_map, conversion_func):
    """Plot Capital Cities"""
    for lat, lon in provinces.values():
        x, y = conversion_func(lon, lat)
        my_map.plot(x, y, 'bo', markersize=2)

def get_vertexes(cities, conversion_func, inverse=False):
    """Convert cities into vertexes groups"""
    vertexes = []
    for city in cities:
        lat, lon = provinces[city]
        if inverse:
            vertex = conversion_func(lon, lat)
        else:
            vertex = conversion_func(lat, lon)
        vertexes.append(vertex)
    return vertexes

def plot_lines_from_vertexes(vertexes, my_map):
    """Plot lines between vertexes"""
    for i in range(len(vertexes)-1):
        x1, y1 = vertexes[i]
        x2, y2 = vertexes[i+1]
        my_map.plot([x1, x2], [y1, y2], color='m', linestyle='-', linewidth=1.5)


def main(cities):
    map = smopy.Map(southernmost_lat+6, westermost_long, northermost_lat-3, eastermost_long-4)

    fig, ax = plt.subplots(figsize=(20, 10))
    
    my_map = map.show_mpl()

    plot_capital_cities(my_map, map.to_pixels)
        
    cities = cities

    vertexes = get_vertexes(cities, map.to_pixels)

    plot_lines_from_vertexes(vertexes, my_map)

    ax.savefig("greedy-google.jpg", dpi=100)