<!-- 由 src/gen_blog_index.py 自动生成 -->
# 🚗 自动驾驶

**📹 ICCV2025** · 共 **43** 篇

**[3D Gaussian Splatting Driven Multi-View Robust Physical Adversarial Camouflage Generation](3d_gaussian_splatting_driven_multi-view_robust_physical_adversarial_camouflage_g.md)**

:   提出PGA，首个基于3DGS的物理对抗攻击框架，通过快速准确重建目标+解决Gaussians互/自遮挡问题+min-max背景对抗优化策略，生成跨视角鲁棒的物理对抗迷彩，在数字和物理域均超越SOTA方法。

**[3D Gaussian Splatting Driven Multi-View Robust Physical Adversarial Camouflage Generation](3d_gaussian_splatting_driven_multiview_robust_physical_adver.md)**

:   提出首个基于3D高斯体（3DGS）的物理对抗攻击框架PGA，通过解决高斯体的互遮挡和自遮挡问题保证跨视角一致性，并设计min-max优化策略过滤非鲁棒对抗特征，在数字域和物理域均大幅超越SOTA方法。

**[3DRealCar: An In-the-wild RGB-D Car Dataset with 360-degree Views](3drealcar_an_in-the-wild_rgb-d_car_dataset_with_360-degree_views.md)**

:   本文提出首个大规模真实3D车辆数据集3DRealCar，包含2500辆来自100+品牌的真实车辆，每辆车约200张高分辨率360度RGB-D视图，覆盖反光/标准/暗光三种光照条件，并提供13类车辆解析标注，支持3D重建、检测、生成等多种任务。

**[3DRealCar: An In-the-wild RGB-D Car Dataset with 360-degree Views](3drealcar_an_inthewild_rgbd_car_dataset_with_360degree_views.md)**

:   提出首个大规模3D真实汽车数据集3DRealCar，包含2,500辆真实汽车的高分辨率（1920×1440）360度RGB-D扫描（平均每辆200张视角），覆盖100+品牌和三种光照条件（标准/高反光/暗光），提供点云、解析图等丰富标注，并基准测试了多种3D重建方法，揭示了反光和暗光条件下的重建挑战。

**[4DSegStreamer: Streaming 4D Panoptic Segmentation via Dual Threads](4dsegstreamer_streaming_4d_panoptic_segmentation_via_dual_th.md)**

:   提出4DSegStreamer，一种通用的**双线程**流式4D全景分割框架——预测线程维护几何和运动记忆并预测未来动态，推理线程通过自我位姿对齐和逆向前向流迭代实现对新到帧的实时查询，可即插即用地集成到现有3D/4D分割方法中，在SemanticKITTI上sLSTQ比PTv3高7.7-15.2%，在高FPS场景下性能鲁棒性远超现有方法。

**[4DSegStreamer: Streaming 4D Panoptic Segmentation via Dual Threads](4dsegstreamer_streaming_4d_panoptic_segmentation_via_dual_threads.md)**

:   提出4DSegStreamer，一种基于双线程系统（预测线程+推理线程）的流式4D全景分割框架，通过几何与运动记忆维护、自车位姿预测和逆向前向光流迭代实现实时高质量4D全景分割。

**[6DOPE-GS: Online 6D Object Pose Estimation using Gaussian Splatting](6dope-gs_online_6d_object_pose_estimation_using_gaussian_splatting.md)**

:   提出6DOPE-GS，一种利用2D高斯溅射（2DGS）联合优化6D物体位姿和3D重建的model-free在线追踪方法，通过动态关键帧选择和基于透明度百分位的密度控制实现5倍加速，同时保持SOTA精度。

**[6DOPE-GS: Online 6D Object Pose Estimation using Gaussian Splatting](6dopegs_online_6d_object_pose_estimation_using_gaussian_spla.md)**

:   利用2D Gaussian Splatting的高效可微渲染能力，提出一种无需CAD模型的在线6D物体位姿估计与跟踪方法，通过联合优化高斯物体场和关键帧位姿，实现比BundleSDF快约5倍的速度同时保持可比精度。

**[A Constrained Optimization Approach for Gaussian Splatting from Coarsely-posed Images and Noisy LiDAR Point Clouds](a_constrained_optimization_approach_for_gaussian_splatting_f.md)**

