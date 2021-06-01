#!/usr/bin/env python
# coding: utf-8

import sympy as sp

def main():
    # θの定義
    theta = sp.Symbol("theta", real = True)
    # 座標の定義
    a_x = 2
    a_y = 0
    p1_x = 5 * sp.cos(2 * theta)
    p1_y = 5 * sp.sin(2 * theta)
    p2_x = 10 * sp.cos(theta)
    p2_y = 10 * sp.sin(theta)
    # 面積を求める
    S = sp.simplify(((p1_x - a_x)*(p2_y - a_y) - (p2_x - a_x)*(p1_y - a_y)) * 0.5)
    #print(S)
    # Sを微分
    S_diff = sp.diff(S, theta)
    # 極値を持つθを計算
    theta_list = sp.solve(S_diff, theta)
    #print(theta_list)
    area = []
    for s in theta_list:
        ans = S.subs(theta, s)
        area.append(abs(ans))
    #print(area)
    print("面積の最大値 :", max(area))

if __name__ == '__main__':
    main()