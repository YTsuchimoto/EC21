# -*- coding: utf-8 -*-
"""
Created on Thu May 27 01:53:11 2021

@author: ikamu
"""

import itertools
import numpy as np

a=[]
for i in range(2,100):
    flag=0
    for j in range(2,i//2+1):
        if(i%j==0):
            flag=1
            break
    if flag==0:
        a.append(i)
#print(a) 
a=np.array(a)

b=[]

for i in range(0,len(a)):
    temp=[1]*(len(a)-1-i)
    b.append(np.array([0,a[i]]).reshape(-1,*temp))
 
c=0
for i in b:
    c=c+i 

sa=[]
sb=[]
for i in range(sum(a)//2,sum(a)):
    if len(np.argwhere(c==i))!=0:
        #print(np.argwhere(c==i))
        d=np.argwhere(c==i)[0]
        for j in range(0,len(a)):
            if(d[j]==0):
                sa.append(a[j])
            elif(d[j]==1):
                sb.append(a[j])
        print("差の絶対値の最小値:",abs(sum(sa)-sum(sb)))
        print("sa,sbの組み合わせ例")
        print("sa:",sa)
        print("sb:",sb)
        break
    
#for i in range(c,len(a)//2):
    #print(list(itertools.combinations(a,i)))
    