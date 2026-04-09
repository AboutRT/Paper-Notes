<!-- 由 src/gen_blog_index.py 自动生成 -->
# 🎯 目标检测

**📹 ICCV2025** · 共 **10** 篇

**[3D-MOOD: Lifting 2D to 3D for Monocular Open-Set Object Detection](3dmood_lifting_2d_to_3d_for_monocular_openset_object_detecti.md)**

:   提出首个端到端的单目开放集3D目标检测器3D-MOOD，通过将开放集2D检测"提升"到3D空间，结合几何感知3D query生成与canonical image space设计，在Omni3D闭集和Argoverse 2/ScanNet开集基准上均达到SOTA。

**[Augmenting Moment Retrieval: Zero-Dependency Two-Stage Learning](augmenting_moment_retrieval_zero-dependency_two-stage_learning.md)**

:   提出 AMR 框架，通过 Splice-and-Boost 数据增强策略和冷启动-蒸馏两阶段训练，在不依赖任何外部数据/预训练模型的前提下，大幅提升视频时刻检索的边界感知能力和语义辨别力，在 QVHighlights 上超越 SOTA +5%。

**[DiffDoctor: Diagnosing Image Diffusion Models Before Treating](diffdoctor_diagnosing_image_diffusion_models_before_treating.md)**

:   提出 DiffDoctor，首个利用像素级反馈微调扩散模型的方法：先训练鲁棒的 artifact 检测器（1M+ 样本，类别平衡策略），再通过最小化合成图中每个像素的 artifact 置信度反向传播梯度到扩散模型，使其在未见 prompt 上也能显著减少 artifact 生成。

**[Dynamic-DINO: Fine-Grained Mixture of Experts Tuning for Real-time Open-Vocabulary Object Detection](dynamicdino_finegrained_mixture_of_experts_tuning_for_realti.md)**

:   首次将Mixture of Experts引入实时开放词汇目标检测器，通过MoE-Tuning将Grounding DINO 1.5 Edge从dense模型扩展为动态推理框架，提出细粒度专家分解和预训练权重分配策略，仅用1.56M开源数据超越使用20M私有数据训练的原版模型。

**[EA-KD: Entropy-based Adaptive Knowledge Distillation](ea-kd_entropy-based_adaptive_knowledge_distillation.md)**

:   提出 EA-KD，一种基于信息熵的即插即用知识蒸馏方法：通过结合 teacher 和 student 输出的熵值动态重加权蒸馏损失，优先学习高熵（高信息量）样本，在图像分类、目标检测和 LLM 蒸馏任务上均一致提升多种 KD 框架的性能，且计算开销可忽略。

**[SFUOD: Source-Free Unknown Object Detection](sfuod_source-free_unknown_object_detection.md)**

:   提出 Source-Free Unknown Object Detection (SFUOD) 新场景，并设计 CollaPAUL 框架，通过协作调优融合源域和目标域知识 + 基于主轴的未知物体伪标签分配，在无源数据条件下同时检测已知和未知物体。

**[ViewSRD: 3D Visual Grounding via Structured Multi-View Decomposition](viewsrd_3d_visual_grounding_via_structured_multi-view_decomposition.md)**

:   提出 ViewSRD 框架，将 3D 视觉定位建模为结构化多视角分解过程：通过 SRD 模块将复杂多锚点查询解耦为简单单锚点查询，并引入跨模态一致视角 token (CCVT) 解决视角变化导致的空间描述不一致问题。

**[VisRL: Intention-Driven Visual Perception via Reinforced Reasoning](visrl_intention-driven_visual_perception_via_reinforced_reasoning.md)**

:   VisRL是首个将强化学习应用于意图驱动视觉感知的框架，通过迭代DPO训练让大多模态模型学会根据查询意图自主选择关注区域（预测bounding box），无需昂贵的中间bounding box标注即可实现比SFT更强的视觉推理能力。

**[Visual-RFT: Visual Reinforcement Fine-Tuning](visual-rft_visual_reinforcement_fine-tuning.md)**

:   Visual-RFT将DeepSeek R1的强化学习+可验证奖励(RLVR)范式从数学/代码领域扩展到视觉感知任务，设计了IoU奖励（目标检测）和CLS奖励（分类）等任务特异的可验证奖励函数，在细粒度分类、少样本检测、推理定位等任务上以极少数据大幅超越SFT。

**[YOLOE: Real-Time Seeing Anything](yoloe_realtime_seeing_anything.md)**

:   提出YOLOE，在YOLO架构中统一支持文本提示、视觉提示和无提示三种开放场景的检测和分割，通过RepRTA（可重参数化区域-文本对齐）、SAVPE（语义激活视觉提示编码器）和LRPC（懒惰区域-提示对比）三个设计实现高效率高性能，以3x更少的训练成本在LVIS上超越YOLO-World v2。
