# Busqueda exhaustiva
from itertools import chain, combinations

def powerset(iterable):
    """Returns an iterable with all the subsets of the given parameter
    >>> powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"""
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

def fitness(lista, total):
    acum_vol = 0
    acum_pre = 0
    for objeto in lista:
        acum_vol += objeto[0]
        acum_pre += objeto[1]
        if acum_vol > total:
            return 0
    return acum_pre

def execute(objetos, total):
    nro_objetos = list(range(len(objetos)))

    precio = 0
    for item in powerset(nro_objetos):
        lista = (objetos[i] for i in item)
        value = fitness(lista, total)
        if value != 0 and value > precio:
            elementos = item
            precio = value

    volumen = sum(objetos[i][0] for i in elementos)

    obj = ", ".join(str(i) for i in sorted(elementos))

    return obj, volumen, precio