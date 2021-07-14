from sympy import *

theta = Symbol('theta')
ax = 2
ay = 0
x1 = 5*cos(2*theta)
y1 = 5*sin(2*theta)
x2 = 10*cos(theta)
y2 = 10*sin(theta)

s = trigsimp(((x1 - ax) * (y2 - ay) - (y1 - ay) * (x2 - ax)) / 2)
s_diff = diff(s, theta)
point = solve(s_diff, theta)

ans = []

for i in point:
    ans_s = s.subs(theta, i)
    ans.append(abs(ans_s))
print('最大値:' + str(simplify(max(ans))))
