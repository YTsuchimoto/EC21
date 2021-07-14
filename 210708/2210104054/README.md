# 2210104054　中島悠太
## Elite crossover
（世代の平均値）×（定数）×（世代の標準偏差）＜（個体の適応度）により，個体がエリートであるかを評価する．
```python
def evalElite(individual, mean, std, eliteP):
    if sum(individual) > mean * eliteP * std:
        return True
    else:
        return False

```
* 両親がエリートである　→　二点交叉
* 片親がエリートである　→　確率で二点交叉あるいは一様交叉
* エリートでない　→　一様交叉
```python
for child1, child2 in zip(offspring[::2], offspring[1::2]):
    #両親がエリートである
    if toolbox.isElite(child1, mean, std, eliteP) and toolbox.isElite(child2, mean, std, eliteP):
        toolbox.mate(child1, child2)
        del child1.fitness.values
        del child2.fitness.values
    #両方がエリートでない
    elif not toolbox.isElite(child1, mean, std, eliteP) and toolbox.isElite(child2, mean, std, eliteP):
        toolbox.uniform(child1, child2, CXPB)
        del child1.fitness.values
        del child2.fitness.values
    #片親だけがエリートである
    else:
        if random.random() < CXPB:
            toolbox.mate(child1, child2)
        else:
            toolbox.uniform(child1, child2, CXPB)
        del child1.fitness.values
        del child2.fitness.values      
```
## How to execute
```
$ python ga_oneMaxProblem.py
```
## results
20ループを回した結果，実装したアルゴリズムのほうが速く収束した．
* 2点交叉のみ
```
Best individual is [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1], (91.0,)
```
* 今回の実装
```
Best individual is [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], (99.0,)
```