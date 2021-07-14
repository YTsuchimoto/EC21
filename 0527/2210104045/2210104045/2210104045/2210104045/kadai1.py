import numpy as np
import random

sosuu = [2]
A = 100
for L in range(3, A, 2):
    for L2 in sosuu:
        if L % L2 == 0:
            break
    else: 
    	sosuu.append(L)
print(sosuu)

m=100
m2=m
i=0
while i<100:
	random.shuffle(sosuu)
	l=list(np.array_split(sosuu, 2))
	m=abs(np.sum(l[0])-np.sum(l[1]))
	if m2>m:
		m2=m
		print(m2)
	if m==m2:
		i=i+1
	#if m==0:
		#break
		
print('最小値:'+str(m))
print('SA:'+str(np.sort(l[0])))
print('SB:'+str(np.sort(l[1])))
