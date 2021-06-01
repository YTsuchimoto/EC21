#Johan Berdougo 2200104056

from math import sqrt, sin, cos, pi
from sympy import *



#Define the points on time t=0
O = Point([0 , 0])
A = Point([2 , 0])
P1 = Point([5, 0])
P2 = Point([10 , 0])

print("O : " ,O)
print("A : " ,A)
print("P1 : " ,P1)
print("P2 : " ,P2)
print("")

#Aply the new position depending on the angular velocity
phi = symbols('phi')

p2_tmp = P2.rotate(phi)
p1_tmp = P1.rotate(2*phi)

#Expression of the area of ΔA P1 P2. 
area = Polygon(p1_tmp, p2_tmp, A).area
print("Expression of the area : ", area)
print("")

#Finding the max value
max_area = maximum(area, phi, Interval(0, 2*pi))

print("max area :", max_area.evalf())



