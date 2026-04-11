<!-- 由 src/gen_blog_index.py 自动生成 -->
# 🤖 机器人/具身智能

**📹 ICCV2025** · 共 **10** 篇

**[Adaptive Articulated Object Manipulation On The Fly with Foundation Model Reasoning and Part Grounding](adaptive_articulated_object_manipulation_on_the_fly_with_foundation_model_reason.md)**

:   本文提出 AdaRPG 框架，利用基础视觉-语言模型对铰接物体进行零件级分割和可操作性推理，并借助 GPT-4o 生成高层控制代码以自适应调度原子操作技能，在仿真和真实环境中实现了跨类别零样本泛化操作。

**[AnyBimanual: Transferring Unimanual Policy for General Bimanual Manipulation](anybimanual_transferring_unimanual_policy_for_general_bimanual_manipulation.md)**

:   提出 AnyBimanual，一个即插即用的框架，通过技能管理器和视觉对齐器将预训练的单臂操控策略迁移到通用双臂操控场景，在仅有少量双臂示范的情况下实现显著的多任务泛化能力。

**[Beyond Losses Reweighting: Empowering Multi-Task Learning via the Generalization Perspective](beyond_losses_reweighting_empowering_multi-task_learning_via_the_generalization_.md)**

:   从泛化角度出发，将锐度感知最小化（SAM）引入多任务学习，通过分解每个任务的 SAM 梯度为"低损失方向"和"平坦方向"并分别聚合，减少梯度冲突并引导模型进入跨任务共同平坦低损失区域。

**[Bridging Domain Generalization to Multimodal Domain Generalization via Unified Representations](bridging_domain_generalization_to_multimodal_domain_generalization_via_unified_r.md)**

:   提出URMMDG框架，通过监督对比学习构建跨模态统一表示空间，并利用互信息最小化解耦类别通用信息与模态/域特定信息，将传统单模态域泛化方法（Mixup、JiGen、IBN-Net）有效迁移到多模态域泛化场景，在EPIC-Kitchens和HAC基准上取得SOTA。

**[Certifiably Optimal Anisotropic Rotation Averaging](certifiably_optimal_anisotropic_rotation_averaging.md)**

:   提出了一种新的SDP松弛方法，通过强制解落在SO(3)的凸包conv(SO(3))内，首次实现了各向异性代价下的可证明全局最优旋转平均，解决了传统O(3)松弛在各向异性场景下完全失效的问题。

**[CombatVLA: An Efficient Vision-Language-Action Model for Combat Tasks in 3D Action Role-Playing Games](combatvla_an_efficient_vision-language-action_model_for_combat_tasks_in_3d_actio.md)**

:   提出CombatVLA，一个针对3D动作角色扮演游戏战斗任务的高效3B参数VLA模型，通过Action-of-Thought数据格式和截断推理策略，实现比现有VLM游戏框架快50倍的推理速度，且战斗成功率超越人类玩家。

**[EvolvingGrasp: Evolutionary Grasp Generation via Efficient Preference Alignment](evolvinggrasp_evolutionary_grasp_generation_via_efficient_preference_alignment.md)**

:   提出 EvolvingGrasp，通过 Handpose-wise Preference Optimization (HPO) 和 Physics-Aware Consistency Model (PCM) 实现灵巧抓取姿态的高效进化式生成与人类偏好对齐，在四个基准数据集上取得 SOTA，并实现 30 倍加速。

**[NavMorph: A Self-Evolving World Model for Vision-and-Language Navigation in Continuous Environments](navmorph_a_self-evolving_world_model_for_vision-and-language_navigation_in_conti.md)**

:   提出 NavMorph，一种基于 RSSM 的**自进化世界模型**，通过 World-aware Navigator 和 Foresight Action Planner 在隐空间建模连续环境动态，并引入上下文进化记忆（CEM）实现在线测试时的快速适应。

**[SITE: towards Spatial Intelligence Thorough Evaluation](site_towards_spatial_intelligence_thorough_evaluation.md)**

:   本文提出 SITE，一个基于认知科学三重分类体系的空间智能综合基准，涵盖 8,068 个多选 VQA 任务（覆盖 31 个数据集、图像+视频），评估结果显示当前最强 VLM（GPT-4o）在整体空间推理上仍落后人类专家约 32%，且 VLM 的空间智能与机器人操控任务的成功率呈高度正相关（Pearson $r=0.902$）。

**[VQ-VLA: Improving Vision-Language-Action Models via Scaling Vector-Quantized Action Tokenizers](vq-vla_improving_vision-language-action_models_via_scaling_vector-quantized_acti.md)**

:   本文提出基于卷积残差 VQ-VAE 的动作 tokenizer，在比先前方法多 100 倍的训练数据（含大量合成数据）上训练后可零样本迁移到各种下游 VLA 任务，在真实机器人上将长时域任务成功率提升最高 30%，推理速度提升近 3 倍。
