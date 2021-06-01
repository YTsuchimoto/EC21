#!/usr/bin/python

import numpy as np
import theano
import theano.tensor as T
import matplotlib.pyplot as plt


'''
#A
x1 = 0
y1 = 2
#P1
x2 = 5 * np.sin(2 * x)
y2 = 5 * np.cos(2 * x)
#P2
x3 = 10 * np.sin(x)
y3 = 10 * np.cos(x)

S = x1*y2 + x2*y3 + x3*y1 - y1*x2 - y2*x3 - y3*x1
S = S / 2
'''

x = T.dscalar('x')
S = 50*T.sin(-2*x)*T.cos(-x) + 20*T.sin(-x) - 10*T.sin(-2*x) - 50*T.cos(-2*x)*T.sin(-x)
f1 = theano.function(inputs = [x], outputs = S)
gS = T.grad(cost = S, wrt = x)
f2 = theano.function(inputs = [x], outputs = gS)

X = range(0, 8)
Y = []
for x in X:
    Y.append(f1(x))
plt.plot(X, Y)
plt.show()