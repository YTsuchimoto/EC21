import random
import deap
from deap import base
from deap import creator
from deap import tools

creator.create("FitnessMax", base.Fitness, weights=(1.0,))  # 適合度
creator.create("Individual", list, fitness=creator.FitnessMax)

toolbox = base.Toolbox()

toolbox.register("attr_int", random.randint, 0, 1)  # 各遺伝子座は0か1の値を取る
toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_int, 20)  # 長さは20
toolbox.register("population", tools.initRepeat, list, toolbox.individual)


# ある遺伝子座が突然変異時、各遺伝子座で多数決を取る
def tasuketsu(individual, indpb):
    a = b = 0
    for i in range(len(individual)):
        if individual[i] == 1:
            a = a + 1
        else:
            b = b + 1

    if a < b:
        individual[random.randint(0, len(individual) - 1)] = 0
    else:
        individual[random.randint(0, len(individual) - 1)] = 1

    return individual,


def eval(individual):
    return sum(individual),


toolbox.register("evaluate", eval)
toolbox.register("mate", tools.cxTwoPoint)
toolbox.register("mutate", tasuketsu, indpb=0.1)  # 多数決を行う突然変異　確率は0.1
toolbox.register("select", tools.selTournament, tournsize=2)


def main():
    oya = toolbox.population(n=10)  # 個体数は10

    fitnesses = list(map(toolbox.evaluate, oya))
    for ind, fit in zip(oya, fitnesses):
        ind.fitness.values = fit

    for i in range(100):  # 100回以下を繰り返す
        print("{} iteration".format(i))

        ko = list(map(toolbox.clone, toolbox.select(oya, len(oya))))  # 選択

        for ko1, ko2 in zip(ko[::2], ko[1::2]):
            if random.random() < 0.5:  # 50%の確率で交叉
                toolbox.mate(ko1, ko2)
                del ko1.fitness.values
                del ko2.fitness.values

        for mutant in ko:
            if random.random() < 0.2:  # 20%の確率で突然変異
                toolbox.mutate(mutant)
                del mutant.fitness.values

        invalid_ind = [ind for ind in ko if not ind.fitness.valid]
        fitnesses = map(toolbox.evaluate, invalid_ind)
        for ind, fit in zip(invalid_ind, fitnesses):
            ind.fitness.values = fit
        # 適応度を計算

        oya[:] = ko  # 子から親へ

        fits = [ind.fitness.values[0] for ind in oya]
        print("Min {}".format(min(fits)))  # 一番小さい適合度
        print("Max {}".format(max(fits)))  # 一番大きい適合度


if __name__ == '__main__':
    main()