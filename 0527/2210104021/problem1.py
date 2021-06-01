# -*- coding: utf-8 -*-
"""
Created on Tue Jun  1 16:34:42 2021

@author: kkawa
"""

import numpy as np

#素数判定
#素数ならTrue，そうでなければFalseを返す．
def IsPrimeNumber(x):
    for i in range(2, x // 2 + 1):
        if x % i == 0:
            return False
    return True


def main():
        
    #Sは[1, 100]での素数の集合
    S = list(filter(IsPrimeNumber, np.arange(2, 100)))
    
    #SA　と　SB　の和の差の絶対値の最大値はSA = []，SB = Sのとき，sum(S)
    best = sum(S)
    
    #bestcombはSAにSの要素を入れる("1")，入れない("0")を表す．
    #探索のループを2**(len(S)-1)にするため，SAはSの最初の要素を入れるものとする.
    bestcomb = "1" + bin(0)[2:].zfill(len(S)-1)
    
    for i in range(2 ** (len(S) - 1)):
        comb = bin(i)[2:].zfill(len(S)-1)
        #countはっ現在のSAの和を表す．count = sum(SA)
        count = S[0]
        for j in range(1, len(S) - 1):
            if comb[j] == "1":
                count += S[j]
                
        #現在のbestの更新
        #sum(SB) = sum(S) - sum(SA), if S = SA + SB
        if abs(count - (sum(S) - count)) < best:
            best = abs(count - (sum(S) - count))
            bestcomb = "1" + comb
            
        #最小値はSを2で割った余り(Sが偶数なら0,奇数なら1)
        #最小値をも発見出来たら，break
        if best == sum(S) % 2: 
            break
    
    #SA，SBの和の差の最小値の表示
    SA = []
    SB = []
    for i in range(len(S)):
        if bestcomb[i] == "1":
            SA.append(S[i])
        else: 
            SB.append(S[i])
    
    print("最小値 : " + str(best))
    print("SA : " + str(SA))
    print("SB : " + str(SB))
    
if __name__ == "__main__":
    main()