"""Target Function"""

import base.util.util as util
import exercise2.main as main



def generate_objects(default=True):
    if default:
        return  main.get_objects()
    
def target(gene_string):
    """Define a Target function."""
    objects = from_binary_array_to_objets(gene_string)
    return value_of(objects)

def from_binary_array_to_objets(gene_string):
    objects = []
    for i, j in enumerate(gene_string):
        if j == "1":
            objects.append(main.get_objects()[i+1])
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
        if acum_vol > 3000:
            return 0
    return acum_pre

def sum_of(subset, index):
    return sum(main.get_objects()[i][index] for i in subset)
