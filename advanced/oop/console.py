"""Console View"""


def main():
    menus = {}

    menus["1. Principal"] = {
        "Ejecutar": execute,
        "Ejecutar 10 veces": lambda: execute_n_times(10),
        "Ejecutar 30 veces": lambda: execute_n_times(30),
        "Ejecutar 50 veces": lambda: execute_n_times(50),
        "Ejecutar 100 veces": lambda: execute_n_times(100),
        "Ejecutar n veces": execute_times_by_user,
    }

    menus["2. Reporte"] = {
        "Reporte Completo": full_report,
        "Reporte de Generaciones": generations_report,
    }

    menus["3. Grafico"] = {
        "Graficar Maximos, minimos y promedios": Report.graphic_min_max_mean,
        "Graficar Rango": Report.graphic_range,
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


def execute_times_by_user():
    n = input("Cuantas ejecuciones: ")
    execute_n_times(n)


def execute_n_times(n):
    show_settings()

    print("\nEjecutando...\n")

    for i in range(n):
        Controller.execute()
        Report.generations_report()
        print("Ejecución {}/{} Terminada".format(i + 1, n))


def _border(printable_string):
    border = "#" * len(printable_string)
    string = border + "\n" + printable_string + "\n" + border + "\n"
    print(string)


def full_report():
    """Print all the reports"""
    print("La configuración usada fue:")

    show_settings()

    generations_report()

    _border("La solucion final es: " + str(Report.solution_report()))

    _border("Valor Cromosoma: " + str(Controller.get_decimal_value_report()))

    _border("Tiempo de ejecucion (s): " +
            str(Controller.get_execution_time()))


def generations_report():
    """Print the report of the generations"""
    print("Generaciones: \n" + str(Report.generations_report()))


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

    from oop.logic.population_manager import PopulationController
    from oop.logic.controller import Controller
    from oop.util.graphic import graphics
    from oop.util.report import Report
    from oop.data.filemanager import FileManager

    Report.FileManager = FileManager
    Report.Controller = Controller
    Report.Population = PopulationController

    pm = PopulationController

    main()
