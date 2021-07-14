import numpy as np

flag = 1
S = []
for i in range(2,100):
    flag = 1
    for j in range(2,int(i/2)+1):
        if i % j == 0:
            flag = 0
            break
    if flag == 1:
        S.append(i)
SA = []
SB = []
S.reverse()
for s in S:
    if np.sum(SA) > np.sum(SB):
        SB.append(s)
    else:
        SA.append(s)
dif = abs(np.sum(SA) - np.sum(SB))
print("S_a",SA)
print("S_b",SB)
print("difference",dif)
