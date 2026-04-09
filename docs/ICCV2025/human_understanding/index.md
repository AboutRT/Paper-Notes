<!-- 由 src/gen_blog_index.py 自动生成 -->
# 🧑 人体理解

**📹 ICCV2025** · 共 **8** 篇

**[A Quality-Guided Mixture of Score-Fusion Experts Framework for Human Recognition](a_qualityguided_mixture_of_scorefusion_experts_framework_for.md)**

:   提出 Quality-guided Mixture of score-fusion Experts (QME) 框架，通过质量引导的 MoE 策略对来自不同生物特征模态（人脸、步态、身体）的相似度分数进行可学习融合，配合伪质量损失和分数三元组损失，在多个全身生物特征识别基准上达到 SOTA。

**[Avat3r: Large Animatable Gaussian Reconstruction Model for High-fidelity 3D Head Avatars](avat3r_large_animatable_gaussian_reconstruction_model_for_hi.md)**

:   提出Avat3r——首个可动画的大型3D重建模型(LRM)，仅需4张输入图像即可在前馈方式下回归出高质量可驱动的3D高斯头部头像，通过整合DUSt3R位置图和Sapiens语义特征作为先验、并用简单的cross-attention建模表情动画，在Ava256和NeRSemble数据集上大幅超越现有方法。

**[CarGait: Cross-Attention based Re-ranking for Gait Recognition](cargait_crossattention_based_reranking_for_gait_recognition.md)**

:   提出CarGait——基于cross-attention的步态识别重排序方法：对任意单阶段步态模型的top-K检索结果，通过probe与候选间步态条带(gait strip)的cross-attention学习细粒度pair-wise交互，生成新的条件化表征并重新计算距离进行重排序。在Gait3D/GREW/OU-MVLP三个数据集、7种基线模型上一致提升Rank-1/5准确率，推理速度6.5ms/probe远超现有重排序方法。

**[Hi3DGen: High-fidelity 3D Geometry Generation from Images via Normal Bridging](hi3dgen_high-fidelity_3d_geometry_generation_from_images_via_normal_bridging.md)**

:   提出 Hi3DGen 框架，以法线图作为中间表示桥接 2D 图像到 3D 几何的映射，通过噪声注入回归式法线估计器（NiRNE）和法线正则化潜在扩散（NoRLD）两大核心组件，显著提升生成 3D 模型的几何细节保真度。

**[Multi-view Gaze Target Estimation](multi-view_gaze_target_estimation.md)**

:   本文首次将注视目标估计（GTE）从单视角扩展到多视角，通过头部信息聚合（HIA）、基于不确定性的注视选择（UGS）和基于极线的场景注意力（ESA）三个模块融合多相机信息，在自建 MVGT 数据集上显著超越单视角 SOTA，并实现了单视角方法无法处理的跨视角估计。

**[NegRefine: Refining Negative Label-Based Zero-Shot OOD Detection](negrefine_refining_negative_label-based_zero-shot_ood_detection.md)**

:   本文提出 NegRefine，通过 LLM 过滤负标签集中的专有名词和子类别标签，并设计多标签匹配评分函数来处理图像同时匹配分布内和负标签的情况，在 ImageNet-1K 基准上平均 AUROC 提升 1.82%、FPR95 降低 4.35%，刷新了零样本 OOD 检测 SOTA。

**[Neural Multi-View Self-Calibrated Photometric Stereo without Photometric Stereo Cues](neural_multi-view_self-calibrated_photometric_stereo_without_photometric_stereo_.md)**

:   提出一种端到端的神经逆渲染框架，从多视图变化光照图像中联合恢复几何、空间变化反射率和光照参数，无需光源标定或中间光度立体线索（如法线图），超越了现有的分阶段 MVPS 方法。

**[SignRep: Enhancing Self-Supervised Sign Representations](signrep_enhancing_self-supervised_sign_representations.md)**

:   提出 SignRep，一个可扩展的自监督手语表征学习框架，通过在 Masked Autoencoder 预训练中利用手语骨架先验、特征正则化和对抗式风格无关损失，仅用单一 RGB 模态即超越了复杂的多模态/多分支方法，在手语识别、字典检索和手语翻译三大任务上均取得 SOTA。
