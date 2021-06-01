from tqdm import tqdm

# 素数生成
s = []
for i in range(2, 100):
    flag = 0
    for j in range(2, i//2+1):
        if(i%j==0):
            flag = 1
            break
    if flag == 0:
        s.append(i)

# 最小値の探索
ans = 100000
sum_s = sum(s)
for i in tqdm(range(pow(2, len(s)))):
    s_a = [s[j] for j in range(len(s)) if i >> j & 1]
    difference = abs(sum_s - sum(s_a) - sum(s_a))
    if ans == 0:
        break
    if difference < ans:
        ans = difference
        ans_s_a = s_a
ans_s_b = list(set(s) - set(ans_s_a))
ans_s_b.sort()
print("min:", ans)
print("Sa:", ans_s_a)
print("Sb:", ans_s_b)