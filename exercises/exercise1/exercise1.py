from random import randint

init_population = 30
cross_over_prob = 0.9
mutation_prob = 0.001
generations = 1000
averages = []
maximums = []

def main():
    population = generate_bits_population(init_population)
    for i in range(generations):
        fitness_values = fitness(population, target)
        fitness_acumulated = acumulate_fitness(fitness_values)
        next_gen_fathers = choose_fathers(fitness_acumulated, population)
        couples = make_couples(next_gen_fathers)
        print("Generacion Nro {}".format(i))
        report(population)
        population = evaluate_crossover(couples)
        if len(set(population)) == 1:
            break
    print("Final Report")
    report(population)
    
    

def report(pop):
    average = sum(int(i,2) for i in pop) / len(pop)
    rounded_average = int(average)
    print("Promedio: {}".format(rounded_average))
    
    maximum = int(max(pop), 2)
    print("Maximo {}".format(maximum))
    print()

def evaluate_crossover(couples):
    childs = []
    for (i, j) in couples:
        prob = get_random_prob()
        if prob < cross_over_prob:
            child1, child2 = cross_over_n_points(i, j)
            childs.append(child1)
            childs.append(child2)
        else:
            childs.append(i)
            childs.append(j)
    return childs

def make_couples(fathers):
    couples = []
    amount = len(fathers) // 2
    for i in range(0,amount):
        couple = [fathers[i*2], fathers[i*2+1]]
        couples.append(couple)
    return couples   

def choose_fathers(acumulated, pop):
    amount = len(pop)
    fathers = []
    for _ in range(amount):
        prob = get_random_prob()
        index = find_bigger(acumulated, prob)
        individual = pop[index]
        fathers.append(individual)
    return fathers

def find_bigger(array, value):
    for i,j in enumerate(array):
        if value <= j:
            return i
    raise MYError

def acumulate_fitness(fit):
    acum = []
    last = 0
    for i in fit:
        last += i
        acum.append(last)
    if acum[-1] != 1:
        acum[-1] = 1
    return acum

def fitness(pop, tar):
    dec_pop = [int(i, 2) for i in pop]
    target_pop = [tar(x) for x in dec_pop]
    total = sum(target_pop)
    fitness_pop = [i / total for i in target_pop]
    return fitness_pop

def target(x):
    return x ** 2

def generate_bits_population(size, n=10):
    maximum = 2 ** n - 1
    random_seeds = (randint(0, maximum) for _ in range(size))
    random_bits = (dec_bin(x) for x in random_seeds)
    bits_population = fill(random_bits, n)
    return bits_population

def dec_bin(x):
    return bin(x)[2:]

def fill(raw, n, neutral="0"):
    filled = []
    for i in raw:
        data = list(i)
        while len(data) < n:
            data.insert(0, neutral)
        next_number = "".join(data)
        filled.append(next_number)
    return filled

def get_random_prob(precision=2):
    toplimit = 10 ** precision
    percentage = randint(0,toplimit)
    prob = percentage / toplimit
    return prob

def cross_over_n_points(father1, father2, n=1):
    length = len(father1)
    split_points = get_split_points(n, length)
    father1_parts = split_in_parts(father1, split_points)
    father2_parts = split_in_parts(father2, split_points)
    child1, child2 = mix(father1_parts, father2_parts)
    return child1, child2
    

def get_split_points(n, length):
    split_points = []
    for _ in range(n):
        split_point = randint(0, length)
        split_points.append(split_point)
    return split_points

def split_in_parts(father, split_points):
    start = 0
    parts = []
    
    lenght = len(father)
    if split_points[-1] != lenght:
        split_points.append(lenght)
        
    for i in split_points:
        end = i
        part = father[start:end]
        parts.append(part)
        start = end
        
    return parts

def mix(father1, father2):
    child1 = []
    child2 = []
    joint = zip(father1, father2)
    for i, (f1, f2) in enumerate(joint):
        if i % 2 == 0:
            child1.extend(f1)
            child2.extend(f2)
        else:
            child1.extend(f2)
            child2.extend(f1)
    child1 = "".join(child1)
    child2 = "".join(child1)
    return child1, child2
    

main()