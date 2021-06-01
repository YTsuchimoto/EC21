#Problem 1 

# Generate S, a set of prime numbers between 1 to 100
def generatePrimeSet():
    S=[]
    for x in range (1, 101):
        count = 0
        for i in range(2, (x//2 + 1)):
            if(x % i == 0):
                count = count + 1
                break
        if (count == 0 and x != 1):
            S.append(x)
    print("S = ",S)
    return S


# Partition S into two subsets, SA and SB, such that the difference between the sum of elements in both sets is minimized
def findMinRecursive(S, n, sumSA, sumSB):

    # Return the absolute difference between SA and SB 
    if n < 0:
        return abs(sumSA - sumSB)

    # For every item S[n], we have two choices :
	
	# 1 : Include the current item in subset SA 
    include = findMinRecursive(S, n - 1, sumSA + S[n], sumSB)

    # 2 : Exclude the current item from subset SA 
    exclude = findMinRecursive(S, n - 1, sumSA, sumSB + S[n])
	
    # We return the minimum of two choices
    return min(include,exclude)
 

S = generatePrimeSet()
n = len(S)
res = findMinRecursive(S, n -1 ,0, 0)
print("The minimum value of the absolute value of difference of each sum of all elements of each SA and SB is :  ",res)