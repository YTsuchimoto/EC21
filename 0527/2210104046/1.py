def bag(n,m,w,v):
    res = [[0 for j in range(m+1)]for i in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,m+1):
            res[i][j] = res[i-1][j]
            if j>=w[i-1] and res[i][j]<res[i-1][j-w[i-1]]+v[i-1]:
                res[i][j] = res[i-1][j-w[i-1]]+v[i-1]
    return res
def show(n,m,w,res):
    print( u"maximum = %d"%res[n][m])
    s1 = []
    s2 = []
    sum1 = 0
    sum2 = 0
    x = [False for i in range(n)]
    j = m
    for  i in range(n,0,-1):
        if res[i][j]!=res[i-1][j]:
            x[i-1] = True
            j-=w[i-1]
    print(u"s1")
    for i in range(n):
        if x[i]:
            s1.append(w[i])
            sum1 += w[i]
    print(s1)
    print("sum1",sum1)

    print(u"s2")
    for i in range(n):
        if w[i] not in s1:
            s2.append(w[i])
            sum2 += w[i]
    print(s2)
    print("sum2",sum2)
    difference = sum1-sum2
    print("difference",difference)
    return s1,s2
    
def primenum():
    num=[]
    i=2
    for i in range(2,100):
        j=2
        for j in range(2,i):
            if(i%j==0):
                break
        else:
            num.append(i)
    return num

def sum(num):
    s = 0
    for i in range(len(num)):
        s += num[i]
        return s
    
num = primenum()
n = 25
s = sum(num)
c= 530
w=num
v=num
res=bag(n,c,w,v)
show(n,c,w,res)
