"""Console View"""

class Console():
    """Console Presentation View"""

    @staticmethod
    def clear_screen():
        """Clears the terminal screen."""
        if system_name().lower() == "windows":
            command = "cls"
        else:
            command = "clear"

        system_call(command)

    @classmethod
    def main(cls):
        menu = cls.__create_menu()
        menu.execute()

    @staticmethod
    def __create_menu():
        return Menu_Builder.build()

    @classmethod
    def execute(cls):
        """Execute the main algorithm and show the report"""
        Algorithm()
        cls.full_report()

    @classmethod
    def full_report(cls):
        """Show all the reports"""
        cls.generations_report()
        cls.solution_report()

    @classmethod
    def generations_report(cls):
        """Show the generations report"""
        data = Settings.load_results()
        data_pd = cls.__get_data_frame(data)

        gens = [i for i, _ in enumerate(data)]

        data_frame = pd.DataFrame.from_items(data_pd, orient='index', columns=gens)
        data_frame_int = data_frame.astype(int)

        print("Reporte detallado por generacion:\n")
        print(data_frame_int)
        print()

    @classmethod
    def solution_report(cls):
        """Show the final solution infered from the generations"""
        data = Settings.load_results()
        last_population = data[-1]
        solution = last_population.maximum
        solution_string = "La solución final es: {}".format(solution)
        cls.__border(solution_string)


    @staticmethod
    def __border(printable_string):
        border = "#" * len(printable_string)
        print(border)
        print(printable_string)
        print(border)


    @classmethod
    def __get_data_frame(cls, data):
        datas = cls.__get_array_data(data)
        labels = ("Máximo", "Mínimo", "Promedio", "Mínimos cuadrados", "Rango")
        return [(i, j) for i, j in zip(labels, datas)]

    @staticmethod
    def __get_array_data(data):
        maximums = [i.maximum for i in data]
        minimums = [i.minimum for i in data]
        averages = [i.average for i in data]
        leasts = [i.least for i in data]
        ranges = [i.range for i in data]
        return (maximums, minimums, averages, leasts, ranges)

    @staticmethod
    def __header_legacy():
        """Show basic Configurations."""
        settings = Settings.load_all_settings()
        population_size = settings["population_size"]
        cross_over_prob = settings["cross_over_prob"]
        mutation_prob = settings["mutation_prob"]
        generations = settings["generations"]
        report = settings["report"]
        print("##########################################")
        print("Población inicial: {}".format(population_size))
        print("Probabilidad de CrossOver: {}".format(cross_over_prob))
        print("Probabilidad de mutacion: {}".format(mutation_prob))
        print("Numero de generaciones maximas: {}".format(generations))
        print("Mostrar reporte: {}".format(report))
        print("##########################################")
        print()

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
    from platform import system as system_name
    from os import system as system_call
    from settings import Settings
    from algorithm import Algorithm
    from ui_console_menu_builder import Menu_Builder

    Console.main()
if __name__ != "__main__":
    import pandas as pd
    from os import system as system_call
    from platform import system as system_name
    from settings import Settings
    from algorithm import Algorithm
    from ui_console_menu_builder import Menu_Builder
