import sympy
from sympy import sin, cos

theta = sympy.Symbol('theta', real = True, nonnegative = True)
# 二つの円の半径
r1 = 5
r2 = 10
# 点A
A_x = -2
A_y = 0

# 三角形の面積
area = ((r2*cos(2*theta)-A_x)*(r1*sin(theta)-A_y)-(r1*cos(theta)-A_x)*(r2*sin(2*theta)-A_y))/2
diff_area = sympy.diff(area, theta)

eq = sympy.solve(diff_area, theta)

area_max = 0 # 三角形の面積の最大値
for i in eq:
    if(area_max < abs(area.subs(theta,i))):
        area_max = area.subs(theta,i)
print('S max is {}'.format(area_max.evalf()))