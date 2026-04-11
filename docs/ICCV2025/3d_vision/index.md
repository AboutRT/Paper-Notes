<!-- 由 src/gen_blog_index.py 自动生成 -->
# 🧊 3D 视觉

**📹 ICCV2025** · 共 **122** 篇

**[TRAN-D: 2D Gaussian Splatting-based Sparse-view Transparent Object Depth Reconstruction via Physics Simulation for Scene Update](2d_gaussian_splattingbased_sparseview_transparent_object_dep.md)**

:   提出TRAN-D，一种基于2D Gaussian Splatting的稀疏视角透明物体深度重建方法，通过分割引导的object-aware损失优化遮挡区域Gaussian分布，并利用物理仿真（MPM）实现物体移除后的场景动态更新，仅需单张图像即可完成场景刷新。

**[3D Gaussian Map with Open-Set Semantic Grouping for Vision-Language Navigation](3d_gaussian_map_with_openset_semantic_grouping_for_visionlan.md)**

:   提出基于3D高斯溅射的场景地图表示（3D Gaussian Map），结合开放集语义分组机制，为视觉-语言导航（VLN）构建兼顾几何结构与丰富语义的3D环境表示，并设计多层级动作预测策略（Multi-Level Action Prediction）融合多粒度空间-语义线索辅助导航决策。

**[3D Mesh Editing using Masked LRMs](3d_mesh_editing_using_masked_lrms.md)**

:   提出MaskedLRM，将3D形状编辑重构为条件重建问题——训练时随机生成3D遮挡物遮盖多视角输入，用一张干净条件视图引导被遮挡区域的补全；推理时用户定义编辑区域并提供单张编辑图像，模型在**<3秒单次前传**中完成3D网格编辑，比优化方法快2-10倍，能执行拓扑变化编辑（加孔/加把手），重建质量与SOTA持平。

**[3D Test-time Adaptation via Graph Spectral Driven Point Shift](3d_test-time_adaptation_via_graph_spectral_driven_point_shift.md)**

:   提出 GSDTTA，将3D点云测试时自适应从空间域转移到图谱域，仅优化最低10%频率分量即可适配点云的全局结构，配合特征图引导的自训练策略，在 ModelNet40-C 和 ScanObjectNN-C 上达到 SOTA。

**[3D Test-time Adaptation via Graph Spectral Driven Point Shift](3d_testtime_adaptation_via_graph_spectral_driven_point_shift.md)**

:   提出GSDTTA，首次将3D点云的测试时适应从空间域转移到图谱域，通过仅优化最低10%频率分量（减少约90%参数）实现全局结构调整，并结合特征图引导的自训练策略生成伪标签，在ModelNet40-C和ScanObjectNN-C上显著超越现有3D TTA方法。

**[3DGraphLLM: Combining Semantic Graphs and Large Language Models for 3D Scene Understanding](3dgraphllm_combining_semantic_graphs_and_large_language_mode.md)**

:   提出3DGraphLLM，首个将**3D语义场景图的可学习表示**直接输入LLM的方法——通过k近邻子图+三元组(object1, relation, object2)编码物体间语义关系，然后投影到LLM的token嵌入空间。在ScanRefer上Acc@0.5提升+6.4%（vs无语义关系的Chat-Scene），在Multi3DRefer上F1@0.5提升+7.5%，推理速度比GPT4Scene-HDM快5倍。

**[3DGraphLLM: Combining Semantic Graphs and Large Language Models for 3D Scene Understanding](3dgraphllm_combining_semantic_graphs_and_large_language_models_for_3d_scene_unde.md)**

:   本文提出3DGraphLLM，将3D场景中物体间的语义关系编码为可学习的图表示并输入LLM，在object grounding、场景描述和视觉问答等多个3D视觉-语言任务上显著超越不使用语义关系的基线方法，同时推理速度比LVLM方法快5倍。

**[3DGS-LM: Faster Gaussian-Splatting Optimization with Levenberg-Marquardt](3dgs-lm_faster_gaussian-splatting_optimization_with_levenberg-marquardt.md)**

:   本文提出3DGS-LM，用定制的Levenberg-Marquardt优化器替换3DGS中的ADAM优化器，通过高效的GPU缓存驱动并行化方案实现Jacobian-向量积的快速计算，在保持相同重建质量的前提下将3DGS优化速度提升20%。

**[3DGS-LM: Faster Gaussian-Splatting Optimization with Levenberg-Marquardt](3dgslm_faster_gaussiansplatting_optimization_with_levenbergm.md)**

:   将3D Gaussian Splatting的ADAM优化器替换为定制化的Levenberg-Marquardt（LM）二阶优化器，通过高效CUDA并行化的PCG算法和梯度缓存结构实现Jacobian-向量积加速，在保持相同重建质量的前提下将优化时间缩短约20%。

**[4D Gaussian Splatting SLAM](4d_gaussian_splatting_slam.md)**

:   提出首个完整的4D Gaussian Splatting SLAM系统，在动态场景中同时进行相机位姿跟踪和4D高斯辐射场重建——将高斯原语分为静态/动态集合，通过稀疏控制点+MLP建模动态物体运动，并创新性地设计2D光流图渲染算法来监督动态高斯的运动学习。

**[4D Visual Pre-training for Robot Learning](4d_visual_pre-training_for_robot_learning.md)**

:   FVP提出了一种基于4D（3D空间+时间）点云预测的视觉预训练框架，通过将预训练目标建模为"下一帧点云预测"并用扩散模型实现，显著提升了多种3D模仿学习方法在真实机器人操作任务上的成功率（DP3平均提升28%）。

**[4D Visual Pre-training for Robot Learning](4d_visual_pretraining_for_robot_learning.md)**

:   FVP提出将3D视觉预训练建模为"下一帧点云预测"问题，用条件扩散模型从历史帧点云预测未来帧点云来学习3D视觉表示，在12个真实世界操作任务中将DP3的平均成功率提升28%，达到SOTA水平。

**[7DGS: Unified Spatial-Temporal-Angular Gaussian Splatting](7dgs_unified_spatial-temporal-angular_gaussian_splatting.md)**

:   将3DGS扩展到7维（空间3D+时间1D+方向3D），通过条件切片机制将7D高斯投影为与3DGS管线兼容的3D高斯，在具有视角依赖效果的动态场景上PSNR提升最高7.36dB，同时维持401 FPS实时渲染。

**[7DGS: Unified Spatial-Temporal-Angular Gaussian Splatting](7dgs_unified_spatialtemporalangular_gaussian_splatting.md)**

:   提出7DGS，将场景元素建模为**7维高斯分布**（3D空间+1D时间+3D视角方向），通过条件切片机制将7D高斯转换为与时间和视角相关的条件3D高斯，统一处理动态场景+视角依赖效果，在自定义7DGS-PBR数据集上比4DGS PSNR提升高达7.36dB，仅用15.3%的高斯点数，401FPS实时渲染。

**[A3GS: Arbitrary Artistic Style into Arbitrary 3D Gaussian Splatting](a3gs_arbitrary_artistic_style_into_arbitrary_3d_gaussian_spl.md)**

