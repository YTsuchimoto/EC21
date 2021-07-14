#q2

import sympy as sym

t = sym.Symbol('t')

area = sym.simplify((1/2)*((5*sym.cos(2*t)-2)*(10*sym.sin(t))-(10*sym.cos(t)-2)*(5*sym.sin(2*t))))

dif = sym.diff(area,t)
s = sym.solve(dif,t)
aarea = 0

for solve in s:
    temparea = abs(area.subs(t,solve))
    if temparea>aarea:
        aarea=temparea
        
print('△AP1P2の面積の最大値は',aarea)

#△AP1P2の面積の最大値は 36.3092188706945