:   提出一种**无需SfM**的约束优化方法，同时估计相机位姿和做3DGS重建——将相机位姿分解为相机-设备中心和设备中心-世界两步优化，设计参数敏感性条件约束和几何约束，从粗糙位姿和噪声LiDAR点云直接重建3D场景，显著优于COLMAP辅助的3DGS基线。

**[ACAM-KD: Adaptive and Cooperative Attention Masking for Knowledge Distillation](acam-kd_adaptive_and_cooperative_attention_masking_for_knowledge_distillation.md)**

:   提出 ACAM-KD，一种自适应学生-教师协作注意力掩码知识蒸馏方法，通过跨注意力特征融合（STCA-FF）和自适应空间-通道掩码（ASCM）动态调整蒸馏焦点，在 COCO 检测上超越 SOTA 最高 1.4 mAP，在 Cityscapes 分割上提升 3.09 mIoU。

**[AD-GS: Object-Aware B-Spline Gaussian Splatting for Self-Supervised Autonomous Driving](ad-gs_object-aware_b-spline_gaussian_splatting_for_self-supervised_autonomous_dr.md)**

:   本文提出 AD-GS，一种基于 3D Gaussian Splatting 的自监督自动驾驶场景渲染框架，核心创新是将可学习 B-spline 曲线与三角函数结合进行局部-全局运动建模，并通过简化的二值伪分割实现鲁棒的场景分解，在不依赖人工 3D 标注的条件下大幅超越现有自监督方法。

**[AdaDrive: Self-Adaptive Slow-Fast System for Language-Grounded Autonomous Driving](adadrive_self-adaptive_slow-fast_system_for_language-grounded_autonomous_driving.md)**

:   AdaDrive提出了首个自适应慢-快架构的LLM增强自动驾驶框架，通过两个自适应连接器动态决定"何时激活LLM"（Connector-W）和"LLM贡献多少"（Connector-H），在语言引导驾驶基准上实现了SOTA性能（驾驶分数80.9%），同时将推理延迟降低至189ms、显存降至6.79GB。

**[Adaptive Dual Uncertainty Optimization: Boosting Monocular 3D Object Detection under Test-Time Shifts](adaptive_dual_uncertainty_optimization_boosting_monocular_3d.md)**

:   提出DUO（Dual Uncertainty Optimization），首个面向单目3D检测（M3OD）的测试时自适应框架，通过共轭焦点损失减少语义不确定性和法线场一致性约束减少几何不确定性，形成互补优化闭环。

**[Adaptive Dual Uncertainty Optimization: Boosting Monocular 3D Object Detection under Test-Time Shifts](adaptive_dual_uncertainty_optimization_boosting_monocular_3d_object_detection_un.md)**

:   提出 DUO（Dual Uncertainty Optimization），首个联合最小化语义不确定性和几何不确定性的测试时自适应框架，通过共轭焦点损失和法向场约束实现鲁棒的单目3D目标检测。

**[AGO: Adaptive Grounding for Open World 3D Occupancy Prediction](ago_adaptive_grounding_for_open_world_3d_occupancy_predictio.md)**

:   提出AGO框架，通过噪声增强的接地训练(grounding training)处理已知类别 + 模态适配器的自适应对齐处理未知类别，并用基于信息熵的开放世界识别器在推理时动态选择最佳特征，在Occ3D-nuScenes自监督基准上超越VEON 4.09 mIoU，同时具备开放世界零样本/少样本迁移能力。

**[Causal-Entity Reflected Egocentric Traffic Accident Video Synthesis](causal-entity_reflected_egocentric_traffic_accident_video_synthesis.md)**

:   提出 Causal-VidSyn 扩散模型，通过事故原因问答（ArA）和驾驶员注视引导的因果 token 选择（CTS&CTG）机制，实现对自车视角交通事故视频中因果实体的精确定位与生成，同时构建了最大规模驾驶员注视数据集 Drive-Gaze（154 万帧）。

**[CCL-LGS: Contrastive Codebook Learning for 3D Language Gaussian Splatting](ccl-lgs_contrastive_codebook_learning_for_3d_language_gaussian_splatting.md)**

