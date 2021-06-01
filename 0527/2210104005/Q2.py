# -*- coding: utf-8 -*-
"""
Created on Thu May 27 10:33:40 2021

@author: やん
"""
import numpy as np
import sympy as sp

theta=sp.Symbol("theta",real=True)
P1=np.array([5*sp.cos(2*theta),5*sp.sin(2*theta)])
P2=np.array([10*sp.cos(theta),10*sp.sin(theta)])
A=np.array([2,0])
AP1=P1-A
AP2=P2-A

S=sp.simplify(1/2*((AP1[0]*AP2[1])-(AP1[1]*AP2[0])))
dS=S.diff(theta)
theta_ans=sp.solve(dS)

ans=[]
print(theta_ans)
for i in range(len(theta_ans)):
    ans.append(abs(S.subs(theta,theta_ans[i])))  
print("max△AP1P2="+str(max(ans)))