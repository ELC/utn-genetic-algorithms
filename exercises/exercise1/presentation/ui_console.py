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
    generation_data = report.generations_report()
    print("Informe por generacion:")
    print(generation_data)

def solution_report():
    """Print the final solution"""
    solution_data = report.solution_report()
    solution_string = "La solucion final es: " + str(solution_data)
    solution_string_formatted = _border(solution_string)
    print(solution_string_formatted)

def show_settings():
    """Show basic Configurations."""
    settings = Settings.load_all_settings()
    print(pd.Series(settings))

def _updated_settings():
    print("\nLa nueva configuración es: ")
    show_settings()

def set_cross_over_prob():
    """Set the cross over probability"""
    actual_value = Settings.get_cross_over_prob()
    print("Valor actual: " + str(actual_value))
    value = input("Ingrese nuevo valor: ")
    float_value = float(value)
    Settings.set_cross_over_prob(float_value)
    _updated_settings()

def set_chromosome_bits():
    """Set the chromosome bits"""
    actual_value = Settings.get_chromosome_bits()
    print("Valor actual: " + str(actual_value))
    value = input("Ingrese nuevo valor: ")
    int_value = int(value)
    Settings.set_chromosome_bits(int_value)
    _updated_settings()

def set_generations():
    """Set the maximum amount of generations"""
    actual_value = Settings.get_generations()
    print("Valor actual: " + str(actual_value))
    value = input("Ingrese nuevo valor: ")
    int_value = int(value)
    Settings.set_generations(int_value)
    _updated_settings()

def set_mutation_prob():
    """Set the mutation probability"""
    actual_value = Settings.get_mutation_prob()
    print("Valor actual: " + str(actual_value))
    value = input("Ingrese nuevo valor: ")
    float_value = float(value)
    Settings.set_mutation_prob(float_value)
    _updated_settings()

def set_population_size():
    """Set the initial population size"""
    actual_value = Settings.get_population_size()
    print("Valor actual: " + str(actual_value))
    value = input("Ingrese nuevo valor: ")
    int_value = int(value)
    Settings.set_population_size(int_value)
    _updated_settings()

def set_elitism(): 
    """Set the elitism status""" 
    actual_value = Settings.get_elitism() 
    print("Valor actual: " + str(actual_value))
    value = input("Ingrese nuevo valor [1=True, 0=False]: ")
    boolean_value = value == "1"
    Settings.set_elitism(boolean_value) 
    _updated_settings()


if __name__ == "__main__":
    import pandas as pd
    from exercise1.logic.settings_manager import Settings
    import exercise1.logic.controller as Controller
    from exercise1.presentation.ui_console_menu_builder import build as menu_build
    import exercise1.logic.report as report
    main()

if __name__ != "__main__":
    import pandas as pd
    from exercise1.logic.settings_manager import Settings
    import exercise1.logic.controller as Controller
    from exercise1.presentation.ui_console_menu_builder import build as menu_build
    import exercise1.logic.report as report

