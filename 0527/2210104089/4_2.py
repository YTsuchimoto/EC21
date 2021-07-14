from sympy import *

t = Symbol('t',real=True)
tri = geometry.Polygon((2,0),(5 * cos(2*t),5*sin(2*t)),(10*cos(t),10*sin(t)) )
dif = diff(tri.area,t)
ans = solve(dif)
ans_list = []
for i in ans:
    ans_list.append(tri.area.subs([(t, i)]))
print("max:{}".format(max(ans_list)))
