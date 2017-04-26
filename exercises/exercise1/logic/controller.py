"""Controller module"""

def execute():
    """Start the process of evolution."""
    population_manager.reset_populations()
    generations = Settings.get_generations()
    next_generation = Population()
    for i in range(generations):
        population_manager.add_population(next_generation)
        actual_generation = next_generation
        actual_generation.evolve()
        next_generation = actual_generation.get_next_generation()
        convergence = next_generation.get_range()
        if convergence == 0:
            break
    population_manager.add_population(next_generation)


if __name__ != '__main__':
    import exercise1.logic.population_manager as population_manager
    from exercise1.entities.population import Population
    from exercise1.logic.settings_manager import Settings
