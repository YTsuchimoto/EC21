import sympy as sym
from sympy.plotting import plot
from sympy import pi

#xを変数として定義する
θ = sym.Symbol('θ',real=True)

#３点の座標が与えられた時の三角形の面積の求め方は、1/2*|(x1−x3)(y2−y3)−(x2−x3)(y1−y3)|
#絶対値は最後に考えることにする（最大と最小の比較により）
f=sym.simplify(1/2*((5*sym.cos(2*θ)-2)*10*sym.sin(θ)-5*sym.sin(2*θ)*(10*sym.cos(θ)-2)))
print('f(θ) = {}'.format(f))

#微分し極値を求める
df = f.diff(θ)
print('f\'(θ) = {}'.format(df))
critical_points = sym.solve(df)
print(critical_points)
MaxS=0
for critical_point in critical_points:
    fx=f.subs(θ, critical_point)
    if fx<0:
        S=-1*fx
    else:
        S=fx
    if MaxS<S:
        MaxS=S
print(MaxS)
