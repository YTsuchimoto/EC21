# -*- coding: utf-8 -*-

#素数のリスト作成
def primeNumber(n):
    a = []
    for i in range(2, n+1):
        frag = 0
        for j in range(2, i // 2 + 1):
            if (i % j == 0):
                frag = 1
                break
        if frag == 0:
            a.append(i)
    return a

S = primeNumber(100)

#動的計画法
#(Saの合計) < (Sbの合計) であれば、(Sの合計) - 2(Saの合計) = (Sbの合計) - (Saの合計)
#今SaとSbそれぞれの合計値の差は絶対値で表すので、Sa <= Sbが常に成り立つとしても一般性を損なわない
#上記を満たすには(Sの合計) - (Saの合計) >= (Saの合計) つまり(Saの合計) <=(Sの合計) / 2 という条件のもとで調べればいい


S_all_sum = sum(S)
#S_all_sumが小数である場合は切り上げる
if S_all_sum % 2 == 0:
    S_all_sum_2 = int(S_all_sum / 2)
else:
    S_all_sum_2 = int(S_all_sum / 2 + 1)

#DPテーブルとどの素数を使ったかを調べるリストを作る
dp=[[0] * (S_all_sum_2 + 1) for i in range(len(S) + 1)]
Sa_0=[[[]for j in range(S_all_sum_2 + 1)]for i in range(len(S)+1)]

for i in range(len(S)):
    for j in range(S_all_sum_2 + 1):
        if j < S[i]:
            dp[i+1][j] = dp[i][j]
            Sa_0[i+1][j].extend(Sa_0[i][j])
        else:
            dp[i+1][j] = max(dp[i][j-S[i]] + S[i], dp[i][j])
            if (dp[i][j-S[i]] + S[i]) > dp[i][j]:
                Sa_0[i+1][j].extend(Sa_0[i][j-S[i]])
                Sa_0[i+1][j].append(S[i])
            else:
                Sa_0[i+1][j].extend(Sa_0[i][j])


dif = abs(S_all_sum - 2 * dp[len(S)][S_all_sum_2])
Sa=Sa_0[len(S)][S_all_sum_2]
for i in range(len(Sa)):
    S.remove(Sa[i])
Sb = S

print("Sa: ",Sa)
print("Sb: ",Sb)
print("Minimum Difference: ",dif)
