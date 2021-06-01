# -*- coding: utf-8 -*-
"""
Created on Fri May 28 16:18:05 2021

@author: owner
"""


from sympy import *



z = Symbol('z')
p1x = 5*cos(2*z)
p1y = 5*sin(2*z)
p2x = 10*cos(z)
p2y = 10*sin(z)
Ax = 2
Ay = 0

#fの絶対値をとり2で割ったものが求める面積
f = (p1x - Ax)*(p2y - Ay) - (p1y - Ay)*(p2x - Ax)
f = trigsimp(f)
#print(f)
diff1 = diff(f)

critical_points = solve(diff1)
#print(critical_points)

ans = []
for i in critical_points:
    f_ins = f.subs(z, i)
    ans.append(abs(f_ins) / 2)

print(trigsimp(max(ans)))









