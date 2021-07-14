# -*- coding: utf-8 -*-

from sympy import *

X1, X2, X3, Y1, Y2, Y3 = symbols('P1_x, P1_y, P2_x, P2_y, P3_x, P3_y')

# The formula for an area of the triangle is as follows:
# Note: The actual area is the absolute value of this.  However, including the 
# absolute-value term makes the derivative too complex for Sympy to handle
area = (X1 * (Y2 - Y3) + X2 * (Y3 - Y1) + X3 * (Y1 - Y2)) / 2
# Reference: https://math.stackexchange.com/questions/516219/finding-out-the-area-of-a-triangle-if-the-coordinates-of-the-three-vertices-are

# Example: Test the area of the tringle created by (0, 0), (1, 0), and (0, 1)
# (Should be 1/2)
print(area.subs([(X1, 0), (Y1, 0), (X2, 1), (Y2, 0), (X3, 0), (Y3, 1)]) == 1/2)
print()

# Let's fix point A at (2, 0)
# Then we can calculate the position of P1 and P2 as a function of time
t = Symbol('t')
Ax, Ay = 2, 0
P1x, P1y = 5 * cos(2 * t), 5 * sin(2 * t)
P2x, P2y = 10 * cos(t), 10 * sin(t)

# Now, substitute these functions into the formula for the area of a trinagle
formula = area.subs([(X1, Ax), (Y1, Ay), (X2, P1x), (Y2, P1y), (X3, P2x), (Y3, P2y)])
print(formula) # Abs(50*sin(t)*cos(2*t) - 20*sin(t) - 50*sin(2*t)*cos(t) + 10*sin(2*t))/2

# For example,
print("When t = 2 Pi/3...")
print("P1 = (%.2f, %.2f)" % (P1x.subs('t', 2 * pi / 3), P1y.subs('t', 2 * pi / 3)))
print("P2 = (%.2f, %.2f)" % (P2x.subs('t', 2 * pi / 3), P2y.subs('t', 2 * pi / 3)))
print("Area = %.2f" % N(formula.subs('t', 2 * pi / 3)))
print()

# Now, we just set the derivative equal to zero.
extrema = solve(formula.diff(t))
for extreme in extrema:
    print(N(extreme))
    print(N(formula.subs('t', extreme)))
    print()
    
# From here, we can see that the maximum area of the triangle is 36.31
# And this occurs when t = -1.82, 1.82, -4.46, or +4.46

print("Maximum area: 36.30921")
