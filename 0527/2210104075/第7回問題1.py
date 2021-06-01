S = [] # 素数集合
for i in range(2, 100):
    flag = 0
    for j in range(2, i//2+1):
        if(i%j==0):
            flag=1
            break
    if flag == 0:
        S.append(i)

SA = [] # 素数集合A
SB = [] # 素数集合B

for i in range(1, len(S)+1):
    if(sum(SA) <= sum(SB)):
        SA.append(S[len(S)-i])
    else:
        SB.append(S[len(S)-i])
print(SA)
print(SB)
print(abs(sum(SA)-sum(SB)))