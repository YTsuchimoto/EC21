#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 31 18:54:35 2021

@author: m.yuta
"""

S=[]
for i in range(2,100):
  flag = 0
  for j in range(2,i//2+1):
    if(i%j==0):
      flag = 1
      break
  if flag == 0:
    S.append(i)


S_a = []
S_b = []

for i in reversed(range(0,len(S))):
    if(sum(S_a)>sum(S_b)):
        S_b.append(S[i])
      
    else:
        S_a.append(S[i])
        
print('S_a:',S_a)
print('Sum of S_a:',sum(S_a))
print('S_b:',S_b)
print('Sum of S_b:',sum(S_b))
print('Minimum absolute value:',abs(sum(S_a)-sum(S_b)))