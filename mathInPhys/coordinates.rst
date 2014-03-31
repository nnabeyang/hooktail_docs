==========================
�F�X�ȍ��W�n
==========================

�����w�ō��W�n���l���邱�Ƃ͂ƂĂ��厖�ł��B
�܂��A���W�ɂ��ĕ׋�����Ƃǂ�Ȑ��E�������Ă���̂��ɂ��Čy���G��܂��B
���̌�A��̓I�ɐF�X�ȍ��W�n���l���鏀���Ƃ��āA���W�ϊ��̍ۂɏo�Ă���v�ʈ��q�Ƃ����ʂƁA
�f�J���g���W�n�ȊO�ł̔������Z�q(grad, div, curl��)���ǂ��Ȃ�̂������Ă݂邱�Ƃɂ��܂��傤�B


���W���猩���Ă��邱��
--------------------------

�����̌v�Z�ł́A�f�J���g���W�n�ȊO�̍��W�n���З͂𔭊������ʂ��悭����܂��B
�K�؂ȍ��W�ϊ����قǂ����ƁA���������ȒP�Ȍ`�ɂȂ��Ė��̌��ʂ����ǂ��Ȃ邱�Ƃ�����܂����A
���G�Ȕ������������ϐ������`�ɋA�����ĉ�����悤�ɂȂ邱�Ƃ�����̂ł�
�i�����w�ł́A������������ϐ������`�ɋA�������邱�Ƃ����W�ϊ��̖ڕW�ł��邱�Ƃ��ƂĂ������̂ł��B
���̂��Ƃ͓��ɋ������Ă����܂��j�B

�t�ɁA���W�ϊ����l���邱�Ƃ́A���W�ϊ��ɂ���Ă��ω����Ȃ��􉽊w�I�Ȑ�����
�l�@���邱�Ƃɂ����W���邱�Ƃł��傤�B���W�ϊ��ɑ΂��ĕs�ςȐ����́A
��͗͊w�A�����`���̗��_�A�����􉽊w�Ȃǂ�׋�����Ƃ��ɂƂĂ��d�v�ɂȂ�܂��B

�����w�ł悭�g����x�b�Z���֐��A���W�����h���֐��Ȃǂ̓���֐��̑����́A
������W�n�Ɩ��ڂȊ֌W�������Ă��܂��̂ŁA
�F�X�ȍ��W�n��׋����Ă��炻����������֐��̕׋������������Ӗ���������₷���Ƃ������Ƃ�����܂��B
�Ȃ񂾂����W�ϊ��̐�ɂ͓�����E���L�����Ă������Ȋ����ł��ˁB


�v�ʈ��q
--------------------------

�f�J���g���W�n :math:`(x_{1},x_{2},x_{3})` �ƁA����V�������W�n :math:`(q_{1},q_{2},q_{3})` ��
�֌W�͈�ʂɎ��̂悤�ɕ\�����Ƃ��ł��܂��B���݂������֐��ɂȂ��Ă���Ƃ������Ƃł��B

.. math::
   x_{i}=x_{i}(q_{1},q_{2},q_{3})

.. math::
   q_{i}=q_{i}(x_{1},x_{2},x_{3})

�������� :math:`(x_{1},x_{2},x_{3})` �̑S�����͎�(1)�̂悤�ɕ\����܂��B

.. math::
   \displaystyle dx_{i}={\partial x_{i}\over \partial q_{1}}
   dq_{1}+{\partial x_{i}\over \partial q_{2}}
   dq_{2}+{\partial x_{i}\over \partial q_{3}}
   dq_{3}
   \tag{1}

����A��ԏ�̔����ȓ�_�Ԃ̋��� :math:`ds` �͎��̂悤�ɕ\���ł��܂��B

.. math::
   ds^{2}&=dx_{1}^{2}+dx_{2}^{2}+dx_{3}^{2}\\
   &=(h_{11}dq_{1})^{2}+(h_{22}dq_{2})^{2}+(h_{33}dq_{3})^{2}+h_{12}^{2}dq_{1}dq_{2}+h_{23}^{2}dq_{3}dq_{3}+h_{31}^{2}dq_{3}dq_{1}\tag{2}   


