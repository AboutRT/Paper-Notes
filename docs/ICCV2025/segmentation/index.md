<!-- 由 src/gen_blog_index.py 自动生成 -->
# ✂️ 语义分割

**📹 ICCV2025** · 共 **17** 篇

**[2HandedAfforder: Learning Precise Actionable Bimanual Affordances from Human Videos](2handedafforder_learning_precise_actionable_bimanual_affordances_from_human_vide.md)**

:   本文提出从人类活动视频中自动提取精确的双手可操作区域(affordance)数据集 2HANDS，并训练基于 VLM 的 2HandedAfforder 模型，实现根据文本提示预测双手抓握的精确物体区域分割，在新提出的 ActAffordance 基准上显著优于现有方法。

**[A Plug-and-Play Physical Motion Restoration Approach for In-the-Wild High-Difficulty Motions](a_plugandplay_physical_motion_restoration_approach_for_inthe.md)**

:   提出即插即用的物理运动修复框架，通过Mask条件运动校正模块（MCM）修复视频运动捕捉中的缺陷帧，结合基于RL测试时适应的物理运动传输模块（PTM），首次实现对野外高难度运动（如体操、武术后空翻）的物理仿真修复。

**[Auto-Vocabulary Semantic Segmentation](auto-vocabulary_semantic_segmentation.md)**

:   本文提出 Auto-Vocabulary Semantic Segmentation (AVS) 新任务，通过 AutoSeg 框架自动从图像中发现目标类别并分割，无需人为指定词汇表，在 PASCAL VOC 上达到 87.1 mIoU，远超唯一同类方法 ZeroSeg (20.1)，甚至超越部分需要指定类别的开放词汇方法。

**[Beyond Single Images: Retrieval Self-Augmented Unsupervised Camouflaged Object Detection](beyond_single_images_retrieval_self-augmented_unsupervised_camouflaged_object_de.md)**

:   本文提出 RISE——一种检索自增强的无监督伪装目标检测范式，通过从训练集本身构建前景/背景原型库并利用 KNN 检索生成伪标签，在无任何标注的条件下大幅超越现有无监督和基于提示的方法。

**[CAVIS: Context-Aware Video Instance Segmentation](cavis_context-aware_video_instance_segmentation.md)**

:   提出CAVIS，通过引入上下文感知实例追踪器（CAIT）融合物体边界周围的上下文信息来增强实例关联，并设计原型化跨帧对比损失（PCC）保证跨帧特征一致性，在VIS和VPS任务上全面刷新SOTA。

**[CorrCLIP: Reconstructing Patch Correlations in CLIP for Open-Vocabulary Semantic Segmentation](corrclip_reconstructing_patch_correlations_in_clip_for_openv.md)**

:   揭示CLIP用于分割时patch间"类间相关性"是性能瓶颈的根本原因，提出CorrCLIP通过SAM限制patch交互范围（scope reconstruction）+DINO计算更一致的相似度值（value reconstruction）+空间/语义特征增强+SAM mask后处理，在8个benchmark上training-free方法平均mIoU从48.6%提升到53.6%。

**[Correspondence as Video: Test-Time Adaption on SAM2 for Reference Segmentation in the Wild](correspondence_as_video_testtime_adaption_on_sam2_for_refere.md)**

:   将reference-target图像对之间的对应关系表示为用扩散模型生成的伪视频序列，利用SAM2的iVOS能力进行分割，结合test-time轻量微调对齐几何变化，在跨域few-shot分割上比SOTA方法提升约5% mIoU，且无需meta-training。

**[E-SAM: Training-Free Segment Every Entity Model](e-sam_training-free_segment_every_entity_model.md)**

:   E-SAM 是一个无需额外训练的框架，通过三个级联模块——多层级掩码生成（MMG）、实体级掩码精炼（EMR）和欠分割修复（USR）——系统性地解决 SAM 自动掩码生成（AMG）中的过分割和欠分割问题，在基准指标上超越现有实体分割方法 **+30.1 分**。

**[FLOSS: Free Lunch in Open-vocabulary Semantic Segmentation](floss_free_lunch_in_openvocabulary_semantic_segmentation.md)**

