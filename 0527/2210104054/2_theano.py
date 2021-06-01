
import numpy as np
from theano import function, shared
import theano.tensor as T


def solve():
  x = T.dscalar('x')
  S = ((5 * np.cos(2 * x) - 2) * (10 * np.sin(x)) - (10 * np.cos(x) - 2) * (5 * np.sin(2 * x))) / 2
  dS = T.grad(cost=S, wrt=x)

  w = shared(value= 2 * np.pi, name='w')
  fS = function(inputs=[x], outputs=S)
  fdS = function(inputs=[x], outputs=dS, updates=[(w,w - 0.001 * dS)])

  for i in range(10000):
    fdS(w.get_value())

  print('x = {}, S = {}'.format(w.get_value() - 2 * np.pi if w.get_value() > 2 * np.pi else w.get_value(), abs(fS(w.get_value()))))

if __name__ == '__main__':
  solve()
