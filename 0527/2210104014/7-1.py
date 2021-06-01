#!/usr/bin/python



A = []
for i in range(2, 100):
    flag = 0
    for j in range(2, i//2 + 1):
        if (i%j == 0):
            flag = 1
            break
    if flag == 0:
        A.append(i)
print(A)


len_A = len(A)
B = [0] * len_A
min = 999999
min_B = []
while(1):
    S1 = []
    S2 = []
    for i in range(len_A):
        if B[i] == 0:
            S1.append(A[i])
        else:
            S2.append(A[i])
    
    can = abs(sum(S1) - sum(S2))
    if can < min:
        min = can
        min_B = B

    i = 0
    while(1):
        if B[i] == 0:
            B[i] = 1
            break
        else:
            B[i] = 0
            i += 1

    if B[len_A - 1] == 1:
        break
    #print(B)

S1 = []
S2 = []
for i in range(len_A):
    if min_B[i] == 0:
        S1.append(A[i])
    else:
        S2.append(A[i])
print("SA:")
print(S1)
print("SB:")
print(S2)