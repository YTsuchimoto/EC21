import numpy as np

def prime_num(n):
    judge = np.ones(n)
    judge[0] = 0
    for i in range(2, n + 1):
        for j in range(2, i//2 + 1):
            if i % j == 0:
                judge[i - 1] = 0
                break
    
    prime = []
    c = 0
    for i in judge:
        c+=1
        if i == 1: prime.append(c)
    
    # print(len(prime))
    print(prime)

    return prime


def find_max(x):
    dp = np.zeros((len(x) + 1, sum(x)//2 + 1))

    for i in range(len(x)):
        for j in range(sum(x)//2 + 1):
            if x[i] <= j:
                dp[i + 1][j] = max(dp[i][j - x[i]] + x[i], dp[i][j])
            else:
                dp[i + 1][j] = dp[i][j]
    
    # print(dp)

    ans = []
    a = sum(x)//2
    for i in reversed(range(len(x))):
        if dp[i + 1][a] == dp[i][a - x[i]] + x[i]:
            ans.append(x[i])
            a -= x[i]

    return ans

    

        


if __name__=="__main__":

    S = prime_num(100)
    S_a = find_max(S)
    S_b = list(set(S) ^ set(S_a))

    print("Sa = " + str(S_a))
    print("Sa total = " + str(sum(S_a)))
    print("Sb = " + str(S_b))
    print("Sb total = " + str(sum(S_b)))
    print("|Sa - Sb| = " + str(sum(S_b) - sum(S_a)))