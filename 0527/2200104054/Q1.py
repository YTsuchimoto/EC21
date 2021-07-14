#q1

pn=[]

for i in range(2,100):

    flag = 0
    for j in range(2, i//2+1):
        if (i%j==0):
            flag=1
            break
        
    if flag == 0:
        pn.append(i) 
    
Sb = pn.copy()
ans = 10000
import itertools

for i in range(len(pn)):
         
    all = itertools.combinations(pn, i)
    for Sa in all:   
        Sb = pn.copy()
        
        for k in range(len(list(Sa))):
            Sb.remove(list(Sa)[k])
        
        if ans > abs(sum(list(Sa))-sum(Sb)):
            ans = abs(sum(list(Sa))-sum(Sb))
            aSa = list(Sa).copy()
            aSb = Sb.copy()

print('最小の絶対値は',ans)
print('その時、Sa',aSa)
print('Sb',aSb)

#最小の絶対値は 0
#その時、Sa [3, 41, 67, 71, 79, 83, 89, 97]
#Sb [2, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 43, 47, 53, 59, 61, 73]