������ :math:`h` �Ƃ����ʂ������Ȃ�o�Ă��܂������A����͌v�ʈ��q�ƌĂ΂��ʂł��B
�v�ʈ��q�Ƃ́A��̍��W�n :math:`(x_{1},x_{2},x_{3})` , :math:`(q_{1},q_{2},q_{3})` �̊ԂɎ�(2)
�����藧�悤�ɖ�����l�������ꂽ�ʂ��ƌ����Ă��ǂ��ł��傤�B
����͒�`�ł�����A���܂莮(2)�ŔY�܂Ȃ��ŉ������B

��ʂ� :math:`(q_{1},q_{2},q_{3})` �͕K�����������̎��������킯�ł͂���܂��񂪁i�Ⴆ�Ίp�x�j�A
�v�ʈ��q���|������ :math:`hdq_{i}` �͕K�������̎����ɂȂ邱�Ƃɒ��ӂ��܂��傤�B
�v�ʈ��q�Ƃ͂��̂悤�Ȏ������������ʂȂ̂ł��B

��(1)���悵�Ď�(2)�ɑ������ƈ�ʂɎ����𓾂܂��B���ꂪ�v�ʈ��q�̐��w�I���̂ł��B

.. math::
   \displaystyle h_{ij}^{2}={\partial x_{1}\over \partial q_{i}}
   {\partial x_{1}\over \partial q_{j}}
   +{\partial x_{2}\over \partial q_{i}}
   {\partial x_{2}\over \partial q_{j}}
   +{\partial x_{3}\over \partial q_{i}}
   {\partial x_{3}\over \partial q_{j}}

���R�r�A���ƌv�ʈ��q
--------------------------

�v�ʈ��q�ƃ��R�r�A���Ƃ͊֌W������܂��B
�����̋c�_�͂����ɂ͎g���܂��񂩂�A���R�r�A���������������Y��Ă��܂����l�͓ǂݔ�΂��Ă��������B
���W�n���\������ȖʌQ���݂��ɒ�������ꍇ�A�v�ʈ��q�̑Ίp�v�f�͗�ɂȂ�܂��B
�ȒP�̂��߂ɂ��̂悤�ȍ��W�n�������l���܂��傤�B

.. math::
   ds^{2}&=dx_{1}^{2}+dx_{2}^{2}+dx_{3}^{2}\\
   &=(h_{11}dq_{1})^{2}+(h_{22}dq_{2})^{2}+(h_{33}dq_{3})^{2}\equiv h_{1}^{2}dq_{1}^{2}+h_{2}^{2}dq_{2}^{2}+h_{3}^{2}dq_{3}^{2}

�v�ʈ��q�͊ȒP�̂��� :math:`h_{11}` �� :math:`h_{1}` �̂悤�ɏ����Ă��܂��܂����B
���̂Ƃ��ʐϗv�f�A�̐ϗv�f�͎����̂悤�ɂȂ邱�Ƃ��킩��ł��傤���B

.. math::
   dS_{ij}=h_{i}h_{j}dq_{i}dq_{j} 

.. math::
   dV=h_{1}h_{2}h_{3}dq_{1}dq_{2}dq_{3} 

���R�r�A���̒�`�Ɣ�ׂĂ݂�ƁA�����Ɋ܂܂��v�ʈ��q�̐ς͎��̃��R�r�A���ɓ��������Ƃ�������܂��ˁB
���R�r�A���ƌv�ʈ��q�͐e�ʂ������̂ł��B
        
.. math::
   \displaystyle h_{i}h_{j}={\partial (x_{i},x_{j})\over \partial (q_{i},q_{j})}

.. math::
   \displaystyle h_{i}h_{j}h_{k}={\partial (x_{i},x_{j},x_{k})\over \partial (q_{i},q_{j},q_{k})}
         

�����x�N�g�����Z�q
--------------------------

�x�N�g���̔��ϕ��ɁA�O�p�`�̋L������������o�Ă����̂��o���Ă��܂����H :math:`\nabla \times {\boldmath V}` 
�Ƃ� :math:`\triangle \bm{V}` �Ƃ��������̂ł��B���������L���͔����x�N�g�����Z�q�ƌĂ΂�A
�x�N�g�����������L���ł��B�����w�̕������ɂ͂悭�o�ꂵ�܂�
�i�悭������Ȃ��l�́A��� �x�N�g�����_ �̃y�[�W�𕜏K���ĉ������j�B
�O�p�`�̋L���ŏ����Ă������͍��W�n�̎����ɂ͋���Ȃ��̂ł����A
���ۂɔ����v�Z���s���Ƃ��ɂ͍��W�̎����ɂ���Čv�Z�������ς��Ă��܂��B
�ł�����A�f�J���g���W�n�ɂ���������x�N�g�����Z�q�Ɣ�ׂāA
���̍��W�n�ɂ���������x�N�g�����Z�q���ǂ�������̂������Ă������Ƃ́A
����A�F�X�Ȕ�����������F�X�ȍ��W�n�̏�ōl���Ă������߂ɂ��ƂĂ��d�v�Ȃ��ƂȂ̂ł��B
���Ȃ��ƂɁA�x�N�g���̊|���Z�ɂ́A���ρA�O�ςȂǂ̎�ނ�����܂�������A
�����x�N�g�����Z�q�̌v�Z�ɂ�����̎�ނ�����̂ł��B
�ȉ��ɁA���z�A���U�A��]�A���v���V�A����4�̉��Z�q�ɂ��Č��Ă����܂��B



