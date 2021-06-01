from sympy import *

x = Symbol('x',real=True)
p1x = 5*cos(2*x)
p1y = 5*sin(2*x)
p2x = 10*cos(x)
p2y = 10*sin(x)
Ax = 2
Ay = 0

#面積
f = ((p1x - Ax)*(p2y - Ay) - (p1y - Ay)*(p2x - Ax))/2
f = trigsimp(f)
#print(f)
#plot(f, (x, 0, 2*pi))

df = diff(f)
#plot(df, (x, 0, 2*pi))
kai = solve(df)

ans = []
for i in kai:
    f_temp = f.subs(x, i)
    ans.append(abs(f_temp))

print(trigsimp(max(ans)))