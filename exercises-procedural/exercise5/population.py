"""Population Class"""

def create_population(population_size, chromosome_size, objects, total):
    while True:
        population = [create_chromosome(chromosome_size) for i in range(population_size)]
        if sum(get_targets(population, objects, total)) != 0:
            return population
    

def create_chromosome(size):
    return util.get_random_number_string(size, binary=True)

def evolve(chromosomes, elitism, mutation_prob, cross_over_prob, objects, total):

    fathers = choose_fathers(chromosomes, elitism, objects, total)
    

    childs = cross_over(fathers, cross_over_prob)

    mutated_childs = mutate_population(childs, mutation_prob)

    if elitism:
        fittests_chromosomes = get_fittest_chromosomes(chromosomes, objects, total)
        mutated_childs.extend(fittests_chromosomes)
    
    return mutated_childs


def mutate(genes):
    amount_of_genes = len(genes)        
    index = util.get_random_number(0, amount_of_genes - 1)

    genes = list(genes)
    gene = genes[index]
    genes[index] = "1" if gene == "0" else "0"
    
    return "".join(genes)

def calc_target(genes, objects, total):
    indexes = calc_indexes(genes)
    return target_function(indexes, len(genes), objects, total)

def calc_indexes(genes):
    return [i for i, gene in enumerate(genes) if gene == "1"]

def get_targets(chromosomes, objects, total):
    return [calc_target(chromosome, objects, total) for chromosome in chromosomes]

def calc_probabilities(chromosomes, objects, total):
    targets = get_targets(chromosomes, objects, total)
    total = sum(targets)
    return [target / total for target in targets]

def choose_fathers(chromosomes, elitism, objects, total):
    number = len(chromosomes)

    if elitism:
        number -= 2

    probabilities = calc_probabilities(chromosomes, objects, total)
    
    return [util.choose_roulette(chromosomes, probabilities) for _ in range(number)]


def cross_over(fathers, cross_over_prob):
    couples = util.get_next_two(fathers)

    precision = util.get_precision(cross_over_prob)

    childs = []

    for (father1, father2) in couples:
        prob = util.get_random_prob(precision=precision)

        if cross_over_prob > prob:
            new_childs = cross_over_1_point(father1, father2)
        else:
            new_childs = father1, father2
        
        childs.extend(new_childs)
    
    return childs


def cross_over_1_point(father1, father2):
    length = len(father1)
    split_points = util.get_random_number(0, length)
    father1_gene_parts = split_chromosome(father1, split_points)
    father2_gene_parts = split_chromosome(father2, split_points)

    child1 = "".join((father2_gene_parts[0], father1_gene_parts[1]))
    child2 = "".join((father1_gene_parts[0], father2_gene_parts[1]))

    return child1, child2


def split_chromosome(chromosome, split_point):
    return [chromosome[:split_point], chromosome[split_point:]]


def mutate_population(chromosomes, mutation_prob):
    """Mutate each chromosome when appropiate"""

    precision = util.get_precision(mutation_prob)

    mutated_chromosomes = []

    for chromosome in chromosomes:
        prob = util.get_random_prob(precision=precision)
        if mutation_prob > prob:
            mutated_chromosomes.append(mutate(chromosome))
        else:
            mutated_chromosomes.append(chromosome)
    
    return mutated_chromosomes

def get_fittest_chromosomes(chromosomes, objects, total):
    """Return the two chromosome with the highest fitness value"""
    fitness = get_targets(chromosomes, objects, total)
    max_fitnesses = sorted(fitness, reverse=True)[:2]

    return [find_chromosome_by_fitness(chromosomes, maximum, objects, total) for maximum in max_fitnesses]

def get_fittest_chromosome(chromosomes, objects, total):
    fitness = get_targets(chromosomes, objects, total)

    return find_chromosome_by_fitness(chromosomes, max(fitness), objects, total)


def find_chromosome_by_fitness(chromosomes, fitness, objects, total):
    """Return the chromosome gene string with the given fitness"""
    for chromosome in chromosomes:
        if calc_target(chromosome, objects, total) == fitness:
            return chromosome

def get_volume(genes, objects):
    indexes = calc_indexes(genes)
    return sum(vol for i, (vol, _) in enumerate(objects) if i in indexes)

def get_price(genes, objects):
    indexes = calc_indexes(genes)
    return sum(price for i, (_, price) in enumerate(objects) if i in indexes)

def target_function(indexes, chromosome_size, objects, total):
    """Define a Target function."""
    acum_vol = 0
    acum_pre = 0
    for index in indexes:
        acum_vol += objects[index][0]
        acum_pre += objects[index][1]
        if acum_vol > total:
            return 0
    return acum_pre


if __name__ != "__main__":
    import exercise5.filemanager as FileManager
    import exercise5.util.util as util
