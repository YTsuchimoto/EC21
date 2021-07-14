import random

from deap import base
from deap import creator
from deap import tools

IND_SIZE = 10  # 遺伝子長

creator.create("FitnessMax", base.Fitness, weights=(1.0,))
creator.create("Individual", list, fitness=creator.FitnessMax)

toolbox = base.Toolbox()
toolbox.register("attribute", random.random)
toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attribute, n=IND_SIZE)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

def evaluate(individual):
    return sum(individual),

# ランダムな点を一様分布から生成された乱数に置き換える
def mutOnePoint_uniform(individual, indpb):
    for i in range(len(individual)):
        if random.random() < indpb:
            individual[i] = random.uniform(0, 1)
    return individual,

toolbox.register("mate", tools.cxTwoPoint)
toolbox.register("mutate", mutOnePoint_uniform, indpb=0.1)
toolbox.register("select", tools.selTournament, tournsize=3)
toolbox.register("evaluate", evaluate)

def main():
    POP = 10  # 個体数
    NGEN = 100  # 世代数
    CXPB = 0.9  # 交叉確率
    MUTPB = 0.1  # 個体の突然変異確率

    print("Start of evolution")

    pop = toolbox.population(n=POP)
    print(pop)

    fitnesses = list(map(toolbox.evaluate, pop))

    # 評価
    for ind, fit in zip(pop, fitnesses):
        ind.fitness.values = fit

    print("Evaluated {} individuals".format(len(pop)))
    for i in range(NGEN):
        print("Generation {}".format(i))

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

        # print(pop2)
        print("Evaluated {} individuals".format(len(invalid_ind)))

        pop[:] = pop2
        fits = [ind.fitness.values[0] for ind in pop]

        print("Min: {}".format(min(fits)))
        print("Max: {}".format(max(fits)))

    print("End of evolution")
    best_ind = tools.selBest(pop, 1)[0]
    print("Best individual is {}, {}".format(best_ind, best_ind.fitness.values))

if __name__ == '__main__':
    main()