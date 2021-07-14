import numpy as np

# generate prime numbers
S = []
for i in range(2, 100):
    flag = 0
    for j in range(2, i // 2 + 1):
        if i % j == 0:
            flag = 1
            break
    if flag == 0:
        S.append(i)

S = np.array(S)


# knapsack-like dp
# save bit arrays as integer in items
sumS = np.sum(S)
if sumS % 2 == 0:
    cons = sumS // 2
else:
    cons = sumS // 2 + 1

dp = np.zeros((len(S) + 1, cons + 1), dtype='int32')
items = np.zeros_like(dp, dtype='>u4')


# dp loop
for i in range(len(S)):
    for j in range(cons + 1):
        if j < S[i]:
            dp[i + 1][j] = dp[i][j]
            items[i + 1][j] = items[i][j]
        else:
            tmp = dp[i][j - S[i]] + S[i]
            if tmp > dp[i][j]:
                dp[i + 1][j] = tmp
                items[i + 1][j] = items[i][j - S[i]] | 1 << i
            else:
                dp[i + 1][j] = dp[i][j]
                items[i + 1][j] = items[i][j]


# convert int to bins
indSa = map(lambda x: items[-1][-1] >> x & 1, range(len(S)))
indSa = np.array(list(indSa)) == 1
indSb = ~indSa


# result
print(f'diff:{sumS - 2 * dp[-1][-1]}, Sa:{S[indSa]}, Sb{S[indSb]}')
