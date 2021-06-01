# -*- coding: utf-8 -*-
# 2210104010 浦上太一

def is_prime(n):
    for i in range(2, n + 1):
        if i * i > n:
            break
        if n % i == 0:
            return False
    return n != 1


def greedy_method(S):
    Sa = []
    Sb = []
    for n in S:
        if sum(Sa) <= sum(Sb):
            Sa.append(n)
        else:
            Sb.append(n)
    return [Sa, Sb]

# def sabun_method(S):


def main():
    S = []
    for i in range(1, 101):
        if is_prime(i):
            S.append(i)
    S.reverse()
    Sa, Sb = greedy_method(S)
    print("Sa: {}".format(Sa))
    print("Sb: {}".format(Sb))
    print("要素の総和の差の絶対値の最小値: {}".format(abs(sum(Sa)-sum(Sb))))


if __name__ == '__main__':
    main()