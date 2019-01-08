# Metodo Greedy
import timeit

def execute(objetos, total):
    valor_precio = [(i, price / vol) for i, (vol, price) in enumerate(objetos)]

    valor_precio.sort(key=lambda k: k[1], reverse=True)

    acum_vol = 0
    acum_price = 0
    resultados = []

    for cod_objeto, _ in valor_precio:

        if acum_vol + objetos[cod_objeto][0] >= total:
            break

        acum_vol += objetos[cod_objeto][0]
        acum_price += objetos[cod_objeto][1]
        resultados.append(cod_objeto)

    obj = ", ".join(str(i) for i in sorted(resultados))

    return obj, acum_vol, acum_price