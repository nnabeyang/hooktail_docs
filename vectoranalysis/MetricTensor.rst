=================================================================
計量テンソル
=================================================================
ベクトル :math:`\bm{A}=A^{k}\bm{e_{k}}=A_{k}\bm{e^{k}}` の両辺に、 :math:`\bm{e_{i}}` と :math:`\bm{e^{i}}` を乗じることで次式を得ます。

.. math::
   \bm{e_{i}}\cdot \bm{A}= A^{k}(\bm{e_{i}} \cdot \bm{e_{k}})      \tag{1}


.. math::
   \bm{e^{i}}\cdot \bm{A} = A_{k}(\bm{e^{i}} \cdot \bm{e^{k}})     \tag{2}

ここまでは単に両辺に内積を取ってみただけで、だからどうってことはありません。今後のために、基底同士の内積は次のような記号で表わすことにしておきましょう。

.. math::
   \bm{e_{i}} \cdot \bm{e_{k}} = g_{ik}

.. math::
   \bm{e^{i}} \cdot \bm{e^{k}} = g^{ik}

また、補足ですが、双対基底の内積はクロネッカーのデルタになりますから、 :math:`\bm{e_{i}} \cdot \bm{e^{k}} = g_{i}^{k}` は :math:`{\delta}_{i}^{k}` と書いた方が意味は明快ですが、統一性の観点から :math:`g` を使うこともあります。ご了承ください。



さて、式 :math:`(1)` の左辺の :math:`\bm{A}` には :math:`\bm{A}=A_{i}\bm{e^{i}}` を、式 :math:`(2)` の左辺の :math:`\bm{A}` には :math:`\bm{A}=A^{i}\bm{e_{i}}` を代入し、 :math:`\bm{e_{k}} \cdot \bm{e^{i}} = {\delta}_{k}^{i}` に気をつけると、 :math:`g` を使って次式を得ます。


.. math::
   A_{i} = g_{ik} A^{k}    \tag{3}

.. math::
   A^{i} = g^{ik} A_{k}    \tag{4}

これはベクトルの共変成分と反変成分の、変換の式になっています。（ ベクトル成分の座標変換_ を参照して下さい。）添字の :math:`i,k` はそれぞれ :math:`1,2,3` を表わしますから、変換の係数は :math:`3 \times 3` で、 :math:`9` 種類あることが分かります。(ただし、内積は順序によりませんので、 :math:`g_{ik}` と :math:`g_{ki}` など、添字の順序が逆のものは同じ値になります。本質的に異なるのは :math:`6` 種類です。)　見やすいように、変換係数を次のように行列で表わしておきましょう。添字は :math:`i,j` としておきます。



.. math::
   g_{ij}=
   \left( \begin{array}{ccc}
   g_{11} & g_{12} & g_{13} \\
   g_{21} & g_{22} & g_{23} \\
   g_{31} & g_{32} & g_{33} \\
   \end{array}
   \right)

.. math::
   g^{ij}=
   \left( \begin{array}{ccc}
   g^{11} & g^{12} & g^{13} \\
   g^{21} & g^{22} & g^{23} \\
   g^{31} & g^{32} & g^{33} \\
   \end{array}
   \right)

.. math::
   g_{i}^{j}=
   \left( \begin{array}{ccc}
   g_{1}^{1} & g_{1}^{2} & g_{1}^{3} \\
   g_{2}^{1} & g_{2}^{2} & g_{2}^{3} \\
   g_{3}^{1} & g_{3}^{2} & g_{3}^{3} \\
   \end{array}
   \right)= 
   \left( \begin{array}{ccc}
   1 & 0 & 0 \\
   0 & 1 & 0 \\
   0 & 0 & 1 \\
   \end{array}
   \right)

変換係数の意味
-----------------------------------------------------------------
共変成分と反変成分の相互の変換を橋渡しする変換係数として、 :math:`g_{ij}` や :math:`g^{ij}` が出てきましたが、これらには図形的にきっちりとした意味があります。このセクションでは、それを見ていきます。

