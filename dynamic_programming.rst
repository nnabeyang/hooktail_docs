====================
0-1ナップサック問題
====================

ナップサック問題は、動的計画法で解ける問題です。時間計算量の比較のために、深さ優先探索でも解いています。

問題の内容
============

入れられる品物の総量の最大値がWのナップサックと、n個の品物が与えられたとします。品物iの重さはw[i]、価値はv[i]としたとき、ナップサックに入れた品物の価値の総和が最大値は何でしょうか。


漸化式
=======

考え方としては、0から(n-1)番目の品物それぞれについて、ナップサックに入れた場合、入れない場合をそれぞれ試して、価値が最大になる値を返せば、正しい答えになるというものです。この考え方をコードにします。a(i, j)をi番目以降の品物を重さの総和j以下になるように選んだ、価値の総和の最大値とします。a(i, j)の言葉で問題で計算しようとしている量を書き直すと、a(0, W)になります。a(i,j)の値はi番目の品物を足すか、足さないかで品物の総和がjになるi+1番目以降の品物の選び方の最大値なので、a(i + 1, j)とa(i + 1, j - w[i])だけがa(i, j)に寄与しえます。品物を加えると、価値の総和はa(i + 1, j - w[i]) + v[i]になり、加えない場合はa(i + 1, j)に等しくなります。このどちらか大きい方がa(i, j)の値になります。

.. code-block:: javascript

        a(i, j) = Math.max(a(i + 1, j), a(i + 1, j - w[i]) + v[i]);

j < w[i]のときは加える可能性は無いのでa(i, j) == a(i + 1, j)で決まりです。
だから、次のように書き換えましょう。

.. code-block:: javascript

        a(i, j) | j < w[i]  = a(i + 1, j);
                | otherwise = Math.max(a(i + 1, j), a(i + 1, j - w[i]) + v[i]);

最後にi == nのときは、品物の種類は0番目からn-1番目までのnなので、結果に影響しないように0を返すことにします。

.. code-block:: javascript

        a(i, j) | i == n = 0
                | j < w[i] = a(i + 1, j);
                | otherwise = Math.max(a(i + 1, j), a(i + 1, j - w[i]) + v[i]);

これで漸化式が完成しました。

深さ優先探索
============

a(i, j)を関数だと思うと、再帰関数で次のように書けます。このような方法を深さ優先探索(Depth-First Search)と言うので、下のコードではa(i, j)を返す関数の名前を ``dfs(i, j)`` としています。

.. code-block:: javascript

        //    n:品物の種類
        // w[i]:品物iの重さ
        // v[i]:品物iの価値
        //    W:ナップサックに入れられる品物の重さの最大値(容量)
        function main(n, w, v, W) {
          console.log(dfs(0, W));// 答えを標準出力
          // dfs(i, j): i番目以降の品物を重さの総和がj以下になるように選んだ、
          //            価値の総和の最大値。
          function dfs(i, j) {
            // 品物の種類はn種しかないので
            // n番目は存在しない(n+1)種目なので
            // 結果に影響を与えないように0を返す。
            if (i == n)        return 0;
            //品物iを加えると重さがjを超えるので加えられない。
            //結果としてdfs(i, j) == dfs(i + 1, j)になる。
            else if (j < w[i]) return dfs(i + 1, j);
            //品物iを加えない場合と、加える場合の大きい方がdfs(i, j)になる。
            else               return Math.max(dfs(i + 1, j), 
                                               dfs(i + 1, j - w[i]) + v[i]);
          }
        }
        main(4, [2, 1, 3, 2], [3, 2, 4, 2], 5);

難無く書けましたが、品物1つずつについて入れる、入れないを選択しているので時間計算量のオーダーはO(2^n)と非常に遅いです。遅い原因は何度も同じ計算をしていることが挙げられます。これについては、console.logなどを使って確かめてみると実感がわくと思います。

動的計画法
==========

先ほどはa(i, j)を関数だと思ってみましたが、ここでは二次元配列だと思ってみます。
そして、ここで見る方法は動的計画法(dynamic programming)と呼ばれているので、a(i, j)の値を要素に持つ二次元配列をdpとします。

.. code-block:: javascript

        dp(i, j) | i == n = 0
                 | j < w[i] = dp(i + 1, j);
                 | otherwise = Math.max(dp(i + 1, j), dp(i + 1, j - w[i]) + v[i]);

サイズ(n)×(W+1)の2次元配列dpにdp[i][j] = a(i, j)と入れていったとすると、次のようになります。

.. code-block:: javascript

        dp[i][j] | i == n = 0
                 | j < w[i] = dp[i + 1][j];
                 | otherwise = Math.max(dp[i + 1][j], dp[i + 1][j - w[i]] + v[i]);

ここでdp[n][j] = 0で初期化すれば、次のように2重ループでdp[i][j] == a(i, j)なdpが作れます。

.. code-block:: javascript

        function main(n, w, v, W) {
          var np = n + 1;
          var Wp = W + 1;
          var dp = new Array(np)
          for(var i = 0; i < np; i++) dp[i] = new Array(Wp);
          //dp[n][j] = 0;
          for(var j = 0; j < Wp; j++) dp[n][j] = 0;
          solve();
          console.log(dp[0][W]);
          //dp[i][j] | j < w[i]  = dp[i+1][j] 
          //         | otherwise = Math.max(dp[i + 1][j], dp[i + 1][j - w[i]] + v[i])
          function solve() {
            for(var i = n - 1; i >= 0; i--) {
              for(var j = 0; j <= W; j++) {
                if (j < w[i]) dp[i][j] = dp[i + 1][j];
                else          dp[i][j] = Math.max(dp[i + 1][j], 
                                                  dp[i + 1][j - w[i]]  + v[i]);
              } 
            }
          }
        }
        main(4, [2, 1, 3, 2], [3, 2, 4, 2], 5);

2重ループ回すだけでdpができるので、時間計算量はO(nW)となります。深さ優先探索のときよりかなり高速化できたことになります。

@@author:nabeyang@@
@@category:プログラミング@@
