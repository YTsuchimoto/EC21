import random

from deap import base
from deap import creator
from deap import tools

creator.create("FitnessMax", base.Fitness, weights=(1.0,))
creator.create("Individual", list, fitness=creator.FitnessMax)

toolbox = base.Toolbox()

toolbox.register("attr_bool", random.randint, 0, 1)

toolbox.register("individual", tools.initRepeat, creator.Individual, 
    toolbox.attr_bool, 100)

toolbox.register("population", tools.initRepeat, list, toolbox.individual)

def evalOneMax(individual):
    return sum(individual),

toolbox.register("evaluate", evalOneMax)

toolbox.register("mate", tools.cxTwoPoint)

################################################################
#          今回新たに考えた突然変異　                              #
################################################################
def new_mut(individual,g,mean,indpb):
    #1世代目では突然変異率に初期値を与えて行う。今回は0.2とした。
    if g==1:
        for i in range(len(individual)):  
            if random.random() < indpb:
                individual[i] = type(individual[i])(not individual[i])
    #2世代目以降は適応度の平均により突然変異率を変化させている。
    #平均が小さいときは突然変異しやすく、平均が大きくなると突然変異しにくくしている。
    else:
        new_indpb=5/mean
        for i in range(len(individual)):  
            if random.random() < new_indpb:
                individual[i] = type(individual[i])(not individual[i])
        
    return individual,

toolbox.register("mutate", new_mut,indpb=0.2)

toolbox.register("select", tools.selTournament, tournsize=3)

def main():
    random.seed(64)

    pop = toolbox.population(n=300)

    CXPB, MUTPB = 0.5, 0.2
    
    print("Start of evolution")
    
    fitnesses = list(map(toolbox.evaluate, pop))
    for ind, fit in zip(pop, fitnesses):
        ind.fitness.values = fit
    
    print("  Evaluated %i individuals" % len(pop))

    fits = [ind.fitness.values[0] for ind in pop]

    g = 0
    mean=0
    while max(fits) < 100 and g < 1000:
        g = g + 1
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
                toolbox.mutate(mutant,g,mean)
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
    print("Best individual is %s, %s" % (best_ind, best_ind.fitness.values))

if __name__ == "__main__":
    main()