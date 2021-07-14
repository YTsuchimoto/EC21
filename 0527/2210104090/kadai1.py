"""
1-100までの素数の集合をSとする．
SをSaとSbに分けたときそれぞれの要素の総和の差の絶対値の最小値とそのときのSaとSbを求めよ．
"""

import itertools

# 素数を生成
S = []
for i in range(2, 100):
    flag = 0
    for j in range(2, i // 2 + 1):
        if i % j == 0:
            flag = 1
            break
    if flag == 0:
        S.append(i)
print(S)

# 全通り調べる
sizeS = len(S)

absAns = []
SaAns = []
SbAns = []
absMin = 10000
for e in itertools.product([0, 1], repeat=sizeS):
    a = list(e)

    Sa = []
    Sb = []
    for i in range(0, sizeS):
        if a[i] == 0:
            Sa.append(int(S[i]))
        else:
            Sb.append(int(S[i]))
    tmp = abs(sum(Sa)-sum(Sb))
    if absMin > tmp:
        SaAns = []
        SbAns = []
        absAns = tmp
        SaAns.append(Sa)
        SbAns.append(Sb)
        absMin = tmp
    elif absMin == tmp:
        SaAns.append(Sa)
        SbAns.append(Sb)


# Saの回答(Sbの回答の同じインデックスに対応)
print(SaAns)
# Sbの回答(Saの回答の同じインデックスに対応)
print(SbAns)
# 最小値の回答
print(absAns)










