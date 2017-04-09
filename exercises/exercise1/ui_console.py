"""Console View"""

class Console():
    """Console Presentation View"""

    @classmethod
    def main(cls):
        menu = cls.__create_menu()
        menu.execute()

    @staticmethod
    def __create_menu():
        return Menu_Builder.build()

    @classmethod
    def execute(cls):
        Algorithm()
        cls.full_report()

    @classmethod
    def full_report(cls):
        cls.generations_report()
        cls.solution_report()

    @classmethod
    def generations_report(cls):
        data = Settings.load_results()
        data_pd = cls.__get_data_frame(data)

        gens = [i for i, _ in enumerate(data)]

        data_frame = pd.DataFrame.from_items(data_pd, orient='index', columns=gens)
        data_frame_int = data_frame.astype(int)

        print(data_frame_int)

    @staticmethod
    def solution_report():
        data = Settings.load_results()
        last_population = data[-1]
        solution = last_population.maximum
        print("La solución final es: {}".format(solution))

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

if __name__ == "__main__":
    import pandas as pd
    from settings import Settings
    from algorithm import Algorithm
    from ui_console_menu_builder import Menu_Builder
    Console.main()
if __name__ != "__main__":
    import pandas as pd
    from settings import Settings
    from algorithm import Algorithm
    from ui_console_menu_builder import Menu_Builder
