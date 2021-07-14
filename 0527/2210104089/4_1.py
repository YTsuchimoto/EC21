s = []
for i in range(2,100):
    flag = 0
    for j in range(2, i//2 + 1):
        if i % j == 0:
            flag = 1
            break
    if flag == 0:
        s.append(i)

sa = []
sb = []
list.sort(s, reverse=True)
dif = s[0]
sa.append(s[0])
for i in range(1, len(s)):
    if dif >= 0:
        dif -= s[i]
        sb.append(s[i])
    elif dif < 0:
        dif += s[i]
        sa.append(s[i])
print("min:{}".format(dif))
print("SA:{}".format(sa))
print("SB:{}".format(sb))
