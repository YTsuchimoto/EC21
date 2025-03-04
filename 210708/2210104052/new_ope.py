import random
from deap import base, creator, tools
import numpy as np
import operator as op

def selRandom(individuals, k):
    return [random.choice(individuals) for i in range(k)]

def ada_Tournament(individuals, k, ave,pre_ave,tournsize, fit_attr="fitness"):
    chosen = []
    if ave > pre_ave:
        if tournsize > 2:
            tournsize = tournsize - 1
    elif ave == pre_ave:
        pass
    else:
        tournsize = tournsize + 1
    for i in range(k):
        aspirants = selRandom(individuals, tournsize)
        chosen.append(max(aspirants, key=op.attrgetter(fit_attr)))
    return chosen,tournsize

creator.create("FitnessMax", base.Fitness, weights=(1.0,))
creator.create("Individual", list, fitness=creator.FitnessMax)

toolbox = base.Toolbox()
# Attribute generator
toolbox.register("attr_bool", random.randint, 0, 1)
# Structure initializers
toolbox.register("individual", tools.initRepeat, creator.Individual,
    toolbox.attr_bool, 100)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

def evalOneMax(individual):
    return sum(individual),

toolbox.register("evaluate", evalOneMax)
toolbox.register("mate", tools.cxTwoPoint)
toolbox.register("mutate", tools.mutFlipBit, indpb=0.05)
toolbox.register("select", ada_Tournament)

def main():
    pop = toolbox.population(n=300)
    fitnesses = list(map(toolbox.evaluate, pop))
    for ind, fit in zip(pop, fitnesses):
        ind.fitness.values = fit
    CXPB, MUTPB = 0.5, 0.2

    fits = [ind.fitness.values[0] for ind in pop]

    g = 0
    #pre_ave = sum(fits) / len(fits)
    pre_ave = ind.fitness.values[0]
    tournsize = 5
    # Begin the evolution
    while max(fits) < 100 and g < 1000:
        # A new generation
        g = g + 1
        print("-- Generation %i --" % g)
          # Select the next generation individuals
        #ave =  sum(fits) / len(fits)
        ave = ind.fitness.values[0]
        print(ave,pre_ave)
        offspring,next_size = toolbox.select(pop, len(pop),ave,pre_ave,tournsize)
        pre_ave = ave

        tournsize = next_size
        print(tournsize)
        # Clone the selected individuals
        offspring = list(map(toolbox.clone, offspring))
        for child1, child2 in zip(offspring[::2], offspring[1::2]):
            if random.random() < CXPB:
                toolbox.mate(child1, child2)
                del child1.fitness.values
                del child2.fitness.values

        for mutant in offspring:
            if random.random() < MUTPB:
                toolbox.mutate(mutant)
                del mutant.fitness.values

        invalid_ind = [ind for ind in offspring if not ind.fitness.valid]
        fitnesses = map(toolbox.evaluate, invalid_ind)
        for ind, fit in zip(invalid_ind, fitnesses):
            ind.fitness.values = fit

        pop[:] = offspring
        print(ind.fitness.values[0])
        fits = [ind.fitness.values[0] for ind in pop]

    length = len(pop)
    mean = sum(fits) / length
    sum2 = sum(x*x for x in fits)
    std = abs(sum2 / length - mean**2)**0.5
    print("  Min %s" % min(fits))
    print("  Max %s" % max(fits))
    print("  Avg %s" % mean)
    print("  Std %s" % std)

if __name__ == "__main__":
    main()
