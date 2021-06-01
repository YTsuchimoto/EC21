#!/usr/bin/env python
# coding: utf-8

a=[]
for i in range(2,100):
    flag = 0
    for j in range(2,i//2+1):
        if(i%j==0):
            flag = 1
            break
    if flag == 0:
        a.append(i)
    
a.reverse()

#print(a)

S__A = []
S__B = []

A , B = 0, 0

for i in range(len(a)):
    if(A > B):
        S__B.append(a[i])
        B += a[i]
        #print(S__B)
    else:
        S__A.append(a[i])
        A += a[i]
        #print(S__A)
        
S__A.reverse()
S__B.reverse()

print('A =', A)
print('B =', B)        
print('Sa =', S__A)
print('Sb =', S__B)
print('差の絶対値 =', abs(A - B))
