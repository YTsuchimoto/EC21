#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 11 15:06:48 2021

@author: m.yuta
"""
import random

from deap import base
from deap import creator
from deap import tools

N = 300


creator.create("FitnessMax", base.Fitness, weights=(1.0,))#適応度
creator.create("Individual", list, fitness=creator.FitnessMax)#個体

toolbox = base.Toolbox()

#遺伝子生成
toolbox.register("attr_bool",random.randint,0,1)
#個体生成（遺伝子の長さ＝１０）
toolbox.register("individual",tools.initRepeat,creator.Individual,toolbox.attr_bool,100)
#世代生成
toolbox.register("population",tools.initRepeat,list,toolbox.individual)

def evalOneMax(individual):
    return sum(individual),

#0となる遺伝子座のうち、一箇所を強制的に1に変化させる操作
def New_mutate(individual):
    flag = 0
    
    while(flag == 0):
        i = random.randint(1,1000) % N
        
        while(i < len(individual)):
            if individual[i] == 0:
                individual[i] = 1
                flag = 1
                break;
            else:
                i = i + 1
        
        if i > len(individual):
            break;
                 
    return individual

toolbox.register("evaluate",evalOneMax)
toolbox.register("mate",tools.cxTwoPoint)#交叉
toolbox.register("mutate",tools.mutFlipBit,indpb=0.05)#突然変異
toolbox.register("select",tools.selTournament,tournsize=3)#選択
toolbox.register("newoperation",New_mutate)#提案操作

        
def main():
    random.seed(32)
    
    pop = toolbox.population(n=N)#個体数
    NGEN = 100 #世代数
    CXPB = 0.5 #交叉確率
    MUTPB = 0.2 #突然変異確率

    print("Start of evolution")

    fitnesses = list(map(toolbox.evaluate, pop))
    
    for ind, fit in zip(pop, fitnesses):
        ind.fitness.values = fit
    
    print("  Evaluated %i individuals" % len(pop))

    for g in range(NGEN):
        print("-- Generation %i --" % g)

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
                
        toolbox.newoperation(tools.selWorst(offspring,1)[0])
        del tools.selWorst(offspring,1)[0].fitness.values
                
                
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
    
    print("Best individual is %s, %s" % (best_ind, best_ind.fitness.values))
    
    
if __name__ == "__main__":
    main()




