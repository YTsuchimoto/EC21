# -*- coding: utf-8 -*-

###########################################################################
#問題1
#1~100までの素数の集合をSとする．
#SをS_AとS_Bに分けたとき，それぞれの要素の総和の差の絶対値の最小値とその時のS_A，S_Bを求めよ．
###########################################################################
#集合Sを求める
s = []
for i in range(2, 100):
    is_primenumber = True
    for j in range(2, i//2+1):
        if(i % j == 0):
            is_primenumber = False
            break
    if is_primenumber == True:
        s.append(i)

#とりあえず交互にS_AとS_Bに割り振る
s_a = []
s_b = []
for i in range(0, len(s)):
    if(i % 2 == 0):
        s_a.append(s[i])
    else:
        s_b.append(s[i])

#収束するまで
#総和が大きいほうから小さいほうへ，総和の差未満の値のうち最大のものを移動
while(True):
    d = abs(sum(s_a) - sum(s_b))
    if(sum(s_a) > sum(s_b)):
        tmp = [x for x in s_a if(x < d)]
        if(tmp == []):
            break
        else:
            target = max(tmp)
            s_a.remove(target)
            s_b.append(target)
    else:
        tmp = [x for x in s_b if(x < d)]
        if(tmp == []):
            break
        else:
            target = max(tmp)
            s_b.remove(target)
            s_a.append(target)

#出力
print('問題1')
print('要素の総和の差の絶対値: ' + str(abs(sum(s_a) - sum(s_b))))
print('s_a: ' + str(s_a))
print('s_b: ' + str(s_b))
print()

#実行結果
#要素の総和の差の絶対値: 2
#s_a: [2, 11, 17, 41, 59, 67, 73, 83, 97, 37, 29, 13]
#s_b: [3, 7, 19, 43, 53, 61, 71, 79, 89, 47, 31, 23, 5]


###########################################################################
#問題2
#平面上に原点Oを中心とする半径5と10の同心円C1とC2がありOから距離2のところに定点Aがある．
#動点P1，P2がそれぞれC1，C2上を一定の速さで反時計回りに回転している．
#時刻t=0でO,A,P1,P2がこの順に一直線上に並び，また，P1の角速度はP2の2倍とする．
#△A P1 P2　の面積の最大値を求めよ．
###########################################################################
import sympy

#P2の角度をΘ（Θ>0）として，ベクトルAP1とAP2を定義
theta = sympy.Symbol('theta', positive=True)
AP1 = [5*sympy.cos(2*theta)-2, 5*sympy.sin(2*theta)]
AP2 = [10*sympy.cos(theta)-2, 10*sympy.sin(theta)]

#△A P1 P2　の面積（後で絶対値を取る）
S = (AP1[0]*AP2[1] - AP1[1]*AP2[0]) / 2

#三角関数を展開して，2ΘをΘで書き換え
S = sympy.expand(S, trig=True)

#SをΘで微分
dS = sympy.diff(S, theta)

#dS=0を解いて，解の候補として，Sが極値を取るときの0を求める
cand = sympy.solve(sympy.diff(S, theta))

#候補についてSを計算し（ここで絶対値を取る），Sの最大値とその時のΘを求める
S_max = 0.0
max_theta = []
for value in cand:
    tmp = float(abs(S.subs(theta,value)))
    if(tmp >= S_max):
        if(tmp > S_max):
            S_max = tmp
            max_theta.clear()
        max_theta.append(value)

#出力
print('問題2')
print('△A P1 P2　の面積の最大値: ' + str(S_max))
print('面積最大のときの∠P2 O A: ' + str(max_theta))

#実行結果
#△A P1 P2　の面積の最大値: 36.30921887069454
#面積最大のときの∠P2 O A  : [2*atan(sqrt(15)/3)]

