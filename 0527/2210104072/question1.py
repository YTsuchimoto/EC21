import itertools

a = []
for i in range(2, 100):
    flag = 0
    for j in range(2, i // 2 + 1):
        if (i % j == 0):
            flag = 1
            break
    if flag == 0:
        a.append(i)
#sum is 1060

for j in reversed(range(0,int(sum(a)/2))):
    for i in range(len(a)):
        for pair in itertools.combinations(a,i):
            if sum(pair)==j:
                break
        else:
            continue
        break
    else:
        continue
    break

print("SA=",end="");print(pair)
print("SB is the other.")
print("difference is ",end="");print(int((sum(a)/2-sum(pair))*2))