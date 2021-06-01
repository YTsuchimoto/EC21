#!/usr/bin/env python3
import sympy as sp


# define "theta" as a symbol
theta = sp.symbols("theta", real=True)
# f(theta) := triangle area
f = 1 / 2 * ((2 - 10 * sp.cos(theta)) *
             (5 * sp.sin(2 * theta) - 10 * sp.sin(theta)) -
             (5 * sp.cos(2 * theta) - 10 * sp.cos(theta)) *
             (0 - 10 * sp.sin(theta)))
f = sp.trigsimp(f)  # simplify f(theta)
# print("f(theta) = {}".format(f))
critical_points = sp.solve(sp.diff(f, theta))  # find theta where f'(theta) = 0

# calculate extremum of f(theta)
F = []
for i in critical_points:
    F.append(abs(f.subs(theta, i)))
answer = max(F)  # find Maxima of f(theta)
print("Maximum area of triangle: {}".format(answer))
