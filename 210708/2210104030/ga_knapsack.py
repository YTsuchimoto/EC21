import random

import numpy as np
from deap import algorithms
from deap import base
from deap import creator
from deap import tools

IND_INIT_SIZE = 5
MAX_ITEM = 50
MAX_WEIGHT = 50
NUM_ITEMS = 20

random.seed(42)

items = {}
for i in range(NUM_ITEMS):
    items[i] = (random.randint(1, 10), random.uniform(0, 100))

creator.create("Fitness", base.Fitness, weights=(-1.0, 1.0))
creator.create("Individual", set, fitness=creator.Fitness)

toolbox = base.Toolbox()
toolbox.register("attr_item", random.randrange, NUM_ITEMS)
toolbox.register("individual", tools.initRepeat, creator.Individual, 
                 toolbox.attr_item, IND_INIT_SIZE)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)


def evalKnapsack(individual):
    weight = 0.0
    value = 0.0
    for item in individual:
        weight += items[item][0]
        value += items[item][1]
    if len(individual) > MAX_ITEM or weight > MAX_WEIGHT:
        return 10000, 0
    return weight, value


def cxMySet(ind1, ind2):
    """Apply a crossover operation on input sets.

    Example
    Parents: {1, 2, 3}, {1, 3, 5}
    AND: {1, 3}
    XOR: {2, 5}
    Candidates of offsprings: {1, 3}, {1, 2, 3}, {1, 3, 5}, {1, 2, 3, 5}
    """
    tmp_and = set(ind1) & set(ind2)
    tmp_xor = set(ind1) ^ set(ind2)
    ind1 &= tmp_and
    ind1 ^= set(random.choices(list(tmp_xor),
                               k=random.randint(0, len(list(tmp_xor)))))
    ind2 &= tmp_and
    ind2 ^= set(random.choices(list(tmp_xor),
                               k=random.randint(0, len(list(tmp_xor)))))
    return ind1, ind2


def mutSet(individual):
    if random.random() < 0.5:
        if len(individual) > 0:
            individual.remove(random.choice(sorted(tuple(individual))))
    else:
        individual.add(random.randrange(NUM_ITEMS))
    return individual,


toolbox.register("evaluate", evalKnapsack)
toolbox.register("mate", cxMySet)
toolbox.register("mutate", mutSet)
toolbox.register("select", tools.selNSGA2)


def main():
    random.seed(42)
    NGEN = 50
    MU = 50
    LAMBDA = 100
    CXPB = 0.7
    MUTPB = 0.2

    pop = toolbox.population(n=MU)
    hof = tools.ParetoFront()
    stats = tools.Statistics(lambda ind: ind.fitness.values)
    stats.register("avg", np.mean, axis=0)
    stats.register("std", np.std, axis=0)
    stats.register("min", np.min, axis=0)
    stats.register("max", np.max, axis=0)

    algorithms.eaMuPlusLambda(pop, toolbox, MU, LAMBDA, CXPB, MUTPB, NGEN, stats,
                              halloffame=hof)

    return pop, stats, hof


if __name__ == "__main__":
    pop, stas, hof = main()
    print('Knapsack problem')
    print('Number  weight  value')
    for k, v in items.items():
        print(f'{k:2}     {v[0]:2}       {v[1]}')
    print(f'Hall of fame: {hof.items[-1]}')
