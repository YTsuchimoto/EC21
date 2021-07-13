import random

from deap import base
from deap import creator
from deap import tools

IND_SIZE = 5

def TriCrossOver(ind1, ind2, ind3):
    for i in range(len(ind1)):
        rand = random.random()
        if rand < 1./3:
            pass
        elif rand < 2./3:
            tmp = ind1[i]
            ind1[i] = ind2[i]
            ind2[i] = ind3[i]
            ind3[i] = tmp
        else:
            tmp = ind1[i]
            ind1[i] = ind3[i]
            ind3[i] = ind2[i]
            ind2[i] = tmp

creator.create("FitnessMin", base.Fitness, weights=(-1.0, -1.0))
creator.create("Individual", list, fitness=creator.FitnessMin)

toolbox = base.Toolbox()
toolbox.register("attr_float", random.random)
toolbox.register("individual", tools.initRepeat, creator.Individual,
                 toolbox.attr_float, n=IND_SIZE)

toolbox.register("TriCO", TriCrossOver)

ind1 = toolbox.individual()
ind2 = toolbox.individual()
ind3 = toolbox.individual()

print("=====parents=====")
print(ind1)
print(ind2)
print(ind3)
child1, child2, child3 = [toolbox.clone(ind) for ind in (ind1,ind2,ind3)]
toolbox.TriCO(child1, child2, child3)

print("=====chlids=====")
print(child1)
print(child2)
print(child3)
