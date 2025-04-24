# Parsimonious_Convolution

简约卷积是我们在论文“<a href="https://www.sciencedirect.com/science/article/abs/pii/S0031320320305252">Joint architecture and knowledge distillation in CNN for Chinese text recognition</p>”
中提出的一种低存储、低计算量卷积模块，我们用它直接替换文本/文字识别网络中的常规卷积。特别地，简约卷积模块可以只通过一个参数进行大小调节。如果与知识蒸馏相配合，可以获得一个与大网络性能相当的较小模型。

它的迷人结构如下图所示：
<div align=center>
<img src=https://github.com/Wukong90/Parsimonious_Convolution/blob/main/Par_conv.png height=250>
</div>

简约卷积对当前层输入特征图划分为两部分，一条支路由深度可分离卷积与逐点卷积构成，其中变量$\Omega$为通道数缩放因子，另一条支路为常规逐点卷积。
