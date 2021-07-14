import random
import numpy

from deap import tools, base, creator, algorithms

# Special mutation and evaluation operators
def mutate_one_up_down(individual, indpb):
    for idx, val in enumerate(individual):
        if random.random() <= indpb:
            # Do mutation
            if random.random() < 0.5:
                individual[idx] -= 1
            else:
                individual[idx] += 1
    return individual,

def evaluate(individual):
    return sum(individual),

# Create Individual type
creator.create("FitnessMax", base.Fitness, weights=(1.0,))
creator.create("Individual", list, fitness=creator.FitnessMax)

# Population initialization rules
toolbox = base.Toolbox()
toolbox.register("attr", random.randint, -1, 1)
toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr, n=10)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

# Set genetic functions
toolbox.register("evaluate", evaluate)
toolbox.register("mate", tools.cxTwoPoint)
toolbox.register("mutate", mutate_one_up_down, indpb=0.2)
toolbox.register("select", tools.selTournament, tournsize=2)

def main():
    pop = toolbox.population(n=20)
    hof = tools.HallOfFame(1)
    stats = tools.Statistics(lambda ind: ind.fitness.values)
    stats.register("avg", numpy.mean)
    stats.register("min", numpy.min)
    stats.register("max", numpy.max)

    pop, logbook = algorithms.eaSimple(pop, toolbox, cxpb=0.5, mutpb=0.2, ngen=20,
                                       stats=stats, halloffame=hof, verbose=True)
    return pop, logbook, hof


if __name__ == "__main__":
    pop, logbook, hof = main()
    print("Best: %s" % hof[0])
