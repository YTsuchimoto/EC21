# -*- coding: utf-8 -*-
"""
Created on Fri May 28 15:51:08 2021

@author: owner
"""

S=[]
for i in range(2,100):
    flag = 0
    for j in range(2,i//2+1):
        if (i%j==0):
            flag=1
            break
    if flag == 0:
        S.append(i)

S.sort(reverse=True)

Sa = []
Sb = []
Sa_sum = 0
Sb_sum = 0

for i in S:
    if Sa_sum <= Sb_sum:
        Sa.append(i)
        Sa_sum = Sa_sum + i
    else:
        Sb.append(i)
        Sb_sum = Sb_sum + i

print('dif : %d' % abs(Sa_sum - Sb_sum))
print('Sa :', Sa)
print('Sb :', Sb)