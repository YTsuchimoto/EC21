2210104051　坪田一希

## 用いた問題
DEAPの公式ドキュメントにあるOnemax問題を用いた．[リンク](https://deap.readthedocs.io/en/master/examples/ga_onemax.html)

## 新しい演算子
親となる２個体に対し強制的に突然変異を起こし，その後一点交叉を行う演算子を作成した．mutate_cross関数として定義した．main関数内では，通常の交差を行うところで，MCPB(新しい演算子を用いる確率)を用いて，通常の交叉と新演算子のどちらかを行う実装とした．今回は確率は0.5とした．

## 結果
最終世代の評価のみ示す．

通常結果（新演算子なし）

```
-- Generation 27 --
  Evaluated 186 individuals
  Min 83.0
  Max 100.0
  Avg 94.81
  Std 2.6344955241309864
-- End of (successful) evolution --
Best individual is [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], (100.0,)
```

新演算子実装結果

```
-- Generation 46 --
  Evaluated 190 individuals
  Min 80.0
  Max 100.0
  Avg 95.48666666666666
  Std 3.640946152978408
-- End of (successful) evolution --
Best individual is [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], (100.0,)```