:   提出CCL-LGS框架，通过零样本跟踪器实现跨视角掩码关联，并利用对比码本学习（CCL）模块蒸馏出类内紧凑、类间可区分的语义特征，从而解决基于2D先验的3D语义场重建中因遮挡、模糊和视角变化导致的跨视角语义不一致问题。

**[CoLMDriver: LLM-based Negotiation Benefits Cooperative Autonomous Driving](colmdriver_llm-based_negotiation_benefits_cooperative_autonomous_driving.md)**

:   首个全流程 LLM 驱动的协作驾驶系统，通过 Actor-Critic 范式的语言协商模块和意图引导的轨迹生成器，在多种 V2V 交互场景中实现比现有方法高 11% 的成功率。

**[Controllable 3D Outdoor Scene Generation via Scene Graphs](controllable_3d_outdoor_scene_generation_via_scene_graphs.md)**

:   首次提出以场景图（Scene Graph）作为控制信号生成大规模3D室外场景的方法——通过GNN将稀疏场景图编码为BEV嵌入图，再经2D→3D级联离散扩散模型生成语义3D场景，并配套交互系统让用户直接编辑场景图来控制生成。

**[CoopTrack: Exploring End-to-End Learning for Efficient Cooperative Sequential Perception](cooptrack_exploring_end-to-end_learning_for_efficient_cooperative_sequential_per.md)**

:   提出 CoopTrack，首个完全实例级端到端协同 3D 多目标跟踪框架，通过可学习的图注意力关联模块和多维特征提取实现跨Agent实例匹配与融合，在 V2X-Seq 上达到 SOTA。

**[Counting Stacked Objects](counting_stacked_objects.md)**

:   将堆叠物体计数问题分解为"体积估计"和"占空比估计"两个子问题，前者用多视角3D重建解决，后者用深度图驱动的神经网络从可见表面推断，首次实现了对不可见堆叠物体的准确计数，性能远超人类。

**[CVFusion: Cross-View Fusion of 4D Radar and Camera for 3D Object Detection](cvfusion_cross-view_fusion_of_4d_radar_and_camera_for_3d_object_detection.md)**

:   提出CVFusion——首个4D雷达-相机两阶段融合网络，第一阶段通过雷达引导迭代（RGIter）BEV融合生成高召回率提案框，第二阶段利用点引导融合（PGF）和网格引导融合（GGF）聚合多视角异构特征进行提案精化，在VoD和TJ4DRadSet上分别取得9.10%和3.68%的mAP提升。

**[DAMap: Distance-aware MapNet for High Quality HD Map Construction](damap_distance-aware_mapnet_for_high_quality_hd_map_construction.md)**

:   揭示当前HD地图构建方法在高质量预测上的两大固有缺陷——不恰当的分类标签与次优的任务特征，提出DAMap（含DAFL、HLS、TMDA三个组件）系统性地解决任务错位问题，在NuScenes和Argoverse2上多个基线方法上一致提升2-3 mAP。

**[DCHM: Depth-Consistent Human Modeling for Multiview Detection](dchm_depth-consistent_human_modeling_for_multiview_detection.md)**

:   提出 DCHM，一种无需 3D 标注的深度一致性人体建模框架，通过超像素级高斯溅射生成伪深度标签来微调单目深度估计网络，结合多视角标签匹配实现稀疏视角、遮挡严重场景下的高精度行人检测，在 Wildtrack 上 MODA 达 84.2%，MODP 较 UMPD 提升 31.2%。

**[Decoupled Diffusion Sparks Adaptive Scene Generation](decoupled_diffusion_sparks_adaptive_scene_generation.md)**

:   提出 Nexus，一个基于解耦扩散的自适应驾驶场景生成框架，通过独立噪声状态实现目标导向与实时响应的统一，将位移误差降低 40%，并构建了包含 540 小时安全关键驾驶数据的 Nexus-Data。

**[DuET: Dual Incremental Object Detection via Exemplar-Free Task Arithmetic](duet_dual_incremental_object_detection_via_exemplar-free_task_arithmetic.md)**