:   提出A³GS，首个**前馈式零样本3DGS风格迁移**网络——使用图卷积网络(GCN)自编码器将3DGS场景编码到潜在空间，通过AdaIN注入任意风格图像特征，仅需**10秒**即可将任意风格迁移到任意3D场景，无需逐风格优化，可处理大规模3DGS场景。

**[A Lesson in Splats: Teacher-Guided Diffusion for 3D Gaussian Splats Generation with 2D Supervision](a_lesson_in_splats_teacher-guided_diffusion_for_3d_gaussian_splats_generation_wi.md)**

:   本文提出了一种仅使用2D图像监督来训练3D扩散模型的新框架——通过将确定性3D重建模型作为"噪声教师"生成3D噪声样本，并结合多步去噪策略和循环一致性正则化，实现了超越教师模型的3D高斯喷溅生成质量（PSNR提升0.5-0.85）。

**[A Lesson in Splats: Teacher-Guided Diffusion for 3D Gaussian Splats Generation with 2D Supervision](a_lesson_in_splats_teacherguided_diffusion_for_3d_gaussian_s.md)**

:   提出一种用2D图像监督训练3D扩散模型的框架：利用预训练的确定性3D重建模型作为"噪声教师"生成3D噪声样本，通过多步去噪策略和渲染损失实现跨模态（3D去噪+2D监督）训练，在用更小模型的情况下超越教师模型0.5-0.85 PSNR。

**[A Recipe for Generating 3D Worlds from a Single Image](a_recipe_for_generating_3d_worlds_from_a_single_image.md)**

:   将单图到3D世界生成分解为两个更简单的子问题——全景合成（无训练in-context learning）和点云条件修复（仅5k步微调ControlNet），结合3DGS重建出可在VR中2米立方体范围内导航的沉浸式3D环境，在图像质量指标上全面超越WonderJourney和DimensionX等SOTA方法。

**[A Simple yet Mighty Hartley Diffusion Versatilist for Generalizable Dense Vision Tasks](a_simple_yet_mighty_hartley_diffusion_versatilist_for_genera.md)**

:   提出HarDiff——基于离散Hartley变换的频域学习策略，通过低频训练（从源域提取结构先验）和高频采样（利用目标域细节引导）增强扩散模型在稠密视觉任务上的跨域泛化能力，在语义分割、深度估计和去雾等12个基准上取得SOTA。

**[A Unified Interpretation of Training-Time Out-of-Distribution Detection](a_unified_interpretation_of_training-time_out-of-distribution_detection.md)**

:   从输入变量间"交互"的新视角出发，统一解释了不同训练时 OOD 检测方法为何有效——它们都促使模型编码更多高阶交互，并进一步验证了高阶交互在 OOD 检测中的主导作用，以及 near-OOD 样本难以检测的交互分布原因。

**[AAA-Gaussians: Anti-Aliased and Artifact-Free 3D Gaussian Rendering](aaa-gaussians_anti-aliased_and_artifact-free_3d_gaussian_rendering.md)**

:   AAA-Gaussians提出了一种统一的3D高斯光栅化框架，通过自适应3D平滑滤波器、视空间透视正确边界计算和基于视锥体的3D裁剪，在单一框架内同时解决了3DGS的锯齿、投影畸变和闪烁三大顽疾，在分布外视角评估中大幅领先其他方法，同时保持实时渲染性能。

**[AAA-Gaussians: Anti-Aliased and Artifact-Free 3D Gaussian Rendering](aaagaussians_antialiased_and_artifactfree_3d_gaussian_render.md)**

:   通过在3DGS渲染管线的所有环节中融入完整的3D评估（而非2D splat近似），提出自适应3D平滑滤波器、视空间边界计算和基于视锥的tile剔除，统一解决了3DGS中的锯齿、投影伪影和弹出伪影（popping），在OOD视角下大幅优于现有方法，同时保持实时渲染（>100 FPS）。

**[Accelerate 3D Object Detection Models via Zero-Shot Attention Key Pruning](accelerate_3d_object_detection_models_via_zero-shot_attention_key_pruning.md)**

:   提出 tgGBC（trim keys gradually Guided By Classification scores），一种零样本运行时剪枝方法，利用分类分数与注意力图的乘积计算键重要性，逐层剪除不重要的键，在多个3D检测器上实现Transformer解码器近2×加速且性能损失<1%。

**[AdaHuman: Animatable Detailed 3D Human Generation with Compositional Multiview Diffusion](adahuman_animatable_detailed_3d_human_generation_with_compos.md)**

:   提出AdaHuman框架，通过姿态条件的联合3D扩散模型（在扩散过程中同步进行多视角图像生成与3DGS重建以保证3D一致性）和组合式3DGS细化模块（利用crop-aware camera ray map融合局部精细细节），从单张野外图片生成高保真可动画的3D人体avatar，在重建和重姿态任务上全面超越现有SOTA。

**[AdaHuman: Animatable Detailed 3D Human Generation with Compositional Multiview Diffusion](adahuman_animatable_detailed_3d_human_generation_with_compositional_multiview_di.md)**

:   提出AdaHuman框架，通过姿态条件化的3D联合扩散模型和组合式3DGS细化模块，从单张图片生成高精度、可动画化的3D人体虚拟人。

**[Advancing Text-to-3D Generation with Linearized Lookahead Variational Score Distillation](advancing_text-to-3d_generation_with_linearized_lookahead_variational_score_dist.md)**

:   通过分析 VSD 中 LoRA 模型与 3D 模型的优化顺序不匹配问题，提出线性化前瞻（Linearized Lookahead）修正项 $L^2$-VSD，仅需额外一次前向传播即可显著提升 text-to-3D 生成质量。

**[Adversarial Exploitation of Data Diversity Improves Visual Localization](adversarial_exploitation_of_data_diversity_improves_visual_l.md)**

:   提出RAP（Robust Absolute Pose regression）——基于外观感知3DGS的双分支联合训练框架，通过对抗判别器弥合合成-真实域差距+外观/位姿增强数据作为额外监督，在Cambridge Landmarks上平移/旋转误差分别降低38-50%/41-44%，在日夜场景和驾驶场景中表现尤为突出。

**[Adversarial Exploitation of Data Diversity Improves Visual Localization](adversarial_exploitation_of_data_diversity_improves_visual_localization.md)**

:   提出RAP框架，通过外观可变的3DGS合成多样化训练数据，并引入对抗判别器弥合合成-真实域差距，使绝对姿态回归方法在多个数据集上大幅超越SOTA——室内平移/旋转误差降低50%/41%，室外降低38%/44%。

**[AJAHR: Amputated Joint Aware 3D Human Mesh Recovery](ajahr_amputated_joint_aware_3d_human_mesh_recovery.md)**

:   首个面向截肢者的3D人体网格恢复框架——通过合成100万+截肢者图像(A3D)、设计BPAC-Net截肢分类器区分截肢与遮挡、以及双Tokenizer切换策略分别编码截肢/正常位姿先验，在截肢者数据上大幅领先(ITW-amputee上MVE比TokenHMR低16.87)，非截肢者数据上也保持竞争力。

