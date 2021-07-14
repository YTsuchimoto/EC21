# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 12:02:54 2021

@author: Masatoshi
"""
import itertools
import numpy as np
s=[]
for i in range(2,100):
    flag=0
    for j in range(2,i//2+1):
        if(i%j==0):
            flag=1
            break
    if flag==0:
        s.append(i)
print(s)
numofs=len(s)
sumofs=np.sum(s)/2
s1=[]
#saの仮置き場
s2=[]
#sbの仮置き場
sa=[]
sb=[]
best=sumofs
#sの和の1/2とs1との差分の最小値
for i in range(numofs//2+1):
    for s1 in itertools.combinations(s,i):
        if(abs(np.sum(s1)-sumofs)<best):
            sa=s1
            best=abs(np.sum(s1)-sumofs)
sb=list(set(s)-set(sa))
print(sa)
print(sb)
print('the absolute value of difference=',abs(np.sum(sa)-np.sum(sb)))
            