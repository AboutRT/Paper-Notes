---
title: >-
  CVPR2025 社会计算方向 4篇论文解读
description: >-
  4篇CVPR2025 社会计算论文解读，主题涵盖：将 Transformer 的深度方向视为离散时间、提出 Classifier-guided、本文提出Classifier-to-Bias（C2等，每篇含核心思想与方法详解。
---

<!-- 由 src/gen_blog_index.py 自动生成 -->
# 👥 社会计算

**📷 CVPR2025** · **4** 篇论文解读

**[As Language Models Scale, Low-order Linear Depth Dynamics Emerge](as_language_models_scale_low-order_linear_depth_dynamics_emerge.md)**

:   将 Transformer 的深度方向视为离散时间动力系统，发现在给定上下文内可以用仅 32 维的线性状态空间代理模型高精度预测层间灵敏度曲线（Spearman 达 0.99），而且令人惊讶的是：**模型越大，低阶线性代理越准确**——这是一条新的 scaling law。

**[Classifier-guided CLIP Distillation for Unsupervised Multi-label Classification](classifier-guided_clip_distillation_for_unsupervised_multi-label_classification.md)**

:   提出 Classifier-guided CLIP Distillation（CCD），通过 CAM 引导的局部视图标签聚合和 CLIP 预测去偏两项核心技术，在完全无标注的条件下达到与全监督方法持平的多标签分类性能（VOC12 上 90.1% mAP）。

**[Classifier-to-Bias: Toward Unsupervised Automatic Bias Detection for Visual Classifiers](classifier-to-bias_toward_unsupervised_automatic_bias_detection_for_visual_class.md)**

:   本文提出Classifier-to-Bias（C2B），首个无需任何标注数据的视觉分类器偏差自动发现框架，仅依靠分类任务的文本描述，利用LLM生成偏差候选并通过检索增强的生成-验证流程来识别预训练模型中的系统性偏差。

**[Learning from Neighbors: Category Extrapolation for Long-Tail Learning](learning_from_neighbors_category_extrapolation_for_long-tail_learning.md)**

:   发现更细粒度的类别划分天然减轻长尾不平衡的影响，提出用 LLM 发现与现有类别相关的细粒度辅助类 + 网络爬虫收集图像 + 邻近静默损失防止辅助类喧宾夺主，在 ImageNet-LT 上 Few 类提升 16 个百分点（41.4→57.4）。
