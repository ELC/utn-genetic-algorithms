"""Console View"""

class Console():
    """Console Presentation View"""

    @classmethod
    def main():
        menu = menu_build()
        menu.execute()

    @classmethod
    def execute():
        """Execute the main algorithm and show the report"""
        Algorithm()
        report.full_report()

    @staticmethod
    def __border(printable_string):
        border = "#" * len(printable_string)
        print(border)
        print(printable_string)
        print(border)


    @staticmethod
    def show_settings():
        """Show basic Configurations."""
        settings = Settings.load_all_settings()
        print(pd.Series(settings))


    @classmethod
    def __updated_settings(cls):
        print()
        print("La nueva configuración es: ")
        cls.show_settings()

    @classmethod
    def set_cross_over_prob(cls):
        """Set the cross over probability"""
        value = input("Ingrese nuevo valor: ")
        float_value = float(value)
        Settings.set_cross_over_prob(float_value)
        cls.__updated_settings()

    @classmethod
    def set_individual_bits(cls):
        """Set the individual bits"""
        value = input("Ingrese nuevo valor: ")
        int_value = int(value)
        Settings.set_individual_bits(int_value)
        cls.__updated_settings()

    @classmethod
    def set_generations(cls):
        """Set the maximum amount of generations"""
        value = input("Ingrese nuevo valor: ")
        int_value = int(value)
        Settings.set_generations(int_value)
        cls.__updated_settings()

    @classmethod
    def set_mutation_prob(cls):
        """Set the mutation probability"""
        value = input("Ingrese nuevo valor: ")
        float_value = float(value)
        Settings.set_mutation_prob(float_value)
        cls.__updated_settings()

    @classmethod
    def set_population_size(cls):
        """Set the initial population size"""
        value = input("Ingrese nuevo valor: ")
        int_value = int(value)
        Settings.set_population_size(int_value)
        cls.__updated_settings()

    @classmethod
    def set_report(cls):
        """Set the report status"""
        value = input("Ingrese nuevo valor [1=True, 0=False]: ")
        boolean_value = value == "1"
        Settings.set_report(boolean_value)
        cls.__updated_settings()


if __name__ == "__main__":
    import pandas as pd
    from exercise1.logic.settings import Settings
    from exercise1.logic.algorithm import Algorithm
    from exercise1.presentation.ui_console_menu_builder import build as menu_build
    import exercise1.logic.report as report
    Console.main()

if __name__ != "__main__":
    import pandas as pd
    from exercise1.logic.settings import Settings
    from exercise1.logic.algorithm import Algorithm
    from exercise1.presentation.ui_console_menu_builder import build as menu_build
    import exercise1.logic.report as report

