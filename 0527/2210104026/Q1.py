# -*- coding: utf-8 -*-
import numpy as np

#1~100の素数探し
a = []
for i in range(2,100):
    flag = 0
    for j in range(2,i//2+1):
        if(i%j == 0):
            flag = 1
            break
    
    if flag == 0:
        a.append(i)

print("a = " + str(a))
min = sum(a)
sa = []
sb = []
for i in range(2 ** len(a)):
    temp1 = []
    temp2 = []
    for j in range(25):
        if (i>>j)&1 == 1:
            temp1.append(a[j])
        else:
            temp2.append(a[j])
    if(min > abs(sum(temp1)-sum(temp2))):
        min = abs(sum(temp1)-sum(temp2))
        sa = temp1
        sb = temp2

print("min_value = " + str(min))
print("SA_sum = " + str(sum(sa)))
print("SB_sum = " + str(sum(sb)))
print("SA = " + str(sa))
print("SB = " + str(sb))