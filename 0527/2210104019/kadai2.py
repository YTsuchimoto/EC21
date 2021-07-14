import numpy as np
import sympy
t = sympy.Symbol('t', real='True')
P1x = 5.0*sympy.cos(2*t)
P1y = 5.0*sympy.sin(2*t)
P2x = 10.0*sympy.cos(t)
P2y = 10.0*sympy.sin(t)
S = ((P1x-2)*P2y - (P2x-2)*P1y)/2
grad_S = sympy.diff(S, t).simplify()
kyokuti = sympy.solve(grad_S)

print(max(abs(S.subs(t, item)) for item in kyokuti))
