# 简约卷积

简约卷积是我们在论文“<a href="https://www.sciencedirect.com/science/article/abs/pii/S0031320320305252">Wang, Zi-Rui, and Jun Du. "Joint architecture and knowledge distillation in CNN for Chinese text recognition." Pattern Recognition 111 (2021): 107722.</p>”中提出的一种低存储、低计算量卷积模块，我们用它直接替换文本/文字识别网络中的常规卷积。特别地，简约卷积模块可以只通过一个参数进行大小调节。如果与知识蒸馏相配合，可以获得一个与大网络性能相当的小模型。

&emsp;它的迷人结构如下图所示：
<div align=center>
<img src=https://github.com/Wukong90/Parsimonious_Convolution/blob/main/Par_conv.png height=250>
</div>
简约卷积对经过Channel Shuffle的当前输入特征图划分为两部分，一条支路由深度可分离卷积与逐点卷积构成，其中变量ω为通道数缩放因子，另一条支路为常规逐点卷积。通过ω可以方便地实现卷积模块大小可控。

&emsp;下图展示了在我们的实验中,常规卷积与简约卷积的权重分布。可以观察到虽然大多数权重都集中在零值附近,但是简约卷积中权重分布更加平坦。直观地感觉到简约卷积中的"有用"权重比例更高，因此虽然是一个十分小的网络，也能够达到大网络一样的精度。
<div align=center>
<img src=https://github.com/Wukong90/Parsimonious_Convolution/blob/main/weights_dis.png height=250>
</div>

# 引用
如果你使用了我们的代码或从事的研究与我们的内容有关,请引用我们的工作.
