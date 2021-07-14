# -*- coding: utf-8 -*-
"""
Created on Tue Jun  1 14:57:24 2021

@author: s70mo
"""
import random

#素数列sを生成
s=[]
for i in range(2,100):
    flag = 0
    for j in range(2,i//2+1):
        if(i%j==0):
            flag = 1
            break
    if(flag==0):
        s.append(i)
print(s)
        
#sをsaとsbに分ける
sa=[]
sb=[]
for i in range(0,len(s)):
    if(i%2==0):
        sa.append(s[i])
    else:
        sb.append(s[i])
print(sa)
print(sb)

#saの和とsbの和の差をdとして計算する
d=sum(sa)-sum(sb)
print(d)

min_d = abs(d)

#入れ替える
for i in range(0,100):
    flag = 0
    if(d>0 and flag==0):
        flag = 1
        while(d>0):
            random_num = random.choice(sa)
            sb.append(random_num)
            sb.sort()
            sa.remove(random_num)
            d=sum(sa)-sum(sb)
    if(d<0 and flag==0):
        flag = 1
        while(d<0):
            random_num = random.choice(sb)
            sa.append(random_num)
            sa.sort()
            sb.remove(random_num)
            d=sum(sa)-sum(sb)
    if(min_d>abs(d)):
        min_d =abs(d)
        print(sa)
        print(sb)
        print(d)
    if(d==0):
        break
        