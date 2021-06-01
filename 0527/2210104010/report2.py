# -*- coding: utf-8 -*-
# 2210104010 浦上太一
from sympy import *
# from theano import *
import numpy as np
import matplotlib.pyplot as plt

def get_distance(x1, y1, x2, y2):
    d = root((x2 - x1) ** 2 + (y2 - y1) ** 2, 2)
    return d

def heron(a, b, c):
    d = (a + b + c) / 2
    return root(d * (d - a) * (d - b) * (d - c), 2)



def main():
    t = Symbol("t", real=True)
    Ax = 2
    Ay = 0
    P1x = 5*cos(2*t)
    P1y = 5*sin(2*t)
    P2x = 10*cos(t)
    P2y = 10*sin(t)
    
    a = get_distance(P1x,P1y,P2x,P2y)
    b = get_distance(P2x,P2y,Ax,Ay)
    c = get_distance(Ax,Ay,P1x,P1y)
    
    S = heron(a,b,c)
    S = simplify(S)
    
    diff_S = diff(S,t)
    diff_S = simplify((diff_S))
    
    li_t = solve(Eq(diff_S,0).expand(trig=True), t)

    # p1= plot(S)
    
    li_S = []
    for val in li_t:
        li_S.append(S.subs(t,val))
    
    # print(li_S,type(li_S))
    print("最大値: {}".format(max(li_S)))        

    


if __name__ == '__main__':
    main()