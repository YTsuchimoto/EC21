#!/usr/bin/env python
# coding: utf-8

# In[20]:


import math
a=[]
sowa=0
for i in range(2,101):
    flag=0
    for j in range(2,int(math.sqrt(i))+1):
        if(i%j==0):
            flag=1
            break
    if flag==0:
        a.append(i)
        sowa+=i

dp=[0 for i in range(10000)]
tansaku=[0 for i in range(10000)]
dp[0]=1
sowa2=0
for i in a:
    sowa2+=i
    for j in range(sowa2,-1,-1):
        if dp[j]==1:
            dp[j+i]=1
            if tansaku[j+i]==0:
                tansaku[j+i]=i


ansmin=99999999
anssum=-1
for i in range(sowa):
    if i>sowa-i:
        break
    if ansmin>(sowa-i)-i and dp[i]==1:
        ansmin=(sowa-i)-i
        anssum=i
b=[]
c=[]
while anssum!=0:
    b.append(tansaku[anssum])
    anssum=anssum-tansaku[anssum]
    if anssum==0:
        break;

for i in a:
    if i not in b:
        c.append(i)
print("S_A")
print(b)
print(sum(b))
print("S_B")
print(c)
print(sum(c))

print("dif:"+str(sum(b)-sum(c)))


# In[ ]:





# In[ ]:





# In[ ]:
