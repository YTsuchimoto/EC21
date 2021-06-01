
# 半分全列挙で差を最小化する

import sys
import bisect

primes = []
for i in range(2,100) :
    isDivided = False
    for j in range(2, i) :
        if j*j > i :
            break
        if i%j == 0 :
            isDivided = True
            break
    if not isDivided :
        primes.append(i)

# primesの前半から作れる和のリストを作成
sumToSetDict_1 = {}
for bit in range(2**(len(primes)//2)) :
    pickedPrimes =[]
    for i in range(len(primes)//2):
        if (bit>>i) & 1 :
            pickedPrimes.append(primes[i])
    sumToSetDict_1[sum(pickedPrimes)] = pickedPrimes

# primesの後半から作れる和のリストを作成
sumToSetDict_2 = {}
for bit in range( 2**((len(primes)+1)//2) ):
    pickedPrimes = []
    for i in range(len(primes)//2, len(primes)):
        if (bit>>(i-len(primes)//2)) & 1:
            pickedPrimes.append(primes[i])
    sum_tmp=sum(pickedPrimes)
    sumToSetDict_2[sum_tmp]=pickedPrimes


ans = sys.maxsize
ansSet_1stHalf = []
ansSet_2ndHalf = []

primesSum = sum(primes)
sortedSumSet2 = sorted(sumToSetDict_2.keys())

# 前半のどの和を選ぶか固定して、もっともprimesSumの半分に近い後半の選び方を二分探索
for sumInSet1 in sumToSetDict_1.keys() :
    rest = primesSum//2-sumInSet1
    index = bisect.bisect(sortedSumSet2,rest) # restを超えるindexを二分探索　index-1とindexが候補
    if not index==0:
        tmpSum = sortedSumSet2[index-1]
        if ans > abs(rest-tmpSum):
            ans = abs(rest-tmpSum)
            ansSet_1stHalf = sumToSetDict_1[sumInSet1]
            ansSet_2ndHalf = sumToSetDict_2[tmpSum]
    if not index==len(sortedSumSet2) :
        tmpSum = sortedSumSet2[index] 
        if ans > abs(rest-tmpSum) :
            ans = abs(rest-tmpSum)
            ansSet_1stHalf = sumToSetDict_1[sumInSet1]
            ansSet_2ndHalf = sumToSetDict_2[tmpSum]

print("minimum difference:"+str(ans))
ansSet = ansSet_1stHalf
ansSet.extend(ansSet_2ndHalf)
print("S_a:"+str(ansSet))
print("S_b:"+str(sorted(set(ansSet) ^ set(primes)))) # ansSetの補集合を出力
