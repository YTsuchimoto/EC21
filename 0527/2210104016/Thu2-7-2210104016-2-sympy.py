'''
問題 2
平面上に原点 O を中心とする半径 5 と 10 の同心円 C_1 と C_2 があり
O から距離 2 のところに定点 A がある. 動点 P_1, P_2 がそれぞれ C_1,
C_2 上を一定の速さで反時計回りに回転している.
時刻 t = 0 で O, A, P_1, P_2 がこの順に一直線上に並び, また, P_1 の
各速度は P_2 の 2 倍とする.
△AP_1P_2 の面積の最大値を求めよ.

回答 sympy 版
'''

import sympy
from sympy import sin, cos

def solve():
  theta = sympy.Symbol('theta', real=True, nonnegative=True)
  S = sympy.trigsimp(((5 * cos(2 * theta) - 2) * (10 * sin(theta)) - (10 * cos(theta) - 2) * (5 * sin(2 * theta))) / 2)
  gS = sympy.diff(S, theta)

  equ = sympy.solve(gS, theta)

  for e in equ:
    print('theta = {}, S = {}'.format(e.evalf(), abs(S.subs(theta, e).evalf())))

if __name__ == '__main__':
  solve()

# 2210104016