**[Amodal3R: Amodal 3D Reconstruction from Occluded 2D Images](amodal3r_amodal_3d_reconstruction_from_occluded_2d_images.md)**

:   提出Amodal3R，一个端到端的遮挡感知3D重建模型，通过在TRELLIS基础上引入mask加权交叉注意力和遮挡感知注意力层，直接在3D潜空间中从部分遮挡的2D图像重建完整的3D物体形状和外观，大幅超越先前"2D补全→3D重建"的两阶段方法。

**[Amodal Depth Anything: Amodal Depth Estimation in the Wild](amodal_depth_anything_amodal_depth_estimation_in_the_wild.md)**

:   提出非模态相对深度估计新范式，构建大规模真实数据集ADIW（564K），基于Depth Anything V2和DepthFM设计两个互补框架（Amodal-DAV2和Amodal-DepthFM），通过最小化修改预训练模型实现遮挡区域深度预测，在ADIW上RMSE比之前SOTA提升27.4%。

**[AnimateAnyMesh: A Feed-Forward 4D Foundation Model for Text-Driven Universal Mesh Animation](animateanymesh_a_feedforward_4d_foundation_model_for_textdri.md)**

:   提出AnimateAnyMesh，首个前馈式文本驱动通用Mesh动画框架：通过DyMeshVAE将动态Mesh分解为初始位置和相对轨迹并压缩到潜空间，再用基于Rectified Flow的MMDiT模型学习文本条件下的轨迹分布，配合4M+规模的DyMesh数据集训练，在6秒内即可为任意拓扑Mesh生成高质量动画，全面碾压DG4D、L4GM和Animate3D。

**[AnyI2V: Animating Any Conditional Image with Motion Control](anyi2v_animating_any_conditional_image_with_motion_control.md)**

:   提出AnyI2V，一个无需训练的框架，可接受任意模态图像（mesh、点云、深度图、骨架等）作为首帧条件，结合用户定义的轨迹实现运动控制的视频生成，在FID/FVD/ObjMC指标上优于现有training-free方法并与训练方法竞争。

**[AR-1-to-3: Single Image to Consistent 3D Object Generation via Next-View Prediction](ar1to3_single_image_to_consistent_3d_object_via_nextview_pre.md)**

:   提出AR-1-to-3，一种基于扩散模型的自回归下一视角预测框架，通过"先近后远"的渐进式生成策略，配合Stacked-LE（堆叠局部特征编码）和LSTM-GE（全局特征编码）两种条件注入机制，显著提升了单图到多视角生成的一致性，在GSO数据集上PSNR达13.18（相比InstantMesh的10.67提升23.5%），Chamfer Distance降至0.063（InstantMesh为0.117）。

**[Articulate3D: Holistic Understanding of 3D Scenes as Universal Scene Description](articulate3d_holistic_understanding_of_3d_scenes_as_universa.md)**

:   提出Articulate3D（280个真实室内场景、8类铰接标注的大规模数据集）和USDNet（基于Mask3D扩展的统一框架），通过密集逐点预测机制同时完成可动零件分割和运动参数估计，在铰接参数预测上比Mask3D†提升5.7%，并支持LLM场景编辑和机器人策略训练。

**[Articulate3D: Holistic Understanding of 3D Scenes as Universal Scene Description](articulate3d_holistic_understanding_of_3d_scenes_as_universal_scene_description.md)**

:   本文提出Articulate3D——首个大规模真实世界室内场景铰接标注数据集（280个高质量扫描），以及USDNet统一框架，能从3D点云同时预测可移动/可交互部件分割和运动参数，为具身AI的物理仿真提供了simulation-ready的场景数据。

**[ATLAS: Decoupling Skeletal and Shape Parameters for Expressive Parametric Human Modeling](atlas_decoupling_skeletal_and_shape_parameters_for_expressiv.md)**

:   提出ATLAS参数化人体模型，通过显式解耦外部表面形状和内部骨骼参数，并引入稀疏非线性姿态校正变形，在60万高分辨率扫描数据上训练，实现了比SMPL-X更精确、更可控的3D人体建模。

**[ATLAS: Decoupling Skeletal and Shape Parameters for Expressive Parametric Human Modeling](atlas_decoupling_skeletal_and_shape_parameters_for_expressive_parametric_human_m.md)**

:   提出 ATLAS 参数化人体模型，通过显式解耦外部表面形状与内部骨骼参数，结合稀疏非线性姿态校正，在 60 万高分辨率扫描上训练，实现比 SMPL-X 更精确可控的人体建模。

**[Auto-Regressively Generating Multi-View Consistent Images](auto-regressively_generating_multi-view_consistent_images.md)**

:   提出 MV-AR，首次将自回归模型引入多视图图像生成，利用所有先前视图作为条件逐步生成后续视图，配合统一的多模态条件注入模块和 Shuffle View 数据增强，在文本/图像/形状条件下均达到与扩散模型可比的一致性。

**[AutoOcc: Automatic Open-Ended Semantic Occupancy Annotation via Vision-Language Guided Gaussian Splatting](autoocc_automatic_openended_semantic_occupancy_annotation_vi.md)**

:   提出AutoOcc，一个以视觉为中心的全自动开放式语义占据标注流水线，通过视觉-语言模型引导的可微高斯泼溅（VL-GS）实现无需人工标签的3D语义占据生成，在Occ3D-nuScenes上以纯视觉输入就达到IoU 83.01/mIoU 20.92，大幅超越现有自动标注方法。

**[Back on Track: Bundle Adjustment for Dynamic Scene Reconstruction](back_on_track_bundle_adjustment_for_dynamic_scene_reconstruc.md)**

:   提出BA-Track框架，通过学习型3D点追踪器将观测到的运动解耦为相机引起的运动和物体自身运动，使传统束调整(BA)能够无差别地处理静态和动态点，在相机位姿估计(ATE在Sintel上达到0.034，较SOTA降低一半以上)和稠密3D重建上取得显著提升。

**[Back on Track: Bundle Adjustment for Dynamic Scene Reconstruction](back_on_track_bundle_adjustment_for_dynamic_scene_reconstruction.md)**

:   提出 BA-Track 框架，利用 3D 点追踪器将观测运动分解为相机运动和物体运动，使传统 Bundle Adjustment 能同时处理静态与动态场景元素，实现精确的相机位姿估计和时间一致的稠密重建。

**[Baking Gaussian Splatting into Diffusion Denoiser for Fast and Scalable Single-stage Image-to-3D Generation and Reconstruction](baking_gaussian_splatting_into_diffusion_denoiser_for_fast_a.md)**

:   提出DiffusionGS，将3D高斯点云直接嵌入扩散模型的去噪器中，通过单阶段3D扩散实现从单张图片到3D物体生成和场景重建，在ABO/GSO上PSNR超越SOTA 2.20/1.25 dB，RealEstate10K上超1.34 dB，推理速度约6秒（A100）。

**[Baking Gaussian Splatting into Diffusion Denoiser for Fast and Scalable Single-stage Image-to-3D Generation and Reconstruction](baking_gaussian_splatting_into_diffusion_denoiser_for_fast_and_scalable_single-s.md)**

