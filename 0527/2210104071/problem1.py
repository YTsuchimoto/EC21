'''
2210104071 寳来輝弥
'''

S = []
SA = []
SB = []

def comb(n, m): #n個の中からm個取り出す
    if m == 1:
        for i in range(n):
            yield [i]
    else:
        # n個からm-1個取り出す組み合わせを求め、その末尾にm個目の選択要素をくっつける
        for c in comb(n, m - 1):
            for i in range(c[-1] + 1, n):
                yield c + [i]

for i in range(2, 100):
    flag = 0
    for j in range(2, i//2+1):
        if(i%j == 0):
            flag = 1
            break
    if flag == 0:
        S.append(i)

diff = 100000
diff_min = 100000

for i in range(1, 25): #i:SAの要素数
    if(diff == 0):
        break
    for c in comb(25, i): #SAにappendするSの要素番号を決定
        if(diff == 0):
            break
        for j in range(i):
            if(diff == 0):
                break
            SA.append(S[c[j]])
            if(len(SA) == i):
                SB = list(set(S) - set(SA)) #ここで作られるSBはソートされていない
                diff = abs(sum(SA) - sum(SB))
                if(diff < diff_min):
                    SA_ans = SA
                    SB_ans = SB
                    diff_min = diff
                if(diff == 0):
                    break
        SA = []

print('SA=', SA_ans, sep='')
print('SB=', sorted(SB_ans), sep='')
print('diff_min:', diff_min, sep='')
