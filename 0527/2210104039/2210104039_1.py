from itertools import combinations

def prime_factorize(n: int) -> list:
    return_list = []
    while n % 2 == 0:
        return_list.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            return_list.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        return_list.append(n)
    return return_list

def main():
    S = []
    for i in range(2,101):
        l = prime_factorize(i)
        if len(l) == 1:
            S.append(i)
    ans = sum(S)
    sum_all = sum(S)
    for i in range(1,len(S)//2+1):
        for v in combinations(S,i):
            sum_Sa = sum(v)
            if ans > abs(sum_all-2*sum_Sa):
                ans = abs(sum_all-2*sum_Sa)
                S_a = list(v)
                S_b = list(set(S)^set(v))
    print("the answer is {}".format(ans))
    print("S_A is {}".format(S_a))
    print("S_B is {}".format(S_b))

if __name__ == '__main__':
    main()