"""API"""

class Api():
    """Manage the program from outside"""

    @staticmethod
    def execute():
        """Execute the main algorithm"""
        Algorithm()

    @staticmethod
    def export_results():
        """Get the results for the previous run"""
        results = Settings.load_results()
        return results

    @staticmethod
    def export_settings():
        """Get the settings"""
        settings = Settings.load_all_settings()
        return settings

    @staticmethod
    def set_cross_over_prob(value):
        """Set the cross over probability"""
        Settings.set_cross_over_prob(value)

    @staticmethod
    def set_individual_bits(value):
        """Set the individual bits probability"""
        Settings.set_individual_bits(value)

    @staticmethod
    def set_generations(value):
        """Set the generations probability"""
        Settings.set_generations(value)

    @staticmethod
    def set_mutation_prob(value):
        """Set the mutation probability"""
        Settings.set_mutation_prob(value)

    @staticmethod
    def set_population_size(value):
        """Set the initial population size"""
        Settings.set_population_size(value)

    @staticmethod
    def set_report(value):
        """Set the report status"""
        Settings.set_report(value)

if __name__ != "__main__":
    from settings import Settings
    from algorithm import Algorithm
