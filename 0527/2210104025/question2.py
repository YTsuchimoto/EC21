import sympy 

#角速度をwとする。
w = sympy.Symbol("w")

#Aはx軸上にあるとする。
A_x, A_y = 2, 0
#P1,P2の座標
P1_x, P1_y = 5*sympy.cos(2*w), 5*sympy.sin(2*w)
P2_x, P2_y = 10*sympy.cos(w), 10*sympy.sin(w)

#求める面積をSとする。3点を原点に平行移動させて面積Sを求める。
S = sympy.simplify((1/2)*((P1_x - A_x)*(P2_y - A_y) - (P2_x - A_x)*(P1_y - A_y)))

#面積Sをwで微分する。
S_diff = sympy.diff(S, w)
#S'(w) = 0 として方程式を解く。
w_ans = sympy.solve(S_diff,w)

#解を順に代入して最大値を求める。
max_S = 0
for i in w_ans:
  if max_S < abs(S.subs(w, i)):
    max_S = abs(S.subs(w, i)) 

print("面積Sの最大値は", max_S)