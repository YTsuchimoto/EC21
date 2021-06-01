from sympy import *

theta = Symbol("theta", real=True)

#座標
p1_x = 5 * cos(2 * theta)
p1_y = 5 * sin(2 * theta)
p2_x = 10 * cos(theta)
p2_y = 10 * sin(theta)
a_x = 2
a_y = 0

s = simplify(1/2*((p1_x-a_x)*(p2_y-a_y)-(p2_x-a_x)*(p1_y-a_y)))
ds = s.diff(theta)
e_d = solve(ds)

ans = []
for d in e_d:
    ans.append(abs(s.subs(theta, d)))
print("The maximum area is {}".format(max(ans)))