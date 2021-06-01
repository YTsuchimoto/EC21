#!/usr/bin/env python
# coding: utf-8

import sympy as spy

theta = spy.Symbol("theta", real = True)

ax, ay = 2, 0
p1x, p1y, p2x, p2y = 5 * spy.cos(2 * theta), 5 * spy.sin(2 * theta), 10 * spy.cos(theta), 10 * spy.sin(theta)

S = spy.simplify((p1x - ax) * (p2y - ay) - (p1y - ay) * (p2x - ax)) / 2

S_ = spy.diff(S, theta)
theta_ = spy.solve(S_, theta)

answer = []

for i in theta_:
    x = S.subs(theta, i)
    answer.append(x)

print('面積Sの最大値 =', max(answer))