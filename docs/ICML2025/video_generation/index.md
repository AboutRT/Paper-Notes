---
title: >-
  ICML2025 视频生成方向 2篇论文解读
description: >-
  2篇ICML2025 视频生成方向论文深度解读，每篇5分钟读懂核心思想。每篇笔记含一句话总结、背景动机、方法详解、实验数据、亮点洞察与局限性分析。
---

<!-- 由 src/gen_blog_index.py 自动生成 -->
# 🎬 视频生成

**🧪 ICML2025** · **2** 篇论文解读

**[Diffusion Adversarial Post-Training For One-Step Video Generation](diffusion_adversarial_post-training_for_one-step_video_generation.md)**

:   提出对抗后训练（Adversarial Post-Training, APT）方法，将预训练的扩散模型直接用 GAN 对抗训练在真实数据上进行微调，实现单步生成 1024px 图像和 1280×720 24fps 视频，在视觉保真度上甚至超越原始 25 步扩散模型。

**[How Far Is Video Generation From World Model A Physical Law Perspective](how_far_is_video_generation_from_world_model_a_physical_law_perspective.md)**

:   通过构建 2D 物理仿真测试平台，系统性评估视频生成模型发现物理定律的能力，发现扩展模型规模仅能实现分布内泛化，无法实现分布外泛化，揭示模型采用"基于案例"的泛化机制而非抽象物理规则。
