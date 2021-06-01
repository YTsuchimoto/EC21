# -*- coding: utf-8 -*-
"""
Created on Sat May 29 18:56:01 2021

@author: akasa
"""

import sympy as sym

#原点Oを2次元座標平面の原点とし、A,P1,P2の座標から面積Sを求める。
s=sym.Symbol('s')
A_x=2
A_y=0
P1_x=5*sym.cos(2*s)
P1_y=5*sym.sin(2*s)
P2_x=10*sym.cos(s)
P2_y=10*sym.sin(s)

S=sym.simplify((1/2)*((P1_x-A_x)*(P2_y-A_y)-(P2_x-A_x)*(P1_y-A_y)))

#微分して極値を求める
diff1=sym.diff(S,s)
solves=sym.solve(diff1,s)

#極値から最大値を求める
Max_S=0
for solve in solves:
    S_=abs(S.subs(s,solve))
    if S_>Max_S:
        Max_S=S_
        
print('最大値:',Max_S)