いま、ベクトル :math:`\bm{r}` の長さが微小に変化したとします。その微小変化を、微小ベクトル :math:`d\bm{r}=dx_{i}\bm{e^{i}}=dx^{i}\bm{e_{i}}` で表わしましょう。 :math:`dx_{i}` や :math:`dx^{i}` は、各座標系におけるこの微小ベクトルの成分です。ベクトルの長さが少し変わったといっても、観測する座標系によって見え方は違うのですから、 :math:`dx_{i}` や :math:`dx^{i}` も当然 :math:`\bm{e^{i}}` や :math:`\bm{e_{i}}` の取り方に依存する量になります。

微小ベクトルの長さ :math:`ds` は次式のように内積で定義されます。( 内積空間_ 参照。)

.. math::
   ds^2 &=d\bm{r}\cdot d\bm{r} \\ 
        &= dx^{i} \bm{e_{i}} \cdot dx^{j} \bm{e_{j}} = g_{ij} dx^{i} dx^{j} \\ 
        &= dx_{i} \bm{e^{i}} \cdot dx_{j} \bm{e^{j}} = g^{ij} dx_{i} dx_{j} \\ 
        &= dx^{i} \bm{e_{i}} \cdot dx_{j} \bm{e^{j}} = g_{i}^{j} dx^{i} dx_{j}= dx^{i}dx_{i}    \tag{5}

この表式の二行目、三行目、四行目はそれぞれ :math:`ds^2` を意味していますが、座標系の取り方が違っています。当然、ベクトル :math:`\bm{r}` の微小な変化 :math:`d\bm{r}` に対し、異なる座標系では異なる変化分が観測されます。例えば、 :math:`\bm{e_{i}}-\bm{e_{j}}` 座標系では、 :math:`dx^{i},dx^{j}` の変化があったように見えるし、 :math:`\bm{e^{i}}-\bm{e^{j}}` 座標系では、 :math:`dx_{i},dx_{j}` の変化があったように見えるわけです。式 :math:`(5)` の右辺が意味しているのは、これらの座標系で、各座標軸に沿った変化分の単純な積、 :math:`dx^{i} dx^{j}` や :math:`dx_{i} dx_{j}` と、本当の変化分の二乗 :math:`ds^2` の *比* が :math:`g_{ij}` や :math:`g^{ij}` だということです。


このように、 :math:`g_{ij}` や :math:`g^{ij}` は図形の計量に関係する係数でしたので、 *計量テンソル* と呼びます。面白いですね。もう一度、式 :math:`(5)` をじっくり眺めてみて下さい。


.. [*] テンソルの概念はまだ勉強していませんが、計量テンソルは二階のテンソルという量になります。また、直交座標系の場合、計量テンソルの成分の平方根を計量因子と呼びます。テンソルを勉強したあとに、この辺りをもう一度復習してみてください。計量因子は次の 直交座標系_ で定義します。 ベクトル演算子の座標変換_ の記事では、定義はもっと天下り的ですが、計量因子の応用を紹介しています。時間があれば参考にしてみて下さい。


.. [*] 計量テンソルの意味は具体例を考えるともっと分かりやすいと思います。例えば、二次元デカルト座標 :math:`(x,y)` から極座標 :math:`(r,\theta )` に座標変換すると、微小面積は :math:`dxdy=rdrd\theta` の関係で結ばれます。これは解析学で習ったと思いますが、 右辺に出てきた :math:`r` はヤコビアンです。この :math:`r` がこの場合の計量テンソルの成分 :math:`g` になります。左辺の :math:`dxdy` は長さの二乗の次元ですが、右辺の :math:`\theta` は角度ですので無次元で、計量テンソルの成分 :math:`r` と :math:`dr` が長さの次元を持っているので辻褄が合うようになっています。このように一般に計量テンソルの成分には長さの次元が入ることがあります。さらに詳しくは 計量テンソルとヤコビアン_ を参照して下さい。



さらにもう一歩
--------------------------------------------------------------
計量テンソルとして、基底ベクトルに応じて :math:`g_{ij}` と :math:`g^{ij}` という、添字が上につくものと添字が下につくものが出てきました。このセクションでは、計量テンソルの成分が互いにどのような関係で結ばれているのかを考えてみます。

ベクトル成分の変換式を、行列の形でもう一度考えて見ましょう。（ ベクトル成分の座標変換_ 参照。）

.. math::
  \left(
  \begin{array}{ccc}
  A^{1}\\
  A^{2}\\
  A^{3}\\
  \end{array}
  \right)
  =
  \left( \begin{array}{ccc}
  g^{11} & g^{12} & g^{13} \\
  g^{21} & g^{22} & g^{23} \\
  g^{31} & g^{32} & g^{33} \\
  \end{array}
  \right) 
  \left(
  \begin{array}{ccc}
  A_{1}\\
  A_{2}\\
  A_{3}\\
  \end{array}
  \right)

線形代数の知識を少し使うと、 :math:`A^{i}` を次のように表わせることが分かります。

.. math::
   A^{i} = \frac{G^{ik}A_{k}}{G}   \tag{6}

ただし、式中 :math:`G` は行列 :math:`g^{ij}` の行列式、 :math:`G^{ik}` は行列 :math:`g^{ij}` の :math:`ik` 成分の余因子を意味するものとしています。(行列式や余因子について、ここでは詳しく説明できませんので、よく分からない人は自分で線形代数の教科書などを参考にして下さい　m(_ _)m。例を書いておきます↓)


.. math::
   G={\rm det}|g^{ij}|= 
   \left| \begin{array}{ccc}
   g^{11} & g^{12} & g^{13} \\
   g^{21} & g^{22} & g^{23} \\
   g^{31} & g^{32} & g^{33} \\
   \end{array}
   \right|  

.. math::
   G^{11}= \left| \begin{array}{cc}
   g^{22} & g^{23} \\
   g^{32} & g^{33} \\
   \end{array}
   \right|  , \text{    }  
   G^{12}=- \left| \begin{array}{cc}
   g^{21} & g^{23} \\
   g^{31} & g^{33} \\
   \end{array}
   \right| , \text{    etc.}

一方、先ほど式 :math:`(4)` で :math:`A^{i} = g^{ik} A_{k}` という関係がありましたから、式 :math:`(6)` と比較して次式を得ます。


.. math::
   g^{ik} = \frac{G^{ik}}{G}       \tag{7}

まったく同様にして、共変ベクトルの計量テンソルの成分も次のように表わせることが分かります。

.. math::
   g_{ik} = \frac{G_{ik}}{G'}      \tag{8}

ただし、 :math:`G'=det|g_{ij}|= \left| \begin{array}{ccc} g_{11} & g_{12} & g_{13} \\ g_{21} & g_{22} & g_{23} \\ g_{31} & g_{32} & g_{33} \\ \end{array} \right|` としました。  


ところで、 双対基底_ の記事で得た :math:`\bm{e^{1}}=\frac{ (\bm{e_{2}}\times \bm{e_{3}}) }{\bm{e_{1}} \cdot (\bm{e_{2} \times \bm{e_{3}}})}` 等の公式を使えば、計量テンソルの成分を次のように表現することもできます。式中、 :math:`\bm{e_{1}} \cdot (\bm{e_{2} \times \bm{e_{3}}})` 等を :math:`V` と置いていますが、これは :math:`\bm{e_{1}},\bm{e_{2}},\bm{e_{3}}` によって張られる平行六面体の体積になります。( 三重積_ を参照してください。)また、 :math:`i,p,q` と :math:`j,r,s` はそれぞれ巡回的な添字だとします。

.. math::
   g^{ij}&=\bm{e^{i}} \cdot \bm{e^{j}} \\
   &=\frac{ (\bm{e_{p}}\times \bm{e_{q}}) }{\bm{e_{i}} \cdot (\bm{e_{p} \times \bm{e_{q}}})} \cdot 
   \frac{ (\bm{e_{r}}\times \bm{e_{s}}) }{\bm{e_{j}} \cdot (\bm{e_{r} \times \bm{e_{s}}})} \\ 
   & = \frac{1}{V^{2}}(\bm{e_{p}}\times \bm{e_{q}}) \cdot (\bm{e_{r}}\times \bm{e_{s}}) \\ 
   & = \frac{1}{V^{2}}((\bm{e_{p}}\times \bm{e_{q}}) \times \bm{e_{r}} )\cdot \bm{e_{s}} \\ 
   & = \frac{1}{V^{2}}[\bm{e_{q}}(\bm{e_{p}}\cdot \bm{e_{r}}) -  \bm{e_{p}}(\bm{e_{q}}\cdot \bm{e_{r}})]\cdot \bm{e_{s}} \\ 
   & = \frac{1}{V^{2}}[(\bm{e_{p}} \cdot \bm{e_{r}})(\bm{e_{q}} \cdot \bm{e_{s}}) -  (\bm{e_{p}} \cdot \bm{e_{s}})(\bm{e_{q}} \cdot \bm{e_{r}}) ] \\ 
   & = \frac{1}{V^{2}}
   \left| \begin{array}{cc}
   \bm{e_{p}} \cdot \bm{e_{r}} & \bm{e_{p}} \cdot \bm{e_{s}} \\
   \bm{e_{q}} \cdot \bm{e_{r}} & \bm{e_{q}} \cdot \bm{e_{s}} \\
   \end{array}
   \right|  \\ 
   & = \frac{1}{V^{2}}
   \left| \begin{array}{cc}
   g_{pr} & g_{ps} \\
   g_{qr} & g_{qs} \\
   \end{array}
   \right|         \tag{9}

色々、細かいテクニックを使って式変形をしましたが、最後はなんだか不思議に簡単な表式に至りました。さきほど、式 :math:`(7)` として :math:`g^{ik} = \frac{G^{ik}}{G}` という式を得ていましたが、これを式 :math:`(9)` と比較することで次式を得ます。

.. math::
   G = V^{2}       \tag{10}

平方根を展開すると :math:`V= \pm \sqrt{G}` となりますが、この符号は :math:`\bm{e_{1}},\bm{e_{2}},\bm{e_{3}}` が右手系ならば正、左手系ならば負になるように決められます。( 三重積_ を参照してください。)  :math:`G` の図形的意味は、これで少し分かりました。 *det|G|は基底の張る平行六面体の体積の二乗になっています* 。

同様にして、共変ベクトルの計量テンソルの成分に対しても次式が導けます。

.. math::
   G' = V'^{2}

計量テンソルの表現行列には、意外と分かりやすい図形的意味があるようです。また、次の関係に注意してみましょう。

.. math::
        1&=\bm{e_{1}}\cdot \bm{e^{1}} \\
        &=\frac{\bm{e^{2}} \times \bm{e^{3}}}{V'}\frac{\bm{e_{2}} \times \bm{e_{3}}}{V} \\
        &= \frac{1}{VV'} (\bm{e^{2}} \times \bm{e^{3}})\cdot (\bm{e_{2}} \times \bm{e_{3}}) \\ 
        &= \frac{1}{VV'} [(\bm{e^{2}} \cdot \bm{e_{2}})(\bm{e^{3}} \cdot\bm{e_{3}} )-(\bm{e^{3}} \cdot \bm{e_{2}})(\bm{e^{2}}\cdot \bm{e_{3}})] \\ 
        &= \frac{1}{VV'}

これより、 :math:`VV'=1` の関係は座標系に関わらず常になりたつことが分かりました。式 :math:`(9)` より :math:`GG'=1` も言えます。またしても、双対基底に関する美しい関係式が得られました！


.. _ベクトル成分の座標変換: http://www12.plala.or.jp/ksp/vectoranalysis/VectorCompoTrans/
.. _ベクトル演算子の座標変換: http://www12.plala.or.jp/ksp/vectoranalysis/
.. _三重積: http://www12.plala.or.jp/ksp/vectoranalysis/Triprod/
.. _直交座標系: http://www12.plala.or.jp/ksp/vectoranalysis/OrthogonalCoords/
.. _双対基底: http://www12.plala.or.jp/ksp/vectoranalysis/DualBases/
.. _内積空間: http://www12.plala.or.jp/ksp/vectoranalysis/InnerdotSpace/
.. _計量テンソルとヤコビアン: http://www12.plala.or.jp/ksp/vectoranalysis/