:   提出DiffusionGS，将3D高斯点云"烘焙"进扩散模型的去噪器中，实现单阶段、视图一致的单视图3D物体生成和场景重建，配合场景-物体混合训练策略和RPPC相机条件编码，在PSNR/FID上大幅超越现有方法，推理速度仅需约6秒。

**[BANet: Bilateral Aggregation Network for Mobile Stereo Matching](banet_bilateral_aggregation_network_for_mobile_stereo_matchi.md)**

:   提出双边聚合网络BANet，通过将代价体分离为高频细节体和低频平滑体分别聚合再融合，仅使用2D卷积即可在移动设备上实现实时高精度立体匹配（骁龙8 Gen 3上45ms，KITTI 2015 D1-all=1.83%，比MobileStereoNet-2D精度高35.3%）。

**[BANet: Bilateral Aggregation Network for Mobile Stereo Matching](banet_bilateral_aggregation_network_for_mobile_stereo_matching.md)**

:   提出双边聚合网络BANet，通过空间注意力将代价体分离为高频细节体和低频平滑体并分别聚合，仅使用2D卷积即可在移动设备上实时运行并大幅超越MobileStereoNet-2D（KITTI 2015上精度提升35.3%），3D版本在GPU上达到实时方法最高精度。

**[Benchmarking and Learning Multi-Dimensional Quality Evaluator for Text-to-3D Generation](benchmarking_and_learning_multidimensional_quality_evaluator.md)**

:   构建MATE-3D基准（8类prompt×8种方法=1280个textured mesh，4维度×21人主观评分=107520标注）并提出HyperScore多维质量评估器：通过可学习条件特征+条件特征融合(模拟注意力转移)+超网络生成维度自适应映射函数(模拟决策过程变化)，在语义对齐、几何、纹理、整体4个维度上全面超越现有指标。

**[Benchmarking Egocentric Visual-Inertial SLAM at City Scale](benchmarking_egocentric_visualinertial_slam_at_city_scale.md)**

:   提出 LaMAria——首个城市尺度的第一人称多传感器 VIO/SLAM 基准数据集，利用测绘级控制点提供厘米精度的地面真值，系统评估了学术界主流 SLAM 方案在真实第一人称场景下的表现，揭示了现有方法与商业系统之间的巨大差距。

**[BézierGS: Dynamic Urban Scene Reconstruction with Bézier Curve Gaussian Splatting](beziergs_dynamic_urban_scene_reconstruction_with_bezier_curv.md)**

:   用可学习的Bézier曲线显式建模动态物体的运动轨迹，替代传统依赖精确bbox标注的范式，实现了对自动驾驶街景中动/静态成分的准确分离与高保真重建。

**[BezierGS: Dynamic Urban Scene Reconstruction with Bézier Curve Gaussian Splatting](beziergs_dynamic_urban_scene_reconstruction_with_bezier_curve_gaussian_splatting.md)**

:   提出用可学习的Bézier曲线建模动态物体运动轨迹的3D高斯溅射方法（BezierGS），摆脱对精确目标标注框的依赖，在Waymo和nuPlan数据集上的动态和静态场景重建均达到SOTA。

**[BillBoard Splatting (BBSplat): Learnable Textured Primitives for Novel View Synthesis](billboard_splatting_bbsplat_learnable_textured_primitives_fo.md)**

:   提出BBSplat——用可学习的RGB纹理和alpha贴图替代2D Gaussian Splatting中的高斯分布不透明度，使每个平面基元具有任意形状和逐像素颜色控制，在用更少基元的情况下弥补2DGS与3DGS之间的渲染质量差距，同时保留精确网格提取能力并实现最高×17的存储压缩。

**[Blended Point Cloud Diffusion for Localized Text-guided Shape Editing](blended_point_cloud_diffusion_for_localized_textguided_shape.md)**

:   提出 BlendedPC，将局部文本引导的3D形状编辑重新定义为语义inpainting问题，通过在Point·E基础上训练Inpaint-E模型，并在推理时引入无需反演(inversion-free)的坐标混合(coordinate blending)机制，在保持原始形状身份的同时实现精准局部编辑，在ShapeTalk数据集上全面超越现有方法。

**[Bolt3D: Generating 3D Scenes in Seconds](bolt3d_generating_3d_scenes_in_seconds.md)**

:   提出一种基于潜在扩散模型的前馈式3D场景生成方法，通过将3D场景表示为多组Splatter Image并使用专门训练的几何VAE，**在单GPU上7秒内生成完整3D场景**，推理成本比优化式方法（CAT3D）降低300倍。

**[Boost 3D Reconstruction using Diffusion-based Monocular Camera Calibration](boost_3d_reconstruction_using_diffusion-based_monocular_camera_calibration.md)**

:   提出 DM-Calib，利用 Stable Diffusion 先验进行单目相机内参估计，设计了 Camera Image 表示将内参无损编码为图像，结合 RANSAC 解算焦距和光心，在5个零样本数据集上大幅超越现有标定方法，并推进了度量深度估计、位姿估计和稀疏视图重建等下游任务。

**[Boost 3D Reconstruction using Diffusion-based Monocular Camera Calibration](boost_3d_reconstruction_using_diffusionbased_monocular_camer.md)**

:   提出DM-Calib——基于扩散模型的单目相机内参估计方法：设计Camera Image表示（将内参无损编码为3通道图像=方位角+仰角+灰度图），微调Stable Diffusion生成Camera Image，用RANSAC提取内参，在5个零样本数据集上超越所有基线，并将相机标定扩展到度量深度估计、位姿估计和稀疏视角3D重建。

**[Boosting Multi-View Indoor 3D Object Detection via Adaptive 3D Volume Construction](boosting_multi-view_indoor_3d_object_detection_via_adaptive_3d_volume.md)**

:   提出SGCDet框架，通过几何与上下文感知聚合模块（自适应特征提升）和稀疏体素构建策略（粗到细的自适应体素选择），在不依赖GT场景几何的前提下，实现了高效且高精度的多视图室内3D目标检测。

**[SGCDet: Boosting Multi-View Indoor 3D Object Detection via Adaptive 3D Volume Construction](boosting_multi-view_indoor_3d_object_detection_via_adaptive_3d_volume_constructi.md)**

:   SGCDet 通过自适应稀疏3D体素构建和几何-上下文感知聚合，实现了高效精准的多视图室内3D目标检测，无需真实几何监督即超越现有方法。

**[Boosting Multi-View Indoor 3D Object Detection via Adaptive 3D Volume Construction](boosting_multiview_indoor_3d_object_detection_via_adaptive_3.md)**

:   SGCDet通过几何与上下文感知的聚合模块（3D可变形注意力+多视角注意力融合）和基于占据概率的稀疏体素构建策略，在无需ground-truth几何监督的情况下，实现了多视角室内3D目标检测的SOTA性能，同时大幅降低计算开销。

**[Bootstrap3D: Improving Multi-view Diffusion Model with Synthetic Data](bootstrap3d_improving_multiview_diffusion_model_with_synthet.md)**

