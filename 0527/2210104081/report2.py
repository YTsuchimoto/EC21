import sympy

x = sympy.Symbol('x')

x_1 = 5*sympy.cos(2*x)
y_1 = 5*sympy.sin(2*x)

x_2 = 10*sympy.cos(x)
y_2 = 10*sympy.sin(x)

x_3 = 2
y_3 = 0

s = ((x_1 - x_3) * (y_2 - y_3) - (x_2 - x_3) * (y_1 - y_3)) * 1/2
s = sympy.simplify(s)
ds = sympy.diff(s)
solves = sympy.solve(ds, x)
max_s = 0

for a in solves:
    if sympy.Abs(s.subs(x, a)) > max_s:
        max_s = sympy.Abs(s.subs(x, a))

max_s = sympy.trigsimp(max_s)
print("max:", max_s)