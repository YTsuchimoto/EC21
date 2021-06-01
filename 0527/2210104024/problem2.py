# -*- coding: utf-8 -*-

import sympy

t=sympy.Symbol('t')
A=[2,0]
P1=[5*sympy.cos(2*t),5*sympy.sin(2*t)]
P2=[10*sympy.cos(t),10*sympy.sin(t)]

S=sympy.simplify((1/2)*((P1[0]-A[0])*(P2[1]-A[1])-(P2[0]-A[0])*(P1[1]-A[1])))

diff1=sympy.diff(S,t)

solves=sympy.solve(diff1,t)

S_max=0
for solve in solves:
    S_cul=abs(S.subs(t,solve))
    if S_cul>S_max:
        S_max=S_cul
        
print("最大値:",S_max)