(1)���z(grad):
^^^^^^^^^^^^^^^^^^^^^^^^^^

���z�x�N�g���͋�ԓI�ȕω�����\���x�N�g���ł����B
���̃x�N�g���̕����́A�ő���ɕω����N����悤�Ȍ����Ɏ���܂��B���̒�`�ɗ����Ԃ��čl���܂��傤�B
        
�Ⴆ�� :math:`q_{1}=\mathrm{const.}` �Ȃ�Ȗʂɐ����ȕ����̕ω����́A :math:`q_{2},q_{3}` �����ɕۂ��� :math:`q_{1}` ������ω�������ꍇ�̕ω����Ƃ��ĕ\�������̂Ŏ��̂悤�ɂȂ�܂��B�����͑厖�ȂƂ���Ȃ̂ŁA�悭������Ȃ��l�͎��̈Ӗ����̊��ł���܂ł�������l���Č��ĉ������B�x�N�g���̉��ɏc���Ə����ȂP�������Ă���̂́u�x�N�g���̑�ꐬ���������l����v�Ƃ����Ӗ��ł��B

.. math::
   \displaystyle \nabla \psi \Big\arrowvert _{1}={\partial \psi \over \partial s_{1}}
   ={1\over h_{1}}
   {\partial \psi \over \partial q_{1}}
         
���̐��������l�Ȃ̂ŁA���ǁA���z�͎����ŕ\�����Ƃ��ł��܂��B

.. math::
   \displaystyle \nabla \phi =\bigg({\partial \phi \over \partial s_{1}}
   ,\  {\partial \phi \over \partial s_{2}}
   ,\  {\partial \phi \over \partial s_{3}}
   \bigg)=\bigg({1\over h_{1}}
   {\partial \phi \over \partial q_{1}}
   ,\  {1\over h_{2}}
   {\partial \phi \over \partial q_{2}}
   ,\  {1\over h_{3}}
   {\partial \phi \over \partial q_{3}}
   \bigg) 

(2)���U(div):
^^^^^^^^^^^^^^^^^^^^^^^^^^

���U�̒�`�͎����ł����ˁi�Y��Ă��܂����l�� �x�N�g�����_ �𕜏K���ĉ������I�j�B

.. math:: 
   \displaystyle \nabla \cdot V=\lim \limits _{\intop \limits d\tau \rightarrow 0}{\intop \limits V\cdot d\sigma \over \intop \limits d\tau }

�����ŁA�����̖������̐ϗv�f�� :math:`d\tau =h_{1}h_{2}h_{3}dq_{1}dq_{2}dq_{3}` �Ɨ^�����Ă������Ƃ��v���o���܂��傤�B���q�̖ʐϕ������߂邽�߂ɁA�܂���ꐬ���������l���܂��B
         
.. math::
   \displaystyle \intop \limits V\cdot d\sigma \Big\arrowvert _{1}
   &=\Big[V_{1}h_{2}h_{3}+{\partial (V_{1}h_{2}h_{3})\over \partial q_{1}}
   dq_{1}\Big]dq_{2}dq_{3}-V_{1}h_{2}h_{3}dq_{2}dq_{3}\\
   &={\partial (V_{1}h_{2}h_{3})\over \partial q_{1}}
   dq_{1}dq_{2}dq_{3} 
         
��񐬕��A��O�����ɂ��Ă����l�̌v�Z�����藧���܂�����A�����𑫂����킹��Ύ����̂悤�ɂȂ�܂��ˁB

