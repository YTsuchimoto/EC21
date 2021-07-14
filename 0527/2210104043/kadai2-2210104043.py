# coding: utf-8
# 2210104043 Yusei Takayama

import numpy as np
import theano.tensor as T
from theano import function, shared
from sympy import Symbol, geometry, cos, sin, solve, diff

eps = 10e-5
learning_rate = 10e-3
max_num = 100000


def solve_by_theano():
  theta = T.dscalar('theta')

  S = ((5 * np.cos(2 * theta) - 2) * (10 * np.sin(theta)) - (10 * np.cos(theta) - 2) * (5 * np.sin(2 * theta))) / 2

  # 微分
  gS = T.grad(cost=S, wrt=theta)

  # 動かす角度θの初期値
  x = shared(value=2 * np.pi * np.random.rand(), name='x')

  func_S = function(inputs=[theta], outputs=abs(S))
  func_gS = function(inputs=[theta], outputs=gS)
  gradient_descent = function(inputs=[theta], outputs=gS, updates=[(x, x - learning_rate * gS)])

  for i in range(max_num):
    gradient_descent(x.get_value())

    # 終了判定
    if abs(func_gS(x.get_value())) <= eps:
      break

  return x.get_value(), func_S(x.get_value())


def solve_by_sympy():
  theta = Symbol('theta', real=True)
  AP_1P_2 = geometry.Polygon((2, 0), (5*cos(2*theta), 5*sin(2*theta)), (10*cos(theta), 10*sin(theta)))

  max_S = 0
  ans_theta = 0

  for x in solve(diff(AP_1P_2.area, theta)):
    S = AP_1P_2.area.subs(theta, x)
    if max_S < S:
      max_S = S
      ans_theta = x

  return ans_theta, float(max_S)



def main():
  theta, max_S = solve_by_theano()
  print('theano : max_S = {}'.format(max_S))
  theta, max_S = solve_by_sympy()
  print('sympy : max_S = {}'.format(max_S))

  """
  theano : max_S = 36.30921887061456
  sympy : max_S = 36.30921887069454
  """


if __name__ == '__main__':
  main()