:   提出Bootstrap3D框架，利用视频扩散模型生成合成多视图数据，并通过微调的MV-LLaVA进行质量过滤与密集描述重写，结合Training Timestep Reschedule (TTR)策略训练多视图扩散模型，在不牺牲视图一致性的前提下大幅提升图像质量和文本对齐能力。

**[BoxDreamer: Dreaming Box Corners for Generalizable Object Pose Estimation](boxdreamer_dreaming_box_corners_for_generalizable_object_pos.md)**

:   提出以3D包围盒角点作为中间表示，通过Transformer解码器预测查询视图中角点的2D投影热图，结合PnP算法实现可泛化的稀疏视角6DoF物体位姿估计，在遮挡和稀疏视角场景下显著优于现有方法。

**[PASDF: Bridging 3D Anomaly Localization and Repair via High-Quality Continuous Geometric Representation](bridging_3d_anomaly_localization_and_repair_via_highquality.md)**

:   提出PASDF框架，通过姿态对齐模块(PAM)将点云对齐到标准姿态 + 神经SDF网络学习连续几何表示 + 基于SDF偏差的异常评分，统一实现3D点云异常检测与异常修复(Marching Cubes提取零等值面作为修复模板)，在Real3D-AD上O-AUROC 80.2%、Anomaly-ShapeNet上90.0%均达SOTA。

**[3DSR: Bridging Diffusion Models and 3D Representations for 3D Consistent Super-Resolution](bridging_diffusion_models_and_3d_representations_a_3d_consis.md)**

:   提出3DSR——将扩散超分模型与3DGS表示交替迭代实现3D一致超分：每步去噪后将SR图像训练到3DGS中获得3D一致渲染→重编码回潜在空间引导下一步去噪，无需微调任何模型即显式保证跨视角一致性，在LLFF上PSNR提升1.16dB+FID降低50%(vs StableSR)。

**[Bring Your Rear Cameras for Egocentric 3D Human Pose Estimation](bring_your_rear_cameras_for_egocentric_3d_human_pose_estimat.md)**

:   首次研究HMD后置相机对全身姿态追踪的价值，提出Transformer-based多视角热力图精炼模块(利用可变形注意力+不确定性感知遮罩)，解决后视角2D关节检测不可靠的问题，并发布两个大规模数据集(Ego4View-Syn/RW)，在Ego4View-RW上MPJPE比SOTA EgoPoseFormer提升>10%(63.38→56.94mm)。

**[BUFFER-X: Towards Zero-Shot Point Cloud Registration in Diverse Scenes](bufferx_towards_zeroshot_point_cloud_registration_in_diverse.md)**

:   通过几何自适应bootstrapping确定体素大小/搜索半径、用FPS替代学习型关键点检测器、以及patch级坐标归一化，构建了一个无需人工调参即可在11个跨域数据集上实现零样本点云配准的pipeline BUFFER-X，在室内外多传感器多场景下取得了平均排名第一的成功率。

**[CAD-Recode: Reverse Engineering CAD Code from Point Clouds](cad-recode_reverse_engineering_cad_code_from_point_clouds.md)**

:   提出 CAD-Recode，将点云翻译为可执行的 Python CadQuery 代码来重建 CAD 模型，利用预训练 LLM（Qwen2-1.5B）作为解码器配合轻量级点云编码器，在 DeepCAD、Fusion360 和 CC3D 三个基准上实现了 10 倍以上的 Chamfer Distance 降低。

**[CAD-Recode: Reverse Engineering CAD Code from Point Clouds](cadrecode_reverse_engineering_cad_code_from_point_clouds.md)**

:   将CAD sketch-extrude序列表示为Python代码，利用轻量级点云投影器 + 预训练LLM解码器将点云翻译为可执行Python代码来重建CAD模型，在DeepCAD/Fusion360/真实世界CC3D数据集上显著超越现有方法，且输出代码可被通用LLM理解用于CAD编辑和问答。

**[Can3Tok: Canonical 3D Tokenization and Latent Modeling of Scene-Level 3D Gaussians](can3tok_canonical_3d_tokenization_and_latent_modeling_of_sce.md)**

:   提出Can3Tok——首个场景级3DGS VAE：通过cross-attention将大量(40K)无序3D Gaussian压缩到低维canonical token(256×768→64×64×4) + 3DGS归一化解决跨场景尺度不一致 + 语义感知过滤去除floater噪声，在DL3DV-10K上唯一成功的场景级3DGS潜在建模方法(L2=30.1, 失败率2.5%)，支持text-to-3DGS和image-to-3DGS前馈生成。

**[CATSplat: Context-Aware Transformer with Spatial Guidance for Generalizable 3D Gaussian Splatting from A Single-View Image](catsplat_contextaware_transformer_with_spatial_guidance_for.md)**

:   提出CATSplat——单视图前馈3DGS重建的泛化Transformer框架：利用VLM文本嵌入（上下文先验）和3D点云特征（空间先验）通过双重cross-attention增强图像特征，在RE10K等数据集上在PSNR/SSIM/LPIPS全面超越Flash3D，且跨数据集泛化性优异。

**[CHARM3R: Towards Unseen Camera Height Robust Monocular 3D Detector](charm3r_towards_unseen_camera_height_robust_monocular_3d_det.md)**

:   通过数学推导发现回归深度和地面深度在相机高度变化时呈现方向相反的误差趋势，CHARM3R 直接在模型内对两种深度做简单平均来抵消趋势，从而大幅提升单目3D检测器对未见相机高度的泛化能力（CARLA 上提升超过 45%）。

**[CHARM3R: Towards Unseen Camera Height Robust Monocular 3D Detector](charm3r_towards_unseen_camera_height_robust_monocular_3d_detector.md)**

:   通过数学证明回归深度和地平面深度在相机高度变化时具有相反的外推趋势，提出CHARM3R在模型内简单平均两种深度估计来抵消趋势，实现Mono3D对未见相机高度的鲁棒泛化，AP3D提升超过45%。

**[CoMoGaussian: Continuous Motion-Aware Gaussian Splatting from Motion-Blurred Images](comogaussian_continuous_motionaware_gaussian_splatting_from.md)**

:   用Neural ODE建模曝光时间内的连续相机运动轨迹，结合刚体变换和可学习的连续运动修正(CMR)变换，从运动模糊图像重建清晰3D高斯场景，在所有benchmark上大幅超越SOTA。

**[DAP-MAE: Domain-Adaptive Point Cloud Masked Autoencoder for Effective Cross-Domain Learning](dapmae_domainadaptive_point_cloud_masked_autoencoder_for_eff.md)**

:   提出一种域自适应点云MAE框架（DAP-MAE），通过异构域适配器（HDA）和域特征生成器（DFG）两个模块，让一次跨域预训练即可在物体分类、人脸表情识别、部件分割、目标检测等多个不同域的下游任务上都达到SOTA。

**[Diorama: Unleashing Zero-shot Single-view 3D Indoor Scene Modeling](diorama_unleashing_zero-shot_single-view_3d_indoor_scene_modeling.md)**

:   提出Diorama，首个零样本开放世界系统，从单张RGB图像通过模块化管线（开放世界感知+基于CAD的场景建模）生成完整的3D室内场景，包含建筑结构和物体摆放，无需端到端训练或人工标注。

