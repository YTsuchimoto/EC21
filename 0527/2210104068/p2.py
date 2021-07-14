"""
Author : VILLIN Victor .
Date : 2020-06-02 .
File : q2.py .

Description : None

Observations : None
"""

# == Imports ==
from sympy import *
# =============



def exercice2():

    theta = Symbol('theta')
    Ox, Oy = symbols('Ox Oy')

    # Assuming the initial positions are all on the x-axis:
    O = Point(Ox,Oy)
    P1 = Point(Ox+5, Oy).rotate(theta*2, O)
    P2 = Point(Ox+10, Oy).rotate(theta, O)
    A = Point(2+Ox, Oy)

    area_expr = Polygon(P1, P2, A).area

    print('area expression: ', area_expr)

    # Once P2 did the full circle, we obtain once again the situation of t=0
    # P2 did full circle
    # <=> theta = 2 * pi
    max_area = maximum(area_expr, theta, Interval(0, 2*pi))

    return max_area


if __name__ == '__main__':

    result = exercice2()
    print('Result for maximum Area of ΔAP1P2:\n',
        result, '=', N(result))
    """
    Result :
    sqrt(Max((25*sqrt(15)*cos(2*atan(sqrt(15)))/2 - 5*sqrt(15) - 45*sin(2*atan(sqrt(15)))/2)**2/2, (45*sin(2*atan(sqrt(15)))/2 + 5*sqrt(15) - 25*sqrt(15)*cos(2*atan(sqrt(15)))/2)**2/2)) = 51.3489897661093
    
    """
