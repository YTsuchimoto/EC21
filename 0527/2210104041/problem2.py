# -*- coding: utf-8 -*-
from sympy import *

def main():
    # θの定義
    theta = Symbol('theta',real=True)

    # 3点の座標
    p1x = 5 * cos(2*theta)
    p1y = 5 * sin(2*theta)
    p2x = 10 * cos(theta)
    p2y = 10 * sin(theta)
    ax = 2
    ay = 0

    triangle = geometry.Polygon((ax,ay),(p1x,p1y),(p2x,p2y))
    max_area = 0
    for s in solve(diff(triangle.area,theta)):
        if max_area < triangle.area.subs(theta,s):
            max_area = triangle.area.subs(theta,s)

    print("The maximum value of the area : {}".format(max_area))

if __name__ == '__main__':
    main()