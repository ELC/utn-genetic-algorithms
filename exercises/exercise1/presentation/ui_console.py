"""Console View"""

def main():
    menu = menu_build()
    menu.execute()

def execute():
    Controller.execute()
    full_report()

def _border(printable_string):
    border = "#" * len(printable_string)
    string = border + "\n" + printable_string + "\n" + border
    return string

def full_report():
    """Print all the reports"""
    print("La configuración usada fue:")
    show_settings()
    generations_report()
    solution_report()

def generations_report():
    """Print the report of the generations"""
    print("Informe por generacion:")
    generation_data = Controller.get_generation_report()
    print(generation_data)

def solution_report():
    """Print the final solution"""
    solution_data = Controller.get_solution_report()
    solution_string = "La solucion final es: " + str(solution_data)
    solution_string_formatted = _border(solution_string)
    print(solution_string_formatted)

def show_settings():
    """Show basic Configurations."""
    print(Controller.show_settings())

def _updated_settings():
    print("\nLa nueva configuración es: ")
    show_settings()

def set_cross_over_prob():
    """Set the cross over probability"""
    actual_value = Controller.get_cross_over_prob()
    print("Valor actual: " + str(actual_value))
    value = input("Ingrese nuevo valor: ")
    Controller.set_cross_over_prob(value)
    _updated_settings()

def set_chromosome_bits():
    """Set the chromosome bits"""
    actual_value = Controller.get_chromosome_bits()
    print("Valor actual: " + str(actual_value))
    value = input("Ingrese nuevo valor: ")
    Controller.set_chromosome_bits(value)
    _updated_settings()

def set_generations():
    """Set the maximum amount of generations"""
    actual_value = Controller.get_generations()
    print("Valor actual: " + str(actual_value))
    value = input("Ingrese nuevo valor: ")
    Controller.set_generations(value)
    _updated_settings()

def set_mutation_prob():
    """Set the mutation probability"""
    actual_value = Controller.get_mutation_prob()
    print("Valor actual: " + str(actual_value))
    value = input("Ingrese nuevo valor: ")
    Controller.set_mutation_prob(value)
    _updated_settings()

def set_population_size():
    """Set the initial population size"""
    actual_value = Controller.get_population_size()
    print("Valor actual: " + str(actual_value))
    value = input("Ingrese nuevo valor: ")
    Controller.set_population_size(value)
    _updated_settings()

def set_elitism():
    """Set the elitism status"""
    actual_value = Controller.get_elitism()
    print("Valor actual: " + str(actual_value))
    value = input("Ingrese nuevo valor [1=True, 0=False]: ")
    Controller.set_elitism(value)
    _updated_settings()


if __name__ == "__main__":
    from exercise1.presentation.ui_console_menu_builder_alt import build as menu_build
    main()

if __name__ != "__main__":
    import exercise1.logic.controller as Controller
    from exercise1.presentation.ui_console_menu_builder_alt import build as menu_build

