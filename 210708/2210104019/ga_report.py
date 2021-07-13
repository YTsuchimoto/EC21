


import random
import numpy as np

from deap import base, creator, tools

creator.create("FitnessMax", base.Fitness, weights=(1.0,))
creator.create("Individual", list, fitness=creator.FitnessMax)

toolbox = base.Toolbox()

Item_num = 100

toolbox.register("attr_bool", random.randint, 0, 1)
toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_bool, Item_num)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

def evalOneMax(individual):
    return sum(individual),

######### original pert #########
point_01list = [[0 for _ in range(Item_num)] for i in [0, 1]]

def new_mutete(individual):
    global point_01list
    before = [n for n in individual]
    point_list = [point_01list[item][i] for i, item in enumerate(individual)]
    # print("point_list", point_list)
    point_exp_list = np.exp(point_list)
    probability_list = [item / np.sum(point_exp_list) for item in point_exp_list]
    i = np.random.choice(Item_num, p=probability_list)
    individual[i] = 0 if individual[i] else 1
    after = individual
    # print("before", before)
    # print("after", after)
    point_01list[before[i]][i] += (evalOneMax(after)[0] - evalOneMax(before)[0])
    return after

#############################

toolbox.register("evaluate", evalOneMax)
toolbox.register("mate", tools.cxTwoPoint)
toolbox.register("mutate", new_mutete) # 突然変異を変更
toolbox.register("select", tools.selTournament, tournsize=3)


def main():
    random.seed(64)
    
    pop = toolbox.population(n=300)
    CXPB, MUTPB, NGEN = 0.5, 0.2, 40
    
    print("Start of evolution")

    fitnesses = list(map(toolbox.evaluate, pop))
    for ind, fit in zip(pop, fitnesses):
        ind.fitness.values = fit
    
    print(f"  Evaluated {len(pop)} individuals")
    
    for g in range(NGEN):
        print(f"-- Generation {g} --")
        
        offspring = toolbox.select(pop, len(pop))
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
        
        print("  Evaluated %i individuals" % len(invalid_ind))
        
        pop[:] = offspring
        
        fits = [ind.fitness.values[0] for ind in pop]
        
        length = len(pop)
        mean = sum(fits) / length
        sum2 = sum(x*x for x in fits)
        std = abs(sum2 / length - mean**2)**0.5
        
        print("  Min %s" % min(fits))
        print("  Max %s" % max(fits))
        print("  Avg %s" % mean)
        print("  Std %s" % std)
    
    print("-- End of (successful) evolution --")
    
    best_ind = tools.selBest(pop, 1)[0]
    print(f"Best individual is {best_ind}, {best_ind.fitness.values}")

if __name__ == "__main__":
    main()
