# -*- coding: utf-8 -*-
"""
Created on Sat May 29 16:40:41 2021

@author: akasa
"""
import itertools

#素数を求める
S=[]
for i in range(2,100):
    flag = 0
    for j in range(2,i//2+1):
        if(i%j == 0):
            flag = 1
            break
    if flag == 0:
        S.append(i)

#問題1を解く
temp=10000
for i in range(1,len(S)//2):
    for S_A in itertools.combinations(S,i):
        S_A=set(S_A)
        S_B=set(S)-S_A
        
    if(temp>abs(sum(S_A)-sum(S_B))):
        temp=abs(sum(S_A)-sum(S_B))
        min_S_A=S_A
        min_S_B=S_B
        
print('最小値:',temp)
print('S_A =',min_S_A)
print('S_B =',min_S_B)
           