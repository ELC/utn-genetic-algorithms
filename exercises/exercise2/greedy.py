# Metodo Greedy
import exercise2.logic.target as target
import timeit
from itertools import takewhile

objetos = target.generate_objects(default=True)

def execute():
    start_time = timeit.default_timer()

    valor_precio = [(i, k[1]/k[0]) for i, k in objetos.items()]

    valor_precio.sort(key=lambda k: k[1], reverse=True)

    nro_objetos = (i for i, _ in valor_precio)

    acum_vol = 0
    resultados = []
    for nro_objeto in nro_objetos:
        if acum_vol + objetos[nro_objeto][0] <= 3000:
            acum_vol += objetos[nro_objeto][0]
            resultados.append(nro_objeto)
        else:
            break

    volumen = target.sum_of(resultados, 0)
    price = target.sum_of(resultados, 1)
    total_time = timeit.default_timer() - start_time

    obj = ", ".join(str(i) for i in sorted(resultados))

    return total_time, obj, volumen, price