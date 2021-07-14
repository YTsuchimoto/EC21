# -*- coding: utf-8 -*-
"""
Created on Tue Jun  1 09:45:27 2021

@author: 2210104029 kondo iori
"""

import math
import itertools
import copy

#100以下の素数を求める
S=[]

for i in range(2,100):
    flag = 0
    for j in range(2,i//2+1):
        if (i%j==0):
            flag=1
            break
    if flag == 0:
        S.append(i)
print(S)
print(len(S))

S_sum=sum(S)
print(S_sum)

#集合SAとSBの差の最小値を求める
value=0
min_value=2000
value_abs=0
SA=[]
SB=[]
SA_sum=0
SA_fin=[]

for i in range(1,len(S)//2+1):
    for pair in itertools.combinations(S,i): #Sの要素i個による組み合わせ全パターン取得
        SA=copy.copy(list(pair))
        SA_sum=sum(SA)
        value=2*SA_sum-S_sum #SA-SB=SA-(S-SA)=2SA-S
        value_abs=abs(value)
        if min_value>value_abs:
            min_value=value_abs
            SA_fin=copy.copy(SA)

for i in S:
    flag=0
    for j in SA_fin:
        if(i==j):
            flag=1
            break
    if flag == 0:
        SB.append(i)
   
print("SAとSBの差の絶対値の最小値")
print(min_value)
print("その時のSAとSB")
print("SA:",SA_fin)
print("SB:",SB)
