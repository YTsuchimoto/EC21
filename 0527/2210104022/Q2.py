import sympy as sp

t = sp.Symbol('t')

P1 = (5 * sp.cos(2 * t), 5 * sp.sin(2 * t))
P2 = (10 * sp.cos(t), 10 * sp.sin(t))
A = (2, 0)

S = sp.simplify(1/2 * ((P1[0] - A[0]) * (P2[1] - A[1]) - (P2[0] - A[0]) * (P1[1] - A[1])))

dS = S.diff()
exts = sp.solve(dS)

ans = max(map(lambda x: abs(S.subs(t, x)), exts))

print(f'answer: {ans}')
