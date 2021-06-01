'''
問題 2
平面上に原点 O を中心とする半径 5 と 10 の同心円 C_1 と C_2 があり
O から距離 2 のところに定点 A がある. 動点 P_1, P_2 がそれぞれ C_1,
C_2 上を一定の速さで反時計回りに回転している.
時刻 t = 0 で O, A, P_1, P_2 がこの順に一直線上に並び, また, P_1 の
各速度は P_2 の 2 倍とする.
△AP_1P_2 の面積の最大値を求めよ.

回答 theano 版
'''

import numpy as np
import theano.tensor as T
from theano import function, shared

def solve():
  theta = T.dscalar('theta')
  S = ((5 * np.cos(2 * theta) - 2) * (10 * np.sin(theta)) - (10 * np.cos(theta) - 2) * (5 * np.sin(2 * theta))) / 2
  gS = T.grad(cost=S, wrt=theta)

  w = shared(value=np.random.rand() * 2 * np.pi, name='w')
  fS = function(inputs=[theta], outputs=S)
  fgS = function(inputs=[theta], outputs=gS, updates=[(w,w - 0.001 * gS)])

  for i in range(10000):
    fgS(w.get_value())

  print('theta = {}, S = {}'.format(w.get_value() - 2 * np.pi if w.get_value() > 2 * np.pi else w.get_value(), abs(fS(w.get_value()))))

if __name__ == '__main__':
  solve()

# 2210104016
