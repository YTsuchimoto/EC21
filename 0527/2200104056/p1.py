#Johan Berdougo 2200104056

#Array of the 100 first prime numbers from the slide
s=[]
for i in range(2,100):
    flag = 0
    for j in range(2,i//2+1):
        if (i%j==0):
            flag=1
            break
    if flag == 0:
        s.append(i)
print("S : ",s)
print("")


#Compute the sum of the elements of an array
def sum(tab):
    tmp = 0
    for x in tab:
        tmp += x
    return tmp


#Iterating from the largest prime number to the smallest and adding them in the sub array with the smallest sum
s1=[]
s2=[]
for i in range(len(s)-1, 0, -1):
    if(sum(s1) < sum(s2)):
        s1.append(s[i])
    else:
        s2.append(s[i])

print("Sa : ",s1)
print("sum : ",sum(s1))
print("")
print("Sb : ",s2)
print("sum : ",sum(s2))
print("")
print("absolute value of difference : ",abs(sum(s1) - sum(s2)))
