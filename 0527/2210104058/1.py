#Ryuhei Nishida
#2210104058

import itertools
#素数を返す関数
def primes(num):
    a=[]
    for i in range(2,num):
        flag =0 
        for j in range(2,i//2+1):
            if(i%j==0):
                flag=1
                break
        if flag == 0:
            a.append(i)
    return a

def main():
    #100までの素数
    p=primes(100)
    #その和
    p_sum = sum(p)

    #差の最小値の初期値
    min = p_sum

    #2〜k個組み合わせ繰り返し
    for k in range(2,len(p)//2+1):

        #pからk個選択
        for v in itertools.combinations(p, k):
            #選択したもの以外の和
            not_v=p_sum-sum(v)
            #最小値判定
            if(abs(not_v-sum(v))<min):
                min = abs(not_v-sum(v))
                S_a=set(v)
                S_b=set(p)^set(v)

    print("answer="+str(min))
    print("S_a="+str(S_a))
    print("S_b="+str(S_b))

if __name__ == '__main__':
    main()
        

