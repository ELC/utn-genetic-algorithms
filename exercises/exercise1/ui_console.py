"""Console View"""

class Console():
    """Console Presentation View"""
    status = "ACTIVE"

    @classmethod
    def menu(cls):
        menu_factory = Menu_Builder()
        menu = menu_factory.build()
        menu.execute()

    @classmethod
    def close(cls):
        cls.status = "CLOSED"

    def execute(self):
        Algorithm()

    def full_report(self):
        self.generations_report()

    def generations_report(self):
        data = Settings.load_results()
        data_pd = self.__get_data_frame(data)

        gens = [i for i, _ in enumerate(data)]

        data_frame = pd.DataFrame.from_items(data_pd, orient='index', columns=gens)
        data_frame_int = data_frame.astype(int)

        print(data_frame_int)

    def __get_data_frame(self, data):
        datas = self.__get_array_data(data)
        labels = ("Máximo", "Mínimo", "Promedio", "Mínimos cuadrados", "Rango")
        return [(i, j) for i, j in zip(labels, datas)]

    def __get_array_data(self, data):
        maximums = [i.maximum for i in data]
        minimums = [i.minimum for i in data]
        averages = [i.average for i in data]
        leasts = [i.least for i in data]
        ranges = [i.range for i in data]
        return (maximums, minimums, averages, leasts, ranges)


    def __header_legacy(self):
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

    def show_settings(self):
        """Show basic Configurations."""
        settings = Settings.load_all_settings()
        print(pd.Series(settings))

if __name__ == "__main__":
    import pandas as pd
    from settings import Settings
    from algorithm import Algorithm
    from ui_console_menu_builder import Menu_Builder
    console = Console()
    console.menu()
else:
    import pandas as pd
    from settings import Settings
    from algorithm import Algorithm
    from ui_console_menu_builder import Menu_Builder
