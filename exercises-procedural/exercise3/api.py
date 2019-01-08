"""API"""

def execute():
    Controller.execute()
    execution_time = Controller.get_execution_time()
    last_pop = population_manager.get_last_population("Exercise3")

    number_generations = last_pop.generation

    best_gene_string = last_pop.get_max_gene_string()

    cities = target.get_cities_from_array(best_gene_string)
    distance = target.get_distance_from_cities(cities)

    show_settings()

    return execution_time, cities[0], distance, cities, number_generations


def show_settings():
    """Show basic Configurations."""
    print(Controller.show_settings())

def generations_report():
    """Print the report of the generations"""
    print("Informe por generacion:")
    generation_data = Controller.get_generation_report()
    print(generation_data)

if __name__ == '__main__':
    import exercise3.logic.controller as Controller
    execute()
else:
    from exercise3.main import calc_distance_beetween_cities
    import exercise3.logic.controller as Controller
    import exercise3.logic.target as target
    import base.logic.population_manager as population_manager