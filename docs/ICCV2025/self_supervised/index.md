<!-- 由 src/gen_blog_index.py 自动生成 -->
# 🔄 自监督/表示学习

**📹 ICCV2025** · 共 **12** 篇

**[A Token-level Text Image Foundation Model for Document Understanding (TokenFD/TokenVL)](a_tokenlevel_text_image_foundation_model_for_document_unders.md)**

:   提出首个 token 级别文本图像基础模型 TokenFD，通过在 2000 万图像、18 亿 BPE token-mask 对上进行 token 级视觉-语言对齐预训练，实现 image-as-text 语义能力，并基于此构建文档理解 MLLM TokenVL，在 OCRBench 上得分 860（8B 组最高），在 DocVQA 等十项 VQA 任务上平均提升 8.8%。

**[AIM: Amending Inherent Interpretability via Self-Supervised Masking](aim_amending_inherent_interpretability_via_self-supervised_masking.md)**

:   本文提出 AIM，一种基于自监督二值掩码的 top-down 特征选择机制，无需额外标注即可引导 CNN 聚焦真实判别特征、抑制虚假相关，同时获得内在可解释性和更强的 OOD 泛化能力。

**[Aligning Moments in Time using Video Queries](aligning_moments_in_time_using_video_queries.md)**

:   提出MATR（Moment Alignment TRansformer），通过双阶段序列对齐机制和自监督预训练策略实现视频到视频的时刻检索（Vid2VidMR），在ActivityNet-VRL上R@1和mIoU分别提升13.1%和8.1%（绝对值），并构建了新的体育领域数据集SportsMoments。

**[Always Skip Attention](always_skip_attention.md)**

:   本文从理论上证明了 Vision Transformer 中的自注意力机制是本质上病态的（ill-conditioned），在无 skip connection 时会导致训练崩溃，并提出 Token Graying（TG）方法通过改善输入 token 的条件数来进一步增强 ViT 的训练稳定性和性能。

**[CObL: Toward Zero-Shot Ordinal Layering without User Prompting](cobl_toward_zero-shot_ordinal_layering_without_user_prompting.md)**

:   本文提出 CObL，一种基于多个冻结 Stable Diffusion UNet 并行生成的架构，能在无需用户提示、不知物体数量的前提下，从单张图像推断出遮挡排序的物体层叠表示（每层一个 amodal 完整物体），并且仅用数千张合成桌面场景就能零样本泛化到真实世界照片。

**[From Linearity to Non-Linearity: How Masked Autoencoders Capture Spatial Correlations](from_linearity_to_non-linearity_how_masked_autoencoders_capture_spatial_correlat.md)**

:   从理论角度分析 MAE 如何学习图像中的空间相关性，推导出线性 MAE 的解析解，揭示了掩码比例和 patch 大小如何选择短距离和长距离空间特征，并将分析扩展到非线性 MAE，为实践中的超参数选择提供了理论指导。

**[Gradient Extrapolation for Debiased Representation Learning](gradient_extrapolation_for_debiased_representation_learning.md)**

:   提出 GERNE 方法，通过构建具有不同虚假相关程度的两个 batch 并对其梯度进行线性外推，引导模型学习去偏差表征，在已知和未知属性情况下均优于 SOTA。

**[LoftUp: Learning a Coordinate-Based Feature Upsampler for Vision Foundation Models](loftup_learning_a_coordinatebased_feature_upsampler_for_visi.md)**

:   提出LoftUp，通过坐标-cross-attention架构直接将低分辨率VFM特征映射到任意高分辨率，并用class-agnostic mask精炼+自蒸馏构建全分辨率伪GT进行训练，在6个下游任务上平均提升10-20%且在视频目标分割上提升近50%。

**[Manual-PA: Learning 3D Part Assembly from Instruction Diagrams](manual-pa_learning_3d_part_assembly_from_instruction_diagrams.md)**

:   提出 Manual-PA，一个基于 Transformer 的说明书引导 3D 零件组装框架：通过对比学习将 3D 零件与说明书步骤图对齐来推断组装顺序，再以学到的顺序作为位置编码的软引导进行 6DoF 位姿预测，在 PartNet 上显著超越现有方法。

**[MoSiC: Optimal-Transport Motion Trajectory for Dense Self-Supervised Learning](mosic_optimal-transport_motion_trajectory_for_dense_self-supervised_learning.md)**

:   MoSiC 利用离线点跟踪器提取长程运动轨迹，通过基于最优传输（Sinkhorn-Knopp）的聚类机制在时间维度上传播聚类分配，从而在视频数据上学习空间-时间一致的稠密表征，仅用视频训练即可将 DINOv2 在多个图像/视频基准上提升 1%–6%。

**[Scaling Language-Free Visual Representation Learning](scaling_languagefree_visual_representation_learning.md)**

:   通过在MetaCLIP的20亿web图像上训练DINOv2/MAE系列模型（1B-7B参数），系统性地证明纯视觉自监督学习在模型和数据规模上展现优于CLIP的scaling behavior，5B+参数时在VQA平均性能上超越CLIP——包括传统认为需要语言监督的OCR/Chart任务。

**[SVIP: Semantically Contextualized Visual Patches for Zero-Shot Learning](svip_semantically_contextualized_visual_patches_for_zero-shot_learning.md)**

:   提出SVIP框架，通过在**输入阶段**识别并替换语义无关的图像patch（用属性级word embedding初始化的可学习嵌入替代），从根源上解决零样本学习中的语义错位问题。
