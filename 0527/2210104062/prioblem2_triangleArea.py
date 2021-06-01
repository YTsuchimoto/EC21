from numpy.lib.type_check import isreal
from sympy import *
import math

from sympy.solvers.solveset import solveset_real

x1=Symbol('x1', real=True)
y1=Symbol('y1', real=True)
x2=Symbol('x2', real=True)
y2=Symbol('y2', real=True)

t=Symbol('t', real=True)

x1=5*cos(2*t)
y1=5*sin(2*t)

x2=10*cos(t)
y2=10*sin(t)

ft = abs( (x1-2)*y2 - (x2-2)*y1 )/2

# ft=simplify(ft)
# print(ft)
# ft = 5*Abs(7*sin(t) - sin(2*t))
# absのまま上手く場合分けして微分するやり方が分からなかったので、手動で第一項、第二項の正負4通りに場合分け
# 極値を求めて最大値を探す

ans = 0

###############################
# when 0<= t < PI/2
ft = 5*Abs(7*sin(t) - sin(2*t))

# diff_ft = diff(ft)
# print(diff_ft)
# diff_ft = 35*cos(t) - 10*cos(2t)
# 上手くsolveさせる方法が分からなかったので二倍角( cos(2t)=2*(cos(t)**2)-1 )を適用してからsolve

diff_ft = 35*cos(t) - 10*( 2*(cos(t)**2)-1 )

anss = solve(Eq(diff_ft,0), t)
for a in anss:
    ft_subs=simplify(ft.subs(t,a))
    # print("when t  = " + str(a) + "\n   f(t) = " + str(ft_subs) )
    if 0 <= a and a < math.pi/2 : #　場合分けの条件に適合しているかチェック
        ans=max(ans,ft_subs)

# print("=================================")
###############################
# when PI/2 <= t < PI
ft = 35*sin(t)+5*sin(2*t)
diff_ft = 35*cos(t) + 10*( 2*(cos(t)**2) -1 )

anss = solve(Eq(diff_ft,0), t)
for a in anss:
    ft_subs=simplify(ft.subs(t,a))
    # print("when t  = " + str(a) + "\n   f(t) = " + str(ft_subs) )
    if math.pi/2 <= a and a < math.pi :
        ans=max(ans,ft_subs)

# print("=================================")
###############################
# when PI<= t < 3*PI/4 
ft = -35*sin(t)+5*sin(2*t)
diff_ft = -35*cos(t) + 10*( 2*(cos(t)**2) -1 )

anss = solve(Eq(diff_ft,0), t)
for a in anss:
    ft_subs=simplify(ft.subs(t,a))
    # print("when t  = " + str(a) + "\n   f(t) = " + str(ft_subs) )
    if math.pi <= a and a < 3*math.pi/4 : 
        ans=max(ans,ft_subs)

# print("=================================")
###############################
# when 3*PI/4<= t < PI 
ft = -35*sin(t)-5*sin(2*t)
diff_ft = -35*cos(t) - 10*( 2*(cos(t)**2) -1 )

anss = solve(Eq(diff_ft,0), t)
for a in anss:
    ft_subs=simplify(ft.subs(t,a))
    # print("when t  = " + str(a) + "\n   f(t) = " + str(ft_subs) )
    if 3*math.pi/4 <= a and a < 2*math.pi :
        ans=max(ans,ft_subs)

print ("answer is "+str(ans))
