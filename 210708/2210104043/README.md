# 進化型計算特論  第 13 回課題
## 2210104043 高山 裕成

### New Operator
突然変異ルールとして, ランダムにインデックス i を指定し,
i + 3, i + 3 + 3, i + 3 + 3 + 4 番目の遺伝子座を 0 か 1 に変える. 遺伝子長を超える場合は遺伝子長で割った余りを出す.

### Problem
One-Max問題を解く.

### How to execute
```
python report13-2210104043.py
```
### Example of result
```
[[1, 1, 0, 0, 0, 0, 1, 1, 0, 0], [0, 0, 0, 1, 1, 0, 0, 1, 0, 0], [1, 0, 0, 0, 0, 0, 1, 0, 1, 0], [0, 0, 1, 0, 0, 1, 0, 1, 0, 0], [0, 1, 0, 0, 1, 0, 1, 0, 1, 0], [1, 1, 0, 0, 1, 1, 0, 0, 1, 1], [1, 1, 1, 0, 1, 0, 0, 1, 0, 0], [1, 0, 1, 0, 0, 1, 1, 1, 1, 1], [0, 0, 1, 1, 1, 0, 1, 0, 0, 0], [1, 1, 1, 0, 1, 0, 0, 0, 0, 1]]
Generation : 1/100
Min: 2.0
Max: 7.0
Generation : 2/100
Min: 4.0
Max: 7.0
Generation : 3/100
Min: 6.0
Max: 7.0
Generation : 4/100
Min: 4.0
Max: 8.0
Generation : 5/100
Min: 7.0
Max: 7.0
Generation : 6/100
Min: 5.0
Max: 7.0
Generation : 7/100
Min: 7.0
Max: 7.0
Generation : 8/100
Min: 7.0
Max: 7.0
Generation : 9/100
Min: 7.0
Max: 8.0
Generation : 10/100
Min: 7.0
Max: 8.0
Generation : 11/100
Min: 6.0
Max: 8.0
Generation : 12/100
Min: 7.0
Max: 8.0
Generation : 13/100
Min: 7.0
Max: 8.0
Generation : 14/100
Min: 8.0
Max: 8.0
Generation : 15/100
Min: 5.0
Max: 8.0
Generation : 16/100
Min: 6.0
Max: 9.0
Generation : 17/100
Min: 8.0
Max: 9.0
Generation : 18/100
Min: 7.0
Max: 9.0
Generation : 19/100
Min: 6.0
Max: 9.0
Generation : 20/100
Min: 7.0
Max: 9.0
Generation : 21/100
Min: 9.0
Max: 9.0
Generation : 22/100
Min: 8.0
Max: 9.0
Generation : 23/100
Min: 9.0
Max: 9.0
Generation : 24/100
Min: 8.0
Max: 9.0
Generation : 25/100
Min: 8.0
Max: 9.0
Generation : 26/100
Min: 9.0
Max: 9.0
Generation : 27/100
Min: 8.0
Max: 9.0
Generation : 28/100
Min: 8.0
Max: 9.0
Generation : 29/100
Min: 8.0
Max: 9.0
Generation : 30/100
Min: 7.0
Max: 9.0
Generation : 31/100
Min: 6.0
Max: 9.0
Generation : 32/100
Min: 8.0
Max: 9.0
Generation : 33/100
Min: 9.0
Max: 9.0
Generation : 34/100
Min: 7.0
Max: 9.0
Generation : 35/100
Min: 6.0
Max: 9.0
Generation : 36/100
Min: 7.0
Max: 9.0
Generation : 37/100
Min: 8.0
Max: 10.0
Generation : 38/100
Min: 8.0
Max: 10.0
Generation : 39/100
Min: 7.0
Max: 10.0
Generation : 40/100
Min: 9.0
Max: 10.0
Generation : 41/100
Min: 9.0
Max: 10.0
Generation : 42/100
Min: 8.0
Max: 10.0
Generation : 43/100
Min: 10.0
Max: 10.0
Generation : 44/100
Min: 10.0
Max: 10.0
Generation : 45/100
Min: 8.0
Max: 10.0
Generation : 46/100
Min: 10.0
Max: 10.0
Generation : 47/100
Min: 7.0
Max: 10.0
Generation : 48/100
Min: 10.0
Max: 10.0
Generation : 49/100
Min: 7.0
Max: 10.0
Generation : 50/100
Min: 10.0
Max: 10.0
Generation : 51/100
Min: 8.0
Max: 10.0
Generation : 52/100
Min: 8.0
Max: 10.0
Generation : 53/100
Min: 10.0
Max: 10.0
Generation : 54/100
Min: 9.0
Max: 10.0
Generation : 55/100
Min: 9.0
Max: 10.0
Generation : 56/100
Min: 7.0
Max: 10.0
Generation : 57/100
Min: 10.0
Max: 10.0
Generation : 58/100
Min: 9.0
Max: 10.0
Generation : 59/100
Min: 9.0
Max: 10.0
Generation : 60/100
Min: 10.0
Max: 10.0
Generation : 61/100
Min: 9.0
Max: 10.0
Generation : 62/100
Min: 10.0
Max: 10.0
Generation : 63/100
Min: 10.0
Max: 10.0
Generation : 64/100
Min: 7.0
Max: 10.0
Generation : 65/100
Min: 7.0
Max: 10.0
Generation : 66/100
Min: 8.0
Max: 10.0
Generation : 67/100
Min: 9.0
Max: 10.0
Generation : 68/100
Min: 10.0
Max: 10.0
Generation : 69/100
Min: 9.0
Max: 10.0
Generation : 70/100
Min: 9.0
Max: 10.0
Generation : 71/100
Min: 7.0
Max: 10.0
Generation : 72/100
Min: 10.0
Max: 10.0
Generation : 73/100
Min: 9.0
Max: 10.0
Generation : 74/100
Min: 8.0
Max: 10.0
Generation : 75/100
Min: 10.0
Max: 10.0
Generation : 76/100
Min: 10.0
Max: 10.0
Generation : 77/100
Min: 8.0
Max: 10.0
Generation : 78/100
Min: 7.0
Max: 10.0
Generation : 79/100
Min: 10.0
Max: 10.0
Generation : 80/100
Min: 9.0
Max: 10.0
Generation : 81/100
Min: 8.0
Max: 10.0
Generation : 82/100
Min: 8.0
Max: 10.0
Generation : 83/100
Min: 8.0
Max: 10.0
Generation : 84/100
Min: 10.0
Max: 10.0
Generation : 85/100
Min: 8.0
Max: 10.0
Generation : 86/100
Min: 10.0
Max: 10.0
Generation : 87/100
Min: 10.0
Max: 10.0
Generation : 88/100
Min: 7.0
Max: 10.0
Generation : 89/100
Min: 9.0
Max: 10.0
Generation : 90/100
Min: 8.0
Max: 10.0
Generation : 91/100
Min: 10.0
Max: 10.0
Generation : 92/100
Min: 10.0
Max: 10.0
Generation : 93/100
Min: 7.0
Max: 10.0
Generation : 94/100
Min: 8.0
Max: 10.0
Generation : 95/100
Min: 8.0
Max: 10.0
Generation : 96/100
Min: 10.0
Max: 10.0
Generation : 97/100
Min: 10.0
Max: 10.0
Generation : 98/100
Min: 10.0
Max: 10.0
Generation : 99/100
Min: 10.0
Max: 10.0
Generation : 100/100
Min: 8.0
Max: 10.0
----------
Best individual : [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], Best score : 10.0
```
