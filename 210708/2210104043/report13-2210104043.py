import random
from copy import deepcopy
from deap import base, creator, tools

IND_SIZE = 10  # 遺伝子長
POP = 10  # 個体数
NGEN = 100  # 世代数
CXPB = 0.9  # 交叉確率
MUTPB = 0.1  # 突然変異確率


def MyMut(individual, indpb):
    init_index = random.randint(0, len(individual)-1)
    individual[(init_index + 3) % len(individual)] = random.randint(0, 1)
    individual[(init_index + 3 + 3) % len(individual)] = random.randint(0, 1)
    individual[(init_index + 3 + 3 + 4) % len(individual)] = random.randint(0, 1)
    # for i in range(len(individual)):
    #     if random.random() < indpb:
    #         individual[i] = random.randint(0, 1)
    return individual,

def eval(individual):
    return sum(individual),

creator.create("FitnessMax", base.Fitness, weights=(1.0,))
creator.create("Individual", list, fitness=creator.FitnessMax)
toolbox = base.Toolbox()
toolbox.register("attribute", random.random)
toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attribute, n=IND_SIZE)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)
toolbox.register("mate", tools.cxTwoPoint)
toolbox.register("mutate", MyMut, indpb=0.1)
toolbox.register("select", tools.selTournament, tournsize=3)
toolbox.register("evaluate", eval)


def main():
    pop = toolbox.population(n=POP)
    print(pop)

    fitnesses = list(map(toolbox.evaluate, pop))

    # 評価
    for ind, fit in zip(pop, fitnesses):
        ind.fitness.values = fit

    for i in range(NGEN):
        print("Generation : {}/{}".format(i+1, NGEN))

        # 選択
        pop2 = toolbox.select(pop, len(pop))
        pop2 = list(map(toolbox.clone, pop2))

        # 交叉
        for child1, child2 in zip(pop2[::2], pop2[1::2]):
            if random.random() < CXPB:
                toolbox.mate(child1, child2)
                del child1.fitness.values
                del child2.fitness.values

        # 突然変異
        for mutant in pop2:
            if random.random() < MUTPB:
                toolbox.mutate(mutant)
                del mutant.fitness.values

        invalid_ind = [ind for ind in pop2 if not ind.fitness.valid]
        fitnesses = map(toolbox.evaluate, invalid_ind)
        for ind, fit in zip(invalid_ind, fitnesses):
            ind.fitness.values = fit

        pop[:] = pop2
        fits = [ind.fitness.values[0] for ind in pop]

        print("Min: {}".format(min(fits)))
        print("Max: {}".format(max(fits)))

    print("----------")
    best_ind = tools.selBest(pop, 1)[0]
    print("Best individual : {}, Best score : {}".format(best_ind, best_ind.fitness.values[0]))

if __name__ == '__main__':
    main()