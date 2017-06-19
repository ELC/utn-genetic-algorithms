def main():
    print("\nAlgoritmos geneticos: ")
    time, elementos, volumen, price = api.execute()
    show(time, elementos, volumen, price)

    print("\nExhaustiva: ")
    time, elementos, volumen, price = exhaustiva.execute()
    show(time, elementos, volumen, price)

    print("\nGreedy: ")
    time, elementos, volumen, price = greedy.execute()
    show(time, elementos, volumen, price)

def show(time, objets, volumen, price):
    print("Objetos: {}".format(objets))
    print("Precio final: {}".format(price))
    print("Volumen final: {}".format(volumen))
    print("Tiempo de ejecucion: {0:.6f}".format(time))

if __name__ == '__main__':
    import exercise2.api as api
    import exercise2.greedy as greedy
    import exercise2.exhaustiva as exhaustiva
    main()
