<!-- 由 src/gen_blog_index.py 自动生成 -->
# 🎬 视频理解

**📹 ICCV2025** · 共 **30** 篇

**[4D-Bench: Benchmarking Multi-Modal Large Language Models for 4D Object Understanding](4d-bench_benchmarking_multi-modal_large_language_models_for_4d_object_understand.md)**

:   4D-Bench 是首个评估多模态大语言模型（MLLM）4D 物体理解能力的基准，包含 4D 物体问答和描述两大任务，揭示了即使 SOTA GPT-4o 也仅达 63% 准确率（人类基线 91%），暴露了当前 MLLM 在多视角时序推理上的显著不足。

**[4D-Bench: Benchmarking Multi-modal Large Language Models for 4D Object Understanding](4dbench_benchmarking_multimodal_large_language_models_for_4d.md)**

:   提出 4D-Bench，首个评估多模态大语言模型对4D物体（具有时间演化的3D物体）理解能力的基准，包含4D物体问答（751 QA对）和4D物体描述（580物体×5标注）两大任务，发现即使SOTA的GPT-4o也仅达63%准确率（人类91%），揭示了MLLM在多视角时空理解上的巨大差距。

**[Adaptive Hyper-Graph Convolution Network for Skeleton-Based Human Action Recognition](adaptive_hyper-graph_convolution_network_for_skeleton-based_human_action_recogni.md)**

:   提出 Hyper-GCN，通过**自适应非均匀超图**替代传统二元图来建模骨骼拓扑，并引入**虚拟超关节**（hyper joints）创建虚拟连接，使多关节协同关系得以直接建模，在 NTU-60/120 和 NW-UCLA 上以最轻量的 GCN 设计实现 SOTA（base 版仅 1.1M 参数、1.63 GFLOPs）。

**[AIM: Adaptive Inference of Multi-Modal LLMs via Token Merging and Pruning](aim_adaptive_inference_of_multi-modal_llms_via_token_merging_and_pruning.md)**

:   提出一种无需训练的自适应推理方法，通过 LLM 前基于嵌入相似度的迭代式 token 合并 + LLM 层内基于 PageRank 多模态重要性的渐进式 token 剪枝，实现多模态 LLM 在 40 倍 FLOPs 减少范围内的灵活精度-效率权衡，在视频和图像理解任务上均取得优异表现。

**[Aligning Effective Tokens with Video Anomaly in Large Language Models](aligning_effective_tokens_with_video_anomaly_in_large_language_models.md)**

:   提出VA-GPT，通过空间有效Token选择（SETS）和时间有效Token生成（TETG）两个模块，在MLLM中高效对齐与视频异常相关的关键Token，实现对异常事件的精准检测、描述和时间定位。

**[AllTracker: Efficient Dense Point Tracking at High Resolution](alltracker_efficient_dense_point_tracking_at_high_resolution.md)**

:   提出AllTracker，将点跟踪重新表述为多帧长程光流问题，在低分辨率网格上通过2D卷积+像素对齐时序注意力迭代优化对应估计再上采样，仅16M参数即实现SOTA准确率和高分辨率（768×1024）全像素密集跟踪，跟踪速度接近光流方法。

**[An Empirical Study of Autoregressive Pre-training from Videos](an_empirical_study_of_autoregressive_pre-training_from_videos.md)**

:   系统性地研究了从视频进行自回归预训练的方法（称为Toto），在超过1万亿视觉token上训练因果Transformer，发现尽管归纳偏置极少，自回归预训练在图像识别、视频分类、目标跟踪和机器人操控等多个下游任务上均具有竞争力，且展现出类似语言模型的缩放规律（但速率较慢）。

**[Attention to Trajectory: Trajectory-Aware Open-Vocabulary Tracking](attention_to_trajectory_trajectory-aware_open-vocabulary_tracking.md)**

:   本文提出TRACT，一种利用轨迹级信息增强开放词汇多目标跟踪（OV-MOT）的方法，通过轨迹一致性强化（TCR）改善关联、通过轨迹特征聚合（TFA）和轨迹语义丰富（TSE）改善分类，在OV-TAO基准上显著提升了跟踪性能，尤其是分类准确率。

**[Beyond Label Semantics: Language-Guided Action Anatomy for Few-shot Action Recognition](beyond_label_semantics_language-guided_action_anatomy_for_few-shot_action_recogn.md)**

:   提出 Language-Guided Action Anatomy (LGA) 框架，利用大语言模型将动作标签解剖为原子级动作描述（主体-动作-对象三要素），同时在视频端通过聚类分割将帧序列划分为对应的原子动作阶段，在原子级别进行多模态融合和匹配，显著提升小样本动作识别性能。

**[Beyond the Frame: Generating 360° Panoramic Videos from Perspective Videos](beyond_the_frame_generating_360deg_panoramic_videos_from_perspective_videos.md)**

