---
title: >-
  ECCV2024 强化学习方向 2篇论文解读
description: >-
  2篇ECCV2024 强化学习论文解读，主题涵盖：提出AdaGlimpse，利用Soft、利用视觉语言模型 (MineCLIP) 的等，每篇含核心思想与方法详解。
---

<!-- 由 src/gen_blog_index.py 自动生成 -->
# 🎮 强化学习

**🎞️ ECCV2024** · **2** 篇论文解读

**[AdaGlimpse: Active Visual Exploration with Arbitrary Glimpse Position and Scale](adaglimpse_active_visual_exploration_with_arbitrary_glimpse_position_and_scale.md)**

:   提出AdaGlimpse，利用Soft Actor-Critic强化学习从连续动作空间中选择任意位置和尺度的glimpse，结合弹性位置编码的ViT编码器实现多任务（重建/分类/分割）的主动视觉探索，以仅6%像素超越了使用18%像素的SOTA方法。

**[Visual Grounding for Object-Level Generalization in Reinforcement Learning](visual_grounding_for_object-level_generalization_in_reinforcement_learning.md)**

:   利用视觉语言模型 (MineCLIP) 的 visual grounding 能力生成目标物体的 confidence map，通过奖励设计和任务表征两条路径将 VLM 知识迁移到强化学习中，实现对未见物体和指令的零样本泛化。
