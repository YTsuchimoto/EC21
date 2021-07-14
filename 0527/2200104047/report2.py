import sympy as sym

t = sym.Symbol('t', real=True)

#外積により三角形の面積を求める
S = ((5*sym.cos(2*t)-2)*10*sym.sin(t) - 5*sym.sin(2*t)*(10*sym.cos(t)-2))/2
S = sym.simplify(S)
dS = sym.diff(S)
sol = sym.solve(dS, t)

op=[]
for i in sol:
    op.append(S.subs(t,i))

#外積により負の面積も出るので、それに関する処理をしている
if sym.simplify(min(op))>0:
    print(sym.simplify(max(op)))
else:
    if (-1)*sym.simplify(min(op))>sym.simplify(max(op)):
        print((-1)*sym.simplify(min(op)))
    else:
        print(sym.simplify(max(op)))