:   提出 DuET 框架，首次以无样本（exemplar-free）的任务算术（Task Arithmetic）模型合并方式，同时解决目标检测中的类别增量和域增量问题（Dual Incremental Object Detection, DuIOD），并引入方向一致性损失（Directional Consistency Loss）缓解符号冲突，在 Pascal Series 和 Diverse Weather Series 上大幅超越现有方法。

**[Extrapolated Urban View Synthesis Benchmark](extrapolated_urban_view_synthesis_benchmark.md)**

:   提出首个外推式城市视图合成（EUVS）基准，利用多遍历/多车辆/多相机公开数据集系统评估外推场景下 3DGS 及 NeRF 方法的泛化能力，揭示当前方法严重过拟合训练视角。

**[GaussRender: Learning 3D Occupancy with Gaussian Rendering](gaussrender_learning_3d_occupancy_with_gaussian_rendering.md)**

:   提出 GaussRender，一个即插即用的可微高斯渲染模块，通过将预测和真值的 3D occupancy 投影到 2D 视图并施加语义和深度一致性约束，消除浮空体素等视觉伪影，在多个 benchmark 上显著提升几何保真度，尤其在 RayIoU 等表面敏感指标上提升突出。

**[GS-LIVM: Real-Time Photo-Realistic LiDAR-Inertial-Visual Mapping with Gaussian Splatting](gs-livm_real-time_photo-realistic_lidar-inertial-visual_mapping_with_gaussian_sp.md)**

:   提出 GS-LIVM，首个为大规模无界室外场景设计的实时光真实感 LiDAR-惯性-视觉建图框架，通过体素级高斯过程回归（Voxel-GPR）解决 LiDAR 点云稀疏不均匀问题，利用协方差中心化设计快速初始化 3D 高斯参数，在多个室外数据集上达到 SOTA 的建图效率和渲染质量。

**[Language Driven Occupancy Prediction (LOcc)](language_driven_occupancy_prediction.md)**

:   提出LOcc，一个有效且可泛化的开放词汇占据(OVO)预测框架，核心是设计了语义传递标注管线（LVLM+OV-Seg→LiDAR→voxel），生成密集细粒度的3D语言占据伪GT，替代了噪声大且稀疏的传统中间特征蒸馏，在Occ3D-nuScenes上全面超越SOTA。

**[LookOut: Real-World Humanoid Egocentric Navigation](lookout_real-world_humanoid_egocentric_navigation.md)**

:   提出LookOut，从自我中心视频预测未来6D头部姿态轨迹（包含平移+旋转），通过时序聚合3D DINO特征理解场景几何/语义约束，并贡献了基于Project Aria眼镜采集的4小时真实世界导航数据集AND。

**[MGSfM: Multi-Camera Geometry Driven Global Structure-from-Motion](mgsfm_multi-camera_geometry_driven_global_structure-from-motion.md)**

:   提出 MGSfM，一个面向多相机系统的全局 Structure-from-Motion (SfM) 框架，通过**解耦旋转平均 (DMRA)** 和**混合平移平均 (MGP)** 两个核心模块，充分利用多相机刚性约束，在大规模场景中实现与增量式 SfM 媲美甚至更优的精度，同时速度提升约 10 倍。

**[Mixed Signals: A Diverse Point Cloud Dataset for Heterogeneous LiDAR V2X Collaboration](mixed_signals_a_diverse_point_cloud_dataset_for_heterogeneous_lidar_v2x_collabor.md)**

:   Mixed Signals 是首个包含异构 LiDAR 配置（不同高度和倾斜角）的真实世界 V2X 数据集，由 3 辆自动驾驶车 + 路侧单元采集，提供 4.51 万点云帧和 24.06 万标注框，同时也是首个左行交通国家（澳大利亚）的 V2X 数据集。

**[MonoSOWA: Scalable Monocular 3D Object Detector Without Human Annotations](monosowa_scalable_monocular_3d_object_detector_without_human_annotations.md)**

:   提出首个完全不依赖人工标注（包括 2D 和 3D）的单目 3D 物体检测方法，通过新提出的局部目标运动模型（LOMM）解耦帧间运动来源，自动标注速度比前人快 700 倍，并通过规范目标空间（COS）融合不同相机设置的多数据集训练。

