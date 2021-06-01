#2210104040
#高橋敬
from itertools import combinations

#2~numまでの素数のリストを返す関数
def GET_PRIME(num):
    prime_list = []
    for i in range(2, num):
        flag = 0
        for j in range(2, i//2+1):
            if i % j == 0:
                flag = 1
                break
        if flag == 0:
            prime_list.append(i)
    return prime_list


def main():
    #1~100までの素数を格納
    S = []
    #1~100までの素数を取得
    S = GET_PRIME(100)
    #リストSの合計値を格納
    sum_S = sum(S)
    #答えの初期化：初期値をリストSの合計とする
    ans = sum_S
    #リストSから選択してくる個数を設定
    for i in range(1, len(S)//2+1):
        #リストSからi個選択->リストS_subに格納
        for S_sub in combinations(S, i):
            #リストS_subの合計
            sum_Sa = sum(S_sub)
            #sum_Saの2倍とSの和との差の絶対値が現在のansよりも小さい->ans,S_A,S_Bを更新する
            if ans > abs(sum_S-2*sum_Sa):
                ans = abs(sum_S-2*sum_Sa)
                S_A = list(S_sub)
                S_B = list(set(S) ^ set(S_sub))
    print("the answer => " + str(ans))
    print("S_A => " + str(S_A))
    print("S_B => " + str(S_B))


if __name__ == '__main__':
    main()
