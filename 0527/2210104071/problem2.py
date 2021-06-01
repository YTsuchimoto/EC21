'''
2210104071 寳来輝弥
'''

import numpy as np
import sympy as sp

theta = sp.Symbol("theta", real=True)
P1 = np.array([5*sp.cos(2*theta), 5*sp.sin(2*theta)])
P2 = np.array([10*sp.cos(theta), 10*sp.sin(theta)])
A = np.array([2, 0])

A_P1 = P1 - A
A_P2 = P2 - A

T = sp.simplify(1/2*((A_P1[0]*A_P2[1]) - (A_P1[1]*A_P2[0])))
dT = T.diff(theta)
theta_ans = sp.solve(dT)

print(theta_ans)

T_ans = []

for i in range (len(theta_ans)):
    T_ans.append(abs(T.subs(theta, theta_ans[i])))

print('T_max = ', max(T_ans), sep='')
