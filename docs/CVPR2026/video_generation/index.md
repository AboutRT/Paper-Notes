---
title: >-
  CVPR2026 视频生成方向 9篇论文解读
description: >-
  9篇CVPR2026 视频生成方向论文深度解读，每篇5分钟读懂核心思想。每篇笔记含一句话总结、背景动机、方法详解、实验数据、亮点洞察与局限性分析。
---

<!-- 由 src/gen_blog_index.py 自动生成 -->
# 🎬 视频生成

**📷 CVPR2026** · **9** 篇论文解读

**[Chain Of Event-Centric Causal Thought For Physically Plausible Video Generation](chain_of_event-centric_causal_thought_for_physically_plausible_video_generation.md)**

:   将物理现象建模为因果连接的事件序列，通过物理公式驱动的事件链推理分解复杂物理过程，再用渐进式语义-视觉双提示引导现成视频扩散模型生成物理合理的因果演进视频。

**[Compressed-Domain-Aware Online Video Super-Resolution](compressed-domain-aware_online_video_super-resolution.md)**

:   CDA-VSR利用视频比特流中免费可得的压缩域信息（运动向量、残差图、帧类型）来分别指导帧对齐、特征融合和自适应重建，在REDS4数据集上比SOTA方法TMP提升PSNR达0.13dB的同时实现>2倍推理速度（~93 FPS@320×180，RTX 3090）。

**[First Frame Is The Place To Go For Video Content Customization](first_frame_is_the_place_to_go_for_video_content_customization.md)**

:   FFGo 揭示了视频生成模型的一个被忽视的固有能力——将首帧作为概念记忆缓冲区存储多个参考主体，仅通过 20-50 个训练样本的轻量 LoRA 适配即可激活这一能力，实现无需架构修改的多参考视频内容定制，在用户研究中以 81.2% 的首选率大幅超越现有方法。

**[Generative Neural Video Compression Via Video Diffusion Prior](generative_neural_video_compression_via_video_diffusion_prior.md)**

:   提出 GNVC-VD，首个基于 DiT 视频扩散模型（Wan2.1）的生成式神经视频压缩框架，通过 flow-matching 在时空潜变量上进行序列级生成式精炼，在极低码率（<0.03 bpp）下实现感知质量 SOTA 并显著减少闪烁伪影。

**[Interpretable Motion-Attentive Maps Spatio-Temporally Localizing Concepts In Vid](interpretable_motion-attentive_maps_spatio-temporally_localizing_concepts_in_vid.md)**

:   提出 GramCol 和 IMAP 两种无需训练/梯度的方法，利用 Video DiT 内部特征为任意文本概念（尤其是运动概念）生成可解释的时空显著性图，并在运动定位和零样本视频语义分割上取得 SOTA。

**[Let Your Image Move With Your Motion -- Implicit Multi-Object Multi-Motion Trans](let_your_image_move_with_your_motion_--_implicit_multi-object_multi-motion_trans.md)**

:   FlexiMMT 是首个支持隐式多目标多运动迁移的 I2V 框架，通过运动解耦掩码注意力机制 (MDMA) 和差异化掩码提取机制 (DMEM)，将多个参考视频的不同运动独立分配给目标图像中的不同物体，实现灵活组合式运动迁移。

**[Physical Simulator In-The-Loop Video Generation](physical_simulator_in-the-loop_video_generation.md)**

:   提出 PSIVG，首个将物理模拟器嵌入视频扩散模型推理循环的无训练框架：从模板视频重建 4D 场景和 3D 网格并初始化物理模拟器，生成物理一致轨迹引导视频生成，并通过 Test-Time Texture Consistency Optimization（TTCO）优化前景纹理一致性。用户研究中 82.3% 偏好率远超所有基线。

**[Semantic Satellite Communications For Synchronized](semantic_satellite_communications_for_synchronized.md)**

:   提出一种 LLM 驱动的自适应多模态语义卫星传输系统，通过双流生成架构（视频驱动音频生成 V2A / 音频驱动视频生成 A2V）实现跨模态语义解耦，结合动态关键帧更新机制和 LLM 智能体规划，在卫星带宽严重受限的条件下实现高保真音视频同步重建。

**[Training-Free Motion Factorization For Compositional Video Generation](training-free_motion_factorization_for_compositional_video_generation.md)**

:   提出一种无需训练的运动分解框架，将复杂场景运动拆分为静止、刚性运动和非刚性运动三类，通过结构化运动推理 (SMR) 消除提示语义歧义，再借助解耦运动引导 (DMG) 模块分别约束各类运动的生成，实现多实例多运动类别的组合视频合成。