**[Diorama: Unleashing Zero-shot Single-view 3D Indoor Scene Modeling](diorama_unleashing_zeroshot_singleview_3d_indoor_scene_model.md)**

:   提出首个零样本开放世界系统 Diorama，通过模块化地组合 foundation model（GPT-4o、SAM、DinoV2、Metric3D 等），将单张 RGB 图像转化为包含建筑结构和 CAD 物体的完整可组合 3D 室内场景，无需任何端到端训练或人工标注。

**[Easi3R: Estimating Disentangled Motion from DUSt3R Without Training](easi3r_estimating_disentangled_motion_from_dust3r_without_training.md)**

:   提出 Easi3R，一种无需训练的即插即用方法，通过解耦 DUSt3R 注意力层中隐含编码的相机运动与物体运动信息，实现动态视频的4D重建、运动分割和相机位姿估计。

**[EgoM2P: Egocentric Multimodal Multitask Pretraining](egom2p_egocentric_multimodal_multitask_pretraining.md)**

:   EgoM2P 是首个面向自我中心(egocentric)4D理解的多模态多任务大模型，通过时序感知的掩码建模框架统一处理 RGB 视频、深度、注视和相机轨迹四种模态，在多个下游任务上匹配或超越专用模型且快一个数量级。

**[EvaGaussians: Event Stream Assisted Gaussian Splatting from Blurry Images](evagaussians_event_stream_assisted_gaussian_splatting_from_blurry_images.md)**

:   提出EvaGaussians框架，利用事件相机的高时间分辨率事件流辅助3D高斯泼溅从运动模糊图像中学习，通过事件辅助初始化、模糊/事件联合重建损失和事件辅助几何正则化，实现高保真新视图合成并保持实时渲染效率。

**[FaceLift: Learning Generalizable Single Image 3D Face Reconstruction from Synthetic Heads](facelift_learning_generalizable_single_image_3d_face_reconstruction_from_synthet.md)**

:   提出 FaceLift，一种仅在合成数据上训练但能良好泛化到真实图像的单图360度高质量3D人头重建方法，通过多视图潜扩散模型生成身份一致的多视角图像，再用基于 Transformer 的重建器生成像素对齐的3D高斯表示。

**[Fish2Mesh Transformer: 3D Human Mesh Recovery from Egocentric Vision](fish2mesh_transformer_3d_human_mesh_recovery_from_egocentric_vision.md)**

:   提出 Fish2Mesh，一种鱼眼感知的 Transformer 模型，通过新颖的自我中心位置编码（EPE）将等距柱状投影的3D球面信息嵌入 Swin Transformer，实现从头戴式鱼眼相机图像精确恢复3D人体网格。

**[FROSS: Faster-than-Real-Time Online 3D Semantic Scene Graph Generation from RGB-D Images](fross_faster-than-real-time_online_3d_semantic_scene_graph_generation_from_rgb-d.md)**

:   提出FROSS方法，通过将2D场景图直接提升到3D空间并用高斯分布表示物体，实现了超实时（144 FPS）的在线3D语义场景图生成，无需精确点云重建。

**[Gaussian Splatting with Discretized SDF for Relightable Assets](gaussian_splatting_with_discretized_sdf_for_relightable_assets.md)**

:   本文提出将连续SDF离散化为高斯基元的额外属性，通过SDF-to-opacity变换统一高斯和SDF表示，配合投影一致性损失和球面初始化，在仅用4G显存的前提下实现了超越现有高斯逆渲染方法的重光照质量。

**[GUAVA: Generalizable Upper Body 3D Gaussian Avatar](guava_generalizable_upper_body_3d_gaussian_avatar.md)**

:   提出 GUAVA，首个从单张图像通过前馈推理快速重建可动画上半身3D高斯虚拟人的框架，结合模板高斯和 UV 高斯表示，支持丰富面部表情和手势驱动，约0.1s完成重建并实时渲染。

**[Hierarchical Material Recognition from Local Appearance](hierarchical_material_recognition_from_local_appearance.md)**

:   提出面向视觉应用的层级式材质分类学体系(taxonomy)与野外数据集 Matador（含深度图的 ~7200 张材质图像，57类），并基于图注意力网络(GAT)利用分类学的层级亲缘关系进行材质识别，在多个基准数据集上达到 SOTA，同时支持新材质的小样本学习和场景中任意点的材质探测。

**[Image-Guided Shape-from-Template Using Mesh Inextensibility Constraints](image-guided_shape-from-template_using_mesh_inextensibility_constraints.md)**

:   提出一种纯图像引导的无监督 Shape-from-Template (SfT) 方法，仅利用颜色、梯度和轮廓等视觉线索配合网格不可伸展性约束来重建变形物体 3D 形状，比最优无监督方法快 400 倍且精度大幅领先。

**[Image as an IMU: Estimating Camera Motion from a Single Motion-Blurred Image](image_as_an_imu_estimating_camera_motion_from_a_single_motion-blurred_image.md)**

:   本文将运动模糊从"不需要的伪影"转变为"有价值的运动线索"，通过从单张模糊图像预测稠密光流场和单目深度图，再用可微分最小二乘求解器恢复相机6DoF瞬时速度，实现媲美甚至超越IMU的运动估计精度和30FPS实时性能。

**[Learning 3D Object Spatial Relationships from Pre-trained 2D Diffusion Models](learning_3d_object_spatial_relationships_from_pre-trained_2d_diffusion_models.md)**

:   提出从预训练 2D 扩散模型合成图像中学习物体间 3D 空间关系（OOR），通过 3D 提升管线构建配对数据集，训练文本条件化的 score-based 扩散模型对物体对的相对位姿和尺度分布建模，并扩展至多物体场景布局和场景编辑。

**[Learning 3D Scene Analogies with Neural Contextual Scene Maps](learning_3d_scene_analogies_with_neural_contextual_scene_maps.md)**

:   提出3D场景类比任务，通过神经上下文场景映射（neural contextual scene maps）在共享相似语义上下文的场景区域间建立稠密三维映射，支持轨迹迁移与物体放置迁移等下游应用。

**[TesserAct: Learning 4D Embodied World Models](learning_4d_embodied_world_models.md)**

:   提出 TesserAct——一种 4D 具身世界模型，通过训练视频生成模型联合预测 RGB、深度和法线视频，再转换为高质量 4D 场景，实现空间-时间一致的 3D 世界动态模拟和机器人动作规划。

**[LocalDyGS: Multi-view Global Dynamic Scene Modeling via Adaptive Local Implicit Feature Decoupling](localdygs_multi-view_global_dynamic_scene_modeling_via_adaptive_local_implicit_f.md)**

:   提出 LocalDyGS——将全局复杂动态场景分解为种子点定义的局部空间、并通过静态-动态特征解耦生成时序高斯来建模各局部运动的框架，首次实现了大尺度复杂动态场景的高质量重建。

**[LONG3R: Long Sequence Streaming 3D Reconstruction](long3r_long_sequence_streaming_3d_reconstruction.md)**

