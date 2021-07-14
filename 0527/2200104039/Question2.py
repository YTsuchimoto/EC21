#!/usr/bin/env python
# coding: utf-8

# 問題2

# In[6]:


import sympy as sp


# In[23]:


Ax=2
Ay=0

theta=sp.Symbol('theta',real=True)
P1x=5*sp.cos(2*theta)
P1y=5*sp.sin(2*theta)
P2x=10*sp.cos(theta)
P2y=10*sp.sin(theta)

area_AP1P2=((P1x-Ax)*(P2y-Ay)-(P1y-Ay)*(P2x-Ax))/2
area_AP1P2=sp.trigsimp(area_AP1P2)
area_AP1P2_diff=sp.diff(area_AP1P2,theta)
results=sp.solve(area_AP1P2_diff,theta)

answers=[]
for i in results:
    tmp=area_AP1P2.subs(theta,i)
    answers.append(tmp)
    
print('△AP1P2の最大値は　',sp.trigsimp(max(answers)))

