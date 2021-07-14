# -*- coding: utf-8 -*-
"""2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zcedbsJ38e6q7hrbFiAVExdXvAyzKbwS
"""

from sympy import *

t, x1, y1, x2, y2  = symbols("t x1 y1 x2 y2")
# 点A(2,0)が原点に来るように平行移動した後
x1 = 5*cos(2*t)-2
y1 = 5*sin(2*t)
x2 = 10*cos(t)-2
y2 = 10*sin(t)

# ヘロンの公式
a = sqrt(x1**2 + y1**2)
b = sqrt(x2**2 + y2**2)
c = sqrt((x1-x2)**2 + (y1-y2)**2)
s = (a + b + c) / 2
S = sqrt(s * (s-a) * (s-b) * (s-c))

# tで微分
dS = diff(S, t)
dS = dS.simplify()
dS

L = solve(Eq(dS,0).expand(trig=True), t)
L = [l for l in L if l.is_real]
L

ans = -1000
for l in L:
    Sval = S.subs(t, l).simplify()
    ans = Max(ans, Sval)

"""求める最大値は"""

ans