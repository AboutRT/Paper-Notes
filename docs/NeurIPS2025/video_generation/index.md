---
title: >-
  NeurIPS2025 视频生成方向 7篇论文解读
description: >-
  7篇NeurIPS2025 视频生成方向论文深度解读，每篇5分钟读懂核心思想。每篇笔记含一句话总结、背景动机、方法详解、实验数据、亮点洞察与局限性分析。
---

<!-- 由 src/gen_blog_index.py 自动生成 -->
# 🎬 视频生成

**🧠 NeurIPS2025** · **7** 篇论文解读

**[Autoregressive Adversarial Posttraining For Realtime Interac](autoregressive_adversarial_posttraining_for_realtime_interac.md)**

:   提出 AAPT（Autoregressive Adversarial Post-Training），通过三阶段后训练流程（扩散适配→一致性蒸馏→对抗训练）将预训练的 8B 视频扩散 Transformer 转化为单步自回归实时视频生成器，利用 student-forcing 训练策略有效抑制误差累积，在单张 H100 上以 24fps/736×416 流式生成长达一分钟（1440帧）的视频，同时支持姿态控制和相机控制等实时交互应用。

**[Photography Perspective Composition Towards Aesthetic Perspective Recommendation](photography_perspective_composition_towards_aesthetic_perspective_recommendation.md)**

:   首次提出摄影视角构图（PPC），超越传统 2D 裁剪，通过 3D 透视变换生成"差→优"的构图过程视频，并基于人类评估训练视角质量评估模型，帮助普通用户提升摄影构图水平。

**[Scaling Rl To Long Videos](scaling_rl_to_long_videos.md)**

:   提出 LongVILA-R1 全栈框架，通过构建 104K 长视频推理数据集、两阶段 CoT-SFT + RL 训练流水线、以及高效的多模态强化学习序列并行 (MR-SP) 系统，将 VLM 的推理能力扩展到长视频（最高支持 8192 帧），在 VideoMME 上达到 65.1%/71.1%。

**[Seeing The Wind From A Falling Leaf](seeing_the_wind_from_a_falling_leaf.md)**

:   本文提出端到端可微逆图形学框架，通过联合建模物体几何、物理属性和力表示，从视频中恢复不可见的力场（如风场），并支持基于物理的视频生成与编辑。

**[Training-Free Efficient Video Generation Via Dynamic Token Carving](training-free_efficient_video_generation_via_dynamic_token_carving.md)**

:   提出 Jenga，一种即插即用的视频扩散 Transformer 推理加速管线，通过 3D 空间填充曲线驱动的动态注意力剪裁和渐进分辨率生成的协同设计，在多个 Video DiT 模型上实现 6-9 倍加速且几乎无质量损失。

**[Video Diffusion Models Excel At Tracking Similar-Looking Objects Without Supervi](video_diffusion_models_excel_at_tracking_similar-looking_objects_without_supervi.md)**

:   本文发现预训练视频扩散模型在高噪声去噪阶段内在地学到了运动表征，无需任何跟踪专用训练即可用于跟踪外观相似的物体，提出的 TED 方法在 DAVIS 等基准上以最高 6% 的改进超越了 17 种自监督方法。

**[Video Killed The Energy Budget Characterizing The Latency And Power Regimes Of O](video_killed_the_energy_budget_characterizing_the_latency_and_power_regimes_of_o.md)**

:   本文对开源文本到视频（T2V）模型进行系统性的延迟和能耗刻画：以 WAN2.1-T2V 为参考模型建立了基于 FLOP 分解的 compute-bound 理论解析模型，实验验证了空间/时间维度的二次缩放和去噪步数的线性缩放规律，并横向对比了 7 个 T2V 模型发现能耗差异可达约 3000 倍。
