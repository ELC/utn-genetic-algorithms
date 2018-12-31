"""Console View"""


def main():
    menus = {}

    menus["1. Principal"] = {
        "Ejecutar": execute,
    }

    menus["2. Reporte"] = {
        "Reporte Completo": full_report,
        "Reporte de Generaciones": generations_report,
    }

    menus["3. Grafico"] = {
        "Graficar Maximos, minimos y promedios": graphic_min_max_mean,
        "Graficar Rango": graphic_range,
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


def execute():
    Controller.execute()
    full_report()


def _border(printable_string):
    border = "#" * len(printable_string)
    string = border + "\n" + printable_string + "\n" + border + "\n"
    print(string)


def full_report():
    """Print all the reports"""
    print("La configuración usada fue:")

    show_settings()

    generations_report()

    _border("La solucion final es: " + str(Controller.get_solution_report()))

    _border("Valor Cromosoma: " + str(Controller.get_decimal_value_report()))

    _border("Tiempo de ejecucion (s): " +
            str(Controller.get_execution_time()))


def generations_report():
    """Print the report of the generations"""
    print("Generaciones: \n" + str(Controller.get_generation_report()))


def show_settings():
    print(Controller.show_settings())


"""########"""
"""Graphics"""
"""########"""


def graphic_min_max_mean():
    maximums = pm.get_maximums()
    averages = pm.get_averages()
    minimums = pm.get_minimums()
    graphics(datas=(maximums, averages, minimums),
             labels=["Máximo", "Promedio", "Minimo"])


def graphic_range():
    graphics(datas=[pm.get_ranges()], labels=["Rangos"])


def graphic_t():
    graphics(datas=[pm.get_totals()], labels=["Totales"])


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

    from exercise1.logic.population_manager import PopulationController
    from exercise1.logic.controller import Controller
    from exercise1.util.graphic import graphics

    pm = PopulationController

    main()
