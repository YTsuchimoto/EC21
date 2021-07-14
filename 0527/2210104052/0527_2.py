import sympy as sm
t = sm.Symbol('t')
w = sm.Symbol('w')

s = 1/2*(10*sm.sin(w*t)*(5*sm.cos(2*w*t))-5*sm.sin(2*w*t)*(10*sm.cos(w*t)))
_s = sm.diff(s,t)
argt = sm.solve(_s,t)
ans = []
for i in argt:
    ans.append(s.subs(t,i))
print("max area:",max(ans))
