#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 27 11:33:30 2021

@author: hyakutakesatoshi
"""
import itertools 

S = []
for i in range(2,100):
    flag = 0
    for j in range(2,i//2+1):
        if(i%j == 0):
            flag = 1
            break
    if flag == 0:
        S.append(i)  

min = 10000
for i in range(0,len(S)//2+1):
    for v in itertools.combinations(S, i):
          Sa = list(v)
          Sb = list( set(S) - set(v) )
          tmp = abs(sum(Sa) - sum(Sb))
          if min > tmp:
              min = abs(sum(Sa) - sum(Sb))
              min_Sa = Sa
              min_Sb = Sb
              
          if min == 0:
              break

min_Sa.sort()
min_Sb.sort()
print('最小値：' + str(min))
print('Sa = ' + str(min_Sa))
print('Sb = ' + str(min_Sb))