:   提出 Argus 模型，首次实现从普通透视视频生成完整 360° 全景视频，通过相机运动模拟、视角对齐帧校准和混合解码三大几何-运动感知技术，在基于扩散模型的框架上让生成的全景视频具备空间一致性和时序连贯性。

**[BlinkTrack: Feature Tracking over 80 FPS via Events and Images](blinktrack_feature_tracking_over_80_fps_via_events_and_images.md)**

:   提出 BlinkTrack，将可微卡尔曼滤波引入学习框架，有效解决事件相机和传统相机异步数据的关联与不确定性感知融合，实现超过 80 FPS 的高帧率特征跟踪，并在遮挡场景中显著优于现有方法。

**[Breaking the Encoder Barrier for Seamless Video-Language Understanding](breaking_the_encoder_barrier_for_seamless_video-language_understanding.md)**

:   提出 ELVA，首个无编码器（encoder-free）的视频大语言模型，通过层级 token 合并、视频引导监督和混合分辨率推理机制，仅用 7M 公开视频-文本对数据即可达到与有编码器架构相当的性能，同时将 FLOPs 降低 95%、推理延迟降低 92%。

**[D3: Training-Free AI-Generated Video Detection Using Second-Order Features](d3_training-free_ai-generated_video_detection_using_second-order_features.md)**

:   本文从牛顿力学的二阶控制系统出发，发现真实视频和 AI 生成视频在二阶时序特征（"加速度"）上存在本质差异——真实视频波动大而生成视频平坦，据此提出 D3，一种完全免训练的 AI 生成视频检测方法，仅需计算帧间特征的二阶差分标准差即可判别，在 40 个测试子集上达到 SOTA。

**[DACoN: DINO for Anime Paint Bucket Colorization with Any Number of Reference Images](dacon_dino_for_anime_paint_bucket_colorization_with_any_number_of_reference_imag.md)**

:   提出DACoN，利用DINOv2基础模型的语义特征与U-Net的高分辨率空间特征融合，实现支持任意数量参考图像的动画线稿自动上色，在关键帧和连续帧上色任务中均超越现有方法。

**[DeSPITE: Exploring Contrastive Deep Skeleton-PointCloud-IMU-Text Embeddings for Action Recognition](despite_exploring_contrastive_deep_skeleton-pointcloud-imu-text_embeddings_for_a.md)**

:   DeSPITE 提出了一种隐私保护的多模态对比预训练模型，将 LiDAR 点云、骨架姿态、IMU 和文本四种模态对齐到统一嵌入空间，实现了跨模态匹配、检索以及人体活动识别的预训练范式。

**[DisTime: Distribution-based Time Representation for Video Large Language Models](distime_distribution-based_time_representation_for_video_large_language_models.md)**

:   提出DisTime框架，通过一个可学习的时间token和基于分布的时间解码器，在Video-LLM中实现连续时间表示，配合大规模自动标注数据集InternVid-TG（125万事件），在时刻检索、密集视频描述、Grounded-VQA三类时间敏感任务上达到SOTA。

**[DOLLAR: Few-Step Video Generation via Distillation and Latent Reward Optimization](dollar_fewstep_video_generation_via_distillation_and_latent.md)**

:   结合变分分数蒸馏（VSD）和一致性蒸馏实现few-step视频生成，同时提出潜空间奖励模型微调方法进一步优化生成质量，4步生成的10秒视频（128帧@12FPS）在VBench上达82.57分超越teacher模型和Gen-3/Kling等基线，1步蒸馏实现278.6倍加速。

**[DreamRelation: Relation-Centric Video Customization](dreamrelation_relation-centric_video_customization.md)**

:   提出 DreamRelation，首个关系中心的视频定制方法，通过 Relation LoRA Triplet + Hybrid Mask Training 实现关系与外观的解耦，并通过时空关系对比损失增强关系动态学习，使动物能模仿人类交互。

**[EgoAdapt: Adaptive Multisensory Distillation and Policy Learning for Efficient Egocentric Perception](egoadapt_adaptive_multisensory_distillation_and_policy_learning_for_efficient_eg.md)**

:   提出 EgoAdapt 框架，将跨模态蒸馏与策略学习联合训练，自适应选择最优模态组合，在自我中心感知任务中实现最高 89% GMACs 缩减的同时保持与 SOTA 持平甚至更优的性能。

**[EMoTive: Event-Guided Trajectory Modeling for 3D Motion Estimation](emotive_event-guided_trajectory_modeling_for_3d_motion_estimation.md)**

:   本文提出 EMoTive，一个基于事件相机的 3D 运动估计框架，通过 Event Kymograph 编码精细时序演化信息，并使用事件密度引导的非均匀 NURBS 参数曲线建模时空轨迹，从轨迹中导出光流和深度运动场，在自建 CarlaEvent3D 数据集和真实世界基准上取得 SOTA 性能。

