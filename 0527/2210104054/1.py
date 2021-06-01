import itertools
s = []
for i in range(2, 98):
    flag = 0
    for j in range(2, i//2+1):
        if(i%j==0):
            flag = 1
            break
    if flag == 0:
            s.append(i)
print(len(s))

li = list(range(0,len(s)))

minimum = float('inf')
ansA = []
ansB = []
print(2 ** len(s))
for i in range(2 ** len(s)):
    Sa = []
    Sb = []
    #print("pattern {}:".format(i), end="")
    for j in range(len(s)):
        if((i >> j) & 1):
            Sa.append(s[j])
        else:
            Sb.append(s[j])
    if(abs(sum(Sa) - sum(Sb)) < minimum):
        minimum = abs(sum(Sa) - sum(Sb))
        ansA = Sa
        ansB = Sb
        print("更新:{}".format(i), end="")
    
print("最小値は {}".format(minimum), end="")
print("-----Sa------")
print(ansA)
print("-----Sb------")
print(ansB)