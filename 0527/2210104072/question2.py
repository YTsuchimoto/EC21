import numpy as np
import sympy as sp
from sympy import *

t = Symbol("theta")
ap1 = np.array([5 * cos(2 * t) - 2, 5 * sin(2 * t)])
ap2 = np.array([10 * cos(t) - 2, 10 * sin(t)])

S = (1 / 2) * (ap1[0] * ap2[1] - ap2[0] * ap1[1])
res = sp.solve(S.diff(t))

ans = []
for i in range(len(res)):
    ans.append(abs(S.subs(t, res[i])))

print('max=',end="");print(max(ans))