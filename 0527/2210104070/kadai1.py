from itertools import product

def get_prime():
    S=[]
    for i in range(2,100):
        flag = 0
        for j in range(2,i//2+1):
            if(i%j==0):
                flag=1
                break
        if flag == 0:
            S.append(i)
    return S
            
def calc():
    prime_list = get_prime()
    num_prime = len(prime_list)
    diff_min=sum(prime_list)
    set_min=[]
    for i in range(2 ** (num_prime - 1)):
        set_a=[]
        set_b=[]
        for j in range(num_prime):
            if (i >> j) & 1:
                set_a.append(prime_list[j])
            else:
                set_b.append(prime_list[j])
        diff_buff = abs(sum(set_a)-sum(set_b))
        if diff_buff<diff_min:
            diff_min = diff_buff
            set_min = [(set_a,set_b)]
        elif diff_buff==diff_min:
            set_min.append((set_a,set_b))
    return diff_min,set_min
            
def main():
    ans_value,ans_set=calc()
    for s in ans_set:
        print(ans_value,s)  

if __name__ == '__main__':
    main()