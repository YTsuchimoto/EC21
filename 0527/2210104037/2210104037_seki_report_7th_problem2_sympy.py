# -*- coding: utf-8 -*-
"""
Created on Fri May 28 13:55:33 2021
@author: Yuya Seki
Well, I'm beginner at python, 
however, I decided to callenge to use sympy.
"""

'''
coordinates of each points as follows:
O:   (0, 0)
A:   (2, 0)
P_1: (5cos2θ, 5sin2θ)
P_2: (10cosθ, 10sinθ)
'''

# sympy is library for algebra calculation
import sympy
# sympy.sin(x) -> sin(x)
from sympy import sin, cos

if __name__ == '__main__':
    # theta is liniar function of t (not identically equal to zero), 
    # then we can equate t with theta
    theta = sympy.Symbol('theta', real=True, nonnegative=True)
    
    '''
    Parallelize each point by 2 
    in the negative direction of the x-axis.
    
    A':   (0, 0)
    P'_1: (5cos2θ - 2, 5sin2θ)
    P'_2: (10cosθ - 2, 10sinθ)
    
    ΔAP_1P_2 = ΔA'P'_1P'_2 and
    ΔA'P'_1P'_2 is given by half the absolute value 
    of the determinant of the following matrix
    | (5cos2θ - 2) (5sin2θ) |
    | (10cosθ - 2) (10sinθ) |
    '''
    # AOT (Area Of Triangle, ΔAP_1P_2)
    # Note that this is a signed area
    AreaOfTriangle = sympy.trigsimp((((5 * cos(2*theta) - 2) * (10 * sin(theta))) - ((10 * cos(theta) - 2) * (5 * sin(2*theta)))) / 2)
    
    # gradient of AOT, d(AOT)/dt
    gAOT = sympy.diff(AreaOfTriangle, theta, 1)
    
    # find the max. at stopping points
    # it must be the biggest value of AOT in the field
    # because area is finite however the shape of trigngle is
    ans = 0
    for x in sympy.solve(gAOT, theta):
        # sind area -> unsigned area
        tmp = sympy.trigsimp(sympy.Abs(AreaOfTriangle.subs(theta, x)))
        if ans < tmp:
            ans = tmp
            
    # print output
    print("--------results of this program--------")
    print("Max. calclated by scypy: {}".format(ans))
    print("Decimal format: {}".format(sympy.N(ans, 10)))
    # I calculated the max. of AOT manually
    # and turned out the output is correct.
    print("\n--------results of manual calc.--------")
    print("Max. calclated by manual: 75/8*sqrt(15)")
