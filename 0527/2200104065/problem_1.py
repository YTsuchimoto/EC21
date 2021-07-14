# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# Super naive primal search algorithm
prime = []
for i in range(2, 100):
    is_composite = 0
    for j in range(2, i//2 + 1):
        if i % j == 0:
            is_composite = 1
            break
    if is_composite == 0:
        prime.append(i)
        
# Implementation of the greedy algorithm described here:
# https://en.wikipedia.org/wiki/Greedy_number_partitioning

# This is a 7/6 approximation.  It's possible there is some trick I am
# not understanding due to the numbers being primes.

prime.sort(reverse=True)
set_a = []
set_b = []

for n in prime:
    if sum(set_a) < sum(set_b):
        set_a.append(n)
    else:
        set_b.append(n)
        
print("Set A:     " + str(set_a))
print("  (Sum:)   " + str(sum(set_a)))
print()
print("Set B:     " + str(set_b))
print("  (Sum:)   " + str(sum(set_b)))
print()
print("Difference:" + str(abs(sum(set_a) - sum(set_b))))
