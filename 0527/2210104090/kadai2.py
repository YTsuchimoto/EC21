"""
三角形AP1P2の面積Sの最大値を求めよ.
面積は公式より，以下のように計算できる．
S = 1/2*|10*sin(theta*t)*(5*cos(2*theta*t)-2)-5*sin(2*theta*t)*(10*cos(theta*t)-2)|
ここで，時刻tにおけるP2の回転した角度をxとすると，
x = theta*t
と表せるため，
S = 1/2*|10*sin(x)*(5*cos(2*x)-2)-5*sin(2*x)*(10*cos(x)-2)|
と表せる．
公式より，
S = |5*sin(x)*(2*cos(x)-7)|
と式変形できる．
このとき，Sが最大となるxを求めれば良い．
"""


import numpy as np
import theano
import theano.tensor as T
import sympy as sp
from sympy import sin, cos, Symbol


x = sp.Symbol('x')
S = 5*sin(x)*(2*cos(x)-7)
# print(S)
S1 = sp.diff(S, x)
# print(S1)
critical_points = sp.solve(S1)
# print(critical_points)
S2 = sp.diff(S, x, 2)
# print(S2)

answer = 0
for p in critical_points:
    tmp = sp.re(S2.subs(x, p))
    if abs(tmp) > answer:
        answer = abs(tmp)
    # print('S(x)はx={}で極値{}をとる'.format(p, S2.subs(x, p)))
    # print(sp.re(S2.subs(x, p)))

# 回答表示
print(answer)