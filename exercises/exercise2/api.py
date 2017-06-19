"""API"""

def execute():
    Controller.execute()
    execution_time = Controller.get_execution_time()
    last_pop = population_manager.get_last_population("Exercise2")

    best_gene_string = last_pop.get_max_gene_string()

    elementos = target.get_indexes(best_gene_string)
    volumen = target.sum_of(elementos, 0)
    price = target.sum_of(elementos, 1)

    obj = ", ".join(str(i) for i in elementos)

    return execution_time, obj, volumen, price

if __name__ == '__main__':
    import exercise2.logic.controller as Controller
    execute()
else:
    import exercise2.logic.controller as Controller
    import exercise2.logic.target as target
    import base.logic.population_manager as population_manager