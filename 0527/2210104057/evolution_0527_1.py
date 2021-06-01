from itertools import combinations

# リストの分割の組み合わせ列挙
def split(a, i):
    l1 = list(combinations(a, i))
    l2 = [tuple(set(a) - set(x)) for x in l1]
    pairs = set((x, y) if x < y else (y, x) for x, y in zip(l1, l2))
    pairs = list(pairs)

    return pairs

def main():
    # 素数のリスト作成
    a = []
    for i in range(2, 100):
        flag = 0
        for j in range(2, i // 2 + 1):
            if (i % j == 0):
                flag = 1
                break
        if flag == 0:
            a.append(i)
    # print(a)

    # リストの分割方法の探索
    min = 1000
    result_pair = ((), ())
    for i in range(1, len(a)):
        pairs = split(a, i)
        for j in range(len(pairs)):
            d = abs(sum(pairs[j][0]) - sum(pairs[j][1]))
            if d < min:
                min = d
                result_pair = pairs[j]
    # print(min)
    print(result_pair)

if __name__ == '__main__':
    main()