#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import math
from deap import base
from deap import creator
from deap import tools
import random


creator.create("FitnessMax", base.Fitness, weights = (1.0,))    #適合度の定義

creator.create("Individual", list, fitness = creator.FitnessMax)  #個体の定義

toolbox = base.Toolbox()
toolbox.register("attr_bool", random.randint, 0, 1)
toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_bool, n = 10)
 #個体長10
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

def evaluate(individual):
    return sum(individual),

toolbox.register("evaluate", evaluate)
toolbox.register("mutate", tools.mutFlipBit, indpb=0.5)
        #突然変異率50%
toolbox.register("select", tools.selTournament, tournsize=1)




ind1 = toolbox.population(n = 1)     #初期個体生成
#print(ind1)

for i in range(100):
    #print("Generation " + str(i))

    ind2 = toolbox.select(ind1, len(ind1))
    ind2 = list(map(toolbox.clone, ind2))

    #mutant = toolbox.clone(ind1)
    #ind2, = toolbox.mutate(mutant)
    #del mutant.fitness.values
    for mutant in ind2:
        toolbox.mutate(mutant)
        del mutant.fitness.values

    #print(list(map(toolbox.evaluate, ind1)))

    eva_ind1 = list(map(toolbox.evaluate, ind1))
    eva_ind2 = list(map(toolbox.evaluate, ind2))
    if eva_ind1 < eva_ind2:
        ind1 = ind2
        print(eva_ind2)
    else:
        print(eva_ind1)
