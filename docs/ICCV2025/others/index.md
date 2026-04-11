<!-- 由 src/gen_blog_index.py 自动生成 -->
# 📂 其他

**📹 ICCV2025** · 共 **23** 篇

**[3DSRBench: A Comprehensive 3D Spatial Reasoning Benchmark](3dsrbench_a_comprehensive_3d_spatial_reasoning_benchmark.md)**

:   提出首个全面的3D空间推理基准3DSRBench，包含2,772个人工标注的VQA对（12种问题类型），通过平衡数据分布和新型FlipEval策略实现鲁棒评估，揭示SOTA LMM（包括GPT-4o、Gemini）在3D空间推理上远落后于人类水平（≈52% vs 95.7%），且在非常规视角下性能显著退化。

**[A Hidden Stumbling Block in Generalized Category Discovery: Distracted Attention](a_hidden_stumbling_block_in_generalized_category_discovery_d.md)**

:   发现GCD中未标注数据（尤其是未知类别）的ViT注意力会分散到背景区域（distracted attention），提出Attention Focusing（AF）模块通过多尺度token重要性度量+自适应剪枝来纠正注意力，作为即插即用模块在SimGCD上最高带来15.4%的性能提升。

**[A Hyperdimensional One Place Signature to Represent Them All: Stackable Descriptors For Visual Place Recognition](a_hyperdimensional_one_place_signature_to_represent_them_all_stackable_descripto.md)**

:   本文提出 HOPS（Hyperdimensional One Place Signatures），利用超维计算（HDC）框架将同一地点在不同环境条件下采集的多个参考描述子融合为统一表示，在不增加计算量和存储开销的前提下，大幅提升视觉场所识别（VPR）的鲁棒性与召回率。

**[A Linear N-Point Solver for Structure and Motion from Asynchronous Tracks](a_linear_n-point_solver_for_structure_and_motion_from_asynchronous_tracks.md)**

:   本文提出了一种统一的线性 N-point 求解器，能够从具有任意时间戳的 2D 点对应中恢复相机线速度和 3D 点结构，适用于全局快门、滚动快门和事件相机等多种传感器模式。

**[A Real-world Display Inverse Rendering Dataset](a_real-world_display_inverse_rendering_dataset.md)**

:   本文构建了首个基于LCD显示器-相机系统的真实世界逆渲染数据集，包含16个不同材质物体在OLAT照明模式下的立体偏振图像及高精度几何真值，并提出了一个简单有效的显示器逆渲染基线方法，超越了现有逆渲染方法。

**[A Real-world Display Inverse Rendering Dataset](a_realworld_display_inverse_rendering_dataset.md)**

:   构建了首个基于LCD显示器-相机系统的真实世界逆渲染数据集，包含16个物体的OLAT（逐像素点亮）采集图像、偏振信息和GT几何，并提出简单有效的基线方法（基于Cook-Torrance BRDF的可微渲染优化），在150秒内超越现有逆渲染方法。

**[ACE-G: Improving Generalization of Scene Coordinate Regression Through Query Pre-Training](aceg_improving_generalization_of_scene_coordinate_regression.md)**

:   将场景坐标回归器拆分为「场景无关的Transformer」和「场景特定的map code」，通过在数万场景上进行交替的mapping/query预训练，显著提升SCR方法在光照、视角变化下的泛化能力，同时保持轻量化的计算开销。

**[AdaptiveAE: An Adaptive Exposure Strategy for HDR Capturing in Dynamic Scenes](adaptiveae_an_adaptive_exposure_strategy_for_hdr_capturing_i.md)**

:   本文提出AdaptiveAE，利用深度强化学习将HDR曝光包围拍摄建模为马尔可夫决策过程（MDP），同时优化ISO和快门速度的组合，在用户定义的时间预算内自适应地为动态场景选择最优曝光参数，在HDRV数据集上达到PSNR 39.70，比之前最好的方法Hasinoff et al. (37.59) 高出2.1 dB。

**[Adversarial Robust Memory-Based Continual Learner](adversarial_robust_memory-based_continual_learner.md)**

:   揭示持续学习与对抗训练结合时的双重挑战（加速遗忘 + 梯度混淆），提出抗遗忘 Logit 校准（AFLC）和鲁棒感知经验回放（RAER）两个即插即用模块，在 Split-CIFAR10/100 和 Split-Tiny-ImageNet 上有效提升对抗鲁棒性达 8.13%。

**[AFUNet: Cross-Iterative Alignment-Fusion Synergy for HDR Reconstruction via Deep Unfolding Paradigm](afunet_crossiterative_alignmentfusion_synergy_for_hdr_recons.md)**

:   将多曝光HDR重建从MAP估计视角建模，通过空间对应先验将问题分解为对齐和融合两个交替子问题，再展开为端到端可训练的AFUNet（含SAM空间对齐+CFM通道融合+DCM数据一致性模块），在三个HDR基准上取得SOTA，PSNR-μ达44.91dB（Kalantari数据集）。

**[Auto-Regressively Generating Multi-View Consistent Images (MV-AR)](autoregressively_generating_multiview_consistent_images.md)**

:   首次将自回归（AR）模型引入多视角图像生成任务，通过逐视角生成利用所有前序视角信息来增强远距离视角间的一致性，同时设计了统一的多模态条件注入架构和Shuffle Views数据增强策略，使单一模型可同时处理文本/图像/几何形状条件。

