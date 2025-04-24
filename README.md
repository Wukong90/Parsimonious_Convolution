# Parsimonious_Convolution

简约卷积是我们在论文“<a href="https://arxiv.org/pdf/2410.11670">Leveraging Structure Knowledge and Deep Models for the Detection of Abnormal Handwritten Text</p>”
中提出的一种低存储、低计算量卷积模块，我们用它直接替换手写文本识别网络中的常规卷积。特别地，简约卷积模块可以只通过一个参数进行大小调节。如果与知识蒸馏相配合，可以获得一个与大网络性能相当的较小模型。

它的迷人结构如下图所示：
<div align=center>
<img src=https://github.com/Wukong90/EHT-dataset/blob/main/original_images/page_sample.png>
</div>
