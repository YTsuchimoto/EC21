# -*- coding: utf-8 -*-
"""
Created on Fri May 28 15:34:48 2021
@author: Yuya Seki
Well, I'm beginner at python, 
however, I decided to callenge to use theano.
"""

# numpy (ease of handling arrays)
import numpy as np
# np.sin(x) -> sin(x)
from numpy import sin, cos

# theano  (for machine learning)
import theano.tensor as T
# theano.function() -> function()
from theano import function, shared

'''
coordinates of each points as follows:
O:   (0, 0)
A:   (2, 0)
P_1: (5cos2θ, 5sin2θ)
P_2: (10cosθ, 10sinθ)

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

if __name__ == '__main__':
    # shared vector (scalar but handle theta as one-diretion vector)
    theta = shared(value=np.random.random(1),name="theta")
    
    # AOT (Area Of Triangle, ΔAP_1P_2)
    # Note that this is a signed area
    AreaOfTriangle = T.sum(abs(((5 * cos(2*theta) - 2) * (10 * sin(theta))) - ((10 * cos(theta) - 2) * (5 * sin(2*theta)))) / 2)
    
    # gradient of AOT, d(AOT)/dt
    gAOT = T.grad(cost=AreaOfTriangle, wrt=theta)
    
    # larning rate
    lr=shared(value=np.float32(0.05),name="lr")
    
    # so as to maxmizing "cost" (benefit),
    # the sign of the update equation is positive
    f = function(inputs=[], outputs=[AreaOfTriangle], updates=[(theta, (theta + lr * gAOT))])
    
    # update theta for 50 times
    for i in range(50):
        # output the status of learning
        print("Epoch: ", i + 1," y=", f()[0], "\t theta=", theta.get_value(), sep="")
        # decrease the learning rate gradually
        if (i+1) % 5==0: lr.set_value(lr.get_value()*np.float32(0.9))
        
    # print output
    print("\n----------results of this program----------")
    print("Max. calclated by theano: {}".format(f()[0]))
    print("θ obtained with theano: {}".format(theta.get_value()[0]))
    # I calculated the max. of AOT manually
    # and turned out the output is correct.
    print("\n----------results of manual calc.----------")
    print("Max. calclated by manual: {}".format(75/8*np.sqrt(15)))
    print("θ calclated by manual: {}".format(np.arctan(-np.sqrt(15)) + np.pi))