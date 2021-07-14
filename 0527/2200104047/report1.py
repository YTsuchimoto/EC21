S=[]
for i in range(2,101):
    flag = 0
    for j in range(1,i+1):
        if i%j == 0:
            flag = flag + 1
    if flag==2:
        S.append(i)
S.reverse()

A=[]
B=[]
for i in S:
    if sum(A)<sum(B):
        A.append(i)
    else:
        B.append(i)
print("A: ", A)
print("B: ", B)
print("sum of A: ", sum(A))
print("sum of B: ", sum(B))
print("A - B: ", sum(A)-sum(B))        
