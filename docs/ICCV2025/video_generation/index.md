---
title: >-
  ICCV2025 视频生成方向 8篇论文解读
description: >-
  8篇ICCV2025 视频生成方向论文深度解读，每篇5分钟读懂核心思想。每篇笔记含一句话总结、背景动机、方法详解、实验数据、亮点洞察与局限性分析。
---

<!-- 由 src/gen_blog_index.py 自动生成 -->
# 🎬 视频生成

**📹 ICCV2025** · **8** 篇论文解读

**[Adversarial Distribution Matching For Diffusion Distillation Towards Efficient I](adversarial_distribution_matching_for_diffusion_distillation_towards_efficient_i.md)**

:   提出对抗分布匹配（ADM）框架，用基于扩散模型的判别器以对抗方式隐式对齐真伪分数估计器的潜空间预测，结合对抗蒸馏预训练（ADP），在SDXL上实现高质量单步图像生成，并在SD3和CogVideoX上取得高效多步图像/视频合成的新基准。

**[Aligning Moments In Time Using Video Queries](aligning_moments_in_time_using_video_queries.md)**

:   提出MATR（Moment Alignment TRansformer），通过双阶段序列对齐机制和自监督预训练策略实现视频到视频的时刻检索（Vid2VidMR），在ActivityNet-VRL上R@1和mIoU分别提升13.1%和8.1%（绝对值），并构建了新的体育领域数据集SportsMoments。

**[Causal-Entity Reflected Egocentric Traffic Accident Video Synthesis](causal-entity_reflected_egocentric_traffic_accident_video_synthesis.md)**

:   提出 Causal-VidSyn 扩散模型，通过事故原因问答（ArA）和驾驶员注视引导的因果 token 选择（CTS&CTG）机制，实现对自车视角交通事故视频中因果实体的精确定位与生成，同时构建了最大规模驾驶员注视数据集 Drive-Gaze（154 万帧）。

**[Dual-Expert Consistency Model For Efficient And High-Quality Video Generation](dual-expert_consistency_model_for_efficient_and_high-quality_video_generation.md)**

:   通过分析一致性蒸馏中不同噪声水平下的优化冲突，提出参数高效的双专家一致性模型（DCM），分别用语义专家和细节专家处理高噪声/低噪声阶段的蒸馏，仅用4步采样即可达到接近50步原始模型的视频生成质量。

**[Long Context Tuning For Video Generation](long_context_tuning_for_video_generation.md)**

:   本文提出 Long Context Tuning (LCT)，将预训练单镜头视频扩散模型的上下文窗口扩展到场景级别，通过交错 3D RoPE、异步噪声策略和上下文因果注意力，实现跨镜头视觉/动态一致性的多镜头场景生成，并展现出零样本组合生成等涌现能力。

**[Multi-Identity Human Image Animation With Structural Video Diffusion](multi-identity_human_image_animation_with_structural_video_diffusion.md)**

:   提出Structural Video Diffusion,通过身份特定嵌入和RGB-深度-法线联合学习,首次实现多身份人体视频生成中的外观一致性保持和3D感知的人-物交互建模。

**[Quantifying And Narrowing The Unknown Interactive Text-To-Video Retrieval Via Un](quantifying_and_narrowing_the_unknown_interactive_text-to-video_retrieval_via_un.md)**

:   提出UMIVR框架，通过显式量化文本歧义、映射不确定性和帧质量三种不确定性，自适应生成澄清问题来迭代精化用户查询，在MSR-VTT-1k等多个基准上实现交互式文本视频检索的显著提升。

**[Versatile Transition Generation With Image-To-Video Diffusion](versatile_transition_generation_with_image-to-video_diffusion.md)**

:   本文提出 VTG，一个统一的过渡视频生成框架，通过插值初始化（噪声/LoRA/文本 SLERP）、双向运动微调和 DINOv2 表征对齐正则化，在单一框架中处理物体变形、运动预测、概念混合和场景过渡四类任务。
