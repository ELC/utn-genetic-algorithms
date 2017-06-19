"""Target Function"""

import base.util.util as util

objetos = {
        1:[150, 20],
        2:[325, 40],
        3:[600, 50],
        4:[805, 36],
        5:[430, 25],
        6:[1200, 64],
        7:[770, 54],
        8:[60, 18],
        9:[930, 46],
        10:[353, 28],
        }

objetos2 = {
        1:[150, 20],
        2:[325, 40],
        3:[600, 50],
        4:[805, 36],
        5:[430, 25],
        6:[1200, 64],
        7:[770, 54],
        8:[60, 18],
        9:[930, 46],
        10:[353, 28],
        11:[150, 20],
        12:[325, 40],
        13:[600, 50],
        14:[805, 36],
        15:[430, 25],
        16:[1200, 64],
        17:[770, 54],
        18:[60, 18],
        19:[930, 46],
        20:[353, 28],
        }

def generate_objects(cant=None, firstmax=None, secondmax=None, default=False):
    if default:
        return  objetos
    # values = [[util.get_random_number(0, firstmax), util.get_random_number(0, secondmax)] for _ in range(cant)]
    # objetos = {i:j for i,j in zip(range(cant),values)}

def target(gene_string):
    """Define a Target function."""
    objects = from_binary_array_to_objets(gene_string)
    return value_of(objects)

def from_binary_array_to_objets(gene_string):
    objects = []
    for i, j in enumerate(gene_string):
        if j == "1":
            objects.append(objetos[i+1])
    return objects

def get_indexes(gene_string):
    indexes = []
    for i, j in enumerate(gene_string):
        if j == "1":
            indexes.append(i+1)
    return indexes

def value_of(subset):
    acum_vol = 0
    acum_pre = 0
    for objeto in subset:
        acum_vol += objeto[0]
        acum_pre += objeto[1]
        if acum_vol > 4200:
            return 0
    return acum_pre

def sum_of(subset, index):
    return sum(objetos[i][index] for i in subset)
