# -*- coding: utf-8 -*-

# 素数リストの作成
def get_prime(max_num):
    prime_list = []
    for i in range(2,max_num):
        flag = 0
        for j in range(2,i//2+1):
            if i % j == 0:
                flag = 1
                break
        if flag == 0:
            prime_list.append(i)
    return prime_list

# DP
def find_max_dp(num_list,limit):
    list_len = len(num_list)

    # DPテーブル
    dp_table = [[0 for i in range(limit + 1)] for i in range(list_len + 1)]

    # DPループ
    for i in range(list_len):
        for j in range(limit + 1):
            if num_list[i] <= j:
                dp_table[i+1][j] = max(dp_table[i][j - num_list[i]] + num_list[i],dp_table[i][j])
            else:
                dp_table[i+1][j] = dp_table[i][j]

    # DP表から解の復元
    ans = []
    tmp_limit = limit
    for i in reversed(range(list_len)):
        if dp_table[i+1][tmp_limit] == dp_table[i][tmp_limit - num_list[i]] + num_list[i]:
            ans.append(num_list[i])
            tmp_limit = tmp_limit - num_list[i]

    return ans


if __name__ == '__main__':
    # 100までの素数の取得
    s = get_prime(100)

    # 配列を2分割した合計値の差分の最小化，つまり全体の合計値の半分以下になる最大の組み合わせを求める
    Sa = find_max_dp(s,sum(s)//2)

    # Saの要素以外
    Sb = list(set(s) ^ set(Sa))

    # 答え
    print(Sa)
    print(sum(Sa))
    print(Sb)
    print(sum(Sb))
