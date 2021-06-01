# -*- coding: utf-8 -*-
"""
Created on Thu May 27 16:09:53 2021

@author: ikamu
"""

import sympy
from sympy import pi

#x=sympy.Symbol('x')
x=sympy.var('x',real=True)
P1x=5*sympy.cos(x)
P1y=5*sympy.sin(x)
P2x=10*sympy.cos(2*x)
P2y=10*sympy.sin(2*x)
Ax=2
Ay=0

S_abs=(1/2)*abs((P1x-Ax)*(P2y-Ay)-(P2x-Ax)*(P1y-Ay))
print("△AP1P2=",S_abs)
S_abs=sympy.simplify(S_abs)
print("=",S_abs)
sympy.plot(S_abs,(x,-2*pi,2*pi))
#print(S.subs(x,pi))

#絶対値がない関数で考える
S=(1/2)*((P1x-Ax)*(P2y-Ay)-(P2x-Ax)*(P1y-Ay))
S=sympy.simplify(S)
sympy.plot(S,(x,-2*pi,2*pi))
a=sympy.solve(sympy.simplify(sympy.diff(S,x)))
#print(a)
x1,x2=a
f2=sympy.diff(S,x,2)
Smax=[]
for i in a:
    if f2.subs(x,i)!=0:
        Smax.append(abs(S.subs(x,i)))
print("△AP1P2の面積の最大値:",max(Smax))
