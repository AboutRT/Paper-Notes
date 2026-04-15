---
title: >-
  ICLR2026 信号/通信方向 4篇论文解读
description: >-
  4篇ICLR2026 信号/通信方向论文深度解读，每篇5分钟读懂核心思想。每篇笔记含一句话总结、背景动机、方法详解、实验数据、亮点洞察与局限性分析。
---

<!-- 由 src/gen_blog_index.py 自动生成 -->
# 📡 信号/通信

**🔬 ICLR2026** · **4** 篇论文解读

**[Deterministic Bounds And Random Estimates Of Metric Tensors On Neuromanifolds](deterministic_bounds_and_random_estimates_of_metric_tensors_on_neuromanifolds.md)**

:   本文通过分析低维概率分布核空间的Fisher信息矩阵(FIM)谱性质，为神经网络参数空间(神经流形)上的度量张量建立了确定性上下界，并基于Hutchinson迹估计器引入了一族有界方差的无偏随机估计方法，仅需单次反向传播即可高效计算。

**[Group Representational Position Encoding](group_representational_position_encoding.md)**

:   提出 GRAPE 框架，基于群作用（group actions）统一了 Transformer 中乘法型（RoPE）和加法型（ALiBi/FoX）两大位置编码家族，证明 RoPE 和 ALiBi 是其精确特例，并提出路径积分加法变体 GRAPE-AP 在下游任务上超越现有方法。

**[Learning Molecular Chirality Via Chiral Determinant Kernels](learning_molecular_chirality_via_chiral_determinant_kernels.md)**

:   提出手性行列式核(ChiDeK)来编码 SE(3) 不变的手性矩阵，首次在 GNN 框架中统一处理中心手性和轴向手性，结合交叉注意力传播立体化学信息，在新构建的轴向手性基准上准确率提升 >7%。

**[Robust Preference Alignment Via Directional Neighborhood Consensus](robust_preference_alignment_via_directional_neighborhood_consensus.md)**

:   提出Robust Preference Selection (RPS)，一种无需重训练的推理时偏好对齐增强方法，通过从目标偏好的局部邻域采样多个候选方向并生成响应、再根据原始偏好选择最优响应，在OOD偏好上相比基线达到最高69%的胜率。
