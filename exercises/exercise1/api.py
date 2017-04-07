"""API"""

class Api():

    @staticmethod
    def execute():
        Algorithm()

    @staticmethod
    def export_results():
        results = Settings.load_results
        return results

    @staticmethod
    def export_settings():
        settings = Settings.load_all_settings()
        return settings

    @staticmethod
    def set_cross_over_prob(value):
        Settings.set_cross_over_prob(value)

    @staticmethod
    def set_individual_bits(value):
        Settings.set_individual_bits(value)

    @staticmethod
    def set_generations(value):
        Settings.set_generations(value)

    @staticmethod
    def set_mutation_prob(value):
        Settings.set_mutation_prob(value)

    @staticmethod
    def set_population_size(value):
        Settings.set_population_size(value)

    @staticmethod
    def set_report(value):
        Settings.set_report(value)


if __name__ != "__main__":
    from settings import Settings
    from algorithm import Algorithm
