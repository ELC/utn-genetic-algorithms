"""Target Function"""

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

def target(gene_string):
    """Define a Target function."""
    objects = []
    for i, j in enumerate(gene_string):
        if j == "1":
            objects.append(objetos[i+1])
    return value_of(objects)

def value_of(subset):
    acum_vol = 0
    acum_pre = 0
    for objeto in subset:
        acum_vol += objeto[0]
        acum_pre += objeto[1]
        if acum_vol > 4200:
            return 0
    return acum_pre