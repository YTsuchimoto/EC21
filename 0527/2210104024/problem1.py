# -*- coding: utf-8 -*-

S=[]
for i in range(2,100):
    flag = 0
    for j in range(2,i//2+1):
        if i%j==0:
            flag=1
            break
    if flag == 0:
        S.append(i)

dif_min=sum(S)
SA=[]
SB=[]
for i in range(pow(2,len(S)-1)):
    new_SA=[]
    new_SB=[]
    for j in range(len(S)):
        if i%2==0:
            new_SA.append(S[j])
        else:
            new_SB.append(S[j])
        i=i//2
    dif=abs(sum(new_SA)-sum(new_SB))
    if dif<dif_min:
        dif_min=dif
        SA=new_SA
        SB=new_SB
    if dif_min==0:
        break
        
print("最小値:",dif_min)
print("SA:",SA)
print("SB:",SB)