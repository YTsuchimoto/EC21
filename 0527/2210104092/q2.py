import sympy
t=sympy.Symbol('t')
p1x=5*sympy.cos(2*t)
p1y=5*sympy.sin(2*t)
p2x=10*sympy.cos(t)
p2y=10*sympy.sin(t)
num=sympy.simplify((1/2)*((p1x-2)*p2y-(p2x-2)*p1y))
dif=sympy.diff(num,t)
ans=sympy.solve(dif,t)
smax=0
for i in ans:
    s=abs(num.subs(t,i))
    if s>smax:
        smax=s
print(smax)