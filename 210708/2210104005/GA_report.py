# -*- coding: utf-8 -*-



from deap import base
from deap import creator
from deap import tools
import random


def cxTwoPoint_New(ind1, ind2): #二点交叉の固定されていない遺伝子座について一様交叉を行う
    size = min(len(ind1), len(ind2))
    cxpoint1 = random.randint(1, size)
    cxpoint2 = random.randint(1, size - 1)
    if cxpoint2 >= cxpoint1:
        cxpoint2 += 1
    else: # Swap the two cx points
        cxpoint1, cxpoint2 = cxpoint2, cxpoint1
    
    for i in range(cxpoint2-cxpoint1):
        if random.random()<0.5:
            ind1[cxpoint1+i],ind2[cxpoint1+i]=ind2[cxpoint1+i],ind1[cxpoint1+i]
        
    return ind1, ind2

creator.create("FitnessMax", base.Fitness, weights=(1.0,))#適合度
creator.create("Individual", list, fitness=creator.FitnessMax)#固体

toolbox = base.Toolbox()

toolbox.register("attr_bool", random.randint, 0, 1)
toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_bool, 50)#固体の長さを決める
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

def eval(individual):
    return sum(individual),

toolbox.register("evaluate", eval)
toolbox.register("mate", cxTwoPoint_New)
toolbox.register("mutate", tools.mutFlipBit, indpb=0.5)#indpb:遺伝子座の突然変異の確立
toolbox.register("select", tools.selTournament, tournsize=3)#tournsizeはトーナメントのサイズ


def main():
    random.seed(64)
    pop = toolbox.population(n=100)#個体数を決めて初期固体を作成
    cx=0.5#交叉の確立
    mut=0.2#各個体で突然変異を行うかの確立
    gen=20#世代数
    
    print("Start")

    fitnesses = list(map(toolbox.evaluate, pop))
    for ind, fit in zip(pop, fitnesses):
        ind.fitness.values = fit
    
    for g in range(gen):
        print("-- Generation {} --" .format(g))
        
        offspring = toolbox.select(pop, len(pop))
        offspring = list(map(toolbox.clone, offspring))

        for child1, child2 in zip(offspring[::2], offspring[1::2]):
            if random.random() < cx:
                toolbox.mate(child1, child2)
                del child1.fitness.values
                del child2.fitness.values
        #交叉処理

        for mutant in offspring:
            if random.random() < mut:
                toolbox.mutate(mutant)
                del mutant.fitness.values
        #突然変異処理
    
        invalid_ind = [ind for ind in offspring if not ind.fitness.valid]
        fitnesses = map(toolbox.evaluate, invalid_ind)
        for ind, fit in zip(invalid_ind, fitnesses):
            ind.fitness.values = fit
        #交叉と突然変異で変化した固体について適応度の再計算
        
        pop[:] = offspring#世代交代
        
        fits = [ind.fitness.values[0] for ind in pop]#平均計算用
        
        length = len(pop)#個体数
        mean = sum(fits) / length#適応度の平均
        
        print("Min:{}".format(min(fits)))
        print("Max:{}".format(max(fits)))
        print("Mean:{}".format(mean))
    
    print("GA END")
    
    best_ind = tools.selBest(pop, 1)[0]
    print("Best individual:{}".format(best_ind))
    print("Best Fit:{}".format(best_ind.fitness.values))
    
if __name__=="__main__":
    main()