**[RoboTron-Sim: Improving Real-World Driving via Simulated Hard-Case](robotron-sim_improving_real-world_driving_via_simulated_hard-case.md)**

:   提出RoboTron-Sim框架，通过构建困难场景仿真数据集HASS、场景感知提示工程SPE和图像到自车编码器I2E，使MLLM有效利用仿真困难案例提升真实世界自动驾驶性能，在nuScenes困难场景下L2距离降低~48%、碰撞率降低~46%，达到开环规划SOTA。

**[Robust 3D Object Detection using Probabilistic Point Clouds from Single-Photon LiDARs](robust_3d_object_detection_using_probabilistic_point_clouds_from_single-photon_l.md)**

:   提出概率点云(PPC)表示——将单光子LiDAR原始时间直方图中的测量置信度作为概率属性附加到每个3D点上，配合轻量级NPD滤波和FPPS采样方法，实现低信噪比(SBR)下鲁棒的3D目标检测，在SUN RGB-D和KITTI上大幅超越点云去噪基线，且几乎不增加计算开销。

**[Splat-LOAM: Gaussian Splatting LiDAR Odometry and Mapping](splat-loam_gaussian_splatting_lidar_odometry_and_mapping.md)**

:   首个纯基于 2D Gaussian 原语的 LiDAR 里程计与建图管线，通过球面投影驱动的可微分光栅化器同时实现高精度位姿估计和轻量化场景重建。

**[TARS: Traffic-Aware Radar Scene Flow Estimation](tars_traffic-aware_radar_scene_flow_estimation.md)**

:   提出 TARS，一种交通感知的雷达场景流估计方法，通过联合目标检测构建交通向量场（TVF），在交通层面而非实例层面捕获刚体运动，在 VOD 和专有数据集上分别超越 SOTA 15% 和 23%。

**[TrafficLoc: Localizing Traffic Surveillance Cameras in 3D Scenes](trafficloc_localizing_traffic_surveillance_cameras_in_3d_scenes.md)**

:   提出 TrafficLoc，一种粗到细的图像-点云配准方法，通过几何引导注意力损失(GAL)、模态间-模态内对比学习(ICL)和稠密训练对齐(DTA)，实现交通监控相机在3D参考地图中的高精度定位，在自建 Carla Intersection 数据集上较 SOTA 提升达 86%。

**[UAVScenes: A Multi-Modal Dataset for UAVs](uavscenes_a_multi-modal_dataset_for_uavs.md)**

:   UAVScenes 是首个同时提供逐帧图像和 LiDAR 点云语义标注及精确 6-DoF 位姿的大规模多模态无人机数据集，包含超 12 万帧标注数据，支持语义分割、深度估计、定位、场景识别和新视角合成等六类感知任务。

**[Unleashing the Temporal Potential of Stereo Event Cameras for Continuous-Time 3D Perception](unleashing_the_temporal_potential_of_stereo_event_cameras_for_continuous-time_3d.md)**

:   提出首个仅依赖立体事件相机的 3D 目标检测框架，通过语义-几何双重滤波模块和目标中心 ROI 对齐，在 blind time 期间实现连续时间 3D 检测，在动态大运动场景下显著优于依赖同步传感器的方法（Ev-3DOD），行人 AP3D 甚至超越使用 LiDAR+RGB+Event 的方法。

**[Unraveling the Effects of Synthetic Data on End-to-End Autonomous Driving](unraveling_the_effects_of_synthetic_data_on_end-to-end_autonomous_driving.md)**

:   提出 SceneCrafter，一个基于 3DGS 的统一仿真框架，通过自适应运动学模型和双向交互式智能体控制，同时支持合成数据生成和闭环评估，实验证明合成数据可显著提升端到端自动驾驶模型的泛化能力（Route Completion 提升 18%）。

**[Where, What, Why: Towards Explainable Driver Attention Prediction](where_what_why_towards_explainable_driver_attention_prediction.md)**

:   本文提出了"可解释驾驶员注意力预测"新范式，构建了首个大规模 W³DA 数据集并设计了 LLada 框架，将空间注意力预测（Where）、语义解析（What）和认知推理（Why）统一在一个端到端的大语言模型驱动架构中。
