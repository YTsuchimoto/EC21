from itertools import combinations
import numpy as np
import copy

#素数を数え上げる
prime_list = []
for i in range(2, 100):
    flag = 0
    for j in range(2, i//2+1):
        if(i % j == 0):
            flag = 1
            break
    if flag == 0:
        prime_list.append(i)

num = len(prime_list)
sub = sum_all = sum(prime_list)
#print(sum_all)

sa_list = []
sb_list = []

#組み合わせ全探索
for k in range(num+1):
    for comb in combinations(prime_list, k):
        #閾値より小さかったら残す
        if sub > abs((sum_all-sum(comb))-sum(comb)):
            sa_list.clear()
            for p in comb:
                sa_list.append(p)
            sub = abs((sum_all-sum(comb))-sum(comb))

print("SA>{}".format(sa_list))
for t in prime_list:
    if t not in sa_list:
        sb_list.append(t)
print("SB>{}".format(sb_list))
