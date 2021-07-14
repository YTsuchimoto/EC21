from sympy import *
import sympy

def area():

    theta = sympy.Symbol('theta', real = True)


    p1 = (5*cos(2*theta), 5*sin(2*theta))
    p2 = (10*cos(theta), 10*sin(theta))
    a = (2, 0)


    tri = sympy.geometry.Polygon(p1, p2, a)
    max_area = 0

    s_diff = sympy.solve(sympy.diff(tri.area, theta))
    # print(s_diff)
    for s in s_diff:
        if max_area < tri.area.subs(theta, s):
            max_area = tri.area.subs(theta, s)
    
    return max_area



if __name__ == "__main__":

    print("The max value of the area is " + str(area()))