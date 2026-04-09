<!-- 由 src/gen_blog_index.py 自动生成 -->
# ✂️ 语义分割

**🧪 ICML2025** · 共 **9** 篇

**[Alberta Wells Dataset: Pinpointing Oil and Gas Wells from Satellite Imagery](alberta_wells_dataset_pinpointing_oil_and_gas_wells_from_satellite_imagery.md)**

:   提出首个大规模油气井检测基准数据集 Alberta Wells Dataset（213k+ 井位、188k+ 卫星图像 patch），将废弃/暂停/活跃油气井的定位问题建模为二值分割和目标检测任务，并评估了多种 CNN 和 Transformer 基线模型。

**[Balanced Learning for Domain Adaptive Semantic Segmentation](balanced_learning_for_domain_adaptive_semantic_segmentation.md)**

:   提出 BLDA——通过分析网络预测 logit 的分布来评估和缓解域自适应语义分割中的类别偏差，用共享锚点分布对齐各类 logit 分布，并在自训练中在线校正 logit 生成无偏伪标签。

**[ConText: Driving In-context Learning for Text Removal and Segmentation](context_driving_in-context_learning_for_text_removal_and_segmentation.md)**

:   首次将视觉上下文学习（V-ICL）范式应用于OCR任务，提出任务链式提示（task-chaining prompting）、上下文感知聚合（CAA）和自提示策略（self-prompting）三项关键设计，在文本去除和分割任务上大幅超越现有V-ICL通用模型和专用模型，分别取得 +4.50 PSNR 和 +3.34% fgIoU 的提升。

**[FeatSharp: Your Vision Model Features, Sharper](featsharp_your_vision_model_features_sharper.md)**

:   提出 FeatSharp，通过将 FeatUp 的联合双边上采样（JBU）与图像瓦片（tiling）特征进行注意力融合，以极低成本将低分辨率视觉编码器的特征图连贯地上采样到高分辨率，同时捕获原始分辨率下丢失的细粒度细节。

**[InfoSAM: Fine-Tuning the Segment Anything Model from An Information-Theoretic Perspective](infosam_fine-tuning_the_segment_anything_model_from_an_information-theoretic_per.md)**

:   提出 InfoSAM，从信息论角度为 SAM 的参数高效微调（PEFT）设计了基于 Rényi 互信息的关系压缩与蒸馏框架，通过压缩伪不变信息、保留域不变关系来提升微调效果。

**[QMamba: On First Exploration of Vision Mamba for Image Quality Assessment](qmamba_on_first_exploration_of_vision_mamba_for_image_quality_assessment.md)**

:   首次将 Vision Mamba（状态空间模型）引入图像质量评估（IQA），提出 QMamba 框架和 StylePrompt 轻量微调策略，在合成/真实/AIGC 多种 IQA 任务上以更低计算成本超越 CNN 和 Transformer 基线。

**[Separating Knowledge and Perception with Procedural Data](separating_knowledge_and_perception_with_procedural_data.md)**

:   仅用程序化生成数据（非真实图像）训练视觉表征模型，再通过 visual memory（KNN 检索数据库）注入真实世界知识，在分类和分割任务上逼近真实数据训练的性能，同时实现对所有真实数据的完全可控（隐私保护、高效遗忘）。

**[SpikeVideoFormer: An Efficient Spike-Driven Video Transformer with Hamming Attention and $\mathcal{O}(T)$ Complexity](spikevideoformer_an_efficient_spike-driven_video_transformer_with_hamming_attent.md)**

:   提出 SpikeVideoFormer，首个面向视频任务的脉冲驱动 Transformer，通过 Hamming 注意力替代点积注意力实现 spike 特征相似性的准确度量，结合联合时空注意力保持 $\mathcal{O}(T)$ 线性时间复杂度，在三个视频任务上达到 SNN SOTA，同时效率比 ANN 高 5-16 倍。

**[unMORE: Unsupervised Multi-Object Segmentation via Center-Boundary Reasoning](unmore_unsupervised_multi-object_segmentation_via_center-boundary_reasoning.md)**

:   提出 unMORE，通过学习三层物体中心表征（存在性/中心场/边界距离场）并设计无网络的多目标推理模块，实现无监督多目标分割，在 COCO 等 6 个数据集上大幅超越所有无监督方法。
