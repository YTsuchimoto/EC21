# -*- coding: utf-8 -*-
from mpmath.libmp.libelefun import agm_fixed
import sympy as sp


theta = sp.Symbol('x',real = True)

A_x = 2
A_y = 0
P1_x = 5 * sp.cos(2 * theta)
P1_y = 5 * sp.sin(2 * theta)
P2_x = 10 * sp.cos(theta)
P2_y = 10 * sp.sin(theta)

S_0 = ((P1_x - A_x) * (P2_y - A_y) - (P2_x - A_x) * (P1_y - A_y) ) * (1 / 2)

S = sp.simplify(S_0)

print(S)
diff1 = sp.diff(S, theta)

#sp.plot(S, (theta,0,2*pi))
critical_points = sp.solve(diff1, theta)

S_1=[]
#絶対値で計算していないのでここで絶対値に直す
for i in critical_points:
    S_1.append(abs(S.subs(theta, i)))

print('Max of AP1P2:',max(S_1))


