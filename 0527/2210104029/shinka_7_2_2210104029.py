# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 00:15:37 2021

@author: 2210104029 kondo iori
"""

import sympy

#面積の式を作成
theta=sympy.Symbol('theta')
S=10 * (5 * (sympy.cos(theta) ** 2 - sympy.sin(theta) ** 2) - 2) * sympy.sin(theta) - 5 * (10 * sympy.cos(theta) - 2) * 2 * sympy.sin(theta) * sympy.cos(theta)
S_fin=S/2

#微分して、極値を求める
S_diff=sympy.diff(S_fin)
S_kyokuchi=sympy.solve(S_diff)

#最大値を求める
S_max=0
for i in range (2,4):
    S_ans=S_fin.subs(theta,S_kyokuchi[i])
    if S_ans<0:
        S_ans =S_ans*-1
    if S_max<S_ans:
        S_max=S_ans

print("三角形の面積の最大値")
print(S_max)