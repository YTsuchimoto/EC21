import numpy as np
import copy


def zettai(sa, sb):
    sa_sum = sum(sa)
    sb_sum = sum(sb)
    return abs(sa_sum - sb_sum)


s = []
sa = []
sb = []
ans = float('inf')

for i in range(2, 100):
    flag = 0
    for j in range(2, i // 2 + 1):
        if i % j == 0:
            flag = 1
            break
    if flag == 0:
        s.append(i)

s_div = np.zeros(len(s))

a = bin(2 ** len(s))
b = a[0]

for k in range(2 ** len(s)):
    k_bin = bin(k)
    if len(str(k_bin)) <= 4:
        if k_bin[-2] == '1':
            s_div[2] = 1
        if k_bin[-1] == '1':
            s_div[1] = 1
    else:
        for l in range(3, len(k_bin) - 2):
            if k_bin[-l] == '1':
                s_div[l] = 1
    # くみを変えてforで回す
    for i in range(len(s)):
        if s_div[i] == 0:
            sa.append(s[i])
        else:
            sb.append(s[i])
    tmp = zettai(sa, sb)
    if tmp < ans:
        ans = copy.deepcopy(tmp)
        ans_sa = copy.deepcopy(sa)
        ans_sb = copy.deepcopy(sb)
    s_div = np.zeros(len(s))
    sa.clear()
    sb.clear()

print('最小値: ' + str(ans))
print('SA = ' + str(ans_sa))
print('SB = ' + str(ans_sb))
