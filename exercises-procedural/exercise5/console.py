"""Console View"""

def main():
    menus = {}

    menus["1. Principal"] = {
        "1. Ejecutar Greedy": execute_greedy,
        "2. Ejecutar Algoritmo Genético": execute_genetic,
        "3. Ejecutar Exahustiva": execute_exhausted,
        "4. Ejecutar Todas": execute_all,
    }

    menus["2. Reporte"] = {
        "Reporte Completo": full_report,
        "Reporte de Generaciones": generations_report,
    }

    menus["3. Grafico"] = {
        "Graficar Maximos, minimos y promedios": Report.graphic_min_max_mean,
        "Graficar Rango": Report.graphic_range,
        "Graficar Totales": Report.graphic_t,
    }

    menus["4. Configuracion"] = {
        "Mostrar configuracion actual": show_settings,
    }

    show_menu(menus)


def show_menu(menu):
    available_options = [str(i) for i in range(len(menu)+1)]

    while True:
        clear_screen()

        for item in sorted(menu):
            print(item)

        print("0. Salir")

        option = input('Ingrese una opción: ')

        if not option in available_options:
            continue

        option = int(option)

        if option == 0:
            return

        selected_option = sorted(menu)[option - 1]

        show_submenu(menu[selected_option])


def show_submenu(submenu):
    available_options = [str(i) for i in range(len(submenu)+1)]

    while True:
        clear_screen()

        for index, item in enumerate(submenu):
            print(f"{index + 1}. {item}")

        print("0. Volver")

        option = input('Ingrese una opción: ')

        if not option in available_options:
            continue

        option = int(option)

        if option == 0:
            return

        selected_option = sorted(submenu)[option - 1]

        print()
        submenu[selected_option]()
        print()

        input("Presione Enter para continuar")

def execute_greedy():
    print("\nGreedy: ")

    objects = load_settings()["objects"]
    total = load_settings()["total_vol"]

    start_time = timeit.default_timer()
    elementos, volumen, price = greedy.execute(objects, total)
    total_time = timeit.default_timer() - start_time

    print("Objetos: ", elementos)
    print("Volumen final: ", volumen)
    print("Precio final: ", price)
    print("Tiempo de ejecucion una vez: {0:.6f}".format(total_time))

def execute_exhausted():
    print("\nExhaustiva: ")

    objects = load_settings()["objects"]
    total = load_settings()["total_vol"]

    start_time = timeit.default_timer()
    elementos, volumen, price = exhaustiva.execute(objects, total)
    total_time = timeit.default_timer() - start_time

    print("Objetos: ", elementos)
    print("Volumen final: ", volumen)
    print("Precio final: ", price)
    print("Tiempo de ejecucion una vez: {0:.6f}".format(total_time))

def execute_genetic():
    execution_time = Controller.execute()
    full_report(execution_time)

def execute_genetic_custom():
    print("\nAlgoritmo Genético: ")

    objects = load_settings()["objects"]
    total_vol = load_settings()["total_vol"]

    execution_time = Controller.execute()

    objects, volume = Report.best_gene()

    print("Objetos: ", str(objects))
    print("Volumen final: ", volume)
    print("Precio final: ", str(Report.solution_report(objects, total_vol)))
    print("Tiempo de ejecucion una vez: {0:.6f}".format(execution_time))



def execute_all():
    execute_greedy()    
    execute_genetic_custom()
    execute_exhausted()


def execute_times_by_user():
    n = int(input("Cuantas ejecuciones: "))
    execute_n_times(n)

def execute_n_times(n):
    show_settings()

    print("\nEjecutando...\n")

    for i in range(n):
        execution_time = Controller.execute()
        Controller.get_generation_report(execution_time)
        print("Ejecución {}/{} Terminada".format(i + 1, n))


def _border(printable_string):
    border = "#" * len(printable_string)
    string = border + "\n" + printable_string + "\n" + border + "\n"
    print(string)


def full_report(execution_time):
    """Print all the reports"""
    print("La configuración usada fue:")

    objects = load_settings()["objects"]
    total_vol = load_settings()["total_vol"]

    show_settings()

    generations_report(execution_time)

    _border("La solucion final es: " + str(Report.solution_report(objects, total_vol)))

    _border("Valor Cromosoma: " + str(Report.best_gene()))

    _border("Tiempo de ejecucion (s): " + str(execution_time))


def generations_report(execution_time):
    """Print the report of the generations"""
    print("Generaciones: \n" + str(Report.generations_report(execution_time)))


def show_settings():
    print(Controller.show_settings())


"""####"""
"""Util"""
"""####"""


def clear_screen():
    if system_name().lower() == "windows":
        command = "cls"
    else:
        command = "clear"

    system_call(command)


if __name__ == "__main__":
    from os import system as system_call
    from platform import system as system_name
    import exercise5.controller as Controller
    from exercise5.util.report import Report
    from exercise5 import exhaustiva
    from exercise5 import greedy
    from exercise5.filemanager import load_settings
    import timeit
    
    main()
