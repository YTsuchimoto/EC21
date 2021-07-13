import random
# GA library
from deap import base
from deap import creator
from deap import tools
from deap import algorithms


def EvalKnapsack(individual):
    """
    目的関数の定義
    各個体の価値と重量を計算する
    """
    weight = 0.0
    value = 0.0
    for i in range(6):
        weight += items[i][0]*individual[i]
        value += items[i][1]*individual[i]
    # if weight >= 100, value = 0
    if weight > 100:
        value = 0.0
    return value,


# 品物（重さ,価値）
items = {}
items[0] = (5, 110)
items[1] = (10, 140)
items[2] = (9, 160)
items[3] = (5, 130)
items[4] = (5, 110)
items[5] = (4, 90)

# 最大化問題として定義
creator.create("FitnessMax", base.Fitness, weights=(1.0,))
# 個体の定義
creator.create("Individual", list, fitness=creator.FitnessMax)

# toolboxの設定
toolbox = base.Toolbox()
# random.uniformの別名をattribute関数として定義
# 各個体の遺伝子の中身を決める関数(各遺伝子は0～10のランダムな整数)
toolbox.register("attribute", random.randint, 0, 10)
# individualという関数を設定
# それぞれの個体に含まれる6個の遺伝子をattributeにより決めるよ、ということ
toolbox.register("individual", tools.initRepeat, creator.Individual,
                 toolbox.attribute, 6)
# 集団の個体数を設定するための関数を準備
toolbox.register("population", tools.initRepeat, list, toolbox.individual)
# トーナメント方式で次世代に子を残す親を決定
toolbox.register("select", tools.selTournament, tournsize=5)
# 交叉関数の設定，一点交叉を採用
toolbox.register("mate", tools.cxOnePoint)
# 突然変異関数の設定
toolbox.register("mutate", tools.mutUniformInt, low=0, up=20, indpb=0.2)
# 目的関数を定義
toolbox.register("evaluate", EvalKnapsack)

# パラメータ
NGEN = 100  # 世代数
POP = 10000  # 集団の個体数
CXPB = 0.9  # 交叉率
MUTPB = 0.1  # 個体が突然変異を起こす確率
pop = toolbox.population(n=POP)  # 個体数を設定

# GAの実行
# 集団内の個体それぞれの適応度（目的関数の値）を計算
for ind in pop:
    ind.fitness.values = toolbox.evaluate(ind)

# 良い結果の個体をhofという変数に格納
hof = tools.ParetoFront()
# 適用するアルゴリズム
algorithms.eaSimple(pop, toolbox, cxpb=CXPB, mutpb=MUTPB, ngen=NGEN,
                    halloffame=hof)
# 最後の集団から最も適応度の高い個体を1個選ぶ関数
best_ind = tools.selBest(pop, 1)[0]

print("best result:  {}\tvalue:  {}".format(best_ind, best_ind.fitness.values))
