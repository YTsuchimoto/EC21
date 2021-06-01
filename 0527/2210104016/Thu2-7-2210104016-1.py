'''
問題 1
1 ~ 100 までの素数の集合を S とする.
S を S_A と S_B に分けたときそれぞれの要素の総和の差の絶対値の
最小値とそのときの S_A, S_B を求めよ.
'''

from itertools import combinations
import numpy as np

# 素数判定
def is_prime(n):
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False
    return True

# 素数集合の生成
def make_prime_list(n):
    prime_list = []
    for i in range(2, n + 1):
        if is_prime(i):
            prime_list.append(i)
    return prime_list

# 組み合わせ探索
def solve(prime_list):
    sum_prime = np.sum(prime_list)
    ans = sum_prime
    S_A = []
    for i in range(1, len(prime_list) // 2 + 1):
        for comb in combinations(prime_list, i):
            sum_A = np.sum(comb)

            if abs(sum_prime - 2 * sum_A) < ans:
                ans = abs(sum_prime - 2 * sum_A)
                S_A = comb

        if ans == 0:
          break

    print('min_diff = {}'.format(ans))
    print('S_A = {}'.format(list(S_A)))
    print('S_B = {}'.format(list(set(prime_list) ^ set(S_A))))

if __name__ == '__main__':
    solve(make_prime_list(100))

# 2210104016
