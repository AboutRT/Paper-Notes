---
title: >-
  ICLR2026 视频生成方向 6篇论文解读
description: >-
  6篇ICLR2026 视频生成方向论文深度解读，每篇5分钟读懂核心思想。每篇笔记含一句话总结、背景动机、方法详解、实验数据、亮点洞察与局限性分析。
---

<!-- 由 src/gen_blog_index.py 自动生成 -->
# 🎬 视频生成

**🔬 ICLR2026** · **6** 篇论文解读

**[Arbitrary Generative Video Interpolation](arbitrary_generative_video_interpolation.md)**

:   ArbInterp 提出了一种支持任意时间戳、任意长度的生成式视频帧插值框架，通过时间戳感知旋转位置编码（TaRoPE）实现精准时间控制，并通过外观-运动解耦的条件注入策略实现长序列的无缝拼接。

**[Geometry-Aware 4D Video Generation For Robot Manipulation](geometry-aware_4d_video_generation_for_robot_manipulation.md)**

:   提出几何感知的4D视频生成框架，通过跨视角 pointmap 对齐监督在视频扩散模型中强制多视角3D一致性，无需相机位姿输入即可从新视角生成时空对齐的未来 RGB-D 序列，并可直接用 FoundationPose 从生成视频中恢复机器人末端执行器轨迹。

**[Language-Guided Open-World Video Anomaly Detection Under Weak Supervision](language-guided_open-world_video_anomaly_detection_under_weak_supervision.md)**

:   提出语言引导的开放世界视频异常检测范式 LaGoVAD，通过将异常定义建模为随机变量并以自然语言形式输入，从理论上规避概念漂移问题；同时构建了目前最大规模的视频异常数据集 PreVAD（35K 视频），在七个数据集上零样本 SOTA。

**[Learning Video Generation For Robotic Manipulation With Collaborative Trajectory](learning_video_generation_for_robotic_manipulation_with_collaborative_trajectory.md)**

:   提出 RoboMaster，通过协作轨迹（collaborative trajectory）将机械臂与物体的交互过程分解为前交互、交互和后交互三阶段，配合外观和形状感知的物体表示，实现高质量轨迹控制的机器人操作视频生成。

**[Streaming Autoregressive Video Generation Via Diagonal Distillation](streaming_autoregressive_video_generation_via_diagonal_distillation.md)**

:   提出 DiagDistill 对角蒸馏框架，通过对角去噪策略（早期多步、后期少步）和光流分布匹配，实现实时流式自回归视频生成，5秒视频仅需2.61秒（31 FPS），比未蒸馏模型加速277.3倍。

**[Target-Aware Video Diffusion Models](target-aware_video_diffusion_models.md)**

:   提出 target-aware 视频扩散模型，仅需一张输入图像和目标物体的分割 mask，即可生成演员与指定目标交互的视频；核心创新是引入 [TGT] 特殊 token 并设计选择性交叉注意力损失，使模型关注目标的空间位置，在目标对齐和视频质量上全面超越基线。
