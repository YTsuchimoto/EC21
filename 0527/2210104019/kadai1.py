def is_sosuu(n):
  for _n in range(2,n):
    if n%_n==0:
      return False
  return True

def sosuulist(_min = 2, _max=100):
  ret = []
  for n in range(_min, _max):
    if is_sosuu(n):
      ret.append(n)
  return ret

ans = 100
ansS = []
sosuu_2_100 = sosuulist(2,100)
for i in range(2**len(sosuu_2_100)):
  Sa, Sb = set(), set()
  tmp = i
  for j in range(len(sosuu_2_100)):
    if tmp%2==0:
      Sa.add(sosuu_2_100[j])
    else:
      Sb.add(sosuu_2_100[j])
    tmp = tmp//2
  # print(Sa, Sb)
  # print(abs(sum(Sa) -sum(Sb)))
  if ans > abs(sum(Sa) -sum(Sb)):
    ans = abs(sum(Sa) -sum(Sb))
    # print(Sa, Sb, ans)
    ansS = [Sa, Sb]
    if ans==0:
      break

_min = abs(sum(ansS[0]) -sum(ansS[1]))

print(f"最小値は{_min}")
print(f"Sa = {ansS[0]}")
print(f"Sb = {ansS[1]}")
