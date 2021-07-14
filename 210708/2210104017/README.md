2210104017 片山唯佳

追加部分以外のコードは授業支援システムにあるdeapのページのExampleの中からKnapsack Problem: Inheriting from Set(サイトURL:<https://deap.readthedocs.io/en/master/examples/ga_knapsack.html>,ソースコードURL:<https://github.com/DEAP/deap/blob/f4b77759897d0322ab5a6551106b28f6f4401a4e/examples/ga/knapsack.py>)を使用した。
追加部分は関数cxSetの79-88行目である。これは交叉の後に価値が重量の3倍以下の品物は価値が低いとみなして削除し、ランダムに選んだ品物と入れ替えるという操作を行う。
