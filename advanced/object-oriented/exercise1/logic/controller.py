"""Controller module"""


class Controller():
    total_time = 0

    @classmethod
    def execute(cls):
        start_time = timeit.default_timer()
        cls._execute()
        Controller.total_time = timeit.default_timer() - start_time

    @staticmethod
    def _execute():
        """Start the process of evolution."""
        PopulationController.reset_populations()
        generations = Settings.get_generations()

        next_generation = Population()
        for _ in range(generations-1):
            PopulationController.add_population(next_generation)
            actual_generation = next_generation
            actual_generation.evolve()
            next_generation = actual_generation.get_next_generation()
            convergence = next_generation.get_range()
            if convergence == 0:
                break

        PopulationController.add_population(next_generation)

    @staticmethod
    def show_settings():
        return pd.Series(Settings.load_all_settings())

    @staticmethod
    def get_generation_report():
        return Report.generations_report()

    @staticmethod
    def get_solution_report():
        return Report.solution_report()

    @staticmethod
    def get_execution_time():
        return Controller.total_time

    @staticmethod
    def get_decimal_value_report():
        population = PopulationController.get_last_population()
        gene_string = population.get_max_gene_string()
        return int(gene_string, 2)


if __name__ != '__main__':

    import timeit

    from exercise1.logic.report import Report
    from exercise1.logic.population_manager import PopulationController
    from exercise1.entities.population import Population
    from exercise1.logic.settings_manager import Settings

    import pandas as pd