**[C4D: 4D Made from 3D through Dual Correspondences](c4d_4d_made_from_3d_through_dual_correspondences.md)**

:   提出C4D框架，通过在DUSt3R的3D pointmap预测基础上联合捕获双重时序对应(短时光流+动态感知长时点跟踪DynPT)，生成运动掩码分离动静区域，并引入相机运动对齐/相机轨迹平滑/点轨迹平滑三个优化目标，将现有3D重建范式升级为完整4D重建(逐帧点云+相机参数+2D/3D轨迹)，在深度/位姿/跟踪多个下游任务上达competitive性能。

**[ConstStyle: Robust Domain Generalization with Unified Style Transformation](conststyle_robust_domain_generalization_with_unified_style_transformation.md)**

:   提出ConstStyle框架，通过构建一个理论驱动的"统一域"（Unified Domain），在训练时将所有样本风格对齐到该统一域，测试时将未见域样本部分投影到统一域，有效缩小域间差距并提升泛化性能。

**[Dataset Ownership Verification for Pre-trained Masked Models](dataset_ownership_verification_for_pre-trained_masked_models.md)**

:   DOV4MM 提出了首个针对掩码预训练模型的数据集所有权验证方法，通过比较"见过"与"未见过"样本在嵌入空间中遮掩信息重构难度的差异，利用配对 t 检验判断黑盒模型是否使用了特定数据集进行预训练，在 10 种掩码图像模型和 4 种掩码语言模型上均实现 p 值远低于 0.05 的准确验证。

**[Despite Exploring Contrastive Deep Skeletonpointcloudimutext](despite_exploring_contrastive_deep_skeletonpointcloudimutext.md)**

:   提出 DeSPITE，一个将 LiDAR 点云、骨架姿态、IMU 信号和文本四种模态对齐到联合嵌入空间的对比学习框架，首次以 LiDAR（而非 RGB）作为核心视觉模态，实现了跨模态匹配/检索等此前不可能的任务，同时作为有效的 HAR 预训练策略在 MSR-Action3D 和 HMPEAR 上取得 SOTA。

**[Doodle Your Keypoints: Sketch-Based Few-Shot Keypoint Detection](doodle_your_keypoints_sketch-based_few-shot_keypoint_detection.md)**

:   提出首个基于草图的跨模态少样本关键点检测框架，利用原型网络、网格定位器、原型域适应和去风格化网络，仅需少量带标注草图即可在真实照片中检测新类别的新关键点。

**[Forgetting Through Transforming: Enabling Federated Unlearning via Class-Aware Representation Transformation](forgetting_through_transforming_enabling_federated_unlearning_via_class-aware_re.md)**

:   提出 FUCRT 方法，通过类感知表征变换实现联邦遗忘：将遗忘类的表征“变换”到语义最近的保留类，而非直接消除，配合双重对比学习对齐跨客户端的变换一致性，在四个数据集上实现 100% 遗忘保障的同时保持甚至提升剩余类性能。

**[IAP: Invisible Adversarial Patch Attack through Perceptibility-Aware Localization](iap_invisible_adversarial_patch_attack_through_perceptibility-aware_localization.md)**

:   提出 IAP 框架，通过**感知感知（perceptibility-aware）的贴片定位**和**保色梯度更新**，首次实现在目标攻击场景下生成真正不可见的对抗补丁，同时能绕过多种 SOTA 补丁防御方法。

**[LaCoOT: Layer Collapse through Optimal Transport](lacoot_layer_collapse_through_optimal_transport.md)**

:   提出 LaCoOT，一种基于最优传输的正则化策略，通过最小化网络内部中间特征分布之间的 Max-Sliced Wasserstein 距离，使得训练后可以直接移除整个网络层，在保持性能的同时显著减少模型深度和推理时间。

**[Omni-DC: Highly Robust Depth Completion with Multiresolution Depth Integration](omni-dc_highly_robust_depth_completion_with_multiresolution_depth_integration.md)**

:   提出 OMNI-DC，通过多分辨率深度积分器（Multi-res DDI）、Laplacian 损失和尺度归一化技术，构建了一个能够零样本泛化到不同数据集和稀疏深度模式的高鲁棒深度补全模型。

**[Thermal Polarimetric Multi-view Stereo](thermal_polarimetric_multi-view_stereo.md)**

:   提出利用热偏振（长波红外偏振）线索进行精细三维形状重建的方法，理论证明 LWIR 偏振观测不受光照环境和材质光学属性的影响，从而实现对透明、半透明和异质材料物体的高精度三维重建，显著优于可见光偏振方法。

**[Toward Material-Agnostic System Identification from Videos](toward_material-agnostic_system_identification_from_videos.md)**

:   提出 MASIV，首个无需预定义材质先验的视觉系统辨识框架：采用可学习的神经本构模型替代手工设计的弹性/塑性方程，通过重建连续体粒子轨迹提供时间密集的几何约束，从多视角视频中推断物体的内在动力学特性。

**[You Share Beliefs, I Adapt: Progressive Heterogeneous Collaborative Perception](you_share_beliefs_i_adapt_progressive_heterogeneous_collaborative_perception.md)**

:   提出PHCP框架，首次在推理阶段解决异构协同感知的域差距问题——通过agent的伪标签做few-shot无监督域适应，自训练适配器对齐特征空间，无需联合训练即在OPV2V上仅用少量无标注数据达到接近SOTA(HEAL)的性能。
