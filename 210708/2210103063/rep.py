import numpy as np, random
from copy import deepcopy
from deap import algorithms, base, creator, tools

n_gene = 100
n_individuals = 1000
n_generations = 1000

p_cxpb = 0.5
p_mutpb = 0.2
p_mutate = 0.05

n_tournsize = 3

def evalOneMax(individual):
  return sum(individual),

def init_creator():
  creator.create("FitnesMax", base.Fitness, weights = (1.0,))
  creator.create("Individual", np.ndarray, fitness=creator.FitnesMax)
  return creator

def my_gene_generator(min, max):
    return random.randint(min, max)

def init_generator(creator):
  toolbox = base.Toolbox()
  toolbox.register("attr_bool", my_gene_generator, 0, 1)
  toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_bool, n_gene)
  toolbox.register("population", tools.initRepeat, list, toolbox.individual)
  return toolbox

def my_mutate(individual, indpb):
  ret = deepcopy(individual)
  for i in range(1,len(individual)-1):
    if random.random() < indpb:
      c = individual[i-1]+individual[i]*2+individual[i+1]*4
      if c == 1 or c == 3 or c == 4 or c == 6:
        ret[i] = 1
      else:
        ret[i] = 0
        
  return ret,

def operator_registration(toolbox):
  toolbox.register("evaluate", evalOneMax)
  toolbox.register("mate", tools.cxTwoPoint)
  toolbox.register("mutate", my_mutate, indpb=p_mutate)
  toolbox.register("select", tools.selTournament, tournsize=n_tournsize)

def stats_register():
  stats = tools.Statistics(lambda ind: ind.fitness.values)
  stats.register("avg", np.mean)
  stats.register("std", np.std)
  stats.register("min", np.min)
  stats.register("max", np.max)
  return stats

def get_cxpoint(size):
  cxpoint1 = random.randint(1, size)
  cxpoint2 = random.randint(1, size - 1)
  if cxpoint2 >= cxpoint1:
    cxpoint += 1
  else:
    cxpoint1, cxpoint2 = cxpoint2, cxpoint1
  return cxpoint1, cxpoint2

def cxTwoPointCopy(ind1, ind2):
  size = min(len(ind1), len(ind2))
  cxpoint1, cxpoint2 = get_cxpoint(size)

  ind1[cxpoint1:cxpoint2], ind2[cxpoint1:cxpoint2] \
    = ind2[cxpoint1:cxpoint2].copy(), ind1[cxpoint1:cxpoint2].copy()

  return ind1, ind2

def set_seed(seed=0):
  random.seed(seed)

if __name__ == "__main__":
  creator = init_creator()
  toolbox = init_generator(creator)
  operator_registration(toolbox)

  set_seed()
  pop = toolbox.population(n=n_individuals)
  hof = tools.HallOfFame(1, similar=np.array_equal)
  stats = stats_register()
  algorithms.eaSimple(pop, toolbox, cxpb=p_cxpb, mutpb=p_mutpb, ngen = n_generations, stats=stats, halloffame=hof)
  best_ind = tools.selBest(pop, 1)[0]
  print("Best individual is \n Eval:\n  %s, \n Gene:\n  %s" % (best_ind.fitness.values, best_ind))


