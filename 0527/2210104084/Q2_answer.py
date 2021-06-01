#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 31 22:47:08 2021

@author: m.yuta
"""
import sympy as sym

theta = sym.Symbol("theta", real=True)

#Aの座標を定義
A_x = 2
A_y = 0

#P1,P2の各座標をthetaを用いて定義
P1_x = 5 * sym.cos(2*theta)
P1_y = 5 * sym.sin(2*theta)
P2_x = 10 * sym.cos(theta)
P2_y = 10 * sym.sin(theta)

#A,P1,P2からなる三角形の面積S
S =  ((P1_x - A_x)*(P2_y - A_y)- (P1_y - A_y)*(P2_x - A_x))/2

#Sの式をsym.trigsimpを用いて簡略化
S = sym.trigsimp(S)

#Sを微分して極値をとるθを求める
dS = sym.diff(S,theta)
theta_candidate = sym.solve(dS,theta)

#Sの式では絶対値を考慮していないのでθの解候補を代入して最大値を求める
theta_answer = []
for thetas in theta_candidate:
    x = S.subs(theta,thetas)
    theta_answer.append(x)
    
theta_answer = sym.trigsimp(max(theta_answer))

print('Max area of AP_1P_2:',theta_answer)