**[Flow4Agent: Long-form Video Understanding via Motion Prior from Optical Flow](flow4agent_long-form_video_understanding_via_motion_prior_from_optical_flow.md)**

:   Flow4Agent 首次将光流运动先验引入 LLM-based 视频理解，通过时域粒度优化（TGO）利用粗粒度光流聚类视频事件并用语义先验过滤冗余场景，通过运动 Token 剪枝（MTP）利用细粒度光流去除帧内静态冗余 token，在 VideoMME/MLVU/LongVideoBench 等长视频基准上取得领先表现。

**[FlowSeek: Optical Flow Made Easier with Depth Foundation Models and Motion Bases](flowseek_optical_flow_made_easier_with_depth_foundation_models_and_motion_bases.md)**

:   FlowSeek 将深度基础模型（Depth Anything V2）的先验知识和经典的低维运动参数化（motion bases）融入光流网络，在仅使用单张消费级 GPU 训练的条件下即可实现 SOTA 的跨数据集泛化性能。

**[Learning to Generalize Without Bias for Open-Vocabulary Action Recognition](learning_to_generalize_without_bias_for_open-vocabulary_action_recognition.md)**

:   本文提出 Open-MeDe，一个基于元学习的开放词汇动作识别框架，通过跨批次元优化模拟"已知到开放"的泛化任务，并结合高斯自集成稳定化策略，在不依赖 CLIP 正则化的情况下同时提升上下文内和上下文外场景的泛化能力。

**[ResidualViT for Efficient Temporally Dense Video Encoding](residualvit_for_efficient_temporally_dense_video_encoding.md)**

:   本文提出 ResidualViT，通过类比视频压缩中的 I帧/P帧 策略，交替使用完整 ViT 和轻量残差 ViT 编码视频帧，在保持接近原始 CLIP 精度的同时，实现最高 60% 的计算成本降低和 2.5 倍推理加速。

**[STiV: Scalable Text and Image Conditioned Video Generation](stiv_scalable_text_and_image_conditioned_video_generation.md)**

:   本文提出 STIV，一个基于 Diffusion Transformer 的统一文本-图像条件视频生成框架，通过帧替换策略整合图像条件并引入联合图像-文本 classifier-free guidance，在单一模型中同时实现 T2V 和 TI2V 生成，8.7B 参数模型在 VBench T2V 和 I2V 上分别达到 83.1 和 90.1 的 SOTA 成绩。

**[Temporal Unlearnable Examples: Preventing Personal Video Data from Unauthorized Exploitation](temporal_unlearnable_examples_preventing_personal_video_data_from_unauthorized_e.md)**

:   本文首次研究防止视频数据被深度跟踪器未授权使用的问题，提出基于 DiT 的生成式框架生成时序不可学习样本（TUE），通过时间对比损失使跟踪器依赖扰动噪声进行时序匹配而非学习真实数据结构，实现了跨模型、跨数据集和跨任务的强可迁移性。

**[Towards Video Thinking Test: A Holistic Benchmark for Advanced Video Reasoning and Understanding](towards_video_thinking_test_a_holistic_benchmark_for_advanced_video_reasoning_an.md)**

:   提出 Video Thinking Test (Video-TT)，一个评估视频大语言模型正确性和鲁棒性的基准，包含 1000 个 YouTube Shorts 视频和 5000 个问题，通过视觉/叙事复杂性因子和自然对抗问题揭示了当前最强模型（GPT-4o 36.6%）与人类（84.3%）之间的巨大差距。

**[UMDATrack: Unified Multi-Domain Adaptive Tracking Under Adverse Weather Conditions](umdatrack_unified_multi-domain_adaptive_tracking_under_adverse_weather_condition.md)**

:   UMDATrack 提出了首个统一多域自适应跟踪框架，利用文本引导扩散模型合成少量（<2% 帧）多天气条件无标注视频，通过域定制适配器（DCA）高效迁移目标表征到不同天气域，并引入基于最优传输的目标感知置信度对齐（TCA）增强跨域定位一致性，在夜间/雾天/雨天等场景中大幅超越现有 SOTA 跟踪器。

**[VACE: All-in-One Video Creation and Editing](vace_allinone_video_creation_and_editing.md)**

:   提出VACE统一视频生成和编辑框架，通过Video Condition Unit（VCU）将参考图→视频生成、视频→视频编辑、mask视频编辑等多种任务的输入统一为标准接口，配合Context Adapter注入时空条件信息，单一模型在各子任务上达到专用模型水平并支持灵活的任务组合。

**[VMBench: A Benchmark for Perception-Aligned Video Motion Generation](vmbench_a_benchmark_for_perception-aligned_video_motion_generation.md)**

:   提出 VMBench——首个面向视频运动质量评估的综合基准，包含五维感知对齐运动指标（PMM）和元信息引导的运动提示生成框架（MMPG），覆盖 969 类运动类型，在 Spearman 相关系数上比现有方法平均提升 35.3%。
