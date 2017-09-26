from itertools import chain, combinations

# Busqueda exhaustiva
import exercise3.logic.target as target
import timeit

objetos = target.generate_objects(default=True)

def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

def execute():
    start_time = timeit.default_timer()

    nro_objetos = objetos.keys()

    resultados = []
    for item in powerset(nro_objetos):
        lista = []
        for i in item:
            lista.append(objetos[i])
        value = target.value_of(lista)
        if value != 0:
            resultados.append([item, value])

    resultados.sort(key=lambda l: l[1], reverse=True)

    elementos, precio = resultados[0]

    volumen = target.sum_of(elementos, 0)

    total_time = timeit.default_timer() - start_time

    obj = ", ".join(str(i) for i in sorted(elementos))

    return total_time, obj, volumen, precio
