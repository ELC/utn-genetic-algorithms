"""API"""

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

if __name__ == '__main__':
    import exercise1.logic.controller as Controller
    import pandas as pd
    import exercise1.logic.report as report
    import exercise1.logic.population_manager as population_manager
    from exercise1.entities.population import Population
    from exercise1.logic.settings_manager import Settings
    execute()