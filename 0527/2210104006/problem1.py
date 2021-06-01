#!/usr/bin/env python3

# find prime numbers
prime = []  # save prime number
for i in range(2, 100):
    flag = 0
    for j in range(2, i // 2 + 1):
        if (i % j == 0):
            flag = 1
            break
    if flag == 0:
        prime.append(i)

# devide prime number into 2 part
Sa = prime[0:len(prime)//2]
Sb = prime[len(prime)//2:]
move_value = 0
counter = 0
min_num = sum(Sa) - sum(Sb)  # initialize minimum value
objective = 0  # initialize objective

# calculate minimum value
while (True):
    # find the best combination
    if abs(sum(Sa) - sum(Sb)) > objective:
        if sum(Sa) > sum(Sb):
            move_value = min(Sa)
            Sa.remove(move_value)
            Sb.append(move_value)
        else:
            move_value = min(Sb)
            Sb.remove(move_value)
            Sa.append(move_value)

        # Decide whether to update the "objective"
        if abs(sum(Sa) - sum(Sb)) < min_num:
            min_num = abs(sum(Sa) - sum(Sb))  # update minimum value
        else:
            counter += 1  # increase counter
            if counter > len(prime):
                objective += 1  # update objective
                counter = 0  # reset couter
    else:
        break

# display result
print("Sa: {}".format(sorted(Sa)))
print("Sb: {}".format(sorted(Sb)))
print("|Sa - Sb| = {}".format(abs(sum(Sa) - sum(Sb))))
