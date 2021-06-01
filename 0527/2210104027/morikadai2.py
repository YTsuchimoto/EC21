#!/usr/bin/env python
# coding: utf-8

# In[30]:


import sympy

th=sympy.Symbol('th')
a1=2
a2=0

p11=5*sympy.cos(2*th)
p12=5*sympy.sin(2*th)
p21=10*sympy.cos(th)
p22=10*sympy.sin(th)

s=sympy.simplify(((p11-a1)*(p22-a2)-(p21-a1)*(p12-a2))/2)

diff=sympy.diff(s)
diffans=sympy.solve(diff)
ans=[]

for diffans in diffans:
    ans.append(abs(s.subs(th,diffans)))

print(sympy.simplify(max(ans)))



# In[ ]:





# In[ ]:
