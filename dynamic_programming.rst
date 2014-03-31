====================
0-1�i�b�v�T�b�N���
====================

�i�b�v�T�b�N���́A���I�v��@�ŉ�������ł��B���Ԍv�Z�ʂ̔�r�̂��߂ɁA�[���D��T���ł������Ă��܂��B

���̓��e
============

�������i���̑��ʂ̍ő�l��W�̃i�b�v�T�b�N�ƁAn�̕i�����^����ꂽ�Ƃ��܂��B�i��i�̏d����w[i]�A���l��v[i]�Ƃ����Ƃ��A�i�b�v�T�b�N�ɓ��ꂽ�i���̉��l�̑��a���ő�l�͉��ł��傤���B


�Q����
=======

�l�����Ƃ��ẮA0����(n-1)�Ԗڂ̕i�����ꂼ��ɂ��āA�i�b�v�T�b�N�ɓ��ꂽ�ꍇ�A����Ȃ��ꍇ�����ꂼ�ꎎ���āA���l���ő�ɂȂ�l��Ԃ��΁A�����������ɂȂ�Ƃ������̂ł��B���̍l�������R�[�h�ɂ��܂��Ba(i, j)��i�Ԗڈȍ~�̕i�����d���̑��aj�ȉ��ɂȂ�悤�ɑI�񂾁A���l�̑��a�̍ő�l�Ƃ��܂��Ba(i, j)�̌��t�Ŗ��Ōv�Z���悤�Ƃ��Ă���ʂ����������ƁAa(0, W)�ɂȂ�܂��Ba(i,j)�̒l��i�Ԗڂ̕i���𑫂����A�����Ȃ����ŕi���̑��a��j�ɂȂ�i+1�Ԗڈȍ~�̕i���̑I�ѕ��̍ő�l�Ȃ̂ŁAa(i + 1, j)��a(i + 1, j - w[i])������a(i, j)�Ɋ�^�����܂��B�i����������ƁA���l�̑��a��a(i + 1, j - w[i]) + v[i]�ɂȂ�A�����Ȃ��ꍇ��a(i + 1, j)�ɓ������Ȃ�܂��B���̂ǂ��炩�傫������a(i, j)�̒l�ɂȂ�܂��B

.. code-block:: javascript

        a(i, j) = Math.max(a(i + 1, j), a(i + 1, j - w[i]) + v[i]);

j < w[i]�̂Ƃ��͉�����\���͖����̂�a(i, j) == a(i + 1, j)�Ō��܂�ł��B
������A���̂悤�ɏ��������܂��傤�B

.. code-block:: javascript

        a(i, j) | j < w[i]  = a(i + 1, j);
                | otherwise = Math.max(a(i + 1, j), a(i + 1, j - w[i]) + v[i]);

�Ō��i == n�̂Ƃ��́A�i���̎�ނ�0�Ԗڂ���n-1�Ԗڂ܂ł�n�Ȃ̂ŁA���ʂɉe�����Ȃ��悤��0��Ԃ����Ƃɂ��܂��B

.. code-block:: javascript

        a(i, j) | i == n = 0
                | j < w[i] = a(i + 1, j);
                | otherwise = Math.max(a(i + 1, j), a(i + 1, j - w[i]) + v[i]);

����őQ�������������܂����B

�[���D��T��
============

a(i, j)���֐����Ǝv���ƁA�ċA�֐��Ŏ��̂悤�ɏ����܂��B���̂悤�ȕ��@��[���D��T��(Depth-First Search)�ƌ����̂ŁA���̃R�[�h�ł�a(i, j)��Ԃ��֐��̖��O�� ``dfs(i, j)`` �Ƃ��Ă��܂��B

.. code-block:: javascript

        //    n:�i���̎��
        // w[i]:�i��i�̏d��
        // v[i]:�i��i�̉��l
        //    W:�i�b�v�T�b�N�ɓ������i���̏d���̍ő�l(�e��)
        function main(n, w, v, W) {
          console.log(dfs(0, W));// ������W���o��
          // dfs(i, j): i�Ԗڈȍ~�̕i�����d���̑��a��j�ȉ��ɂȂ�悤�ɑI�񂾁A
          //            ���l�̑��a�̍ő�l�B
          function dfs(i, j) {
            // �i���̎�ނ�n�킵���Ȃ��̂�
            // n�Ԗڂ͑��݂��Ȃ�(n+1)��ڂȂ̂�
            // ���ʂɉe����^���Ȃ��悤��0��Ԃ��B
            if (i == n)        return 0;
            //�i��i��������Əd����j�𒴂���̂ŉ������Ȃ��B
            //���ʂƂ���dfs(i, j) == dfs(i + 1, j)�ɂȂ�B
            else if (j < w[i]) return dfs(i + 1, j);
            //�i��i�������Ȃ��ꍇ�ƁA������ꍇ�̑傫������dfs(i, j)�ɂȂ�B
            else               return Math.max(dfs(i + 1, j), 
                                               dfs(i + 1, j - w[i]) + v[i]);
          }
        }
        main(4, [2, 1, 3, 2], [3, 2, 4, 2], 5);

��������܂������A�i��1���ɂ��ē����A����Ȃ���I�����Ă���̂Ŏ��Ԍv�Z�ʂ̃I�[�_�[��O(2^n)�Ɣ��ɒx���ł��B�x�������͉��x�������v�Z�����Ă��邱�Ƃ��������܂��B����ɂ��ẮAconsole.log�Ȃǂ��g���Ċm���߂Ă݂�Ǝ������킭�Ǝv���܂��B

���I�v��@
==========

��قǂ�a(i, j)���֐����Ǝv���Ă݂܂������A�����ł͓񎟌��z�񂾂Ǝv���Ă݂܂��B
�����āA�����Ō�����@�͓��I�v��@(dynamic programming)�ƌĂ΂�Ă���̂ŁAa(i, j)�̒l��v�f�Ɏ��񎟌��z���dp�Ƃ��܂��B

.. code-block:: javascript

        dp(i, j) | i == n = 0
                 | j < w[i] = dp(i + 1, j);
                 | otherwise = Math.max(dp(i + 1, j), dp(i + 1, j - w[i]) + v[i]);

�T�C�Y(n)�~(W+1)��2�����z��dp��dp[i][j] = a(i, j)�Ɠ���Ă������Ƃ���ƁA���̂悤�ɂȂ�܂��B

.. code-block:: javascript

        dp[i][j] | i == n = 0
                 | j < w[i] = dp[i + 1][j];
                 | otherwise = Math.max(dp[i + 1][j], dp[i + 1][j - w[i]] + v[i]);

������dp[n][j] = 0�ŏ���������΁A���̂悤��2�d���[�v��dp[i][j] == a(i, j)��dp�����܂��B

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

2�d���[�v�񂷂�����dp���ł���̂ŁA���Ԍv�Z�ʂ�O(nW)�ƂȂ�܂��B�[���D��T���̂Ƃ���肩�Ȃ荂�����ł������ƂɂȂ�܂��B

@@author:nabeyang@@
@@category:�v���O���~���O@@
