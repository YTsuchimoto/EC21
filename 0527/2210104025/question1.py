#SAとSBの要素の和
#差の絶対値の最小は0か1

a1 = [5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]
b = 2
c = 3 

for i in range(0, len(a1)):
  
  x = (a1[i]-1)/2
  x = int(x)
  y = x + 1

  b = b + x
  c = c + y 
  if b == c:
    True
  else:
    b = b - x + y
    c = c - y + x

#差を表示
print("差は", b-c)

a2 = [2,3]
a2.extend(a1)

a_reverse = a2[::-1]
#SAには素数リストの末尾だけ入れておく
SA = [a2[-1]]
#97が要素として含まれる方を考える。
n = b - a_reverse[0]

#素数かどうかを判定

for i in range(1, len(a2)):
  
  ele_1 = a_reverse[i]
  prime = 0
  if n > a2[-1]:
    n = n - ele_1 
    #素因数分解をして、素数でないなら1を返す
    for i in range(2,n):
      if n % i == 0:
        prime = 1

    if prime == 1:
      SA.append(ele_1)
    else:
      #素数なら
     n = n + ele_1

#nがリストの末尾より小さくなった時
for i in range(0, len(a2)):
  ele_2= a2[i]
  n2 = n - ele_2
  if n2 in a2 and n2 not in SA and ele_2 not in SA:
    SA.append(n2)
    SA.append(ele_2)
    break

print("SA =",SA)

for i in range(0, len(SA)):
  if SA[i] in a2:
    a2.remove(SA[i])

print("SB =", a2)