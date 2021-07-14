#!/usr/bin/env python
# coding: utf-8

# 問題1

# In[11]:


s=[]

for i in range(2,100):
    flag=0
    for j in range(2,i//2+1):
        if(i%j==0):
            flag=1
            break
    if flag==0:
        s.append(i)

print(s)


# In[14]:


s.reverse()

sa=[]
sb=[]
sa_sum=0
sb_sum=0

for i in range(len(s)):
    if (sa_sum>sb_sum):
        sb.append(s[i])
        sb_sum=sum(sb)
    else:
        sa.append(s[i])
        sa_sum=sum(sa)
        
sa.reverse()
sb.reverse()
print('sa = ',sa)
print('sb = ',sb)
print('|sa - sb| = ',abs(sa_sum-sb_sum))


# In[ ]:




