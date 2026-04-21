---
title: >-
  ECCV2024 图学习方向 5篇论文解读
description: >-
  5篇ECCV2024 图学习论文解读，主题涵盖：针对多标签类增量学习(MLCIL)中部分标签导致的、提出样本级偏置预测方法 SBP，通过、提出首个全图卷积多标签识别模型 GKGNet等，每篇含核心思想与方法详解。
---

<!-- 由 src/gen_blog_index.py 自动生成 -->
# 🕸️ 图学习

**🎞️ ECCV2024** · **5** 篇论文解读

**[Confidence Self-Calibration for Multi-Label Class-Incremental Learning](confidence_self-calibration_for_multi-label_class-incremental_learning.md)**

:   针对多标签类增量学习(MLCIL)中部分标签导致的过度自信预测和假阳性错误问题，提出 Confidence Self-Calibration (CSC) 框架，通过类增量图卷积网络(CI-GCN)校准标签关系 + 最大熵正则化校准置信度，在 MS-COCO 和 VOC 上大幅超越 SOTA。

**[Fine-Grained Scene Graph Generation via Sample-Level Bias Prediction](fine-grained_scene_graph_generation_via_sample-level_bias_prediction.md)**

:   提出样本级偏置预测方法 SBP，通过 Bias-Oriented GAN 利用物体对 union region 的上下文信息预测样本特异性纠偏向量，将粗粒度关系修正为细粒度关系，在 VG/GQA/VG-1800 上相比数据集级纠偏方法平均提升 5.6%/3.9%/3.2% 的 Average@K。

**[GKGNet: Group K-Nearest Neighbor Based Graph Convolutional Network for Multi-Label Image Recognition](gkgnet_group_k-nearest_neighbor_based_graph_convolutional_network_for_multi-labe.md)**

:   提出首个全图卷积多标签识别模型 GKGNet，通过 Group KNN 机制动态构建标签与图像区域间的图结构，在 MS-COCO 和 VOC2007 上以更低计算量取得 SOTA。

**[SENC: Handling Self-collision in Neural Cloth Simulation](senc_handling_self-collision_in_neural_cloth_simulation.md)**

:   提出 SENC，通过基于 Global Intersection Analysis (GIA) 的自碰撞损失和自碰撞感知图神经网络，首次在自监督神经布料模拟中有效解决布料自碰撞问题。

**[Synchronous Diffusion for Unsupervised Smooth Non-Rigid 3D Shape Matching](synchronous_diffusion_for_unsupervised_smooth_non-rigid_3d_shape_matching.md)**

:   提出同步扩散正则化方法用于无监督非刚性3D形状匹配，核心思想是"在两个形状上同步地扩散同一函数应产生一致输出"，通过这一简单而高效的正则化可以显著提升现有深度功能映射方法的匹配平滑性，在FAUST、SCAPE、TOPKIDS等多个数据集上达到SOTA。