:   挑战OVSS中"平均80个模板"的默认做法，发现每个类别存在特定的"专家模板"（class-expert）远优于平均分类器，提出用预测熵无监督选择专家模板+融合专家预测的FLOSS方法，在不需要标签和训练的情况下一致提升现有OVSS方法。

**[Hybrid-TTA: Continual Test-time Adaptation via Dynamic Domain Shift Detection](hybrid-tta_continual_test-time_adaptation_via_dynamic_domain_shift_detection.md)**

:   Hybrid-TTA 提出一种持续测试时自适应（CTTA）框架，通过动态域偏移检测（DDSD）模块判断当前输入是否来自新域，自适应地在全参数微调（Full Tuning）和高效微调（Adapter Tuning）之间切换；同时引入掩码图像建模自适应（MIMA）作为辅助任务增强模型稳定性，在 Cityscapes-to-ACDC 基准上达到 62.2% mIoU，且推理速度比可比方法快约 **20 倍**。

**[LawDIS: Language-Window-based Controllable Dichotomous Image Segmentation](lawdis_language-window-based_controllable_dichotomous_image_segmentati.md)**

:   提出LawDIS，一种基于Stable Diffusion的语言-窗口双控可控二分图像分割框架，在宏观模式下通过语言提示指导目标分割，在微观模式下通过可变尺寸窗口精细化局部细节，在DIS5K上全面超越11种SOTA方法。

**[LawDIS: Language-Window-based Controllable Dichotomous Image Segmentation](lawdis_language-window-based_controllable_dichotomous_image_segmentation.md)**

:   提出 LawDIS，一个基于潜在扩散模型的可控二分图像分割框架，通过宏观语言控制（LS）和微观窗口细化（WR）两种模式的协同，实现高质量前景目标掩码生成，在 DIS5K 基准上全面超越 11 种 SOTA 方法。

**[MOVE: Motion-Guided Few-Shot Video Object Segmentation](move_motion-guided_few-shot_video_object_segmentation.md)**

:   本文提出运动引导的少样本视频目标分割新任务及大规模数据集 MOVE（224 类运动、4300 视频、314K mask），并设计解耦运动-外观网络 DMA，通过帧差提取运动原型+外观原型的双分支架构，在新基准上显著优于现有 FSVOS 方法。

**[Online Generic Event Boundary Detection](online_generic_event_boundary_detection.md)**

:   本文提出在线通用事件边界检测（On-GEBD）这一新任务——在流式视频中实时检测事件边界，并设计了基于认知科学事件分割理论（EST）的 ESTimator 框架，通过一致事件预测器（CEA）和在线边界判别器（OBD）的协同，在 Kinetics-GEBD 上 Avg F1 达到 0.748，超越所有在线基线且接近离线方法的性能。

**[RAGNet: Large-scale Reasoning-based Affordance Segmentation Benchmark towards General Grasping](ragnet_large-scale_reasoning-based_affordance_segmentation_benchmark_towards_gen.md)**

:   构建了首个大规模推理式 affordance 分割基准 RAGNet（273k 图像、180 类别、26k 推理指令），并提出 AffordanceNet 框架，将 VLM 预训练的 affordance 预测与抓取姿态生成相结合，展现出强大的开放世界泛化和推理能力。

**[SAM2Long: Enhancing SAM 2 for Long Video Segmentation with a Training-Free Memory Tree](sam2long_enhancing_sam_2_for_long_video_segmentation_with_a.md)**

:   针对SAM 2在长视频中因贪心选择策略导致的错误累积问题，提出一种training-free的约束树搜索记忆策略，维护多条分割路径并在视频级别选择最优结果，在9个VOS和3个VOT benchmark上平均提升3.7 J&F，长视频场景最高提升5.3。

**[SCORE: Scene Context Matters in Open-Vocabulary Remote Sensing Instance Segmentation](score_scene_context_matters_in_openvocabulary_remote_sensing.md)**

:   提出SCORE框架，通过引入区域上下文（RAI）和全局上下文适配（GCA）两个模块，将遥感专用CLIP的多粒度场景知识注入到开放词汇实例分割pipeline中，在多个遥感数据集上的跨数据集评估中平均mAP超越前SOTA 5.53%。
