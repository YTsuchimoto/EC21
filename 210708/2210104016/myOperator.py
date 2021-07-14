import random
import copy
import math

def selMyOperator(individuals, k, tournsize, fit_attr, attr='max'):
    '''
    tournsize - The number of individuals participating in each tournament.
    fit_attr – The attribute of individuals to use as selection criterion.
    attr - Set up the problem (maximization problem : max, minimization problem : min).

    '''

    new_individuals = copy.deepcopy(individuals)
    g = list(range(k))

    for _ in range(math.floor(k / tournsize)):
        select = random.sample(g, tournsize)
        fitness = []
        for individual in select:
            fitness.append(fit_attr(individuals[individual]) + [individual])
            g.remove(individual)

        fitness = sorted(fitness, key=lambda x:(x[0], -x[1]), reverse=True if attr=='max' else False)

        for individual in select:
            if individual == fitness[0][1]:
                continue
            for gene in range(len(individuals[0])):
                for x in range(tournsize):
                    if (random.randint(0, 2) == 1):
                        new_individuals[individual][gene] = individuals[fitness[x][-1]][gene]
                        break

    return new_individuals

#2210104016
