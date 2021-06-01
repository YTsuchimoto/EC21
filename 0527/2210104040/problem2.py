#2210104040
#高橋敬

#!/usr/bin/env python
# coding: utf-8

import sympy as sp


def main():
#############################################################################
    # Aの定義
    Ax = 2
    Ay = 0
    # θの定義
    THETA = sp.Symbol("Theta", real=True)
    # P1の定義
    P1x = 5 * sp.cos(2 * THETA)
    P1y = 5 * sp.sin(2 * THETA)
    # P2の定義
    P2x = 10 * sp.cos(THETA)
    P2y = 10 * sp.sin(THETA)
#############################################################################
    # 面積Sの算出
    S = sp.simplify(((P1x - Ax)*(P2y - Ay) -(P2x - Ax)*(P1y - Ay)) * 0.5)
    # Sをθで微分
    S_diff = sp.diff(S, THETA)
    # 極値を持つθを計算->リストに格納
    THETA_list = sp.solve(S_diff, THETA)
#############################################################################
    # θごとの三角形の面積を求める
    area_list = []
    for s in THETA_list:
        ans = S.subs(THETA, s)
        area_list.append(abs(ans))
#############################################################################
    #最大値を算出
    max_area = max(area_list)
    #答えの表示
    print("The maximum value of the area : {}".format(max_area))

if __name__ == '__main__':
    main()
