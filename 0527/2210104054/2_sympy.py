''

import sympy
from sympy import sin, cos

def solve():
  x = sympy.Symbol('x', real=True, nonnegative=True)
  S = sympy.trigsimp(((5 * cos(2 * x) - 2) * (10 * sin(x)) - (10 * cos(x) - 2) * (5 * sin(2 * x))) / 2)
  dS = sympy.diff(S, x)

  equ = sympy.solve(dS, x)

  for e in equ:
    print('x = {}, S = {}'.format(e.evalf(), abs(S.subs(x, e).evalf())))

if __name__ == '__main__':
  solve()