.. math::
   \displaystyle \intop \limits V\cdot d\sigma =\Big[{\partial (V_{1}h_{2}h_{3})\over \partial q_{1}}
   +{\partial (V_{2}h_{3}h_{1})\over \partial q_{2}}
   +{\partial (V_{3}h_{1}h_{2})\over \partial q_{3}}
   \Big]dq_{1}dq_{2}dq_{3} 

����� :math:`d\tau =h_{1}h_{2}h_{3}dq_{1}dq_{2}dq_{3}` �Ŋ���΁A���U�̒�`��莟�̂悤�ɂȂ�܂��B

.. math::
   \displaystyle \nabla \cdot V={1\over h_{1}h_{2}h_{3}}
   \bigg[{\partial (V_{1}h_{2}h_{3})\over \partial q_{1}}
   +{\partial (V_{2}h_{3}h_{1})\over \partial q_{2}}
   +{\partial (V_{3}h_{1}h_{2})\over \partial q_{3}}
   \bigg] 
         

(3)��](curl):
^^^^^^^^^^^^^^^^^^^^^^^^^^
��]�����߂�ɂ̓X�g�[�N�X�̒藝���g���܂��B�܂� :math:`q_{1}=\mathrm{const.}` �Ȃ�Ȗʏ�̉�]���l���Ă݂܂��B
�X�g�[�N�X�̒藝��莟�������藧���܂��B�X�g�[�N�X�̒藝�͂ƂĂ��d�v�Ȓ藝�ł��̂ŁA
�Y��Ă��܂����l�� �x�N�g�����_ �̂Ƃ���𕜏K���Ă����ĉ������B

.. math::
   \displaystyle \int _{S}\nabla \times V\cdot d\sigma =\nabla \times V\Big\arrowvert _{1}h_{2}h_{3}dq_{2}dq_{3}=\ointop \limits V\cdot d\lambda

�����ŉE�ӂ̎���ϕ��͎��̐}������ΈӖ���������܂��ˁB
�}��1,2,3,4�̒����ɉ����ď��Ԃɐ��ϕ������Ă����܂��B

.. image:: _images/Joh-stokes7.png

.. math::
   \displaystyle \ointop \limits V\cdot d\lambda 
   &=V_{2}h_{2}dq_{2}+\Big[V_{3}h_{3}+{\partial (V_{3}h_{3})\over \partial q_{2}}
   dq_{2}\Big]dq_{3}-\Big[V_{2}h_{2}+{\partial (V_{2}h_{2})\over \partial q_{3}}
   dq_{3}\Big]dq_{2}-V_{3}h_{3}dq_{3}\\
   &=\Big[{\partial (h_{3}V_{3})\over \partial q_{2}}
   -{\partial (h_{2}V_{2})\over \partial q_{3}}
   \Big]dq_{2}dq_{3} 

�����莟���������܂��B

.. math::
   \displaystyle \nabla \times V\Big\arrowvert _{1}={1\over h_{2}h_{3}}
   \Big[{\partial (h_{3}V_{3})\over \partial q_{2}}
   -{\partial (h_{2}V_{2})\over \partial q_{3}}
   \Big]dq_{2}dq_{3} 
         
�S�Ă̐����ɂ��Čv�Z���đ������킹��ƁA���̂悤�ɂȂ�܂��B

.. math::
   \displaystyle \nabla \times {\boldmath V}={1\over h_{2}h_{3}}
   \Big[{\partial (h_{3}V_{3})\over \partial q_{2}}
   -{\partial (h_{2}V_{2})\over \partial q_{3}}
   \Big]dq_{2}dq_{3} 
   +{1\over h_{3}h_{1}}
   \Big[{\partial (h_{1}V_{1})\over \partial q_{3}}
   -{\partial (h_{3}V_{3})\over \partial q_{1}}
   \Big]dq_{3}dq_{1} 
   +{1\over h_{1}h_{2}}
   \Big[{\partial (h_{2}V_{2})\over \partial q_{1}}
   -{\partial (h_{3}V_{3})\over \partial q_{1}}
   \Big]dq_{1}dq_{2} 

����ł͒����Ċo����̂���ςł�����A���̂悤�� �s��_ �̌`�ɂ܂Ƃ߂�Ƃ��ꂢ�ł��B

.. math::
   \nabla \times {\boldmath V}=\frac{1}{h_{1} h_{2} h_{3}}
   \left|
   \begin{array}{ccc}
   h_{1}{\boldmath e}_1 & h_{2}{\boldmath e}_2 & h_{3}{\boldmath e}_3 \\
   \frac{\partial}{\partial q_{1}} & \frac{\partial}{\partial q_{2}} & \frac{\partial}{\partial q_{3}} \\
   h_{1} V_1 & h_{2} V_2 & h_{3} V_3 \\
   \end{array}
   \right|

