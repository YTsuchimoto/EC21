import random
import numpy as np
from deap import algorithms
from deap import base
from deap import creator
from deap import tools

from myOperator import selMyOperator

NUM_ITEMS = 10 # 品物の種類数
MAX_WEIGHT = 10 # 各品物の最大重量
MAX_VALUE = 100 # 各品物の最大価値
MAX_NUM = 10 # 各品物の最大数
MAX_SUM_WEIGHT = 150 # 最大重量

items = {}
for i in range(NUM_ITEMS):
    items[i] = (random.randint(1, MAX_WEIGHT), random.randint(0, MAX_VALUE))

def evalKnapsack(individual):
    weight = 0.0
    value = 0.0
    for i in range(NUM_ITEMS):
        weight += items[i][0]*individual[i]
        value += items[i][1]*individual[i]
    if weight > MAX_SUM_WEIGHT:
        value=0.0
    return [value, weight]

def main():
    random.seed(100)
    NGEN = 50 # 世代数
    POP = 15000 # 個体数
    CXPB = 0.9 # 交叉率
    MUTPB = 0.1 # 突然変異率
    TOURNSIZE = 10

    creator.create("FitnessMax", base.Fitness, weights=(1.0,))
    creator.create("Individual", list, fitness=creator.FitnessMax)

    toolbox = base.Toolbox()
    toolbox.register("attr_item", random.randint, 0, MAX_NUM)
    toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_item, NUM_ITEMS)
    toolbox.register("population", tools.initRepeat, list, toolbox.individual)

    toolbox.register("evaluate", evalKnapsack)
    toolbox.register("select", selMyOperator, tournsize=TOURNSIZE, fit_attr=toolbox.evaluate, attr='max')
    toolbox.register("mate", tools.cxUniform, indpb=0.5)
    toolbox.register("mutate", tools.mutUniformInt, low=0, up=10, indpb=0.2)

    pop = toolbox.population(n=POP)
    hof = tools.ParetoFront()
    stats = tools.Statistics(lambda ind: ind.fitness.values)
    stats.register("avg", np.mean, axis=0)
    stats.register("std", np.std, axis=0)
    stats.register("min", np.min, axis=0)
    stats.register("max", np.max, axis=0)

    algorithms.eaSimple(pop, toolbox, CXPB, MUTPB, NGEN, stats, halloffame=hof)

    return hof


if __name__ == "__main__":
    hof = main()
    print('Knapsack problem')
    for k, v in items.items():
        print('Number:{:3} weight = {:3} value = {:3}'.format(k, v[0], v[1]))
    print('Hall of fame: {}'.format(hof.items[-1]))
    print('value = {}, weight = {}'.format(evalKnapsack(hof.items[-1])[0], evalKnapsack(hof.items[-1])[1]))

#2210104016
