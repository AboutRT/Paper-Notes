---
title: >-
  ECCV2024 具身智能方向 12篇论文解读
description: >-
  12篇ECCV2024 具身智能论文解读，主题涵盖：提出 STAformer 架构和两个基于、提出EconomicGrasp框架、提出 DISCO 框架，通过可微分场景语义表示和双等，每篇含核心思想与方法详解。
---

<!-- 由 src/gen_blog_index.py 自动生成 -->
# 🤖 具身智能

**🎞️ ECCV2024** · **12** 篇论文解读

**[AFF-ttention! Affordances and Attention models for Short-Term Object Interaction Anticipation](aff-ttention_affordances_and_attention_models_for_short-term_object_interaction_.md)**

:   提出 STAformer 架构和两个基于 affordance 的模块（环境 affordance 数据库 + 交互热点），将第一人称视频中的短期物体交互预测（STA）在 Ego4D 和 EPIC-Kitchens 上提升了 30-45% 的相对性能。

**[An Economic Framework for 6-DoF Grasp Detection](an_economic_framework_for_6-dof_grasp_detection.md)**

:   提出EconomicGrasp框架，通过发现密集监督中的歧义问题（ambiguity problem）是性能与资源矛盾的根源，设计经济监督范式（保留所有视角但裁剪角度/深度）和焦点表示模块（交互式抓取头+复合评分），在GraspNet-1Billion上以1/4训练时间、1/8内存成本超越SOTA约3AP。

**[DISCO: Embodied Navigation and Interaction via Differentiable Scene Semantics and Dual-Level Control](disco_embodied_navigation_and_interaction_via_differentiable_scene_semantics_and.md)**

:   提出 DISCO 框架，通过可微分场景语义表示和双层粗-细动作控制，在 ALFRED 基准上实现具身导航与交互的显著性能提升（未见场景成功率超越 SOTA +8.6%，且无需逐步指令）。

**[GraspXL: Generating Grasping Motions for Diverse Objects at Scale](graspxl_generating_grasping_motions_for_diverse_objects_at_scale.md)**

:   提出 GraspXL，一个基于强化学习的抓取动作生成框架，仅用58个物体训练即可泛化到50万+未见物体，同时支持多运动目标（抓取区域、朝向、手腕旋转、手部位置）控制和多种灵巧手平台。

**[Hierarchically Structured Neural Bones for Reconstructing Animatable Objects from Casual Videos](hierarchically_structured_neural_bones_for_reconstructing_animatable_objects_fro.md)**

:   提出层次化神经骨骼（Hierarchical Neural Bones）框架，通过树状结构的骨骼系统以粗到细的方式分解物体运动，从随手拍摄的视频中重建可操控的高质量 3D 模型。

**[LLM as Copilot for Coarse-Grained Vision-and-Language Navigation](llm_as_copilot_for_coarse-grained_vision-and-language_navigation.md)**

:   本文提出VLN-Copilot框架，让视觉语言导航智能体在粗粒度（简短模糊）指令下遇到困惑时主动向LLM求助，LLM作为副驾驶实时生成细粒度导航指导，在两个粗粒度VLN数据集上显著提升导航成功率。

**[Octopus: Embodied Vision-Language Programmer from Environmental Feedback](octopus_embodied_vision-language_programmer_from_environmental_feedback.md)**

:   提出 Octopus，一个具身视觉-语言编程模型，通过生成可执行代码来连接高层规划与底层操控，并引入 Reinforcement Learning with Environmental Feedback (RLEF) 训练方案来提升决策质量。

**[Prioritized Semantic Learning for Zero-shot Instance Navigation](prioritized_semantic_learning_for_zero-shot_instance_navigation.md)**

:   提出Prioritized Semantic Learning (PSL)方法，通过语义增强的Agent架构、优先语义训练策略和语义扩展推理方案，显著提升零样本目标/实例导航中Agent的语义感知能力，在ObjectNav和新提出的InstanceNav任务上实现SOTA。

**[QUAR-VLA: Vision-Language-Action Model for Quadruped Robots](quar-vla_vision-language-action_model_for_quadruped_robots.md)**

:   首次提出四足机器人视觉-语言-动作（QUAR-VLA）范式，构建 259K episode 的多任务数据集 QUARD 和基于预训练多模态大模型的 QUART 模型，实现感知、导航、全身操作等多任务统一控制。

**[ReALFRED: An Embodied Instruction Following Benchmark in Photo-Realistic Environments](realfred_an_embodied_instruction_following_benchmark_in_photo-realistic_environm.md)**

:   提出 ReALFRED 基准，使用 150 个真实世界 3D 扫描的多房间可交互环境替代 ALFRED 的合成单房间场景，提供 30,696 条自由格式语言指令，揭示了现有具身指令跟随方法在真实环境中性能显著下降的问题。

**[See and Think: Embodied Agent in Virtual Environment](see_and_think_embodied_agent_in_virtual_environment.md)**

:   提出 STEVE，一个基于视觉感知、语言指令和代码动作三大组件的 Minecraft 开放世界具身智能体，通过 STEVE-21K 数据集微调 LLaMA-2 并结合视觉编码器和技能数据库，在科技树解锁和方块搜索任务上大幅超越现有方法。

**[SemGrasp: Semantic Grasp Generation via Language Aligned Discretization](semgrasp_semantic_grasp_generation_via_language_aligned_discretization.md)**

:   提出SemGrasp方法，设计层次化VQ-VAE将抓取姿态离散为"方向-方式-精修"三个语义token，然后微调多模态大语言模型(MLLM)在统一语义空间中融合物体、抓取与语言，实现根据自然语言指令生成物理合理且语义一致的人类抓取姿态。
