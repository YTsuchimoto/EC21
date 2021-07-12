import random
from deap import algorithms, base, creator, tools

creator.create("FitnessMax", base.Fitness, weights=(1.0,))
creator.create("Individual", list, fitness=creator.FitnessMax)


# My new operator 
def newCross(indiv1, indiv2):
    # Selection of a random number of genes that we will swap
    nbChanges = random.randint(1,len(indiv1)-1)
    # Generate nbChanges random index of the genes we will swap 
    listofChanges = random.sample(range(0,len(indiv1)), nbChanges)
    # Swaping for each index
    for index in listofChanges:
        indiv1[index], indiv2[index] = indiv2[index], indiv1[index]
    
    return indiv1, indiv2



def evalOneMax(individual):
    return (sum(individual),)



toolbox = base.Toolbox()
toolbox.register("attr_bool", random.randint, 0, 1)
toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_bool, n=100)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)
toolbox.register("evaluate", evalOneMax)
toolbox.register("mate", newCross)
toolbox.register("mutate", tools.mutFlipBit, indpb=0.05)
toolbox.register("select", tools.selTournament, tournsize=3)

if __name__ == "__main__":
    pop = toolbox.population(n=300)
    algorithms.eaSimple(pop, toolbox, cxpb=0.5, mutpb=0.2, ngen=40, verbose=False)
    print(tools.selBest(pop, k=1))