����]�̂��Ƃ��Acurl�ł͂Ȃ���rot(���[�e�[�V����)�ƌĂԐl�����܂����A�Ӗ��͓����ł��B

(4)���v���V�A��:
^^^^^^^^^^^^^^^^^^^^^^^^^^
�Ō�Ƀ��v���V�A���ɂ��ď��������G��܂��B
���v���V�A�� :math:`\triangle` �̓i�u�� :math:`\nabla` ���悵�����̂ł����B
������A����������Ƃ͖����̂ł��B���z�̌v�Z�Ɣ��U�̌v�Z��g�ݍ��킹�邾���ł��B
�x�N�g���ɍ�p����Ƃ��ɂ͐������ɍ�p������̂ł����ˁB

.. math::
   \triangle \phi =\nabla \cdot (\nabla \phi)

.. math::
   \triangle \bm{V}=(\nabla \cdot (\nabla V_{1}), \nabla \cdot (\nabla V_{2}),\nabla \cdot (\nabla V_{3}) )

���łɌ��z�Ɣ��U�̌v�Z�͋��߂��̂ł�����A���v���V�A�����ǂ��Ȃ邩�����Ōv�Z���Ă݂Ă��������B�����͂��̃y�[�W�̈�ԍŌ�ɏ����Ă����܂��B


�����炢
--------------------------
���̃y�[�W�̌��ʂ́A�܂���ł悭�g���܂�����A�����Ƃ��Ă܂Ƃ߂Ă����܂��B

.. math::
   \displaystyle h_{ij}^{2}={\partial x_{1}\over \partial q_{i}}
   {\partial x_{1}\over \partial q_{j}}
   +{\partial x_{2}\over \partial q_{i}}
   {\partial x_{2}\over \partial q_{j}}
   +{\partial x_{3}\over \partial q_{i}}
   {\partial x_{3}\over \partial q_{j}}

.. math::
   \displaystyle \nabla \phi =\bigg({\partial \phi \over \partial s_{1}}
   ,\  {\partial \phi \over \partial s_{2}}
   ,\  {\partial \phi \over \partial s_{3}}
   \bigg)=\bigg({1\over h_{1}}
   {\partial \phi \over \partial q_{1}}
   ,\  {1\over h_{2}}
   {\partial \phi \over \partial q_{2}}
   ,\  {1\over h_{3}}
   {\partial \phi \over \partial h_{3}}
   \bigg) 

.. math::
   \displaystyle \nabla \cdot V={1\over h_{1}h_{2}h_{3}}
   \bigg[{\partial (V_{1}h_{2}h_{3})\over \partial q_{1}}
   +{\partial (V_{2}h_{3}h_{1})\over \partial q_{2}}
   +{\partial (V_{3}h_{1}h_{2})\over \partial q_{3}}
   \bigg] 

.. math::
   \nabla \times {\boldmath V}=\frac{1}{h_{1} h_{2} h_{3}}
   \left|
   \begin{array}{ccc}
   h_{1}{\boldmath e}_1 & h_{2}{\boldmath e}_2 & h_{3}{\boldmath e}_3 \\
   \frac{\partial}{\partial q_{1}} & \frac{\partial}{\partial q_{2}} & \frac{\partial}{\partial q_{3}} \\
   h_{1} V_1 & h_{2} V_2 & h_{3} V_3 \\
   \end{array}
   \right|

.. math::
   \triangle \phi =\nabla \cdot (\nabla \phi) =
   {1\over h_{1}h_{2}h_{3}}
   \bigg[{\partial \over \partial q_{1}}
   (\frac{h_{2} h_{3}}{h_{1}}{\partial \phi \over \partial q_{1}})
   +{\partial \over \partial q_{2}}
   (\frac{h_{3} h_{1}}{h_{2}}{\partial \phi \over \partial q_{2}})
   +{\partial \over \partial q_{3}}
   (\frac{h_{1} h_{2}}{h_{3}}{\partial \phi \over \partial q_{3}})
   \bigg] 

.. _�s��: http://www12.plala.or.jp/ksp/mathInPhys/determinant/index.html
.. _�x�N�g�����: http://www12.plala.or.jp/ksp/formula/mathFormula/html/node59.html

