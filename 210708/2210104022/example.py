from SPX import *

import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from deap import base
from deap import benchmarks
from deap import creator
from deap import tools

D = 3
N = 100
RANGE = 5.12

creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
creator.create("Individual", list, fitness=creator.FitnessMin)

toolbox = base.Toolbox()

toolbox.register("attr_float", random.uniform, -RANGE, RANGE)
toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_float, D)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)
toolbox.register("evaluate", benchmarks.rastrigin)
toolbox.register("mate", cxSimplexCrossoverBounded, low=-RANGE, up=RANGE)
toolbox.register("mutate", tools.mutPolynomialBounded, low=-RANGE, up=RANGE, indpb=1 / D, eta=20)
toolbox.register("select", tools.selBest, k=N)


def main():
    stats = tools.Statistics(key=lambda ind: ind.fitness.values)
    stats.register("avg", np.mean)
    stats.register("std", np.std)
    stats.register("best", np.min)
    logbook = tools.Logbook()
    logbook.header = ['nevals'] + stats.fields

    random.seed(64)
    pop = toolbox.population(n=N)
    CXPB, MUTPB = 1.0, 1.0
    maxEval = 10000

    nevals = 0

    fitness = list(map(toolbox.evaluate, pop))
    for ind, fit in zip(pop, fitness):
        ind.fitness.values = fit
    nevals = nevals + len(pop)

    record = stats.compile(pop)
    logbook.record(nevals=nevals, **record)

    g = 0
    while nevals <= maxEval:
        g = g + 1

        ofs = []
        for i in range(N):
            parents = random.sample(pop, D + 1)
            child = None

            if random.random() < CXPB:
                child = toolbox.mate(parents)

            if random.random() < MUTPB and child is not None:
                toolbox.mutate(child)

            if child is not None:
                ofs.append(creator.Individual(child))

        fitness = map(toolbox.evaluate, ofs)
        for ind, fit in zip(ofs, fitness):
            ind.fitness.values = fit
        nevals = nevals + len(ofs)
        pop.extend(ofs)

        pop = toolbox.select(pop)

        record = stats.compile(pop)
        logbook.record(nevals=nevals, **record)

    return pop, logbook


if __name__ == '__main__':
    _, log = main()
    data = pd.DataFrame(log)
    data.plot(x='nevals', y=['avg', 'best'])
    plt.xlabel('# of evaluations')
    plt.ylabel('fitness')
    plt.legend()
    plt.show()
    plt.savefig('result.png')