:   提出 LONG3R，一种基于循环记忆机制的流式多视图3D重建模型，通过记忆门控、双源精炼解码器和3D时空记忆三大创新，在保持实时推理速度的同时显著提升长序列重建质量。

**[MaterialMVP: Illumination-Invariant Material Generation via Multi-view PBR Diffusion](materialmvp_illumination-invariant_material_generation_via_multi-view_pbr_diffus.md)**

:   MaterialMVP 是一个端到端的多视图 PBR 纹理生成模型，通过参考注意力、一致性正则化训练和双通道材质生成框架，从3D网格和图像提示生成光照不变且多视图一致的高质量 PBR 材质。

**[Monocular Semantic Scene Completion via Masked Recurrent Networks](monocular_semantic_scene_completion_via_masked_recurrent_networks.md)**

:   提出 MonoMRN，一个两阶段单目语义场景补全框架：先做粗粒度预测，再用 Masked Sparse GRU（MS-GRU）循环精炼被遮挡区域，并引入距离注意力投影减少深度投影误差，在 NYUv2 和 SemanticKITTI 上均达到 SOTA。

**[MonoMobility: Zero-Shot 3D Mobility Analysis from Monocular Videos](monomobility_zero-shot_3d_mobility_analysis_from_monocular_videos.md)**

:   MonoMobility 提出首个从单目视频零样本分析关节物体运动部件及运动属性（运动轴、运动类型）的框架，通过2D高斯泼溅场景表示和端到端动态场景优化算法，无需标注数据即可处理旋转、平移及复合运动。

**[MuGS: Multi-Baseline Generalizable Gaussian Splatting Reconstruction](mugs_multi-baseline_generalizable_gaussian_splatting_reconstruction.md)**

:   MuGS 是首个支持多基线设置（小基线到大基线）的泛化3D高斯泼溅方法，通过融合 MVS 和 MDE 特征、投影-采样深度一致性网络和参考视图损失，在不同基线数据集上均达到 SOTA。

**[Multi-View 3D Point Tracking](multi-view_3d_point_tracking.md)**

:   提出 MVTracker——首个数据驱动的多视角3D点跟踪器，通过将多视图深度图反投影为统一的3D特征点云，利用 kNN 关联和 Transformer 迭代优化，在仅需4个相机的实用配置下实现鲁棒的长程3D点轨迹估计，在 Panoptic Studio 和 DexYCB 上分别达到 3.1 cm 和 2.0 cm 的中位轨迹误差。

**[MV-Adapter: Multi-view Consistent Image Generation Made Easy](mv-adapter_multi-view_consistent_image_generation_made_easy.md)**

:   提出首个基于Adapter的多视角图像生成方案MV-Adapter，通过复制self-attention层+并行注意力架构实现即插即用的多视角生成，在SDXL上达到768分辨率，兼容各种T2I衍生模型。

**[Not All Frame Features Are Equal: Video-to-4D Generation via Decoupling Dynamic-Static Features](not_all_frame_features_are_equal_video-to-4d_generation_via_decoupling_dynamic-s.md)**

:   DS4D 首次提出在video-to-4D生成中沿时间轴和空间轴解耦动静态特征，通过动静态特征解耦模块（DSFD）获取动态表征，并通过时空相似性融合模块（TSSF）跨视角自适应聚合动态信息，在Consistent4D和Objaverse数据集上达到SOTA。

**[Online Language Splatting](online_language_splatting.md)**

:   首个在 3DGS-SLAM 系统中实现**在线、近实时、开放词汇**语言建图的框架，通过高分辨率 CLIP 嵌入、两阶段在线自编码器压缩和颜色-语言解耦优化三项创新，在精度超越离线 SOTA 的同时实现 40×–200× 的效率提升。

**[PanSt3R: Multi-view Consistent Panoptic Segmentation](panst3r_multi-view_consistent_panoptic_segmentation.md)**

:   基于MUSt3R构建PanSt3R，在**单次前向传播**中同时完成3D重建和多视角全景分割，无需相机参数、无需测试时优化，比现有方法快数个量级。

**[PCR-GS: COLMAP-Free 3D Gaussian Splatting via Pose Co-Regularizations](pcr-gs_colmap-free_3d_gaussian_splatting_via_pose_co-regularizations.md)**

:   提出 PCR-GS，通过 DINO 特征重投影正则化和基于小波变换的频率正则化对相机位姿进行协同约束，在无需 COLMAP 先验的条件下实现了复杂相机轨迹场景的高质量 3D-GS 重建与位姿估计。

**[PolarAnything: Diffusion-based Polarimetric Image Synthesis](polaranything_diffusion-based_polarimetric_image_synthesis.md)**

:   提出 PolarAnything，首个基于单张 RGB 图像生成偏振图像的扩散模型框架，通过对编码后的 AoLP 和 DoLP 进行去噪扩散，实现了物理准确且逼真的偏振属性合成，无需 3D 资产或偏振相机。

**[PseudoMapTrainer: Learning Online Mapping without HD Maps](pseudomaptrainer_learning_online_mapping_without_hd_maps.md)**

:   提出 PseudoMapTrainer，首次实现**完全不依赖 GT HD Map** 训练在线建图模型：利用 2D Gaussian Splatting（RoGS）从多视角相机图像重建道路表面并结合预训练语义分割（Mask2Former）生成矢量化伪标签，同时设计 mask-aware 匹配算法与损失函数处理部分遮挡的伪标签，支持单次行程和多次行程（众包数据）两种模式。

**[RobuSTereo: Robust Zero-Shot Stereo Matching under Adverse Weather](robustereo_robust_zero-shot_stereo_matching_under_adverse_weather.md)**

:   提出 RobuSTereo 框架，通过基于扩散模型的立体数据生成管线和结合去噪 ViT 与 VGG19 的鲁棒特征编码器，大幅提升立体匹配模型在雨、雾、雪等恶劣天气下的零样本泛化能力。

**[RoCo-Sim: Enhancing Roadside Collaborative Perception through Foreground Simulation](roco-sim_enhancing_roadside_collaborative_perception_through_foreground_simulati.md)**

:   RoCo-Sim 是首个面向路侧协同感知的仿真框架，通过相机外参优化、多视图遮挡感知采样、DepthSAM 深度渲染和可扩展后处理工具包，从单张图像生成多样且多视图一致的路侧仿真数据，将路侧3D检测性能提升 83%+。

**[Ross3D: Reconstructive Visual Instruction Tuning with 3D-Awareness](ross3d_reconstructive_visual_instruction_tuning_with_3d-awareness.md)**

:   Ross3D 提出将3D感知的视觉重建预训练任务（跨视图重建 + 全局BEV重建）注入2D大型多模态模型的训练流程中，在不修改输入表示的前提下通过输出级监督信号显著提升3D场景理解能力，在SQA3D、ScanQA、Scan2Cap、ScanRefer、Multi3DRefer五个基准上均达到SOTA。

**[Scene Coordinate Reconstruction Priors](scene_coordinate_reconstruction_priors.md)**

:   提出场景坐标回归(SCR)的概率化训练框架，引入手工设计的深度分布先验和基于3D点云扩散模型的学习先验，在多视角约束不足时显著改善场景重建质量、相机位姿估计和下游任务表现。

