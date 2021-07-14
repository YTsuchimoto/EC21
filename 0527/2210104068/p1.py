""" 
Author : VILLIN Victor .
Date : 2020-06-02 .
File : q1.py .

Description : None

Observations : None
"""

# == Imports ==
import itertools
# =============

def prime_numbers(max):
    """
    :param max: max>2 , maximum prime value to find, from 0
    :return: list of all primes < max
    """
    assert max > 1
    primes = []

    for i in range(2, max):
        is_prime = True
        for j in range(2, int(i**0.5)+1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
    return primes

def subsets(s, n):
    """
    :param s: original set
    :param n: size of the subsets
    :return: all subsets of s, of size n
    """
    return itertools.combinations(s, n)

def all_possible_subsets(s):
    for i in range(len(s)//2+1):
        print('building possible sets...', i)
        yield subsets(s, i+1)


def compute_absolute_difference(SA, SB):
    return abs(sum(SA)-sum(SB))


def exercice1():
    S = set(prime_numbers(100))

    min_diff = None

    for possible_subsets in all_possible_subsets(S):
        for p in possible_subsets:
            Sa = set(p)
            Sb = S.difference(Sa)

            diff = compute_absolute_difference(Sa, Sb)
            if min_diff is None or min_diff > diff:
                print(Sa, Sb, diff)
                min_diff = diff

    return min_diff



if __name__ == '__main__':

    result = exercice1()
    print(result)
    """
    Exercice 1 : 0 is the minimum possible distance, with
    Sa = {97, 67, 3, 71, 41, 79, 83, 89}
    Sb = {2, 5, 37, 7, 73, 11, 43, 13, 47, 17, 19, 61, 53, 23, 59, 29, 31}
    """

