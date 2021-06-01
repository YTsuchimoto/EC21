import numpy as np
import itertools

#素数列挙関数
def seachPrimeNum(N):
    max = int(np.sqrt(N))
    seachList = [i for i in range(2,N+1)]
    primeNum = []
    while seachList[0] <= max:
        primeNum.append(seachList[0])
        tmp = seachList[0]
        seachList = [i for i in seachList if i % tmp != 0]
    primeNum.extend(seachList)
    return primeNum

#素数のリストの作成
S=seachPrimeNum(100)

#全通りのパターンから解を探し出す
#(Saの要素数<=Sbの要素数とすることで計算時間を半減させる。)
#ansが０になった時点でこれ以上の解は存在しないため終了させる

ans=100000000000000
for i in range(int(len(S)/2)+1):
    for Sa in itertools.combinations(S, i):
        Sb=list(set(S)-set(Sa))
        Sa=list(Sa)
        sumSa=sum(Sa)
        sumSb=sum(Sb)
        dif=abs(sumSa-sumSb)
        if dif<ans:
            ans=dif
            ansSa=Sa
            ansSb=Sb
        if ans==0:
             break

print("dif : "+str(ans))
print("Sa : "+str(Sa))
print("Sb : "+str(Sb))