**[SeHDR: Single-Exposure HDR Novel View Synthesis via 3D Gaussian Bracketing](sehdr_single-exposure_hdr_novel_view_synthesis_via_3d_gaussian_bracketing.md)**

:   SeHDR 是首个从单曝光多视图 LDR 图像生成 HDR 新视角的3DGS框架，通过在3D空间扩展包围曝光原理（Bracketed 3D Gaussians）并设计可微分神经曝光融合（NeEF）在球谐空间融合，无需 HDR 监督即超越现有方法 14.3dB。

**[SHeaP: Self-Supervised Head Geometry Predictor Learned via 2D Gaussians](sheap_self-supervised_head_geometry_predictor_learned_via_2d_gaussians.md)**

:   提出SHeaP，利用2D Gaussian Splatting替代传统可微mesh渲染进行自监督3DMM预测训练，通过将Gaussians绑定到3DMM mesh上实现重动画，并设计graph卷积Gaussians生成器和几何一致性正则化，在NoW和Nersemble基准上超越所有自监督方法。

**[Sparfels: Fast Reconstruction from Sparse Unposed Imagery](sparfels_fast_reconstruction_from_sparse_unposed_imagery.md)**

:   提出Sparfels方法，将3D基础模型（MASt3R）与高效的测试时优化（2DGS）相结合，通过MASt3R提供初始化点云/相机和对应关系引导优化，并创新性地引入泼溅色彩方差损失，在3分钟内从稀疏无位姿图像实现SOTA几何重建。

**[Spatial-Temporal Aware Visuomotor Diffusion Policy Learning](spatial-temporal_aware_visuomotor_diffusion_policy_learning.md)**

:   提出 4D Diffusion Policy（DP4），通过动态高斯世界模型为扩散策略注入3D空间和4D时空感知能力，在17个仿真任务和3个真实机器人任务上大幅超越基线（Adroit +16.4%, DexArt +14%, RLBench +6.45%, 真实任务 +8.6%）。

**[SpinMeRound: Consistent Multi-View Identity Generation Using Diffusion Models](spinmeround_consistent_multi-view_identity_generation_using_diffusion_models.md)**

:   提出 SpinMeRound，一种基于身份嵌入的多视角扩散模型，能从单张或少量人脸图像生成 360° 全头部一致性肖像及对应法线图，在人脸新视角合成任务上超越现有多视角扩散方法。

**[Stable Score Distillation](stable_score_distillation.md)**

:   提出 Stable Score Distillation (SSD)，通过单分类器跨提示词引导和 null-text 分支的跨轨迹正则化，实现更稳定精准的文本引导 2D/3D 编辑，在保持源内容结构的同时提升编辑对齐度。

**[StealthAttack: Robust 3D Gaussian Splatting Poisoning via Density-Guided Illusions](stealthattack_robust_3d_gaussian_splatting_poisoning_via_density-guided_illusion.md)**

:   首次针对3D高斯泼溅(3DGS)提出密度引导的投毒攻击方法，通过在低密度区域注入幻觉物体的高斯点并引入自适应噪声破坏多视角一致性，实现从目标视角清晰可见而不干扰其余视角的隐蔽攻击。

**[Stereo Any Video: Temporally Consistent Stereo Matching](stereo_any_video_temporally_consistent_stereo_matching.md)**

:   提出Stereo Any Video框架，通过融合单目视频深度基础模型先验(Video Depth Anything)、全对全配对相关(all-to-all-pair correlation)和时序凸上采样(temporal convex upsampling)三大核心模块，在不依赖相机位姿或光流的前提下实现空间精确且时序一致的视频立体匹配，在多个数据集零样本设定下达到SOTA。

**[TAR3D: Creating High-Quality 3D Assets via Next-Part Prediction](tar3d_creating_high-quality_3d_assets_via_next-part_prediction.md)**

:   提出TAR3D框架——首次将三平面表示量化为离散几何部件并用GPT自回归生成，通过3D VQ-VAE编码任意面数网格为固定长度序列+TriPE位置编码保留3D空间信息，在文本/图像→3D任务上全面超越现有方法。

**[TokenUnify: Scaling Up Autoregressive Pretraining for Neuron Segmentation](tokenunify_scaling_up_autoregressive_pretraining_for_neuron_segmentation.md)**

:   提出 TokenUnify，通过统一随机 token 预测、下一 token 预测和下一全部 token 预测三种互补学习目标，在大规模电子显微镜数据上实现层次化预测编码，将自回归误差累积从 O(K) 降至 O(√K)，下游神经元分割提升 44%。

**[Trace3D: Consistent Segmentation Lifting via Gaussian Instance Tracing](trace3d_consistent_segmentation_lifting_via_gaussian_instance_tracing.md)**

:   提出Gaussian Instance Tracing (GIT)机制，通过反向光栅化为每个高斯核维护跨视角的实例权重矩阵，统一解决2D分割多视角不一致和边界高斯模糊两大问题，在离线对比学习和在线自提示两种设定下均显著提升3D分割质量。

**[TRACE: Learning 3D Gaussian Physical Dynamics from Multi-view Videos](trace_learning_3d_gaussian_physical_dynamics_from_multi-view_videos.md)**

:   提出TRACE框架，将每个3D高斯核视为刚性粒子并为其学习独立的平移-旋转动力学系统（包含速度、加速度、角速度、角加速度等完整物理参数），无需任何人工标注即可从多视角动态视频中学习3D场景的物理运动规律并准确外推未来帧。

**[TriDi: Trilateral Diffusion of 3D Humans, Objects, and Interactions](tridi_trilateral_diffusion_of_3d_humans_objects_and_interactions.md)**

:   提出 TriDi，首个建模人体(H)、物体(O)和交互(I)三变量联合分布的统一扩散模型，一个网络覆盖 7 种条件生成模式，超越各专用单向基线。

**[VoluMe: Authentic 3D Video Calls from Live Gaussian Splat Prediction](volume_-_authentic_3d_video_calls_from_live_gaussian_splat_prediction.md)**

:   微软提出首个从单目2D摄像头实时预测3D高斯泼溅重建的方法，实现真实感、保真性、实时性和时序稳定性四项要求的统一，使任何人仅用标准笔记本摄像头即可进行体积3D视频通话。

**[Zero-Shot Inexact CAD Model Alignment from a Single Image](zero-shot_inexact_cad_model_alignment_from_a_single_image.md)**

:   提出一种弱监督的9-DoF CAD模型对齐方法，通过增强DINOv2特征的几何感知能力并在归一化物体坐标（NOC）空间进行稠密对齐优化，实现无需位姿标注、可泛化到未见类别的零样本3D对齐。

**[ZeroStereo: Zero-shot Stereo Matching from Single Images](zerostereo_zero-shot_stereo_matching_from_single_images.md)**

:   提出 ZeroStereo 管线：从任意单张图像出发，利用单目深度估计生成伪视差，再用微调的扩散修复模型合成高质量右视图，实现只需 35K 合成数据即达到 SOTA 零样本立体匹配泛化性能。
