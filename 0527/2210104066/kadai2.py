#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 29 11:03:48 2021

@author: hyakutakesatoshi
"""

from sympy import *
import numpy as np

theta = Symbol('theta', real = True)
p1_x = 5 * cos(2 * theta)
p1_y = 5 * sin(2 * theta)
p2_x = 10 * cos(theta)
p2_y = 10 * sin(theta)
a_x = 2
a_y = 0

tmp = 0.5 * ((p1_x-a_x) * (p2_y-a_y) - (p1_y-a_y) * (p2_x-a_x))
fS = simplify(tmp)  #目的関数
fdS = fS.diff(theta)  #勾配

ans =  np.min(abs(np.array(solve(fdS))))  #極値をとる時のtheta
print(abs(fS.subs(theta, ans)))