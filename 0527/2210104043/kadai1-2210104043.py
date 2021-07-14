# coding: utf-8
# 2210104043 Yusei Takayama
import math
from itertools import combinations

def make_primes_list(x):
    if x < 2: return []

    primes = [i for i in range(x)]
    primes[1] = 0

    for prime in primes:
        if prime > math.sqrt(x): break
        if prime == 0: continue
        for non_prime in range(2 * prime, x, prime): primes[non_prime] = 0

    return [prime for prime in primes if prime != 0]

def solve(s):
    m = 10e9
    S_A = []
    S_B = []
    for k in range(1, len(s) // 2 + 1):
        for s_a in combinations(s, k):
            s_b = set(s) ^ set(s_a)
            miria = abs(sum(s_a) - sum(s_b))
            if miria < m:
                m = miria
                S_A = s_a
                S_B = s_b
                if m == 0:
                    return m, list(S_A), list(S_B)

    return m, list(S_A), list(S_B)

# dp 書かなくてごめんなさい
def main():
    s = make_primes_list(100)
    m, s_a, s_b = solve(s)
    print("min = " + str(m))
    print("S_A")
    print(s_a)
    print("S_B")
    print(s_b)

if __name__ == '__main__':
    main()
