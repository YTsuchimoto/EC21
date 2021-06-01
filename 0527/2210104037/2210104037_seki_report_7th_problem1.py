# -*- coding: utf-8 -*-
"""
Created on Thu May 27 13:27:57 2021
@author: Yuya Seki
This problen is symmetrical for S_A and S_B, that is, 
summation of S_A exceeds an half of total sum of S (= W) by delta,
summation of S_B falls W by delta simultaneously.
Therfore, we can solve it applying Dynamic Programming (DP), 
which works out Knapsack problem, well-known NP-complete problem.
Note that desired difference is given from double of delta.
"""

def knapsack(N, W, weight):
    # initialization
    dp = [[0]*(W+1) for i in range(N+1)]
    
    # DP
    for i in range(N):
        for w in range(W + 1):
            if weight[i] <= w:  # can pick up ith element in addition to the state of dp[i][w-weight[i]
                dp[i + 1][w] = max(dp[i][w - weight[i]] + weight[i], dp[i][w])
            else:  # can't pick up
                dp[i + 1][w] = dp[i][w]
    return dp
# knapsack

if __name__ == '__main__':
    # make list contains all prime numbers less than 100
    # it is quite computationally intensive method
    S = []
    for i in range(2, 100):
        flag = 0
        for j in range(2, i // 2 + 1):
            if (i % j == 0):
                flag = True
                break
        if not flag:
            S.append(i)
    #S = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]
    
    # size of S
    N = len(S)
    
    # double every element in S
    # in order for capacity of the knapsack to be integer 
    # halve output later
    # It's not essential process (only for keeping it consistent with the explanation above.).
    for i in range(N):
        S[i] = S[i] * 2
    
    # size of S
    N = len(S)
        
    # capacity of the knapsack
    W = sum(S) // 2
    
    # conduct dynamic programming
    dp = knapsack(N, W, S)
    
    # back track DP table
    S_A = []
    current_w = W
    for i in range(N):
        # if (N - i)th element is picked up
        # N - i - 1 = 24, 23, ..., 0 (subtract 1 because it is list index)
        if(dp[N - i][current_w] == dp[N - i - 1][current_w - S[N - i - 1]] + S[N - i - 1]):
            # add (N - i)th element into S_A
            S_A.append(S[N - i - 1])
            # now search from 1st to (N - i - 2)th elements
            # redundunt capacity is given by (current_w - S[N - i - 1])
            current_w = current_w - S[N - i - 1]
    
    # halve output
    for i in range(N):
        S[i] = S[i] // 2
    
    # halve output
    for i in range(len(S_A)):
        S_A[i] = S_A[i] // 2
    
    # S_B = S\S_A
    S_B = list(set(S) - set(S_A))
    
    # sort (for easy understanding)
    S_A.sort()
    S_B.sort()
    
    # print answer
    # print("Summation of S_A calculated from DP algorithm: {}".format(dp[N][W] // 2))
    print("Answer: {}".format(sum(S_A) - sum(S_B)))
    print("That is, min. of differnce of the summation of two subsets.\n")
    print("One example of the subsets that gives the min. is as follows:")
    print("S_A: {}, summation: {}".format(S_A, sum(S_A)))
    print("S_B: {}, summation: {}".format(S_B, sum(S_B)))